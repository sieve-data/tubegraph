---
title: VS Code Keyboard Shortcuts
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

[[modern_code_editors_like_visual_studio_code_and_jetbrains | Visual Studio Code]] (VS Code) is a powerful tool, often compared to a knife, whose effectiveness depends on the user's skill <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it may appear as a simple text editor, it contains numerous productivity-boosting features <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Mastering keyboard shortcuts can significantly enhance your ability to write and analyze code faster, ultimately saving valuable time <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Embracing Keyboard-Driven Workflow

For maximum productivity in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]], reducing reliance on the mouse is crucial <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While the mouse makes the tool approachable, it's not the most efficient way to work <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Nearly every command in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] can be executed with a keyboard shortcut <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Memorizing 10 to 20 key shortcuts can drastically improve your workflow, and with practice, keyboard navigation becomes second nature <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Core Navigation and Editing Shortcuts

### Opening VS Code from the Command Line
Instead of using the file explorer, you can quickly open a directory or edit a file using the [[vs_codes_integrated_terminal_and_intellisense | VS Code CLI]] with the `code` command <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. On Mac or Linux, you may first need to add the binary to your system's path <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### The Command Palette
The first essential shortcut to learn is `Ctrl+P` (or `Cmd+P` on Mac), which opens the [[command_palette_usage_in_vs_code | Command Palette]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This feature provides access to virtually all of [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code's]] power via the keyboard without needing to memorize countless key bindings <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

*   **Recent Files**: By default, it lists recently opened files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **File Search**: Begin typing a file name to quickly locate it within your project, which is much faster than clicking through directories <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Accessing Commands**: Type a right angle bracket (`>`) to access nearly any command executable in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]], including commands from [[vs_code_extensions_for_productivity | installed extensions]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. For example, you can toggle the minimap or start/stop the Quokka extension for JavaScript execution <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Navigating Code Symbols
Instead of endlessly scrolling, use the [[command_palette_usage_in_vs_code | Command Palette]] to navigate code symbols:
*   **Symbols in Current File**: Type `@` in the [[command_palette_usage_in_vs_code | Command Palette]] to list every symbol in the current file, allowing for quick navigation <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. You can bypass the [[command_palette_usage_in_vs_code | Command Palette]] by using `Ctrl+Shift+Period` (or `Cmd+Shift+O` on Mac) directly in the file <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Symbols Across Project**: Use `#` followed by the symbol name in the [[command_palette_usage_in_vs_code | Command Palette]] to find an interface or other symbol throughout your entire project, including dependencies like `node_modules` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For long class names, typing just the first character of each camel-cased word will often suffice <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Efficient Code Editing
*   **Go to Line**: Use `Ctrl+G` (or `Cmd+G` on Mac) followed by the line number to quickly jump to a specific line <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Word-by-Word Navigation**: Once on a line, use `Ctrl+Arrow` (or `Alt+Arrow` on Mac) to move the cursor word by word <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Highlighting**: Hold down the `Shift` key while using arrow keys to highlight text character by character, or `Ctrl+Shift+Arrow` to highlight word by word <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Highlight and Select Word**: Position your cursor on a word and press `Ctrl+D` (or `Cmd+D` on Mac) to highlight it for deletion or replacement <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Multi-Line Editing (Same Word)**: Press `Ctrl+D` repeatedly to select all occurrences of the currently highlighted word, enabling simultaneous editing across multiple lines <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Multi-Cursor Editing (Mouse-Driven)**: Hold down `Alt` (or `Option` on Mac) and click at different points in the editor to set up multiple cursors <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. This is useful for repetitive tasks like writing CSS properties or editing HTML tags <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Cut Line**: With your cursor on a line, use `Ctrl+X` (or `Cmd+X` on Mac) to cut the entire line without needing to highlight it first <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Move Line**: Use `Alt+Up` or `Alt+Down` (or `Option+Up/Down` on Mac) to move the current line up or down quickly <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Copy and Move Line**: Use `Alt+Shift+Up` or `Alt+Shift+Down` (or `Option+Shift+Up/Down` on Mac) to duplicate the current line and move the copy <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Toggle Comments**: Highlight code (e.g., using `Ctrl+L` to select line by line) then use `Ctrl+Forward Slash` (or `Cmd+Forward Slash` on Mac) to toggle comments on the selected lines <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Integrated Terminal Shortcuts
[[vs_codes_integrated_terminal_and_intellisense | VS Code's integrated terminal]] is highly functional:
*   **Open Terminal**: Use `Ctrl+Backtick` (or `Cmd+Backtick` on Mac) to open a new terminal session in your current working directory <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Navigate Terminal Text**: Use `Ctrl+Arrows` (or `Alt+Arrows` on Mac) to navigate word by word within the terminal's input text <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Clear Terminal**: Use `Ctrl+K` (or `Cmd+K` on Mac) to clear the terminal output <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Previous Command**: Press the `Up Arrow` key to cycle through your command history <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Enhancing Productivity with Extensions and Snippets

### Extensions Enhancing Keyboard Use
While not direct keyboard shortcuts, these [[vs_code_extensions_for_productivity | extensions]] enhance keyboard-driven workflows:
*   **Auto Rename Tag**: Automatically renames the closing HTML tag when you edit the opening one, and works in other languages too <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Add JSDoc Comments**: After highlighting a function, use the [[command_palette_usage_in_vs_code | Command Palette]] to automatically add a JSDoc comment <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. JSDoc comments can include link tags to connect to other symbols in your source code, making documentation interactive <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Better Comments**: Provides automatic highlighting for comment text, e.g., turning lines starting with `!` red and `TODO` items orange <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **GitLens**: Offers enhanced visualization and exploration of [[git_version_control_and_collaboration_tools_in_vs_code | Git]] history <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Remote Repositories / Remote SSH / Remote Containers**: These [[vs_code_extensions_for_productivity | Microsoft extensions]] enable [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] to work directly with GitHub repos, remote servers via SSH, or Docker containers as development environments, turning the editor into a full integrated development environment (IDE) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Paste JSON as Code**: For TypeScript users, this [[vs_code_extensions_for_productivity | extension]] can take a JSON object and automatically infer types using `quicktype`, saving hours of manual work <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Custom Snippets
For boilerplate code you write repeatedly, create [[custom_snippets_and_boilerplate_code_in_vs_code | custom snippets]]:
1.  Run the "Configure User Snippets" command from the [[command_palette_usage_in_vs_code | Command Palette]] <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
2.  Define global snippets or scope them to a specific workspace by modifying the JSON file <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
3.  Insert your custom boilerplate using the "Insert Snippet" command from the [[command_palette_usage_in_vs_code | Command Palette]] <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
Before creating your own, check the [[using_extensions_and_snippets_in_vs_code | extensions]] panel, as many popular frameworks already have pre-built snippets available <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Other Productivity Tips
*   **Create Nested Directories**: When creating a new file in the file explorer, you can create nested directories automatically by including slashes in the file name (e.g., `src/components/MyComponent/index.js`) <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Safe Renaming**: Instead of a dangerous find-and-replace, right-click on the symbol you want to rename, find all its references or implementations, then use the "Rename Symbol" option to safely rename it across all relevant files <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.