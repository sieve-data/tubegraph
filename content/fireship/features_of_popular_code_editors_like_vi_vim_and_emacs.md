---
title: Features of popular code editors like vi vim and emacs
videoId: 8PhdfcX9tG0
---

From: [[fireship]] <br/> 

Computer programmers frequently create their own bugs, a process made possible by [[modern_code_editors_like_visual_studio_code_and_jetbrains | modern code editors]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The [[History of code editors | history of code editors]] reveals how these tools have evolved over 50 years <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Features like undo, find and replace, and copy and paste, now commonplace, were revolutionary in the 1960s, made possible by the computer screen and visual terminal <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. These innovations eventually replaced punch cards, where a single wrong keystroke required starting over <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Vi

Vi was written by Bill Joy and released in 1976 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It remains a standard tool on most Linux distributions today, accessible by typing `vi` into the terminal <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Keyboard-Based and Modal Operation
Vi is a keyboard-based editor where the mouse has no useful function <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This design predates the mainstream adoption of the mouse, which occurred with the Apple Macintosh in 1984 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Vi is a modal editor, meaning keys perform different actions depending on the current mode <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. To type text, a user must enter "insert mode" by pressing the `i` key <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. After adding code, pressing `escape` returns to "command mode," where commands like "write quick" can save the file <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Efficiency and Limitations
Once mastered, vi can be very fast for code editing <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For example, `dd` deletes an entire line, and `3d` deletes three lines at once, without needing mouse highlighting <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. The challenge lies in memorizing its numerous commands <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Vi is simple but lacks essential features like syntax highlighting or the ability to implement plugins for extended functionality <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It is associated with the "cult of vi" faction in the developer community <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Emacs

Emacs, standing for "Editor MACROS," was created by Guy Steele at MIT around the same time as vi <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Extensibility and Features
Like vi, Emacs is primarily a keyboard-based editor <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. However, it is highly extensible and integrates additional features such as debuggers, a file manager, terminal emulator, and even a music player <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. It functions not merely as a text editor but as a full-blown [[Comparison of text editors and IDEs | integrated development environment]] (IDE) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This extensibility means it can do more but requires significant initial configuration <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### User Experience
Emacs can feel more user-friendly than vi <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. It allows users to pull up a menu to navigate commands and is a non-modal editor, eliminating the need to understand different modes <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. However, it requires extensive use of modifier keys, which can lead to a repetitive strain injury known as "Emacs pinky" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Emacs is complex, with over 10,000 built-in commands used to create macros for customization and automation <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. It is associated with the "church of Emacs," founded by Richard Stallman <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Vim

Vim, or "Vi Improved," is a superset of vi's core functionality, sharing a similar feel <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Created in 1991, it is more popular among developers for daily use <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Enhanced Features
Vim provides essential features missing in vi, such as syntax highlighting, multi-level undo, and a robust plugin system for customization <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. It is more developer-friendly, offering a "vim tutor" command to learn the basics <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Coding Speed and Completion
While initially annoying, mastering Vim allows users to keep their fingers on the home row of the keyboard, potentially improving coding speed over time <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. It also provides code completion features, similar to a regular [[Comparison of text editors and IDEs | IDE]] <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Neovim: A Modern Fork
Neovim is a popular fork of Vim that emerged in 2015, addressing some of Vim's limitations <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. It offers faster performance <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. A key improvement in Neovim is the embedding of Lua as its scripting language, replacing VimScript, which some consider problematic <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Lua is a fast and proven language used by platforms like Roblox <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.