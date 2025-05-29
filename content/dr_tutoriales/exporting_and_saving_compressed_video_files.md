---
title: Exporting and saving compressed video files
videoId: AFydlHKAkZE
---

From: [[dr_tutoriales]] <br/> 

This article outlines how to export and save compressed video files using VLC Media Player, ensuring the [[maintaining_video_quality_while_compressing | video quality]] is maintained. The process aims to [[reducing_video_file_size_for_easier_transfer | reduce file size]] for easier transfer via platforms like WhatsApp or email, or simply to save storage space on your computer <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Requirements
To follow this [[step_by_step_guide_on_using_a_video_compressor | guide]], you will need VLC Media Player installed on your computer <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. VLC is primarily known for opening and playing video files, but it also has editing capabilities, including video compression <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Preparing the Video for Compression
1.  **Open with VLC**: Open the video file you wish to compress with VLC Media Player <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  **Access Convert/Save Function**: Once VLC is open, navigate to "Media" in the top-left menu <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  **Select "Convert/Save"**: Choose the "Convert/Save" option from the "Media" menu <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
4.  **Add Video File**: In the new window that appears, click "Add" and select the video file you want to compress. For example, a 1.93 GB HD chapter of a series can be used <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Configuring Export Settings in VLC
After adding your video, click the "Convert/Save" button <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This is where you configure the [[vlc_settings_for_compressing_videos | settings]] to compress the video while maintaining its [[maintaining_video_quality_while_compressing | quality]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

1.  **Profile Selection**:
    *   Set the profile to `H.264 + MP3` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  **Access Profile Settings**: Click the "Tools" or "Options" icon next to the profile dropdown <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  **Encapsulation**:
    *   Under "Encapsulation," ensure `MP4/MOV` is selected <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
4.  **Video Codec**:
    *   Go to the "Video Codec" tab <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Set the "Codec" to `H.264` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Leave "Bitrate" and "Quality" unused <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Crucially, set the "Resolution" to "Scale 1" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This ensures the output resolution remains the same as the original, preventing quality loss <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   Filters should not be touched <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
5.  **Audio Codec**:
    *   Go to the "Audio Codec" tab <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   It is recommended to keep the audio settings as "original audio" to avoid losing the audio track during conversion <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
6.  **Save Profile**: Click "Save" to apply these profile settings <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## Exporting the Compressed File
1.  **Choose Destination**: Back in the Convert window, click "Browse" to select the destination folder where the compressed video will be saved <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Name the File**: Give your compressed video a new name, for example, "compressed" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  **Start Conversion**: Click "Start" to begin the compression process <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Monitoring and Verifying the Compressed File
*   **Monitor Progress**: VLC will display a loading bar (the reproduction bar) at the bottom. This bar indicates the progress of the conversion. Once it reaches the end, the video will be completely converted <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Check File Size**: After the conversion is complete <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, locate the new compressed file. [[checking_compressed_file_size | Checking its properties]] will show its reduced size. For instance, a 1.93 GB file can be reduced to 384 MB, representing a reduction of over 50% <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Verify Quality**: Open and play the compressed video to ensure that the audio reproduces correctly and the video quality remains good <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.