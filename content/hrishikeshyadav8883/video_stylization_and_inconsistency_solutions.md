---
title: Video stylization and inconsistency solutions
videoId: oyd1b5Oif84
---

From: [[hrishikeshyadav8883]] <br/> 

Lum, a new Space Time Diffusion Model launched by Google Research, aims to address significant challenges in [[challenges_and_innovations_in_realistic_video_generation | realistic video generation]], particularly focusing on achieving high resolution, realism, and, most importantly, consistency in generated videos <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a><a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a><a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## The Challenge of Temporal Consistency

Inconsistencies are a common issue in existing [[evaluation_of_text_to_video_models_and_applications | text to video generation]] models like Pika and Runway Gen 2 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a><a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For instance, when generating longer videos with Pika, content that is consistent for the initial 3 seconds can become inconsistent as the duration increases <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a><a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Examples include:
*   **"Iron Man fighting the Hulk"**: While initially consistent, extending the video leads to inconsistencies <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a><a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Anime character prompt**: Random elements can appear within the first 3 seconds, making the video incoherent <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a><a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

This issue arises because many prior models, such as Imagen, Pika, and Zeroscope, generate videos bit by bit or through a cascade of models, which makes maintaining global temporal consistency difficult <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a><a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a><a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a><a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

## Lum's Solution: The [[space_time_unet_model_for_video_generation | Space Time UNet Model]]

Lum addresses inconsistency by introducing a [[space_time_unet_model_for_video_generation | Space Time UNet architecture]] that generates the *entire temporal duration* of a video at once, rather than segment by segment <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a><a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a><a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a><a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This approach involves deploying both perpetual and temporal down- and up-sampling, allowing the model to directly generate full-frame rate videos by processing them in multiple space-time cells <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a><a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a><a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The model analyzes consistency across both spatial (X) and temporal (T) axes simultaneously <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a><a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## Key Features and Applications of Lum

### 1. [[challenges_and_innovations_in_realistic_video_generation | Realistic Video Generation]]
Lum excels in generating realistic videos with high resolution and strong temporal consistency. For example, a sailboat sailing on a sunny day shows consistent reflections, a detail often lacking in other text-to-video models <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a><a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### 2. [[semantic_similarity_in_video_recommendations | Video Stylization]]
Lum offers innovative video stylization, allowing users to apply a specific artistic style from a reference image to a generated video <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a><a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Reference Image to Video**: This is a novel capability, transforming a source video (e.g., someone running) into a different style like wooden boxes or origami <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a><a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Sticker Generation**: It can easily generate stylized stickers from a reference image, maintaining an outline and consistency suitable for marketing or product illustration <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a><a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### 3. [[video_segment_generation_and_processing | Cinemagraphs]]
Lum can add motion to static images, a feature also found in Runway Gen 2. Lum's approach offers comparable results, although Runway Gen 2's motion brush feature might be considered superior for some specific applications <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a><a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a><a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### 4. [[video_segment_generation_and_processing | Video Inpainting]]
The model features robust video inpainting capabilities, allowing for seamless filling of missing or removed parts within a video while maintaining high consistency and realism <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a><a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. An example shows a hand approaching a scene, and leaves are realistically generated to fill the space, appearing too consistent and realistic <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a><a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Technical Aspects and Evaluation

Lum's model leverages pre-trained T2I (text-to-image) weighted fixed layers and newly added temporal layers <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a><a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a><a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. It also incorporates multi-diffusion, particularly for reference images and inpainting tasks <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a><a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.

The model was trained on a dataset of 30 million videos, each with corresponding text captions (prompts) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a><a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. Videos are 80 frames long at 16 frames per second (5 seconds) <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. Evaluation was conducted on a collection of 113 text prompts, comparing Lum to other prominent text-to-video diffusion models like Imagen, Zeroscope, Pika, and Runway Gen 2 <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a><a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a><a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

User study results indicate that Lum (represented by the blue line in evaluation metrics) shows superior quality compared to models like Imagen and Pika, especially in overall quality and image-to-video capabilities due to its effective reference image processing <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a><a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a><a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a><a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. While Lum and Runway Gen 2 are comparable for image-to-video tasks, Lum demonstrates better performance in text-to-video generation <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a><a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a><a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

## Future Outlook

The year 2024 is anticipated to be a pivotal year for [[video_content_quiz_generation | video generation]], with a strong movement towards AI-generated short films and movies <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a><a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Models like Lum represent a significant step in this direction, with continuous daily advancements in new AI models <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.