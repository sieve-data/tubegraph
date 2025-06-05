---
title: Introduction to Vim as a text editor
videoId: -txKSRn0qeA
---

From: [[fireship]] <br/> 

Vim is a text editor designed for writing code, where navigation is primarily done with the keyboard rather than a mouse <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is based on the original Unix text editor `vi`, which was created in 1976 <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Vim, or "vi improved," followed in 1991, introducing several enhancements <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Why Learn Vim?

In the age of modern Integrated Development Environments (IDEs), Vim offers distinct advantages for developers:
*   **Increased Productivity** When writing code all day, keeping your fingers on the keyboard at all times enhances [[Productivity tips for Visual Studio Code | productivity]], as every time you use the mouse, your workflow can be interrupted <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Precision and Efficiency** Learning Vim can be challenging initially, similar to learning a musical instrument, but this effort leads to more precise and productive code editing in the long run <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **Evergreen Skill** Vim is considered an "evergreen skill," meaning that once learned, the knowledge remains valuable throughout your career, allowing you to work faster and more efficiently within any editor <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>. A side-by-side comparison shows that Vim allows more actions to be performed from the keyboard, reducing editing time and increasing coding time <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Ubiquitous Presence** Vim runs in the terminal and is installed on almost every machine <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. You may even find yourself accidentally dropped into it with no obvious way to escape <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Basic Vim Interaction and Survival

Vim operates with different [[editing_text_in_vim_using_different_modes | modes]] for various tasks. When you open a file, you are typically in "normal mode" <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. You can toggle between modes like "insert," "visual," and "command line" depending on your objective <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

### Essential Commands
*   **Quitting Vim**
    *   To close an unmodified file: `:q` <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>
    *   To discard changes and quit: `:q!` <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>
    *   To write (save) changes and then quit: `:wq` <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>
*   **Saving a File**
    *   To save changes to a file: `:w` <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>
*   **Running Shell Commands**
    *   To run a program directly from Vim (e.g., a shell command): `:!` followed by the command (e.g., `:!python main.py`) <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>
*   **Pasting from System Clipboard**
    *   To paste content from your system clipboard: `+p` <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>

## [[Vim navigation and keyboard shortcuts | Vim Navigation]] and [[editing_text_in_vim_using_different_modes | Editing Basics]]

### Navigating Text
You can move around text using arrow keys or the letters `h`, `j`, `k`, and `l` <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. These keys are often preferred as they keep your hands on the home row.
*   `k`: Move cursor up (mnemonic: "kicking up" a soccer ball) <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>
*   `j`: Move cursor down (mnemonic: "jumping down") <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>
*   `h`: Move cursor left (mnemonic: "going home" to the left) <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>
*   `l`: Move cursor right <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>

You can also add line numbers for easier navigation:
*   To display line numbers: `:set number` <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>
*   To navigate to a specific line number: `:number` (e.g., `:10` to go to line 10) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>

### Basic Text Manipulation
*   `x`: Delete a single character at the cursor's position <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>
*   `dd`: Delete an entire line <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>
*   `u`: Undo the last action <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>
*   `r` + `new_char`: Replace the character under the cursor with `new_char` (e.g., `rh` replaces the character with 'h') <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>

### Entering and Exiting Insert Mode
To change text, you need to enter "insert mode," which frees up the keyboard for typing into the document <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   `i`: Enter insert mode at the cursor's current position <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>, <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>
*   `I` (Shift + i): Enter insert mode at the beginning of the current line <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>, <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>
*   `a`: Enter insert mode *after* the cursor's current position <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>, <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>
*   `A` (Shift + a): Enter insert mode at the end of the current line <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>, <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>
*   `Escape`: Exit insert mode and return to normal mode <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>

### Productivity Tip: Remapping Caps Lock
Many Vim users remap their Caps Lock key to act as the Escape key <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. This makes the Escape key more accessible, as it's closer to the pinky finger than the corner of the keyboard <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

## [[Setting up Vim within Visual Studio Code | Setting Up Vim Within Visual Studio Code]]

You don't need to abandon [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] to benefit from Vim's power <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. You can leverage [[Advanced Vim commands and customization | Vim's]] capabilities directly within your favorite editor <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

### Installation Steps
1.  **Install the Vim Extension**:
    *   In [[efficient_navigation_and_code_editing_in_vs_code | VS Code]], go to the Extensions panel <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
    *   Search for "Vim" <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
    *   Look for the extension named "Vim" by "vscode-vim.vim," which should have around 2 million installations <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
    *   Install this extension <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
2.  **Set Up Key Repeat**:
    *   Search Google for "vs code vim github" to find the `vscode-vim/vim` GitHub repository <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
    *   Scroll down to the installation section to find instructions for enabling key repeating <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. This feature allows keys to repeat when held down, which is helpful for [[Vim navigation and keyboard shortcuts | navigation]] <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
    *   Run the provided command for your operating system in the terminal (e.g., for Mac) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
3.  **Restart and Verify**:
    *   Restart [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] for the changes to take effect <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
    *   To verify, create a new file and observe if your cursor is slightly wider <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
    *   Hit `i` to enter insert mode, then hit `return` several times <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
    *   Hit `escape`, then try hitting and holding `k`; if your cursor moves smoothly up, key repeating is enabled <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

### Vim in VS Code: No Getting Stuck
When using Vim within [[efficient_navigation_and_code_editing_in_vs_code | VS Code]], you are primarily utilizing Vim's key bindings, which means you still have access to your mouse and standard [[VS Code keyboard shortcuts and commands | VS Code keyboard shortcuts and commands]] <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This alleviates the common fear of getting stuck in Vim, as you can easily close files or navigate using familiar [[efficient_navigation_and_code_editing_in_vs_code | VS Code]] methods <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.