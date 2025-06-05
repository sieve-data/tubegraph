---
title: Productivity tips for Visual Studio Code
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

Visual Studio Code (VS Code) is a powerful tool designed to boost developer productivity, offering a wide array of features beyond a simple text editor with code highlighting <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Mastering its capabilities can significantly enhance the speed of writing and analyzing code <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Getting Started

### Opening Projects from the Command Line
While you can open a directory by using the file explorer and clicking "Open with VS Code," a quicker method is to use the [[vs_code_keyboard_shortcuts_and_commands | VS Code CLI]] from your terminal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Simply use the `code` command <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Note**: On Mac or Linux, you may first need to add the VS Code binary to your system's path <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Keyboard-Centric Workflow

Reliance on the mouse can slow down your workflow in VS Code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While VS Code is approachable with mouse usage, the most efficient way to work is by prioritizing keyboard commands <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. You don't need to learn complex systems like Vim or Emacs <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, but understanding that almost any mouse action has a quicker keyboard equivalent is crucial <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Memorizing 10-20 key shortcuts can significantly improve your productivity <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### The Command Palette
The Command Palette is a central tool for keyboard-driven interaction <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Open**: `Ctrl+P` (or `Cmd+P` on Mac) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Functionality**:
    *   Lists recently opened files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
    *   Allows finding files in your project by typing their name <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
    *   Accesses virtually any VS Code command by typing `>` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This includes commands for [[using_extensions_to_enhance_vs_code_functionality | extensions]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Lists every symbol (functions, interfaces, etc.) within the current file by typing `@` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. You can bypass the Command Palette for this with `Ctrl+Shift+Period` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   Finds a symbol throughout the entire project, including dependencies, by typing `#` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Supports fuzzy searching; for long names, you only need to type the first character of each camel-cased word <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## [[efficient_navigation_and_code_editing_in_vs_code | Efficient Code Editing]]

### Navigation
*   **Go to Line**: Use `Ctrl+G` (or `Cmd+G`) followed by the desired line number to quickly jump to a specific line <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Character and Word Movement**: Use arrow keys for character-by-character movement <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Use `Ctrl+Arrow` (or `Alt+Arrow` on Mac) to move word by word <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Selection and Multi-Cursor Editing
*   **Highlighting**: Hold `Shift` while using arrow keys for character selection or `Ctrl+Arrow` for word selection <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Highlight Word**: Place the cursor on a word and hit `Ctrl+D` (or `Cmd+D`) to highlight it <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Multi-Cursor (Next Occurrence)**: After highlighting a word with `Ctrl+D`, press `Ctrl+D` again to select the next identical occurrence, allowing simultaneous editing <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Multi-Cursor (Arbitrary Positions)**: Hold down `Alt` (or `Option` on Mac) and click at different points in the editor to set up multiple cursors in arbitrary places <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. This is useful for repetitive tasks like writing CSS properties or editing HTML tags <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Line Manipulation
*   **Cut Line**: Place your cursor on a line and hit `Ctrl+X` (or `Cmd+X`) to cut it without needing to highlight <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Move Line**: Use `Alt+Up` or `Alt+Down` (or `Option+Up`/`Down` on Mac) to move the current line up or down <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Copy Line**: Use `Alt+Shift+Up` or `Alt+Shift+Down` (or `Option+Shift+Up`/`Down` on Mac) to copy the current line up or down <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Toggle Comments**: Highlight the desired code and use `Ctrl+/` (or `Cmd+/`) to toggle comments on or off <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## [[using_extensions_to_enhance_vs_code_functionality | Using Extensions to Enhance Functionality]]

VS Code's functionality can be greatly expanded with extensions.

### Code Execution & Prototyping
*   **Quokka**: This [[using_extensions_to_enhance_vs_code_functionality | extension]] allows you to execute JavaScript directly within your file, appending the output into the editor <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. It facilitates rapid prototyping for plain JavaScript <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### HTML/XML Tag Management
*   **Auto Rename Tag**: Automatically renames the corresponding closing HTML/XML tag when you edit the opening one <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. It also works in other languages <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Commenting Tools
*   **Add JSDoc Comments**: After installation, highlight a function and use the Command Palette to automatically add a JSDoc comment block <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. JSDoc comments can include link tags to connect to other symbols in your source code, providing quick navigation and hover information <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Better Comments**: Provides automatic highlighting for different types of comments (e.g., "bang" for red, "to-do" for orange) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### [[version_control_and_remote_development_in_vs_code | Version Control and Remote Development]]
*   **GitLens**: Offers enhanced visualization and exploration of your code within Git <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. It shows who last modified a line of code <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Remote Repositories**: This [[version_control_and_remote_development_in_vs_code | extension]] allows you to work directly with Git repositories on GitHub without cloning them locally <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. You can create branches, edit code, and submit pull requests entirely within VS Code <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Remote SSH**: Connect to and develop on a remote server <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Remote Containers**: Use a Docker container as your development environment instead of your local system <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. These Microsoft-managed extensions can transform VS Code into a full Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Data Structuring
*   **Paste JSON as Code**: For TypeScript users, this [[using_extensions_to_enhance_vs_code_functionality | extension]] can take a JSON object and automatically infer and generate corresponding TypeScript types using `quicktype` <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This can save hours of manual work <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Integrated Terminal

VS Code includes a powerful integrated terminal.
*   **Open Terminal**: Use `Ctrl+Backtick` (or `Cmd+Backtick` on Mac) to open a new terminal session in your current working directory <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Shells**: It uses your default shell, but you can select a different one (e.g., PowerShell, [[using_vs_code_with_linux_and_windows | WSL]]) by clicking the caret <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Managing Multiple Sessions**: For organization, rename or color different terminal sessions (e.g., for test runner, dev server) by clicking the icon <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Terminal Command Navigation**: Use `Ctrl+Arrow` (or `Alt+Arrow` on Mac) to navigate within a typed command before hitting Enter <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Clear Terminal**: Use `Ctrl+K` (or `Cmd+K`) to clear the terminal output <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Command History**: Use the `Up Arrow` to cycle through previous commands in your history <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### VS Code Tasks
To avoid repeatedly typing common terminal commands (e.g., `npm run build`), you can create a VS Code task <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Definition**: Tasks are JSON configurations that contain commands you want to run <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Execution**: Run tasks directly from the Command Palette <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## [[using_vs_code_with_git | Git Integration]]

While [[using_vs_code_with_git | Git]] commands can be complex and error-prone, VS Code's Source Control tab offers a more visual and safer approach <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Overview**: The Source Control tab provides a breakdown of all changes in your current working directory <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Staging Files**: Point and click at files to stage them <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Icons indicate if a file has been modified, added, or removed <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Git Commands**: A drop-down menu provides a list of all possible [[using_vs_code_with_git | Git]] commands without needing to look them up <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Code Snippets

Custom code snippets allow you to quickly insert boilerplate code you frequently write <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Configuration**: Run the `Configure User Snippets` command from the Command Palette <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. You can create global snippets or scope them to an individual workspace by modifying a JSON file <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Insertion**: Use the `Insert Snippet` command to add your custom boilerplate <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Pre-built Snippets**: Before creating your own, check the [[using_extensions_to_enhance_vs_code_functionality | extensions]] panel, as pre-built snippets for popular frameworks are often available <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## File System Navigation

*   **Creating Nested Directories**: When creating a new file in the File Explorer, you can specify nested directories that don't yet exist by including slashes in the file name (e.g., `src/components/MyComponent/index.tsx`). VS Code will automatically create these directories <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Refactoring

*   **Safely Renaming Symbols**: Instead of using find and replace, which can be dangerous, right-click on the symbol you want to rename to find all its references or implementations <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Then, use the `Rename Symbol` option to safely rename it across all relevant files <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.