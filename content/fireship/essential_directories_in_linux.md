---
title: Essential directories in Linux
videoId: 42iQKuQodW4
---

From: [[fireship]] <br/> 

The [[linux_file_system_hierarchy|Linux file system]] is structured as a "cryptic labyrinth of directories" defined by the [[linux_file_system_hierarchy|File System Hierarchy Standard]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. You can [[navigating_the_linux_file_system|navigate through it]] using the [[basic_linux_commands_and_operations|`change directory` (cd) command]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Typing `cd /` will drop you into the root directory <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The contents of any directory can be listed using the [[basic_linux_commands_and_operations|`ls` command]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Key Directories

### `/bin`
The `/bin` directory contains [[role_of_binaries_and_executables_in_linux|binaries or executables]] that are essential for the entire [[linux_system_architecture_and_components|operating system]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These can be run from the [[basic_linux_commands_and_shell_usage|command line]] at any time <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples include `gzip`, `curl`, and even the `ls` command itself <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### `/sbin`
The `/sbin` directory holds system [[role_of_binaries_and_executables_in_linux|binaries]] that should only be executed by the root user <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Examples include `mount` or `delete user` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### `/lib`
Common libraries shared by many [[role_of_binaries_and_executables_in_linux|binaries]] are stored in the `/lib` directory <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### `/usr`
The `/usr` directory (short for "user") has its own `/bin` and `/sbin` directories <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The [[role_of_binaries_and_executables_in_linux|binaries]] or applications found here are considered non-essential to the [[linux_system_architecture_and_components|operating system]] itself and are intended for the end user <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

*   `/usr/local`: This subdirectory under `/usr` contains any [[role_of_binaries_and_executables_in_linux|binaries]] that you compile manually <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It provides a safe location that won't conflict with software installed by a system package manager <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

All these [[role_of_binaries_and_executables_in_linux|binaries]] are mapped together using the `PATH` environment variable, allowing them to be executed from any directory in the terminal <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. To find where a binary lives, use `which` followed by the binary name (e.g., `which ls`) to view its full path <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### `/etc`
The `/etc` directory stands for "etc" or "editable text configuration" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Many files within this directory end in `.conf` and are typically text-based configuration files that can be modified in a text editor to customize system software behavior <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### `/home`
As an [[linux_system_architecture_and_components|operating system]], [[introduction_to_linux|Linux]] supports multiple users <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The `/home` directory contains a folder for each user registered on the system <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This user-specific folder contains the user's files, configurations, and software <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. To modify it, you must be logged in as that user or as the root user <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The tilde `~` symbol represents your normal starting location when opening a terminal session <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### `/boot`
The `/boot` directory contains the files necessary to boot the system, including the [[role_of_linux_kernel_in_operating_systems|Linux kernel]] itself <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### `/dev`
`/dev` stands for "device files" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. In this directory, you can interface with hardware or drivers as if they were regular files, for instance, creating disk partitions or interacting with a floppy drive <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### `/opt`
The `/opt` directory contains optional or add-on software <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, though users rarely interact with it directly <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### `/var`
`/var` contains variable files that change as the [[linux_system_architecture_and_components|operating system]] is being used <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Examples include logs and cache files <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### `/tmp`
`/tmp` is designated for temporary files <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, which are not persisted between reboots <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### `/proc`
The `/proc` directory is an "illusionary file system" that doesn't actually exist on the disk <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Instead, it is created in memory on the fly by the [[role_of_linux_kernel_in_operating_systems|Linux kernel]] to keep track of running processes <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.