---
title: Basic Linux commands and shell usage
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

The terminal is a graphical user interface that allows users to send commands via the shell <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The shell acts as a layer of protection between user space and the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. There are various types of shells, but the most common one is [[basic_bash_commands_and_scripts | Bash]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Core Utilities

Many core utilities for [[introduction_to_linux | Linux]] are provided by the GNU project, which predates the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] itself and was started in 1983 by Richard Stallman <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These utilities make the [[role_of_linux_kernel_in_operating_systems | kernel]] useful to humans <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Getting Help
*   **`man`**: Displays the manual page for any command <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For example, `man touch` shows how to create a new file <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### File and Directory Management
*   **`echo`**: Prints a string argument to the standard output <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **`touch`**: Used to create a new file <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **`ls`**: Lists the files in the current directory <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   **`-L` flag**: Lists more details about files <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   **`-H` flag**: Makes file details human-readable, such as exact file size <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Flags can be combined (e.g., `ls -lh`) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **`cat`**: Reads and displays the contents of a file <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **`stat`**: Provides metadata about a file, such as its birth time, modification time, and last access time <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **`rm`**: Removes a file <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **`mkdir`**: Creates a new directory <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **`cd`**: Changes directories <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   `cd ..`: Navigates to the parent directory.
    *   `cd /`: Navigates to the root of the [[navigating_the_linux_file_system | file system]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **`pwd`**: Prints the current working directory <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Input/Output Redirection and Pipes
The Linux terminal makes it easy to combine commands <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **`>` (Redirection)**: Redirects the output of one command to a new file <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **`<` (Redirection)**: Redirects the input from a file to a command <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **`|` (Pipes)**: Allows the output of one command to be passed as input to another command <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. For example, `cat log.txt | sort | uniq` would read a log file, sort its lines, and then remove duplicates <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### [[basic_bash_commands_and_scripts | Bash Scripts]]
If a user finds themselves performing the same tasks repeatedly, it may be time to write a [[basic_bash_commands_and_scripts | Bash script]] in its own dedicated file <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Shebang**: At the top of a script file, a shebang (e.g., `#!/bin/bash`) tells [[introduction_to_linux | Linux]] to use the [[basic_bash_commands_and_scripts | Bash]] interpreter for execution <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **`read`**: Reads a value from standard input <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Execution**: A script can be executed by entering its file path in the terminal <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### User and Group Management
*   **`whoami`**: Returns the current [[introduction_to_linux | Linux]] username <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **`id`**: Shows the unique User ID (UID) for the current user <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. The special `root` user has a UID of zero and the highest level of privilege <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **`su`**: Switches to the root user <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **`sudo`**: Prefixes any command to run it with elevated (root) privilege <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Any user can be granted `sudo` privilege <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **`sudo -l`**: Checks your `sudo` privilege <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Groups**: [[introduction_to_linux | Linux]] also has groups, which have Group IDs (GIDs) and simplify permission management for multiple users <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

### Environment Variables
*   **`PATH`**: A special environment variable that contains paths to directories, separated by colons <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. When a command is entered, [[introduction_to_linux | Linux]] searches through the `PATH` for a matching [[role_of_binaries_and_executables_in_linux | binary]] in each directory and executes the first one it finds <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **`export`**: Used to set the value for an environment variable <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **`.bashrc`**: A script file that runs before every terminal session, commonly customized to update the `PATH` for an individual user or change the terminal prompt using the `PS1` environment variable <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### File Permissions
File permissions can be viewed using `ls -L` on any file <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Symbolic Permissions**: Represented by nine cryptic characters <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
    *   The first triplet represents the owner <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   The middle triplet represents the group <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   The last triplet is for everyone else <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Each position contains a letter (r, w, x) for read, write, and execute privileges <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. A letter means access granted, while a dash (`-`) means permission denied <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Octal Notation**: Permissions can also be represented as numbers in octal notation <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. For example, `777` allows anyone to do anything to a file, which is generally a bad idea as it violates the principle of least privilege <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **`chmod`**: Modifies permissions on a file <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **`chown`**: Changes the owner of a file <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **`chgrp`**: Assigns groups to a file <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Process Management
Anytime a command is run or a program executed, it creates a process on the CPU, which is managed by the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **`ps`**: Views active processes <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Each process has a unique Process ID (PID) and the user who created it <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **`htop`**: Provides an interactive breakdown of processes that can be filtered <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Background Processes**: A long-running script can be created as a background process by adding an ampersand (`&`) to the end of the command <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **`crontab`**: Used to schedule scripts to run at specific times or intervals <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **`kill`**: Sends a signal to a process, typically to terminate it <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   Gracefully sends a `Sigterm` signal <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   The `-9` flag (e.g., `kill -9 [PID]`) forcefully kills a process with a `Sigkill` signal <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### Other Useful Utilities
*   **`grep`**: For searching through text <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **`sed`**: For modifying text <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **`gzip`**: For making files smaller <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **`tar`**: For archiving directories <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.