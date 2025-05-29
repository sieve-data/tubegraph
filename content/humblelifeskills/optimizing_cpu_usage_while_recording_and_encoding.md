---
title: Optimizing CPU usage while recording and encoding
videoId: 6Vq_htdkC1k
---

From: [[humblelifeskills]] <br/> 

When recording video on an [[optimizing_video_settings_and_performance_for_older_computers | old machine]] with a [[recording_and_encoding_with_software_encoders | software encoder]] rather than a modern GPU, optimizing CPU usage is crucial to prevent slowdowns and enable efficient workflows <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This can be achieved by decoupling the recording and encoding processes.

## Workflow Overview

A strategy to [[improving_video_encoding_speed_on_older_macs | improve video encoding speed]] on older systems involves recording in a faster, less CPU-intensive format like MKV, and then using a separate process for conversion to MP4 in the background <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This allows the primary recording application (e.g., OBS) to run more smoothly without simultaneously handling intensive MP4 encoding <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Components and Configuration

### OBS (Open Broadcaster Software)
*   **Recording Format:** Configure OBS to record in MKV (Matroska container) format <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This format is faster to write on older machines compared to MP4 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Real-time Recording:** OBS allows for recording in real-time with custom scenes and effects, similar to streaming but offline <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Handbrake Watcher and Handbrake CLI
*   **Purpose:** `Handbrake Watcher` is a program that monitors a specified folder for MKV files <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Once an MKV file is detected and no longer being written to, it triggers `Handbrake CLI` (command-line interface) to convert it to MP4 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Handbrake CLI Path:** The `Handbrake Watcher` configuration needs the path to the Handbrake command-line tool (e.g., `applications handbrake CLI`) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Preset Configuration:**
    *   A custom preset, such as "TEC coda X 720p60 json" (for DTube at 60 frames per second), can be used <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   To make this preset accessible via the command line, it should be set as the default preset within Handbrake's GUI <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Smart File Detection:** `Handbrake Watcher` is designed to be smart, waiting for a file to be finished writing before attempting conversion. It checks if a file was modified less than 30 seconds ago before processing it <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Managing CPU Load

*   **Staged Processing:** To avoid overwhelming the CPU, it's recommended to record an MKV file, stop the recording, and then allow `Handbrake Watcher` to convert it in the background <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Attempting to record, encode, and run OBS simultaneously on an older machine can "hammer" the processor, leading to lag <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Quality Settings:** Adjusting settings like `CRF` (Constant Rate Factor) requires experimentation to find the optimal balance between quality and the CPU's capabilities <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Using "ultra fast" settings can help manage CPU load <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Automated Conversion:** The system allows for multiple MKV files to stack up in the watched folder, with `Handbrake Watcher` processing them sequentially in the background <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **File Deletion:** Handbrake properties can be configured to automatically delete the original MKV file after successful conversion <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This optimized workflow significantly speeds up the video production cycle, especially on older hardware, by allowing recording to continue without being bottlenecked by the encoding process <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.