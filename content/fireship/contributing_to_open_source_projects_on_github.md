---
title: Contributing to Open Source Projects on Github
videoId: HkdAHXoRtos
---

From: [[fireship]] <br/> 

While many development tools have a limited lifespan, [[Version Control Basics with Git | Git]] remains a consistent and revolutionary force in the software world <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It serves as a history book for your code, and services like GitHub make open-source software accessible globally <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This guide covers the basics of [[Version Control Basics with Git | Git]] and how to contribute to open-source projects on GitHub.

## What is Git?
[[Version Control Basics with Git | Git]] is a [[Version Control Basics with Git | version control system]] that manages files <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Software development involves a series of small milestones, primarily writing code in various files <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. [[Version Control Basics with Git | Git]] helps track these continuous changes, allowing for the creation of multiple [[Branching and Merging Strategies in Git | branches]] or paths that can later be merged, facilitating collaboration among developers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Setting Up a Local Git Repository
To begin tracking files with [[Version Control Basics with Git | Git]], you first need to initialize a repository <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done either directly in [[Using VS Code with Git | VS Code]] or from the command line <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

To initialize [[Version Control Basics with Git | Git]] from the command line:
`git init` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
This command initializes an empty [[Version Control Basics with Git | Git]] repository in your current working directory <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. When files are added to a new project, they will appear in the source control panel with a "u" icon, indicating they are untracked <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

> [!PRO TIP] Initializing and De-initializing a Git Repo
> When you initialize a [[Version Control Basics with Git | Git]] repository, it creates a hidden `.git` directory <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To completely de-initialize or remove [[Version Control Basics with Git | Git]] from your project, you can simply remove this directory (but be careful!) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

> [!PRO TIP] Enhance VS Code with GitLens
> Install the GitLens plugin for [[Using VS Code with Git | VS Code]] to embed useful information directly in your code and easily navigate your [[Version Control Basics with Git | Git]] history <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Ignoring Files with `.gitignore`
It's important to control which files are included in [[Version Control Basics with Git | source control]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. You should exclude sensitive private API keys, source code for dependencies (like `node_modules`), and unnecessary log files <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. [[Version Control Basics with Git | Git]] uses a `.gitignore` file to filter out anything that matches a specified file path or pattern <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. You can create this file manually or use a [[Using VS Code with Git | VS Code]] plugin to automatically generate default settings for your environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Committing Changes
A "commit" is like a page in a history book, with its own unique ID, and cannot be changed without [[Version Control Basics with Git | Git]] knowing about it <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

1.  **Stage Files**: Before committing, you must "stage" the files you want to include in the commit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   To stage files from the command line: `git add <file>` or `git add .` to stage the entire working directory <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   In [[Using VS Code with Git | VS Code]], you can stage or unstage files by clicking the plus or minus button <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   To unstage files from the command line: `git reset <file>` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
        > [!WARNING] Be careful with `git reset --hard`!
        > Using the `--hard` flag with `git reset` will not only unstage files but also delete them permanently <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. On a new project, this command would delete everything <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

2.  **Commit Staged Files**:
    *   Run `git commit -m "Your descriptive message"` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Commit messages can be multi-line, with a summary on the first line and a more descriptive set of changes on the second <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

> [!PRO TIP] Make Many Small Commits
> This practice helps prevent catastrophic code loss and makes code changes easier to follow <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

> [!PRO TIP] Use Emojis in Commit Messages
> Emojis can potentially help you get more GitHub stars on your project <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Branching and Merging
The "master" branch is typically the main trunk of a project, containing the source code that is released to customers <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. When fixing a bug or experimenting with a new feature, it's common to create a new branch based on your most recent commit <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This allows multiple developers to work on the same codebase without interfering with each other <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

*   **View Branches**: `git branch` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>
*   **Switch Branches**: `git checkout <branch_name>` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
*   **Create and Switch to a New Branch**: `git checkout -b <new_branch_name>` <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>

#### Stashing Work
When you have half-finished or experimental work that you're not ready to commit, you can use `git stash` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
> `git stash` saves all your current changes without committing them and reverts your working directory to a clean state <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Later, you can use `git stash pop` or `git stash apply` to reapply these changes to your current working directory <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

#### Merging Branches
Once a feature or bug fix is ready, you merge it back into the master branch <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
1.  Switch to the target branch (e.g., master): `git checkout master` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
2.  Merge the feature branch: `git merge <feature_branch_name>` <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>

#### Merge Conflicts
Conflicts occur when the same line of code is changed in different [[Branching and Merging Strategies in Git | branches]] that are being merged <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. [[Using VS Code with Git | VS Code]] provides options to resolve these conflicts, such as accepting current changes, incoming changes, or both <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Often, it's best to abort the merge and fix files manually <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.> [!TIP] Frequent Merging from Master
> If you're working on a feature branch for an extended period, it's advisable to merge the master branch into your feature branch whenever it changes (or daily for active repositories) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This helps you get the latest code and identify breaking changes early <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

> [!PRO TIP] Squash Commits on Merge
> When merging a feature branch with many small, irrelevant commits into the master branch, use the `squash` flag <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This squashes them into a single commit, keeping the change history on master concise while preserving original commits on the feature branch <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. After squashing, you'll need to add an additional commit on your own, e.g., "Merged in feature branch" <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## Working with GitHub (Remote)
Once you've mastered local [[Version Control Basics with Git | Git]] operations, you can interact with remote repositories on GitHub.

### Pushing a Local Repository to GitHub
1.  Create a new repository on GitHub <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
2.  Connect your local code to this remote repository: `git remote add origin <repository_url>` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
3.  Push your files to the remote repository: `git push -u origin master` (or `main`) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>

### Contributing to an Existing Open-Source Project
The typical pattern for contributing to any open-source project involves these steps <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>:

1.  **Fork the Project**: "Forking" copies the code from the source repository to a new repository under your own GitHub account <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Clone Your Fork**: Copy your forked repository to your local machine using the `git clone` command <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    `git clone <your_fork_url>` <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>
3.  **Make Changes**:
    *   Open the cloned project in [[Using VS Code with Git | VS Code]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Install project dependencies (e.g., `npm install`) <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   Create and switch to a new branch for your changes: `git checkout -b <your_feature_branch_name>` <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Implement your desired changes.
    *   *Example: Encrypting a mailing address for a sticker giveaway* <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>
        *   Run `npm run address` (if applicable) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
        *   Create a file (e.g., `stickers/<your_github_username>.txt`) and paste the encrypted string into it <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

    > [!NOTE] Security of Encrypted Address
    > Although your address goes into a public repository, it's encrypted with the RSA algorithm <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Data can be encrypted with a public key, but only the holder of the private key can decrypt it <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Brute-forcing the private key is essentially impossible <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

4.  **Commit and Push Changes**:
    *   Stage your changes: `git add .` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>
    *   Commit your changes: `git commit -m "Your descriptive commit message"` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>
    *   Push your branch to your remote fork: `git push origin <your_feature_branch_name>` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>

5.  **Create a Pull Request**: On GitHub, you'll see an option to create a new "pull request" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. A pull request is similar to a merge, but it involves the additional step of requesting that the project maintainers "pull" your remote changes and merge them into their master branch <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

This process provides the basic tools needed to contribute to open-source software <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.