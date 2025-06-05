---
title: File System and Permissions in Linux
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

Understanding the file system and permissions is crucial for anyone using [[Introduction to Linux and its History | Linux]], especially developers, as it dictates how data is organized, accessed, and secured <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## Linux Kernel and the File System

At its core, the [[Linux Kernel and System Architecture | Linux kernel]] provides a virtual file system, allowing interaction with files across different underlying systems <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. The most common default file system on [[Introduction to Linux and its History | Linux]] is the fourth extended file system (ext4) <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. The kernel is responsible for managing memory for processes, including creating virtual memory, and interacting with peripheral devices via drivers to turn data into screen pixels <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

When performing actions that require kernel access, such as writing a file, system calls are used to transition from user space (Ring 3) to the kernel's privileged space (Ring 0) <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Libraries like Glibc provide wrappers for these system calls <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## File System Structure

When you use the [[Shell Commands and Bash Scripting | terminal]], you typically start in your *home directory*, which acts as a personal workspace for the logged-in user <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. This can be navigated with the `cd` command <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>, and your current location can be printed using `pwd` <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

The entire [[Linux Kernel and System Architecture | Linux]] file system branches out from the */ (root)* directory <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. Several critical directories reside here:
*   `/boot`: Contains the [[Linux Kernel and System Architecture | Linux kernel]] itself <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   `/dev`: Houses external devices like hard drives <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
*   `/etc`: Stores configuration files <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   `/var`: Holds log files <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   `/bin`: Contains common binaries <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   `/sbin`: Contains system binaries <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
*   `/usr`: Holds user system resources, where binaries might also live <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

[[Shell Commands and Bash Scripting | Linux]] finds executable binaries by searching directories listed in the `PATH` environment variable, which contains paths separated by colons <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>. This variable can be customized using the `export` keyword, often in the `.bashrc` file, which runs before every [[Shell Commands and Bash Scripting | terminal]] session <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

## Users and Groups

Every user in [[Introduction to Linux and its History | Linux]] has a username, viewable with `whoami` <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>, and a unique User ID (UID), which can be seen using the `id` command <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. The special user, `root`, has a UID of zero and possesses the highest level of privilege, often referred to as "admin" or "super user" <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

Users can temporarily switch to the `root` user with the `su` command or run individual commands with elevated privileges by prefixing them with `sudo` <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Your `sudo` privileges can be checked with `sudo -l` <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.

[[Introduction to Linux and its History | Linux]] also uses *groups*, which have Group IDs and simplify permission management for multiple users <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.

## File Permissions

File permissions control who can read, write, or execute a file. They are displayed when using `ls -l` <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>:
*   **Symbolic Permissions**: The cryptic nine characters (e.g., `rwxrw-r--`) are divided into three triplets <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>:
    *   **Owner**: The first triplet represents the file's owner.
    *   **Group**: The middle triplet represents the group associated with the file.
    *   **Others**: The last triplet applies to everyone else.
    *   Each position within a triplet indicates specific privileges: `r` (read), `w` (write), and `x` (execute). A dash (`-`) signifies permission denied <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.

*   **Octal Notation**: Permissions can also be represented by numbers in octal notation <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.
    *   `r` = 4
    *   `w` = 2
    *   `x` = 1
    *   For example, `777` grants read, write, and execute permissions to the owner, group, and others <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. However, granting `777` is generally a bad idea, as it violates the *principle of least privilege*, which advises granting access only when necessary and trusting no one <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

### Modifying Permissions

*   **`chmod`**: Changes the permissions of a file <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>.
*   **`chown`**: Changes the owner of a file <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
*   **`chgrp`**: Assigns a new group to a file <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

## Basic File Management Commands

*   `touch`: Creates a new empty file or updates its timestamp <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   `ls`: Lists files and directories <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. Flags like `-l` provide more details, and `-h` makes file sizes human-readable <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   `cat`: Displays the content of files <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
*   `stat`: Shows detailed metadata about a file, such as birth time, modification time, and last access time <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.
*   `rm`: Removes files <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   `mkdir`: Creates new directories <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   `grep`: Searches for patterns within text <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.
*   `sed`: Modifies text streams <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.
*   `gzip`: Compresses files <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   `tar`: Archives directories <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.

These commands, often used in conjunction with redirection (`>` for output, `<` for input) <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a> and pipes (`|` to pass output of one command as input to another) <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>, form the foundation of file system interaction in [[Introduction to Linux and its History | Linux]].