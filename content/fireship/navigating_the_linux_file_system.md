---
title: Navigating the Linux file system
videoId: 42iQKuQodW4
---

From: [[fireship]] <br/> 

The [[linux_file_system_hierarchy | Linux file system]] is a complex structure of directories defined by the [[linux_file_system_hierarchy | File System Hierarchy Standard]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Basic Navigation

To navigate through the file system, you use the [[basic_linux_commands_and_shell_usage | change directory command]] `cd` <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
*   `cd /` will take you to the root directory <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
Once in a directory, the [[basic_linux_commands_and_shell_usage | `ls` command]] can be used to list its contents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## [[essential_directories_in_linux | Essential Directories]]

### `/bin` and `/sbin` (Binaries)

*   **`/bin`**: Contains [[role_of_binaries_and_executables_in_linux | binaries]] or [[role_of_binaries_and_executables_in_linux | executables]] that are essential to the entire [[introduction_to_linux | operating system]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. These can be [[basic_linux_commands_and_operations | run]] from the [[basic_linux_commands_and_shell_usage | command line]] at any time <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Examples include `gzip`, `curl`, and `ls` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **`/sbin`**: Contains [[role_of_binaries_and_executables_in_linux | system binaries]] that should only be [[basic_linux_commands_and_operations | executed]] by the root user <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Examples include `mount` or `delete user` <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### `/lib` (Libraries)

*   Many [[role_of_binaries_and_executables_in_linux | binaries]] may share common libraries, which are stored in the `/lib` directory <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### `/usr` (User Programs)

The `/usr` (user) directory has its own `/bin` and `/sbin` directories <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   The [[role_of_binaries_and_executables_in_linux | binaries]] or applications here are non-essential to the [[introduction_to_linux | operating system]] itself and are intended for the end user <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   A `local` directory under `/usr` contains any [[role_of_binaries_and_executables_in_linux | binaries]] that you compile manually <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This provides a safe place that won't conflict with software installed by a system package manager <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### PATH Environment Variable

All these [[role_of_binaries_and_executables_in_linux | binaries]] get mapped together with the `PATH` environment variable <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, allowing you to [[basic_linux_commands_and_operations | execute]] them from any directory in the [[basic_linux_commands_and_shell_usage | terminal]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   To find where a [[role_of_binaries_and_executables_in_linux | binary]] lives, [[basic_linux_commands_and_operations | run `which`]] followed by the [[role_of_binaries_and_executables_in_linux | binary]] name to view its full path in the [[linux_file_system_hierarchy | file system]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### `/etc` (Editable Text Configuration)

The `/etc` directory, which stands for "editable text configuration," is where you can [[customizing_linux_through_configuration_files | customize the behavior of the software]] on your system <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   Many of these [[customizing_linux_through_configuration_files | files]] end in `.conf` and are typically just text-based [[customizing_linux_through_configuration_files | config files]] that you can modify in your editor <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### `/home` (User Data)

As an [[introduction_to_linux | operating system]], [[introduction_to_linux | Linux]] can support multiple users <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   In the `/home` directory, you'll find a folder named after each user registered on the system <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   This folder contains the files, configuration, and software for that specific user <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   You need to be logged in as that user or as a root user to modify its contents <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   When you open a [[basic_linux_commands_and_shell_usage | terminal]] session, your normal starting location is represented by a tilde `~` (squiggly) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Other Important Directories at Root (`/`)

*   **`/boot`**: Contains the files needed to [[linux_system_architecture_and_components | boot]] the system, including the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] itself <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **`/dev`**: Stands for device files <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Here, you can interface with [[linux_system_architecture_and_components | hardware]] or [[linux_system_architecture_and_components | drivers]] as if they were regular files <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Examples include creating disk partitions or interfacing with a floppy drive <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **`/opt`**: Contains optional or add-on software <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. You will rarely interact with it directly <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **`/var`**: Contains variable files that change as the [[introduction_to_linux | operating system]] is being used, such as logs and cache files <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **`/tmp`**: Is for temporary files that won't be persisted between reboots <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **`/proc`**: An illusionary [[linux_file_system_hierarchy | file system]] that doesn't actually exist on the disk <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. It is created in memory on the fly by the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] to keep track of running processes <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.