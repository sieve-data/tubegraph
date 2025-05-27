import os
from typing import List

from dotenv import load_dotenv
from github import Github, GithubException, InputGitTreeElement

load_dotenv()


def _get_repo():
    """Authenticate and return the PyGitHub Repository object."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN env-var missing; cannot push to GitHub.")
    gh = Github(token)
    try:
        return gh.get_repo(GITHUB_REPO)
    except GithubException as exc:
        raise RuntimeError(f"Cannot access repo {GITHUB_REPO}: {exc}") from exc


# Constants for the target repository
GITHUB_REPO = "sieve-data/tubegraph"


def commit_files_to_main(file_paths: List[str], username: str) -> str:
    """
    Upload *all* `file_paths` to content/<username>/ in a **single** commit
    on the repository's default branch.

    Returns a human-readable summary.
    """
    repo = _get_repo()
    branch_name = repo.default_branch  # e.g. "main"

    # --- 1. Gather parent commit / tree for the branch head ------------------
    head_commit = repo.get_branch(branch_name).commit  # github.Commit
    base_tree = repo.get_git_tree(head_commit.sha)  # github.GitTree

    # --- 2. Create a blob + tree element for every file ----------------------
    tree_elements = []
    for abs_path in file_paths:
        with open(abs_path, "rb") as fh:
            content_str = fh.read().decode()  # GitHub expects str

        # New blob that holds the file contents
        blob = repo.create_git_blob(content_str, encoding="utf-8")

        rel_name = os.path.basename(abs_path)
        dest_path = f"content/{username}/{rel_name}"  # repo-relative path

        tree_elements.append(
            InputGitTreeElement(
                path=dest_path,
                mode="100644",  # normal file
                type="blob",
                sha=blob.sha,
            )
        )

    # --- 3. Create a new tree that overlays these blobs on the branch tree ---
    new_tree = repo.create_git_tree(tree=tree_elements, base_tree=base_tree)

    # --- 4. Commit the tree ---------------------------------------------------
    commit_msg = (
        f"Add/Update {len(file_paths)} TubeGraph post"
        f"{'' if len(file_paths) == 1 else 's'} for {username}"
    )

    # FIX: get the GitCommit object for the parent
    parent_git_commit = repo.get_git_commit(head_commit.sha)

    new_commit = repo.create_git_commit(
        message=commit_msg,
        tree=new_tree,
        parents=[parent_git_commit],
    )

    # --- 5. Move the branch ref to the new commit ----------------------------
    repo.get_git_ref(f"heads/{branch_name}").edit(new_commit.sha)

    # --- 6. Return a summary --------------------------------------------------
    changed_files = "\n".join(f" • {el.path}" for el in tree_elements)
    return f"Committed {len(tree_elements)} file(s) in one commit:\n{changed_files}"


commit_files_to_main(["test.md", "test_2.md"], "test_dir")
