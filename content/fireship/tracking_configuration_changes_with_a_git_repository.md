---
title: Tracking configuration changes with a git repository
videoId: r_MpUP6aKiQ
---

From: [[fireship]] <br/> 

Dot files enable users to set up or restore a fully customized development environment by maintaining a repository of text-based configuration files <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach adheres to the "Do Not Repeat Yourself" (DRY) principle, which developers are trained to apply to code, but it is equally applicable to configuring a development environment <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Instead of reinstalling and reconfiguring everything from scratch on a new machine, dot files provide an automated solution <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## What are Dot Files?

Dot files are small, hidden files on a system that begin with a period, such as `.bash_profile`, `.env`, or `.gitconfig` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. They can be either files or folders <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Some files might be hidden by the operating system even without a dot prefix <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. These files store configurations for pre-installed software and custom software that users install <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

By maintaining a repository of these files, developers can:
*   Chronicle the installation of favorite applications and command-line tools <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Keep track of how software is configured <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Record system preferences and changes made to the computer <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This allows for the replication of a perfect development environment on a new computer in a completely hands-off and automated way <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Maintaining a dot files repository also fosters discipline in other important skills, such as command-line use and understanding the inner workings of a machine <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Getting Started with a Dot Files Repository

To begin, users should organize all their configuration files in a [[introduction_to_git_and_github | Git]] repository <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This enables [[version_control_basics_with_git | tracking changes]] and cloning the repository onto other machines <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The repository should include at least one script that applies or installs the configurations on a new system <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This can reduce weeks of manual labor to a simple `git clone` followed by an install script <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

An example repository structure might include a hidden folder for the dot files, such as `.dotfiles` <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Identifying Key Dot Files

Two common and important dot files to track are:

*   **`.gitconfig`**: This file stores [[version_control_basics_with_git | Git]] settings, such as user name and email address, which are typically set when first using [[introduction_to_git_and_github | Git]] <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. As users continue to learn and use [[version_control_basics_with_git | Git]], this file can grow with more configurations <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    > [!NOTE]
    > When publishing a dot files repository publicly (e.g., on GitHub), it is recommended to use the no-reply email address available with a GitHub account to keep a personal email address private <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

*   **`.zshrc`**: As the new default shell on macOS <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, `zsh` uses the `.zshrc` file for shell experience customization, such as the command prompt <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This file can also be expanded with many other customizations <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Challenges of Moving Dot Files

Simply moving dot files like `.gitconfig` or `.zshrc` from the home directory into a separate repository will break their configurations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This happens because software expects to find these configuration files in the home directory <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. For example, moving `.gitconfig` will cause [[version_control_basics_with_git | Git]] to automatically configure committer information based on the username and hostname, overriding the intended settings <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Similarly, `zsh` will lose its custom prompt if `.zshrc` is moved and not found <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

Some files, like `zsh` history, should remain in the home directory and not be tracked in the repository <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## Solution: Symbolic Links (Symlinks)

To solve the issue of breaking configurations while still tracking files in a repository, a symbolic link (symlink) can be used <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. A symlink allows a file to effectively exist in two places at once <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

A symlink is created using the `ln` command with the `-s` option (for symbolic link):
```bash
ln -s /path/to/real/file /path/to/original/location
```
For example, to symlink `.zshrc`:
```bash
ln -s ~/.dotfiles/.zshrc ~/.zshrc
```
<a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

When a symlink is created, the file appears in its original expected location (e.g., the home directory) but points to the actual file within the dot files repository <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Any changes made to either the symlinked file or the real file are reflected in both locations <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This allows software to find and use the configuration files from their expected home directory locations while the "real" files are version-controlled in the dot files repository <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Automating Software Installation with Homebrew

Beyond configuration files, a dot files repository can also manage software installations. Homebrew is a package manager that helps automate this process on macOS <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

Homebrew can keep track of installed software and output a list using the `brew bundle dump` command <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Running this command in the dot files repository creates a `Brewfile` <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

A `Brewfile` lists:
*   **Taps**: Repositories where Homebrew stores its own software and information about other installable software <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Brews**: Command-line tools, which Homebrew helps keep up to date <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Casks**: Full-blown applications <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

This `Brewfile` can then be committed to the [[introduction_to_git_and_github | Git]] repository <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

## The Installation Process (Bootstrap)

To use the dot files repository to set up a new machine, the typical bootstrap process involves:
1.  **Installing Command-Line Tools**: Before [[introduction_to_git_and_github | Git]] and Homebrew can be used, command-line tools often need to be installed <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
2.  **Cloning the Repository**: The dot files repository is cloned to the new machine <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. SSH is preferred for cloning, but HTTPS can be used initially <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
3.  **Symlinking Files**: Symbolic links are created for configuration files from the repository back to their expected locations in the home directory <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
4.  **Installing Homebrew and Software**: Homebrew is installed, and then pointed to the `Brewfile` to reinstall all recorded software <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

While these steps can be listed in a `README` file, a fully automated install script is highly recommended to reduce manual steps and errors, especially with many symlinks <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Future Improvements

Further enhancements to a dot files process can include:
*   Saving system preferences <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   Organizing the repository into separate files <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   Building a robust install script <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   Automating all installation and configuration steps <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.