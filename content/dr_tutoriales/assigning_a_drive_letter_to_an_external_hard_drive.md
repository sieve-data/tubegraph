---
title: Assigning a drive letter to an external hard drive
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This tutorial outlines the process for making your computer detect an external USB or hard drive that is not automatically recognized upon plugging it in <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This often occurs when an external hard drive is plugged in but doesn't work <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Checking for Detection

First, plug the external hard drive or USB into your computer <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Wait a few seconds for the computer to attempt detection <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To confirm if the drive is detected:
1.  Access "This PC" (or "My Computer") by opening the folder symbol <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
2.  Navigate to the "This PC" section <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
3.  If the external hard drive is not listed, it means it hasn't been detected <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Accessing Disk Management

To make the computer detect the drive, you'll need to manage its disk properties:
1.  Go to "This PC" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  Right-click on "This PC" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
3.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
4.  In the new window, navigate to the "Storage" section <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
5.  Click on "Disk Management" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Identifying and Assigning the Drive

In Disk Management, you should find the external hard drive listed, possibly as "Disk 1" or similar, and it will appear as "Unassigned" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This unassigned space needs to be given a drive letter <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Creating a Simple Volume (Formatting)

1.  Right-click on the unassigned space on the external hard drive <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Follow the "New Simple Volume Wizard" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>:
    *   Click "Next" on the initial wizard screen <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Accept the default volume size by clicking "Next" <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   Choose a letter to assign to the disk, such as "S", then click "Next" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   At the "Format Partition" step, it is crucial to format the volume for your computer to detect the hard drive <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
        *   **Important Note**: [[recovering_files_from_formatted_drives | Formatting]] means all data previously on the drive will be lost <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. If you need to recover files, a separate video tutorial is available that explains how to [[recovering_files_from_formatted_drives | recover all lost files]] easily <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Set the following format settings <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>:
        *   File system: NTFS (default)
        *   Allocation unit size: Default
        *   Volume label: Enter a descriptive name (e.g., "external hard drive")
        *   Check "Perform a quick format" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Verification

Once completed, the drive will be assigned and no longer appear in blue in Disk Management <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A folder may automatically open, showing the newly assigned hard drive with its name (e.g., "Hard Drive S") and capacity <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. If you return to "This PC", your external hard drive will now be listed and detected whenever it's plugged into your computer <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.