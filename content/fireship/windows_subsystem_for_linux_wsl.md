---
title: Windows Subsystem for Linux WSL
videoId: -atblwgc63E
---

From: [[fireship]] <br/> 

Windows Subsystem for Linux (WSL) enables users to run a real [[introduction_to_linux_and_its_history | Linux]] environment directly on Windows without the need for a virtual machine [00:00:16]. This feature has made Windows "the ultimate platform" for web developers [00:00:02]. With WSL, developers can use the command line to interact with the [[introduction_to_linux_and_its_history | Linux]] filesystem as if they were natively on [[introduction_to_linux_and_its_history | Linux]] [00:00:24]. It allows for simultaneous work on server code in [[setting_up_vim_within_visual_studio_code | Vim]] on one screen while using Windows-exclusive software like Adobe Photoshop on another [00:00:31]. For full-stack developers, WSL can link [[introduction_to_linux_and_its_history | Linux]] to [[using_vs_code_with_linux_and_windows | VS Code]], facilitating the use of [[introduction_to_linux_and_its_history | Linux]]-based utilities and the spawning of actual [[introduction_to_linux_and_its_history | Linux]] processes from application code [00:00:38].

The integration of [[introduction_to_linux_and_its_history | Linux]] within Windows is a significant improvement, especially for web development [00:00:54]. It allows for the setup of essential tools like browsers, [[using_vs_code_with_git | Git]], Node.js, and Docker within a cohesive environment [00:01:00].

## WSL 1 vs. WSL 2

There are two versions of WSL: WSL 1 and WSL 2 [00:01:25]. Both offer the same user experience, but WSL 2 features an improved underlying architecture primarily designed for faster performance [00:01:30]. While WSL 2 was not generally available at the time of the transcript, a seamless upgrade process was anticipated [00:01:38].

## Installation and Setup

To get started with WSL, Windows 10 is required [00:01:18].

### Enabling WSL

1.  Open a new PowerShell session as an administrator [00:01:47].
2.  Paste the provided command (available in the full article) [00:01:50].
3.  Restart your system when prompted [00:01:54].

### Installing a Linux Distribution

After rebooting:
1.  Go to the Microsoft Store [00:01:56].
2.  Search for "[[introduction_to_linux_and_its_history | Linux]]" to find distributions available for Windows [00:01:58].
3.  Install one or more distros and switch between them as needed [00:02:02]. Ubuntu is a recommended choice, especially since its publisher, Canonical, collaborated with Microsoft on WSL's development [00:02:05].

### Verifying Installation

Once installed, open the command line and run `wsl -l` to list your [[introduction_to_linux_and_its_history | Linux]] versions [00:02:15]. Typing `wsl` will enter a terminal session for your default [[introduction_to_linux_and_its_history | Linux]] version [00:02:21].

## Bridging Windows and Linux

With WSL, users run actual x64 [[introduction_to_linux_and_its_history | Linux]] binaries; it's not emulated or modified, allowing all standard [[introduction_to_linux_and_its_history | Linux]] apps and tools to function [00:02:26]. Additionally, WSL enables access to the Windows file system and allows running Windows apps from within the [[introduction_to_linux_and_its_history | Linux]] environment [00:02:34].

Historically, developers might have used a dual-boot system to switch between Windows and [[introduction_to_linux_and_its_history | Linux]] for different tasks [00:02:40]. This was inefficient and prevented file sharing between operating systems [00:02:56]. WSL eliminates this, offering the "best of both worlds" [00:03:01].

## Enhanced Terminal Experience

Windows' traditional terminal is improved with the new Windows Terminal, available in the Microsoft Store [00:03:05]. This new terminal allows users to easily open sessions in PowerShell or [[introduction_to_linux_and_its_history | Linux]] [00:03:14].

### Basic Linux Commands

For those new to [[introduction_to_linux_and_its_history | Linux]], useful commands include:
*   `ls`: List directory contents [00:03:20].
*   `mkdir`: Create a new directory [00:03:23].
*   `cd`: Change directory [00:03:26].
*   `touch`: Create a new file [00:03:28].
*   `sudo`: Prefix any command to run it as an administrator [00:03:37].
*   `apt`: [[introduction_to_linux_and_its_history | Linux]] package manager for installing new software in Ubuntu [00:03:40].

For editing files, `code` can be used to launch [[using_vs_code_with_linux_and_windows | VS Code]] [00:03:35].

### Customizing the Terminal

The appearance of the command line can be customized [00:03:56]. Each [[introduction_to_linux_and_its_history | Linux]] terminal session runs a startup script (e.g., `.bashrc`) [00:03:59]. The `PS1` environment variable in this file controls the primary prompt string [00:04:12]. This can be modified to display information like a timestamp or a shortened working directory name [00:04:36].

For more advanced customization, installing Z shell and "Oh My Zsh" provides access to numerous themes and plugins [00:04:45]. Setting the theme variable in the `.zshrc` file to "random" can allow users to preview different themes with each new session [00:05:05].

## Integrating with VS Code

The [[using_vs_code_with_linux_and_windows | Remote WSL extension]] in [[using_vs_code_with_linux_and_windows | VS Code]] enables full integration with your [[introduction_to_linux_and_its_history | Linux]] distros or Windows [00:05:21]. This allows developers to open a [[using_vs_code_with_linux_and_windows | VS Code]] window that operates within the chosen [[introduction_to_linux_and_its_history | Linux]] environment [00:05:26].

When a terminal session is opened within [[using_vs_code_with_linux_and_windows | VS Code]] in WSL mode, it runs Z shell on the [[introduction_to_linux_and_its_history | Linux]] OS [00:05:46]. This means all code execution and development occur on [[introduction_to_linux_and_its_history | Linux]] [00:05:48]. This is beneficial for back-end development as it allows for the same low-level dependencies as a [[introduction_to_linux_and_its_history | Linux]] server [00:06:05].

## Essential Web Development Tools

### Node.js

Node.js is a crucial dependency for web developers [00:06:13]. Ubuntu does not include Node.js by default [00:06:16]. The most reliable installation method is using Node Version Manager (NVM) [00:06:23]. NVM can be installed via a curl command in Bash or as a plugin in Z shell [00:06:27]. NVM allows users to install specific Node.js versions (like the recommended version from nodejs.org and the latest bleeding-edge version) and switch between them using `nvm use` [00:06:40].

### Git

[[using_vs_code_with_git | Git]] is another essential low-level dependency [00:07:05]. While installed by default on Ubuntu, it's advisable to update to the latest version using the `apt` package manager [00:07:08]. Setting a global username and email address with `git config` ensures commits are properly attributed [00:07:18]. Caching [[using_vs_code_with_git | Git]] credentials can prevent repeated username and password prompts when pushing to remote repositories like GitHub [00:07:31].

### GitHub CLI

The GitHub CLI for [[introduction_to_linux_and_its_history | Linux]] can be installed by downloading the Debian release from the GitHub Docs and using the `dpkg` install command [00:07:48]. This provides the `gh` command for managing GitHub repositories, issues, and pull requests directly from the command line [00:08:02].

### Docker

[[integrating_linux_tools_in_windows_for_web_development | Docker Desktop]] is highly recommended for managing containers on Windows, though it typically requires Windows Pro [00:08:11]. It offers a graphical interface to view logs and statistics for running containers, which can be more intuitive than the command line [00:08:18]. As of the transcript, direct interoperability between WSL and [[integrating_linux_tools_in_windows_for_web_development | Docker]] was still being developed [00:08:33]. Full support was expected in WSL 2 with an experimental option to connect [[integrating_linux_tools_in_windows_for_web_development | Docker]] across both [[introduction_to_linux_and_its_history | Linux]] and Windows environments [00:08:46]. While not essential for new web developers, [[integrating_linux_tools_in_windows_for_web_development | Docker]] is a valuable tool to consider at some point [00:09:01].

## Web Browsers for Development

For web development, having multiple browsers is crucial [00:09:08].
*   **Chrome**: Preferred for debugging front-end JavaScript applications due to its powerful debugging tools and a [[using_extensions_to_enhance_vs_code_functionality | VS Code extension]] that connects Chrome to the [[using_vs_code_with_linux_and_windows | VS Code]] debugger [00:09:13].
*   **Mozilla Firefox**: Recommended for design and CSS work, offering a superior suite of CSS tools for features like Flexbox and Grid [00:09:27].
*   **Brave**: Useful for inspecting sites in a privacy-conscious environment, ensuring web apps function correctly even with analytics tracking or user authentication in privacy-focused browsers [00:09:41].

This setup provides a strong foundation for [[setting_up_a_web_development_environment_on_windows | developing full-stack web applications on Windows with Linux]] [00:10:01].