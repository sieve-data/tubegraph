---
title: AI prompting with reasoning models
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

AI prompting with reasoning models, such as DeepSeek R1, allows users to leverage advanced AI capabilities that can even lead to superhuman capabilities <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. These models are designed to "think and reason," enabling them to process complex instructions and generate highly detailed and intelligent outputs <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## DeepSeek R1: An Overview

DeepSeek R1 is a specific reasoning model developed in China and made open source <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is reportedly on par with OpenAI's GPT-4o reasoning model and has gained popularity because it is free to use on their website, deepseek.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Data Privacy and Hosting Options

While deepseek.com offers free access, users should be aware that the service is currently hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This means any data sent to deepseek.com, including sensitive information, falls under China's rules, laws, and regulations <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. It's strongly advised not to input sensitive data like tax returns or medical records into the system directly <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Fortunately, several alternatives exist to protect data privacy while still utilizing these powerful models:

### 1. Third-Party API Providers
Various API providers host AI models, allowing users to send data to regions with different data privacy laws, such as North America <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Fireworks AI:** Cursor, an AI coding app, uses Fireworks AI to host its DeepSeek model, ensuring data is not sent to China <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Fireworks AI offers pricing around $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Groq:** Groq also provides hosting for distilled versions of models like DeepSeek, which are incredibly fast <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Perplexity:** Perplexity, for example, has some reasoning models built-in and is hosted in the United States <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **OpenRouter:** This is another API provider that offers access to various models, often with free credits to start <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

### 2. Local Hosting on Your Machine
Running models locally ensures your data never leaves your device <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Open Web UI:** This is a recommended interface for running models locally <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
    *   **Setup:** Requires downloading Docker and running two simple commands in the terminal (one to pull the container, one to run it) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. For NVIDIA GPUs, a specific command (`gpus Dall`) can be used for efficiency <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The interface is then accessible via `localhost:3000` in a web browser <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
*   **Ollama:** This tool allows downloading and running any local model, appearing as a small llama icon in the system tray when running <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. Models like DeepSeek R1 can be pulled from Ollama into Open Web UI <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Apollo App (Mobile):** This paid app allows downloading and running local models directly on mobile devices, including Apple silicon, useful even without internet access <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. Model downloads can be several gigabytes and depend on available device memory <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

## Prompting Techniques and Workflow

[[Prompting techniques for AIgenerated content]] are crucial for leveraging the full power of reasoning models.

### Transcribing and Analyzing Content
A practical application involves transcribing video content and using an AI model to analyze it <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Example Workflow:**
    1.  Transcribe a live stream video using a custom app <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    2.  Copy the generated transcript <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    3.  Paste the transcript into the AI model's interface (e.g., DeepSeek.com or Open Web UI) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    4.  Add specific instructions for the desired output, such as "generate a blog post off a transcript" <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Advanced Chaining Prompts
These models can take advantage of [[sequential_prompting_with_ai_tools | advanced chaining prompts]] to "think through all of that text and do some work on our behalf" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This is likened to hiring an admin to process information and create content <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Improving Prompts with Playgrounds
Tools like platform.openai.com offer a "playground" where users can describe a desired prompt, and the platform will reconfigure it to be more efficient for the language model <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   **Prompt Design Principles:**
    1.  Clearly state desired instructions <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
    2.  Define the expected output type <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
    3.  Specify what is *not* desired as a starting point <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Information Verification
AI models can be used for information verification by analyzing an article and searching the internet to confirm claims <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This requires enabling web search in the model's interface <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

## Model Parameters and Performance

*   **Parameter Count:** Larger parameter models (e.g., 600 billion+) tend to have more intelligence but take longer to process information <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Distilled Models:** These are smaller, more efficient versions that run faster but may not provide the same level of detailed results as larger models <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For example, a 7-billion parameter model running locally can still perform impressive analysis on transcripts <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>.
*   **Reliability:** Free, popular services like deepseek.com can experience server busyness and timeouts due to high demand <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Using APIs or local hosting can improve reliability <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Quantization:** The quantization level (e.g., Q4 for 4-bit) of a model affects its memory usage and intelligence. Lower quantization means less memory but potentially less desired output <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.

## Prompt Engineering and Temperature Settings

Reasoning models, including OpenAI's GPT-4o Pro and DeepSeek's reasoning models, "spend extra time and actually pay attention to your instructions" <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This attention to detail means every instruction is considered <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

### Temperature Setting
The "temperature" setting in AI models controls the creativity of the output <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>:
*   **Lower Temperature (e.g., 0.8 default to lower):** Makes the model "hallucinate less" and follow instructions more closely, ideal for logical reasoning, especially for tasks like code generation <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.
*   **Higher Temperature (e.g., 1):** Encourages extreme creativity, useful for creative writing or non-logical reasoning where out-of-the-box thinking is desired <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.

> [!NOTE] Wine vs. Coffee Mode
> Renaming the temperature setting to "wine versus coffee mode" could represent its function: "Wine mode" for creative, "YOLO mode" outputs, and "coffee mode" for rational, execution-style results <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>. This highlights an opportunity to improve [[improving_ai_designs_and_interfaces | AI designs and interfaces]] by adding more "humanity and lightness" to AI products <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

## Future Implications and Opportunities

The rapid advancement of reasoning models presents significant opportunities and an "AI arms race" <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

### Business Advantage
Integrating AI models into workflows can provide an "unfair advantage" for businesses by improving efficiency, reducing costs, and enhancing product quality <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. By identifying the right model for specific tasks, businesses can significantly outperform competitors <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. The output from models like DeepSeek R1 can be "human level incredible," akin to work done by a senior writer or research engineer <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### On-Device AI
The ability to run powerful AI models locally on devices like phones and potentially even watches in the future is a "Game Changer" <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Use Cases:**
    *   Transcription on lightweight models <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>.
    *   Emergency response: a watch understanding a situation (e.g., a fall) and providing crucial information (medications, recent events) to paramedics <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>.
    *   Coordination with devices like AirPods <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
    *   Advanced translation or negotiation assistance, understanding tone, cadence, and micro-expressions <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>.

### Multimodal AI
Models like OpenAI's GPT-4o are capable of understanding audio, tone, and other subtle implications, which opens up new possibilities for AI applications, such as analyzing breathing rates in negotiations <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>.

### Accessibility and Experimentation
The field of AI is rapidly evolving, and new models are constantly being developed and made accessible <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>. Users are encouraged to:
*   Experiment with different models to find the right tool for their specific needs <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.
*   Utilize playgrounds to generate and refine prompts <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.
*   Share discoveries with the community <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.
*   Not be fearful of being left behind, as everyone is still exploring the full potential of this technology <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>.