---
title: Hosting and running AI models locally versus using external providers
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

The advancement of AI models, particularly reasoning models like DeepSeek R1, presents new opportunities and challenges for developers and businesses. These models, capable of human-level reasoning and even superhuman capabilities, are becoming increasingly powerful and accessible <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>, <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. Understanding where and how to run these models is crucial for performance, data privacy, and cost-effectiveness.

## Understanding DeepSeek R1

DeepSeek R1 is an advanced reasoning model developed in China <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. It has gained significant attention because it is open-source, available for study, and is reportedly on par with models like ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>, <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. A major draw is that it is free to use on its website, deepseek.com <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

## Using External AI Model Providers

When [[prompting_techniques_for_effective_use_of_ai_models | prompting]] AI models, several options exist for where the model is actually hosted and processed.

### Direct Use via DeepSeek.com

Users can directly access DeepSeek R1 via deepseek.com <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. This method is free and allows for enabling web search capabilities <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>, <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>.

**Considerations for DeepSeek.com:**
*   **Data Hosting Location:** The service is currently hosted in China <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. This means data sent to the model will be subject to Chinese laws and regulations <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. Users should exercise extreme caution and avoid inputting sensitive data like tax returns or medical records <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.
*   **Server Availability:** Due to its popularity and free access, the deepseek.com server can often be busy, leading to timeouts and requiring retries <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>, <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

### API Providers

To mitigate data privacy concerns and improve reliability, users can access DeepSeek R1 and other models through API providers. These providers host the models in different regions, offering more control over data locality.

**Examples of API Providers:**
*   **Fireworks AI:** Hosts the DeepSeek model and allows access via an API key, often located in regions like North America <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>, <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>, <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. Cursor, a coding app, uses Fireworks AI for its DeepSeek integration <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.
*   **Groq:** Offers very fast inference speeds, particularly for distilled versions of models like Llama 70b <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>, <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **OpenRouter:** Another API provider that offers access to a wide range of models, including DeepSeek R1 <a class="yt-timestamp" data-t="38:56:00">[38:56:00]</a>.

**Benefits of API Providers:**
*   **Data Control:** Data can be kept within desired geographical regions (e.g., North America, Europe) to comply with privacy regulations <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>, <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>.
*   **Reliability & Speed:** Often more reliable and faster than direct website usage, especially for smaller, distilled models <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>, <a class="yt-timestamp" data-t="11:17:00">[11:17:10]</a>.
*   **Full Model Access:** Providers like Fireworks AI can host the full, larger models, offering more detailed and human-level outputs compared to smaller, distilled versions <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>, <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

**Cost of API Usage:**
*   API usage is typically token-based. Fireworks AI charges around $8 per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>. While this seems low, these costs can add up quickly for frequent content generation or research, especially for businesses built around AI tools <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>, <a class="yt-timestamp" data-t="17:49:00">[17:49:00]</a>.

### [[leveraging_competition_among_ai_models_for_better_results | Competition Among Models]]

The AI landscape is highly competitive, leading to constant innovation and price drops. OpenAI's upcoming 03 and Mini models are expected to be on par with current advanced reasoning models, potentially driving down prices further <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>, <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>. The choice of model can provide an "unfair advantage" for businesses <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>, allowing them to out-compete others by being more efficient and effective <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.

## Hosting Models Locally

Running AI models directly on a local machine provides the ultimate control over data and offers offline capabilities.

### Benefits of Local Hosting

*   **Data Privacy:** No data leaves your machine, ensuring complete privacy <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This is crucial for sensitive business data (e.g., legal, medical) <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Offline Access:** Models can be used without an internet connection, even on a plane <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>, <a class="yt-timestamp" data-t="32:26:00">[32:26:00]</a>.

### [[tools_and_platforms_for_ai_app_development | Tools and Platforms for Local Hosting]]

*   **Open Web UI:** This is a user-friendly web interface that closely resembles ChatGPT, allowing users to interact with local models <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>, <a class="yt-timestamp" data-t="22:54:00">[22:54:00]</a>. It can also connect to external API providers <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.
*   **Docker:** A containerization platform essential for easily setting up and running Open Web UI <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>. It bundles the entire application, simplifying deployment <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>.
*   **Ollama:** A tool for downloading and running various AI models locally <a class="yt-timestamp" data-t="25:15:00">[25:15:00]</a>. It acts as a gateway to different open-source models <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>.

**Setup Process for Local Hosting:**
1.  **Install Docker Desktop:** Download and install Docker for your operating system (e.g., Apple Silicon for M-series Macs) <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>, <a class="yt-timestamp" data-t="23:09:00">[23:09:00]</a>.
2.  **Pull Open Web UI Container:** Use a simple Docker command to download the Open Web UI container image <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>.
3.  **Run Open Web UI Container:** Execute another Docker command to start the Open Web UI application. For NVIDIA GPUs, include `--gpus all` to leverage GPU acceleration <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>, <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>. A single-user mode is available that doesn't require sign-in <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.
4.  **Access Open Web UI:** Navigate to `localhost:3000` in your web browser <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.
5.  **Install Ollama:** Download and install Ollama for your machine <a class="yt-timestamp" data-t="25:18:00">[25:18:00]</a>.
6.  **Download Models:** Within Open Web UI's admin panel, connect to the Ollama API and download desired models (e.g., DeepSeek R1) <a class="yt-timestamp" data-t="25:59:00">[25:59:00]</a>, <a class="yt-timestamp" data-t="26:37:00">[26:37:00]</a>. Ollama also allows you to browse popular models <a class="yt-timestamp" data-t="33:43:00">[33:43:00]</a>.

### Local Model Performance and Characteristics

*   **Resource Usage:** Running models locally consumes significant RAM and CPU/GPU resources <a class="yt-timestamp" data-t="28:00:00">[28:00:00]</a>.
*   **Model Size and Intelligence:** Larger models (e.g., 600 billion+ parameters) are more intelligent but take longer to process <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>, <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. Locally run models are often "distilled" or smaller versions (e.g., 7 billion parameters), which run faster but may not produce results as detailed as full models <a class="yt-timestamp" data-t="07:17:00">[07:17:17]</a>, <a class="yt-timestamp" data-t="32:58:00">[32:58:00]</a>.
*   **Quantization:** Models can be quantized to different bit levels (e.g., Q4), which affects memory usage and intelligence. Lower quantization (e.g., 4-bit) means less memory but potentially less desired output quality <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>, <a class="yt-timestamp" data-t="36:30:00">[36:30:00]</a>.
*   **Temperature Control:** A crucial setting that affects model output:
    *   **Lower Temperature (e.g., 0):** Reduces "hallucination" and makes the model follow instructions more precisely, ideal for logical reasoning tasks like code generation <a class="yt-timestamp" data-t="29:48:00">[29:48:00]</a>, <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.
    *   **Higher Temperature (e.g., 1):** Increases creativity and "thinking outside the box," suitable for creative writing or non-logical tasks <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>. This can be likened to a "wine mode" versus a "coffee mode" for output <a class="yt-timestamp" data-t="30:42:00">[30:42:00]</a>.

## Running Models on Mobile Devices

The ability to run AI models on mobile devices, even offline, is becoming a reality.

*   **Apollo App:** An application for mobile devices that allows users to download and run AI models locally on their phones <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>, <a class="yt-timestamp" data-t="38:37:00">[38:37:00]</a>.
*   **Memory Constraints:** Mobile devices have limited memory, restricting the size of models that can be run locally (e.g., 4 GB models are common) <a class="yt-timestamp" data-t="39:16:00">[39:16:00]</a>, <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.
*   **Optimized for Hardware:** Models optimized for specific mobile hardware, like Apple Silicon's MLX infrastructure, perform very efficiently <a class="yt-timestamp" data-t="42:00:00">[42:00:00]</a>, <a class="yt-timestamp" data-t="44:50:00">[44:50:00]</a>.
*   **Use Cases:** Local mobile models enable offline capabilities for critical applications, such as transcribing real-time audio on a watch to understand situations and provide emergency information <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>, <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>.

## [[prompting_techniques_for_effective_use_of_ai_models | Prompting and Building Apps with AI]]

Advanced reasoning models excel at paying attention to detailed instructions in prompts, making them highly effective for complex tasks <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>, <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>.

*   **Prompt Engineering:** OpenAI's platform.openai.com offers a playground where users can describe a task and have the system reconfigure and optimize the prompt for efficiency <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>, <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a>. This helps in [[planning_before_using_ai_tools | planning]] and defining desired outputs <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>.
*   **Content Generation:** Models can generate high-quality content, such as blog posts from video transcripts, with human-level accuracy and detail, often requiring less human intervention than previous models like earlier ChatGPT versions <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>, <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.
*   **[[building_apps_using_ai_tools | Building Apps Using AI Tools]]:** The power of these models opens up vast opportunities for [[building_and_scaling_niche_ai_saas_businesses | building and scaling niche AI SaaS businesses]] <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. The focus is shifting to how people can build interfaces and applications that interact with these powerful models <a class="yt-timestamp" data-t="31:51:00">[31:51:00]</a>. [[deploying_ai_agents_in_production | Deploying AI agents in production]] becomes a key consideration for bringing these capabilities to a wider audience <a class="yt-timestamp" data-t="16:22:00">[16:22:00]</a>.

## Conclusion

The choice between hosting AI models locally or using external providers depends on specific needs for data privacy, cost, performance, and accessibility. While free online services are convenient, they come with data privacy risks. API providers offer a balance of control and performance, and local hosting provides maximum privacy and offline capability, especially with the emergence of efficient mobile AI <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a>. Experimentation with different models and platforms is highly encouraged to find the right tool for the job <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>, <a class="yt-timestamp" data-t="42:45:00">[42:45:00]</a>. The field is rapidly evolving, and embracing this new intelligence can lead to significant advantages and new startup ideas <a class="yt-timestamp" data-t="48:57:00">[48:57:00]</a>.