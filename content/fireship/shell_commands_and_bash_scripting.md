---
title: Shell Commands and Bash Scripting
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

Linux, a free and open-source operating system kernel, serves as the dominant OS on servers and is essential knowledge for programmers and developers <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Understanding how to interact with it via shell commands and bash scripts is a fundamental skill <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Shell and Command Execution

The **shell** acts as a graphical user interface (GUI) within the terminal, allowing users to send commands and providing a layer of protection between user space and the kernel <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. While many flavors of shells exist, **Bash** (Bourne Again SHell) is the most common <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

When a command is executed, it often involves a **system call** to the Linux kernel, which then manages permissions, drivers, and other low-level operations <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Core utilities for Linux, which make the kernel useful to humans, are often provided by the GNU project <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Basic Shell Commands

Here are some essential commands for interacting with the Linux file system and managing data:

*   **`echo`**: Used to print a string argument to the standard output, like "Hello Linux Kernel" <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **`man`**: Displays the manual page for any command, providing information on its usage and functionality <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For example, `man touch` shows that `touch` is used to create a new file <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **`touch`**: Creates a new, empty file <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **`ls`**: Lists the files and directories in the current working directory <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   Adding flags like `-l` provides more details (e.g., permissions, owner, size) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   The `-h` flag makes sizes human-readable <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Flags can be combined, e.g., `ls -lh` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **`cat`**: Reads and concatenates file contents to the standard output <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **`stat`**: Displays detailed metadata about a file, such as birth time, modification time, and last access time <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **`rm`**: Removes (deletes) files <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Command Redirection and Pipes

The Linux terminal allows for powerful command combination:

*   **Redirection (`>` or `<`)**:
    *   The angle bracket `>` redirects the output of a command to a new file, overwriting its contents <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   Flipping the angle bracket `<` redirects the input of a file to a command <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Pipes (`|`)**: Pipes take the output of one command and pass it as input to another command <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, `cat logfile.txt | sort | uniq` would read a log file, sort its lines, and then remove duplicate lines <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Bash Scripting

When performing repetitive tasks, writing a **bash script** in a dedicated file is efficient <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

To create a script, an interactive text editor like Nano (built into most Linux distros) can be used <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Alternatively, Vim or Emacs are available for more advanced users <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

A bash script starts with a **shebang** (e.g., `#!/bin/bash`) on the first line, which tells Linux which interpreter to use for the script <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Scripts can include any bash code, such as `echo` for output and `read` to get input from the standard input <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Once saved, a script can be executed by entering its file path in the terminal <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## User Management and Privileges

Linux handles users and permissions meticulously:

*   **`whoami`**: Returns your current Linux username <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **`id`**: Shows your unique User ID (UID) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **`root`**: The special user with a UID of zero, also known as admin or superuser, having the highest level of privilege <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **`su`**: Switches to the root user <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **`sudo`**: Prefixes a command to run it with elevated privileges, useful for users who have been granted `sudo` privilege <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. You can check your `sudo` privilege with `sudo -l` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Groups**: Linux uses groups, each with a Group ID (GID), to simplify managing [[file_system_and_permissions_in_linux | permissions]] for multiple users <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

## Navigating and Customizing the File System

For a more in-depth exploration of the [[file_system_and_permissions_in_linux | file system]], refer to the dedicated topic.

*   **`pwd`**: Prints the current working directory <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **`mkdir`**: Creates a new directory <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **`cd`**: Changes the current directory <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   `cd` by itself returns to the home directory <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
    *   `cd /` moves to the root of the file system <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

Key directories in the root file system (`/`):
*   `/boot`: Contains the Linux kernel <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   `/dev`: Contains external devices like hard drives <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   `/etc`: Holds configuration files <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   `/var`: Contains log files <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   `/bin`: Stores essential binaries (executable programs) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   `/sbin`: Stores system binaries <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### The `PATH` Environment Variable

When you run a command, Linux searches for an executable binary. The `PATH` environment variable contains a colon-separated list of directories where Linux looks for these binaries <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. It executes the first matching binary it finds <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

*   The `PATH` can be customized using the `export` keyword to set its value <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   A common technique is to update the `PATH` for an individual user by modifying the `.bashrc` file <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### `.bashrc` File

The `.bashrc` file is a script that runs before every terminal session, allowing users to customize their environment <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This includes customizing the `PS1` environment variable to change the terminal prompt's appearance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## [[file_system_and_permissions_in_linux | File Permissions]]

Permissions dictate who can read, write, or execute a file:

*   **`ls -l`**: Shows symbolic permissions, which are nine cryptic characters (e.g., `rwx r-x r--`) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   The first triplet represents the owner, the middle triplet is for the group, and the last triplet is for everyone else <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Each position contains 'r' (read), 'w' (write), or 'x' (execute), or a dash '-' for denied access <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Octal Notation**: Permissions can also be represented as numbers in octal notation (e.g., `777`) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   `777` grants read, write, and execute permissions to the owner, group, and everyone else <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   It's generally a bad idea to use `777` due to the "principle of least privilege," which advocates granting access only when necessary <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **`chmod`**: Modifies the permissions on a file <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **`chown`**: Changes the owner of a file <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **`chgrp`**: Assigns a new group to a file <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## Processes and Scheduling

The Linux kernel manages **processes**, which are created whenever a command or program is executed <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

*   **`ps`**: Views active processes, showing a unique Process ID (PID) and the user who created it <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **`htop`**: Provides an interactive, filtered breakdown of processes <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Background Processes**: Adding an ampersand (`&`) to the end of a command will run it as a background process <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **`cron`**: Used to schedule scripts to run at specific times or intervals <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **`kill`**: Sends signals to processes to terminate them.
    *   By default, `kill` sends a `SigTerm` signal for graceful termination <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   Using the `-9` flag (e.g., `kill -9 [PID]`) sends a `SigKill` signal for forceful termination <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Other Useful Utilities

Beyond the basics, several other standard Linux utilities are commonly used:
*   **`grep`**: For searching through text in files <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **`sed`**: For modifying text <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **`gzip`**: For compressing files <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **`tar`**: For archiving directories <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Linux Distributions

A **Linux distribution (distro)** is a complete operating system built on the Linux kernel, offering a highly opinionated set of default software tailored for specific target audiences <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Distros can vary in:
*   **Package Managers**: Different distros use different package managers to install software, such as `apt` (Debian), `yum` (Red Hat), or `Pac-Man` (Arch) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Release Schedules**: Some have fixed release dates, while others (rolling releases) continuously update their software <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Desktop Environments**: If used as a personal computer, a distro will have a default desktop environment like GNOME or KDE Plasma, which significantly impacts the user experience <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Common Linux distro families include:
*   **Slackware**: An "Original Gangster" from the 90s <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Debian**: Known for its open philosophy and ease of use <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Red Hat**: Popular in enterprise for its long-term support <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Arch**: Known for its complexity and simplicity, often chosen by users seeking deep customization and mastery <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.