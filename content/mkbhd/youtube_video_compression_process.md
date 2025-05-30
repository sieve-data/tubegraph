---
title: YouTube video compression process
videoId: JR4KHfqw-oE
---

From: [[mkbhd]] <br/> 

YouTube's video compression process significantly alters the quality of uploaded videos, often leading to a noticeable difference between the original file and the version displayed on the platform <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While a video might look "crispy and sharp" in 4K on YouTube, the original file on a creator's computer looks "miles better" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This [[impact_of_compression_on_video_and_audio_quality | impact of compression on video and audio quality]] can make creators question the effort spent on minor adjustments like color, sharpening, and stabilization, as these subtle details are often lost during playback on various devices <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Why YouTube Compresses Files

YouTube compresses video files primarily to efficiently process and stream the millions of hours of content uploaded monthly <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This process involves converting a single uploaded file into multiple versions (e.g., 4K, 1440p, 1080p, 720p, 480p) to allow dynamic switching based on a viewer's internet connection and device capabilities <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. For example, a 5-gigabyte raw video file is crunched down to just a few megabytes while aiming to maintain similar perceived quality, significantly speeding up playback <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The Compression Algorithm: Block Motion Estimation

Video compression algorithms, such as block motion estimation, scan an entire video and divide it into smaller blocks or groups of pixels <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. They then analyze frames one by one <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. If a block of pixels remains consistent across multiple frames, the algorithm optimizes by keeping that original block, saving space <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This means:
*   **Static elements** like backgrounds tend to retain their quality well, as they don't change much from frame to frame <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Moving elements**, such as a person speaking, will degrade more noticeably <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

This process is akin to rounding a precise number repeatedly, eventually leading to a much broader approximation <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## [[experiments_on_youtube_reupload_and_download_effects | Experiments on YouTube Reupload and Download Effects]]

To test the severity of YouTube's compression in 2019, an experiment was conducted involving repeatedly uploading and downloading a video <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This method, inspired by a 2010 experiment by a channel called "Ontologist" using a webcam video <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, aimed to observe the cumulative degradation. The plan was to upload a video, download it, then re-upload that downloaded version, and repeat the process potentially a thousand times <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Stages of Degradation

The base video for the experiment was an 8K, super sharp, and clean "talking head tech video" with high-quality audio <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

*   **After 1 Download (File #2)**: The video downloaded from YouTube's native downloader was at 720p <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. While less sharp, it generally resembled the original <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **After 5 Downloads**: The video became noticeably softer <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The effects of compression algorithms became apparent, with moving parts degrading more than the static background <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Later Stages (Dramatic Compression)**:
    *   **Visuals**: The image became progressively softer, with details on the face blurring <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Large, discernible blocks of pixels emerged <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Skin tones began shifting, notably from brown to magenta <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Waving arms left disappearing faint magenta trails on the shirt and wall <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. Facial features like eyes, nose, and mouth almost completely disappeared, turning into a "faceless cartoon avatar" or "pink blocks" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The video quality looked like a "struggling graphics card" or "Minecraft quality" <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. However, the static background remained surprisingly clear, even appearing similar to the original upload in the final stages <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Pauses in movement caused the video frame to temporarily sharpen or "reset" before degrading again <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   **Audio**: The audio experienced a consistent shift, cutting back by about two frames with every download and upload <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This led to increasingly delayed audio <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, eventually becoming muffled as if "behind a thin cloth" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. By the 1000th upload, the audio was completely gone <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. The last audible words were heard around the 800th video <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Despite the heavy compression, the video still triggered the HD badge as it was technically a 720p file <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## [[evolution_and_improvement_of_youtube_processing_since_2010 | Evolution and Improvement of YouTube Processing Since 2010]]

Comparing the 2019 experiment to the 2010 "Ontologist" experiment, YouTube's processing, with its changes in scale and codecs, showed significant [[evolution_and_improvement_of_youtube_processing_since_2010 | evolution and improvement of YouTube processing since 2010]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The audio, despite the shifting issue, held up much better in 2019, getting only "a little muffled" compared to the complete audio disintegration observed in the 2010 webcam video <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Conclusion

The experiment highlighted YouTube's sophisticated compression capabilities. While the video quality on the platform still falls short of the original file, it has vastly improved since 2010 <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. The ability to compress large files into small, streamable versions while maintaining a relatively good user experience demonstrates the efficiency of their algorithms <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.