---
title: Using AI models for practical applications and startups
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Ray Fernando, a 12-year ex-Apple engineer who streams AI coding and is building an AI startup in real-time, discusses the practical applications of new reasoning models, specifically DeepSeek R1, for individuals and [[strategies_for_building_ai_startups | startups]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These advanced models are capable of thinking and reasoning, potentially leading to superhuman capabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## DeepSeek R1: An Overview
DeepSeek R1 is an advanced reasoning model from China that has been made open source for study <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is reportedly on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> and has gained popularity because it is free to use on its website, deepseek.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Data Privacy Considerations
When using deepseek.com or its app, user data is sent to servers hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This means the data is subject to Chinese rules, laws, and regulations, so users should be cautious about entering sensitive information, such as tax returns or medical records <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Methods for Using AI Models
There are several ways to interact with AI models, each with different implications for data privacy and control:

### 1. Direct Web Interface (deepseek.com)
This is the simplest way to access DeepSeek R1, but it involves sending data to Chinese servers <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **How to use**: Visit deepseek.com, click the "DeepSeek" button to enable thinking, and paste your prompt <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Web search can also be enabled for the prompt <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Limitations**: The server can often be busy due to popularity, leading to timeouts <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Data privacy is a significant concern <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### 2. API Providers (Fireworks AI, Groq, OpenRouter)
To maintain data control while leveraging powerful models, users can utilize API providers that host these models in regions like North America <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Examples**:
    *   **Fireworks AI**: Hosts the DeepSeek model and allows access via an API key <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. An application like Cursor uses the Fireworks API to ensure data is not sent to China <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Fireworks AI costs about $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
    *   **Groq**: Provides a distilled Llama 70B model that is incredibly fast <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   **OpenRouter**: Another API provider that offers access to numerous models, often with free credits to start <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>.
*   **Setup**: Requires setting up an API connection within a web UI, like Open Web UI. This involves obtaining a base URL and an API key from the provider <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>.

### 3. Local Machine (Open Web UI with Docker and Ollama)
For complete control and privacy, models can be run directly on a personal machine, even without an internet connection (e.g., on a plane) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.
*   **Tools**:
    *   **Docker**: Required to run containers, which package the entire application <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
    *   **Open Web UI**: A user-friendly interface similar to ChatGPT for managing and interacting with local models <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
    *   **Ollama**: A tool for downloading and running various local AI models <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
*   **Setup Process**:
    1.  Download and install Docker Desktop for your operating system (e.g., Apple Silicon for Mac) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
    2.  Pull the Open Web UI Docker container using a terminal command <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.
    3.  Run the container. For Nvidia GPUs, include `gpus=all` for efficiency <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
    4.  Access the Open Web UI via `localhost:3000` in your web browser <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
    5.  Download Ollama and install it <a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>.
    6.  Within Open Web UI's admin panel, connect to the Ollama API, which is often pre-configured <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
    7.  Pull models like DeepSeek R1 from Ollama within Open Web UI's settings <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Performance**: Running models locally consumes system resources (e.g., RAM) <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>. Smaller, "distilled" versions of models run faster but may offer less detailed results than larger models run via API <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.

### 4. Mobile Devices (Apollo App)
Some applications allow running AI models directly on mobile devices for local processing.
*   **Apollo App**: A paid app for iOS that allows users to download and run AI models locally on their phones, utilizing the device's memory <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>, <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. It can also connect to API providers like OpenRouter <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>.
*   **Requirements**: Models can be large (several gigabytes), requiring sufficient phone storage <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Optimized to run on Apple hardware/silicon <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **Benefit**: Enables AI capabilities even without internet connectivity <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>.

## Practical Applications and Use Cases
AI models offer significant advantages for content creation, research, and business operations, often acting like a virtual "admin" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

*   **Content Generation**: Transcribing videos and automatically generating blog posts from transcripts, including analysis, geopolitical implications, future predictions, graphs, and SEO enhancements <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Information Verification**: Using web search capabilities to verify claims within articles or other texts <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
*   **Research and Analysis**: Performing thoughtful analysis on large texts, extracting key takeaways, and presenting information in a structured, human-like manner <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>, <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **Prompt Improvement**: Using tools like OpenAI's platform playground to refine prompts for efficiency and desired outputs, creating "long chains of thought" <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   **Business Efficiency**: Providing an "unfair advantage" for [[strategies_for_building_ai_startups | startups]] by increasing efficiency, lowering costs, and enhancing product quality <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Future Applications**: The potential for AI to understand audio, tone, and even breathing rate opens doors for applications in negotiation, emergency services (e.g., watch-based AI assisting paramedics), and advanced translation <a class="yt-timestamp" data-t="00:45:49">[00:45:49]</a>, <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. These potential [[startup_ideas_using_ai_technology | startup ideas using AI technology]] include developing apps for watches or other devices <a class="yt-timestamp" data-t="00:45:14">[00:45:14]</a>.

## Model Performance and Tweaking
The performance and output quality of AI models can vary based on their size and configuration:
*   **Parameters**: Models with a larger number of parameters (e.g., 600 billion+) are more intelligent and take longer to think, but yield better results <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Distilled models are smaller, faster, and efficient but may not provide the same level of detail <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Reasoning Models**: Models like DeepSeek R1 and OpenAI's 01 Pro spend extra time paying attention to instructions, leading to more detailed and accurate outputs <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Temperature**: A crucial setting that influences model output.
    *   **Lower Temperature (e.g., 0.8 to lower)**: Reduces "hallucination," making the model follow instructions better and preventing it from veering off-topic <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>. Ideal for logical reasoning and coding <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
    *   **Higher Temperature (e.g., 1)**: Encourages extreme creativity <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Useful for creative writing or non-logical reasoning where out-of-the-box thinking is desired <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.

> "To me I would rename that temperature as you know wine versus coffee mode. Wine might get you a little more creative. But if you know if if you want more rational execution style maybe you want coffee mode." <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>

## Cost of API Usage
While some models are free to use on their native websites, using APIs incurs costs based on token usage.
*   **Fireworks AI**: Approximately $8 per million tokens <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **OpenAI (01 Pro)**: Historically, around $15 for input and $60 for output per million tokens <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. However, future models like 03 and Mini are expected to significantly drop prices as they become more efficient <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Token Accumulation**: These costs add up significantly when AI is integrated into daily workflows for content pumping, ongoing research, or [[using_ai_to_build_saas_startups | building businesses around AI]] <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

## Getting Started and Opportunities
The current era offers significant opportunities for experimentation and innovation with AI models <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.
*   **Experimentation**: Users are encouraged to try out different models on Ollama and compare their outputs using Open Web UI to see what works best for their specific use cases <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.
*   **Developing Prompts**: A good starting point for prompt generation includes defining desired instructions, expected output types, and unwanted elements <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Iteration over time helps refine prompts for specific use cases <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Startup Potential**: Leveraging these models can uncover multi-million dollar [[startup_ideas_using_ai_technology | startup ideas using AI technology]] <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>. There is a "rush to understand who can host these huge models" reliably for businesses and apps <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Community and Learning**: It's important to not feel left behind as the technology evolves rapidly <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>. Engaging with the community, sharing discoveries, and experimenting are key to understanding the intelligence these models offer <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

For more information and assistance in setting up these tools, Ray Fernando can be reached at rayfernando.com or his YouTube channel, Ray Fernando 1337 <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.