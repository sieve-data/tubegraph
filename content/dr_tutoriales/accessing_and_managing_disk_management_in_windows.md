---
title: Accessing and managing disk management in Windows
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This guide explains how to ensure your computer or laptop [[detecting_external_hard_drives_on_windows_10 | detects USB or external hard drives]] that are not automatically recognized when plugged in <a class="yt-timestamp" data-t="00:00:07"></a>. This solution addresses a common problem where an external drive might not appear in your system <a class="yt-timestamp" data-t="00:01:17"></a>.

## Initial Check for External Drive Detection

First, plug the external hard drive or USB into your computer <a class="yt-timestamp" data-t="00:00:44"></a>. Allow a few seconds for the computer to attempt to detect it <a class="yt-timestamp" data-t="00:00:51"></a>.

To confirm if the drive is detected:
1.  Access "This PC" (also referred to as "our team" or "our computer") <a class="yt-timestamp" data-t="00:01:02"></a>.
2.  Open the folder icon <a class="yt-timestamp" data-t="00:01:05"></a>.
3.  Navigate to the "This PC" section <a class="yt-timestamp" data-t="00:01:07"></a>.
    *   If no external hard drive is detected, only your existing drives (e.g., "windows" and "lenovo disk") will be visible <a class="yt-timestamp" data-t="00:01:10"></a>.

## Accessing Disk Management

To resolve the detection issue, you need to access Disk Management:
1.  In the "This PC" section, right-click on "This PC" <a class="yt-timestamp" data-t="00:01:20"></a>.
2.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26"></a>. This will open a new window <a class="yt-timestamp" data-t="00:01:31"></a>.
3.  In the new window, navigate to the "Storage" section and click on "Disk Management" <a class="yt-timestamp" data-t="00:01:33"></a>.

## Identifying and Assigning the Unassigned Disk

Within Disk Management, you will likely find a disk labeled as "Disk 1" (or similar) that is "not assigned" <a class="yt-timestamp" data-t="00:01:37"></a>. This unassigned space typically represents your external hard drive <a class="yt-timestamp" data-t="00:01:44"></a>.

To assign this unassigned part to the disk:
1.  Right-click on the unassigned section of the disk <a class="yt-timestamp" data-t="00:02:02"></a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04"></a>.
3.  Follow the "New Simple Volume Wizard" steps <a class="yt-timestamp" data-t="00:02:07"></a>:
    *   Click "Next" <a class="yt-timestamp" data-t="00:02:13"></a>.
    *   The wizard will automatically suggest the size of the simple volume (e.g., 953 megabytes) <a class="yt-timestamp" data-t="00:02:14"></a>. Click "Next" <a class="yt-timestamp" data-t="00:02:18"></a>.
    *   Choose a letter to assign to the hard disk (e.g., "S") <a class="yt-timestamp" data-t="00:02:21"></a>. Click "Next" <a class="yt-timestamp" data-t="00:02:31"></a>.

## Formatting the Volume

This is a crucial step to allow your computer to [[detecting_external_hard_drives_on_windows_10 | detect]] the hard drive <a class="yt-timestamp" data-t="00:02:37"></a>.

> [!CAUTION]
> You will need to [[formatting_external_drives_in_windows | format]] the volume internally <a class="yt-timestamp" data-t="00:02:42"></a>. [[formatting_external_drives_in_windows | Formatting]] means all occupied memory with files, documents, etc., will be erased <a class="yt-timestamp" data-t="00:02:47"></a>. If you lose files due to [[formatting_external_drives_in_windows | formatting]], a linked video tutorial is available to help recover them <a class="yt-timestamp" data-t="00:02:52"></a>.

To [[formatting_external_drives_in_windows | format]] the volume:
1.  Ensure "[[formatting_external_drives_in_windows | Format]] this volume with the following settings" is selected <a class="yt-timestamp" data-t="00:03:06"></a>.
2.  Leave the file system as "NTFS" (default) <a class="yt-timestamp" data-t="00:03:09"></a>.
3.  In the "Volume label" field, you can name the drive (e.g., "external hard drive") <a class="yt-timestamp" data-t="00:03:12"></a>.
4.  Select "Perform a quick [[formatting_external_drives_in_windows | format]]" <a class="yt-timestamp" data-t="00:03:19"></a>.
5.  Click "Next" <a class="yt-timestamp" data-t="00:03:22"></a>.

## Finalizing the Process

1.  Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24"></a>.
2.  The disk will now be assigned and no longer appear in blue in Disk Management <a class="yt-timestamp" data-t="00:03:27"></a>.
3.  A folder for the new hard drive will automatically open, showing its name and assigned gigabytes (e.g., "Subscribe External Hard Drive 931 gigabyte") <a class="yt-timestamp" data-t="00:03:33"></a>.
4.  Returning to "This PC," your new hard drive will now be visible and accessible <a class="yt-timestamp" data-t="00:03:45"></a>.

From this point forward, your computer will perfectly [[detecting_external_hard_drives_on_windows_10 | detect]] this external drive every time you plug it in <a class="yt-timestamp" data-t="00:03:47"></a>.