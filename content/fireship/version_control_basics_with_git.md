---
title: Version Control Basics with Git
videoId: HkdAHXoRtos
---

From: [[fireship]] <br/> 

[[Introduction to Git and Github | Git]] is a version control system that has revolutionized the software world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It acts as a history book for your code <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, and services like [[Contributing to Open Source Projects on Github | GitHub]] make open-source software accessible globally <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. At its core, Git helps manage files by tracking changes and enabling collaboration <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## What is Git?
Git is a [[Version control and remote development in VS Code | version control system]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It allows you to keep track of all changes as your application constantly moves between states of chaos and stability <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Git facilitates collaboration by enabling developers to create multiple branches or paths of development and later merge them <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Initializing a Git Repository
To start tracking files with Git, you first need to initialize a repository <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done directly in [[Using VS Code with Git | VS Code]] or from the command line <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

To initialize from the command line, run:
```bash
git init
```
This command initializes an empty Git repository in your current working directory <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. After initialization, Git will add your files to the "changes" list in the source control panel, showing which files have changed since the last snapshot <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Newly created files will appear with a "U" icon, meaning "untracked" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

> [!PRO TIP] Initializing a Git repository creates a hidden `.git` directory <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To completely uninitialize Git from a project, you can remove this directory <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

> [!PRO TIP] Consider installing the GitLens plugin for VS Code. It embeds useful Git information directly into your code and provides an extra panel for navigating Git history <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The `.gitignore` File
It's crucial to create a `.gitignore` file when setting up a Git repository <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This file tells Git which files or patterns to ignore and not include in source control <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Examples of what to exclude include sensitive private API keys, source code for dependencies (like `node_modules`), and unnecessary log files <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

You can create this file manually or use a VS Code plugin to automatically generate default `.gitignore` entries for your environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Committing Changes (Snapshots)
A commit is like a page in a history book, with its own unique ID, and cannot be changed without Git knowing about it <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Staging Files
Before making a commit, you need to "stage" the files you want to include in that commit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
To stage files from the command line:
```bash
git add [file_name] # Add individual files
git add .           # Add all files in the current directory
```
VS Code makes staging easy with plus (+) and minus (-) buttons <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
To unstage files from the command line:
```bash
git reset [file_name]
```
> [!WARNING] Be careful with `git reset --hard` as it will not only unstage files but also delete them forever <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

> [!PRO TIP] Make many small commits. This practice helps prevent catastrophic code losses and makes changes easier to follow <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Making a Commit
After staging your files, you can commit them:
```bash
git commit -m "Your descriptive commit message"
```
The `-m` flag allows you to add a descriptive message about the changes in your code <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
Commit messages can also be multi-line, with a summary on the first line and more detailed changes below <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
After a commit, your working directory will be clean, and Git will show which files were created, modified, or deleted <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## Branching and Merging
When working on a stable codebase, you often need to fix bugs or experiment with new features without affecting the main code <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This is where [[Branching and Merging Strategies in Git | branches]] come in.

The `master` (or `main`) branch is typically the main trunk of your project, containing the source code delivered to customers <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Creating and Switching Branches
To see your current branches:
```bash
git branch
```
To create a new branch and switch to it:
```bash
git checkout -b [new_branch_name]
```
This command creates a new branch based on your most recent commit and moves you to it, isolating any code you write there <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

To switch between existing branches:
```bash
git checkout [branch_name]
```
When you switch branches, your files will revert to the state of that branch <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### `git stash`
If you're working on something half-finished or experimental and need to switch branches, you can use `git stash` to temporarily save your work-in-progress without committing it <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
```bash
git stash # Saves current changes and reverts to a clean working directory
```
Later, to restore the changes:
```bash
git stash pop # Applies the changes and removes them from the stash list
git stash apply # Applies the changes but keeps them in the stash list
```

### Merging Branches
Once a feature or bug fix is ready on its dedicated branch, you can merge it back into the `master` branch <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
First, switch to the branch you want to merge *into* (e.g., `master`):
```bash
git checkout master
```
Then, merge the other branch (e.g., `feature`):
```bash
git merge feature
```
Merging allows multiple developers to work on the same codebase on their own branches without conflict <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

#### Merge Conflicts
Merge conflicts occur when changes in different branches affect the same lines of code <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Git doesn't know which change to use <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. VS Code provides options to resolve these conflicts, such as accepting the current change, the incoming change, or both <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Sometimes it's best to abort the merge and fix the files manually <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

> [!PRO TIP] If you're working on a feature branch for an extended period, merge the `master` branch back into your feature branch periodically (e.g., daily) to get the latest code and prevent major conflicts <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

#### Squashing Commits
On a feature branch, you might create many small, possibly irrelevant commits <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Instead of merging all of these into `master`, you can use the `--squash` flag during a merge to combine them into a single commit <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
```bash
git merge --squash feature_branch
git commit -m "Merged feature branch" # You'll need to create an additional commit after squashing
```
This keeps the `master` branch's change history concise while preserving the original commits on the feature branch <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Working with Remotes (GitHub)
Git allows you to work with remote repositories, like those hosted on GitHub, for collaboration and sharing <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

### Pushing a Local Repository to GitHub
1.  **Create a Repository on GitHub**: First, create an empty repository on GitHub.
2.  **Connect Local to Remote**: GitHub will provide commands to connect your local code to this remote repository.
    ```bash
    git remote add origin [remote_repository_url] # Connects your local code to the remote
    ```
3.  **Push Files**: Push your local commits to the remote repository.
    ```bash
    git push -u origin master # Pushes the master branch to the remote 'origin'
    ```
After these steps, your code will be visible on GitHub <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Contributing to Open-Source Projects
The typical pattern for [[Contributing to Open Source Projects on Github | contributing to any open-source project]] involves:
1.  **Fork the Project**: Forking copies the code from the source to a repository under your own GitHub account <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Clone Your Fork**: Clone your forked repository to your local machine to begin making changes.
    ```bash
    git clone [your_fork_url]
    ```
    This copies the code from the remote repository to your local computer <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
3.  **Create a Feature Branch**: Create a new branch for your specific changes.
    ```bash
    git checkout -b my-feature-branch
    ```
4.  **Make Changes and Commit**: Implement your desired changes, then stage and commit them to your new branch <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
5.  **Push to Your Remote Fork**: Push your branch with the committed changes to your forked repository on GitHub.
    ```bash
    git push origin my-feature-branch
    ```
6.  **Create a Pull Request**: On GitHub, you'll see an option to create a new pull request <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. A pull request is like a merge, but it includes the additional step of needing to "pull" the remote changes <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. It's essentially saying, "Please pull my remote changes and merge them into the master branch" <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

> [!NOTE] When submitting personal information to a public repository (as described in the video's sticker giveaway), ensure it is encrypted. Using an RSA algorithm means data can be encrypted with a public key but only decrypted by the owner of the private key <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This provides a layer of security, though physical theft of the private key remains a theoretical risk <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.