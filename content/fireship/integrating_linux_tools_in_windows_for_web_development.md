---
title: Integrating Linux tools in Windows for web development
videoId: -atblwgc63E
---

From: [[fireship]] <br/> 

In 2020, Windows has emerged as a robust platform for [[introduction_to_web_development | web development]], largely due to a feature called [[windows_subsystem_for_linux_wsl | Windows Subsystem for Linux]] (WSL) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This integration allows developers to run a real Linux environment directly on Windows, eliminating the need for a separate virtual machine <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This setup enables seamless switching between server-side coding in a Linux environment and using Windows-specific [[programming_software | software]] like Adobe Photoshop <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

This guide provides a comprehensive approach to [[setting_up_a_web_development_environment_on_windows | setting up a modern web development environment on Windows]] with Linux <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Windows Subsystem for Linux (WSL)

[[windows_subsystem_for_linux_wsl | WSL]] allows users to run actual L64 Linux binaries directly on Windows, providing access to all the applications and tools available on a native Linux machine <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. It also enables access to the Windows file system and the ability to run Windows applications from the Linux environment <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This contrasts with traditional dual-boot systems, which require restarting to switch operating systems and do not share files or functionality <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### WSL 1 vs. WSL 2
There are two versions: [[windows_subsystem_for_linux_wsl | WSL]] 1 and [[windows_subsystem_for_linux_wsl | WSL]] 2 <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. While both offer the same user experience, [[windows_subsystem_for_linux_wsl | WSL]] 2 is an architectural improvement focused on speed <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. [[windows_subsystem_for_linux_wsl | WSL]] 2 was not generally available at the time of recording but was expected soon, with a seamless upgrade process <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Installation
To get started with [[windows_subsystem_for_linux_wsl | WSL]]:
1.  Ensure you have Windows 10 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
2.  Opt into [[windows_subsystem_for_linux_wsl | WSL]] by opening a PowerShell session as an administrator and pasting a specific command (available in the full article) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A system restart will be prompted <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  After rebooting, go to the Microsoft Store and search for "Linux" to find distributions available for installation <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
4.  Ubuntu is a recommended choice, developed in collaboration with Microsoft for [[windows_subsystem_for_linux_wsl | WSL]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
5.  Once installed, you can list your Linux versions by opening the command line and running `wsl -l` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Typing `wsl` will enter a terminal session for your default Linux distribution <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Terminal Setup

The default Windows terminal can be improved by installing the new Windows Terminal from the Microsoft Store <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This terminal allows easy switching between PowerShell and Linux sessions <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Useful Linux Commands
*   `ls`: List contents of a directory <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   `mkdir`: Create a new directory <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   `cd`: Change directory <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   `touch`: Create a new file <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   `vi` (or `vim`): Edit files (for advanced users) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   `code`: Launch [[using_vs_code_with_linux_and_windows | VS Code]] to edit a file <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   `sudo`: Prefix any command to run as an administrator <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   `apt`: Package manager in Ubuntu for installing new [[programming_software | software]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Customizing the Terminal
To enhance the terminal's appearance:
*   **Bash RC**: The `bashrc` file (or `zshrc` for Z shell) is a startup script run when a new Linux terminal session opens <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **PS1 Environment Variable**: Modify the `PS1` variable in `bashrc` to change the primary prompt string <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Examples of variables and values for customization can be found in the full article <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Z Shell (zsh) and Oh My Zsh**: Install Z shell and Oh My Zsh for access to themes and plugins for the command line <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Themes can be randomized by setting the theme variable in the `zshrc` file to "random" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Integrating with VS Code

To fully integrate your Linux environment with [[using_vs_code_with_linux_and_windows | VS Code]], install the **Remote [[windows_subsystem_for_linux_wsl | WSL]] extension** <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This extension allows [[using_vs_code_with_linux_and_windows | VS Code]] to open windows fully integrated with either your Linux distros or Windows <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

When a [[using_vs_code_with_linux_and_windows | VS Code]] window is opened in [[windows_subsystem_for_linux_wsl | WSL]], a blue box in the bottom left corner indicates that you are running Ubuntu <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Opening a terminal session within [[using_vs_code_with_linux_and_windows | VS Code]] (Ctrl+Backtick) will run Z shell on your Linux OS <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. All code written and executed in this environment will happen on Linux, ensuring consistent low-level dependencies with a Linux server <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Essential Web Development Tools

### Node.js
Node.js is a crucial low-level dependency for [[introduction_to_web_development | web development]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Ubuntu does not come with Node.js installed by default <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The most reliable way to install it is using Node Version Manager (NVM) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. NVM can be installed via a `curl` command in bash, or as a plugin for `zsh` <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. NVM allows you to install multiple Node.js versions (e.g., recommended and latest bleeding-edge) and switch between them using `nvm use` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This provides an easy way to manage your Node.js installation on Linux <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Git
Git is another essential low-level dependency <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. It is installed on Ubuntu by default but can be updated to the latest version using the `apt` package manager <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. It's recommended to set a global username and email address with `git config` to tie commits to your identity <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. To avoid repeatedly entering credentials when pushing to remote repositories like GitHub, you can cache your Git credentials for a specified duration (e.g., one hour) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### GitHub CLI
For GitHub users, installing the GitHub CLI for Linux is beneficial <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This involves downloading the Debian release from the GitHub Docs and installing it using the `D package install` command <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The `gh` command then allows easy creation and management of GitHub repositories, as well as fetching issues or pull requests <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Docker
For container management, installing the Docker Desktop app on Windows is highly recommended, though it may require Windows Pro <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This app provides an intuitive way to manage containers, inspect logs, and view stats, often preferred over command-line usage <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

Currently, full interoperability between [[windows_subsystem_for_linux_wsl | WSL]] and Docker is under development <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. If you are running [[windows_subsystem_for_linux_wsl | WSL]] 2, you might find an experimental support option to connect Docker across both Linux and Windows environments <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Docker is not strictly essential for new [[introduction_to_web_development | web development]] beginners but becomes valuable later <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

## Web Browsers

For [[introduction_to_web_development | web development]], it's beneficial to have multiple [[web_development_tools_and_browser_recommendations | browsers]] installed <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>:
*   **Chrome**: Preferred for debugging front-end [[using_javascript_on_web_and_server_environments | JavaScript]] applications due to its powerful debugging tools. A [[using_vs_code_with_linux_and_windows | VS Code]] extension can connect Chrome directly to the [[using_vs_code_with_linux_and_windows | VS Code]] debugger <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Mozilla Firefox**: Recommended for design or CSS-related tasks, as it offers a superior suite of CSS tools for features like Flexbox and Grid <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Brave**: Useful for inspecting your site in a privacy-conscious environment <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. Testing how your [[building_web_apps_with_various_programming_languages | web apps]] perform with analytics data or user authentication in such [[web_development_tools_and_browser_recommendations | browsers]] is important as their popularity grows <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

This setup provides a solid foundation for developing full-stack [[building_web_apps_with_various_programming_languages | web applications]] on Windows with Linux <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.