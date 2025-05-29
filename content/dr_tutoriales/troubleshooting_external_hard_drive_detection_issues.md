---
title: Troubleshooting external hard drive detection issues
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This tutorial guides you on how to make your computer or laptop detect USB drives or external hard drives that are not being recognized when plugged in <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The issue often arises when an external hard drive is plugged in but doesn't work <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Initial Steps for [[detecting_external_hard_drives_on_windows_10 | Detecting External Hard Drives]]

First, plug the external hard drive or USB into your computer <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Allow a few seconds for the computer to try and detect it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. If it's not detected, you'll need to proceed with further steps <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

To check if the drive is detected, access "This PC" (or "My Computer") by opening a folder symbol <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. In the "This PC" section, you'll typically see your Windows and Lenovo hard disks, but not the external one if it's not detected <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## [[accessing_and_managing_disk_management_in_windows | Accessing Disk Management]]

To resolve the detection problem, you will need to [[accessing_and_managing_disk_management_in_windows | access Disk Management]]:
1.  Go to "This PC" and right-click on it <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
3.  A new window will open; navigate to the "Storage" part and click on "Disk Management" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Identifying the Undetected Drive

In Disk Management, you should find a disk (e.g., "Disk 1") that is not assigned <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This unassigned space typically represents your external hard drive, which might show an unusual size like 200 megabytes, even if it's a 1-terabyte drive (usually closer to 900+ GB) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## [[formatting_external_drives_in_windows | Assigning a Simple Volume and Formatting]]

The next step is to assign this unassigned part directly to the record, which involves [[formatting_external_drives_in_windows | formatting external drives in Windows]]:
1.  Right-click on the unassigned disk <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Follow the "New Simple Volume Wizard":
    *   Click "Next" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Leave the default simple volume size (e.g., 953 megabytes) and click "Next" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Assign a letter to the hard disk (e.g., "S") and click "Next" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

    > [!caution] Formatting Warning
    > This step is crucial because it requires [[formatting_external_drives_in_windows | formatting the volume]] for your computer to detect the drive <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. [[formatting_external_drives_in_windows | Formatting]] means all occupied memory with files and documents will be erased <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. However, you can recover lost files using a separate tutorial <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    >
    > For more information, refer to the video tutorial on [[recovering_lost_files_after_formatting | recovering lost files after formatting]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

4.  On the format screen, select "Format this volume with the following settings" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>:
    *   Leave "NTFS" and "Default" as they are <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Enter a volume label, such as "external hard drive" <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Select "Quick format" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
5.  Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Verification

After completing these steps, the disk should appear assigned in Disk Management (no longer blue) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. You can then go back to "This PC," and your external hard drive, now labeled and with its correct storage size (e.g., 931 gigabytes), will be detected <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. From now on, your computer will perfectly detect the external hard drive every time you plug it in <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## Related Content

For additional tutorials:
*   Learn how to [[troubleshooting_bluetooth_connections | activate Bluetooth on Windows 7]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   If you've lost files due to formatting, a video tutorial is available to help you [[recovering_lost_files_after_formatting | recover them quickly]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.