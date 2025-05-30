---
title: Integrating various models with Bolt new
videoId: 3PFcAu_oU80
---

From: [[colemedin]] <br/> 

Bolt.new is described as a powerful and open-source Large Language Model (LLM) web development platform that enables users to create and deploy full-stack applications directly in the browser with the assistance of AI <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is considered a significant improvement over tools like Claude or v0 for speeding up full-stack development <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While not perfect, it serves as a valuable AI coding assistant <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Limitations of the Standard Bolt.new Platform

Despite its capabilities, the standard Bolt.new platform presents two primary limitations:
1.  **Limited Usage**: Users face restrictions on platform usage, similar to services like Claude or v0, which can interrupt coding sessions <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Fixed LLM Choice**: The platform is hardcoded to use Claude 3.5 Sonnet as its LLM <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. While Claude 3.5 Sonnet is a capable LLM, users cannot choose other models like GPT, or utilize local LLMs fine-tuned for coding, which could offer cost savings or specific optimizations <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## The Forked Solution: Overcoming Limitations

To address these issues, a solution was developed by forking the Bolt.new repository, running it locally, and extending its functionality <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This approach enables [[enhancing_bolt_new_with_multiple_large_language_models | enhancing_bolt_new_with_multiple_large_language_models]] and offers unlimited usage without cost when using local models <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. The original Bolt.new is open-source, allowing forking and modification <a class="yt-timestamp" data-t="01:50:07">[01:50:07]</a>.

### Demonstration of the Modified Platform

The key difference in the forked version's user interface (UI) is the addition of a dropdown menu allowing users to select their desired Large Language Model (LLM) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Supported models include:
*   **Anthropic**: Various models <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **OpenAI**: Such as GPT-4o <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Groq**: Including Llama 3.1 or 3.2 <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Ollama (Local Models)**: Integrations for numerous coding-specific models like Quen 2.5 Coder, Deep Seek Coder, and Code Llama <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Any local model runnable with Ollama can be integrated <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

Using a local model ensures privacy as data remains on the user's computer <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Models can be changed at any point during a conversation, allowing for flexible development <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

While smaller models (e.g., 7 billion parameters) might not always perform optimally with the web container due to the large context prompts used by Bolt.new, they can still produce good results when extracted and run in other environments like JS Fiddle <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>, <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. More powerful local models, such as Deep Seek Coder 236B, may even outperform Claude 3.5 Sonnet for base Bolt.new functionalities <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### [[technical_insights_on_modifying_bolt_new_frontend_and_backend | Technical Insights on Modifying Bolt.new Frontend and Backend]]

The forked version's code is available on GitHub, providing instructions for setup and usage <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

#### Setup Instructions
*   **Prerequisites**: Follow the instructions in the README, similar to the original Bolt.new repository <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Cloning and Installation**: Clone the custom fork URL, then install all necessary packages <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Environment Variables**: Set API keys in the `.env` example file for specific models (e.g., GPT, Groq). Ollama, being local, does not require an API key <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Browser**: Google Chrome Canary browser is required to run the application <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **Running the Application**: Execute `pnpm run dev` to start the local Bolt.new instance <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

#### Code Modifications
The repository follows a standard front-end structure <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

*   **`constants` File (`utils` folder)**:
    *   Defines the default model (Claude 3.5 Sonnet) and default providers (Anthropic) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   Contains a comprehensive list of available models for the dropdown. Each model entry includes its name (model ID), label for display, and provider, which determines the API key used by the backend <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
    *   Adding new models is straightforward: copy an existing record, specify the model ID, and provide a label <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. For Ollama models, installing Ollama and pulling the desired model is also necessary <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

*   **Front-End Changes**:
    *   **Main Chat Component**: A new state was added to represent the selected model, updated via the dropdown <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
    *   **Passing Model to Backend**: Due to limitations with the AI SDK's `useChat` hook, the model ID is embedded into the content of the user message itself <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. Bolt.new had a similar approach for file modifications <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
    *   **Base Chat Component**: This component iterates over the model list to create the dropdown menu <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
    *   **User Message Component**: Regular expressions are used to remove the model ID from the user messages before displaying them in the front end, preventing confusion for the LLM <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

*   **Back-End Changes**:
    *   **API Endpoint**: Serves as the entry point for LLM requests <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
    *   **`streamText` Function (`StreamText.ts`)**: This function performs the core work of retrieving the LLM response <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. It extracts the latest specified model from the user's messages and sanitizes messages to remove the model ID from the prompt sent to the LLM <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   **`getModel` Function**: Retrieves the specific LLM based on its provider and model ID <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
    *   **`apiKey` Typescript File**: Contains a switch statement to fetch the appropriate API key based on the provider (Anthropic, OpenAI, Groq). For Ollama, an empty string is returned as no API key is needed <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
    *   **Model Instance Functions**: Separate functions are used to obtain the model instance from each provider (e.g., Anthropic, OpenAI, Groq, Ollama) using the Vercel AI SDK <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
    *   **Extending Providers**: New providers like Together AI or Fireworks can be integrated by adding a new function, an API key environment variable, and updating the relevant switch statements, provided the provider is supported by the Vercel AI SDK <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

This customized version significantly boosts productivity by allowing users to choose any model and avoid usage limitations, potentially eliminating costs by leveraging local LLMs <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.