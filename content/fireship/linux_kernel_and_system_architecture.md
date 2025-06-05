---
title: Linux Kernel and System Architecture
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

Linux is a free, open-source operating system that holds a 4% share of the PC market, but it is the dominant operating system on servers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Programmers and developers need to understand Linux because it is where their code will eventually run <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Historical Context

### Unix and POSIX
Before Linux, there was Unix, an operating system developed at AT&T Bell Labs in the 1970s <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Its development led to the standardization known as POSIX (Portable Operating System Interface) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This standard ensures compatibility between different systems <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Unix's influence is still strong today, with macOS, Android, FreeBSD, and most [[Linux Distributions and Package Managers | Linux distributions]] being POSIX compliant <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### The Birth of Linux
In 1987, Minix, an OS for academic use, was developed <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. However, its code redistribution was restricted <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This limitation inspired Finnish computer science student Linus Torvalds to develop Linux in 1991 <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Linux is free and open-source software, licensed under GPL 2.0 <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This means it is free to distribute, modify, and even make money from <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## The Linux Kernel

What is commonly referred to as Linux is, in fact, an operating system kernel, not a complete operating system <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Kernel Functions
The kernel is written in the [[lowlevel_systems_programming_languages | C programming language]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> and acts as the interface between software applications and the hardware <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

When a computer powers on:
1.  The boot loader (usually Grub) loads the Linux kernel into RAM <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  The kernel detects hardware and starts the init system, typically SystemD <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  Once initialized, the kernel starts applications in user space, leading to a login screen <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The kernel has significant responsibilities during operation:
*   **Memory Management**: It allocates and deallocates memory for processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. It can also create virtual memory by using the hard drive to extend physically available memory <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **[[File System and Permissions in Linux | Virtual File System]]**: Provides a consistent interface for interacting with files across different systems <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. The fourth extended [[File System and Permissions in Linux | file system]] (EXT4) is the most common default on Linux <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Device Interaction**: Interacts with peripheral devices through drivers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### CPU Protection Rings
The kernel operates within the CPU's protection rings, specifically in Ring 0, which has the highest level of privilege <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Most user-space applications operate in Ring 3, which has the lowest level of privilege <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### System Calls
When a user wants to perform an action requiring kernel access, such as writing a file, a system call is made <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This call transitions the operation from Ring 3 to Ring 0 <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Functions like `write` are often wrappers provided by GLIBC (GNU Standard Library for C), which simplifies making system calls <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## The GNU Project and Core Utilities

The GNU Project, pronounced "Gnu," was started in 1983 by Richard Stallman, predating the Linux kernel <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It provides the core utilities that make the kernel useful to humans <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### The Terminal and Shell
The best way to explore these utilities is through the terminal, a graphical user interface for sending commands via the shell <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The shell provides a layer of protection between user space and the kernel <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Bash is the most common shell <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Common shell utilities include:
*   `echo`: Prints a string to standard output <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This involves a system call to the kernel to manage drivers and display pixels <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   `man`: Displays the manual page for any command <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   `touch`: Creates a new file <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   `ls`: Lists files in a directory <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Flags like `-l` (long format) and `-h` (human-readable) provide more details <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   `cat`: Reads and displays file contents <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   `stat`: Accesses metadata about files, such as birth time, modification time, and last access time <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   `rm`: Removes files <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Command Chaining
The Linux terminal allows for powerful command combinations:
*   **Redirection**: Uses angle brackets (`>` or `<`) to redirect the output of one command to a file or the input of a command from a file <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Pipes (`|`)**: Takes the output of one command and passes it as input to another <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. For example, `cat file | sort | uniq` reads a file, sorts its lines, then removes duplicates <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Bash Scripts
For repetitive tasks, Bash scripts can be written in dedicated files <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Text editors like Nano (minimalist, built into most distros), Vim, or Emacs can be used <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. A shebang (`#!`) at the top of the script tells Linux which interpreter (e.g., `bash`) to use <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## Users, Groups, and Permissions

### User Management
*   `whoami`: Returns the current Linux username <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   `id`: Displays the user's unique User ID (UID) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The special user `root` (UID 0) has the highest level of privilege <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   `su`: Switches to the root user <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   `sudo`: Executes a command with elevated (root) privileges <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. `sudo -l` checks a user's sudo privileges <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Group Management
Linux uses groups, which have Group IDs (GIDs), to manage permissions for multiple users more easily <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

### [[File System and Permissions in Linux | File Permissions]]
The `ls -l` command displays file permissions, represented by nine cryptic characters called symbolic permissions <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   The first triplet: owner permissions.
*   The middle triplet: group permissions.
*   The last triplet: permissions for everyone else <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

Each triplet consists of `r` (read), `w` (write), and `x` (execute) <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. A dash indicates permission denied <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Permissions can also be represented numerically in octal notation (e.g., `777`) <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   It is crucial to follow the **principle of least privilege**, granting access only when necessary <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

Commands to modify permissions:
*   `chmod`: Changes file permissions (e.g., `chmod 777 file.txt` or `chmod +rwx file.txt`) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   `chown`: Changes the owner of a file <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   `chgrp`: Assigns groups to files <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## Linux File System Hierarchy

By default, users start in their `home` directory, a personal workspace <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   `mkdir`: Makes a new directory <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   `cd`: Changes directories <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   `pwd`: Prints the current working directory <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

Navigating to the root of the [[File System and Permissions in Linux | file system]] (`cd /`) reveals critical directories:
*   `/boot`: Contains the Linux kernel itself <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   `/dev`: Contains external devices like hard drives <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   `/etc`: Contains configuration files <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   `/var`: Contains log files <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   `/bin`: Holds user binaries <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   `/sbin`: Holds system binaries <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### The PATH Environment Variable
When a command (e.g., `ls`) is run, Linux looks for an executable binary on the system <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The `PATH` environment variable contains a list of directories, separated by colons, where Linux searches for these binaries <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The first matching binary found is executed <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   `export`: Sets the value for an environment variable <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   `.bashrc`: A script that runs before every terminal session, commonly customized to update the `PATH` or modify the `PS1` environment variable for the terminal prompt <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Processes

Any command or program executed creates a process on the CPU, managed by the Linux kernel <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   `ps`: Views processes, showing each one's unique Process ID (PID) and the user who created it <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   `htop`: Provides an interactive breakdown of processes <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **System daemons**: Processes that run in the background <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Background processes**: Custom scripts can be run in the background by appending an ampersand (`&`) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **`crontab`**: Schedules scripts to run at specific times <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   `kill`: Terminates processes <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   `kill PID`: Sends a `Sigterm` signal for a graceful termination <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   `kill -9 PID`: Sends a `Sigkill` signal for a forceful termination <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Additional Common Utilities
Beyond the basics, other standard utilities include:
*   `grep`: Searches through text <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   `sed`: Modifies text <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   `gzip`: Compresses files <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   `tar`: Archives directories <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## [[Linux Distributions and Package Managers | Linux Distributions]]

A Linux distribution is a complete operating system built on the Linux kernel <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Each distribution has an opinionated set of default software tailored for its target audience <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

Key differentiating factors among distributions:
*   **[[Linux Distributions and Package Managers | Package Managers]]**: Different distributions use different package managers (e.g., `apt`, `yum`, `pacman`) to install software <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Release Schedules**: Some have predictable fixed release dates, while others (rolling releases) constantly provide the latest software <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Desktop Environments**: For PC use, a desktop environment (e.g., Gnome, KDE Plasma) significantly impacts the user experience <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Notable distribution families:
*   **Slackware**: An "Original Gangster" from the 1990s <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Debian**: The most popular overall, known for its open philosophy and ease of use <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Red Hat**: A common choice in enterprise environments due to its long-term support <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Arch**: Known for its "paradox of complexity and simplicity," often favored by users who deeply engage with their operating system <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.