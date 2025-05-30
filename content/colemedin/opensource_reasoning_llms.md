---
title: Opensource reasoning LLMs
videoId: -GmEIqi0yNE
---

From: [[colemedin]] <br/> 

One of the most impactful advancements in AI currently is the development of reasoning models, which are Large Language Models (LLMs) capable of internal thought processes before generating a final response to a user <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This capability leads to significantly improved results <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

Several reasoning LLMs are already available, including OpenAI's 01 and 03, and the open-source Qwen <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. DeepSeek has recently entered this space with the release of their open-source reasoning LLM, R1 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. R1 offers various versions, with some variations reportedly more powerful than OpenAI's 01 and Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## DeepSeek R1 Overview

DeepSeek R1 is a fully open-source model released under an MIT license, allowing for free commercial use <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. As a "thinking model," it processes its response internally before delivering the final answer <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Users can interact with R1 through a ChatGPT-like interface by enabling "Deep Think" on chat.deepseek.com <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. When a question is posed, R1 displays grayed-out text, indicating its internal thought process, before providing the final, bolded answer <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This reasoning approach consistently yields better answers <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### [[benchmark_performance_of_llms | Benchmark Performance]]

While benchmarks should be viewed with caution as they are provided by DeepSeek, R1 demonstrates impressive performance <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. In comparisons with OpenAI's 01, 01 Mini, and their original DeepSeek V3 model, R1 performs comparably, and sometimes even better, across various benchmarks <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This performance is particularly notable given that R1 is a smaller, open-source model with more affordable versions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Cost-Effectiveness

DeepSeek R1 is significantly more affordable than its competitors <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. For example:
*   It costs $0.55 per million input tokens and $2.19 per million output tokens <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   This makes it multitudes cheaper than 01 Mini, and dozens of times cheaper than 01 <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   Even compared to Claude 3.5 Sonnet, R1 is more affordable, costing $3 per million input tokens <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Running DeepSeek R1 Locally

DeepSeek has created smaller versions of R1 by fine-tuning their reasoning capabilities onto competitor models like Qwen and [[using_llama_for_llms | Llama]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. These distilled versions can be downloaded and run locally via platforms like Ollama and Hugging Face <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

A 14 billion parameter version of R1 (based on Qwen) is capable of performing on par with 01 Mini, making it accessible to run on most personal computers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Using Ollama

To run R1 locally with Ollama:
1.  Install Ollama from ollama.com <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
2.  Navigate to the DeepSeek R1 page on Ollama and select the desired version (e.g., 14 billion parameter version) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
3.  Copy the provided command and paste it into a terminal <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This will either install the model or immediately launch a chat interface <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
4.  When interacting, the model will output a "thinking" tag at the start and end of its internal processing, with the final user-facing response appearing after the closing tag <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This allows for filtering the output if building an AI agent <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Using Hugging Face

For users preferring platforms like LM Studio or Llama CPP, models can also be installed via Hugging Face <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
1.  Go to the main R1 page on Hugging Face <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
2.  Scroll down to "Quantizations" and select a suitable model, such as the Qwen 14 billion parameter version from "UNSLOTH" <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
3.  Click "Use this model" to reveal installation options for LM Studio and Llama CPP <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

The largest version of R1, a 671 billion parameter model, is approximately 400 GB in Q4 quantization and is generally too large to run on consumer hardware without significant investment <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This version is typically accessed via the DeepSeek or OpenRouter API <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## DeepSeek R1 as an [[Using Local Language Models LLM for Code Generation | AI Coding Assistant]]

DeepSeek R1 was tested as an [[Using Local Language Models LLM for Code Generation | AI coding assistant]] using Bolt.DIY, an open-source tool that allows integration with various LLMs, including locally downloaded models <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The most powerful 671 billion parameter version of R1 was used via the DeepSeek API for this demonstration <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

The task involved building a chat interface for an n8n AI agent, including chat history management and [[The role of cloud services in hosting LLMs | Superbase]] integration, all with a single prompt <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This setup was compared to Claude 3.5 Sonnet, a model widely used by other [[coding_capabilities_of_reasoning_llms | AI coding assistants]] like Lovable and Bolt.new <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

### R1's Performance

R1 successfully built the complex chat application in a single shot <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The entire process used only 9,000 tokens, resulting in a cost of less than a single penny <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

Initial results from R1's one-shot attempt:
*   **Authentication**: [[The role of cloud services in hosting LLMs | Superbase]] authentication worked immediately <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **UI/UX**: The application's design was significantly better than a similar one built with Lovable, featuring clear message distinction, a well-designed toggle, and good mobile responsiveness <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
*   **Functionality**: Conversation history was displayed correctly, and it could send messages and receive responses from the n8n agent <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>, <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
*   **Initial Issues**:
    *   Messages were duplicated <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
    *   No "new conversation" button <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
    *   No logout button <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

These minor issues were easily fixed with a couple of follow-up prompts to R1 <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. The final, corrected application included a "new conversation" button, no duplicate messages, and a logout button <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

### Claude 3.5 Sonnet's Performance

Using the exact same prompt, Claude 3.5 Sonnet's one-shot attempt yielded a "decent" looking result, but not as polished as R1's <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   **UI/UX**: The design was not as appealing as R1's <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **Missing Features**: It also initially lacked features like creating a new conversation and logging out, similar to R1's first attempt <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Functionality**: Crucially, Claude 3.5 Sonnet's one-shot attempt failed to communicate with the n8n agent, unlike R1's successful initial communication <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. This indicates that Claude generally struggles more with these types of complex, multi-component requests <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

Overall, R1 significantly outperformed Claude 3.5 Sonnet in this complex [[coding_capabilities_of_reasoning_llms | AI coding]] task <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

## Conclusion

DeepSeek R1 demonstrates impressive power and affordability, offering a compelling open-source alternative to proprietary LLM APIs like those from Anthropic or OpenAI <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>. Its ability to run locally or through platforms like OpenRouter makes its capabilities widely accessible <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.