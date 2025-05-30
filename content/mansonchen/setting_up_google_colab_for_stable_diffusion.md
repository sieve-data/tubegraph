---
title: Setting Up Google Colab for Stable Diffusion
videoId: 7mLIwyn3MaM
---

From: [[mansonchen]] <br/> 

This article outlines how to use Google Colab with [[deforum_stable_diffusion_overview | Deforum Stable Diffusion]] to generate visual hooks for creative content, a method that has shown good success in augmenting creative strategies <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Accessing and Running the Notebook

To begin, the Stable Diffusion notebook is used <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. You can run the cells by simply hitting the play button <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Google Drive Access
The notebook will request Google Drive access to read from and write to your drive <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. After granting access, click play for path setup <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Initial Model Checkpoint Selection
While a custom "deliberate model" checkpoint can be used <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, for the first run, it's crucial to select the `V 1.5 pruned EMA only checkpoint` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a> <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This specific checkpoint is linked on the resource page <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

#### Setting Up the Model Directory
A critical step is to ensure the downloaded model is placed in the correct directory <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. After downloading the `V 1.5 pruned EMA only checkpoint` model <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, you need to create a specific folder path within your Google Drive: `content/drive/my drive/AI/models/` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Then, move your checkpoint file into this `models` folder <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This setup can be a bit tricky initially <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Configuring Settings and Running Prompts

The notebook has many settings, but for the first run, most do not require adjustment <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

*   **Animation Mode**: Use the 3D animation mode <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Max Frames**: The maximum number of frames to generate is 150 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Motion Parameters**: Motion parameters can be kept as is <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A document will be linked to explain how to work with these parameters <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Prompt**: Input your desired prompt. Example prompts are available on the resource page <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Hit run on the prompt cell <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Batch Name**: You can rename the batch, for example, to "Formula One car four" <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Once initiated, the notebook will begin generating the different frames based on your prompt <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Generating the Video

After the frames are generated, which can take approximately three minutes for a 12-second video <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, you can create the video from these frames by hitting the play button <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Customizations and Additional Features

The speaker's specific "Manson's [[deforum_stable_diffusion_overview | Deforum Stable Diffusion]] notebook" includes a few added features <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>:
*   **Real ESRGAN**: An upscaler that creates higher-quality videos <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Interpolation**: An additional feature at the bottom of the notebook <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

The core Deforum section remains the same as the basic Deforum settings <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, with these additions making the process easier <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. A link to this customized notebook is also available on the resource page <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.