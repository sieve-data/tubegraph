---
title: Detecting external hard drive on Windows 10
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This tutorial explains how to resolve issues where a computer, PC, or laptop does not detect a plugged-in USB or external hard drive <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The problem often arises when an external hard drive is plugged in but remains undetected <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

> [!NOTE]
> Before starting, you can find a separate video tutorial on how to [[activating_bluetooth_on_windows_10 | activate the Bluetooth]] of a Windows 7 computer in the simplest way possible <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Troubleshooting Steps

1.  **Plug in the External Drive**
    First, plug the external hard drive or USB into the computer <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Allow a few seconds for the computer to attempt detection <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

2.  **Verify Non-Detection**
    Access "This PC" (or "My Computer") by opening a folder symbol <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. In the "This PC" section, confirm that the external hard drive is not detected <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Typically, only internal drives like "Windows" and "Lenovo hard disk" will appear <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

3.  **Access Disk Management**
    Right-click on "This PC" (or "My Computer") <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. A new window will open; navigate to the "Storage" section and click on "Disk Management" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This tool is essential for [[managing_disk_partitions_in_windows_10 | managing disk partitions in Windows 10]].

4.  **Identify the Unassigned Disk**
    In Disk Management, locate "Disk 1" (or similar) which appears as unassigned <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This represents the external hard drive <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It may show a small partition (e.g., 200 MB) that is not part of the main storage <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. The goal is to [[assigning_a_drive_letter_to_an_external_hard_drive | assign this unassigned part directly to the disk]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

5.  **Create a New Simple Volume**
    *   Right-click on the unassigned disk and select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   Follow the "New Simple Volume Wizard" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Click "Next" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Keep the default simple volume size <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> (e.g., 953 MB) and click "Next" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Assign a drive letter to the disk (e.g., 'S') <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Click "Next" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

6.  **Format the Volume**
    *   The wizard will prompt you to [[formatting_an_external_hard_drive_for_detection | format this volume]] for the computer to detect the drive <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This applies to hard drives, pen drives, or other devices <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Formatting means that all occupied memory with files and documents will be cleared <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Set the file system to NTFS (default) and leave the allocation unit size as default <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   In the "Volume label" field, enter a name for the drive (e.g., "external hard drive") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Enable "Perform a quick format" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Click "Next" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Finally, click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

> [!WARNING]
> While formatting erases data, it is possible to [[recovering_files_from_formatted_drives | recover all lost memory and files]] easily and simply <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. A separate video tutorial provides instructions for this, ensuring recovery <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

7.  **Confirm Detection**
    After formatting, the disk will appear assigned in Disk Management <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A new folder will open, showing the hard drive with its assigned letter (e.g., 'S') and name (e.g., "external hard drive"), displaying its full capacity (e.g., 931 GB) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The drive will now appear in "This PC" and will be detected every time it's plugged into the computer <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.