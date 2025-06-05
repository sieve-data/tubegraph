---
title: History and evolution of Bash
videoId: I4EWvMFj37g
---

From: [[fireship]] <br/> 

Bash, also known as the Born-Again Shell, is a command language interpreter used for interacting with a computer from the command line <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's referred to as a "shell" because it acts as a layer surrounding the operating system kernel, concealing its complex details while enabling programmers to perform essential tasks like accessing data and writing files through simple commands <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Historical Context
The foundational concept of a shell was revolutionary when it emerged in the early 1970s, at a time when programmers were still relying on punch cards <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Over the years, this concept evolved, with the Bourne shell becoming the most widely used version <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Bash itself came into existence in 1989 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Bash as a Default Shell and Application
On Unix machines, including macOS and most [[history_of_linux | Linux]] distributions, Bash is typically the default shell when you open a terminal <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It presents a prompt where commands can be typed, which are then interpreted by the shell and executed on the operating system <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. To check if you are running Bash, you can type `which $SHELL` from the command line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Bash operates like any other application stored in the binaries directory <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Bash as a Programming Language and Scripting
Beyond its role as a command interpreter, Bash also functions as a programming language, allowing users to write [[basic_bash_commands_and_scripts | scripts]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This capability enables the automation of any command that would otherwise be typed manually into the command line <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Customization and Startup Scripts
When the shell is first launched, it executes a [[bash_startup_scripts_and_customization | startup script]] defined in the `.bash_profile` or `.bashrc` file on your system <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This feature allows for the customization of the shell's behavior and appearance for each new session <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Writing Bash Scripts
Custom Bash [[basic_bash_commands_and_scripts | scripts]] can be added to any project by creating a file with a `.sh` extension or no file extension at all <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Shebang**: The first line of a Bash script should always be a "shebang" (e.g., `#!/bin/bash`), followed by the path to the application responsible for running it <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Commands**: Below the shebang, commands like `echo` (to print output) can be written, which will be interpreted line by line <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Variables**: To create a variable, type a name in all uppercase, followed by an equals sign. The variable can then be referenced later in the script by preceding its name with a dollar sign <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Execution**: Scripts are executed by simply typing the file name into the shell <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Advanced Scripting Features
Bash scripts support various programming constructs:
*   **Positional Arguments**: When running a script, arguments passed to it are automatically assigned variable names like `$1`, `$2`, `$3`, and so on <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **User Input and Loops**: Loops, such as a `do while` loop, can be used to prompt the user for additional input mid-script, allowing for conditional continuation or exit <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Conditional Logic**: `if` statements enable conditional logic, testing a value on the left against a value on the right, and executing commands based on whether the condition is true or false <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Background Processes**: Multiple long-running processes can be run in parallel in the background by appending an ampersand (`&`) after the command <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.