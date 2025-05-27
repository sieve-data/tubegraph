from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()
"""
Utility to commit files to a GitHub repository using the git CLI.

Requirements
------------
* `git` installed and on $PATH.
* `GITHUB_TOKEN` env‑var set with a PAT that has **push** permission to
  the target repo.
* The caller runs this from any directory – the repository is cloned
  into a temporary directory on every call, so concurrent invocations
  are isolated and safe.
"""


GITHUB_REPO = "sieve-data/tubegraph"  # "<owner>/<repo>"


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def _run(cmd: List[str] | tuple[str, ...], cwd: Path) -> str:
    """Run *cmd* inside *cwd* and return *stdout* (raise on error)."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(cmd)} failed (exit {result.returncode}):\n"
            f"{result.stdout}\n{result.stderr}"
        )
    return result.stdout.strip()


def _clone_repo(tmpdir: Path, token: str) -> Path:
    """Clone *GITHUB_REPO* into *tmpdir* and return the repo path."""
    owner_repo = GITHUB_REPO
    # Embed PAT in the HTTPS URL for non‑interactive auth
    repo_url = f"https://{token}@github.com/{owner_repo}.git"
    repo_path = tmpdir / "repo"
    _run(["git", "clone", "--depth", "1", repo_url, str(repo_path)], cwd=tmpdir)
    return repo_path


def _copy_files(file_paths: List[str], username: str, repo_path: Path) -> List[Path]:
    """Copy *file_paths* into *content/<username>/* inside *repo_path*.

    Returns the list of *repo‑relative* destination paths (Path objects).
    """
    dest_dir = repo_path / "content" / username
    dest_dir.mkdir(parents=True, exist_ok=True)

    rel_paths: list[Path] = []
    for src in file_paths:
        src_path = Path(src)
        if not src_path.is_file():
            raise FileNotFoundError(src)

        dest_path = dest_dir / src_path.name
        shutil.copy2(src_path, dest_path)
        rel_paths.append(dest_path.relative_to(repo_path))

    return rel_paths


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def commit_files_to_main(file_paths: List[str], username: str) -> str:
    """Upload *file_paths* into *content/<username>/* and push one commit.

    Each invocation works in its own clone, avoiding lock/contention issues
    when multiple processes run concurrently. If *git push* fails due to a
    fast‑forward error the function raises – the caller can simply retry.
    """
    if not file_paths:
        raise ValueError("file_paths cannot be empty")

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN env‑var missing; cannot push to GitHub.")

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        repo_path = _clone_repo(tmpdir, token)

        # Configure Git user identity for this repository
        _run(["git", "config", "user.email", "pandaaditya48@gmail.com"], cwd=repo_path)
        _run(["git", "config", "user.name", "adi-panda"], cwd=repo_path)

        added_rel_paths = _copy_files(file_paths, username, repo_path)

        # Stage & commit -----------------------------------------------------
        _run(["git", "add", *map(str, added_rel_paths)], cwd=repo_path)
        plural = "" if len(added_rel_paths) == 1 else "s"
        commit_msg = (
            f"Add/Update {len(added_rel_paths)} TubeGraph post{plural} for {username}"
        )
        _run(["git", "commit", "-m", commit_msg], cwd=repo_path)

        # Re‑sync & push -----------------------------------------------------
        _run(["git", "pull", "--rebase", "origin", "main"], cwd=repo_path)
        _run(["git", "push", "origin", "HEAD:main"], cwd=repo_path)

    changed_files = "\n".join(f" • {p}" for p in added_rel_paths)
    plural = "" if len(added_rel_paths) == 1 else "s"
    return (
        f"Committed {len(added_rel_paths)} file{plural} in one commit:\n{changed_files}"
    )


# commit_files_to_main(["test3.md", "test4.md"], "test_dir_2")
