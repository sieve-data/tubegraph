---
title: Branching and Merging Strategies in Git
videoId: HkdAHXoRtos
---

From: [[fireship]] <br/> 

While many development tools have a limited lifespan, Git remains consistent and has revolutionized the software world <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It functions as a history book for your code, and services like GitHub make open-source software widely accessible <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is Git?
Git is a [[version_control_basics_with_git | version control system]] designed for managing files and tracking changes in software development <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Software development involves a series of small milestones, primarily writing code across many files <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Git allows you to track these changes, offering the ability to create multiple "branches" or paths, which can later be merged to facilitate collaboration among developers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Initializing a Git Repository
To begin tracking files, you must first initialize Git <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done either directly in VS Code or via the command line <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

To initialize from the command line, run `git init` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This creates an empty Git repository in your current working directory and adds existing files to the "changes list" in the source control panel <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Files with a 'u' icon are "untracked," meaning they are newly created in the working directory <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

> [!PRO TIP]
> Initializing a Git repository creates a hidden `.git` directory <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To completely uninitialize Git or remove it from a project, you can delete this directory <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Ignoring Files with `.gitignore`
It's crucial to create a `.gitignore` file when setting up a Git repository <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This file prevents sensitive data (like API keys), dependency source code (e.g., `node_modules`), and unnecessary log files from being included in [[tracking_configuration_changes_with_a_git_repository | source control]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Git automatically filters out anything matching paths or patterns in this file <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. While you can create it manually, a VS Code plugin can automatically generate default `.gitignore` settings for your environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Committing Changes
A commit is like a page in a history book, possessing a unique ID and being unchangeable without Git's awareness <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

1.  **Stage Files**: Before committing, you must "stage" the files you want to include <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   Use `git add` to stage files; you can add individual files or the entire directory using a period (`.`) <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   [[using_vs_code_with_git | VS Code]] allows staging or unstaging files by clicking plus or minus buttons <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   To unstage from the command line, use `git reset` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Be cautious with the `--hard` flag, as it will delete unstaged files forever <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

2.  **Create a Commit**: After staging, run `git commit` with the `-m` flag to add a descriptive message <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Commits can be multi-line: a summary on the first line, followed by more descriptive changes on subsequent lines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   After committing, files are removed from "staged changes," resulting in a clean working directory <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

> [!PRO TIP]
> Make many small commits <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This practice helps prevent catastrophic code losses and makes changes easier to follow <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

> [!TOOL]
> The `git lens` plugin for VS Code embeds useful information directly in your code and provides a panel for navigating your Git history <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Branching in Git
The `master` branch is typically the main trunk of a project, containing the stable source code released to customers <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. When fixing bugs or experimenting with new features, you typically create a new branch based on your most recent commit <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This allows multiple developers to work on the same codebase independently without conflicts <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

*   **List Branches**: Use `git branch` to see all current branches <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Create and Switch Branches**: Use `git checkout -b <branch_name>` to create a new branch and immediately switch to it <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Managing Work in Progress with `git stash`
If you're working on something half-finished or experimental and need to switch branches without committing, you can use `git stash` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This command saves all current changes without committing them and reverts your working directory to a clean state <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Later, you can retrieve these changes using `git stash pop` or `git stash apply` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Merging Branches
Once a feature or bug fix on a separate branch is complete, you'll want to merge it back into the `master` branch <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

1.  **Switch to Target Branch**: First, check out the `master` branch: `git checkout master` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
2.  **Merge**: Then, run `git merge <feature_branch_name>` to integrate the latest commits from your feature branch into `master` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Merge Conflicts
Merging can lead to problems, especially if changes occurred on the `master` branch while you were working on a feature branch, affecting the same lines of code <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. When a merge conflict occurs, Git doesn't know which change to use <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

[[using_vs_code_with_git | VS Code]] offers options to resolve conflicts, such as accepting current changes, incoming changes, or both <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It's often best to review conflicts, then abort the merge (`git merge --abort`) and fix the files manually <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Small commits make conflicts easier to resolve <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

> [!TIP]
> If you're working on a feature for an extended period, it's good practice to frequently merge the `master` branch back into your feature branch (e.g., daily) to incorporate the latest code and identify potential breaking changes or conflicts early <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Squashing Commits
On a feature branch, you might create many commits that are less relevant to the `master` branch's history <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. To maintain a concise change history on `master` while preserving original commits on the feature branch, you can use the `--squash` flag during a merge <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

`git merge --squash <feature_branch_name>`

When merging with `--squash`, it won't automatically update the `master` branch's head commit <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. You'll need to create an additional commit yourself, for example, with a message like "Merged in feature branch," to finalize the squash and maintain a compact history <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## Remote Operations with GitHub
Beyond local operations, Git integrates seamlessly with remote services like GitHub.

### Pushing to GitHub
To push a local repository to GitHub:
1.  Create a repository on GitHub <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
2.  Connect your local code to the remote repository using `git remote add origin <remote_url>` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  Push the files using `git push -u origin master` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Contributing via Forking and Pull Requests
[[contributing_to_open_source_projects_on_github | Contributing to an open-source project]] typically follows these steps:
1.  **Fork the Project**: This copies the code from the source to a new repository under your own GitHub account <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Clone Your Fork**: Copy your forked repository to your local machine using `git clone <your_fork_url>` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
3.  **Make Changes**: Work on the code locally. This includes installing dependencies (e.g., `npm install`) and creating a new branch for your changes (e.g., `git checkout -b my-sticker`) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   *Example*: A specific command `npm run address` might be used to prompt for information, printing an encrypted string to be added to a new file (e.g., `github_username.txt`) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This specific example used RSA encryption to keep sensitive information (like an address for a sticker giveaway) private, as only the holder of the private key can decrypt the data <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
4.  **Commit and Push Changes**: After making changes, stage and commit them locally (`git add`, `git commit`) <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Then push your local branch to your remote fork: `git push origin <branch_name>` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
5.  **Create a Pull Request**: On GitHub, you'll see an option to create a new pull request <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. A pull request is similar to a merge, but it includes the additional step of needing to "pull" the remote changes, essentially requesting that your changes be merged into the original project's master branch <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.