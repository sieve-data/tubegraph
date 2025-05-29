---
title: Using OBS with older machines
videoId: 6Vq_htdkC1k
---

From: [[humblelifeskills]] <br/> 

Operating [[using_obs_software_for_periscope_producer | OBS]] and simultaneously recording on an older machine can lead to performance slowdowns <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This is primarily because older hardware often relies on software encoders for video processing, as opposed to modern GPUs with dedicated hardware encoding capabilities <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Optimizing Recording Workflow

To mitigate performance issues and streamline the recording process on older systems, a specific workflow can be implemented:

1.  **Record in MKV Format**
    Recording in MKV (Matroska container) format is often faster than directly encoding to MP4 on less powerful machines <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The MKV format is also noted for its higher quality <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

2.  **Automate Conversion with Handbrake Watcher**
    After recording in MKV, an external tool called "Handbrake Watcher" can be used to monitor a designated folder for newly created MKV files <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

    *   **Conversion Process**: Handbrake Watcher automatically converts these MKV files to MP4 format using the Handbrake command-line interface (CLI) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   **Preset Configuration**: To ensure consistent output, a specific preset (e.g., `TEC coda X 720p60 json`, ideal for DTube at 60 frames per second) within the Handbrake GUI should be right-clicked and set as the default. This allows the command-line interface to utilize that preset <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   **Smart Monitoring**: The watcher is designed to intelligently wait for a file to be completely written before initiating the conversion process <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This allows users to record multiple MKV files, which will then stack up for conversion <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   **Background Processing**: This setup allows users to record in MKV, stop recording, and then let the Handbrake Watcher handle the conversion in the background. Users can then return later to find the converted MP4 files ready <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The final output is typically a 720p, 60 frames per second MP4 file, ready for platforms like DTube <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   **Efficiency**: This method significantly speeds up the post-production cycle compared to other software like ScreenFlow, which might require considerable time for encoding <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   **File Management**: There is an option within Handbrake properties to delete the original MKV file after successful conversion <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Performance Considerations

While this workflow is effective, simultaneous recording and software encoding on an older machine can still lead to significant CPU load and lag <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

*   **Recommended Approach**: To optimize performance, it is advisable to record a segment, stop the recording, allow Handbrake to process the file in the background (which may take a few minutes), and then resume recording or other tasks <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Real-time Elements**: Despite hardware limitations, [[building_and_adjusting_scene_assets_in_obs | custom scenes]] and effects can still be added in real-time within [[using_obs_software_for_periscope_producer | OBS]] during recording, similar to a live streaming setup but for offline production <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.