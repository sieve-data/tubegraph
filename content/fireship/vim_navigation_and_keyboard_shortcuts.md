---
title: Vim navigation and keyboard shortcuts
videoId: -txKSRn0qeA
---

From: [[fireship]] <br/> 

[[introduction_to_vim_as_a_text_editor | Vim]] is a keyboard-based text editor for writing code, emphasizing navigation without a mouse <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is an improved version of the original Unix text editor `vi`, which was created in 1976, with Vim itself following in 1991 <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The core philosophy behind Vim is to keep developers' fingers "glued to the keyboard at all times" to maximize productivity, as every time the mouse is touched, productivity declines <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

Learning Vim is compared to learning a musical instrument, being challenging initially but leading to more precise and productive code [[efficient_navigation_and_code_editing_in_vs_code | editing]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Vim is commonly found in the terminal and is installed on almost every machine <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Essential Vim Commands

### Exiting Vim

If you find yourself accidentally dropped into Vim, here's how to exit:
*   To close an unmodified file: Type `:q` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   To discard changes and quit: Type `:q!` <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   To write (save) changes and then quit: Type `:wq` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Vim Modes

Vim operates in different modes depending on the task:
*   **Normal Mode**: The default mode upon opening a file, used for navigation and executing commands <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Insert Mode**: Allows typing and modifying text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Visual Mode**: Used for selecting text.
*   **Command Line Mode**: Used for executing commands (e.g., saving, quitting, running shell commands).

To switch back to Normal Mode from any other mode, press the `escape` key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Basic Navigation

In Normal Mode, you can move around using:
*   **Arrow keys** <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **h**: Move left <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **j**: Move down <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **k**: Move up <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **l**: Move right <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

These keys (`h`, `j`, `k`, `l`) are positioned on the keyboard to be easily accessible from the home row, enhancing efficiency <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. You can still use your mouse to click and move around even when using Vim key bindings inside [[setting_up_vim_within_visual_studio_code | VS Code]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Editing Commands

#### Entering Insert Mode

To modify text, you must enter Insert Mode:
*   **i**: Enters Insert Mode at the current cursor position <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **I** (Shift+i): Enters Insert Mode at the beginning of the current line <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **a**: Enters Insert Mode *after* the current cursor position <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **A** (Shift+a): Enters Insert Mode at the end of the current line <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

#### Deleting and Replacing Text (Normal Mode)

You can make quick edits without entering Insert Mode:
*   **x**: Deletes the character under the cursor <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **dd**: Deletes the entire line <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **u**: Undoes the last change <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **r**: Replaces the character under the cursor with a new character <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

#### Other Handy Commands

*   **:+p**: Pastes content from the system clipboard <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **:w**: Saves the current file <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **:set number**: Adds line numbers to the document <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **:number**: Navigates to a specific line number (e.g., `:25` goes to line 25) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **:`shell_command`**: Runs a shell command directly from Vim (e.g., `:!npm start`) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Productivity Tips

*   **Key Repeat**: Enable key repeating for smoother navigation (e.g., holding `j` to continuously move down) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Instructions for this can typically be found in the documentation for Vim extensions in your editor <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Remapping Caps Lock to Escape**: Many Vim users remap their Caps Lock key to act as `escape`. This makes the `escape` key more accessible, as it's closer to the home row, allowing for quicker switching back to Normal Mode <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### [[setting_up_vim_within_visual_studio_code | Vim in VS Code]]

You don't need to abandon [[vs_code_keyboard_shortcuts_and_commands | VS Code]] to benefit from Vim's [[efficient_navigation_and_code_editing_in_vs_code | efficiency]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The VS Code Vim extension, specifically `vscodevim.vim`, allows you to leverage Vim's key bindings within your preferred IDE <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This means you can use the powerful keyboard-centric commands without the fear of getting "stuck" in Vim, as you still have access to all standard VS Code functionalities, including mouse interaction <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.