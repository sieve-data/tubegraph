---
title: Prompting with reasoning models
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Prompting with new reasoning models, specifically DeepSeek R1, is a significant advancement in AI capabilities, enabling models to "think and reason" which can lead to superhuman capabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These advanced models are transforming how users interact with AI, allowing for more sophisticated outputs and applications <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## DeepSeek R1: An Overview
DeepSeek R1, developed in China, is an open-source reasoning model available for study <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is reportedly on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Its popularity has surged because it's free to use on their website, DeepSeek.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Data Privacy Considerations
When using DeepSeek.com, it's crucial to understand that your data is hosted in China, subject to their rules and regulations <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
> [!caution] Data Sensitivity
> Be very careful about putting any sensitive data, such as tax returns or medical records, into DeepSeek.com, as it will not belong to a region you may control <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a> <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a> <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

## Hosting and Running Reasoning Models

Several alternatives exist for interacting with reasoning models while maintaining data privacy and control:

### 1. Using API Providers
API providers like Fireworks AI and Groq host these models in regions outside China (e.g., North America), allowing users to send data to a controlled cloud environment <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a> <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This method typically uses a web UI like Open Web UI to connect to these providers <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

**Setup with Open Web UI and API Providers:**
*   **Open Web UI**: A chat interface similar to ChatGPT, typically run in a Docker container <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Connecting to Providers**: In Open Web UI, navigate to Admin Panel > Settings > Connections and add a new connection for the API provider (e.g., Fireworks AI or Groq) using their base URL and an API key <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a> <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.
*   **Model Selection**: Once configured, models from these providers (like DeepSeek R1) become selectable within Open Web UI <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### 2. Running Models Locally on Your Machine
For maximum privacy and offline capability, models can be run directly on your computer <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

**Setup for Local Execution:**
*   **Docker**: Download and install Docker Desktop for your operating system (e.g., Apple Silicon for M-series Macs) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Open Web UI Container**: Use Docker commands to pull and run the Open Web UI container, with an option to utilize your GPU for efficiency on NVIDIA systems <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. Running in single-user mode avoids sign-in <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
*   **Ollama**: Download and install Ollama, which allows you to download and run various local models <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. DeepSeek R1 models can be pulled directly through Ollama <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Access**: Once running, access the Open Web UI via `localhost:3000` <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. Locally run models are identifiable by "colon latest" in their name (e.g., `deepseek-r1:latest`) <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.

### 3. Running Models on Mobile Devices
Apps like Apollo allow downloading and running models directly on mobile devices, offering offline AI capabilities <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. Apollo indicates memory requirements for models and can connect to API providers like OpenRouter for additional models <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>.

## Effective Prompting Techniques
Prompting with reasoning models involves crafting instructions to leverage their advanced thinking capabilities.

### Basic Prompting
Users can paste large texts, like video transcripts, and provide additional instructions to the model <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. For example, a prompt can be used to analyze a transcript and generate a blog post <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### [[sequential_prompting_with_ai_tools | Advanced Chaining Prompts]]
These prompts take full advantage of reasoning models by guiding them through complex tasks <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This is akin to hiring an assistant to process information and create content <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Large parameter models (e.g., 600 billion+) can "think" longer and yield highly detailed, human-level results, like blog posts with analysis, geopolitical implications, future predictions, and key takeaways from a transcript <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a> <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### Distilled vs. Large Models
*   **Large Models**: Have more parameters (e.g., 600B+), tend to take longer to process, but provide more intelligent and detailed results <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Distilled Models**: Smaller, faster versions that capture the "essence" of larger models. They run more efficiently but may not offer the same depth of reasoning or detail <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Utilizing Web Search
Some models, particularly directly through DeepSeek.com or its app, offer web search capabilities for tasks like information verification, allowing the AI to search the internet to validate claims within an article <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

### Improving Prompts with OpenAI Playground
The OpenAI platform provides a "playground" where users can input a one-line prompt and use a "generate" feature to reconfigure it into a more detailed, efficient prompt for the language model <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This helps in building longer "chains of thought or reason" <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.

### Prompt Generation Tips
*   Clearly define desired instructions <a class="yt-timestamp" data-t="00:39:32">[00:19:32]</a>.
*   Specify the expected output format <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
*   Indicate what you *don't* want in the output <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Temperature Setting
The "temperature" setting in models controls their creativity and adherence to instructions <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>:
*   **Lower Temperature (e.g., 0)**: Reduces "hallucinations," makes the model follow instructions better, and is useful for logical reasoning tasks like code <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>. This can be thought of as "coffee mode" <a class="yt-timestamp" data-t="00:30:54">[00:30:54]</a>.
*   **Higher Temperature (e.g., 1)**: Increases creativity, allowing the model to "think out of the box" and explore tangents, suitable for creative writing <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. This can be thought of as "wine mode" <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.

## Cost and Efficiency
[[pricing_models_for_ai_apps | Pricing models for AI apps]] differ between providers. Fireworks AI charges around $8 per million tokens, significantly cheaper than OpenAI's reported rates for 01 Pro ($15 input, $60 output per million tokens) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. While a million tokens might seem like a lot, costs add up quickly when integrating AI into workflows, content creation, or business operations <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Future efficiency improvements are expected to drive down costs for AI models <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

## Future Implications and Opportunities
The advent of powerful reasoning models creates immense opportunities for businesses to gain an unfair advantage through efficiency and product quality <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

*   [[building_a_healthcarerelated_ai_app | Healthcare-related AI Apps]]: Small, efficient models running locally on devices like smartwatches could enable real-time transcription and situational awareness (e.g., detecting falls, providing medical information to paramedics) <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
*   [[multimodal_language_models_for_ad_creation | Multimodal Language Models]]: Models like GPT-4o can understand not just audio, but also tone, cadence, and even breathing rates, picking up "micro-expressions" <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This could revolutionize negotiations by providing real-time insights into human behavior <a class="yt-timestamp" data-t="00:46:49">[00:46:49]</a>.
*   [[challenges_in_ai_design_tools | Challenges in AI Design Tools]]: There's a need for more playful and human-centric interfaces for AI products <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.
*   **Picking the Right Tool**: It's essential to select the appropriate model for the specific use case, as not every task requires the most powerful or detailed reasoning <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.

The rapid advancements signify that "we're all actually still trying to understand what this intelligence can give us" <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a> <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>. Experimentation and community sharing are encouraged to discover new applications <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.