---
title: Forking open source platforms for custom modifications
videoId: 3PFcAu_oU80
---

From: [[colemedin]] <br/> 

[[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] is a powerful and [[open_source_development | open source]] LLM web development platform that allows users to create and deploy full-stack applications directly in the browser with the assistance of AI <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is considered a significant advancement over tools like Claude or Vercel, and greatly speeds up full-stack development <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While not perfect, it functions as an excellent coding assistant for starting projects <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Limitations of Original Bolt.new

Despite its advantages, the original [[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] platform has two primary drawbacks <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:
1.  **Limited Usage**: Similar to other platforms, it imposes usage limitations, which can interrupt development workflow <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Fixed LLM Choice**: Users are restricted to using Claude 3.5 Sonnet as the sole Large Language Model (LLM), preventing the use of other models like GPT, or locally fine-tuned LLMs for coding <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## The Solution: Forking and Customizing Bolt.new

To address these limitations, a solution was developed by forking the [[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] platform, running it locally, and extending its functionality <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This approach eliminates usage limits and allows for the selection of various LLMs <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

Since [[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] is [[open_source_development | open source]], its code is available on GitHub, enabling users to download, run, and modify it themselves <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This accessibility allows for the extension of the application by leveraging its source code <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Demonstration of the Forked Version

The forked version of [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt.new]] presents a key difference: a dropdown menu for selecting the desired LLM <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Available models include those from <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>:
*   Anthropic
*   OpenAI
*   Groq
*   [[integration_with_various_platforms | Ollama]] (for local models like Code Llama, Deepseek Coder, Quen 2.5 Coder, etc.) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>

This allows for the use of models like GPT-4o or local Ollama models on a private localhost setup <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Users can switch models mid-conversation <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Performance with Different Models
While larger models generally perform well, smaller models (e.g., 7 billion parameters) may not always integrate seamlessly with the web container, occasionally failing to spin it up <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This is because the underlying prompts for [[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] are extensive, which smaller models may struggle to handle <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. However, even when the web container preview is imperfect, the generated code often functions correctly when tested externally (e.g., in a JSFiddle) <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. More powerful local models, such as Deepseek Coder 236b, can potentially yield better results than the default Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The ability to fine-tune these models further expands possibilities <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## How to Run the Forked Version

The forked version's code is available on GitHub, allowing users to download and run it <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Using local models with [[integration_with_various_platforms | Ollama]] means no payment for credits and unlimited usage <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Installation Steps
1.  **Clone the Repository**: Clone the custom fork's URL <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  **Install Packages**: Install all necessary packages <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
3.  **Set Environment Variables**: Open the `.env.example` file and configure API keys for specific models you intend to use (e.g., GPT, Groq). No API key is needed for [[integration_with_various_platforms | Ollama]] models as they run locally <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
4.  **Run Development Server**: Execute `pnpm run dev` to start the application <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### Prerequisites
*   **Browser**: Google Chrome Canary is required to run the application <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## [[Technical insights on modifying Bolt new frontend and backend | Technical Insights on Modifications]]

The repository structure is a standard frontend application, familiar to those with experience in Next.js, Vue, or React <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Model Definitions
The `constants.ts` file within the `utils` folder defines the default model (Claude 3.5 Sonnet) and lists all available LLMs for the dropdown menu <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Each model is an object with `name` (model ID), `label` (display name), and `provider` <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. The `provider` determines which API key the backend fetches for requests <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Adding new models is straightforward: copy an existing record, update the model ID (e.g., from [[integration_with_various_platforms | Ollama]]), and provide a new label <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. For [[integration_with_various_platforms | Ollama]] models, users need to install [[integration_with_various_platforms | Ollama]] and pull the specific model via a terminal command <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

It's important to note that some smaller models may not work optimally with [[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] due to context limitations <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Frontend Modifications
Modifications primarily focused on the chat component to integrate model selection <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>:
*   **Model State**: A new state was added in the main chat component to represent the selected model, updating from the dropdown <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **Passing Model to Backend**: The model is embedded into the content of the user's message itself (similar to how file modifications are passed in the original Bolt.new) and later removed before display <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Dropdown Creation**: The `base track` component loops over the model list to create the dropdown <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Message Sanitization**: The `user message` component uses a regular expression to remove the model information from user messages displayed in the frontend <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Backend Modifications
The API endpoint handles responses from the LLM, primarily through the `streamText` function <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Model Extraction**: Within `streamText`, the latest specified model is extracted from the messages, allowing for model changes mid-conversation <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Messages are also sanitized to remove model IDs from the prompt <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **`getModel` Function**: This function retrieves the model based on its provider and ID <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **`getApiKey` Function**: In the `apiKey.ts` file, a switch statement retrieves the correct API key based on the provider (Anthropic, OpenAI, Groq). For local models like [[integration_with_various_platforms | Ollama]], an empty string is returned as no API key is needed <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **`getModelInstance` Function**: Another switch statement, based on the provider, passes the API key and specific model to different functions, each working with a specific provider from the Vercel AI SDK to retrieve the model instance <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

### Extending to New Providers
To add a new provider (e.g., Together AI, Fireworks), a new function, API key in the environment file, and updates to both switch statements (in `getApiKey` and `getModelInstance`) are required <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. The Vercel AI SDK documentation lists supported providers like OpenAI, Anthropic, Groq, Perplexity, Fireworks, and [[integration_with_various_platforms | Ollama]] <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

This project offers significant value by allowing users to create full-stack applications with unlimited usage and a wide choice of LLMs, including local ones, enhancing [[Community Contributions to Software Development | productivity]] while coding <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.