---
title: Efficient navigation and code editing in VS Code
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

[[productivity_tips_for_visual_studio_code | Visual Studio Code]] (VS Code) is a powerful tool with many [[productivity_tips_for_visual_studio_code | productivity-boosting features]] that can significantly speed up coding and analysis <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Mastering these features can lead to writing and analyzing code faster, ultimately saving time <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Getting Started

Once VS Code is installed, you can open a directory with files. While opening via the file explorer works <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, a quicker method is to use the VS Code CLI (Command Line Interface) from the terminal with the `code` command <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. On Mac or Linux, ensure the VS Code binary is added to your path first <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Keyboard-First Approach

For efficient [[productivity_tips_for_visual_studio_code | VS Code usage]], relying less on the mouse is crucial <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While the mouse makes the tool approachable, it's not the most efficient way to work <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Anything done with the mouse can likely be done quicker with the keyboard <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Memorizing around 10 to 20 [[vs_code_keyboard_shortcuts_and_commands | keyboard shortcuts]] can significantly improve workflow <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### The Command Palette

The most important [[vs_code_keyboard_shortcuts_and_commands | keyboard shortcut]] to memorize is `Ctrl+P` (or `Cmd+P` on Mac), which opens the command palette <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The command palette provides access to most VS Code functionalities from the keyboard without needing to memorize many keybindings <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

*   **File Navigation**: By default, it lists recently opened files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. You can start typing a file name to find it in your project, which is much faster than clicking through directories <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Command Execution**: Typing a right angle bracket (`>`) gives you access to virtually any command in VS Code, including commands for [[using_extensions_to_enhance_vs_code_functionality | extensions]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. For example, you can toggle the minimap <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   The [[using_extensions_to_enhance_vs_code_functionality | Quokka extension]] can be started and stopped via the command palette, allowing JavaScript code to be executed in the background with output appended directly in the editor for rapid prototyping <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Finding Code and Symbols

Navigating large files and projects efficiently is key.

*   **Symbols in Current File**: Instead of scrolling, use the `@` symbol from the command palette to list every symbol in the current file, allowing quick navigation <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. You can also bypass the command palette by using `Ctrl+Shift+Period` directly in the file <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Symbols Throughout Project**: To find a symbol across the entire project, including dependencies like `node_modules`, use a `#` followed by the symbol's name <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   **Fuzzy Search**: For long class names, you only need to type the first character of each camel-cased word <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Efficient Code Editing

*   **Go to Line**: To quickly move to a specific line, use `Ctrl+G` followed by the line number <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Text Navigation & Selection**:
    *   Use arrow keys to move character by character <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    *   Hold `Shift` while using arrow keys to highlight text <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Use `Ctrl+Arrow` to move word by word <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   To highlight a word where your cursor is, use `Ctrl+D` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Pressing `Ctrl+D` repeatedly will select subsequent occurrences of the same text, enabling multi-line editing <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Multi-Cursor Editing**: Hold `Alt` and click in different parts of the editor to set up multiple cursors, useful for repetitive CSS properties or HTML tags <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   The [[using_extensions_to_enhance_vs_code_functionality | Auto Rename Tag extension]] automatically renames the closing HTML tag when you edit the opening one, and works in other languages too <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Cutting, Moving, and Copying Lines**:
    *   To cut a line, simply place your cursor on it and hit `Ctrl+X` (no highlighting needed) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   To move a line, use `Alt` followed by the up or down arrows <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   To copy a line while moving it, use `Alt+Shift` followed by the arrows <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Commenting Code**:
    *   Highlight the desired code using the mouse or `Ctrl+L` (to highlight line by line) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Use `Ctrl+/` to toggle comments on the highlighted code <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
    *   The [[using_extensions_to_enhance_vs_code_functionality | Add JsDoc Comments extension]] allows you to highlight a function and use the command palette to automatically add JSDoc comments <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
        *   **Bonus Tip**: In JSDoc comments, use the `@link` tag to link to other symbols in your source code; hovering over the link will show its comment, and clicking will navigate to that part of the code <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   The [[using_extensions_to_enhance_vs_code_functionality | Better Comments extension]] provides automatic highlighting in comment text, making `!` lines red and `TODO`s orange <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## Terminal and Version Control Integration

*   **Integrated Terminal**: Open a new terminal session directly in your current working directory using `Ctrl+Backtick` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. You can switch between different shells (e.g., PowerShell, WSL) if needed <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   For multiple terminal sessions, you can name or color them to stay organized <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
    *   Within the terminal, use `Ctrl+Arrows` to navigate word by word within a command <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Use `Ctrl+K` to clear the terminal, and the up arrow to recall the last command <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **VS Code Tasks**: Create a VS Code task (a JSON configuration) to run common terminal commands (e.g., `npm run build`, `npm run test`) via the command palette, simplifying repetitive actions <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **[[version_control_and_remote_development_in_vs_code | Version Control]]**: The source control tab in VS Code offers a visual breakdown of changes in your working directory, making [[using_vs_code_with_git | Git]] operations easier by pointing and clicking to stage files <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. It also lists available [[using_vs_code_with_git | Git]] commands <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
    *   The [[using_extensions_to_enhance_vs_code_functionality | GitLens extension]] provides advanced ways to visualize and explore code history <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   [[version_control_and_remote_development_in_vs_code | Remote Repositories extension]]: Allows working with GitHub repositories without cloning them locally; you can create branches, edit code, and submit pull requests entirely within VS Code <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   [[version_control_and_remote_development_in_vs_code | Remote SSH]] and [[version_control_and_remote_development_in_vs_code | Remote Containers]]: These extensions enable connecting to remote servers via SSH or using Docker containers as your development environment, turning VS Code into a full-blown integrated development environment (IDE) <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Customization and Productivity Tools

*   **Custom Snippets**: For repetitive boilerplate code, create custom snippets via the "Configure User Snippets" command palette action <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. These can be global or workspace-scoped <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   Before building your own, check the [[using_extensions_to_enhance_vs_code_functionality | extensions]] panel for pre-built snippets for popular frameworks <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **Creating Nested Directories**: When creating a new file in the file explorer, you can automatically create non-existent nested directories by putting a slash in front of the file name (e.g., `folder/subfolder/file.js`) <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **[[using_extensions_to_enhance_vs_code_functionality | Paste JSON as Code extension]]**: This extension uses "QuickType" to automatically infer and generate TypeScript types from a JSON object, saving hours of manual conversion <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Safe Renaming**: Instead of a dangerous find-and-replace for renaming, right-click the symbol you want to rename to find all its references or implementations <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Then, use the "Rename Symbol" option to safely rename it across all files <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.