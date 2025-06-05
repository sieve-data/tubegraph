---
title: Creating AIgenerated images using stable diffusion
videoId: ky5ZB-mqZKM
---

From: [[fireship]] <br/> 

The field of [[impact_of_aigenerated_images_on_the_internet_and_media | AI-generated images]] has advanced significantly, making it possible to create highly realistic visuals. One notable example is "Itana," an Instagram model from Barcelona, who is entirely artificial but earns approximately $10,000 per month from her subscription tier <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article outlines how to create your own AI-generated images and influencers using [[opensource_tools_for_generating_realistic_images | open-source tools]].

## Evolution of AI Image Generation

Generative Adversarial Networks (GANs) first appeared about 10 years ago, initially producing only small, indistinct images <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Today, anyone can create high-resolution, realistic images <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Open-Source Tools for Image Generation

While commercial options like Midjourney and [[openai_gpt_40_image_generator | OpenAI's DALL-E]] are popular, they are paid, closed-source products with built-in safety layers <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. A robust [[opensource_ai_image_generators | open-source ecosystem]] exists for generative AI, with the most well-known base model being [[diffusion_algorithm_in_ai_and_image_generation | Stable Diffusion XL]], released in late July 2023 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Checkpoints
Large models like [[diffusion_algorithm_in_ai_and_image_generation | Stable Diffusion XL]] require significant computing power <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This can be mitigated by fine-tuning them through "checkpoints," which are created using specialized training data <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. These checkpoints, some highly optimized for photorealism, are available on websites like CivitAI <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Juggernaut XL, based on [[diffusion_algorithm_in_ai_and_image_generation | Stable Diffusion]], is a common default model for realistic images <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### User Interfaces (UIs)
To work with these models without writing code, several UIs are available:
*   **Stable Diffusion Web UI**: A powerful tool, though potentially overwhelming for beginners due to many options <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Comfy UI**: Features a drag-and-drop editor similar to Blender or Unreal Engine <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Focus (Fucus)**: Recommended for its intuitive UI, similar to Midjourney but free <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Many AI UIs are built on Gradio, another open-source project that uses Svelte for its front end <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Getting Started with Focus

To begin [[using_ai_models_locally | using AI models locally]] with Focus:
1.  Clone the repository <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
2.  Create a Python virtual environment and install the necessary packages <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
3.  Run the Python script, which automatically downloads default models like Juggernaut XL <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. These files are multi-gigabyte in size and may take time to download <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Generating Images

Focus can generate two quality images in about 45 seconds on a modest Nvidia 370 GPU <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Key Features and [[techniques_for_enhancing_aigenerated_images | Techniques for Enhancing AI-Generated Images]]
*   **Advanced Tab**: Provides options for performance, aspect ratio, and the number of images <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **Styles Tab**: Allows mixing and matching different artistic styles, such as retro video game or anime <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Prompt Engineering**: To create realistic images, use highly specific prompts and consider adding "imperfections" like rough skin or no makeup <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Input Image (Image Blending)**:
    *   Save a base image, then create a new prompt <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   Check the "input image" box and drop the base image to blend it with new text prompts <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   Use the "advanced box" under the image to fine-tune blending, for example, using "face swap" to maintain facial continuity across different poses <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Inpaint or Outpaint**: If imperfections occur (e.g., unrealistic hands), use the inpaint or outpaint feature within the image prompt section <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Paint over the problematic parts and describe what needs fixing, and the AI will regenerate those sections <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Beyond Still Images

The capabilities of AI extend beyond still images. While platforms like Pabs offer closed-source text-to-video, [[diffusion_algorithm_in_ai_and_image_generation | Stability AI]] introduced [[diffusion_algorithm_in_ai_and_image_generation | Stable Diffusion Video]] in November 2023 <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.