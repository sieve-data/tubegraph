---
title: Evaluation of text to video models and applications
videoId: oyd1b5Oif84
---

From: [[hrishikeshyadav8883]] <br/> 

## Introduction to Lum

[[google_research_lum_text_to_video_generation | Google Research]] has launched Lum, a new spacetime diffusion model for realistic video generation <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Lum's key distinctions are its ability to produce more realistic, higher-resolution videos with significant consistency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This consistency, particularly evident in details like reflections, is not common in many existing prompt-to-video generation models <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Addressing Inconsistency in Video Generation

Previous models often generate videos "bit by bit," which leads to temporal inconsistency when extending video duration <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>, <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This issue has been observed in models like Pika and Runway Gen 2 <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, extending a "fighting" scene in Pika beyond three seconds often introduces inconsistencies <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Similarly, an anime character prompt in Pika might result in random, illogical elements appearing in frames <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

Lum addresses this by using a SpaceTime Unit Model architecture <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This architecture generates the entire temporal duration of the video at once, processing it in multiple spacetime cells, which inherently improves global temporal consistency <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Applications and Unique Features of Lum

Lum introduces several unique applications:

*   **Stylized Generation:** A new feature that takes a reference image and applies its style to generate a video <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This allows for creating highly consistent, stylized videos, such as illustrations or animations of objects like a gold-plated rose pendant <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   **[[video_segment_generation_and_processing | Sticker Generation]]:** This stylized generation can easily create video stickers by referencing a style image, even with simple prompts <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. These can be used for marketing or product showcases <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **[[video_segment_generation_and_processing | Video Stylization]]:** The model can transform a source video (e.g., someone running) into a different artistic style, such as wooden box figures or origami <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Cinemagraphs:** Lum can add motion to static images, converting them into videos, similar to Runway Gen 2's motion brush feature <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **[[video_segment_generation_and_processing | Video Inpainting]]:** Lum demonstrates a stable version of video inpainting, effectively filling in missing parts of a video with realistic and consistent content, even as elements move through the masked area <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. An example shows a hand approaching, and leaves appearing consistently where content was missing <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This can also convert one object in a video into another (e.g., bread to pancake) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

## Technical Aspects and Evaluation

Lum is a [[google_research_lum_text_to_video_generation | text-to-video diffusion model]] designed for synthesizing videos that portray realistic, diverse, and coherent motion <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>, <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. It differs from existing models that often rely on temporal or spatial super-resolution, which makes global temporal consistency difficult to achieve <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Lum directly generates a full frame rate by processing it in multiple spacetime cells <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. The model trains new temporal layers while keeping pre-trained T21 weighted layers fixed <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.

The model was trained on a dataset containing 30 million videos with text captions <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>, <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. These videos were 80 frames long at 16 frames per second (5 seconds total) <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. Lum's performance was evaluated against 113 text prompts, including 18 new prompts and 95 from prior works <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

### Comparison Metrics

Lum was compared to prominent text-to-video diffusion models like Imagen Video and ZeroScope <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>, <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
A user study was conducted to evaluate the models based on metrics such as:

*   **Quality:** Lum received higher quality scores compared to Imagen Video and Pika <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   **Text Alignment:** Lum also showed better text alignment <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Image-to-Video Generation:** For image-to-video generation (reference image W), Lum (represented by the blue line) significantly outperformed other models, including Runway Gen 2 <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>, <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>, <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## Future Outlook

The year 2024 is seen as a pivotal year for video generation, with a focus on making AI-generated content mainstream through short films and movies <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The continuous release of new models suggests rapid advancements in the field <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.