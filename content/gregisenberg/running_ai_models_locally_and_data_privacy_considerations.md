---
title: Running AI models locally and data privacy considerations
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

This article discusses the capabilities of new reasoning models like DeepSeek R1, emphasizing the importance of [[privacy_and_data_concerns_with_ai | data privacy]] when interacting with AI, and exploring options for running these models locally or via alternative hosting providers.

## Understanding DeepSeek R1 and Reasoning Models
DeepSeek R1 is a new reasoning model from DeepSeek out of China, noted for its advanced capabilities in thinking and reasoning, potentially leading to superhuman capabilities <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>. It is open source and reportedly on par with OpenAI's GPT-01 reasoning model <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. DeepSeek R1 is also free to use on their website, deepseek.com <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. These models, including OpenAI's 01 Pro and DeepSeek's reasoning models, are designed to spend extra time and pay attention to instructions, leading to highly detailed and human-level outputs <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

## [[privacy_and_data_concerns_with_ai | Data Privacy Considerations]]
A critical [[privacy_and_data_concerns_with_ai | data privacy]] concern arises when using cloud-hosted AI models. If you use deepseek.com directly or their app, your data is sent to and hosted in China <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. This means your data is subject to China's rules and laws, which may differ from your own region <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. It is strongly advised not to input sensitive data, such as tax returns or medical records, into deepseek.com or similar services where data residency is uncertain or outside your control, as it could become publicly accessible <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>, <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## [[comparison_of_ai_model_hosting_options | AI Model Hosting Options]]
To mitigate [[privacy_and_data_concerns_with_ai | data privacy]] risks and ensure reliability, several options are available for hosting or running AI models:

### 1. Direct Use of DeepSeek.com
*   **Pros:** Free to use <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>, offers web search capabilities when enabled <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   **Cons:** Data is hosted in China, raising [[privacy_and_data_concerns_with_ai | data privacy]] issues <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. The server can be busy due to popularity, leading to timeouts <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

### 2. Using API Providers
API providers host AI models in various regions, allowing you to control where your data resides <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Fireworks AI:** Hosts the DeepSeek model (and others) and allows access via API key. Data sent to Fireworks AI is hosted in North America <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Groq:** Provides incredibly fast hosting for distilled models like DeepSeek R1, also in North America <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.
*   **Open Router:** Another API provider offering access to a wide range of models <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>.

**Cost Comparison:** Fireworks AI charges around $8 per million tokens, significantly cheaper than OpenAI's GPT-01 Pro, which costs about $15 input and $60 output per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

### 3. Running Models Locally
Running AI models directly on your machine is the most secure option for [[privacy_and_data_concerns_with_ai | data privacy]], as your data never leaves your device <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

#### Running on Desktop (Mac/PC)
**Tools Needed:**
*   **Open Web UI:** A user-friendly interface similar to ChatGPT for interacting with local models <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Docker:** A containerization platform required to run Open Web UI <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>.
*   **Ollama:** A tool for downloading and running local AI models <a class="yt-timestamp" data-t="25:15:00">[25:15:00]</a>.

**Setup Workflow:**
1.  **Download and Install Docker Desktop:** Get the correct version for your machine (e.g., Apple silicon) <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>.
2.  **Pull and Run Open Web UI Container:** Use specific Docker commands in your terminal to set up the Open Web UI environment <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>. For NVIDIA GPUs, include `--gpus all` in the Docker run command to leverage your GPU for better performance <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.
3.  **Access Open Web UI:** Once running, navigate to `localhost:3000` in your web browser <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.
4.  **Download and Install Ollama:** Visit ollama.com and download the application for your OS <a class="yt-timestamp" data-t="25:15:00">[25:15:00]</a>.
5.  **Download Models via Ollama:** Use Ollama to download desired models (e.g., DeepSeek R1). These models will be stored locally on your machine <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>.
6.  **Connect Ollama Models to Open Web UI:** In the Open Web UI admin panel, configure connections to include Ollama, which will automatically detect available local models <a class="yt-timestamp" data-t="26:08:00">[26:08:00]</a>. You can then select these local models for your chats <a class="yt-timestamp" data-t="27:20:00">[27:20:20]</a>.

**Benefits:** Models run entirely on your computer, allowing for offline use (e.g., on a plane) <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>, <a class="yt-timestamp" data-t="27:47:00">[27:47:00]</a>. Local models may be smaller (distilled) versions, running faster but potentially with less detail than larger cloud-hosted models <a class="yt-timestamp" data-t="07:17:00">[07:17:17]</a>, <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.

#### Running on Mobile Devices
*   **Apollo App:** A paid app available on mobile app stores that allows users to download and run AI models directly on their phones <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>.
*   **Functionality:** Apollo can run models locally (if the device has enough memory for the model's size) or connect to API providers like Open Router <a class="yt-timestamp" data-t="39:09:00">[39:09:00]</a>.
*   **Optimization:** Models running on Apple silicon are highly optimized, allowing powerful AI to run on mobile devices <a class="yt-timestamp" data-t="41:57:00">[41:57:00]</a>.

## [[working_with_ai_models_and_api_documentation | Prompt Engineering and Customization]]
Effective prompting is crucial for leveraging AI models.
*   **Advanced Chaining Prompts:** These prompts take advantage of models' reasoning capabilities to process large texts and perform complex tasks like generating blog posts or analysis <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Prompt Improvement:** Tools like OpenAI's platform playground (platform.openai.com) can help refine prompts by adding details to a simple input to make it more efficient for the language model <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>.
*   **Temperature Setting:** This control influences the model's output. A lower temperature (e.g., 0.8 default down to 0) makes the model less "hallucinatory" and more likely to follow instructions logically, useful for code or precise tasks. A higher temperature (e.g., up to 1) encourages extreme creativity, suitable for creative writing or out-of-the-box thinking <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>.

## [[business_opportunities_using_ai_studio_and_machine_learning_models | Business Implications and Future Outlook]]
The ability to run and customize AI models offers a significant [[business_opportunities_using_ai_studio_and_machine_learning_models | unfair advantage]] for businesses and startups, allowing for efficiency, cost reduction, and superior product creation <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. The quality of output from advanced reasoning models like DeepSeek R1 can be "human level," resembling the work of a senior writer or research engineer <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.

The ongoing "AI arms race" is driving immense demand for GPUs and hosting providers capable of supporting large models <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>. Future models, like OpenAI's upcoming GPT-4o, are expected to bring further breakthroughs, including understanding audio tone and micro-expressions, opening new avenues for [[building_apps_with_ai_tools | application development]] such as advanced negotiation aids or emergency response systems on wearable devices <a class="yt-timestamp" data-t="46:11:00">[46:11:00]</a>, <a class="yt-timestamp" data-t="43:52:00">[43:52:00]</a>.

Choosing the "right tool for the job" is essential in AI, as not all tasks require the most powerful model <a class="yt-timestamp" data-t="42:45:00">[42:45:00]</a>. Experimentation with different models and settings is encouraged to find the best fit for specific use cases <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>. The field is rapidly evolving, making it an exciting time for discovery and [[using_data_sets_to_generate_new_ai_business_ideas | new business ideas]] <a class="yt-timestamp" data-t="50:38:00">[50:38:00]</a>.