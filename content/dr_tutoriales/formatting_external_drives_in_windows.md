---
title: Formatting external drives in Windows
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This guide provides a step-by-step tutorial on how to ensure your computer [[detecting_external_hard_drives_on_windows_10 | detects USB or external hard drives]] that are not automatically recognized upon plugging them in <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process often involves formatting the drive, which is crucial for its proper function within the Windows operating system <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Initial Detection Problem

Sometimes, when an external hard drive or USB device is plugged into a computer, it may not be detected <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Even after plugging it in and waiting a few seconds, the computer might fail to recognize it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To confirm this, you can access "This PC" (also known as "My Computer") by opening the folder symbol. If no external hard drive is listed, it means your computer has not detected it <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Resolving Detection Issues Through Disk Management

The primary method to resolve non-detection issues is to utilize Windows's Disk Management utility <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Accessing Disk Management

1.  Navigate to "This PC" (or "My Computer") <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  Right-click on "This PC" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
3.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
4.  In the "Computer Management" window that opens, go to the "Storage" section <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
5.  Click on "Disk Management" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Identifying the Unassigned Disk

Within Disk Management, you should be able to locate the external hard drive <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. It will typically appear as an "unassigned" disk, meaning it does not have a drive letter or file system assigned to it <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For instance, a 1TB drive might show up as 900-something GB and unassigned <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Assigning and Formatting the Volume

To make the external drive detectable and usable, you need to assign it a partition and format it.

1.  Right-click on the unassigned partition of the external drive <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Follow the "New Simple Volume Wizard" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>:
    *   Click "Next" on the welcome screen <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Leave the default volume size, then click "Next" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Assign a drive letter to the disk (e.g., 'S') and click "Next" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   On the formatting screen, this is crucial <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>:
        *   Choose to "Format this volume" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
        *   Understand that "formatting" means all existing data on the drive will be erased <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
        *   If you have lost files due to formatting, there are methods to [[recovering_lost_files_after_formatting | recover them]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
        *   Leave the file system as "NTFS" (default) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
        *   You can change the "Volume label" (e.g., "External Hard Drive") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
        *   Ensure "Perform a quick format" is checked <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
        *   Click "Next" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Verification

After completing these steps, the external hard drive should now be assigned, indicated by its status changing from "unassigned" to showing its capacity and assigned drive letter <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. You can then navigate back to "This PC," and your external hard drive will appear, ready for use <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. From now on, your computer will perfectly [[detecting_external_hard_drives_on_windows_10 | detect the external drive]] every time you plug it in <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.