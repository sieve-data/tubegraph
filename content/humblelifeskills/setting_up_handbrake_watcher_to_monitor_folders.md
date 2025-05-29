---
title: Setting up Handbrake Watcher to monitor folders
videoId: 6Vq_htdkC1k
---

From: [[humblelifeskills]] <br/> 

This article details a workflow for automating video file conversion using Handbrake Watcher, particularly useful for [[using_obs_with_older_machines|older machines]] that struggle with real-time encoding. The process involves recording in MKV format with OBS and then automatically converting these files to MP4 using [[automating_file_conversion_with_handbrakecli|HandbrakeCLI]] via Handbrake Watcher <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Why Use Handbrake Watcher?

The primary motivation for this setup is to overcome the limitations of [[using_obs_with_older_machines|older machines]] that rely on software encoders rather than modern GPU hardware for video encoding <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Recording directly to MP4 can be slower on such systems <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. By recording in MKV (Matroska container) first, which is faster for older machines <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, and then automating the conversion to MP4 in the background, the process becomes more efficient <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This also speeds up the overall workflow for [[exporting_and_uploading_videos_with_elgato_turbo_264_hd|uploading videos]] to platforms like DTube <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, reducing the time spent compared to previous methods like [[automating_video_editing_with_screenflow|ScreenFlow]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## How Handbrake Watcher Works

Handbrake Watcher continuously monitors a specified folder for newly written MKV files <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Once an MKV file is detected and confirmed to be completely written (it smartly waits if a file was modified less than 30 seconds ago) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, it automatically triggers [[automating_file_conversion_with_handbrakecli|HandbrakeCLI]] to convert it to an MP4 file using a predefined preset <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This allows users to record multiple MKV files, which will then stack up and be processed in the background <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Setting Up Handbrake Watcher

### Initial Setup and Configuration

1.  **OBS Recording Settings:**
    *   Configure OBS to record in MKV format <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
    *   For [[using_obs_with_older_machines|older machines]], consider "ultra fast" CPU settings and experiment with Constant Rate Factor (CRF) to balance quality and CPU load <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Handbrake Watcher Properties:**
    *   **Input File Type:** Set to look for `.mkv` files <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   **Output File Type:** Set to convert to `.mp4` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   **[[automating_file_conversion_with_handbrakecli|HandbrakeCLI]] Path:** Specify the path to your Handbrake command-line interface executable (e.g., `applications/handbrakeCLI`) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   **Preset Options:** This is crucial for consistent output.
        *   Within the Handbrake GUI, right-click on your desired preset (e.g., "TEC Coder X 720p60 json," which encodes for DTube at 60 frames per second) <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
        *   Make this preset the default <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This makes the preset accessible to [[automating_file_conversion_with_handbrakecli|HandbrakeCLI]] via the preset list <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
            *   *Note:* Importing JSON files directly into [[automating_file_conversion_with_handbrakecli|HandbrakeCLI]] was found to be problematic; setting it as the default in the GUI is the workaround <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Workflow Example

1.  **Start Recording:** Begin an OBS recording, which saves an MKV file to the designated watch folder <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
2.  **Stop Recording:** Once the recording is complete, the Handbrake Watcher will detect the newly finished MKV file <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
3.  **Automatic Conversion:** Handbrake Watcher initiates the conversion of the MKV to an MP4 file in the background <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
4.  **Continue Working:** You can continue recording new MKV files or perform other tasks while the conversion happens, as it runs in the background <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Advanced Options

*   **Delete Original Files:** In the Handbrake properties, you can configure Handbrake Watcher to delete the original MKV file after a successful conversion <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This setup allows for a more fluid and efficient video production workflow, especially when dealing with hardware limitations <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.