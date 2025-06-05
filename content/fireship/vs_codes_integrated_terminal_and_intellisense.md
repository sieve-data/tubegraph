---
title: VS Codes integrated terminal and Intellisense
videoId: u21W_tfPVrY
---

From: [[fireship]] <br/> 

Visual Studio Code (VS Code) has rapidly become the most popular code editor among developers due to its minimal design, powerful features, and open-source nature <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Two key features that enhance productivity are its integrated terminal and robust IntelliSense capabilities.

## Integrated Terminal

VS Code includes an integrated command line [[Terminal and Git Integration in VS Code | terminal]] that can be accessed in several ways:
*   By dragging from the bottom of the screen <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
*   Using the `Ctrl + Backtick` [[VS Code Keyboard Shortcuts | key binding]] <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.
*   Opening the [[Command Palette Usage in VS Code | command palette]] with `Ctrl + P` and searching for "terminal" <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.

A notable feature of the integrated terminal is its ability to automatically recognize scripts set up in your project <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. For JavaScript projects, this includes scripts configured with NPM, Grunt, or Gulp <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. You can simply type `NPM`, and it will display all available scripts, allowing you to run them directly without manual typing <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

## IntelliSense

[[Intellisense]] is VS Code's term for code auto-completion <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. It provides powerful developer tooling, especially when working with strongly typed languages like TypeScript <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. While IntelliSense often appears automatically, you can manually trigger it with `Ctrl + Space` <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

Key functionalities of IntelliSense include:

*   **Viewing File Definitions**
    To see all methods, classes, interfaces, and properties defined within a large file, open the [[Command Palette Usage in VS Code | command palette]] (`Ctrl + P`) and type the `@` symbol <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

*   **Peeking Definitions**
    Instead of opening multiple files to find type definitions, you can click on an interface and select "Peak Definition". This will display the definition within your current view, even if it's buried deep in `node_modules` <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

*   **Finding References**
    To identify all instances where an interface or symbol is referenced in your project, right-click on it and select "Find References" <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

*   **Renaming Symbols**
    If you need to rename a symbol, highlight it, then right-click and choose "Rename Symbol" or press `F2` <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This feature automatically updates all references to that symbol across every file in your project, offering a safer alternative to a standard find-and-replace action as it analyzes the actual code reference rather than just text <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This is another benefit of using strongly typed code <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Paste JSON as Code [[VS Code Extensions for Productivity | Extension]]
The "Paste JSON as Code" [[VS Code Extensions for Productivity | extension]] allows you to easily generate strong type definitions from JSON API responses <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. By copying a JSON example, pasting it into a file, and then using the "Paste JSON as Code" command from the [[Command Palette Usage in VS Code | command palette]], you can automatically create a set of interfaces that model the API response <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. This enables powerful developer tooling for any API, regardless of whether it natively provides type definitions <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.