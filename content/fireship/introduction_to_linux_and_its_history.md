---
title: Introduction to Linux and its History
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

[[introduction_to_computer_science_concepts | Linux]] is a superior, free, and open-source operating system <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While it holds only about a 4% share of the PC market among humans <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, it is the dominant operating system on servers, utilized by approximately 96% of non-human bots <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. For programmers and developers, understanding [[introduction_to_computer_science_concepts | Linux]] is crucial, as it's the environment where code will eventually run and often require fixing via an SSH connection to a terminal <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Historical Context

### Unix and POSIX
Before [[introduction_to_computer_science_concepts | Linux]], there was Unix, an operating system developed at AT&T Bell Labs in the 1970s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Its development led to the standardization called POSIX (Portable Operating System Interface), which ensures compatibility between different systems <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The influence of POSIX is still strong today, with macOS, Android, FreeBSD, and most [[linux_distributions_and_package_managers | Linux distributions]] being POSIX compliant <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### The Birth of Linux
In 1987, Minix, an operating system intended for academic use, was developed, but its code redistribution was restricted <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This restriction inspired Linus Torvalds, a Finnish computer science student, to develop [[introduction_to_computer_science_concepts | Linux]] in 1991 <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Importantly, [[introduction_to_computer_science_concepts | Linux]] is free open-source software, licensed under GPL 2.0 <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This "freedom" means it can be freely distributed, modified, and even used for commercial purposes <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## The [[linux_kernel_and_system_architecture | Linux Kernel]]

What is commonly referred to as [[introduction_to_computer_science_concepts | Linux]] is, in fact, not a complete operating system but rather an operating system [[linux_kernel_and_system_architecture | kernel]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Written in the C programming language <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, the [[linux_kernel_and_system_architecture | kernel]] acts as the intermediary between software applications and hardware <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Boot Process
When a computer powers on, the boot loader (commonly GRUB) loads the [[linux_kernel_and_system_architecture | Linux kernel]] into Random Access Memory (RAM) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. From there, the [[linux_kernel_and_system_architecture | kernel]] detects hardware and initiates the init system, typically a tool called systemd, though alternatives exist <a class="yt="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Once initialized, the [[linux_kernel_and_system_architecture | kernel]] starts applications in user space, usually leading to a login screen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Kernel Responsibilities
The [[linux_kernel_and_system_architecture | kernel]] has several key responsibilities:
*   **Memory Management** It allocates and deallocates memory for processes <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. It can also create virtual memory, leveraging the hard drive to exceed physically available RAM <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **[[file_system_and_permissions_in_linux | File System]] Interaction** The [[linux_kernel_and_system_architecture | kernel]] provides a virtual [[file_system_and_permissions_in_linux | file system]] for interacting with files across different systems <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. The fourth extended [[file_system_and_permissions_in_linux | file system]] (ext4) is the most common default on [[introduction_to_computer_science_concepts | Linux]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Device Management** It interacts with peripheral devices through drivers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Protection Rings and System Calls
The [[linux_kernel_and_system_architecture | kernel]] operates within the CPU's protection ring 0, holding the highest level of privilege <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Most user-space operations occur in ring 3, with the lowest privilege <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. When a user action requires kernel access (e.g., writing a file), a system call is made, transitioning from ring 3 to ring 0 <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Functions like `write` in C code, while appearing as direct commands, are often wrappers provided by `glibc` (the GNU standard library for C), which then make the actual system calls <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## GNU Utilities and the Shell
The GNU project, initiated in 1983 by Richard Stallman, predates the [[linux_kernel_and_system_architecture | Linux kernel]] <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It provides all the core utilities that make the [[linux_kernel_and_system_architecture | kernel]] useful to humans <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### The Terminal and Shell
The best way to explore these utilities is through the terminal, a graphical user interface for sending commands via the shell <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The shell acts as a protective layer between user space and the [[linux_kernel_and_system_architecture | kernel]] <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Bash is the most common shell <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Basic Commands and Concepts
*   **`echo`**: Prints a string to standard output, involving a system call to the [[linux_kernel_and_system_architecture | kernel]] to render pixels on the screen <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **`man`**: Accesses the manual page for any command (e.g., `man touch`) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **`touch`**: Creates a new, empty file <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **`ls`**: Lists files in the current directory <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Flags like `-l` (long listing) and `-h` (human-readable) provide more details, such as file size <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **`cat`**: Reads file contents <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **`stat`**: Displays file metadata like birth time, modification time, and last access time <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **`rm`**: Removes files <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Redirection (`>` and `<`)**: Used to redirect command output to a file or file content as input to a command <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Pipes (`|`)**: Take the output of one command and pass it as input to another, e.g., `cat log.txt | sort | uniq` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Bash Scripting
For repetitive tasks, [[introduction_to_computer_science_concepts | Linux]] users can write Bash scripts <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. These files start with a "shebang" (e.g., `#!/bin/bash`) to tell [[introduction_to_computer_science_concepts | Linux]] to use the Bash interpreter <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Text editors like Nano (built into most [[linux_distributions_and_package_managers | Linux distributions]]), Vim, or Emacs can be used to create these scripts <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Users, Groups, and Permissions
[[introduction_to_computer_science_concepts | Linux]] manages access through users and groups.
*   **Users**: Every user has a unique ID (UID) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The `whoami` command returns the username <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, and `id` shows the UID <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Root**: A special user with UID 0, often called admin or superuser, possessing the highest level of privilege <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Users can switch to root with `su` or run commands with elevated privilege using `sudo` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Groups**: Have Group IDs (GIDs) and simplify managing permissions for multiple users <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **[[file_system_and_permissions_in_linux | File Permissions]]**: Viewed with `ls -l` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Symbolic permissions are represented by nine characters: three triplets for owner, group, and others. Each triplet contains `r` (read), `w` (write), and `x` (execute) if granted, or a dash (`-`) if denied <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Permissions can also be represented numerically (octal notation), e.g., `777` grants all permissions to everyone, though this is generally discouraged due to the "principle of least privilege" <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   `chmod`: Modifies [[file_system_and_permissions_in_linux | file permissions]] <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
    *   `chown`: Changes the owner of a file <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   `chgrp`: Assigns groups to files <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## [[file_system_and_permissions_in_linux | Linux File System]] Hierarchy
By default, users start in their home directory, a personal workspace <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   `mkdir`: Creates a new directory <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   `cd`: Changes directories <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   `pwd`: Prints the current working directory <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

Key directories in the root (`/`) of the [[file_system_and_permissions_in_linux | file system]]:
*   `/boot`: Contains the [[linux_kernel_and_system_architecture | Linux kernel]] <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   `/dev`: Contains external devices like hard drives <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   `/etc`: Stores configuration files <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   `/var`: Contains log files <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   `/bin`: Holds user binaries (executables) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   `/sbin`: Holds system binaries <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   `/usr`: Holds user system resources, including more binaries <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### The PATH Environment Variable
When a command is entered, [[introduction_to_computer_science_concepts | Linux]] searches for an executable binary in directories listed in the `PATH` environment variable <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. `PATH` contains a list of directories separated by colons <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. The first matching binary found is executed <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. The `export` keyword is used to set environment variables, often customized in the `.bashrc` file for individual users, which runs before every terminal session <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

## Processes and System Management
Any command or program execution creates a process on the CPU, managed by the [[linux_kernel_and_system_architecture | Linux kernel]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   `ps`: Views processes, each with a unique Process ID (PID) and creator user <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   `htop`: Provides an interactive breakdown of processes <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Background Processes**: A long-running script can be run in the background by appending an ampersand (`&`) to the command <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Scheduled Tasks**: `cron` (or `crontab`) allows scheduling scripts to run at specific times <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Killing Processes**:
    *   `kill [PID]`: Gracefully sends a `Sigterm` signal to a process <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   `kill -9 [PID]`: Forcefully kills a process with a `Sigkill` signal <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Other Essential Utilities
Common [[introduction_to_computer_science_concepts | Linux]] utilities include:
*   `grep`: Searches through text <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   `sed`: Modifies text <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   `gzip`: Compresses files <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   `tar`: Archives directories <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## [[linux_distributions_and_package_managers | Linux Distributions]]
A [[linux_distributions_and_package_managers | Linux distribution]] is a complete operating system built on the [[linux_kernel_and_system_architecture | Linux kernel]], featuring a curated set of default software tailored for specific target audiences <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Key Differences Between Distributions
*   **[[linux_distributions_and_package_managers | Package Managers]]**: Different [[linux_distributions_and_package_managers | distributions]] use different [[linux_distributions_and_package_managers | package managers]] to install software (e.g., `apt`, `yum`, `pacman`) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Release Schedules**: Some have fixed release dates, while "rolling releases" keep software continuously updated to the cutting edge <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Desktop Environments**: For PC users, the default desktop environment (e.g., GNOME, KDE Plasma) significantly impacts the user experience <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Families of Distributions
*   **Slackware**: An "Original Gangster" from the 90s <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Debian**: The most popular overall, known for its open philosophy and ease of use <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Red Hat**: A common choice in enterprise environments due to its long-term support plans <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Arch**: Favored by advanced users who embrace its blend of complexity and simplicity, reflecting mastery over the digital world <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.