---
title: Advanced Vim commands and customization
videoId: -txKSRn0qeA
---

From: [[fireship]] <br/> 

[[introduction_to_vim_as_a_text_editor | Vim]] is a keyboard-based text editor designed for writing code, where navigation around the screen is primarily done with the keyboard rather than a mouse <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is based on the original Unix text editor `vi`, which originated in 1976 <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. [[introduction_to_vim_as_a_text_editor | Vim]] itself followed in 1991, introducing numerous improvements <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

The core philosophy behind [[introduction_to_vim_as_a_text_editor | Vim]] is to maximize a developer's productivity by keeping their fingers "glued to the keyboard at all times," as touching the mouse can reduce efficiency <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Learning [[introduction_to_vim_as_a_text_editor | Vim]] can be initially challenging, but this effort leads to more precise and productive code editing <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

[[introduction_to_vim_as_a_text_editor | Vim]] runs directly in the terminal and is pre-installed on most machines <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Basic Operations and Modes

[[editing_text_in_vim_using_different_modes | Vim]] operates with various modes, including Normal, Insert, Visual, and Command Line <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Exiting Vim

If you find yourself in [[introduction_to_vim_as_a_text_editor | Vim]] and need to exit <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:
*   `:q` - Closes an unmodified file <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   `:q!` - Discards any changes and quits <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   `:wq` - Writes (saves) the changes and then quits <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Opening Files

To open a file using [[introduction_to_vim_as_a_text_editor | Vim]], you typically use the command `vim filename` <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## [[vim_navigation_and_keyboard_shortcuts | Navigation and Editing Commands]]

### Basic Navigation

In Normal mode, you can move around the text using either the arrow keys or the letters `h`, `j`, `k`, and `l` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>:
*   `h` - Move left <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   `j` - Move down <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   `k` - Move up <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   `l` - Move right <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
These keys are positioned conveniently on the keyboard, with `h` to the left of `j` and `k`, and `l` to their right <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

You can also navigate to a specific line number using `:number` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Editing Text

[[editing_text_in_vim_using_different_modes | Vim]] provides several commands for inserting, deleting, and replacing text:

*   `i` - Enters Insert mode, allowing you to type into the document at the current cursor position <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   `I` (Shift + i) - Enters Insert mode at the beginning of the current line <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   `a` - Enters Insert mode immediately *after* the current cursor position <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   `A` (Shift + a) - Enters Insert mode at the very end of the current line <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   `x` - Deletes the character under the cursor <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   `dd` - Deletes an entire line <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   `r` - Replaces the character under the cursor with the next character typed <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This command allows for changes without leaving Normal mode <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   `u` - Undoes the last change <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

To return to Normal mode after making edits, press the `escape` key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Clipboard Operations

To paste content from the system clipboard into [[introduction_to_vim_as_a_text_editor | Vim]], use `+p` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Saving Files

To save changes to a file, use `:w` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Running [[shell_commands_and_bash_scripting | Shell Commands]]

You can run [[shell_commands_and_bash_scripting | shell commands]] directly from [[introduction_to_vim_as_a_text_editor | Vim]] using `:!` followed by the desired command <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## [[setting_up_vim_within_visual_studio_code | Vim in Visual Studio Code]]

You don't need to abandon [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] to gain the benefits of [[introduction_to_vim_as_a_text_editor | Vim]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. [[introduction_to_vim_as_a_text_editor | Vim]] is an "evergreen skill," meaning the knowledge remains valuable throughout your career, enabling faster and more efficient work within your editor <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. By using [[introduction_to_vim_as_a_text_editor | Vim]] key bindings in [[efficient_navigation_and_code_editing_in_vs_code | VS Code]], you gain the advantage of keyboard-driven efficiency without the risk of getting "stuck" in [[introduction_to_vim_as_a_text_editor | Vim]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Installing the Vim Extension

To enable [[introduction_to_vim_as_a_text_editor | Vim]] functionality in [[efficient_navigation_and_code_editing_in_vs_code | VS Code]]:
1.  Go to the [[using_extensions_to_enhance_vs_code_functionality | VS Code]] Extensions panel <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Search for "vim" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  Install the extension named "Vim" by `vscode-vim.vim`, which typically has around 2 million installations <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Setting Up Key Repeat

Key repeat is a useful feature for [[introduction_to_vim_as_a_text_editor | Vim]] beginners, allowing a key press to repeat its action (e.g., holding `j` to move down multiple lines) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
1.  Search Google for "vs code vim github" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Navigate to the `vscode-vim/vim` GitHub repository <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Scroll to the installation section for instructions on enabling key repeating for your operating system <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
4.  Run the provided command in your terminal <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
5.  Restart [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] for the changes to take effect <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
6.  To verify, create a new file, enter Insert mode with `i`, hit Return multiple times, then hit `escape` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Hold `k` and check if your cursor moves up smoothly <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Customization and Productivity Tips

### Remapping Caps Lock to Escape

Many [[introduction_to_vim_as_a_text_editor | Vim]] users remap their Caps Lock key to `escape` <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This makes the `escape` key more accessible, as it's closer to the pinky finger compared to the corner of the keyboard <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This remapping is highly recommended for those serious about learning [[introduction_to_vim_as_a_text_editor | Vim]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Displaying Line Numbers

To add line numbers to your document, run the command `:set number` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.