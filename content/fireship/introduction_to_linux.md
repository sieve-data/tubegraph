---
title: Introduction to Linux
videoId: rrB13utjYV4
---

From: [[fireship]] <br/> 

[[history_of_linux | Linux]] is an open-source operating system that enables human interaction with computers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was [[history_and_creation_of_linux | created]] in 1991 by Linus Torvalds, a student at the University of Helsinki <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Torvalds' objective was to develop a free version of the Minix operating system, which itself was based on Unix <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Modern Usage
Today, [[history_of_linux | Linux]] is widely adopted in various environments, including the vast majority of web servers <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It is also used in embedded applications like smart TVs, mobile devices running Android, and is considered a top choice for personal computers <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Users can choose from numerous [[linux_distributions_and_their_origins | distros]] (distributions) such as Debian, Arch, and Fedora <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## How Linux Works
Like Windows or Mac OS, [[history_of_linux | Linux]] functions as an operating system by managing a computer's memory and processes, facilitating communication between hardware and software <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Core Components
When a [[history_of_linux | Linux]] machine starts, a bootloader first loads the system into memory <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. At its core is the [[linux_kernel_and_its_role | kernel]], which serves as the foundational component from which the rest of the operating system develops <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The [[linux_kernel_and_its_role | kernel]] is organized into smaller subsystems, including:
*   A process scheduler <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Device drivers <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   A memory manager <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

These subsystems are exposed via a system call interface, which is further wrapped by the C standard Library, providing an API for user applications to interact with <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Beyond the [[linux_kernel_and_its_role | kernel]], applications that make the operating system usable for humans are primarily supplied by the GNU project <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. These include:
*   A [[basic_linux_commands_and_shell_usage | shell]] for command-line interaction with the [[linux_kernel_and_its_role | kernel]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>
*   Windowing systems for desktop environments <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Developer utilities <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Countless other applications <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

## Getting Started with Linux
To begin using [[history_of_linux | Linux]], one must first install a preferred [[linux_distributions_and_their_origins | Linux distro]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### [[basic_linux_commands_and_operations | Basic Commands]] and Operations
After installation, opening the terminal reveals that users are typically logged in as the root user on the specific [[history_of_linux | Linux]] machine <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

*   **Current Directory:** The home directory of the root user is represented by a tilde (`~`) character <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Its full name can be shown with the `pwd` (print working directory) [[basic_linux_commands_and_operations | command]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Navigation:**
    *   Use `cd ..` to change directories and move to the root of the file system <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
    *   The `ls` [[basic_linux_commands_and_operations | command]] lists all subdirectories in the current location, which include critical system files <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   To return to the home directory, use `cd ~` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **File Manipulation:**
    *   Create a new file with `touch` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   Edit files directly from the terminal using tools like `vi`, `vim`, `nano`, or `emacs` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For example, in Vim, one types `i` to insert, then content, then `Escape`, followed by `:wq` to write and quit <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   Read the content of a file using the `cat` [[basic_linux_commands_and_operations | command]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   For large files, `grep` can be used to find lines containing a specific search term or pattern <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   The `du` (disk usage) [[basic_linux_commands_and_operations | command]] shows the size of a file <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Permissions:** Every file has an owner and assigned permissions <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
    *   `chown` changes the owner of a file <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   `chmod` modifies file permissions <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   If a current user lacks proper permissions, `sudo` (super user do) can be placed before any [[basic_linux_commands_and_operations | command]] to execute it with elevated privileges <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Software Installation:** New software can be installed using a package manager like `apt` (Advanced Package Tool), which retrieves code from the cloud and places it in the correct system location <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Command History:** The `history` [[basic_linux_commands_and_operations | command]] displays a list of previously entered [[basic_linux_commands_and_operations | commands]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.