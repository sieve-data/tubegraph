---
title: Automating file conversion with HandbrakeCLI
videoId: 6Vq_htdkC1k
---

From: [[humblelifeskills]] <br/> 

Automating video file conversion can significantly speed up the production workflow, especially when using older machines or relying on software encoding rather than dedicated hardware encoders like GPUs <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This process leverages OBS for recording, [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] to monitor a designated folder, and Handbrake's Command Line Interface (CLI) for automated conversion <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Workflow Overview

The core idea is to record videos in MKV (Matroska) format, which is often faster for software encoding on older machines compared to MP4 <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Once the MKV file is saved, [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] automatically detects it and initiates a conversion to MP4 using pre-defined Handbrake CLI settings <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Components

*   **OBS (Open Broadcaster Software):** Used for recording video content in MKV format <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   **[[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]]:** A program that continuously monitors a specified folder for new or modified MKV files <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It intelligently waits until a file has not been modified for a certain period (e.g., 30 seconds) before starting the conversion, ensuring the recording is complete <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Handbrake Command Line Interface (CLI):** The command-line version of Handbrake used by [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] to perform the actual video encoding <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Configuration and Settings

To set up this automated workflow, specific settings within [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] and Handbrake itself are required:

1.  **Handbrake Watcher Settings:**
    *   **Input File Type:** Configured to look for MKV files <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   **Output File Type:** Set to convert to MP4 <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   **Handbrake CLI Path:** Specify the path to the `handbrake CLI` executable (e.g., `applications handbrake CLI`) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   **Preset Options:** Crucially, Handbrake Watcher utilizes a preset defined within Handbrake <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

2.  **Handbrake Preset Setup:**
    *   Within the Handbrake Graphical User Interface (GUI), create or select a desired encoding preset, such as "TEC Coder X 720p60" for DTube at 60 frames per second <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   Right-click on this preset and set it as the *default* preset <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This makes it accessible to the command line interface without needing to import `.json` files <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   Adjust Constant Rate Factor (CRF) settings for optimal quality based on CPU and hardware capabilities <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Benefits of Automation

This automated conversion process offers several advantages:

*   **Faster Recording:** Recording in MKV format is generally quicker on systems using software encoding <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Background Processing:** Once an MKV recording is complete, the conversion to MP4 happens automatically in the background, freeing up the user to continue recording or perform other tasks <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Streamlined Workflow:** It eliminates the need for manual post-processing, such as exporting with [[automating_video_editing_with_screenflow | ScreenFlow]], which can take considerable time (e.g., half an hour) and break momentum <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Continuous Production:** Users can stack up multiple MKV recordings, and [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] will process them sequentially <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Direct Upload Readiness:** Converted MP4 files (e.g., 720p 60fps) are immediately ready for upload to platforms like DTube or YouTube <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Real-time Recording:** Enables recording custom scenes and adding effects in real-time within OBS, mimicking a live streaming setup but for offline content <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Optional File Deletion:** [[setting_up_handbrake_watcher_to_monitor_folders | Handbrake Watcher]] can be configured to automatically delete the original MKV file after successful conversion <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Performance Considerations

While efficient, running OBS for recording and Handbrake for encoding simultaneously, especially on an older machine, can heavily tax the CPU <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The ideal workflow involves recording, then pausing to allow Handbrake to complete its conversion in the background before resuming new tasks <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.