---
title: Introduction to Git and Github
videoId: HkdAHXoRtos
---

From: [[fireship]] <br/> 

## The Importance of Git

While many development tools have a limited shelf life, Git remains a consistent and revolutionary force in the software world <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It functions as a history book for your code, and services like GitHub make [[contributing_to_open_source_projects_on_github | open source software]] widely accessible <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is Git?

Git is primarily a [[version_control_basics_with_git | version control system]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. At its core, it's a system for managing files <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Software development involves reaching small milestones, which often means writing code in various files <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Git allows you to track all these changes as your application transitions between states of chaos and stability <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Git supports the creation of multiple [[Branching and Merging Strategies in Git | branches]] or paths, which can later be merged, facilitating collaboration among large groups of developers <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

> [!info] Example Project
> This guide uses an example of building an [[contributing_to_open_source_projects_on_github | open source]] Node.js command-line utility. This utility encrypts a mailing address and adds it to a GitHub repository to allow users to receive stickers <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Initializing a Git Repository

Before Git can track files, you need to initialize a repository <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done either directly in [[Using VS Code with Git | VS Code]] or from the command line <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. While memorizing commands is beneficial, [[Using VS Code with Git | VS Code]]'s integrated tooling can often speed up the process <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### `git init` Command

To initialize a Git repository from the command line, run:
```bash
git init
```
This command initializes an empty Git repository in your current working directory <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. After initialization, files in the directory will appear in the source control panel as "changes" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. For a new project, files will typically have a 'U' icon, indicating they are "untracked" or newly created <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Pro Tip: Uninitializing Git
When you initialize a Git repository, a hidden `.git` directory is created <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To completely uninitialize Git or remove it from your project, you can delete this directory, but exercise caution <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Pro Tip: GitLens Plugin for [[Using VS Code with Git | VS Code]]
Consider installing the GitLens plugin for [[Using VS Code with Git | VS Code]]. It embeds useful information directly into your code and provides a panel for navigating your Git history <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Ignoring Files with `.gitignore`

It's crucial to create a `.gitignore` file when setting up a Git repository <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. You should not include everything in source control, especially sensitive private API keys, source code for dependencies (like `node_modules`), or unnecessary log files <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Git will automatically filter out anything matching the patterns specified in this file <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. While you can create it manually, a [[Using VS Code with Git | VS Code]] plugin can automatically generate defaults for your environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Committing Changes

A "commit" is like a page in a history book, with its own unique ID, that cannot be changed without Git detecting it <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Staging Files (`git add`)
Before committing, you need to "stage" the files you want to include in the commit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Use `git add` to stage individual files or the entire working directory (using a period: `git add .`) <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. [[Using VS Code with Git | VS Code]] allows easy staging or un-staging by clicking plus or minus buttons <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

To un-stage files from the command line, use `git reset` <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Be cautious with the `--hard` flag, as it can not only un-stage but also permanently delete files <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Pro Tip: Make Many Small Commits
This practice helps prevent catastrophic code loss and makes changes easier to follow <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Creating a Commit (`git commit`)
After staging your files with `git add`, create a commit using `git commit` with the `-m` flag to add a descriptive message <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>:
```bash
git commit -m "Your descriptive message here"
```
You can also make multi-line commit messages, with a summary on the first line and more detailed changes on subsequent lines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Committing moves files out of staged changes, resulting in a clean working directory, and shows which files were created, modified, or deleted <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## [[Branching and Merging Strategies in Git | Branching and Merging]]

### What is a Branch?
The "master" branch (often now renamed to `main`) is considered the main trunk, containing the source code that is released to customers <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. When you need to fix a bug or experiment with a new feature, you typically create a new [[Branching and Merging Strategies in Git | branch]] based on your most recent commit <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This allows multiple developers to work on the same codebase simultaneously without interfering with each other <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Managing Branches
*   **List Branches**: Run `git branch` to see all current branches <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Switch Branches**: Use `git checkout [branch_name]` to switch between existing branches <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Create and Switch to a New Branch**: Use `git checkout -b [new_branch_name]` <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Any code written while on this new [[Branching and Merging Strategies in Git | branch]] will be isolated to it <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### [[Branching and Merging Strategies in Git | Merging]] Branches (`git merge`)
Once a feature is complete, you will [[Branching and Merging Strategies in Git | merge]] that [[Branching and Merging Strategies in Git | branch]] into the master [[Branching and Merging Strategies in Git | branch]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
1.  Check out the master [[Branching and Merging Strategies in Git | branch]]: `git checkout master` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
2.  [[Branching and Merging Strategies in Git | Merge]] the feature [[Branching and Merging Strategies in Git | branch]]: `git merge [feature_branch_name]` <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This brings the latest commits from the feature [[Branching and Merging Strategies in Git | branch]] into the master <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### Merge Conflicts
[[Branching and Merging Strategies in Git | Merging]] is a common point for issues, especially when changes on different [[Branching and Merging Strategies in Git | branches]] affect the same lines of code, leading to "merge conflicts" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. [[Using VS Code with Git | VS Code]] offers options to resolve these, such as accepting the current change, the incoming change, or both <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Often, it's best to abort the [[Branching and Merging Strategies in Git | merge]] and fix the files manually <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Small commits make resolving conflicts easier <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

When working on a feature, you'll often want to [[Branching and Merging Strategies in Git | merge]] the master [[Branching and Merging Strategies in Git | branch]] back into your feature [[Branching and Merging Strategies in Git | branch]] to get the latest code and anticipate breaking changes <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This is particularly important for long-running features <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Pro Tip: Squashing Commits (`--squash`)
On a feature [[Branching and Merging Strategies in Git | branch]], you might create many small, possibly irrelevant, commits <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Instead of [[Branching and Merging Strategies in Git | merging]] all of them into the master [[Branching and Merging Strategies in Git | branch]], you can use the `--squash` flag during a [[Branching and Merging Strategies in Git | merge]] to combine them into a single commit <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This keeps the change history on the master [[Branching and Merging Strategies in Git | branch]] concise while preserving original commits on the feature [[Branching and Merging Strategies in Git | branch]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. When squashing, you'll need to manually add an additional commit on your own to reflect the squashed changes <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Git Stash

If you're working on something half-finished or experimental and need to switch [[Branching and Merging Strategies in Git | branches]] without committing, `git stash` is useful <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This command saves your current changes without committing them and reverts your working directory to a clean state <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Later, you can retrieve these changes using `git stash pop` (removes stash after applying) or `git stash apply` (keeps stash) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Working with GitHub

### Pushing a Repository to GitHub
To push a local repository to GitHub:
1.  Create a repository on GitHub <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
2.  Use `git remote add origin [repository_url]` to connect your local code to the remote repository <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
3.  Use `git push origin [branch_name]` (e.g., `git push origin master`) to push the files to the remote repository <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### [[Contributing to Open Source Projects on Github | Contributing to Open Source Projects]] (Fork, Clone, Pull Request)
This is a typical pattern for [[contributing_to_open_source_projects_on_github | open source projects]] <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>:

1.  **Fork the existing project**: This copies the code from the source to a repository under your own GitHub account <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Clone your fork**: Use `git clone [your_fork_url]` to copy the code from your remote fork to your local machine <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
3.  **Make changes**:
    *   Open the cloned repository in [[Using VS Code with Git | VS Code]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Install dependencies (e.g., `npm install`) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   Create a new [[Branching and Merging Strategies in Git | branch]] for your changes: `git checkout -b [your_branch_name]` <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Implement your changes (e.g., running `npm run address` to generate an encrypted mailing address, then creating a file with your GitHub username and pasting the encrypted string into it) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

    > [!caution] Security Note on Public Data
    > When adding information like a mailing address to a public repository, even if encrypted (e.g., with RSA algorithm), be aware that it's in a public format. While encryption with a private key (held by the recipient) makes decryption by others extremely difficult, physical theft of the private key remains a theoretical risk <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

4.  **Commit and Push your [[Branching and Merging Strategies in Git | branch]]**:
    *   Stage your changes: `git add .` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   Commit your changes: `git commit -m "Your commit message"` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
    *   Push your [[Branching and Merging Strategies in Git | branch]] to your remote fork: `git push origin [your_branch_name]` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

5.  **Create a Pull Request**: On GitHub, you'll see an option to create a new pull request <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. A pull request is similar to a [[Branching and Merging Strategies in Git | merge]], but it involves "pulling" remote changes from your fork into the original project's master [[Branching and Merging Strategies in Git | branch]] <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.