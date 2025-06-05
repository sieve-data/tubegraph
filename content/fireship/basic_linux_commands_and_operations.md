---
title: Basic Linux commands and operations
videoId: rrB13utjYV4
---

From: [[fireship]] <br/> 

[[Introduction to Linux | Linux]] is an open-source operating system that enables human interaction with computers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It functions like other operating systems such as Windows or macOS, managing a computer's memory and processes and facilitating communication between hardware and software <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Interacting with the System

At its core, [[Linux system architecture and components | Linux]] contains the [[role_of_linux_kernel_in_operating_systems | kernel]], which handles fundamental operations like process scheduling, device drivers, and memory management <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Beyond the [[role_of_linux_kernel_in_operating_systems | kernel]], applications from the GNU project, such as a [[basic_linux_commands_and_shell_usage | shell]], allow users to interact with the system <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

To begin, users typically open a terminal <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. In the terminal, you might be logged in as the `root` user on a specific machine <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## [[Navigating the Linux file system | Navigating the File System]]

When you first open a terminal, you are usually in the `home` directory of the current user <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This `home` directory can be represented by the tilde character (`~`) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

Key commands for [[navigating_the_linux_file_system | file system navigation]]:
*   `pwd` (Print Working Directory): Shows the full name of your current directory <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   `cd` (Change Directory):
    *   `cd ..`: Navigates up one directory to the root of the [[linux_file_system_hierarchy | file system]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   `cd ~`: Returns to the `home` directory <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   `ls` (List): Prints all subdirectories within the current location <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These often represent critical system files <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## File Operations

[[Basic Bash commands and scripts | Linux]] provides commands to create, edit, and view files:
*   `touch`: Creates a new file <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Text Editors: Files can be edited directly from the terminal using tools like `vi`, `Vim`, `Nano`, or `emacs` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   In `Vim`: Type `i` to enter insert mode, then `Escape`, followed by `:wq` to write (save) and quit the file <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   `cat`: Reads and prints the content of a file to the terminal <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   `grep`: Used to find specific lines within a file that contain a search term or pattern, especially useful for large files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## File Management

Managing files includes checking their size, ownership, and permissions:
*   `du` (Disk Usage): Shows the size of a file <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Permissions: Every file has an owner and a set of permissions <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   `chown`: Changes the owner of a file <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   `chmod`: Changes the permissions of a file <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   `sudo` (Super User Do): Allows a user to run commands with elevated privileges, typically when current permissions are insufficient <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## System Management

*   Package Manager: To install new software, a package manager like Advanced Package Tool (`apt`) can be used. It retrieves code from the cloud and places it in the correct location on your system <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   `history`: Displays a list of previously executed commands <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.