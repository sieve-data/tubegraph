---
title: Basic Bash commands and scripts
videoId: I4EWvMFj37g
---

From: [[fireship]] <br/> 

Bash, short for "Born-Again Shell," is a command language interpreter used for interacting with a computer from the command line <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is commonly referred to as a "shell" because it encapsulates the operating system kernel, simplifying its complex details while enabling programmers to perform essential tasks like accessing data and writing files by typing straightforward commands <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## History and Evolution of Bash

The concept of a shell was revolutionary when it emerged in the early 1970s, a time when programmers typically used punch cards <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The shell concept evolved over the years, with the Bourne shell becoming the most prevalent version <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. In 1989, the Born-Again Shell, or Bash, was introduced <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

Bash is typically the default shell on Unix machines, including macOS and most [[basic_linux_commands_and_operations | Linux]] distributions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It provides a prompt where commands can be typed, which are then interpreted by the shell and executed on the operating system <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

To check if Bash is currently running, you can type `which $SHELL` into the command line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Bash functions like any other application found in the [[role_of_binaries_and_executables_in_linux | binaries]] directory <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Bash as a Programming Language

Beyond being a command interpreter, Bash is also a [[scripting_and_utility_programming_languages | programming language]] that enables users to write [[scripting_and_utility_programming_languages | scripts]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This capability means that any sequence of commands manually typed into the command line can be automated with code <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Startup Scripts and Customization

When the shell is first launched, it executes a [[bash_startup_scripts_and_customization | startup script]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This script is defined in files like `.bash_profile` or `.bashrc` on your system <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. These files allow you to customize the behavior and appearance of the shell for every new session <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Creating and Running Bash Scripts

You can add your own custom Bash [[scripting_and_utility_programming_languages | scripts]] to any project by creating a file that ends in `.sh` or has no file extension at all <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

#### Shebang

The very first line in a Bash script should always be a shebang, followed by the path to the application that should run the script <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. For Bash, this is commonly `#!/bin/bash`.

#### Basic Commands

Below the shebang, you can begin writing commands, which will be interpreted line by line <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **`echo`**: A common command used to print something to the terminal <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

#### Variables

To create a [[using_variables_and_arguments_in_bash_scripts | variable]], type a name in all caps followed by an equal sign and its value <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   Example: `MY_VARIABLE="Hello World"`
*   To reference the [[using_variables_and_arguments_in_bash_scripts | variable]] later in the script, use a dollar sign in front of its name <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   Example: `echo $MY_VARIABLE`

#### Executing Scripts

To execute a script, simply type its filename into the shell <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

#### Arguments

You can pass [[using_variables_and_arguments_in_bash_scripts | arguments]] when running a script <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Positional [[using_variables_and_arguments_in_bash_scripts | arguments]] are automatically assigned [[using_variables_and_arguments_in_bash_scripts | variable]] names like `$1`, `$2`, `$3`, and so on <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

#### User Input

For cases where additional user input is needed in the middle of a script, Bash can prompt the user <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

#### Conditional Logic and Loops

Bash supports [[conditional_logic_and_loops_in_bash | loops]] and [[conditional_logic_and_loops_in_bash | conditional logic]] for more complex [[scripting_and_utility_programming_languages | scripting]]:

*   **[[conditional_logic_and_loops_in_bash | Loops]]**: You can create [[conditional_logic_and_loops_in_bash | loops]], such as a `do while` loop, to repeatedly prompt a user or perform actions <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **[[conditional_logic_and_loops_in_bash | Conditional Logic]]**: [[conditional_logic_and_loops_in_bash | Conditional logic]] can be implemented with an `if` statement to test conditions <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. If a condition is true, one command runs; otherwise, an `else` command can be executed <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

#### Running Processes in Parallel

A useful feature is the ability to run multiple long-running processes in parallel in the background by adding an ampersand (`&`) after the command <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.