---
title: Animation and Video Generation
videoId: 7mLIwyn3MaM
---

From: [[mansonchen]] <br/> 

## Using Deforum Stable Diffusion for Creative Visual Hooks

Deforum Stable Diffusion can be utilized to [[ai_generated_visuals_in_video_advertising | generate]] [[ai_assets_and_video_generation | visual hooks]] for [[video_ad_creation_workflow | creatives]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This approach has shown good success in augmenting [[video_ad_creation_workflow | creative strategy]] by providing another method to [[video_ad_creation_workflow | create ads]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The notebook is designed to help users [[automatic_video_ad_creation | create ads]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Setting Up the Stable Diffusion Notebook

To begin, the Stable Diffusion notebook is run by hitting play on its cells <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. It requires Google Drive access to read and write data <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Model Checkpoint Selection

For initial setup, it's recommended to select the `V 1.5 pruned EMA only checkpoint` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. While a custom model like the `deliberate model` might be used by the creator <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, the linked resource page provides the `V 1.5 pruned EMA only checkpoint` <a class="yt="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Initial Settings and Parameters

The notebook offers numerous settings, but for first-time users, many can be left as default <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Key settings include:
*   **3D Animation Mode**: This is used for [[ai_generated_video_content | video generation]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Max Frames**: The maximum number of frames to [[ai_generated_video_content | generate]] can be set, for example, to 150 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Motion Parameters**: These control the animation and a document is available to explain how to work with them <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Prompts and Batch Naming

Users input a prompt to guide the [[ai_generated_video_content | generation]] process <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Example prompts are typically provided in a resource page <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The batch name can also be customized, for instance, `Formula One car four` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Video Generation Process

Once settings and prompts are defined, the notebook starts to [[creating_and_editing_video_assets | generate]] individual frames based on the prompt <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. A 12-second video can be generated in approximately three minutes <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. After frames are generated, a video is created from those frames by hitting the play button <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Model Directory Setup

A crucial step for setup is correctly placing the downloaded model. The `V 1.5 pruned EMA only checkpoint` file needs to be moved into a specific directory structure within Google Drive:
`content/drive/my drive/AI/models/` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This initial setup can be challenging <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Custom Notebook Enhancements

The creator's modified "Manson's Deforum Stable Diffusion notebook" includes additional features to enhance [[ai_assets_and_video_generation | video quality]] and workflow <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>:
*   **Real ESRGAN**: This is an upscaler that helps create a higher-quality video <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Interpolation**: An interpolation feature is also included, though the basic Deforum settings for core [[ai_generated_video_content | generation]] remain the same <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
These additions simplify the [[video_ad_creation_workflow | video ad creation workflow]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.