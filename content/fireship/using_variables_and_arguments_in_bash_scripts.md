---
title: Using variables and arguments in Bash scripts
videoId: I4EWvMFj37g
---

From: [[fireship]] <br/> 
Bash, a command language interpreter, serves as a [[basic_linux_commands_and_shell_usage | shell]] that surrounds the operating system kernel, enabling programmers to access data and write files through simple commands <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Bash is also a [[scripting_and_utility_programming_languages | programming language]] that facilitates the automation of command-line actions through [[basic_bash_commands_and_scripts | scripts]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Creating and Executing Bash Scripts
You can create custom [[basic_bash_commands_and_scripts | Bash scripts]] by creating a file that ends in `.sh` or has no file extension <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The very first line of a [[basic_bash_commands_and_scripts | Bash script]] should be a "shebang" ( `#!` ) followed by the path to the application that should run the script <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Below the shebang, you can write commands that will be interpreted line by line <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. To execute a script, simply type its filename into the [[basic_linux_commands_and_shell_usage | shell]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Using Variables in Bash Scripts
Within a [[basic_bash_commands_and_scripts | Bash script]], you can create a variable by typing a name in all capital letters, followed by an equal sign (`=`), and then the value <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. To reference the variable later in the script, place a dollar sign (`$`) in front of its name <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. For instance, the `echo` command can be used to print something <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Handling Arguments in Bash Scripts
When running a [[basic_bash_commands_and_scripts | script]], you can pass in arguments <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These "positional arguments" are automatically assigned variable names like `$1`, `$2`, `$3`, and so on, based on their order <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### User Input and Control Flow
[[conditional_logic_and_loops_in_bash | Loops]] can be implemented in Bash to request additional user input in the middle of a script <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For example, a `do while` [[conditional_logic_and_loops_in_bash | loop]] can prompt the user to continue or exit the script <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. [[conditional_logic_and_loops_in_bash | Conditional logic]] can be applied using an `if` statement to test conditions, running a command if true and an `else` command otherwise <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.