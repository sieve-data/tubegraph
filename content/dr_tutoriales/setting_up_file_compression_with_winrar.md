---
title: Setting up file compression with WinRAR
videoId: TB8o2n-8poQ
---

From: [[dr_tutoriales]] <br/> 

WinRAR is a program designed to facilitate file compression and decompression, allowing users to reduce file sizes for easier transport and sharing, particularly via email [00:00:36]. For instance, Gmail has a file attachment limit of 25 megabytes [00:00:13], making compression necessary for larger files [00:00:18].

## [[downloading_and_installing_winrar | Downloading and Installing WinRAR]]

Before compressing files, WinRAR must be installed on your computer [00:01:15]. If you do not have it:
1.  Access your preferred search engine, such as Google Chrome [00:00:48].
2.  Search for "WinRAR" [00:00:56].
3.  The first search result typically allows you to download the program [00:01:01].

## [[how_to_compress_files_with_winrar | Compressing Files with WinRAR]]

Once WinRAR is installed, you can proceed with compressing your desired file [00:01:17].

### Checking Original File Size
It's useful to know the original size of the file you intend to compress. For example, a video file named "test one" was found to be 55.6 megabytes [00:01:28]. This size would prevent it from being directly transferred via Gmail [00:01:35].
To check a file's size:
1.  Right-click on the file [00:01:26].
2.  Select "Properties" [00:01:28].

### Compression Steps
To compress a file using WinRAR:
1.  Right-click on the file you wish to compress [00:01:57].
2.  From the context menu, select "Add to archive..." (represented by a book icon) [00:02:02].
3.  A configuration window will appear where you can adjust settings:
    *   **Archive name**: Choose a name for your compressed file. The `.rar` extension indicates it is compressed [00:02:07].
    *   **Compression method**: Select "Best" for the highest compression [00:02:13].
    *   **Dictionary size**: Set this to the lowest possible value [00:02:16].
    *   **Split to volumes, bytes**: Input "0" [00:02:18].
    *   **Compression options**: Check "Create solid archive" [00:02:21].
    *   **Set password**: Optionally, you can set a password for the compressed file [00:02:24].
4.  Click "OK" to begin the compression process [00:02:51]. The process takes a few seconds, depending on the file size [00:02:56].

### Checking Compressed File Size
After compression, you can re-check the file's properties to see the reduction in size [00:03:04]. For the example video, the size was reduced from 55.6 megabytes to 43.9 megabytes, representing approximately a 20% compression [00:03:09].

> [!NOTE] Other methods for video compression exist, such as using VLC media player, which can also be effective [00:01:46]. For a more general guide, refer to [[step_by_step_video_compression_tutorial | step by step video compression tutorial]].