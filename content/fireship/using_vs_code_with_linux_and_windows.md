---
title: Using VS Code with Linux and Windows
videoId: -atblwgc63E
---

From: [[fireship]] <br/> 
Windows has evolved into a powerful platform for web development, largely due to features like the [[windows_subsystem_for_linux_wsl | Windows Subsystem for Linux (WSL)]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## [[windows_subsystem_for_linux_wsl | Windows Subsystem for Linux (WSL)]]
[[windows_subsystem_for_linux_wsl | WSL]] enables users to run a real Linux environment directly on Windows without the need for a separate virtual machine <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This means you can work with the Linux filesystem and run Linux binaries as if you were on a native Linux machine, while simultaneously accessing Windows applications like Adobe Photoshop <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

For full-stack developers, [[windows_subsystem_for_linux_wsl | WSL]] can be linked to [[setting_up_a_web_development_environment_on_windows | VS Code]], allowing the use of any Linux-based utility and the spawning of actual Linux processes from your application code <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### WSL Versions
There are two versions: [[windows_subsystem_for_linux_wsl | WSL1]] and [[windows_subsystem_for_linux_wsl | WSL2]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Both offer the same user experience, but [[windows_subsystem_for_linux_wsl | WSL2]] features an improved underlying architecture primarily designed for faster performance <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Installation of WSL
To get started with [[windows_subsystem_for_linux_wsl | WSL]], you'll need Windows 10 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The initial steps for installation involve:
1.  **Opt-in to WSL**: Open a new PowerShell session as an administrator and paste the provided command (found in the full article) <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. A system restart will be required <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
2.  **Install a Linux Distribution**: After rebooting, head to the Microsoft Store. Search for "Linux" to find various distributions. Ubuntu is a solid choice, as its publisher, Canonical, collaborated with Microsoft on [[windows_subsystem_for_linux_wsl | WSL]]'s development <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. You can install multiple distros and switch between them as needed <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Verify Installation**: Once installed, you can open the command line and run `wsl -l` to list your Linux versions <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Typing `wsl` will enter a terminal session for your default version <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This setup offers the benefit of running actual x64 Linux binaries, allowing access to all standard Linux apps and tools <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Additionally, you can access the Windows file system and run Windows applications from within the Linux environment <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, avoiding the inefficiencies of a dual-boot system <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Terminal and Command Line Enhancements

Windows' terminal has been significantly improved. You can install the new Windows Terminal from the Microsoft Store, which allows you to easily open sessions in PowerShell or Linux <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Basic Linux Commands
For those new to Linux, here are some useful commands:
*   `ls`: List contents of a directory <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   `mkdir`: Create a new directory <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   `cd`: Change directory <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   `touch`: Create a new file <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   `sudo`: Prefix any command to run it as an administrator <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   `code`: Launch [[setting_up_a_web_development_environment_on_windows | VS Code]] to edit a file <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   `apt`: Package manager in Ubuntu for installing new software <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Customizing the Terminal Appearance
You can customize the command line's appearance:
*   **Bash RC File**: When a new Linux terminal session starts, it runs a startup script in the `.bashrc` file <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **PS1 Environment Variable**: The `PS1` environment variable in `.bashrc` controls the primary prompt string <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. You can modify this by exporting a new value for `PS1` at the bottom of the `.bashrc` file <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Z Shell and Oh My Zsh**: For more advanced customization, install Z shell. This gives you access to "Oh My Zsh," which provides many themes and plugins for the command line <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. You can set the theme variable in the `ZSHRC` file to `random` to cycle through themes upon opening a new session, then copy the name of any theme you like <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## [[version_control_and_remote_development_in_vs_code | VS Code]] and WSL Integration
To seamlessly connect your terminal to [[setting_up_a_web_development_environment_on_windows | VS Code]], install the Remote - WSL extension <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This allows you to open a [[setting_up_a_web_development_environment_on_windows | VS Code]] window fully integrated with one of your Linux distros or with Windows <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

Once connected (indicated by a blue box in the bottom left corner showing your Linux distro, e.g., Ubuntu), opening a terminal session (`Ctrl+Backtick`) will run Z shell on your Linux OS <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. All code written and processes executed will happen on Linux, providing consistency with server environments that also run Ubuntu <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Essential Web Development Dependencies

### Node.js
Node.js is a critical dependency for web development. Ubuntu does not include Node.js by default <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The most reliable way to install it is using Node Version Manager (NVM) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. You can install NVM using a curl command in bash or by adding it as a plugin to your ZSHRC file if you're using Z shell <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. NVM allows you to install and switch between different Node.js versions, including the recommended and latest bleeding-edge versions <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Git
[[using_vs_code_with_git | Git]] is pre-installed on Ubuntu, but it's advisable to update to the latest version using the `apt` package manager <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. After updating, set your global username and email address with `git config` so your commits are properly attributed <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. A pro tip is to cache your [[using_vs_code_with_git | Git]] credentials to avoid repeatedly entering your username and password for remote repository operations <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### GitHub CLI
For GitHub users, installing the new GitHub CLI for Linux is recommended. Download the Debian release from the GitHub Docs and install it using the `D package install` command <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This provides access to the `gh` command, allowing you to easily create and manage repos, fetch issues, or pull requests directly from the command line <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Docker
For managing containers, the Docker Desktop app on Windows is highly recommended, though it may require Windows Pro <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. It provides an intuitive interface to manage containers, inspect logs, and view statistics <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Full interoperability between [[windows_subsystem_for_linux_wsl | WSL2]] and Docker is actively being developed; for [[windows_subsystem_for_linux_wsl | WSL2]] users, experimental support can be enabled to connect Docker in both Linux and Windows environments <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Docker is not essential for beginners but becomes valuable for more advanced development <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

## Web Browsers for Development
For web development, it's beneficial to have several browsers installed:
*   **Chrome**: Preferred for debugging front-end JavaScript applications due to its powerful JavaScript debugging tools. A [[using_extensions_to_enhance_vs_code_functionality | VS Code extension]] can connect Chrome directly to the [[setting_up_a_web_development_environment_on_windows | VS Code]] debugger <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Mozilla Firefox**: Ideal for design and CSS work due to its superior suite of CSS tools for features like Flexbox and Grid <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Brave**: Recommended for inspecting sites in a privacy-conscious environment <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Testing in Brave helps ensure your web app functions correctly in browsers that block analytics or handle authentication differently <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

This comprehensive setup provides a strong foundation for developing full-stack web applications on Windows with Linux <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. More [[productivity_tips_for_visual_studio_code | productivity tips]] for developers are often found in specialized courses <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.