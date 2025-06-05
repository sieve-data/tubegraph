---
title: Terminal and Git Integration in VS Code
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

[[modern_code_editors_like_visual_studio_code_and_jetbrains | Visual Studio Code]] offers robust integration for the terminal and [[Git version control and collaboration tools in VS Code | Git version control]], streamlining common development workflows and enhancing productivity <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## VS Code Terminal

The integrated terminal in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] allows developers to execute command-line operations directly within the editor <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Opening and Managing Terminals
*   **Opening a new session**: A new terminal session can be opened in the current working directory using `Ctrl + Backtick` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Default Shell**: The terminal uses your system's default shell (e.g., Bash on Linux/Mac) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Different shells like PowerShell or WSL can be selected by clicking the caret icon <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Multiple Sessions**: Developers often need multiple terminal sessions simultaneously (e.g., for a test runner, a dev server) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. To keep these organized, you can click the icon in the terminal panel to change the name or color of each session <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Terminal Navigation and Commands
*   **Navigation**: When typing a command, `Ctrl + Arrows` can be used to quickly navigate to different parts of the text, as the mouse does not work for text selection in the terminal <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Clearing Terminal**: To clear the terminal after an error message, use `Ctrl + K` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Command History**: The `Up Arrow` key allows you to access and rerun previous commands from your history <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Automating Commands with VS Code Tasks
For frequently used commands like `npm run build` or `npm run test`, [[VS Codes integrated terminal and Intellisense | VS Code tasks]] can be created <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. A task is a JSON configuration that defines a command to run in the terminal <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Instead of typing the command, it can be executed automatically via the [[Command Palette Usage in VS Code | Command Palette]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, and the task's name will appear in the terminal sidebar <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Git Version Control

[[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] simplifies [[Git version control and collaboration tools in VS Code | Git version control]] operations, which are often complex and prone to errors when using the command line <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Source Control Tab
The Source Control tab in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] provides a visual breakdown of all changes in the current working directory <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Staging Files**: Files can be staged by pointing and clicking, with icons indicating if a file has been modified, added, or removed <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Git Commands**: A dropdown menu provides a list of possible Git commands, including common actions like committing files, eliminating the need to look them up in documentation <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Git Extensions
*   **GitLens**: This extension provides advanced visualization and exploration tools for your code repository <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. It can identify who last modified a line of code, which is useful for debugging <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Remote Repositories**: This extension allows working with Git repositories on platforms like GitHub without needing to clone them locally <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. After installation and logging in with a GitHub account, you can create new branches, edit code, and submit pull requests directly from [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Remote SSH**: Connects to a remote server <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Remote Containers**: Uses a Docker container as the development environment instead of the local system <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. These Microsoft-managed extensions can transform [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] into a full-fledged Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Safe Renaming of Symbols
When renaming code elements, a simple find and replace across the project can be dangerous <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. A safer approach in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] is to:
1.  Right-click the element to be renamed.
2.  Find all its references or implementations.
3.  Use the "Rename Symbol" option to safely rename it across all relevant files <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.