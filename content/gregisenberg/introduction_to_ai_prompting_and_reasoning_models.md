---
title: Introduction to AI prompting and reasoning models
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

This article explores the burgeoning field of AI prompting and reasoning models, focusing on DeepSeek R1 and practical methods for its application and hosting. Ray Fernando, a 12-year ex-Apple engineer, discusses the capabilities of these advanced models and their implications for individuals and businesses alike <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## DeepSeek R1: A New Era of Reasoning Models

DeepSeek R1 is a new reasoning model, specifically designed to "think and reason," which can lead to "superhuman capabilities" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Developed in China, this model has been made open source for study <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is reportedly on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> and has gained significant traction because it is free to use on its website, deepseek.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

The models that possess "really large parameter" counts (e.g., 600 billion+ parameters) tend to have "more intelligence to leverage" and take longer to think, but their results are "really really really great" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Smaller, "distilled" versions of these models run faster and are efficient, though they might not "think as long" or provide the same level of detailed results <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Data Privacy and Hosting Considerations

When using deepseek.com, it's crucial to understand that the service is hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This means any data sent to the system falls under Chinese laws and regulations, potentially leading to privacy concerns for sensitive information <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

> [!CAUTION] Data Privacy Warning
> Avoid submitting sensitive data (e.g., tax returns, medical records) directly to deepseek.com or its associated apps, as your data will be sent to and stored in China, where different privacy laws apply <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Alternative Methods for Using DeepSeek Models

To mitigate data privacy concerns and improve reliability, several alternatives exist for accessing and running DeepSeek models:

### 1. Cloud-Based API Providers
Various API providers host DeepSeek models, allowing users to interact with them without sending data directly to China <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Fireworks AI**: Cursor, a coding app, uses Fireworks AI to host DeepSeek models, keeping data out of China <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Fireworks AI generally costs about $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Groq**: Hosts a "distilled llama 70b" model, which is "incredibly fast" and nearly instant in response <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **OpenRouter**: Another API provider that offers access to various models, including DeepSeek R1 <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

### 2. Running Models Locally
For maximum data control and offline capability, models can be run directly on a user's machine <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

#### Open Web UI
Open Web UI is a recommended interface for running models locally <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.
*   **Setup**: Requires Docker Desktop installed on your machine (e.g., Apple Silicon version for M-series Macs) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Commands**:
    1.  Pull the container: `docker pull ollama/ollama-webui` <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>
    2.  Run the container (for single-user mode): `docker run -d -p 3000:8080 --restart always -v ollama-webui:/app/backend/data --name ollama-webui ollama/ollama-webui` <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. For NVIDIA GPUs, add `--gpus all` to leverage the GPU <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
*   **Access**: Once running, access the interface via `localhost:3000` <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

#### Ollama
Ollama is a tool for downloading and running local AI models <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
*   **Installation**: Download from ollama.com <a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>.
*   **Integration with Open Web UI**: Ollama models (like DeepSeek R1) can be pulled directly into Open Web UI's model section <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.

#### Apollo App (Mobile)
For mobile devices, the Apollo app allows downloading and running local AI models, especially optimized for Apple silicon <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.
*   **Capabilities**: Allows offline use of models on devices <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>. Model sizes can be several gigabytes, so device memory is a factor <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.
*   **Use Case**: Enables powerful AI capabilities, even without an internet connection, such as advanced transcription or situational awareness for emergency response <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Practical Application: Content Generation from Transcripts

One practical example is generating a blog post from a video transcript <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Workflow**: Transcribe a video <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, then provide the transcript to a model like DeepSeek R1 with instructions to analyze and generate a blog post <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Quality**: Full reasoning models can produce "human-level" outputs that resemble content a "senior writer would do" or a "research engineer" <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Distilled models, while faster, provide less detailed responses <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Benefits**: Reasoning models "spend extra time and actually pay attention to your instructions," leading to highly tailored and useful outputs <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

## Optimizing Prompts for AI Models

The quality of AI output heavily relies on effective prompting.

### [[creating_and_using_reusable_modular_ai_prompts | Creating and Using Reusable Modular AI Prompts]]
OpenAI's platform.openai.com offers a playground to reconfigure and improve prompts <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   Users can describe a desired prompt, and the platform will reconfigure it to be more efficient for the language model <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.
*   This mechanism helps generate "long chains of thought or reason or outputs" <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.

### Key Elements for Effective Prompts
When designing prompts, consider:
1.  **Instructions**: Clearly state what you want the model to do <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>.
2.  **Desired Output**: Define the expected format or type of output <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>.
3.  **Undesired Output**: Specify what you *don't* want the model to include <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>.

### Temperature Setting
The "temperature" setting in AI models controls creativity and adherence to instructions <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>:
*   **Lower Temperature (e.g., 0.8 default to lower)**: Makes the model "hallucinate less," follow instructions better, and stay on topic <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. Ideal for logical reasoning and coding <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Higher Temperature (e.g., to 1)**: Encourages extreme creativity, useful for creative writing or "non-logical reasoning" <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.
*   This can be likened to "coffee mode" for rational execution and "wine mode" for creative output <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

## The Future of AI: Models, Hosting, and Applications

The rapid advancement of AI models is creating an "AI arms race" <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>, with increasing demand for GPUs and reliable hosting providers <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

### Omni Models
OpenAI's GPT-4o models represent a significant breakthrough, capable of understanding not just text but also "audio and tone and all these extra implications" <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>. This enables advanced capabilities like understanding breathing rate in negotiation or mimicking "micro expressions" <a class="yt-timestamp" data-t="00:46:33">[00:46:33]</a>.

### [[tutorial_on_ai_tools_and_startup_ideas | Startup Opportunities]]
The accessibility of powerful models creates vast opportunities for [[framework_for_developing_ai_saas_ideas | developing AI SaaS ideas]] and [[practical_examples_of_ai_project_development | practical examples of AI project development]] <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>:
*   **Competitive Advantage**: Leveraging the right model for specific tasks can provide a significant advantage in business <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **[[developing_user_interfaces_with_ai_tools | Developing User Interfaces with AI Tools]]**: The intelligence of models requires innovative user interfaces to make them accessible and playful <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.
*   **New Use Cases**: Ideas range from real-time translation and negotiation assistance to emergency response systems integrated with personal devices like watches or airpods <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

> [!TIP] Start Experimenting
> "Whatever you can get your hands on make sure you do that" to experiment with models and discover potential app ideas. The "playground" feature in tools like OpenAI is a great starting point for generating prompts and observing outputs <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.

The evolution of AI models, particularly reasoning models like DeepSeek R1 and Omni models, signifies a significant leap in intelligence and potential applications <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. By understanding their capabilities, hosting options, and prompt optimization techniques, individuals and businesses can harness this technology for innovation and competitive advantage <a class="yt-timestamp" data-t="00:47:42">[00:47:42]</a>.