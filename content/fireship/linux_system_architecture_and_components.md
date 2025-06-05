---
title: Linux system architecture and components
videoId: rrB13utjYV4
---

From: [[fireship]] <br/> 
[[Introduction to Linux | Linux]] is an open-source [[Role of Linux Kernel in Operating Systems | operating system]] that enables human interaction with computers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was developed in 1991 by University of Helsinki student Linus Torvalds <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Torvalds' objective was to create a free version of the Minix [[Role of Linux Kernel in Operating Systems | operating system]], which itself was based on Unix <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

Today, [[Introduction to Linux | Linux]] is ubiquitous, powering the vast majority of web servers, embedded applications (like smart TVs), mobile devices running Android, and is a strong option for personal computers <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Users can choose from many different [[Linux distribution options | Linux distributions]] (distros) such as Debian, Arch, and Fedora <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Role of Linux as an Operating System
Similar to Windows or Mac OS, [[Introduction to Linux | Linux]] is an [[Role of Linux Kernel in Operating Systems | operating system]] that manages a computer's memory and processes, facilitating communication between hardware and software <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Core Architecture
When a [[Introduction to Linux | Linux]] machine is started, a bootloader first loads the system into memory <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. At its core, [[Introduction to Linux | Linux]] features the [[Linux kernel and its role | kernel]], which serves as the foundational component from which the rest of the [[Role of Linux Kernel in Operating Systems | operating system]] develops <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

The [[Linux kernel and its role | kernel]] is organized into several smaller subsystems <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>:
*   Process scheduler <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Device drivers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Memory manager <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>

These subsystems are exposed via a system call interface, which is further wrapped by the C standard library. This library provides an Application Programming Interface (API) for user applications to interact with the [[Linux kernel and its role | kernel]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Beyond the Kernel
Beyond the [[Linux kernel and its role | kernel]], applications are provided, primarily by the GNU project, to make the [[Role of Linux Kernel in Operating Systems | operating system]] usable for humans <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. These include:
*   A shell for command-line interaction with the [[Linux kernel and its role | kernel]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>
*   Windowing systems on the desktop <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Developer utilities <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Numerous other applications <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

### Interacting with the System
To get started with [[Introduction to Linux | Linux]], users install their preferred [[Linux distribution options | Linux distribution]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Interaction commonly occurs through the terminal, where users are often logged in as the root user on a specific [[Introduction to Linux | Linux]] machine <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Initially, a user might find themselves in the root user's home directory, represented by the tilde (~) character <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The full path of the current working directory can be shown using the `pwd` command <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. To navigate to the root of the [[Linux file system hierarchy | file system]], the `cd ..` command is used <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The `ls` command lists all subdirectories in the current location, which often include critical system files at the [[Linux file system hierarchy | file system]] root <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Users can return to their home directory with `cd ~` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Key System Commands
[[Basic Linux commands and operations | Basic Linux commands]] are essential for managing files and processes:
*   **`touch`**: Creates a new file <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Text Editors (e.g., `vi`, `Vim`, `Nano`, `Emacs`)**: Used to edit files directly from the terminal <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For example, in Vim, one types 'i' for insert mode, then presses 'Escape' and `:wq` to write and quit <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **`cat`**: Reads and displays the content of a file <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **`grep`**: Searches for lines containing a specific term or pattern within a file <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **`du` (disk usage)**: Shows the size of a file <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **`chown`**: Changes the owner of a file <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **`chmod`**: Modifies the permissions assigned to a file <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **`sudo` (super user do)**: Executes a command with elevated privileges if the current user lacks proper permissions <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **`history`**: Recaps previously entered commands <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Software Management
New software can be installed using a package manager, such as Advanced Package Tool (APT). A package manager retrieves software code from the cloud and places it in the correct location on the system <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.