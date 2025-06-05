---
title: GNU project and core utilities
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

The [[gnu_project_and_richard_stallman|GNU Project]], pronounced "Gnu," is a foundational project that predates the [[Linux kernel and its role|Linux kernel]] itself, having been started in 1983 by [[gnu_project_and_richard_stallman|Richard Stallman]] <a class="yt-timestamp" data-t="03:07:44">[03:07:44]</a>. It provides the core utilities that make the [[Linux kernel and its role|Linux kernel]] useful to humans, effectively making the combination of [[GNU Project and Richard Stallman|GNU]] software and the [[Linux kernel and its role|Linux kernel]] what most people refer to as "Linux" <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

## [[Linux system architecture and components|GNU Standard Library (GLibC)]]

The [[GNU Project and Richard Stallman|GNU]] Standard Library for C, known as GLibC, provides wrappers for making system calls that allow applications to interact with the operating system <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. For example, the `write` function in C, while not a system call itself, is a wrapper provided by GLibC that transitions from user space (Ring 3) to the [[Linux kernel and its role|kernel]] space (Ring 0) to output text to the console <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Interacting with [[basic_linux_commands_and_shell_usage|GNU]] Core Utilities

The best way to explore these core libraries is by opening the [[basic_linux_commands_and_shell_usage|terminal]], which is a graphical user interface that allows users to send commands via the [[basic_linux_commands_and_shell_usage|shell]] <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. The [[basic_linux_commands_and_shell_usage|shell]] acts as a layer of protection between user space and the [[Linux kernel and its role|kernel]] <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. Bash is the most common [[basic_linux_commands_and_shell_usage|shell]] <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.

When a command is executed, like `echo "Hello Linux Kernel"`, the [[basic_linux_commands_and_shell_usage|GNU]] shell utility `echo` takes the message and prints it to standard output <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. Under the hood, this involves a system call to the [[Linux kernel and its role|kernel]], which manages permissions and drivers to render pixels on the screen <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## Essential Core Utilities

Several core utilities are commonly used in [[basic_linux_commands_and_operations|Linux]]:

*   **`man`**: Displays the manual page for any command <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
*   **`touch`**: Used to create a new, empty file <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
*   **`ls`**: Lists files in a directory <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. Can be used with flags like `-l` for more details and `-h` for human-readable sizes <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **`cat`**: Reads the contents of a file <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
*   **`stat`**: Provides metadata about a file, such as birth time, modification time, and last access time <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
*   **`rm`**: Removes files <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **`echo`**: Prints text to the standard output <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **`whoami`**: Returns the current [[Linux system architecture and components|Linux]] username <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
*   **`id`**: Shows the user's unique ID (UID) <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.
*   **`su`**: Switches to the root user <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.
*   **`sudo`**: Prefixes a command to run it with elevated privileges <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.
*   **`mkdir`**: Creates a new directory <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **`cd`**: Changes directories <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.
*   **`pwd`**: Prints the current working directory <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
*   **`chmod`**: Modifies file permissions <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>.
*   **`chown`**: Changes the owner of a file <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
*   **`chgrp`**: Assigns groups to files <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.
*   **`ps`**: Views active processes <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
*   **`htop`**: Provides an interactive breakdown of processes <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>.
*   **`kill`**: Terminates a process, either gracefully (`Sigterm`) or forcefully (`Sigkill` with `-9` flag) <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

## Other Useful Utilities

Beyond the core utilities, other common tools include:

*   **`grep`**: For searching through text <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.
*   **`sed`**: For modifying text <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.
*   **`gzip`**: For making files smaller (compression) <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.
*   **`tar`**: For archiving directories <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.