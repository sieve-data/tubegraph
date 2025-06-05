---
title: Role of binaries and executables in Linux
videoId: 42iQKuQodW4
---

From: [[fireship]] <br/> 

The [[introduction_to_linux | Linux]] file system, defined by the File System Hierarchy Standard, organizes various types of files, including binaries and executables, which are crucial for the operating system's functionality <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These executable programs allow users to interact with the system and perform various operations.

## Essential Binaries

At the root of the file system, the `/bin` directory contains binaries or executables that are essential for the entire [[linux_system_architecture_and_components | operating system]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. These can be run from the command line at any time <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples include `gzip`, `curl`, and even the `ls` command used to list directory contents <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### System Binaries

The `/sbin` directory holds system binaries that are typically intended for execution only by the root user <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a> <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Examples include `mount` and `delete user` commands <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## User-Specific and Optional Binaries

### User Binaries

The `/usr` directory, often referred to as the "user" directory, contains its own `bin` and `sbin` subdirectories <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The binaries and applications found here are generally non-essential to the core [[linux_system_architecture_and_components | operating system]] and are instead intended for the end user <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Local Binaries

Within `/usr`, there is also a `/local` directory <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This location is designed to store binaries that a user might compile manually <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It provides a safe space for these custom binaries, preventing conflicts with software installed by the system's package manager <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How Binaries are Accessed

All these various binary directories are mapped together through the `PATH` environment variable <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This mapping enables users to execute binaries from any directory in the terminal without specifying their full path <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. To discover the full path of a binary, the `which` command can be used, followed by the binary's name <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Related Directories and Their Role with Binaries

*   **`/lib`**: Contains common libraries that many binaries may share <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a> <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **`/etc`**: Stands for "etc" or "editable text configuration" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a> <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This directory holds configuration files, often ending in `.conf`, which are typically text-based and can be modified by users to customize software behavior <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **`/home`**: As an [[introduction_to_linux | operating system]], [[introduction_to_linux | Linux]] supports multiple users <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The `/home` directory contains a folder for each registered user, holding their files, configurations, and software <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a> <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Modifications usually require being logged in as that user or as the root user <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The squiggly character `~` represents a user's normal starting location in a terminal session <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **`/boot`**: Contains files necessary to boot the system, including the [[linux_kernel_and_its_role | Linux kernel]] itself <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **`/dev`**: Stands for "device files" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Here, users can interface with hardware or drivers as if they were regular files, for tasks like creating disk partitions or interacting with a floppy drive <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **`/opt`**: Holds optional or add-on software <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **`/var`**: Contains variable files that change as the [[linux_system_architecture_and_components | operating system]] is used, such as logs and cache files <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **`/tmp`**: Used for temporary files that are not persisted between reboots <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a> <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **`/proc`**: An illusionary file system created in memory by the [[linux_kernel_and_its_role | Linux kernel]] to track running processes <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a> <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.