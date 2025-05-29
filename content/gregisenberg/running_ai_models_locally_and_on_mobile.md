---
title: Running AI models locally and on mobile
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

This article explores various methods for running Artificial Intelligence (AI) models, with a focus on DeepSeek's new reasoning models, and the implications of data privacy when using cloud-hosted versus local solutions. It also covers practical steps for setting up local AI environments on desktop and mobile devices.

## Understanding DeepSeek R1 and Data Privacy Concerns

Ray Fernando, a 12-year ex-Apple engineer and AI startup builder, discusses the DeepSeek R1 reasoning model, an advanced AI model capable of thought and reasoning, potentially leading to superhuman capabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This specific model from DeepSeek, based out of China, has been made [[open_source_ai_models_and_data_privacy | open source]] for study <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. It is reportedly on par with ChatGPT's 01 reasoning model and has gained popularity due to being free to use on their website, deepseek.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Data Privacy Caveats

When using deepseek.com, your data is sent to a server in China, where different rules, laws, and regulations apply <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. It's crucial to be cautious about putting any sensitive business data or personal information, such as tax returns or medical records, into this system, as it would not belong to a region you control <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

## Alternatives for Running DeepSeek Models

To mitigate data privacy concerns and improve reliability (as the DeepSeek server can often be busy <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>), there are several alternatives:

### 1. Using Web UI with API Providers

Instead of direct usage on deepseek.com, you can use a web user interface (UI) to interact with API providers <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These providers host the models in regions like North America, ensuring your data remains within specific jurisdictions <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

*   **Fireworks AI:** This provider hosts the DeepSeek model and allows access via an API key and model string <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. An example is the coding app Cursor, which uses the Fireworks API for its DeepSeek model <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Fireworks AI is priced at approximately $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Groq:** Groq also hosts a distilled version of the Llama 70B model, which is incredibly fast <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Open Router:** Another API provider that offers access to many models, often with free credits to start <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Perplexity:** This platform also has some of these models built-in and is hosted in the United States <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Running Models Locally on Your Machine

Running AI models locally means your data never leaves your device, offering maximum privacy and enabling offline use <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This is particularly useful for private businesses like lawyers or doctors handling sensitive information <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

#### Setup for Local Desktop Use (Open WebUI & Ollama)

The best interface for running models locally is Open WebUI, which looks similar to ChatGPT <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>, <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.

1.  **Download Docker:** Install the Docker Desktop app for your operating system (e.g., Apple Silicon for M machines) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
2.  **Pull and Run the Container:** Use simple terminal commands from the Open WebUI quick start guide to pull and run the Docker container <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. For NVIDIA GPUs, include `gpus all` in the run command for better efficiency <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
3.  **Access Open WebUI:** Once running, navigate to `localhost:3000` in your web browser <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
4.  **Download Models (Ollama):** Download and install Ollama from ollama.com. Ollama acts as a gateway to various local models <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>, <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.
5.  **Connect Ollama to Open WebUI:** In Open WebUI's admin panel settings (under connections), the Ollama API will be pre-configured <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>. From there, you can search for and pull models (e.g., DeepSeek R1) directly from Ollama to your local machine <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.

### Running Models on Mobile (Apollo App)

You can run local AI models directly on mobile devices using apps like Apollo.

1.  **Download Apollo:** Search for "Apollo private local AI" on your app store <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>.
2.  **Select AI Providers:** In the app's settings, choose "AI providers" <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. Options include Open Router, local models, or custom backends <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>.
3.  **Download Local Models:** Apollo will show available models based on your device's memory. Downloaded models are typically several gigabytes in size <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. For example, a distilled Quen model (1.5B) can be downloaded quickly <a class="yt-timestamp" data-t="00:41:38">[00:41:38]</a>.
4.  **Optimized for Apple Hardware:** Models run on Apple devices are optimized to run efficiently on Apple silicon and MLX infrastructure <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>. This enables powerful on-device reasoning capabilities, even offline <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>.

## Prompting and Model Behavior

### Advanced Prompting Techniques

Advanced "chaining prompts" allow you to fully leverage reasoning models to process large amounts of text and perform complex tasks, such as generating blog posts from transcripts <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. These prompts can be configured to produce specific outputs, like graphs or detailed analyses <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

*   **Improving Prompts:** Tools like OpenAI's playground (platform.openai.com) can help reconfigure simple prompts into more detailed, efficient instructions for language models <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. When crafting prompts, consider desired instructions, expected output types, and what you *don't* want <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

### Model Parameters: Temperature

The "temperature" setting influences a model's output <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>:
*   **Lower Temperature (e.g., 0):** Makes the model less prone to "hallucinations" and more likely to follow instructions precisely, ideal for logical reasoning tasks like code generation <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>, <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Higher Temperature (e.g., 1):** Encourages extreme creativity and "out-of-the-box" thinking, useful for creative writing or non-logical tasks <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Experimenting with different temperatures is encouraged to see variations in output <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>.

## The Future of AI and Applications

The demand for chips (GPUs) to host these large models is increasing, driving a competitive "AI arms race" <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Upcoming models like OpenAI's 03 and Mini models are expected to rival current reasoning models in capability while significantly reducing prices due to increased efficiency <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

Advanced [[operator_ai_capabilities_and_limitations | AI capabilities]], such as GPT-4o's ability to understand audio, tone, cadence, and micro-expressions, open up new possibilities for applications <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>, <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>. This could lead to innovative [[using_ai_for_app_development | apps with AI integration]] in areas like:

*   Emergency assistance (e.g., a watch understanding a fall and displaying emergency medical information) <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.
*   Advanced real-time translation <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>.
*   Negotiation assistance (e.g., AI analyzing breathing rate or micro-expressions to provide strategic advice) <a class="yt-timestamp" data-t="00:45:49">[00:45:49]</a>.

Developers are actively exploring how to build interfaces that effectively leverage the intelligence of these models <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.

## Conclusion

The ability to run powerful reasoning models locally on desktop and mobile devices is a game-changer, offering enhanced privacy and offline functionality <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. While cloud-hosted options like DeepSeek.com are convenient and free, vigilance regarding [[open_source_ai_models_and_data_privacy | data privacy]] is essential <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>. API providers like Fireworks, Groq, and Open Router offer a middle ground, hosting models in specific regions <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>.

For those looking to [[implementing_ai_in_app_development_processes | implement AI]] in their workflows or [[building_and_deploying_apps_with_ai_integration | build new apps]], experimenting with these models is crucial <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>. The journey into AI doesn't have to be complicated; understanding prompting and playing with available tools can lead to significant breakthroughs and new business opportunities <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

---
*   Ray Fernando can be reached at rayfernando.com <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.
*   His YouTube channel is Ray Fernando 1337, where he live streams about new tech and AI models <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a>.