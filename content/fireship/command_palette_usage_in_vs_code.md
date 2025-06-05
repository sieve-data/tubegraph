---
title: Command Palette Usage in VS Code
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

The Command Palette in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] is a powerful feature that allows users to access virtually any command or file within the editor using only the keyboard <a class="yt-timestamp" data-t="01:50:56">[01:50]</a>. It significantly boosts productivity by reducing reliance on the mouse <a class="yt-timestamp" data-t="01:13:25">[01:13]</a>.

## Opening the Command Palette

To open the Command Palette, use the keyboard shortcut `Ctrl+P` (or `Cmd+P` on Mac) <a class="yt-timestamp" data-t="01:47:38">[01:47]</a>.

## Core Functionality

### File Navigation
By default, when opened, the Command Palette displays a list of recently opened files <a class="yt-timestamp" data-t="01:56:04">[01:56]</a>. You can quickly find a file in your project by simply typing its name, which is much faster than navigating through directories in the file explorer <a class="yt-timestamp" data-t="01:59:08">[01:59]</a>.

### Command Execution
To access and run any command available in [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]], type a right angle bracket `>` in the Command Palette <a class="yt-timestamp" data-t="02:09:05">[02:09]</a>. This includes commands for installed [[using_extensions_and_snippets_in_vs_code | extensions]] <a class="yt-timestamp" data-t="02:15:23">[02:15]</a>.

Examples:
*   Toggle the minimap <a class="yt-timestamp" data-t="02:18:24">[02:18]</a>.
*   Start or stop the [[using_extensions_and_snippets_in_vs_code | Quokka extension]] to execute JavaScript code directly in the file <a class="yt-timestamp" data-t="02:27:00">[02:27]</a>.

### Symbol Navigation
The Command Palette provides efficient ways to navigate through symbols (functions, interfaces, classes, etc.) within your code:

*   **Current File Symbols**: Type `@` (at symbol) in the Command Palette to list all symbols in the currently open file, allowing for quick navigation <a class="yt-timestamp" data-t="03:01:21">[03:01]</a>.
    *   Alternatively, you can bypass the Command Palette for current file symbols by pressing `Ctrl+Shift+Period` (or `Cmd+Shift+O` on Mac) <a class="yt-timestamp" data-t="03:08:02">[03:08]</a>.
*   **Project-wide Symbols**: To find a symbol throughout your entire project, including dependencies like `node_modules`, type `#` (hashtag) followed by the symbol's name <a class="yt-timestamp" data-t="03:19:07">[03:19]</a>.
    *   For long camel-cased class names, you only need to type the first character of each camel-cased word for the search to work <a class="yt-timestamp" data-t="03:28:01">[03:28]</a>.

## Advanced Usage

### Custom Snippets and Boilerplate Code
The Command Palette can be used to manage and insert [[custom_snippets_and_boilerplate_code_in_vs_code | custom code snippets]].
*   Run the "Configure User Snippets" command from the palette to create global or workspace-scoped snippets <a class="yt-timestamp" data-t="09:43:08">[09:43]</a>.
*   Once configured, use the "Insert Snippet" command to quickly add your custom boilerplate code <a class="yt-timestamp" data-t="09:57:48">[09:57]</a>.

### Running Tasks
Instead of manually typing commands in the [[terminal_and_git_integration_in_vs_code | integrated terminal]], you can define [[terminal_and_git_integration_in_vs_code | VS Code tasks]] in a `tasks.json` file <a class="yt-timestamp" data-t="07:22:18">[07:22]</a>. These tasks can then be executed automatically via the Command Palette <a class="yt-timestamp" data-t="07:30:19">[07:30]</a>.