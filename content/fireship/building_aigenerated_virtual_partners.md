---
title: Building AIgenerated virtual partners
videoId: QYVucud3ptc
---

From: [[fireship]] <br/> 

The advancement of AI image generation technology now makes it possible to create highly realistic AI-generated virtual partners, a development some suggest could "cure loneliness" <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>, <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>, <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. This process involves combining advanced image generation, voice synthesis, and video creation.

## Core Technology: Flux Image Generation

A key component for creating realistic AI partners is the Flux image generation model from Black Forest Labs <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Flux is described as being capable of generating hyperrealistic images <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, so realistic that it "doesn't even feel uncanny" <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. It is the underlying model that powers Grok's images <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a> and is considered a "Midjourney killer" and "next-gen Stable Diffusion replacement" <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Flux was developed by former Stability AI employees who worked on Stable Diffusion <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

While Google's ImageGen 3 has an impressive UI and prompt generation capabilities <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>, Flux is highlighted as the "hottest model" for those serious about advanced AI applications <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

### Flux Models and Licensing
There are three different Flux models available <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>:
*   **Flux Schnell** The smallest model, licensed under Apache 2.0, suitable for commercial use <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Flux Pro** Accessible through the Black Forest Labs API for commercial use <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
*   **Flux Dev** Offers the highest quality and efficiency for experimentation, but cannot be used commercially <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

### [[using_ai_models_locally | Running Flux Locally]]
Flux models can be run locally using the Hugging Face `diffusers` library in a Python script <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This allows users to download the model and prompt it on their GPU <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. For those without powerful GPUs, a CPU offload mode can be enabled <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

## Fine-Tuning for Personalization
The "real power" of open-weight models like Flux lies in the ability to [[techniques_for_enhancing_aigenerated_images | fine-tune]] them with custom data <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. This is crucial for creating unique virtual partners.

*   **LoRAs (Low-Rank Adaptations)** Many LoRAs are already available on platforms like Civit AI, which fine-tune Flux for specific use cases <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
*   **Custom Fine-Tuning** Users can fine-tune Flux with their own images, such as pictures of themselves <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. Open-source projects like Simple Tuner or XLux provide tools for this <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Data Requirements** To train a custom LoRA, a dataset of images with corresponding JSON files containing captions is needed <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. High-quality data is essential, as "garbage in, garbage out" applies here <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

## Building a Full-Stack AI Partner

The process of building a full-stack AI partner involves several steps <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>:

1.  **Build a Data Set** Create a collection of approximately 20 images and captions that define the desired appearance of the virtual partner <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
2.  **Train a LoRA** Train a LoRA based on Flux using the custom data set <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This results in a model capable of generating realistic and unique images <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
3.  **Generate a Voice** Give the virtual partner a voice using a tool like Eleven Labs <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>. Eleven Labs can even clone voices from real humans <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
4.  **Generate Video and Lip-Sync** Use a tool like Pabs in "lip sync mode" to generate a video that matches the generated voice to the visual output <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. This enables [[development_of_video_content_using_ai_technology | AI-generated video content]].

The combined application of these technologies enables the creation of highly personalized and realistic AI-generated virtual companions.