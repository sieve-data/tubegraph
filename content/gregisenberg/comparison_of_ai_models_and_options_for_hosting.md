---
title: Comparison of AI models and options for hosting
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Ray Fernando, an ex-Apple engineer, discusses various AI models and methods for hosting them, focusing on the new reasoning models like DeepSeek R1 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The discussion covers the capabilities of these models, data privacy concerns, and practical ways to run them for business and personal use.

## DeepSeek R1: An Advanced Reasoning Model

DeepSeek R1 is an advanced reasoning model developed in China <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is an open-source model available for study <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> and is considered on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Its popularity stems from being free to use on its website <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Capabilities
Reasoning models, including DeepSeek R1, can "think and reason," potentially leading to "superhuman capabilities" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These models are highly advanced and can process large amounts of text to perform complex tasks, such as generating detailed blog posts from transcripts <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. They excel at following instructions and paying attention to details, leading to human-level outputs that might otherwise require significant human effort from a senior writer or research engineer <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

## Hosting Options and Data Privacy

The choice of hosting significantly impacts data privacy and model performance.

### 1. Direct Use via DeepSeek.com
Using DeepSeek directly through `deepseek.com` or its app means data is hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Users should exercise caution when inputting sensitive information, as their data would be subject to Chinese laws and regulations, not necessarily those of their home country <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The free service can also experience busy servers and reliability issues due to high demand <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### 2. Third-Party API Providers
For more control over data location and potentially better reliability, users can access models via API providers.

*   **Fireworks AI**: This provider hosts the DeepSeek model outside of China, often in regions like North America <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Services like Cursor use Fireworks API <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Groq**: Groq hosts distilled versions of models, such as the Llama 70B, offering incredible speed <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **OpenRouter**: Another API provider that offers access to various models, often with initial free credits <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

#### Advantages of API Providers
*   **Data Control**: Data can reside in regions like North America, adhering to different privacy laws <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Reliability & Speed**: While direct DeepSeek.com can be busy, API providers like Groq offer near-instant responses with distilled models <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Larger models from providers like Fireworks AI take longer but yield very detailed and high-quality results <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Cost**: Fireworks AI is priced around $8 per million tokens, which is significantly cheaper than OpenAI's 01 Pro, which costs $15 for input and $60 for output per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. These token costs can add up quickly for ongoing use or business applications <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

### 3. Local Hosting on Your Machine
[[running_ai_models_locally_with_docker_and_open_web_ui | Running AI models locally]] offers the highest degree of data privacy and control, as data never leaves the user's machine <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   **Open Web UI**: An excellent interface for managing and interacting with local AI models <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.
    *   **Setup**: Requires [[running_ai_models_locally_with_docker_and_open_web_ui | Docker]] (desktop app) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. Users pull the container and run it using terminal commands <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. For NVIDIA GPUs, a specific command (`gpus Dall`) is used to leverage the GPU for efficiency <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The application runs on `localhost:3000` <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
    *   **Model Management**: Open Web UI connects with [[running_ai_models_locally_with_docker_and_open_web_ui | Ollama]] to download and manage local models like DeepSeek R1 <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>. It also allows connecting to API providers like Fireworks and Groq by adding their base URL and API keys <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.
*   **Ollama**: A tool for downloading and running various AI models locally <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. It simplifies the process of getting models like DeepSeek R1 (e.g., `deepseek-r1:latest`) running on a machine <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
*   **Model Parameters**: Locally run models often have fewer parameters (e.g., 7 billion parameter model) compared to large online models, but they can still perform impressive analysis <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>. The "quantization level" (e.g., Q4 for 4 bits) also affects intelligence and memory usage, with higher levels providing more detailed results but requiring more memory <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
*   **Temperature Setting**: A crucial setting in Open Web UI is "temperature" <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. A lower temperature (e.g., 0.8 default to lower) reduces "hallucinations" and makes the model follow instructions more precisely, useful for logical reasoning and code <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. A higher temperature (e.g., 1.0) increases creativity, suitable for creative writing or non-logical tasks <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.

### 4. Local Hosting on Mobile Devices
AI models can also be run locally on mobile devices.

*   **Apollo App**: This paid app allows users to download and run AI models directly on their phone <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. It provides its own interface and allows selection of local models based on device memory <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. Models optimized for Apple Silicon (MLX) can run efficiently on Apple devices <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **Use Cases**: Running models locally on a phone means they function without an internet connection <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. This enables applications like real-time transcription, emergency response assistance (e.g., understanding a situation from audio, accessing emergency medical info), or even sophisticated negotiation assistance by analyzing tone and cadence <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## OpenAI's Platform and Prompt Improvement
OpenAI's platform (`platform.openai.com`) offers a playground environment where users can describe a task and have the platform reconfigure the prompt for language models to be more efficient <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. This feature helps generate "advanced chaining prompts" or "long chains of thought or reason" to maximize model intelligence <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. When creating prompts, it's beneficial to define desired instructions, expected outputs, and undesired outputs <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

## Future of AI Models
The rapid advancement of AI models, particularly reasoning models like DeepSeek R1 and OpenAI's 01 Pro, indicates a "new AI arms race" where out-competing competitors depends on leveraging the right model for specific tasks <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Future models, such as OpenAI's upcoming 03 and Mini models, are expected to be on par with current advanced reasoning models, leading to significant price drops and increased efficiency <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. The ability of models like GPT-4's Omni to understand audio, tone, and even breathing rates opens new possibilities for applications like sophisticated negotiation assistance <a class="yt-timestamp" data-t="00:46:15">[00:46:15]</a>. The industry is also seeing a rush to host these large parameter models, driving demand for GPUs and services <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

Experimentation with different models and hosting options is key to finding the right tool for a given job <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>. Even smaller, locally run models can be incredibly powerful for specific use cases where deep reasoning might not be required <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.