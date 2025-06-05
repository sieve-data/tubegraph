---
title: Setting up Vim within Visual Studio Code
videoId: -txKSRn0qeA
---

From: [[fireship]] <br/> 

Vim is a keyboard-based text editor for writing code, based on the original Unix text editor `vi` which emerged in 1976. Vim itself followed in 1991 with numerous improvements <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While modern Integrated Development Environments (IDEs) are prevalent, Vim focuses on keeping your fingers "glued to the keyboard" to avoid productivity decline caused by mouse usage <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

Learning Vim can be challenging initially, akin to learning an instrument, but it leads to more precise and productive code editing <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Why Learn Vim?

[[introduction_to_vim_as_a_text_editor | Learning Vim]] is considered an "evergreen skill," meaning the knowledge gained will remain valuable throughout a developer's career <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. It enables developers to work faster and more efficiently within their editor <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. With Vim, more actions can be performed directly from the keyboard, reducing editing time and increasing coding time <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Initial Vim Survival Guide (Outside VS Code)

Vim runs in the terminal and is pre-installed on most machines <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. If you accidentally find yourself in Vim outside of VS Code:
*   To close an unmodified file, type `:q` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   To discard changes and quit, use `:q!` <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   To write changes and then quit, use `:wq` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[using_extensions_to_enhance_vs_code_functionality | Setting Up Vim in VS Code]]

To get the benefits of Vim without leaving VS Code <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, follow these steps:

### 1. Install the Vim Extension
*   Open VS Code and navigate to the Extensions panel <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   Search for "Vim" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   Look for the extension named "Vim" by "vscode-vim.vim" with approximately 2 million installations <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   Install this extension <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### 2. Enable Key Repeat (macOS specific instructions given)
Key repeat allows a key press to continue repeating its action if held down, which is handy for Vim navigation <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Go to Google and search for "vs code vim github" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   Locate the GitHub repository "vscode-vim/vim" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Scroll down to the "Installation" section <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   Find and run the instructions for enabling key repeat for your operating system in the terminal (e.g., for macOS) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Restart VS Code for the changes to take effect <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### 3. Verify Setup
*   Create a new file in VS Code <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   Observe that your cursor is a bit wider than default <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Press `i` to enter Insert Mode <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Hit `Return` multiple times <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   Press `Escape` to return to Normal (Command) Mode <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Hold down `k` and observe if the cursor moves smoothly upwards <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. If it moves smoothly, key repeat is enabled <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

Within VS Code, you still have access to your mouse, and you don't have to worry about getting stuck in Vim because you are using Vim keybindings, not the standalone Vim editor <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## [[efficient_navigation_and_code_editing_in_vs_code | Essential Vim Commands]]

Vim operates in different modes:
*   **Normal Mode (Command Mode)**: For navigation and issuing commands <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Insert Mode**: For typing text into the document <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Visual Mode**: For selecting text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Command Line Mode**: For running commands (e.g., `:set number`) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Basic Navigation and Editing

*   **Entering Insert Mode**:
    *   `i`: Insert text at the current cursor position <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   `I` (Shift + i): Insert text at the beginning of the current line <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   `a`: Append text after the current cursor position <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   `A` (Shift + a): Append text at the end of the current line <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Exiting Insert Mode**: `Escape` key to return to Normal Mode <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Movement (Normal Mode)**:
    *   Arrow keys: Move around the text <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   `h`: Move left <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   `j`: Move down <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   `k`: Move up <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   `l`: Move right <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   *Mnemonic aids*: `k` for kicking up, `j` for jumping down; `h` for going home (left), `l` for right <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>, <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The keys' physical position on the keyboard (h left of j/k, l right of j/k) also helps <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Deletion (Normal Mode)**:
    *   `x`: Delete the character under the cursor <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   `dd`: Delete the entire line <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Undo (Normal Mode)**: `u`: Undo the last change <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Replace Character (Normal Mode)**: `r`: Replace the character under the cursor with the next character typed <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>, <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Line Numbers (Command Line Mode)**: `:set number`: Add line numbers to the document <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Navigate to Line (Command Line Mode)**: `:number`: Navigate to a specific line number <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Paste from System Clipboard (Command Line Mode)**: `+p`: Paste content from the system clipboard <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Save File (Command Line Mode)**: `:w`: Save the current file <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Run Shell Command (Command Line Mode)**: `:! [shell_command]`: Run a shell command directly from Vim <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## [[productivity_tips_for_visual_studio_code | Productivity Tips]] for Vim

*   **Remap Caps Lock to Escape**: Many Vim users remap their Caps Lock key to act as the Escape key. This makes the Escape key much more accessible, being closer to the pinky finger than the default location in the corner of the keyboard <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This is encouraged for serious Vim learners <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Learn More

For those interested in [[advanced_vim_commands_and_customization | advanced Vim commands]] and integrating Vim further into VS Code, resources like the "Vim for VS Code" course are available, which offer exercises and cover 22 different commands <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.