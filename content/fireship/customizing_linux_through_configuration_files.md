---
title: Customizing Linux through configuration files
videoId: 42iQKuQodW4
---

From: [[fireship]] <br/> 

The [[introduction_to_linux | Linux]] file system is organized according to the File System Hierarchy Standard <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. To navigate this structure, users can employ [[basic_linux_commands_and_operations | commands]] like `cd` to change directories and `ls` to list contents <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Understanding this structure is crucial for customizing the system.

## System-Wide Configuration: The `/etc` Directory

To customize the behavior of software across the entire [[introduction_to_linux | Linux]] system, the `/etc` directory is used <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The name "etc" is often interpreted as "editable text configuration" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

*   Many files within `/etc` end with `.conf` <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   These are typically text-based configuration files that can be modified with a text editor <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## User-Specific Configuration: The `/home` Directory

[[introduction_to_linux | Linux]] is designed to support multiple users <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Each user on the system has a dedicated folder within the `/home` directory <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

*   A user's home directory contains their personal files, configuration settings, and software <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Modifying these files generally requires being logged in as that specific user or as the root user <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   When a terminal session opens, the user's home directory is the default starting location, often represented by a tilde (squiggly) symbol `~` in the file path <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Custom Binaries: The `/usr/local` Directory

Within the `/usr` directory, which holds non-essential applications intended for the end user <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, there is a `local` directory <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

*   `/usr/local` is the designated place for binaries that users compile manually <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   This location prevents conflicts with software installed by system package managers <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Executables and the `PATH` Environment Variable

The various executable programs (binaries) found in directories like `/bin`, `/sbin`, `/usr/bin`, `/usr/sbin`, and `/usr/local/bin` are mapped together by the `PATH` environment variable <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This mapping allows users to execute these commands from any directory in the terminal <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To find the full path of an executable within the [[navigating_the_linux_file_system | file system]], the `which` command can be used, followed by the binary's name (e.g., `which ls`) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.