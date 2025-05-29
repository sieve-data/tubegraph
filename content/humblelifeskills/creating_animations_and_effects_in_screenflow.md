---
title: Creating animations and effects in ScreenFlow
videoId: rza5Eg44eak
---

From: [[humblelifeskills]] <br/> 

[[automating_video_editing_with_screenflow | ScreenFlow]] templates can be used to significantly speed up video production, including automating intro animations, crossfades, intro/outro audio, and green-screen effects <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. When recording, users can select a pre-made template in [[using_screenflow_templates_for_video_production | ScreenFlow]] to use as a base, which arranges the recorded elements (screen, camera, mic) in a specific, pre-formatted way <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This pre-formatting greatly enhances productivity in video making <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Template Placeholders and Structure

[[screenflow_template_configuration_and_structure | ScreenFlow]] (version 8.22 was mentioned) allows the insertion of "template placeholder clips" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. These placeholders can include screen recordings, computer audio, camera, microphone, and even iOS devices plugged in via USB <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

A typical template arrangement might include:
*   **Borders** Borders can be created on their own nested layer, consisting of four sub-layers for the left, right, bottom, and top <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The colors of these borders can be customized at any point <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Their duration can be set, for example, to five minutes, to ensure they don't unexpectedly cut out during recording <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. In an example, intro borders stay on screen for two seconds before disappearing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Intro Logo and Text** This can be a group of layers including top text, text underneath, an image, and an annotation (e.g., a black background with adjusted layer opacity) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Text can also have effects like a drop shadow <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Audio Layer** The audio from the camera and microphone placeholder can be extracted to a separate layer, allowing independent manipulation without affecting video cuts <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Background Video** A video file can be set as a background layer, playing continuously <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Applying Effects and Actions

[[automating_video_editing_with_screenflow | ScreenFlow]]'s "actions" feature is particularly powerful for automating effects <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Audio Filters
Audio filters can be applied to a layer even before recording <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. For example, a style preset like "Apple effects batch" can apply an Apple codec with pre-configured compression, master gain, release time, and limiter settings to the audio layer <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This pre-processing helps to achieve a consistent audio sound directly after recording <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Visual Animations and Movements
To create animations, select a layer and click the "action" button <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This adds an action layer on top, allowing users to define time-sensitive actions within that layer <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. These actions can include:
*   Moving elements <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
*   Enlarging <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
*   Rotating <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   Cropping <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>

For instance, a camera/microphone placeholder might move from left to right during an intro to avoid overlapping with text, then move back to the middle with a slow animation <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

### Style Presets
Once a series of effects or actions are defined for a layer, they can be saved as "style presets" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This allows for quick application of complex effects, such as moving a webcam to the bottom-left corner and scaling it down <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. When applied, the action transitions the element from its original state to the defined preset's state over the duration of the action <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

By leveraging these powerful templating features, users can significantly streamline their video production process <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.