---
title: Running AI models locally and on mobile devices
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

## Introduction: The Power of Reasoning Models
Reasoning models, such as DeepSeek R1, are advanced AI models capable of complex thought and reasoning, potentially leading to "superhuman capabilities" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. DeepSeek's R1 model, developed in China, is open-source for study and is considered on par with ChatGPT's reasoning model <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. A key advantage is its free availability on its website <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Options for Running AI Models

There are several ways to utilize these powerful AI models, each with its own benefits and considerations:

### 1. Direct Web Interface (DeepSeek.com)
DeepSeek.com allows users to directly interact with their R1 model <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Functionality:** To enable DeepThink (the reasoning model), users must click the "DeepSeek" button until it turns blue <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Web search can also be enabled <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Data Privacy Concern:** The primary drawback of using deepseek.com is that its servers are currently hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This means any data sent to the system falls under Chinese laws and regulations, posing a risk for sensitive business or personal data <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   <p class="callout callout_danger">⚠️  **Caution:** It is strongly advised not to input sensitive data like tax returns or medical records into deepseek.com due to data privacy concerns <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.</p>
*   **Reliability:** The servers can become busy due to high popularity, leading to timeouts or failures <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### 2. Using API Providers (e.g., Fireworks AI, Groq, OpenRouter)
A more secure alternative is to use API providers that host these models in regions with desired data regulations, such as North America <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

*   **Fireworks AI:** [[building_native_ios_apps_with_ai_and_cursor | Cursor]], a coding app, uses the Fireworks AI API for its DeepSeek model, ensuring data is not sent to China <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Fireworks AI hosts the DeepSeek model and allows API key access <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Pricing is approximately $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Groq:** Groq also hosts models, including a "distilled Llama 70B" version of DeepSeek, which is incredibly fast <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **OpenRouter:** This is another API provider offering access to various models <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Web UI for API Management:** Open Web UI is a local interface that can connect to these API providers, allowing users to select models and send prompts without direct data transfer to the model's origin <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### 3. Running Models Locally on Your Machine
Running models locally offers maximum control over data and offline functionality <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

#### Desktop Setup (Mac/PC)
1.  **Download Docker:** Install the Docker Desktop app for your operating system (e.g., Apple silicon for M-series Macs) <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
2.  **Install Open Web UI:** This serves as the best local interface for models <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.
    *   Pull the container: `docker pull ghcr.io/open-webui/open-webui:main` <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.
    *   Run the container:
        *   For NVIDIA GPUs: `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --gpus all --restart always ghcr.io/open-webui/open-webui:main` <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>, <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
        *   For single-user mode (no sign-in): `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --restart always ghcr.io/open-webui/open-webui:main` <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   Access the UI: Navigate to `localhost:3000` in your browser <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
3.  **Download Ollama:** This tool enables running any local model <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
    *   Install Ollama from `ollama.com` <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.
    *   Once installed and running, Ollama will automatically configure its API connection in Open Web UI's admin panel <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.
    *   From Open Web UI, you can then "pull" models like DeepSeek R1 from Ollama <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Benefits:** Data stays on your machine, enabling offline use (e.g., on a plane) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Performance depends on local hardware, with higher RAM (e.g., 128GB) beneficial <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

#### Mobile Device Setup (iOS)
*   **Apollo App:** The Apollo app (a paid application) allows users to download and run AI models directly on their mobile devices <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>.
    *   Models can be downloaded from within the app, similar to Ollama <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>.
    *   The app checks device memory to determine compatible models <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. Model sizes can be several gigabytes <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.
    *   Apollo also supports connecting to API providers like OpenRouter for cloud-based model access <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Advantages:** Enables AI reasoning capabilities on the go, without internet connection, optimized for Apple hardware (MLX infrastructure) <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>, <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.
*   **Use Cases:** Local models can be used for scenarios where data privacy is paramount, or for quick tasks that don't require the full reasoning depth of larger models <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>. Future applications could include context-aware emergency assistance via smartwatches, analyzing tone and cadence in negotiations, or advanced translation <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>, <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>.

## Understanding AI Models: Parameters and Performance
*   **Model Parameters:** Models with larger parameter counts (e.g., 600 billion+) generally possess more intelligence and take longer to "think," but yield high-quality results <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Distilled Models:** These are smaller, optimized versions of larger models, designed for faster execution with comparable efficiency, though they might not "think as long" or provide the same depth of results as full models <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. An example is the distilled Llama 70B <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Quantization:** This refers to compressing the model's parameters (e.g., Q4 for 4-bit quantization) <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>. Higher quantization levels (e.g., 32-bit, 16-bit) require more memory but generally lead to higher intelligence and more desirable outputs <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>.

## Optimizing Prompts and Outputs
Reasoning models, including OpenAI's 01 Pro and DeepSeek, excel at paying close attention to detailed instructions in prompts <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

*   **Advanced Chaining Prompts:** These prompts allow models to "think through all of that text and do some work on our behalf," acting like an "admin" <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   An example involves generating a blog post from a video transcript, including analysis, geopolitical implications, and future predictions, which can be remarkably human-level in quality <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>, <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **OpenAI's Playground:** platform.openai.com offers a "playground" where users can describe a desired prompt, and it will reconfigure it for optimal efficiency with language models, helping create "long chains of thought or reason or outputs" <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   **Prompt Design Tips:**
    *   Clearly state desired instructions.
    *   Define expected output format.
    *   Specify what you *don't* want in the output <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Temperature Setting:** This control influences the model's output creativity <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
    *   Lower temperature (e.g., 0.8 default to lower) reduces "hallucinations" and makes the model follow instructions more precisely, ideal for logical reasoning like coding <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.
    *   Higher temperature (e.g., 1.0) encourages extreme creativity, useful for creative writing or non-logical tasks <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. It can be thought of as "wine mode" (creative) versus "coffee mode" (rational execution) <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

## The Future of AI Models
The demand for AI chips and hosting services is rapidly increasing as models become more advanced and widely used <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This competitive landscape drives down API costs, making powerful AI more accessible <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. The upcoming OpenAI 03 and Mini models are anticipated to further reduce prices <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. The ability to run advanced reasoning models locally or on mobile devices signifies a significant leap in AI accessibility and application. For those interested in [[building_a_startup_using_ai_tools | building a startup using AI tools]], [[tools_for_building_production_applications_using_ai | building production applications using AI]], or even [[building_ios_apps_with_ai | building iOS apps with AI]] and [[building_apps_with_ai_tools | building apps with AI tools]], exploring these options can provide an "unfair advantage" by increasing efficiency and lowering costs <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

[[aigenerated_assets_for_mobile_app_development | AI-generated assets for mobile app development]] will likely see continued innovation with the advancement of models like those discussed. [[building_and_deploying_ai_agents_for_business_tasks | Building and deploying AI agents for business tasks]] will also benefit from the efficiency and reasoning capabilities of these models, especially with careful [[testing_and_optimizing_ai_models_for_agent_tasks | testing and optimizing AI models for agent tasks]]. The ability to try different models via Ollama and compare their outputs is key for finding the "right tool for the job" <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>, and using a framework like Open Web UI or Apollo can greatly assist in this process. [[using_multiple_ai_models_to_solve_coding_issues | Using multiple AI models to solve coding issues]] could also leverage this localized and accessible intelligence.