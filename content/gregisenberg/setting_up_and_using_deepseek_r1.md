---
title: Setting up and using DeepSeek R1
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

DeepSeek R1 is an advanced reasoning model that has gained significant attention due to its capabilities, open-source nature, and free accessibility on its website <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. Developed in China, this model is considered to be on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. Its ability to "think and reason" can lead to superhuman capabilities <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

## Accessing DeepSeek R1

There are several ways to interact with DeepSeek R1, each with its own implications, particularly concerning data privacy.

### Directly via DeepSeek.com

You can access DeepSeek R1 directly on deepseek.com or through its mobile app <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
However, it's important to note that the website and app are currently hosted in China <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. This means any data sent to the system will be subject to China's rules, laws, and regulations <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Users should exercise caution and avoid inputting sensitive data like tax returns or medical records into the system, as it may not remain within the user's region of control <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>, <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>.

### Via API Providers

For greater control over data location and reliability, DeepSeek R1 can be accessed through API providers that host the model in other regions, such as North America <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

Notable providers include:
*   **Fireworks AI** <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>, <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>: Offers the full DeepSeek model, with hosting outside of China <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. Pricing is approximately $8 per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.
*   **Groq** <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>: Known for its incredibly fast distilled models, such as the distilled Llama 70B model <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
*   **OpenRouter** <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>: Another API provider that offers access to various models, including DeepSeek R1 <a class="yt-timestamp" data-t="39:01:00">[39:01:01]</a>.

## Prompting with DeepSeek R1

Prompting with DeepSeek R1, especially with its reasoning models, goes beyond simple queries. These models pay close attention to instructions and can perform complex analyses <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.

### Basic Usage

To use the model on deepseek.com, simply click the "DeepSeek" button until it turns blue, indicating "Deep Think" is enabled <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. You can also enable web search for tasks requiring internet access <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

### Advanced Prompting Techniques

*   **Complex Instructions:** Instead of short prompts, provide detailed instructions to guide the model. This allows it to "think through" large amounts of text and perform work on your behalf <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
*   **Transcript Analysis:** A common use case is to provide a transcript (e.g., from a live stream or interview) and instruct the model to analyze it and generate content like a blog post <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. This leverages the model's ability to understand context, extract key points, and structure information <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Comparison to Other Models:** DeepSeek's reasoning models often produce outputs that are considered "human-level incredible," resembling the work of a senior writer or research engineer <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. This contrasts with models like older ChatGPT versions, which might provide good "thought starters" but require significant human effort for refinement <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
*   **Configurable Outputs:** Instructions can be configured to request specific outputs, such as graphs or particular formatting <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>.
*   **Prompt Improvement:** Utilize tools like platform.openai.com's playground to generate and refine prompts <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>. Describe the desired task, and the tool can reconfigure a one-line prompt into a more detailed, efficient instruction set <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a>. When creating prompts, consider:
    *   Desired instructions <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>
    *   Expected output type <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>
    *   Undesired outputs <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>

## Running DeepSeek R1 Locally

Running models locally offers significant advantages in terms of data privacy and offline access, such as when flying on a plane <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

### Open Web UI

**Open Web UI** is recommended as the best interface for running models locally <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>.
To set it up:
1.  **Download Docker:** Install the Docker Desktop app for your operating system (e.g., Apple Silicon for M machines) <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>.
2.  **Pull the Container:** Use the command from Open Web UI's quick start guide to download the necessary files (several gigabytes) <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>.
3.  **Run the Container:** Execute the `docker run` command. For NVIDIA GPUs on PC, include `gpus=all` to leverage GPU acceleration <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>. The single-user mode (not requiring sign-in) is often preferred for personal use <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.
4.  **Access Web UI:** Once running, navigate to `localhost:3000` in your web browser <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.

### Ollama

**Ollama** is a tool used to download and manage local models <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>.
1.  **Download Ollama:** Install Ollama for your machine <a class="yt-timestamp" data-t="25:19:00">[25:19:00]</a>.
2.  **Connect to Open Web UI:** In Open Web UI, go to the Admin Panel (User -> Admin Panel -> Settings -> Connections) <a class="yt-timestamp" data-t="25:55:00">[25:55:00]</a>. Ollama API should be pre-configured <a class="yt-timestamp" data-t="26:15:00">[26:15:00]</a>.
3.  **Download Models:** Click the "add/change model" option and search for "DeepSeek" or other models. The "pull from ollama.com" option will download the model to your machine <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>.
4.  **Select Local Model:** In a new chat, select the local DeepSeek R1 model (usually indicated by `:latest`) <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>.

Running models locally consumes system resources like RAM <a class="yt-timestamp" data-t="28:08:00">[28:08:00]</a>. Smaller, "distilled" versions of models run faster and are efficient, though they may not provide the same level of detailed thought as larger models <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## Model Configuration and Optimization

*   **Temperature Setting:** This parameter controls the model's creativity:
    *   **Lower Temperature (e.g., 0.8 to lower):** Makes the model less likely to "hallucinate" and more likely to follow instructions precisely, suitable for logical reasoning and code generation <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>.
    *   **Higher Temperature (e.g., 1):** Encourages extreme creativity and out-of-the-box thinking, useful for creative writing or non-logical tasks <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>.
    *   Experimenting with different temperatures for specific tasks is encouraged <a class="yt-timestamp" data-t="30:19:00">[30:19:00]</a>.
*   **Quantization Level:** Refers to the bit-depth of the model (e.g., Q4 for 4-bit quantization) <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. A higher quantization level generally means more memory usage but potentially greater intelligence and desired output quality <a class="yt-timestamp" data-t="36:21:00">[36:21:00]</a>.

## Mobile Access

Models can also be run locally on mobile devices using apps like **Apollo** (a paid app) <a class="yt-timestamp" data-t="37:04:00">[37:04:00]</a>. Apollo allows downloading models directly to the phone, provided the device has sufficient memory <a class="yt-timestamp" data-t="39:16:00">[39:16:00]</a>. These models are often optimized for Apple Hardware or Apple Silicon <a class="yt-timestamp" data-t="42:57:00">[42:57:00]</a>.

## Cost Considerations

Using AI models, especially via API, involves token costs. While DeepSeek on its website is free, API usage has costs. For example, Fireworks AI is significantly cheaper than OpenAI's 01 Pro for input and output tokens <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>. However, these costs can add up quickly when integrating AI into workflows for content generation or research <a class="yt-timestamp" data-t="17:39:00">[17:39:39]</a>. Anticipated future models from OpenAI (like 03 and Mini) are expected to drive prices down further due to increased efficiency <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>.

## Future Implications and Advice

The rapid advancement of AI models, including the "AI arms race" and increased demand for specialized chips, marks just the beginning of a transformative era <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
The speaker notes that there's a strong desire for providers to host large parameter models reliably, ensuring data localization (e.g., North America, Europe) to meet legal and privacy requirements <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

Key takeaways for users:
*   **Pick the Right Tool:** Not every task requires the most powerful model; selecting a model based on the specific use case (e.g., depth of reasoning vs. speed) is crucial <a class="yt-timestamp" data-t="42:45:00">[42:45:00]</a>.
*   **Experimentation:** The current age allows for easy experimentation with various models to understand their strengths and weaknesses <a class="yt-timestamp" data-t="42:49:00">[42:49:00]</a>.
*   **Omni Models:** Future models, like OpenAI's 4o and upcoming 03, are expected to have breakthrough capabilities, including understanding audio, tone, cadence, and even micro-expressions, which could revolutionize applications like negotiation <a class="yt-timestamp" data-t="46:13:00">[46:13:00]</a>.
*   **Don't Be Fearful:** For those new to AI, it's not too late to get started; the field is still rapidly evolving, and everyone is learning <a class="yt-timestamp" data-t="50:32:00">[50:32:00]</a>.
*   **Play, Discover, Share:** Engage with the technology, experiment with prompts, and share findings with the community <a class="yt-timestamp" data-t="50:57:00">[50:57:00]</a>. This engagement can lead to new application ideas, potentially even a multi-million dollar startup <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>.

For further assistance or to discuss startup ideas, Ray Fernando, an ex-Apple engineer who streams AI coding and builds an AI startup <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, can be reached via his website rayfernando.com or YouTube channel Ray Fernando 1337 <a class="yt-timestamp" data-t="49:06:00">[49:06:00]</a>. He regularly explores new technologies and brings on experts to explain AI models <a class="yt-timestamp" data-t="49:26:00">[49:26:00]</a>.