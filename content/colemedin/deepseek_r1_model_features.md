---
title: DeepSeek R1 model features
videoId: -GmEIqi0yNE
---

From: [[colemedin]] <br/> 

DeepSeek R1 is a recently released open-source reasoning Large Language Model (LLM) developed by DeepSeek <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. It is described as one of the "hottest things with AI right now" due to its ability to "think to themselves before giving a final answer to the user" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Key Features

### Reasoning Capabilities
DeepSeek R1 is a "thinking model" that processes its response internally before providing the final answer <a class="yt-timestamp" data-t="01:43:08">[01:43:08]</a>. This internal thought process, displayed as "greyed out text" in their chat platform, generally leads to better answers <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. Users can experience this feature on chat.deepseek.com by enabling "deep think" <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

### Open-Source and Licensing
DeepSeek R1 is a fully open-source model released under an MIT license, allowing for free commercial use <a class="yt-timestamp" data-t="01:33:08">[01:33:08]</a>.

### Performance Benchmarks
DeepSeek R1's performance is often on par with or even surpasses models like OpenAI's O1 and Claude 3.5 Sonet <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>, <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. Benchmarks from the DeepSeek blog indicate its strong performance across various tests, often matching or exceeding O1 in every benchmark <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>, <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. Notably, its 14 billion parameter model is "on par with O1 mini" <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>, which is considered incredible for a model of its size <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

### Cost-Effectiveness
DeepSeek R1 is significantly more affordable than many competitors. Its pricing is reported at 55 cents for every million input tokens and $2.19 for every million output tokens <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This makes it "dozens and dozens of times cheaper" than O1, despite comparable performance <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. It is also cheaper than Claude 3.5 Sonet <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

## Versions and Local Deployment

DeepSeek R1 is available in various versions, allowing for flexibility in deployment:
*   **DeepSeek R1 (API)**: The most powerful version is a 671 billion parameter model, accessible via the DeepSeek API or OpenRouter API <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>, <a class="yt-timestamp" data-t="10:27:00">[10:27:27]</a>. This version, even with Q4 quantization, is very large (400 GB) and generally too big for personal computers <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.
*   **Distilled Versions**: Smaller, fine-tuned versions of R1 are available, based on competitor models like [[qwen_25_coder_32b_local_ai_model | Qwen]] and Llama <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>, <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. These can be downloaded and run locally. Examples include:
    *   1.5 billion parameter model (based on [[qwen_25_coder_32b_local_ai_model | Qwen]]) <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>
    *   8 billion parameter model (based on Llama) <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>
    *   14 billion parameter model (based on [[qwen_25_coder_32b_local_ai_model | Qwen]]), which can be run by "almost anyone on their computer" <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>, <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
    *   70 billion parameter model (based on Llama) <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>

### Local Deployment Options
DeepSeek R1 models can be run using [[working_with_local_large_language_models | local large language models]] platforms:
*   **Ollama**: Models can be installed and run easily via the Ollama command line interface <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.
*   **Hugging Face**: Models are available for download and can be used with platforms like LM Studio and Llama CPP <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>, <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.

## Practical Application in Bolt.DIY

DeepSeek R1 has been demonstrated as an AI coding assistant within Bolt.DIY, an open-source AI coding assistant <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

### AI Coding Performance
In a demonstration, DeepSeek R1 was tasked with building a complex chat interface for an n8n AI agent with Supabase integration, including chat history management and authentication <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>, <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.
*   **One-shot Generation**: R1 built a functional and visually appealing application in a single prompt ("one-shot") <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>, <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. The entire process used only 9,000 tokens, costing "multitudes less than a single penny" <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.
*   **Comparison to Claude 3.5 Sonet**: When compared to Claude 3.5 Sonet (often considered a top AI coding model), R1 demonstrated superior performance <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>, <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>, <a class="yt-timestamp" data-t="18:37:00">[18:37:00]</a>. While Sonet produced a "decent" looking app initially, it failed to communicate with the n8n agent API in its first attempt, unlike R1 <a class="yt-timestamp" data-t="19:25:00">[19:25:00]</a>, <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.
*   **Iterative Improvement**: Even with initial minor glitches, R1 allowed for very quick iterative fixes with a few additional prompts, resulting in a perfectly functioning application with features like new conversation initiation and logout buttons <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>, <a class="yt-timestamp" data-t="18:29:00">[18:29:00]</a>.

DeepSeek R1 is highlighted as an "absolutely insane" model that offers significant power and affordability, making it a compelling choice for AI development <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>, <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>.