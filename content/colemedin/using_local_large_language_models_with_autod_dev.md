---
title: Using local large language models with autod Dev
videoId: 8ommGcs_-VU
---

From: [[colemedin]] <br/> 

[[working_with_local_large_language_models | Autod Dev]] is a community-driven fork of Bolt.new that aims to implement much-needed features, including the ability to use any [[large language model | large language model]] (LLM), such as [[working_with_local_large_language_models | local ones]] with Ollama <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While Bolt.new originally only supported Claude 3.5 Sonnet, many users prefer [[working_with_local_large_language_models | local LLMs]] because they eliminate costs and avoid rate limits <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Adding support for other [[large language model | large language models]] was a priority in [[autod Dev | Autod Dev]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This article provides tips and tricks for [[creating_applications_with_local_llms_in_autod_dev | using local LLMs to build full applications]] within [[autod Dev | Autod Dev]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Getting Started with Autod Dev

To follow along with [[creating_applications_with_local_llms_in_autod_dev | using local LLMs]] in [[autod Dev | Autod Dev]], it's assumed that [[autod Dev | Autod Dev]] is already up and running on your machine <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. If not, the [[autod Dev | Autod Dev]] README provides full setup instructions, including how to run it with or without Docker, and how to install Ollama to get [[working_with_local_large_language_models | local LLMs]] on your machine <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Tips and Tricks for Using Local LLMs with Autod Dev

### Fixing Context Length Issues

A common issue when [[working_with_local_large_language_models | using local LLMs]] with [[autod Dev | Autod Dev]] is that the model might not open the web container or create necessary files <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This happens because Ollama's default context length for any model is 2048 tokens, which is insufficient for the Bolt.new prompt <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. As a result, the model loses context and cannot interact with the web container properly <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The solution is to create a slight variation of the Ollama model with an increased context length <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This can be done by creating a file (e.g., `Model file`) with two lines <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>:

```
FROM [your_olama_model_ID]
PARAMETER num_ctx [new_context_limit]
```
For example, to increase the context for `Quen 2.5 Coder 7B` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>:
```
FROM quen 2.5 coder 7B
PARAMETER num_ctx 32768
```
The new context limit should be above 8192, as that is the default limit for Bolt.new <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Running the command `olama create -f [your_model_file_name] [new_model_name]` will create this modified model, which will then work seamlessly within [[autod Dev | Autod Dev]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Iterative Development Strategy

When [[creating_applications_with_local_llms_in_autod_dev | building applications]] with [[working_with_local_large_language_models | local LLMs]], it's highly recommended to start simple and iteratively increase complexity <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This strategy helps avoid hallucinations and ensures the application isn't broken from the start <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Even with larger models like Claude 3.5 Sonnet, this approach is beneficial for developing complex applications <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

When providing prompts for UI/UX, be detailed with requirements such as colors, padding, and measurements. Providing these design details can significantly guide the [[large language model | LLM]] in creating the desired output <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

### [[Comparing local and cloudbased large language models | Comparison and Recommendations]]

While [[comparison_between_local_and_large_ai_models | smaller models]] and [[working_with_local_large_language_models | local LLMs]] are powerful, it's important to acknowledge that massive closed-source models like Claude 3.5 Sonnet and GPT-4o generally offer the best performance <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. However, these models come with rate limits and costs <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

For a powerful, affordable, and open-source alternative that can mitigate some issues faced with [[comparison_between_local_and_large_ai_models | smaller local models]], DeepSeek Coder Version 2 (236 billion parameters) is highly recommended <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. It can be accessed via OpenRouter or the DeepSeek API directly <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. DeepSeek Coder V2 is significantly more affordable than Claude, costing around 14 cents per million input tokens and 28 cents per million output tokens, compared to Claude's $3 and $15 respectively <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Its benchmarks are also very strong, making it a good choice for [[creating_applications_with_local_llms_in_autod_dev | developing web applications]] without commercial platform rate limits <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Building an Application with a Local LLM

An example of [[creating_applications_with_local_llms_in_autod_dev | building a full application]] with a [[working_with_local_large_language_models | local LLM]] involved using Quen 2.5 Coder 7B within [[autod Dev | Autod Dev]] to [[ai_agents_and_large_language_models | chat with an AI agent]] built in n8n <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

The process involved:
1.  **Initial Simple Prompt**: Starting with a basic prompt to create a Next.js chat interface using the `Quen 2.5 Coder 7B` model with the increased context length <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This initially produced a functional but visually basic application <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
2.  **UI/UX Refinement**: Iterating on the initial application by providing a detailed prompt with UI/UX requirements, including specific colors, padding, and measurements <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This significantly improved the visual appearance and functionality, including a loading indicator <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
3.  **Integrating with an [[ai_agents_and_large_language_models | AI Agent]]**: The final iteration involved integrating the chat interface with an n8n [[ai_agents_and_large_language_models | agent]] API endpoint <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. The prompt included the API endpoint, required payload structure, authorization details, and the expected output field from the JSON response <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
    *   Even if the model messes up styling during this step, simply prompting it to correct the styling will fix it <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   The completed application successfully communicated with the n8n [[ai_agents_and_large_language_models | agent]], demonstrating its ability to process requests and retrieve information from a knowledge base <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

This demonstration highlighted the power of even a [[comparison_between_local_and_large_ai_models | smaller model]] like Quen 2.5 Coder (7 billion parameters) to create a robust starting point for a production-ready application using [[autod Dev | Autod Dev]] and Ollama <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

## Future of Autod Dev

More content on [[autod Dev | Autod Dev]] is planned, including tutorials on contributing, deploying applications, and working with Docker <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. The future of [[autod Dev | Autod Dev]] is exciting, especially its potential with [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.