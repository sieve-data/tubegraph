---
title: Linux file system hierarchy
videoId: 42iQKuQodW4
---

From: [[fireship]] <br/> 

The [[navigating_the_linux_file_system | Linux file system]] is a complex structure defined by the File System Hierarchy Standard <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Navigating the File System

To [[navigating_the_linux_file_system | navigate]] the file system, you can use the `cd` (change directory) command <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
*   Typing `cd /` will take you to the root directory <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   The `ls` command can be used to list the contents of a directory <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Essential Directories

Here's an overview of [[essential_directories_in_linux | essential directories]] found in the [[navigating_the_linux_file_system | Linux file system]]:

### `/` (Root Directory)

This is the top-level directory of the file system <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. All other directories branch off from here.

### `/bin`

The `/bin` directory contains binaries or executables that are essential to the entire [[linux_system_architecture_and_components | operating system]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These binaries, such as `gzip`, `curl`, and `ls`, can be run from the command line at any time <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### `/sbin`

This directory holds system binaries that should only be executed by the root user, such as `mount` or `delete user` <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### `/lib`

The `/lib` directory stores common libraries that are shared among many binaries <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### `/usr` (User Directory)

The `/usr` directory contains its own `bin` and `sbin` directories <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The binaries and applications here are non-essential to the [[linux_system_architecture_and_components | operating system]] itself and are intended for the end user <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

#### `/usr/local`

Found under `/usr`, this directory contains any binaries that you compile manually <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It provides a safe place for these binaries to avoid conflicts with software installed by a system package manager <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### Path Environment Variable

All these binaries are mapped together using the `PATH` environment variable <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, allowing them to be executed from any directory in the terminal <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. To find where a binary lives, you can run `which` followed by the binary name (e.g., `which ls`) to view its full path in the file system <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### `/etc` (Editable Text Configuration)

The `/etc` directory stands for "editable text configuration" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Many files here end in `.conf` and are typically text-based configuration files that can be modified in an editor to customize software behavior <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### `/home`

As an [[introduction_to_linux | operating system]], [[introduction_to_linux | Linux]] supports multiple users <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The `/home` directory contains a folder for each user registered on the system <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Each user's folder contains their files, configuration, and software <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. You must be logged in as that user or as the root user to modify its contents <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The squiggly `~` symbol represents your normal starting location when opening a terminal session <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### `/boot`

This directory contains the files necessary to boot the system, including the [[linux_kernel_and_its_role | Linux kernel]] itself <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### `/dev` (Device Files)

The `/dev` directory contains device files, allowing you to interface with hardware or drivers as if they were regular files <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Examples include creating disk partitions or interfacing with a floppy drive <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### `/opt` (Optional or Add-on Software)

The `/opt` directory contains optional or add-on software <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a> and is rarely interacted with by users <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### `/var` (Variable Files)

This directory holds variable files that change as the [[linux_system_architecture_and_components | operating system]] is being used, such as logs and cache files <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### `/tmp` (Temporary Files)

The `/tmp` directory is used for temporary files that are not persisted between reboots <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### `/proc` (Processes)

The `/proc` directory is an illusionary file system that does not physically exist on the disk <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Instead, it is created in memory on the fly by the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] to keep track of running processes <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.