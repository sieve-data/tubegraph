---
title: VS Code keyboard shortcuts and commands
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

Visual Studio Code (VS Code) is a powerful tool, often compared to a "knife" that is "only as good as the hands that wield it" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it may appear as a simple text editor, it contains numerous [[productivity_tips_for_visual_studio_code | productivity-boosting features]] that can significantly speed up code writing and analysis <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The key to unlocking its full potential lies in leveraging its keyboard shortcuts and command-line interface (CLI) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Opening Projects with the CLI

While it's common to open a directory by using the file explorer and selecting "Open with VS Code," a much quicker method is to use the VS Code CLI <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. From the terminal, you can quickly open a directory or edit a file using the `code` command <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. On Mac or Linux, you must first add the VS Code binary to your system's path for this to work <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Embracing a Keyboard-First Approach

A core [[productivity_tips_for_visual_studio_code | productivity secret]] in VS Code is to reduce reliance on the mouse <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Although VS Code is approachable due to its mouse support for nearly every action, it's not the most efficient way to work <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. While not requiring you to learn something as extensive as [[vim_navigation_and_keyboard_shortcuts | Vim]] or Emacs, understanding that almost any mouse action can be performed faster with the keyboard is crucial <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Memorizing even 10 to 20 key shortcuts can significantly enhance your workflow <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## The Command Palette

The most important shortcut to learn is `Control + P` (or `Cmd + P` on Mac), which opens the Command Palette <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This feature provides access to nearly all of VS Code's power directly from the keyboard without needing to memorize countless keybindings <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Key functions of the Command Palette:
*   **Recent Files**: By default, it lists recently opened files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **File Search**: Type a file name to quickly find it within your project, which is faster than navigating through directories in the file explorer <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Execute Commands**: Type `>` (a right-angle bracket) to access virtually any command available in VS Code, including commands from [[using_extensions_to_enhance_vs_code_functionality | installed extensions]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Examples include toggling the minimap <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## [[efficient_navigation_and_code_editing_in_vs_code | Navigation and Searching]]

*   **Symbols in Current File**: When working in a large file, avoid scrolling <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. While `Control + F` (or `Cmd + F`) can find text on the page <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, a better approach is to use `@` (the at symbol) in the Command Palette to list all symbols in the current code, allowing for quick navigation <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. You can also bypass the Command Palette and use `Control + Shift + .` (or `Cmd + Shift + .`) to do this directly <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Symbols Across Project/Dependencies**: To find a symbol throughout the entire project, including dependencies like `node_modules`, use `#` (the hashtag) followed by the symbol name in the Command Palette <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For long camel-cased names, you only need to type the first character of each word <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Go to Line**: To quickly move to a specific line, use `Control + G` (or `Cmd + G`) followed by the line number <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## [[efficient_navigation_and_code_editing_in_vs_code | Code Editing Techniques]]

*   **Basic Movement and Highlighting**:
    *   Use arrow keys to move character by character <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    *   Hold `Shift` while using arrow keys to highlight text <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Use `Control + Arrow` (or `Alt + Arrow`) to move word by word <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Highlighting a Word**: Place your cursor on a word and use `Control + D` (or `Cmd + D`) to highlight it for deletion or replacement <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Multi-Cursor Editing (Same Word)**: If the highlighted word appears multiple times, hitting `Control + D` (or `Cmd + D`) repeatedly will add cursors to each occurrence, allowing simultaneous editing <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Multi-Cursor Editing (Arbitrary Positions)**: Hold down `Alt` (or `Option`) and click at different points in the editor to set up multiple cursors <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This is useful for repetitive CSS properties or HTML tags <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Cutting a Line**: Place your cursor on a line and hit `Control + X` (or `Cmd + X`) to cut the entire line without highlighting <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Moving Lines**: Use `Alt + Up/Down Arrow` to move a line up or down <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Copying Lines**: Use `Alt + Shift + Up/Down Arrow` to duplicate and move a line <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Toggling Comments**: Highlight the desired code (e.g., using `Control + L` to highlight line by line) and then use `Control + /` (or `Cmd + /`) to toggle comments on the selected block <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Extensions Enhancing Editing
*   **Auto Rename Tag**: Automatically renames the corresponding closing HTML tag when you edit the opening tag <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. It works in other languages beyond HTML as well <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Quokka.js**: An extension that runs JavaScript code in the background and appends the output directly into the editor, facilitating rapid prototyping <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. It can be started and stopped via the Command Palette <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Add JSDoc Comments**: After highlighting a function, use the Command Palette to automatically add JSDoc comments <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. JSDoc comments can include `@link` tags to connect to other symbols in your source code, allowing for quick navigation by clicking the link <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Better Comments**: Provides automatic highlighting for comment text. For example, lines starting with `!` can appear red, and `TODO`s can be highlighted orange <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## Terminal Integration

VS Code offers robust integrated terminal capabilities <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Open Terminal**: Use `Control + Backtick` (`` ` ``) to open a new terminal session in your current working directory <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Change Shell**: If needed, you can select a different default shell like PowerShell or WSL (Windows Subsystem for Linux) from the caret icon <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Manage Multiple Sessions**: For multiple terminal sessions (e.g., test runner, dev server), you can click the icon to rename or change the color of each session for better organization <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.*   **Navigate Terminal Commands**: Use `Control + Arrow` to quickly navigate within a typed command in the terminal line <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The mouse won't work for this <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Clear Terminal**: Use `Control + K` to clear the terminal <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Recall Last Command**: After clearing, use the `Up Arrow` to recall the last command from your history <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **VS Code Tasks**: To avoid repeatedly typing common commands like `npm run build` or `npm run test`, create a [[productivity_tips_for_visual_studio_code | VS Code task]] <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. A task is a JSON configuration containing a command to run in the terminal <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Once configured, you can run it directly from the Command Palette <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## [[version_control_and_remote_development_in_vs_code | Version Control and Remote Development]]

While [[using_vs_code_with_git | Git commands]] can be complex and dangerous to type manually <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>, VS Code offers a visual interface for [[using_vs_code_with_git | Git]].
*   **Source Control Tab**: The Source Control tab in VS Code provides a breakdown of all changes in your current working directory <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Staging Files**: You can point and click to stage files, and icons next to each file indicate if it's modified, added, or removed <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Git Commands Menu**: A dropdown menu lists all possible [[using_vs_code_with_git | Git commands]], eliminating the need to look them up <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **GitLens Extension**: For complex projects with multiple developers, the [[using_extensions_to_enhance_vs_code_functionality | GitLens extension]] provides advanced ways to visualize and explore your code, including blame information <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Remote Development Extensions
Microsoft provides extensions for [[version_control_and_remote_development_in_vs_code | remote development]] that transform VS Code into a full-blown Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Remote Repositories**: This extension allows you to open a Git repository directly from GitHub without cloning it locally <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. You can create branches, edit code, and submit pull requests directly within VS Code <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Remote SSH**: Connect to a remote server via SSH <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Remote Containers**: Use a Docker container as your development environment instead of your local system <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

## Code Snippets

To avoid writing the same boilerplate code repeatedly, you can create custom snippets <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Configure User Snippets**: Run the "Configure User Snippets" command from the Command Palette <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Scope**: Snippets can be global (for all projects) or scoped to an individual workspace <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Creation**: Modify a JSON file with the code you want to insert <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Usage**: Use the "Insert Snippet" command to quickly add your custom boilerplate <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Pre-built Snippets**: Check the [[using_extensions_to_enhance_vs_code_functionality | extensions]] panel for pre-built snippets for popular frameworks before creating your own <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Other Productivity Enhancements

*   **Create Nested Directories with Files**: When creating a new file in the file explorer, you can automatically create any nested directories by simply including slashes in the file name (e.g., `src/components/MyComponent.js`) <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Paste JSON as Code Extension**: This extension simplifies converting JSON objects into TypeScript types by inferring types using a tool called "Quick Type," potentially saving hours of work <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Safe Renaming of Symbols**: Instead of using find-and-replace, which can be dangerous <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>, right-click on the symbol you want to rename to "Find All References" or "Implementations" <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Then, use the "Rename Symbol" option to safely rename it across all relevant files <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.