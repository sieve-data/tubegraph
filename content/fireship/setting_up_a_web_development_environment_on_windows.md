---
title: Setting up a web development environment on Windows
videoId: -atblwgc63E
---

From: [[fireship]] <br/> 

In 2020, Windows has become a powerful platform for web developers, largely due to the integration of the [[windows_subsystem_for_linux_wsl | Windows Subsystem for Linux (WSL)]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This guide provides a comprehensive overview of setting up a modern [[introduction_to_web_development | web development]] environment on Windows with Linux <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## [[windows_subsystem_for_linux_wsl | Windows Subsystem for Linux (WSL)]]

[[windows_subsystem_for_linux_wsl | WSL]] allows users to run a real Linux environment directly on Windows without the need for a virtual machine <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This means you can work with the Linux filesystem and run Linux binaries natively <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This setup allows for simultaneous work with server code in a Linux environment and applications like Adobe Photoshop on Windows <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It provides the benefits of both operating systems without the inefficiency of a dual-boot system <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### WSL1 vs WSL2

There are two versions: WSL1 and WSL2 <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Both offer the same user experience, but WSL2 features an improved underlying architecture primarily designed for faster performance <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. As of the video's recording, WSL2 was not generally available but was expected soon with a seamless upgrade path <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Installation

To get started, you'll need Windows 10 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

1.  **Opt into WSL**: Open a new PowerShell session as an administrator <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> and paste the necessary command (available in the full article mentioned in the video) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This will prompt a system restart <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
2.  **Install a Linux Distribution**: After rebooting, go to the Microsoft Store and search for "Linux" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. You can install one or more distributions and switch between them <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a> <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Ubuntu is a recommended choice, as Canonical (its publisher) collaborated with Microsoft on WSL's development <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  **Verify Installation**: Once installed, open the command line and run `wsl --list` (or `wsl -l`) to list your Linux versions <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a> <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Typing `wsl` will enter a terminal session for your default version <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Basic WSL Usage

You can access the Windows file system from within the Linux environment and run Windows applications <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Here are some basic Linux commands:
*   `ls`: List contents of a directory <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   `mkdir`: Create a new directory <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   `cd`: Change directory <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   `touch`: Create a new file <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   `sudo`: Prefix any command to run it as an administrator <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   `apt`: Package manager in Ubuntu for installing new software <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Terminal Setup

Windows Terminal is a significant improvement over previous Windows command line tools and can be installed from the Microsoft Store <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a> <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. It allows you to easily open sessions in PowerShell or Linux <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Customizing the Prompt

When a new Linux terminal session starts, it runs a configurable startup script in `.bashrc` or `.zshrc` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a> <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   The `PS1` environment variable in the `.bashrc` file represents the primary prompt string value <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   You can modify this file to change the prompt, for example, to show a timestamp or shorten the working directory path <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Enhancing the Terminal with Z Shell

Installing [[using_dotfiles_to_automate_development_environment_setup | Z Shell]] (Zsh) and `Oh My Zsh` provides access to many themes and plugins for the command line <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   You can install `Oh My Zsh` by fetching its remote URL with `curl` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a> <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   To explore themes, open the root `.zshrc` file and set the theme variable to `random` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a> <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This will apply a different theme each time a new terminal session is opened <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Once you find a preferred theme, you can set its name as the theme variable <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## [[using_vs_code_with_linux_and_windows | VS Code]] Integration

[[integrating_linux_tools_in_windows_for_web_development | Integrating Linux tools in Windows for web development]] is seamlessly done through [[using_vs_code_with_linux_and_windows | VS Code]]. Install the Remote [[windows_subsystem_for_linux_wsl | WSL]] extension <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a> <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a> <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   This extension allows you to open a [[using_vs_code_with_linux_and_windows | VS Code]] window fully integrated with your Linux distributions or Windows <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a> <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   Press `Ctrl+Shift+P` to open the command palette and select the option to open or reopen a window in [[windows_subsystem_for_linux_wsl | WSL]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a> <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   When a terminal session is opened within [[using_vs_code_with_linux_and_windows | VS Code]] (Ctrl+Backtick), it will run in the Linux environment <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a> <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   All code written and executed here will run on Linux, providing consistency with server environments (e.g., Ubuntu on a server) and simplifying back-end development <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a> <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   For editing files, you can use `code` to launch [[using_vs_code_with_linux_and_windows | VS Code]] from the Linux command line <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. If you prefer [[setting_up_vim_within_visual_studio_code | Vim]], you can use `vi` instead <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Essential Tools and Dependencies

### [[setting_up_a_nodejs_and_express_environment | Node.js]]

[[setting_up_a_nodejs_and_express_environment | Node.js]] is a critical dependency for [[introduction_to_web_development | web development]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a> <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. Ubuntu does not include Node.js by default <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   The most reliable way to install Node.js is with `nvm` (Node Version Manager) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   You can install `nvm` using a `curl` command in Bash <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   If using Zsh, add it as a plugin to your `.zshrc` file <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a> <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   Use `nvm install` to install specific Node.js versions (e.g., the recommended version from nodejs.org and the latest bleeding-edge version) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   Switch between installed versions using `nvm use` <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a> <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This provides an easy way to manage your Node.js installation <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Git

Git is another essential low-level dependency <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   It is installed by default on Ubuntu, but you might want to update to the latest version using the `apt` package manager <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a> <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Set Global Username and Email**: Configure your global Git username and email using `git config` commands <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. This ties your commits to your identity <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Cache Credentials**: To avoid repeatedly entering your username and password when pushing to remote repositories like GitHub, cache your Git credentials for a specified duration (e.g., one hour) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### GitHub CLI

The brand-new GitHub CLI for Linux is a useful tool <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a> <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Download the Debian release from the GitHub Docs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   Install it using the `dpkg install` command <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a> <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   This provides access to the `gh` command, which can be used to create and manage repositories, fetch issues, or pull requests <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Docker

While not essential for beginners, Docker is a valuable tool for web development <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   It's highly recommended to install the Docker Desktop app on Windows, ideally with Windows Pro for full functionality <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   The desktop app offers a graphical interface to manage containers, inspect logs, and view statistics <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **WSL Interop**: At the time of recording, interoperability between [[windows_subsystem_for_linux_wsl | WSL]] and Docker was still being developed <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a> <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Full support is being added in [[windows_subsystem_for_linux_wsl | WSL 2]], with an experimental support option to connect Docker across both Linux and Windows environments <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a> <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a> <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## [[web_development_tools_and_browser_recommendations | Web Browsers]] for Development

For [[introduction_to_web_development | web development]], it's beneficial to have several browsers installed <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a> <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Google Chrome**: Preferred for debugging front-end JavaScript applications due to its powerful JavaScript debugging tools <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a> <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A [[using_vs_code_with_linux_and_windows | VS Code]] extension can connect Chrome directly to the [[using_vs_code_with_linux_and_windows | VS Code]] debugger <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a> <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Mozilla Firefox**: Recommended for design or CSS-related tasks, as it offers a superior suite of CSS tools for features like Flexbox and Grid <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a> <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a> <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Brave**: Useful for inspecting your site in a privacy-conscious environment <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a> <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. It helps assess how your web application functions (e.g., analytics, user authentication) in browsers with strong privacy features, which are becoming increasingly popular <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a> <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

This setup provides a solid starting point for developing full-stack web applications on Windows with Linux <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a> <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.