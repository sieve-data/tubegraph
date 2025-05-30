---
title: Using Local Language Models LLM for Code Generation
videoId: p1YvKuRfEhg
---

From: [[colemedin]] <br/> 

A community-driven fork of the popular AI code generator `bolt.new` has been developed to enable users to select their preferred Large Language Model (LLM) for code generation, including the option to use [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This contrasts with the main version of `bolt.new`, which forces users to use a single, predetermined model <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The integration of [[working_with_local_large_language_models | local LLMs]] allows for infinite code generation completely free of charge <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

The project emphasizes a community-driven approach, incorporating user suggestions, feedback, and contributions <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This collaborative effort aims to evolve the `bolt.new` fork into a powerful and versatile tool for AI-powered code generation <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Key Improvements and Features

The fork introduces several significant improvements over the official `bolt.new` platform <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:

### Selectable LLM Providers and Models
Users can now choose their LLM provider, such as OpenAI or Google, and select specific models <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This includes integration with OpenRouter for a wide range of models <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> and Gemini (1.5 Flash and Pro) <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Dynamic Olama Integration for Local LLMs
A crucial feature is the integration with [[using_llama_for_LLMs | Olama]], enabling the use of [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
Originally, the fork had a hardcoded list of [[using_llama_for_LLMs | Olama]] models <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. However, a community contribution made the list of available [[using_llama_for_LLMs | Olama]] models dynamic, displaying only those models actually downloaded locally by the user via the [[using_llama_for_LLMs | Olama]] API <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This resolves issues where users would select models they didn't possess, leading to confusion <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

> [!INFO] Technical Details
> The base URL for [[using_llama_for_LLMs | Olama]] is now an environment variable <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. Hardcoded [[using_llama_for_LLMs | Olama]] models have been removed from the constants file, replaced by a function that queries the [[using_llama_for_LLMs | Olama]] API for currently installed models <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Code Download as Zip
The most requested feature was the ability to download the generated code as a zip file <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This eliminates the need to manually copy and paste individual files out of the `bolt.new` UI <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The download function utilizes `jszip` and `file-saver` to compile files into a zip archive <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Provider Filtering
A new dropdown allows users to filter models by provider, streamlining the selection process and preventing users from sifting through a massive combined list of models <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## Demonstration Overview
The demonstration showcased the process of selecting an LLM provider and model, entering a prompt (or using a predefined template), and witnessing the AI generate project files, run `npm` commands, and provide an app preview <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. An example of a to-do app was created, highlighting `bolt.new`'s strength in generating front ends <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Future Work and Challenges
The project has a comprehensive list of requested features for future implementation <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>:

*   **LM Studio Integration:** Many users prefer LM Studio for their [[working_with_local_large_language_models | local models]], necessitating an integration <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   **Deepseek API Integration:** Due to the strong performance of Deepseek Coder models (especially the 36 billion parameter version), integration with their API is requested <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Improving `bolt.new` Prompting for Smaller Models:**
    [[benchmark_performance_of_LLMs | Smaller models]] often struggle with the default `bolt.new` prompting, failing to open the web container and generate code <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. This indicates an opportunity to refine the prompting to be more understandable for LLMs with less context handling capability <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
    > [!TIP] Workaround for Smaller Models
    > A temporary workaround involves sending a prompt, stopping generation as it starts, manually opening the code container, and then redoing the prompt. This has been reported to help smaller models generate code correctly <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

*   **Attaching Images to Prompts:** The paid version of `bolt.new` allows image attachments, a feature currently missing from the open-source fork <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Backend Agent Integration:** A significant future goal is to implement [[local_LLMs_for_AI_agent_swarms | AI agent swarms]] in the backend, allowing multiple LLMs to work together for more robust code generation, potentially using tools like LangChain, LangGraph, or OpenAI swarm <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This would be a game-changer for AI code generators <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Publishing Projects to GitHub:** Similar to the paid version, direct GitHub publishing is a desired feature <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Loading Local Projects:** The ability to import existing projects from local environments (e.g., VS Code) into `bolt.new` for continued work <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **General Prompting Improvements:** Refining the core `bolt.new` prompt for better overall results, especially concerning UI/UX aspects and state management, as the open-source version sometimes lags behind the paid version in UI aesthetics <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Community-Driven Development
The project emphasizes its evolution from "my fork" to "our fork," with a commitment to continuous improvement through community contributions <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. The goal is not monetization but collaborative learning and building something truly amazing together <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.