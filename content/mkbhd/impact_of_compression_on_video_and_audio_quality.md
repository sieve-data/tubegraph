---
title: Impact of compression on video and audio quality
videoId: JR4KHfqw-oE
---

From: [[mkbhd]] <br/> 

Video and audio quality can be significantly affected by compression, particularly on platforms like YouTube. While high-end camera gear can capture "absolutely incredible" images, the video file uploaded to YouTube often looks "significantly better" on a creator's personal computer than it does on the platform [00:00:10]. Even though YouTube allows viewing in 4K with a "crispy and sharp" appearance, the original file is "miles better" [00:00:28]. This difference often leads creators to question the effort put into "little things" like color adjustments, sharpening, and stabilization, which may not be noticeable to viewers on smaller screens [00:00:39].

A running joke among creators is that YouTube's processing can act as a denoiser, softening noise in high-ISO footage automatically [00:00:58].

## [[youtube_video_compression_process | YouTube Video Compression Process]]

YouTube must [[youtube_video_compression_process | compress video files]] to efficiently process millions of hours of video uploaded monthly [00:01:10]. This compression is essential for converting uploads into various resolutions (e.g., 4K, 1440p, 1080p, 720p, 480p) and allowing dynamic switching between them [00:01:19]. The goal is to "crunch down" video files to the smallest reasonable size [00:01:30]. For instance, a 5-gigabyte original file is compressed to just a few megabytes for playback [00:01:38]. YouTube assumes that a smaller, compressed file will look "pretty much just as good" while significantly speeding up delivery [00:01:56].

## [[experiments_on_youtube_reupload_and_download_effects | Experiments on YouTube Reupload and Download Effects]]

To investigate the severity of YouTube's compression in 2019, an [[experiments_on_youtube_reupload_and_download_effects | experiment]] was conducted: a video was uploaded, then downloaded, and this process was repeated a thousand times to observe the cumulative degradation of quality [00:02:13]. This method, dubbed "Mr. B style," aimed to see how far the video would "break" [00:02:23].

This [[experiments_on_youtube_reupload_and_download_effects | experiment]] had been performed previously in 2010 by a channel named Ontologist using a webcam video [00:02:47]. However, it was hypothesized that YouTube's processing had evolved due to changes in scale, different codecs, and support for HD videos [00:02:55].

The original source file for the experiment was an 8K, "super sharp, super clean" talking head video with high-quality audio [00:03:48].

### Initial Downloads (1-5 Uploads/Downloads)

After the first download, the video was converted to a 720p version through YouTube's native downloader [00:04:20]. While there was a noticeable loss of sharpness, the video still "generally basically resembles the original file" [00:04:43].

By five downloads, the video began to look softer, and the effects of compression algorithms became apparent [00:05:04]. Video compression algorithms work by dividing the video into blocks of pixels and tracking changes frame by frame [00:05:16]. If a block of pixels remains the same across multiple frames, the algorithm "doesn't have to change much," saving space [00:05:30]. This process, known as block motion estimation, leads to moving parts of the video (like the speaker) breaking down more significantly than static parts (like the background) [00:05:51].

### Progressive Degradation (Beyond 5 Downloads)

Beyond five downloads, the compression became more dramatic [00:06:16]. The speaker's face and skin details became "super soft," while the static background, which wasn't moving frame to frame, retained its clarity [00:06:20].

The audio also began to shift, cutting back by about two frames with every download and upload [00:06:41]. While initially unnoticeable, this shift accumulated over multiple iterations [00:06:54].

By 20 downloads and uploads, visible blocks and larger chunks of pixels started to appear, a result of the compression algorithm holding them together [00:07:13]. This was likened to repeatedly rounding a precise number, eventually simplifying it significantly [00:07:27]. However, when the speaker paused and stopped moving, the video would briefly "sharpen up again" as consecutive frames allowed the pixels to duplicate without much change [00:07:44].

Further downloads led to "brutal blockiness," where larger sections of pixels were grouped due to similar colors [00:08:26]. The speaker's skin tone began shifting, notably from brown to magenta [00:08:39]. Pauses in movement became even more dramatic, causing the entire frame to briefly "reset" and improve in clarity before moving again [00:08:44].

By 500 downloads, the video resembled "a struggling graphics card" or a game with RTX (ray tracing) turned off [00:09:12]. The audio experienced a significant delay of four seconds and started to show signs of compression, sounding "a little muffled" [00:09:19]. Waving arms left "disappearing faint magenta trails" on the shirt and wall [00:09:34].

At 800 downloads, the speaker's facial features were almost entirely gone, looking like a "faceless cartoon avatar" [00:10:00]. The magenta trails became more pronounced, closer to pink [00:10:10]. The audio had shifted so much that the entire last sentence of the video was cut off [00:10:18]. Pauses in movement continued to be dramatic, causing the video to momentarily snap back to a clearer image before descending back into a "caricature" [00:10:31]. Colors were increasingly simplified into larger blocks [00:10:44]. Remarkably, the static background remained "still fine" [00:10:50].

### The Grand Finale (1000 Uploads/Downloads)

At 1000 uploads, the video reached "personal hell" [00:11:13]. Facial features, structure, contrast, and detail were "gone," turning the image into "pink blocks" [00:11:17]. Despite this, the background remained "pristine," very similar to the original upload [00:11:27]. The video appeared like graphics turned "as low as they could possibly get," resembling "Minecraft quality" [00:12:08]. The audio was "completely gone," having slid "completely out the other side" [00:12:18]. The speaker's voice was last audible around the 800th video [00:12:30]. Despite the extreme degradation, the video still triggered the "HD badge" as it was technically a 720p file [00:12:45].

## Conclusions

The experiment provided valuable insights into the [[comparison_of_original_video_quality_vs_compressed_quality | impact of compression on video and audio quality]]:
*   **YouTube's Processing Improvement** The platform's processing and compression in 2019 showed significant improvement compared to the 2010 version of the experiment [00:13:42].
*   **Audio Quality Persistence** The audio generally "held up pretty well" aside from the synchronization issue [00:13:57]. The quality remained "pretty decent" and only became "a little muffled" [00:14:01]. In contrast, the audio in the 2010 webcam video experiment became "a puddle" [00:14:06].
*   **Video Quality Degradation** While initial compression is subtle, repeated re-encoding severely degrades video, especially moving elements, leading to blockiness and color shifts. Static elements are preserved much better due to block motion estimation.

Ultimately, while the original file always looks better on a local computer, YouTube's compression is a necessary process to manage millions of hours of content efficiently, and its algorithms have evolved to maintain a surprisingly high degree of quality over many compression cycles [00:01:10].