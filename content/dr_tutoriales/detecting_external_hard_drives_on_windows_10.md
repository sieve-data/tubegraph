---
title: Detecting external hard drives on Windows 10
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

It is a common issue for Windows computers, including PCs and laptops, to not detect connected USB or external hard drives <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This can happen even when the drive is properly plugged in <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Initial Steps when a drive is not detected

First, plug the external hard drive or USB into your computer <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Allow a few seconds for the computer to try and detect it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. If it doesn't appear, you'll need to proceed with further steps <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

To check if the drive is recognized, open "This PC" (also referred to as "Our Team") by clicking on the folder symbol <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. If the external hard drive is not listed alongside your existing drives (like Windows or Lenovo disks), it means it's not detected <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Accessing Disk Management

To make your computer detect the drive, you'll need to access Disk Management:
1.  Navigate to "This PC" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  Right-click on "This PC" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
3.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
4.  In the Computer Management window that opens, go to the "Storage" section <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
5.  Click on "Disk Management" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

This process is part of [[accessing_and_managing_disk_management_in_windows | accessing and managing disk management in Windows]].

## Identifying and Assigning the External Drive

Within Disk Management, you will likely find a disk (e.g., "Disk 1") that is "not assigned" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This is usually your external hard drive, even if its reported size (e.g., 200 megabytes) does not match its actual capacity (e.g., 1 terabyte) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

To make the computer recognize the drive, you must assign this unassigned part:
1.  Right-click on the "not assigned" section of the disk <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Follow the steps in the "New Simple Volume Wizard" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Click "Next" to accept the default size of the simple volume <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Assign a drive letter to the hard disk (e.g., 'S') <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Click "Next" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   **Crucially, you must format this volume** for your computer to detect the hard drive or other devices like a pendrive <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
        *   Formatting means that all existing files and documents on the drive will be lost <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
        *   You can recover lost files through a separate video tutorial that explains how to recover all memory and files quickly and simply <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Leave the file system as "NTFS" and the allocation unit size as "Default" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Provide a "Volume label" for the drive (e.g., "external hard drive") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Select "Quick format" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Post-Formatting

Once the process is complete, the disk will be assigned and will no longer appear as "not assigned" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A folder for the newly formatted hard drive will appear, showing its correct capacity (e.g., 931 gigabytes) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

The external hard drive will now be visible under "This PC" <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, and it will be detected perfectly every time you connect it to your computer <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Related Guides:
*   [[activating_bluetooth_in_windows_10 | How to activate Bluetooth in Windows 7]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Information on recovering lost files after formatting <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>