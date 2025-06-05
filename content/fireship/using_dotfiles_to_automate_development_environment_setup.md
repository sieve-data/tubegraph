---
title: Using dotfiles to automate development environment setup
videoId: r_MpUP6aKiQ
---

From: [[fireship]] <br/> 

Dotfiles are text-based configuration files, often hidden on your system, that start with a period (e.g., `.bashprofile`, `.env`, `.gitconfig`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. They allow developers to fully set up or restore a customized development environment <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Why Use Dotfiles?

The "Do Not Repeat Yourself" (DRY) principle, common in coding, also applies to configuring a development environment <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Instead of manually reinstalling and reconfiguring everything from scratch on a new machine, dotfiles enable an automated and hands-off replication of your ideal setup <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

A dotfiles repository allows you to:
*   Chronicle the installation of your favorite applications and [[shell_commands_and_bash_scripting | command line]] tools <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Keep track of how software is configured <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Record system preferences and changes made to your computer <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Maintaining your own dotfiles repository also helps develop discipline in [[shell_commands_and_bash_scripting | command line]] use, [[version_control_and_remote_development_in_vs_code | Git]], and understanding the organization and inner workings of your machine <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Core Components of a Dotfiles Setup

### Git Repository
To get started, organize all your configuration files in a [[version_control_and_remote_development_in_vs_code | Git]] repository <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This allows you to track changes and clone the repository onto other machines <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. It's recommended to make the dotfiles folder itself hidden by prefixing it with a period (e.g., `.dotfiles`) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Installation Script
The dotfiles repository should contain at least one [[shell_commands_and_bash_scripting | script]] that applies or installs the configurations on a new system <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This reduces weeks of manual labor to a simple `git clone` followed by an install [[shell_commands_and_bash_scripting | script]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Symbolic Links (Symlinks)
Moving dotfiles from their expected home directory location into a repository can break software configurations <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. To solve this without duplicating files, use symbolic links (symlinks) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

A symlink creates a pointer from the original expected location of the dotfile (e.g., in the home directory) to its actual location within your dotfiles repository <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Software will follow this link and use the file from the repository, ensuring configurations are applied correctly <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Changes made to the symlinked file are reflected in the real file in the repository <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

To create a symbolic link, use the `ln -s` [[shell_commands_and_bash_scripting | command]] <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Package Manager (Homebrew Example)
An automated way to install software is crucial <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Homebrew is a package manager for macOS that helps track and reinstall software <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

You can use `brew bundle dump --describe` within your dotfiles repo to create a `Brewfile` <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>, <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This file lists all installed taps (Homebrew repositories), brews (command-line tools), and casks (full applications), allowing them to be reinstalled later <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

### Documenting the Bootstrap Process
To avoid forgetting [[steps_to_bootstrap_a_new_computer_with_a_dotfiles_repository | steps to bootstrap a new computer]], keep a list of instructions in your repository's `README` file <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

A typical bootstrapping process might include:
1.  Installing [[shell_commands_and_bash_scripting | command line]] tools (e.g., for [[version_control_and_remote_development_in_vs_code | Git]] and Homebrew) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
2.  Cloning the dotfiles repository <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
3.  Repeating the symlinking [[steps_to_bootstrap_a_new_computer_with_a_dotfiles_repository | steps]] (though this is best automated into an install [[shell_commands_and_bash_scripting | script]]) <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
4.  Installing Homebrew and then pointing it to your `Brewfile` to reinstall all software <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## Common Dotfiles Examples

### `.gitconfig`
This file stores your [[version_control_and_remote_development_in_vs_code | Git]] configuration, including your name and email address for commits <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. It can grow with more specific configurations as you use [[version_control_and_remote_development_in_vs_code | Git]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. When making your dotfiles repo public, it's recommended to use a no-reply email address available with your GitHub account to keep your personal email private <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### `.zshrc`
`zsh` is the default [[shell_commands_and_bash_scripting | shell]] on macOS <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The `.zshrc` file is used to customize your [[shell_commands_and_bash_scripting | shell]] experience, such as customizing the prompt <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### `.Brewfile`
Created by `brew bundle dump`, this file lists all software installed via Homebrew, including taps, brews (command-line tools), and casks (full applications) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## Managing Dotfiles with VS Code

[[version_control_and_remote_development_in_vs_code | VS Code]]'s file explorer can show hidden files by default <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. You can also toggle hidden files in Finder and [[version_control_and_remote_development_in_vs_code | VS Code]] using the `Command + Shift + Period` key combination <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. When a symlink is created, [[version_control_and_remote_development_in_vs_code | VS Code]] will often show an arrow icon next to the file, indicating it's a symlink <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. [[version_control_and_remote_development_in_vs_code | VS Code]] can follow symlinks and treat them as real files for editing <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Files Not to Track
While many configuration files are suitable for tracking, some, like `zsh_history`, are typically left in the home directory and not tracked in your dotfiles repository <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.