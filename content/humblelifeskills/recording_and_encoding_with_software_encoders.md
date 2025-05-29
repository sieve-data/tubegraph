---
title: Recording and encoding with software encoders
videoId: 6Vq_htdkC1k
---

From: [[humblelifeskills]] <br/> 

When working with older computer hardware that lacks a modern GPU for hardware encoding, it's necessary to rely on software encoders for video recording and processing <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This approach can be slower, but a specific workflow can [[improving_video_encoding_speed_on_older_macs | improve video encoding speed on older Macs]] and optimize the overall process.

## Workflow Overview

The described workflow leverages OBS for recording and Handbrake for encoding, automated by a "Handbrake Watcher" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

1.  **Recording with OBS**:
    *   Record directly into MKV (Matroska Container) format, which is faster for recording on older machines than MP4 <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   Utilize "ultra fast" settings and adjust CRF (Constant Rate Factor) to achieve desired quality based on CPU and hardware configuration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

2.  **Automated Encoding with Handbrake Watcher**:
    *   A program called "Handbrake Watcher" monitors a specified folder for newly created MKV files <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
    *   Once an MKV file is detected (and has not been modified for a set period, e.g., 30 seconds to ensure the recording is complete) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, Handbrake Watcher initiates a conversion to MP4 <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   Handbrake's command-line interface (CLI) is used for the conversion <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Handbrake Configuration

To ensure Handbrake Watcher functions correctly, specific settings are needed for Handbrake:

*   **Preset Selection**: A preset for encoding (e.g., a "TEC coda X 720p60 json file" for d.tube at 60 frames per second) should be set as the default within Handbrake's GUI <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This allows the command-line interface to easily access and use that preset for conversion <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Benefits of this Workflow

This method significantly streamlines the video production process:

*   **Background Processing**: Recording in MKV allows the user to quickly finish recording sessions. Handbrake can then convert the MKV files to MP4 in the background, freeing up the user to perform other tasks <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Improved Efficiency**: Compared to recording with other software like ScreenFlow, which could take a significant amount of time (e.g., half an hour) to process, this automated conversion speeds up the entire cycle <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Continuous Production**: Users can record multiple MKV files consecutively, and Handbrake Watcher will stack them up for conversion, handling them as resources become available <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Real-time Effects**: OBS allows for custom scenes and the addition of effects in real-time during recording, akin to streaming but for offline content <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## CPU Considerations

[[optimizing_cpu_usage_while_recording_and_encoding | Optimizing CPU usage while recording and encoding]] is crucial, especially on older machines:

> <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a> "my processor is getting hammered because it's doing software encoding and trying to run OBS and trying to record at the same time"

To mitigate high CPU load, it's recommended to:

*   Stop recording after a session <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Allow Handbrake time to complete the conversion in the background before continuing demanding tasks <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## File Management

Handbrake's properties also allow for the option to delete the original MKV file after a successful MP4 conversion, helping manage storage space <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The resulting MP4 files are typically 720p at 60 frames per second, ready for upload <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.