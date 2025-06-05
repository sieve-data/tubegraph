---
title: Opensource tools for generating realistic images
videoId: ky5ZB-mqZKM
---

From: [[fireship]] <br/> 

[[Opensource AI image generators | Opensource AI image generators]] allow individuals to create highly realistic images, including artificial influencers, for free <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These tools have evolved significantly from early generative adversarial networks (GANs) which, about 10 years ago, could only produce tiny, barely discernible images <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Today, anyone can generate high-resolution, realistic images <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

An example of the capabilities of these tools is Itana, an artificial Instagram model from Barcelona <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. She is entirely artificial and can generate approximately $10,000 per month from subscription tiers <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Why Open Source?

While commercial options like Midjourney and [[OpenAI GPT 40 image generator | OpenAI's DALL-E]] exist, they are paid, closed-source products with "unwanted safety layers" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. A robust [[open source AI models | open source]] ecosystem for generative AI provides powerful alternatives <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Key Open Source Models

The most well-known base model in the open-source ecosystem is [[Diffusion Algorithm in AI and Image Generation | Stable Diffusion XL]], released in late July 2023 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. While such large models require significant computing power, they can be fine-tuned by creating "checkpoints" using specialized training data <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. These checkpoints, often found on websites like Civitai, are optimized for specific outputs, including photo-realism <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Juggernaut XL is an example of a checkpoint based on [[Diffusion Algorithm in AI and Image Generation | Stable Diffusion]] that works well for realistic images <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## User Interfaces (UIs)

To work with these models without writing code, various user interfaces (UIs) are available <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>:

*   **[[creating_aigenerated_images_using_stable_diffusion | Stable Diffusion Web UI]]**: A powerful, well-known option, though it can be overwhelming for beginners due to many buttons <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Comfy UI**: Features a drag-and-drop editor similar to Blender or Unreal Engine <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Focus (Fucus)**: Praised for its intuitive UI, which is similar to Midjourney but free <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

All these AI UIs are based on an [[open source AI models | open source]] project called Gradio, which builds its front end with Svelte <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Getting Started with Focus (Fucus)

To set up Focus:
1.  Clone its repository <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
2.  Create a Python virtual environment <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
3.  Install necessary packages <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
4.  Run a Python script to automatically download default models, such as Juggernaut XL <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. These files are typically multiple gigabytes in size <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Focus can generate two quality images in about 45 seconds on a modest Nvidia 370 GPU <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Its advanced tab offers options for performance, aspect ratio, number of images, and various artistic styles (e.g., retro video game, anime) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## [[Techniques for enhancing AIgenerated images | Image Generation Techniques]]

To generate realistic images, especially for AI influencers:

*   **Specific Prompting**: Create highly specific prompts and include imperfections like "rough skin" or "no makeup" to enhance realism <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Input Image Blending**: Use an "input image" feature to blend multiple images and text <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Features like "face swap" maintain continuity between faces <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Inpaint/Outpaint**: For imperfections in generated images (e.g., hands), use inpaint or outpaint functions to select and regenerate specific parts <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Beyond Images

The advancement of [[Diffusion Algorithm in AI and Image Generation | Stable Diffusion]] extends beyond static images to video generation. Stability AI introduced [[Diffusion Algorithm in AI and Image Generation | Stable Diffusion Video]] in November 2023, allowing for text-to-video capabilities <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.