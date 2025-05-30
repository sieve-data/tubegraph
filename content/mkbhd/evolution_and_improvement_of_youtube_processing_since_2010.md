---
title: Evolution and improvement of YouTube processing since 2010
videoId: JR4KHfqw-oE
---

From: [[mkbhd]] <br/> 

YouTube's video processing involves significant compression to manage the millions of hours of video uploaded monthly and to provide various resolutions for dynamic switching <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This process converts large original video files (e.g., 5 gigabytes) into much smaller versions (e.g., a few megabytes) that are still visually acceptable for streaming <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Despite high-end cameras capturing "legit absolutely incredible" images, the uploaded video file often looks "significantly better" on a creator's computer than on YouTube, even in 4K <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. YouTube's compression can even "clean up" noise, acting like an automatic denoiser <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Experiments on YouTube Reupload and Download Effects

To evaluate the impact of this compression, an experiment was conducted in 2019 involving repeatedly uploading and downloading a video <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The process involved uploading a video, letting it process, downloading it, and then re-uploading the downloaded version, repeating this cycle for 1000 iterations <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

This concept echoed a similar [[experiments_on_youtube_reupload_and_download_effects | experiment]] from 2010 by a channel named "Ontologist," which used a webcam video <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The 2019 experiment aimed to assess how YouTube's processing had evolved, considering changes in scale, codecs, and the introduction of HD video support <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Methodology and Initial State

The original file for the 2019 experiment was an 8K, "super sharp, super clean" talking-head tech video with high-quality audio <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The YouTube native downloader consistently provided a 720p version of the video after the first download <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Progressive Degradation Observations

As the video underwent more upload/download cycles, specific degradations became apparent:

*   **Softening and Blockiness**
    *   After five downloads, the video became noticeably softer, and the effects of compression algorithms became visible <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   Video compression algorithms work by dividing the video into blocks of pixels and tracking changes frame by frame using a process called block motion estimation. This means static areas (like the background) retain more detail than moving subjects (like the person speaking) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   Around 20 downloads, larger "chunks of pixels" became discernible, resembling a "math problem" where precise measurements are repeatedly rounded <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Pauses in movement allowed the video to temporarily sharpen as consecutive frames didn't change significantly <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Color Shifts and Artifacts**
    *   After many cycles, the skin tone of the subject began shifting towards magenta <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   Moving arms started leaving "disappearing faint magenta trails" on clothing and backgrounds <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. These trails became more pronounced and pinker <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   By the final stages, facial features were almost entirely lost, turning into "pink blocks" or a "pink blobbering blob" <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   The overall visual quality resembled a "struggling graphics card" or graphics with "rtx off" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   The thousandth upload featured extremely large blocks, likened to "Minecraft quality," and was almost unintelligible as a human <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Audio Degradation**
    *   Audio quality showed less drastic degradation than video but consistently shifted its timing. With each download/upload cycle, the audio was delayed by about two frames <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
    *   This shifting became noticeable after several downloads, eventually leading to the audio starting four seconds into the video <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a> and later cutting off entire sentences <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
    *   Audio compression led to a slightly muffled sound <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   By the thousandth upload, the audio was completely gone, with the last audible segment occurring around the 800th video <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Conclusion on YouTube Processing Improvements

Despite the dramatic degradation, the experiment's findings highlight significant improvements in [[youtube_video_compression_process | YouTube's compression process]] since 2010 <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

*   **Video Quality**: The overall visual quality held up "much better than the 2010 version" <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Audio Quality**: The audio, aside from the time shifting, maintained a "pretty decent" quality, not turning into a "puddle" as it did in the 2010 webcam video experiment <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

The experiment concluded that YouTube's processing in 2019 demonstrated notable resilience and efficiency compared to a decade prior <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.