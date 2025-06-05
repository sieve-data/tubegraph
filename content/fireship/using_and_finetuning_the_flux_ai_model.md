---
title: Using and finetuning the Flux AI model
videoId: QYVucud3ptc
---

From: [[fireship]] <br/> 

Flux, developed by Black Forest Labs, is a new image generation model that has gained significant attention <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It is the underlying model that powers Groq's images <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Flux is lauded for its ability to generate hyperrealistic images with accurate text <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, often being called the "Midjourney killer" and a "next-gen Stable Diffusion replacement" <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Key Capabilities and Concerns
Flux excels at generating highly realistic images that can be difficult to distinguish from real photographs <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. One particular concern highlighted by Google DeepMind's research is the danger of impersonation, which Flux is particularly good at <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## [[comparison_between_flux_and_other_ai_models | Comparison with Other AI Models]]
While new models like Imagine 3 from Google and Groq 2 from Elon Musk also emerged around the same time, Flux stands out <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Imagine 3**: Google's Imagine 3 offers an impressive UI with AI-generated prompts and improved image quality compared to its predecessor, Imagine 2, which had issues with generating "ethnically diverse Nazis" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. However, Imagine 3 is tuned to prevent impersonation or offensive content <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Stable Diffusion**: Flux was created by former employees of Stability AI who worked on Stable Diffusion <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. It sets a new bar for [[open_source_ai_models | open source AI models]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, potentially rivaling Stable Diffusion 3 Large <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Flux Model Versions
There are three distinct Flux models <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>:
*   **Flux Pro**: Accessible through the Black Forest Labs API <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Flux Dev**: Offers the highest quality and efficiency for experimentation, but cannot be used commercially <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Flux Schnell**: The smallest model, licensed under Apache 2.0, making it suitable for commercial use <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## [[using_ai_models_locally | Running Flux Locally]]
Flux can be run [[using_ai_models_locally | locally]] on your machine <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
1.  **Hugging Face Diffusers Library**: One option is to use the Hugging Face Diffusers library in a Python script <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This will automatically download the model and allow you to prompt it on your GPU <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  **CPU Offload**: If you don't have a powerful GPU, enable CPU offload mode <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Execution**: After installing dependencies in a virtual environment, you can run the script to generate images [[using_ai_models_locally | locally]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## [[training_and_finetuning_ai_models | Finetuning Flux Models]]
The power of [[open_source_ai_models | open source]] weights lies in the ability to [[training_and_finetuning_ai_models | finetune]] models with custom data <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Tools for Finetuning
Several [[open_source_ai_models | open source]] projects simplify the [[training_and_finetuning_ai_models | finetuning]] process <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>:
*   **Simple Tuner** <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>
*   **XLux**: For node-based workflows, XLux has a setup for Comfy UI or customizable YAML training scripts <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Data Preparation
To [[training_and_finetuning_ai_models | finetune]] a LoRA (Low Rank Adaptation) based on Flux, you need data <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>:
*   A folder of images with corresponding JSON files <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Each JSON file should contain a caption for its respective image <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   High-quality data is essential, as "garbage in, garbage out" applies <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Training Process
Once data is prepared, you can [[training_and_finetuning_ai_models | finetune]] your hyperparameters and start [[training_and_finetuning_ai_models | training]] your own model with a single command <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Applications
The ability to [[training_and_finetuning_ai_models | finetune]] Flux allows for advanced applications, such as generating custom AI partners <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>:
1.  **Image Data Set**: Build a data set of about 20 images with captions for the desired partner's appearance <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  **Train LoRA**: [[training_and_finetuning_ai_models | Train]] a LoRA based on Flux to generate realistic, unique images of your partner <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
3.  **Voice Generation**: Use tools like 11 Labs to give the partner a voice, which can even be cloned from a real human <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
4.  **Video Generation**: Employ tools like Pabs to generate a video and use lip-sync mode to match the voice to the video <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.