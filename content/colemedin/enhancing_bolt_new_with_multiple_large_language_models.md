---
title: Enhancing Bolt new with multiple large language models
videoId: 3PFcAu_oU80
---

From: [[colemedin]] <br/> 

[[Integrating various models with Bolt new | Bolt.new]] is a powerful, open-source large language model (LLM) web development platform that allows users to create and deploy full-stack applications directly in the browser with the help of AI <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is considered a significant improvement over tools like Claude or Vercel, and greatly accelerates full-stack development <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While not perfect, it functions as a fantastic coding assistant to initiate projects <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Limitations of the Stock Bolt.new Platform

Despite its utility, the original [[integrating_various_models_with_bolt_new | Bolt.new]] platform presents two significant problems <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:

1.  **Limited Usage**: Similar to other platforms, [[integrating_various_models_with_bolt_new | Bolt.new]] imposes usage limits, which can force users to stop coding mid-application <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Fixed LLM Choice**: The platform is restricted to using Claude 3.5 Sonnet, preventing users from selecting other LLMs like GPT or fine-tuned [[working_with_local_large_language_models | local LLMs]] that might offer cost savings or specialized capabilities <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This highlights the [[limitations_of_large_language_models | limitations of large language models]] when restricted to a single option <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## The Solution: A Forked and Extended Bolt.new Version

To address these issues, a solution has been developed by forking [[integrating_various_models_with_bolt_new | Bolt.new]], running it locally, and extending its platform to support multiple LLMs <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This allows for unlimited usage and the flexibility to choose different models <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Key Enhancement: LLM Selection

The primary enhancement in this forked version is a dropdown menu that allows users to select the [[reasoning_large_language_models_and_their_impact | large language model]] they wish to use with [[integrating_various_models_with_bolt_new | Bolt.new]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Supported Models
The expanded selection includes models from:
*   Anthropic <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   OpenAI (e.g., GPT-4o) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>
*   Grok <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   Ollama, for various [[working_with_local_large_language_models | local LLMs]] specifically fine-tuned for coding, such as Code Llama, Deepseek Coder, and Qwen 2.5 Coder <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Benefits
Running [[integrating_various_models_with_bolt_new | Bolt.new]] locally with [[working_with_local_large_language_models | local models]] offers several [[benefits_of_hosting_your_own_large_language_models | benefits]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>:
*   **Unlimited Usage**: There are no usage limits, and users pay nothing for credits when using [[working_with_local_large_language_models | local models]] via Ollama <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Privacy**: Running locally ensures that operations are entirely private, unless data is explicitly sent to cloud-based models like GPT <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Flexibility**: Users can switch between models mid-conversation, enabling experimentation with different LLMs for various tasks <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Power**: Potentially, more powerful [[working_with_local_large_language_models | local models]] (e.g., Deepseek Coder 236B), if the [[hardware_requirements_for_running_large_language_models_locally | machine can support them]], may yield better results than default cloud models <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The ability to [[using_knowledge_bases_to_enhance_language_models | fine-tune these models]] further expands possibilities <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Challenges with Local Models
While beneficial, some [[challenges_with_large_language_models | challenges with large language models]] arise, particularly with smaller local models:
*   **Web Container Integration**: Smaller models (e.g., 7 billion parameters) may not always work optimally with [[integrating_various_models_with_bolt_new | Bolt.new]]'s web container, sometimes failing to spin it up <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Context Limitations**: Due to massive behind-the-scenes prompts in [[integrating_various_models_with_bolt_new | Bolt.new]], weaker models may struggle with context limitations, leading to suboptimal results in the preview environment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a> <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. However, the generated code often functions correctly when tested externally (e.g., in a JSFiddle) <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## How to Run the Forked Version

The modified [[integrating_various_models_with_bolt_new | Bolt.new]] code is available on GitHub, allowing users to download and run it locally <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

### Prerequisites
*   Google Chrome Canary browser is required <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   Ollama must be installed and running on your machine to use [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Models can be downloaded from ollama.com's library using a simple terminal command <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

### Installation Steps
1.  Clone the custom Fork version URL from the provided GitHub repository <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Install all necessary packages <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
3.  Open the `.env.example` file and set environment variables for API keys of desired cloud models (e.g., GPT, Grok) <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. No API key is needed for Ollama as it connects directly to the local host <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
4.  Run the `pnpm run dev` command to start the application <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

## Technical Overview of Changes

The modifications involved changes in both the frontend and backend components of [[integrating_various_models_with_bolt_new | Bolt.new]], which uses a standard front-end structure <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Frontend Modifications

1.  **`constants` file (`utils` folder)**: This file defines the default model (Claude 3.5 Sonnet) and a comprehensive list of available models <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Each model is an object with a `name` (model ID), `label` (display name), and `provider` <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Adding new models for existing providers (e.g., Ollama) is straightforward by adding a new record with the model ID and label <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
2.  **Main Chat Component**: A new state was introduced to represent the selected model in the frontend <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
3.  **Passing Model to Backend**: Due to limitations with the Vercel AI SDK's `useChat` Hook, the selected model is embedded within the content of the user's message itself <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This method was inspired by [[integrating_various_models_with_bolt_new | Bolt.new]]'s approach to pass file modifications to the backend <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
4.  **Base Chat Component**: This component loops over the model list to create the model selection dropdown <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
5.  **User Message Component**: Regular expressions are used to remove the model information from the user message content before it is displayed in the frontend, preventing confusion for the LLM and the user <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Backend Modifications

1.  **API Endpoint**: The API endpoint serves as the entry point to the backend, calling the `streamText` function to process responses from the LLM <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
2.  **`streamText.ts` file**: Within the `streamText` function, the latest model specified by the user is extracted from the messages, allowing for dynamic model switching mid-conversation <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Messages are also sanitized to remove model IDs before being passed to the LLM <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
3.  **`getModel` function**: This function retrieves the appropriate LLM instance based on the provider and model ID <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
4.  **`apiKey.ts` file**: A simple switch statement determines the correct API key based on the provider (e.g., Anthropic, OpenAI, Groq), returning an empty string if no API key is needed (e.g., for Ollama) <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
5.  **Model Instance Retrieval**: Separate functions, using the Vercel AI SDK, are used to fetch the model instance for each specific provider <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. To add a new provider (e.g., Together AI, Fireworks), a new function, API key environment variable, and additions to the switch statements in `apiKey.ts` and `getModel` are required, provided the provider is supported by the Vercel AI SDK <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

This extended version of [[integrating_various_models_with_bolt_new | Bolt.new]] significantly boosts productivity when coding with LLMs by offering unlimited usage and unparalleled model flexibility <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.