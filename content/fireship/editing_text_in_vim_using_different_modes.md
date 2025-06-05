---
title: Editing text in Vim using different modes
videoId: -txKSRn0qeA
---

From: [[fireship]] <br/> 

[[introduction_to_vim_as_a_text_editor | Vim]] is a keyboard-based text editor used for writing code, designed to keep a developer's fingers on the keyboard to maximize productivity <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It is based on the original Unix text editor `vi` (1976), with [[introduction_to_vim_as_a_text_editor | Vim]] (Vi IMproved) following in 1991 <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Learning [[introduction_to_vim_as_a_text_editor | Vim]] can be challenging initially, but it leads to more precise and productive code editing <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. [[introduction_to_vim_as_a_text_editor | Vim]] is an evergreen skill, meaning the knowledge gained will last throughout a career <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Basic Operations and Modes

[[introduction_to_vim_as_a_text_editor | Vim]] typically runs in the terminal and is installed on most machines <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. When using [[introduction_to_vim_as_a_text_editor | Vim]], you toggle between different modes depending on the task <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The primary modes are:

*   **Normal Mode:** The default mode for navigation and executing commands.
*   **Insert Mode:** For typing and adding text.
*   **Visual Mode:** For selecting blocks of text.
*   **Command Line Mode:** For executing commands preceded by a colon (`:`).

### Exiting Vim

If you find yourself accidentally in [[introduction_to_vim_as_a_text_editor | Vim]] without knowing how to escape <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:

*   `:q` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>: Closes an unmodified file.
*   `:q!` <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>: Throws away changes and quits.
*   `:wq` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>: Writes (saves) the changes and then quits.

### Saving a File and Running Commands

*   `:w` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>: Saves the current file.
*   `:!command` <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>: Runs a shell command directly from [[introduction_to_vim_as_a_text_editor | Vim]].

## Navigation and Editing in Normal Mode

In **Normal Mode**, you can navigate and perform actions without directly typing into the document.

### Navigation

You can move around text using arrow keys or the following keyboard shortcuts <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a> <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>:

*   `h`: Move left <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   `j`: Move down <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   `k`: Move up <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   `l`: Move right <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

The placement of these keys on the keyboard (h left of j/k, l right of j/k) can help remember their function <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Basic Editing Commands

While in Normal Mode, you can perform quick edits:

*   `x`: Deletes the character under the cursor <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   `dd`: Deletes an entire line <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   `u`: Undoes the last action <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   `+p` (or `"+p`): Pastes content from the system clipboard <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   `r` (followed by a character): Replaces the character under the cursor with the new character typed <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This is done without leaving Normal Mode <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Command Line Mode for Configuration

To add line numbers, enter Command Line Mode by typing `:` then the command:

*   `:set number` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>: Adds line numbers to the display.
*   `:number` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>: Navigates to a specific line number.

## Entering and Exiting Insert Mode

To type text directly into the document, you must switch to **Insert Mode**. Pressing the `Escape` key returns you to **Normal Mode** <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

Common ways to enter Insert Mode:

*   `i`: Inserts text *before* the cursor's current position <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   `I` (Shift + `i`): Inserts text at the beginning of the current line <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   `a`: Inserts text *after* the cursor's current position <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   `A` (Shift + `a`): Appends text to the end of the current line <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Remapping Caps Lock to Escape

Many [[advanced_vim_commands_and_customization | Vim]] users remap their Caps Lock key to function as the Escape key. This makes the Escape key more accessible, as it is closer to the home row, improving efficiency <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## [[setting_up_vim_within_visual_studio_code | Vim]] within [[efficient_navigation_and_code_editing_in_vs_code | Visual Studio Code]]

You do not need to abandon [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] to gain the benefits of [[introduction_to_vim_as_a_text_editor | Vim]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. You can leverage [[introduction_to_vim_as_a_text_editor | Vim]]'s functionality directly within [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] using an extension <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This allows you to perform more actions from the keyboard, reducing mouse usage and increasing coding time <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Setting Up the Vim Extension

1.  Open the Extensions panel in [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Search for "vim" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  Install the extension named "Vim" by "vscodevim.vim", which typically has millions of installations <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Enabling Key Repeat

For a smoother [[advanced_vim_commands_and_customization | Vim]] experience in [[efficient_navigation_and_code_editing_in_vs_code | VS Code]], especially for new users, enable key repeating <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This allows keys like `j` (move down) or `k` (move up) to repeat their action when held down <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

Instructions for enabling key repeat can be found on the `vscode-vim/vim` GitHub repository <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. After running the appropriate command for your operating system (e.g., Mac) in the terminal, restart [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] for changes to take effect <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

*   To verify key repeat: Create a new file, hit `i` to enter Insert Mode, hit `Return` multiple times, then `Escape`. Hold `k` to see if the cursor moves smoothly upwards <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### No Fear of Getting Stuck

When using [[introduction_to_vim_as_a_text_editor | Vim]] inside [[efficient_navigation_and_code_editing_in_vs_code | VS Code]], you are primarily using [[advanced_vim_commands_and_customization | Vim]] keybindings. You still have access to your mouse and can close files or navigate normally, so there's no need to fear getting stuck in [[introduction_to_vim_as_a_text_editor | Vim]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

For more in-depth learning, consider exploring courses like "Vim for VS Code" which offers exercises and teaches additional commands <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.