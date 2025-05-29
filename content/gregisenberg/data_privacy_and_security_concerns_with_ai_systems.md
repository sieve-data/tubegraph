---
title: Data privacy and security concerns with AI systems
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

When working with AI models, especially newer reasoning models like DeepSeek R1, it's crucial to understand the implications for data privacy and security. While these models offer powerful capabilities, their use comes with various caveats, particularly concerning where your data is processed and stored <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Direct Use of DeepSeek.com: Data Residency Concerns
DeepSeek R1 is an advanced reasoning model developed in China and made open-source <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. While it's free to use on their website and reportedly on par with models like ChatGPT's reasoning capabilities, there's a significant [[security_concerns_with_using_chinese_ai_tools | security concern with using Chinese AI tools]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

[!WARNING] Data Transference to China
If you access DeepSeek via DeepSeek.com or its mobile app, your data is transmitted to and processed by servers located in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Different countries have their own rules, laws, and regulations regarding data <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Therefore, it's advisable to be extremely cautious about inputting any sensitive information into this system, as it would not fall under the legal jurisdiction of your own region <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
For instance, highly sensitive data like tax returns or medical records should not be input directly into DeepSeek.com, as there's a risk of it being exposed or used in unexpected ways <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Alternatives for Enhanced Data Security

To mitigate data privacy concerns, several alternatives allow users to leverage these powerful AI models without sending sensitive data to regions with different data governance laws. The goal is to ensure data remains within a controlled or preferred jurisdiction <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 1. Using API Providers
Instead of interacting directly with DeepSeek's website, you can use third-party API providers that host these models in preferred geographical regions, such as North America or Europe <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Fireworks AI**: This provider hosts the DeepSeek model and allows access via an API key, ensuring data does not go to China <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. An application like Cursor uses the Fireworks API to run its DeepSeek model <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Grock**: Grock is another API provider that hosts distilled versions of models like Llama 70B, offering incredible speed <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Perplexity**: Perplexity also integrates some of these models but is hosted in the United States <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **OpenRouter**: This API provider also offers access to a wide range of models, including DeepSeek R1, and can be used with mobile apps like Apollo <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

Using a web UI like Open Web UI with these API providers allows users to connect to the models while keeping data within a chosen cloud region (e.g., North America), preventing it from being sent to China <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 2. Running Models Locally on Your Machine
For maximum [[security_concerns_with_using_chinese_ai_tools | data privacy and security]], models can be run entirely on your local machine, ensuring no data leaves your device <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This is particularly useful for private businesses like legal or medical practices, where data confidentiality is paramount <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Open Web UI and Docker**: This combination provides an excellent interface for running models locally.
    1.  **Install Docker**: Download the Docker Desktop app for your operating system (e.g., Apple Silicon for M-series Macs) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
    2.  **Pull and Run Open Web UI Container**: Use Docker commands to pull and run the Open Web UI container. For NVIDIA GPUs on PC, include the `--gpus all` command to leverage your GPU <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. Running in single-user mode avoids a sign-in <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    3.  **Access Locally**: Once running, access the interface via `localhost:3000` <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
*   **Ollama**: Ollama.com is a tool that allows you to download and run various local AI models directly on your machine <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. Once installed, models like DeepSeek R1 can be pulled and used within the Open Web UI <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
    *   Models downloaded via Ollama can be identified by `:latest` in their name when selected in Open Web UI <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.
    *   Running models locally consumes system resources (e.g., RAM), so adequate hardware is beneficial <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.
    *   Even smaller, distilled models (e.g., 7 billion parameters) running locally can perform impressive analytical tasks on large transcripts <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   **Mobile Devices (Apollo App)**: For mobile use, applications like Apollo allow users to download and run models locally on their phone, leveraging optimized hardware like Apple Silicon for efficient processing <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. This means [[personal_experiences_and_insights_on_using_ai_for_building_projects | AI can be used]] even without an internet connection <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>.

## General Considerations for AI Use

*   **Understanding Model Size and Efficiency**: Larger parameter models (e.g., 600 billion+) are more intelligent but take longer to process <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Smaller, "distilled" versions run faster and can be efficient for many tasks, though they may not provide the same depth of reasoning as full models <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Experimentation**: It's highly encouraged to experiment with different models and settings (like temperature) to find what works best for your specific use case <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   **Temperature Setting**: A lower temperature (e.g., closer to 0) makes the model less likely to "hallucinate" and adhere more closely to instructions, useful for logical tasks like coding <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. A higher temperature (e.g., 1) encourages extreme creativity, useful for creative writing or non-logical reasoning <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.
*   **Prompt Engineering**: Utilize tools like OpenAI's playground to refine prompts. Starting with clear instructions, desired output types, and unwanted elements can help generate more effective and chained prompts that leverage the models' reasoning capabilities <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   **Cost Efficiency**: While some models like DeepSeek R1 are free on their native platforms, using API providers like Fireworks AI or Grock involves token-based pricing, which can be significantly cheaper than some premium models like OpenAI's GPT-4 <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. However, for high-volume use, these token costs can quickly add up <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

[!NOTE] The rapidly evolving AI landscape means models are becoming more efficient and prices are expected to drop <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

## Future Implications
The advancements in AI reasoning models, including the ability of some (like GPT-4o) to understand audio tone and Cadence, open up vast [[applications_and_implications_of_ai_in_different_industries | opportunities for AI integration]] in various sectors, from healthcare to negotiation assistance <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>. As models become more powerful and accessible, understanding how to use them securely and effectively will be key to [[leveraging_ai_for_business_efficiency | gaining an unfair advantage]] in competitive landscapes <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
It's important for individuals to not fear being left behind, as the field is still rapidly developing, and experimentation with prompts and available tools is a great starting point <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>.