---
title: Generating Visual Hooks for Creatives
videoId: 7mLIwyn3MaM
---

From: [[mansonchen]] <br/> 

[[aigenerated visual hooks|AI-generated visual hooks]] can significantly augment creative strategy for advertising <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Using tools like Deforum Stable Diffusion has shown success in [[visual hooks and modular creative strategy|generating visual hooks]] for creatives <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, providing an additional method to [[visual treatments and hooks in advertising|create ads]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Tools and Setup

The process relies on a Stable Diffusion notebook, specifically a customized "Manson's Deform Stable Diffusion notebook" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Initial Setup
1.  **Google Drive Access**: The notebook requires access to Google Drive for reading and writing files <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
2.  **Model Checkpoint**:
    *   A custom model checkpoint, such as the "deliberate model," can be used <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
    *   For first-time users, the "V 1.5 pruned EMA only checkpoint" is recommended <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
3.  **Model Directory**: The downloaded model file must be placed in a specific directory structure within your Google Drive: `content/drive/my drive/AI/models/` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Setting this up can be a bit tricky initially <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Generating Visual Hooks

The process involves running cells within the Stable Diffusion notebook.

### Key Settings and Parameters
*   **Animation Mode**: Typically, the "3D animation mode" is utilized <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Max Frames**: The number of frames to generate can be set (e.g., 150 frames) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Motion Parameters**: These parameters influence the animation's movement <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Prompts**: Text prompts guide the AI in generating the visuals <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Example prompts are typically provided in associated resources <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Batch Name**: A name can be assigned to the generated batch of frames <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Workflow Steps
1.  **Run Cells**: Execute the notebook cells, starting with path setup and model selection <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
2.  **Define Prompt**: Input the desired text prompt <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
3.  **Start Generation**: Initiate the generation process, which creates individual frames based on the prompt and settings <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
4.  **Create Video from Frames**: Once frames are generated, a video is compiled from them <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Generation Speed
*   Generating a 12-second video, comprising 150 frames, can take approximately three minutes <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Enhancements to the Notebook

The "Manson's Deform Stable Diffusion notebook" includes several enhancements beyond basic Deforum settings <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>:
*   **Real-ESRGAN Upscaler**: This feature helps produce higher-quality video output <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Interpolation**: An interpolation feature is also included <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

These additions are designed to simplify the user's workflow <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.