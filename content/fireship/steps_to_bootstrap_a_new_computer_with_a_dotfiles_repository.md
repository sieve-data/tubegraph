---
title: Steps to bootstrap a new computer with a dotfiles repository
videoId: r_MpUP6aKiQ
---

From: [[fireship]] <br/> 

[[using_dotfiles_to_automate_development_environment_setup | Dotfiles]] are text-based configuration files that help set up or restore a fully customized development environment by maintaining a repository of these files <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This practice aligns with the "Don't Repeat Yourself" (DRY) principle, extending it beyond coding to a developer's environment configuration <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## What Are Dotfiles?

Dotfiles are small, hidden files on your system that typically start with a period (e.g., `.bashprofile.env`, `.git config`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. They can be individual files or even folders <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Mac OS is "littered" with these hidden files <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Visual Studio Code's file explorer can show them <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, and in Finder, they can be revealed by pressing `Command + Shift + Period` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Software, whether pre-installed or custom, uses these files for configuration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Common examples include:
*   `.git config`: Stores [[introduction_to_git_and_github | Git]] user information (like name and email address) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. It can grow with more [[introduction_to_git_and_github | Git]] configurations <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   `.zshrc`: Used to customize the Zsh shell experience, which is the new default shell on Mac OS <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Why Use a Dotfiles Repository?

Maintaining a repository of dotfiles allows you to:
*   Chronicle the installation of your favorite applications and command-line tools <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Keep track of how all your software is configured <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Record all the various system preferences and changes you've made to your computer <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This system lets you replicate your ideal development environment on a new computer in a completely hands-off and automated way, reducing weeks of manual labor to a [[introduction_to_git_and_github | Git]] clone followed by an install script <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It also helps developers build discipline in areas like command-line use, [[introduction_to_git_and_github | Git]], and understanding their machine's inner workings <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Getting Started: Organizing Your Dotfiles

To begin, organize all your configuration files in a [[introduction_to_git_and_github | Git]] repository <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This allows you to track changes and clone the repository on other machines <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The repository should contain at least one script to apply or install the configurations on a new system <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

When configuring [[introduction_to_git_and_github | Git]] for your dotfiles repository, consider using the "no-reply" email address available with your GitHub account. This keeps your personal email address secret when you publish your dotfiles repo <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Handling Configuration Files with Symbolic Links

A common issue arises when you move configuration files (like `.git config` or `.zshrc`) into your dotfiles repository: the software that relies on them can no longer find them in their expected locations (e.g., the home directory) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This breaks the configuration, as seen when [[introduction_to_git_and_github | Git]] automatically configures committer information instead of using the user's defined settings <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>, or when the custom Zsh prompt disappears because `.zshrc` cannot be found <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

To resolve this, you can use **symbolic links** (symlinks) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. A symlink allows a file to appear as if it's in two places at the same time <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

To create a symlink, use the `ln` command with the `-s` (symbolic link) option <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>:
```bash
ln -s /full/path/to/real/file/in/dotfiles/repo /path/to/original/location
```
For example, to link `.zshrc` back to the home directory:
```bash
ln -s ~/.dotfiles/.zshrc ~/.zshrc
```
This makes the file appear in its original location, allowing software to use it, while the actual file resides and is tracked in your dotfiles repository <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Changes made to the symlinked file are reflected in the real file, and vice-versa <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Managing Software Installations with Homebrew

Beyond configuration files, your dotfiles repository can also manage software installations. For macOS, **Homebrew** is a popular package manager <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

Homebrew can keep track of what it has installed <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. You can generate a `Brewfile` that lists all your installed software using:
```bash
brew bundle dump --describe
```
This command creates a `Brewfile` in your current directory, which should be your dotfiles repository <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. The `Brewfile` lists:
*   **Taps**: Repositories where Homebrew keeps its software and information <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Brews**: Command-line tools typically used in your shell <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Casks**: Full-blown applications that you recognize <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

This `Brewfile` can then be tracked in your [[introduction_to_git_and_github | Git]] repository <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

## Bootstrapping a New Computer

When setting up a new machine, you'll use your dotfiles repository to automate the process. A typical bootstrapping process, outlined in a `README` within your repository, would look like this:

### 1. Install Command-Line Tools
Before using [[introduction_to_git_and_github | Git]] and Homebrew, you'll need to install the essential command-line tools for your operating system <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

### 2. Clone Your Dotfiles Repository
Clone your dotfiles repository to the new machine <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. SSH is preferred, but you might start with HTTPS and switch remotes after setting up SSH <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
```bash
git clone git@github.com:your_username/dotfiles.git ~/.dotfiles
```

### 3. Create Symbolic Links
Once your configuration files are on the machine, you need to create the symlinks back to their original locations <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
```bash
ln -s ~/.dotfiles/.zshrc ~/.zshrc
ln -s ~/.dotfiles/.gitconfig ~/.gitconfig
# ... and so on for all your configuration files
```
Manually creating symlinks can become cumbersome with many files <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, so it's advisable to eventually incorporate this step into an install script <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### 4. Install Homebrew and Software
Finally, install Homebrew (if not already installed) and then point it to your `Brewfile` to reinstall all your desired software <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew bundle --file=~/.dotfiles/Brewfile
```
This automated software installation process is highly satisfying <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Next Steps and Improvements

This is a foundational approach. Further improvements to your [[using_dotfiles_to_automate_development_environment_setup | dotfiles]] process could include:
*   Saving system preferences <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   Organizing your repository into separate files for better modularity <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   Building a comprehensive install script to automate all manual steps <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

Automating your computer setup with [[using_dotfiles_to_automate_development_environment_setup | dotfiles]] significantly boosts developer productivity <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.