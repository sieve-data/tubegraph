---
title: Using VS Code with Git
videoId: HkdAHXoRtos
---

From: [[fireship]] <br/> 

[[Version Control Basics with Git|Git]] is a powerful [[version_control_and_remote_development_in_vs_code|version control system]] that has revolutionized the software world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It's essentially a history book of your code <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, allowing you to manage files <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, keep track of changes <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, create multiple branches, and facilitate collaboration among developers <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Services like GitHub make open-source software globally accessible <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Initializing a Git Repository

To begin tracking files with [[Version Control Basics with Git|Git]], you first need to initialize a [[Version Control Basics with Git|Git]] repository <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done directly within [[using_vs_code_with_linux_and_windows|VS Code]] or from the command line <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Command Line Initialization
Run `git init` in your terminal to initialize an empty [[Version Control Basics with Git|Git]] repository in your current working directory <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. After initialization, [[using_vs_code_with_linux_and_windows|VS Code]]'s Source Control panel will list your files under "Changes," indicating which files have changed since the last snapshot <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Newly created files will have a "U" icon, meaning "untracked" <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### The .git Directory
When a [[Version Control Basics with Git|Git]] repository is initialized, a hidden `.git` directory is created <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. If you want to completely uninitialize [[Version Control Basics with Git|Git]] or remove it from your project, you can delete this directory <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Essential Tools and Pro Tips
*   **[[using_extensions_to_enhance_vs_code_functionality|Git Lens Plugin]]**: Install the [[using_extensions_to_enhance_vs_code_functionality|Git Lens]] plugin for [[using_vs_code_with_linux_and_windows|VS Code]]. It embeds useful [[introduction_to_git_and_github|Git]] information directly into your code and provides a panel for navigating your [[Version Control Basics with Git|Git]] history <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **`.gitignore` File**: Create a `.gitignore` file to specify files and directories that [[Version Control Basics with Git|Git]] should ignore, such as sensitive API keys, `node_modules`, or log files <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. [[Version Control Basics with Git|Git]] will automatically filter out anything matching patterns in this file <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. [[using_vs_code_with_linux_and_windows|VS Code]] plugins can automatically generate default `.gitignore` files for your environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Committing Changes (Snapshots)

A commit is like a page in a history book <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, with a unique ID, and cannot be changed without [[Version Control Basics with Git|Git]] detecting it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Staging Files
Before committing, you need to "stage" the files you want to include in the commit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **`git add`**: Use `git add <file>` to stage individual files or `git add .` to stage the entire working directory <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **[[using_vs_code_with_linux_and_windows|VS Code]] Interface**: [[using_vs_code_with_linux_and_windows|VS Code]] allows you to stage or unstage files by clicking the plus (+) or minus (-) buttons <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **`git reset`**: To unstage files from the command line, use `git reset` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Be cautious with the `hard` flag, as it will not only unstage but also permanently delete the files <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Best Practice for Commits
It's a good practice to make many small commits <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This helps prevent catastrophic code loss and makes changes easier to follow <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Performing a Commit
1.  **Stage Files**: First, run `git add` to stage your files <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
2.  **Commit**: Then, run `git commit -m "Your descriptive message"` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **Descriptive Messages**: Use descriptive messages. You can use emojis to potentially gain more GitHub stars <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   **Multi-line Comments**: Comments can be multi-line, providing a summary on the first line and more detailed changes on subsequent lines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    
After a commit, your working directory becomes clean, and [[Version Control Basics with Git|Git]] will show which files were created, modified, or deleted <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The [[using_extensions_to_enhance_vs_code_functionality|Git Lens]] plugin allows you to navigate this history and see exact line changes <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Branches

Branches allow you to work on new features or bug fixes without affecting the stable "master" (or "main") branch <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This facilitates collaboration by allowing multiple developers to work on the same codebase simultaneously <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

*   **View Branches**: Use `git branch` to see all current branches in your codebase <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Switch/Create Branches**: Use `git checkout <branch_name>` to switch between branches <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. To create and switch to a new branch simultaneously, use `git checkout -b <new_branch_name>` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Any code written while on this branch will be isolated to it <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Stashing Changes

`git stash` is a mechanism to save your work in progress without making a formal commit <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. It saves your current changes and reverts your working directory to a clean state <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Later, you can retrieve these changes using `git stash pop` or `git stash apply` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

## Merging Branches

Merging combines changes from one branch into another <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   **Basic Merge**: To merge a feature branch into the master branch, first checkout the master branch, then run `git merge <feature_branch_name>` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Merge Conflicts**: Conflicts occur when the same lines of code are changed in different branches <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. [[using_vs_code_with_linux_and_windows|VS Code]] provides options to resolve these, such as accepting current, incoming, or both changes <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Often, it's best to abort the merge and fix files manually <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Making small commits makes conflict resolution easier <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Merging Master into Feature**: It's common to merge the master branch back into your feature branch periodically to get the latest code and identify potential breaking changes or conflicts early <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Squashing Commits**: When merging a feature branch with many small, irrelevant commits into the master branch, you can use the `--squash` flag with `git merge` <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This combines all feature branch commits into a single commit on the master branch, keeping the change history concise while preserving the original commits on the feature branch <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. You'll need to manually add an additional commit message after squashing <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

## Working with Remote Repositories (GitHub)

[[Introduction to Git and Github|GitHub]] allows for remote collaboration and hosting of [[Version Control Basics with Git|Git]] repositories.

### Pushing a Local Repository to GitHub
1.  **Create Repository**: Create a new repository on [[Introduction to Git and Github|GitHub]] <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
2.  **Connect Remote**: Use `git remote add origin <repository_url>` to connect your local code to the remote repository <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Push Code**: Use `git push -u origin master` (or `main`) to push your files to the remote repository <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Contributing to an Existing Project (Forking and Pull Requests)
This is the typical pattern for contributing to open-source projects <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

1.  **Fork the Project**: Forking copies the code from the source project to a new repository under your own [[Introduction to Git and Github|GitHub]] account <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Clone Your Fork**: Clone your forked repository to your local machine using `git clone <your_fork_url>` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
3.  **Make Changes**: Open the cloned project in [[using_vs_code_with_linux_and_windows|VS Code]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Install dependencies (e.g., `npm install`) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   Create a new branch for your changes (e.g., `git checkout -b my-sticker`) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Implement your changes (e.g., run `npm run address` to encrypt a mailing address, then create a `github_username.txt` file in the `stickers` directory and paste the encrypted string) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
        *   _Security Note_: Encrypted data (like a mailing address) in a public repo uses RSA algorithm, where data is encrypted with a public key but only decryptable with a private key <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
    *   Stage and commit your changes (`git add .` then `git commit -m "Add my sticker address"`) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
4.  **Push to Your Remote Fork**: Push your new branch to your remote fork using `git push origin <branch_name>` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
5.  **Create a Pull Request (PR)**: On [[Introduction to Git and Github|GitHub]], you'll see an option to create a new pull request <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. A pull request is like a merge, but it requires the original repository maintainer to "pull" your remote changes and merge them into their master branch <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.