---
title: Comparison of original video quality vs compressed quality
videoId: JR4KHfqw-oE
---

From: [[mkbhd]] <br/> 

When creating videos with high-end gear, the raw images captured by cameras are "legit absolutely incredible" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, the video file uploaded to YouTube appears "significantly better" on the creator's computer than on YouTube itself, even when viewed in 4K <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This difference is due to [[youtube_video_compression_process | YouTube's compression]] and processing <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Why YouTube Compresses Video

[[youtube_video_compression_process | YouTube's processing]] handles millions of hours of video uploaded monthly <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. To do this efficiently and create multiple versions (e.g., 4K, 1440p, 1080p, 720p, 480p) for dynamic switching, YouTube must "crunch down the video files to as small as they reasonably can" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

For instance, an original 5-gigabyte video file is compressed down to "just a few megabytes" by YouTube, which speeds up content delivery significantly <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This compression can even "clean up" noise from high ISO footage, softening it <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## The Repeated Upload/Download Experiment

To assess the severity of YouTube's compression in 2019, an [[experiments_on_youtube_reupload_and_download_effects | experiment]] was conducted: uploading a video, downloading it, and then re-uploading and re-downloading it repeatedly until the quality degraded significantly <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The goal was to continue this process a thousand times <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

This type of [[experiments_on_youtube_reupload_and_download_effects | experiment]] had been done previously in 2010 by a channel called Ontologist using webcam video <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The 2019 test aimed to see how much [[evolution_and_improvement_of_youtube_processing_since_2010 | YouTube's processing]] had evolved since then, especially with changes in scale, codecs, and support for HD videos <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The base video for the 2019 test was an 8K, "super sharp, super clean" talking head tech video with a white background and high-quality audio <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Breakdown of Quality Degradation

#### After 1 Download (File Number 2)
The video was downloaded using YouTube's native downloader, which provided a 720p version <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. While there was less sharpness compared to the original, the file generally "basically resembles the original file" <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

#### After 5 Downloads
At this stage, the video started "getting softer" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The effects of compression algorithms became visible, not just in losing detail but in how they tried to save detail efficiently <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Video Compression Algorithm**: These algorithms scan the video, dividing it into smaller blocks or groups of pixels <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. If a block of pixels remains the same across multiple frames, the algorithm knows it doesn't need to change much, saving space <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This process is called "block motion estimation" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Visual Effects**: Parts of the video that don't move, like the background, tend to "stay fine" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. However, moving parts, like the speaker, begin to "break down a little bit" <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

#### After 10 Downloads
More "dramatic compression" became apparent, with the video appearing "super soft overall" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Details in the speaker's face and skin were very soft <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The stationary background still looked "the same as the beginning" because it wasn't moving, allowing the compression to reuse pixels <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

*   **Audio Shift**: The audio began to shift or cut back by "about two frames with every download and upload" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This wasn't immediately noticeable but accumulated over time <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

#### After 20 Downloads
At 20 downloads and uploads, visible "blocks" or "bigger chunks of pixels" appeared, held together by the compression algorithm <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This was likened to rounding a precise number repeatedly until it becomes a large, rounded figure <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

Interestingly, moments where the speaker paused and stopped moving for a couple of frames would cause the video to "sharpen up again" as pixels were duplicated, then revert to chaos upon movement <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

#### After 50 Downloads
The audio shift continued, with the audio not starting for a full "two seconds, two and a half seconds into the video" <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. "Brutal blockiness" emerged, where larger sections of pixels were grouped due to similar colors <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The speaker's skin tone began shifting from brown to more magenta <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

Pauses in movement became even more dramatic, with the "whole video frame kind of resets" <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. For example, waving a hand could smear magenta over the background, but when still frames returned, the smears would disappear as the video "snaps back" <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

#### After 100 Downloads
The video now looked like a "struggling graphics card" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The audio took four seconds to come in <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, and subtle audio compression was audible, making it sound "a little muffled" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Waving arms left "disappearing faint magenta trails" on the speaker's shirt and the wall <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

#### After 200 Downloads
The video started with an "okay" first frame before descending into "chaos" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. The speaker looked like a "faceless cartoon avatar" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Skin details, eyes, nose, and mouth were "almost completely gone" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Magenta trails became even more pronounced, closer to pink <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

The audio had shifted so much that the entire last sentence of the video was cut off <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Pauses continued to cause dramatic resets, where the speaker would briefly appear human before descending back into a caricature <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. Colors were heavily simplified into larger blocks <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>, though the background remained "still fine" <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

#### After 1000 Downloads (Grand Finale)
The video became "part art, part chaos" and "completely unintelligible," barely resembling a human being <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Blocks were even bigger, akin to turning graphics settings "all the way down" to "Minecraft quality" <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

The audio was "completely gone," having slid out entirely <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. The last audible words were heard around the 800th video <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Despite the extreme degradation, the video technically still triggered the HD badge because it remained a 720p file <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

However, the background remained "pristine" and "very similar to the original upload" <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

## Key Learnings

1.  **YouTube's Processing Improvement**: The experiment increased respect for [[youtube_video_compression_process | YouTube's processing]] and compression <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. The quality retained is "much better than the 2010 version" of a similar [[experiments_on_youtube_reupload_and_download_effects | experiment]] <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
2.  **Audio Resilience (Except for Shift)**: The audio held up "pretty well" in actual quality, only getting "a little muffled" but not turning into a complete "puddle" like in the 2010 webcam video <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. The main issue was the consistent time shifting <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
3.  **Stationary Elements Preserve Quality**: Parts of the video that remained still, like the background, retained surprisingly high quality even after hundreds of compressions, demonstrating the efficiency of block motion estimation <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  **Moving Elements Degrade Faster**: Moving subjects or complex details degrade much faster, showing severe artifacting and loss of features <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
