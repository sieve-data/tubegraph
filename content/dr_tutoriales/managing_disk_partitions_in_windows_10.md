---
title: Managing disk partitions in Windows 10
videoId: fwqH2nxikgU
---

From: [[dr_tutoriales]] <br/> 

When a computer or laptop fails to [[detecting_external_hard_drive_on_windows_10 | detect a USB or external hard drive]] upon plugging it in, it often indicates that the disk is not properly assigned or formatted [00:00:06]. This guide outlines the steps to make your computer detect the external hard drive by managing its partitions.

## Accessing Disk Management

To begin, ensure your external hard drive or USB is plugged into your computer [00:00:44].

1.  Open "This PC" (or "My Computer") by clicking on the folder symbol [00:01:02].
2.  In the "This PC" window, you will likely observe that no external hard drive is detected [00:01:08].
3.  Right-click on "This PC" [00:01:22].
4.  From the context menu, select "Manage" [00:01:26]. This will open the Computer Management window [00:01:29].
5.  In the Computer Management window, navigate to "Storage" and then click on "Disk Management" [00:01:33].

## Identifying and Assigning the Disk

In Disk Management, you should find a disk, often labeled "Disk 1," that is unassigned [00:01:37]. This typically represents the external hard drive that is not being detected [00:01:41].

### Creating a New Simple Volume

To make the external hard drive usable, you need to create a new simple volume and [[formatting_an_external_hard_drive_for_detection | format]] it:

1.  Right-click on the unassigned space of the external hard drive within Disk Management [00:02:02].
2.  Select "New Simple Volume" [00:02:04]. This will launch the "New Simple Volume Wizard" [00:02:07].
3.  Click "Next" to proceed [00:02:12].
4.  The wizard will present the size of the simple volume. You can accept the default size [00:02:14]. Click "Next" again [00:02:17].
5.  The next step is to [[assigning_a_drive_letter_to_an_external_hard_drive | assign a drive letter]] to the hard disk [00:02:21]. Choose any available letter (e.g., 'S' was suggested in the tutorial) [00:02:23]. Click "Next" [00:02:29].

### Formatting the Volume

Formatting is crucial for the computer to detect the hard drive [00:02:35]. Formatting means that all memory occupied by existing files and documents will be erased [00:02:45].

> [!CAUTION] Data Loss Warning
> Formatting a drive will erase all data on it [00:02:47]. If you need to [[recovering_files_from_formatted_drives | recover files from a formatted drive]], there are tutorials available that claim to help recover lost memory and files [00:02:54].

1.  In the formatting options, ensure that "Format this volume with the following settings" is selected [00:03:07].
2.  Leave the file system as "NTFS" (default) [00:03:09].
3.  In the "Volume label" field, you can name your external hard drive (e.g., "external hard drive") [00:03:12].
4.  Ensure "Perform a quick format" is checked [00:03:19].
5.  Click "Next" [00:03:21].
6.  Finally, click "Finish" to complete the process [00:03:24].

After these steps, the external hard drive will be assigned and should appear in "This PC," making it detectable and usable by your computer [00:03:27]. It will now be properly recognized each time it's plugged in [00:03:49].