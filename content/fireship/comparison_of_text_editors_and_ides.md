---
title: Comparison of text editors and IDEs
videoId: 8PhdfcX9tG0
---

From: [[fireship]] <br/> 
Code editors are fundamental [[developer_productivity_tools | developer productivity tools]] that have evolved significantly since the first computer bug was discovered by Grace Hopper on September 9, 1947, when a real moth found its way onto the Harvard Mark II Aiken Relay Calculator's number 70 relay <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Early innovations like undo, find and replace, and copy and paste were revolutionary in the 1960s, made possible by the computer screen and visual terminal, eventually replacing punch cards where a single error meant starting over <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

The search for the "best" code editor in the 2020s involves exploring a range of tools, from basic command-line editors to advanced cloud-based Integrated Development Environments (IDEs) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Command-Line Text Editors

These editors primarily rely on a text user interface, often launched directly from the terminal.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]
[[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]], written by Bill Joy and released in 1976, remains a standard tool on most Linux distributions <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Keyboard-based and Modal:** It's primarily a keyboard-based editor where the mouse has no useful function, largely because mice didn't go mainstream until the Apple Macintosh in 1984 <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]] is a modal editor, meaning keys perform different functions based on the current mode (e.g., "insert mode" for writing text, "command mode" for actions) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Efficiency:** Once accustomed to its commands, editing can be very fast; for example, `dd` deletes an entire line, and `3dd` deletes three lines without needing a mouse highlight <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Limitations:** It lacks features like syntax highlighting and the ability to implement plugins <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]]
Around the same time, Guy Steele at MIT created [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]] (Editor Macros) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Extensible IDE:** Like [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]], it's keyboard-based but is highly extensible, integrating features like debuggers, a file manager, a terminal emulator, and even a music player, acting as a full-blown Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This extensibility means more initial configuration time <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Non-modal:** [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]] is a non-modal editor, which can feel more user-friendly as it avoids different modes <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Complexity:** It requires using many modifier keys, which can lead to "Emacs pinky" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, and has over 10,000 built-in commands for customization and automation <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **"Cults":** The philosophical differences between [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]] and [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]] have led to "the cult of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]" and "the church of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]]" (founded by Richard Stallman), a long-standing rivalry <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] (Vi Improved)
Released in 1991, [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] is a superset of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]'s core functionality <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Popularity & Features:** It's more popular among developers as a daily editor due to essential features like syntax highlighting, multi-level undo, and plugins <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Learning Curve:** While initially annoying, learning [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] keeps fingers on the home row, improving coding speed over time, and it also supports code completion like a regular IDE <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.## [[History of code editors | The Evolution of Code Editors]]

The journey of code editors began long before modern software. The first official computer bug was discovered by Grace Hopper at 3:45 PM on September 9, 1947, when a real moth was found on the number 70 relay of the Harvard Mark II Aiken Relay Calculator <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Today's programmers create their own bugs, but this wouldn't be possible without a [[modern_code_editors_like_visual_studio_code_and_jetbrains | modern code editor]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

In the 1960s, features like undo, find and replace, and copy and paste were revolutionary, made possible by the computer screen and visual terminal <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. These advancements eventually replaced punch cards, where a single wrong keystroke meant starting over from scratch <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This article explores the evolution of code editors from basic command-line tools to advanced cloud-based Integrated Development Environments (IDEs) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Command-Line Text Editors

These editors are primarily text-user interface (TUI) based, often launched from the terminal.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]
[[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]], written by Bill Joy, was released in 1976 and remains a standard tool on most Linux distributions <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Keyboard-Based and Modal:** It's primarily a keyboard-based editor where the mouse has no useful function, a design choice influenced by the mouse not becoming mainstream until the Apple Macintosh in 1984 <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]] is a modal editor, meaning keys perform different actions depending on the active mode (e.g., "insert mode" for typing, "command mode" for operations) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Efficiency:** With practice, [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]] can be very fast for editing. For example, `dd` deletes an entire line, and `3dd` deletes three lines at once without needing to highlight with a mouse <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Limitations:** It lacks features like syntax highlighting and the ability to implement plugins for extended functionality <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]]
Around the same period, Guy Steele at MIT created [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]], which stands for Editor Macros <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Extensible IDE:** Like [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]], it's primarily keyboard-based but is highly extensible. It integrates features such as debuggers, a file manager, a terminal emulator, and even a music player, making it a full-blown Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This extensibility, however, requires significant initial configuration <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Non-modal:** [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]] is a non-modal editor, which can feel more user-friendly as it doesn't require understanding different modes <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Complexity:** It requires extensive use of modifier keys, which can lead to a repetitive strain injury known as "Emacs pinky" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It boasts over 10,000 built-in commands for customization and automation <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **"Cults":** The philosophical differences between [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]] and [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]] have led to two distinct factions: "the cult of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]" and "the church of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Emacs]]," founded by high priest Richard Stallman <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] (Vi Improved)
Created in 1991, [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] is a superset of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vi]]'s core functionality <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Popularity & Features:** [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] is more popular among developers for daily use, offering essential features like syntax highlighting, multi-level undo, and plugins <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Learning Curve:** While initially challenging, learning [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] helps keep fingers on the keyboard's home row, potentially improving coding speed <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. It also provides code completion features similar to a regular IDE <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Neovim
Neovim, a popular fork of [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] released in 2015, addresses some of its perceived shortcomings <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Performance and Scripting:** Neovim is faster than [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]] <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> and replaces [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]]'s native scripting language, Vimscript, with Lua, a fast and proven language also used by platforms like Roblox <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Nano
Nano, part of the GNU project, was released in 1999 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **User-Friendly:** It's a keyboard-based editor launched from the command line, but unlike [[features_of_popular_code_editors_like_vi_vim_and_emacs | Vim]], it's non-modal and has a much gentler learning curve <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Keybindings are displayed at the bottom of the screen, making it easy to learn essential commands like how to exit (`Ctrl+X`) <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Simplicity:** While it lacks features needed for a full-blown IDE, it's excellent for quickly editing files from the terminal on most machines <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Graphical User Interface (GUI) Editors

The majority of developers today use editors with a graphical user interface, making them more visually intuitive.

### Notepad
Notepad on Windows, released in 1983, was one of the earliest GUI programs <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. It was designed to commercialize the mouse for MS-DOS <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Mouse Interaction:** Users could simply click to place the cursor or click, hold, and drag to highlight text, which was a groundbreaking feature in the early 1980s <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Notepad++
Notepad++ is a more modern version of Notepad designed for programmers <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Features:** It supports macros and plugins, allowing it to function as a primary development environment <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Adobe Dreamweaver
Adobe Dreamweaver was once a very popular tool for [[comparison_of_web_development_frameworks | web development]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Limitations:** Despite its visual appeal, it can feel slow and overly complex, like much of Adobe software <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. It's considered antiquated, with first-class support for older technologies like jQuery and Bootstrap, making it a poor choice for commercial use in 2022 <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### [[modern_code_editors_like_visual_studio_code_and_jetbrains | Visual Studio Code (VS Code)]]
[[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] is currently the most popular lightweight editor <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Approachability and Shortcuts:** It features a graphical user interface that is very approachable for beginners, while also offering numerous built-in shortcuts for quick actions, similar to text-based editors <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **[[VS_Code_Extensions_for_Productivity | Extension Ecosystem]]:** A major benefit of [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] is its popularity and vast [[VS_Code_Extensions_for_Productivity | extension ecosystem]], ensuring support for various tooling like Tailwind CSS <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Technology & Customization:** The application is open source and built with Electron, based on web technologies, making it easy for web developers to extend <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. While it has a reputation as a memory hog, it can be configured for a minimal editing experience (Zen Mode) or as a full-blown IDE, capable of remote file editing on GitHub, cloud resource connection, and Docker container interaction <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Integrated Development Environments (IDEs)

IDEs are comprehensive toolsets designed for specific types of application development.

### Platform-Specific IDEs
For specific platforms, dedicated IDEs are often the optimal choice:
*   **Xcode:** For building iOS apps, Apple's integrated development environment, Xcode, is typically used <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Android Studio:** For Android apps, Google's Android Studio is the preferred IDE <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Visual Studio:** Microsoft's Visual Studio is a true IDE offering a comprehensive set of tools for developing desktop, web, and server-side applications with the .NET framework <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It provides powerful code completion, refactoring, and debugging tools for core languages like C++ and C# <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. While initially overwhelming with its numerous tools and wizards, these become invaluable during complex projects <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. IDEs excel when committed to a specific platform <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### [[modern_code_editors_like_visual_studio_code_and_jetbrains | JetBrains]]
[[modern_code_editors_like_visual_studio_code_and_jetbrains | JetBrains]] offers a family of editors and IDEs considered the gold standard for professional coding <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Products:** Their most well-known product is IntelliJ for Java development <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Webstorm is their IDE for [[comparison_of_web_development_frameworks | web development]] <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Cost & Features:** While [[modern_code_editors_like_visual_studio_code_and_jetbrains | JetBrains]] products come with a cost (e.g., ~$69/year), they offer a more polished and reliable experience, with less need to install numerous plugins <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Webstorm, for instance, includes a wizard for project setup, though some options like Meteor, Cordova, and Angular.js v1 are outdated <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Code Refactoring:** A notable feature is its robust code refactoring. In a React app, for example, a UI element can be easily extracted into its own named component, a function that feels more reliable in Webstorm compared to [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] with extensions <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Fleet:** [[modern_code_editors_like_visual_studio_code_and_jetbrains | JetBrains]] is also developing a new editor called Fleet, intended as a competitor to [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## [[Future trends in cloudbased code editing | The Future of Code Editing]]

The industry is moving towards [[future_trends_in_cloudbased_code_editing | entirely cloud-based code editors]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Browser-Based Options:** [[modern_code_editors_like_visual_studio_code_and_jetbrains | VS Code]] can already be run in a browser via vscode.dev <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **Cloud Hardware:** GitHub Codespaces allows developers to edit code on powerful cloud hardware <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **WebAssembly:** Tools like StackBlitz use WebAssembly to run full-stack web applications directly in the browser <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.