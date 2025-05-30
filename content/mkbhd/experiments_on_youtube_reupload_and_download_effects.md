---
title: Experiments on YouTube reupload and download effects
videoId: JR4KHfqw-oE
---

From: [[mkbhd]] <br/> 

An experiment conducted in 2019 aimed to analyze the [[youtube_video_compression_process | YouTube video compression process]] and [[evolution_and_improvement_of_youtube_processing_since_2010 | YouTube processing evolution]] by repeatedly uploading and downloading the same video <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The goal was to see how video and audio quality deteriorated over many iterations <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Methodology

The experiment involved the following steps, repeated one thousand times <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>:
1.  Upload a video to YouTube <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Allow it to process <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  Download the processed video <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
4.  Upload the downloaded video again <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The base video for the experiment was an 8K, super sharp, super clean "talking head tech video" with a white background and high-quality audio <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Comparison to Previous Experiments

This experiment echoed a similar one conducted in 2010 by a channel named "Ontologist," which used a webcam video <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The 2019 experiment aimed to test if YouTube's processing had improved given changes in scale, codecs, and the introduction of HD video support since 2010 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## YouTube's Compression Process

YouTube needs to compress uploaded files to manage the millions of hours of video uploaded monthly and to process them into various resolutions (4K, 1440p, 1080p, 720p, 480p) for dynamic switching <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This process crunches down large video files, such as a 5-gigabyte original file, to just a few megabytes while maintaining reasonable quality <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The [[youtube_video_compression_process | video compression algorithm]] works by scanning the entire video and dividing it into smaller blocks of pixels <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. If a block of pixels remains consistent across multiple frames, the algorithm knows it doesn't need to change much, thus saving space <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This technique is known as "block motion estimation" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Observations on Quality Degradation

### Initial Download (1st Iteration)

The first download, obtained through YouTube's native video manager, resulted in a 720p version of the video <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. While it had less sharpness, it generally resembled the original file <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Video Quality over Iterations

As the video underwent multiple uploads and downloads, distinct patterns of degradation emerged:

*   **Softening and Loss of Detail**: After five downloads, the video noticeably softened, and the effects of compression algorithms became apparent <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The face and skin details became extremely soft <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Differential Compression**: Parts of the video that remained still, like the background, retained more detail and appeared largely unchanged, while moving elements, such as the speaker, degraded more rapidly <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Blockiness**: By 20 downloads and uploads, visible blocks or larger chunks of pixels emerged, indicating the algorithm's grouping of pixels <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This resembled a "struggling graphics card" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Color Shifts**: The speaker's skin tone began shifting from brown to magenta <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, with waving arms leaving faint, then more prominent, magenta trails <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **"Reset" Effect**: When the subject paused movement for a few frames, the video would momentarily sharpen and appear clearer, as the algorithm duplicated stable pixels <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This effect became even more dramatic at later stages, with the entire frame seeming to reset <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Loss of Features**: Eventually, facial features like eyes, nose, and mouth almost completely disappeared, transforming the speaker into a "faceless cartoon avatar" or a "pink blobbering blob" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Grand Finale (1000th Upload)**: The video became almost unintelligible, appearing as "Minecraft quality" with large blocks <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Despite the extreme degradation, the background still looked remarkably similar to the original upload <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Even at 1000 uploads, the video still triggered the HD badge as it was technically a 720p file <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Audio Quality over Iterations

The audio also experienced degradation, though less drastic than the video:

*   **Audio Shift**: YouTube's processing caused a subtle audio shift, cutting back the audio by about two frames with every download and upload <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This accumulated over time, becoming noticeable <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. By later stages, the audio started several seconds into the video <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, eventually resulting in the entire last sentence being cut off <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Muffled Sound**: Audio compression started to be audible, making the sound slightly muffled <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Complete Loss**: The audio was completely gone by the 1000th upload, with the last audible segment around the 800th video <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Conclusions

The experiment led to several conclusions:

*   **Improved YouTube Processing**: YouTube's processing and compression in 2019 were significantly better than in 2010 <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Audio Resilience**: Audio quality held up reasonably well, aside from the time-shifting issue. It became slightly muffled but didn't degrade as severely as the video <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
*   **Differential Compression Effectiveness**: The compression algorithm's ability to simplify static parts of the video while still allowing for detail in moving parts demonstrates its efficiency <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

While an original file looks better on a computer than on YouTube, the platform's compression is remarkably effective at maintaining watchable quality for millions of hours of content <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.