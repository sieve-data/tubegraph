---
title: Web development tools and browser recommendations
videoId: -atblwgc63E
---

From: [[fireship]] <br/> 

In 2020, Windows has emerged as a robust platform for [[introduction_to_web_development | web development]], largely due to features like the Windows Subsystem for Linux (WSL) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This integration allows developers to leverage the strengths of both Windows and Linux simultaneously <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Windows Subsystem for Linux (WSL)

WSL enables running a real Linux environment directly on Windows without requiring a virtual machine <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This means developers can work with server code in a Linux environment while simultaneously using Windows-specific software like Adobe Photoshop <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For full-stack developers, WSL can link Linux to VS Code, allowing the use of Linux-based utilities and processes from application code <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### WSL1 vs. WSL2
There are two versions, WSL1 and WSL2, which offer the same user experience but differ in their underlying architecture <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. WSL2 is an improvement primarily focused on speed <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The upgrade process between versions is designed to be seamless <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Installation and Usage
To get started with WSL, Windows 10 is required <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The process involves:
1.  Opting into WSL via a PowerShell session run as an administrator <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  Restarting the system <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
3.  Installing a Linux distribution (e.g., Ubuntu, which collaborated with Microsoft on WSL development) from the Microsoft Store <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
Once installed, users can list Linux versions using `wsl -l` and enter a terminal session by typing `wsl` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This environment runs actual x64 Linux binaries, allowing access to Linux apps and tools, as well as the Windows file system and Windows applications <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Benefits of WSL
WSL eliminates the inefficiency of dual-boot systems, where users would have to restart to switch between Windows for applications like Adobe programs or Microsoft Excel and Linux for [[introduction_to_web_development | web development]] <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. With WSL, both operating systems' functionalities and files can be accessed simultaneously, offering the "best of both worlds" <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## Enhanced Terminal Experience
Windows has significantly improved its terminal experience with the new Windows Terminal, available for installation from the Microsoft Store <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This terminal allows easy switching between PowerShell and Linux sessions <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Basic Linux Commands
For those new to Linux, essential commands include:
*   `ls`: List directory contents <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   `mkdir`: Create a new directory <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   `cd`: Change directory <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   `touch`: Create a new file <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   `code`: Launch VS Code to edit a file <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   `sudo`: Run a command as an administrator <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   `apt`: Package manager for installing software in Ubuntu <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Terminal Customization
To enhance the terminal's aesthetics:
*   **PS1 Environment Variable**: The primary prompt string value (`PS1`) in the `.bashrc` or `.zshrc` startup script can be modified to change the appearance of the command line prompt <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Z Shell (Zsh) and Oh My Zsh**: Installing Zsh provides access to "Oh My Zsh", a framework that offers numerous themes and plugins for the command line <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Themes can be set to "random" in the `.zshrc` file to preview different styles <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## VS Code Integration for Web Development

The Remote WSL extension for VS Code is crucial for a seamless [[integrating_linux_tools_in_windows_for_web_development | web development]] experience <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. It allows VS Code windows to be fully integrated with either Linux distributions or Windows <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. When a VS Code window is opened in WSL, the integrated terminal runs Z shell on the Linux OS, and all code execution occurs within that Linux environment <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

This integration is beneficial because it allows developers to have the same low-level dependencies as their production server (e.g., Ubuntu), simplifying back-end development <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Essential Web Development Tools

### [[javascript_trends_and_frameworks | Node.js]]
[[javascript_trends_and_frameworks | Node.js]] is an essential low-level dependency for [[introduction_to_web_development | web developers]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Since Ubuntu doesn't include [[javascript_trends_and_frameworks | Node.js]] by default <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>, the most reliable installation method is using `nvm` (Node Version Manager) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. `nvm` can be installed via a `curl` command in Bash or as a plugin in Zsh, providing easy management of multiple [[javascript_trends_and_frameworks | Node.js]] versions <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Git
Git is typically installed on Ubuntu by default, but it's advisable to update to the latest version using the `apt` package manager <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Developers should also configure a global username and email address with `git config` to tie commits to their identity <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Caching Git credentials for one hour can prevent repeated password prompts when pushing to remote repositories like GitHub <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### GitHub CLI
For GitHub users, the new GitHub CLI for Linux is a valuable tool <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. It can be installed by downloading the Debian release from the GitHub Docs and using the `D package install` command <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The `gh` command provides easy management of repositories, issues, and pull requests on GitHub <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Docker
Docker Desktop is highly recommended for Windows users to manage containers, offering a more intuitive graphical interface than the command line <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. While interoperability between WSL and Docker was previously in development, WSL2 now offers experimental support to connect Docker in both Linux and Windows environments <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Although not essential for beginners, Docker becomes important for professional [[introduction_to_web_development | web development]] at some point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

## Browser Recommendations for Web Development

Having multiple browsers installed is crucial for [[introduction_to_web_development | web development]] <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Chrome**: Preferred for debugging front-end [[javascript_and_frontend_development | JavaScript]] applications due to its powerful debugging tools. A VS Code extension can connect Chrome directly to the VS Code debugger <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Mozilla Firefox**: Recommended for design and CSS-related tasks, as it offers a superior suite of CSS tools for features like Flexbox and Grid <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Brave**: Important for testing websites in a privacy-conscious environment <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This ensures that web application features relying on analytics or user authentication function correctly as privacy-focused browsers gain popularity <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

This guide provides a solid starting point for setting up a modern full-stack [[building_web_apps_with_various_programming_languages | web application]] development environment on Windows with Linux <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.