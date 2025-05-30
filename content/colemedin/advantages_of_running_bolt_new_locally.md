---
title: Advantages of running Bolt new locally
videoId: 3PFcAu_oU80
---

From: [[colemedin]] <br/> 

[[introduction_to_ottodev_and_the_boltnew_fork | Bolt New]] is a powerful, open-source Large Language Model (LLM) web development platform designed to create and deploy full-stack applications directly in the browser with AI assistance <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It significantly accelerates full-stack development <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, acting as a "fantastic coding assistant" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

While the official Bolt New platform is highly effective, it presents two main challenges:
*   **Limited Usage:** Users face restrictions similar to other AI tools like Claude or v0, often being forced to stop coding mid-application <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Fixed LLM Choice:** The platform exclusively uses Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, which, while good, limits options for users who prefer other models like GPT, or specialized local LLMs <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Solution: The Bolt New Fork (Bolt DIY)

By forking [[recent_updates_and_features_in_bolt_new_fork | Bolt New]] and running it locally, these limitations are overcome, offering enhanced flexibility and control <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This local version allows for extending the platform beyond a single LLM <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Key Advantages of Running Bolt New Locally

Running a forked version of Bolt New, often referred to as [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | Bolt DIY]], provides several significant benefits:

### 1. Unlimited Usage and Cost Savings
*   **No Usage Limits:** Running Bolt New locally removes usage restrictions, allowing for uninterrupted coding sessions <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Free to Use:** If using local models via Ollama, there are no API keys or costs involved, providing "unlimited credits" and "a lot of power" directly on your machine <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### 2. Flexible LLM Selection
*   **Multiple Model Options:** Users can select from a wide range of LLMs, including those from Anthropic, OpenAI, and Groq <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Local LLM Integration via Ollama:** The platform integrates with Ollama, enabling the use of numerous local models specifically fine-tuned for coding, such as Quen 2.5 Coder, Deepseek Coder, and Code Llama <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Literally any local model runnable with Ollama can be used <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Mid-Conversation Model Switching:** Models can be changed at any point during a chat session, allowing for dynamic adaptation <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Potential for Better Results:** More powerful local models, like Deepseek Coder 236B, can potentially yield better results than the default Claude 3.5 Sonnet used in the base Bolt New platform <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Fine-tuned Models:** The ability to use local models opens possibilities for fine-tuning them for specific tasks <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### 3. Privacy and Control
*   **Local Hosting:** The application runs entirely on the user's computer, ensuring privacy, especially when using local models <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### 4. Extensibility and Customization
*   **Open Source Advantage:** As [[recent_updates_and_features_in_bolt_new_fork | Bolt New]] is open source, its code can be downloaded and run locally <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Code Access:** Having access to the source code allows for extending the application, including adding new models or even entirely different LLM providers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   **Adding New Models:** New models can be easily added by defining them in the `constants` file within the `utils` folder, specifying the model ID, label, and provider <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   **Adding New Providers:** While more technical, new LLM providers (e.g., Together AI, Fireworks) can be integrated by adding corresponding functions and API key handling <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>, <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## How to Get Started with Bolt DIY

To run your own forked version of Bolt New:
1.  **Clone the Repository:** Obtain the custom URL for the forked version of Bolt New and clone it <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  **Install Packages:** Install all necessary packages <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
3.  **Configure Environment Variables:** Open the `.env.example` file and set API keys for any external models (e.g., GPT, Groq) you wish to use. No API key is needed for Ollama models <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
4.  **Run the Application:** Execute the `pnpm Run Dev` command to launch your local Bolt New instance <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
5.  **Browser Requirement:** Google Chrome Canary is required to run the application <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

[[technical_insights_on_modifying_bolt_new_frontend_and_backend | Technical modifications]] were made to integrate the model selection into the UI and handle model changes in the backend, including extracting the selected model from user messages and sanitizing prompts <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>, <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

Running [[using_bolt_diy_as_an_ai_coding_assistant | Bolt DIY as an AI coding assistant]] locally significantly boosts productivity, offers unparalleled model choice, and provides freedom from usage limitations, all while potentially costing nothing <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. [[community_involvement_in_bolt_diy_project | Community involvement in Bolt DIY project]] is encouraged, with opportunities for [[core_contributor_opportunities_for_the_bolt_new_fork_project | core contributor opportunities]] and suggestions for [[future_enhancements_and_highpriority_items_for_bolt_new | future enhancements and high-priority items]] for the Bolt New fork project. [[resources_and_tools_for_hosting_and_troubleshooting_bolt_diy | Resources and tools for hosting and troubleshooting Bolt DIY]] are available in the linked GitHub repository <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.