---
title: Formatting an external hard drive for detection
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

This tutorial explains how to make your computer detect a USB drive or external hard drive that is not being recognized upon connection <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This solution addresses common issues where an external hard drive is plugged in but not detected <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Initial Detection Check

First, plug the external hard drive or USB into your computer <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Wait a few seconds for the computer to attempt detection <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To check if the drive is detected:
1.  Access "This PC" by opening the folder symbol (File Explorer) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  Navigate to the "This PC" section <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
3.  Observe if the external hard drive appears alongside your other drives (e.g., Windows and Lenovo disk) <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. If it's not listed, proceed to the next steps <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Accessing Disk Management

To enable detection, you'll need to access Disk Management:
1.  Right-click on "This PC" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  Select "Manage" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
3.  In the Computer Management window that opens, navigate to the "Storage" section <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
4.  Click on "Disk Management" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Identifying and Initializing the Drive

Within Disk Management, you should see your external hard drive, often labeled as "Disk 1" with unallocated space <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This unassigned space needs to be configured <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Creating a New Simple Volume

To make the drive usable, you'll create a new simple volume:
1.  Right-click on the unallocated space of the external drive <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Select "New Simple Volume" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  The "New Simple Volume Wizard" will appear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Click "Next" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
4.  Accept the default volume size, then click "Next" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
5.  [[assigning_a_drive_letter_to_an_external_hard_drive | Assign a drive letter]] to the disk (e.g., 'S') <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Click "Next" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Formatting the Volume

This is a critical step that prepares the drive for use by your computer:
1.  The wizard will prompt you to format the volume <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
2.  **Important Note**: [[recovering_files_from_formatted_drives | Formatting]] the drive means all existing data (files, documents, etc.) on that partition will be erased <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. If you had files on the drive before it stopped being detected, a separate video tutorial is available to help [[recovering_files_from_formatted_drives | recover lost files]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
3.  Keep the file system as "NTFS" and leave other settings as default <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  In the "Volume label" field, you can name the drive (e.g., "External Hard Drive") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
5.  Ensure "Perform a quick format" is checked <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
6.  Click "Next" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
7.  Click "Finish" to complete the process <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Verification

Once finished, the drive should now be assigned and appear in Disk Management (no longer in blue) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. If you go back to "This PC," you will see your newly formatted external hard drive with its assigned letter and specified name (e.g., "External Hard Drive S:") <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

From now on, your computer will perfectly detect this external hard drive every time you connect it <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.