---
title: Open Source AI Code Generators
videoId: p1YvKuRfEhg
---

From: [[colemedin]] <br/> 

Recently, a popular AI code generator called Bolt.new has seen a community-driven fork emerge, focusing on key improvements and [[opensource_ai_coding_assistants_and_community_building|community building]] around its development <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This project highlights the [[benefits_of_opensourcing_ai_coding_assistants|benefits of opensourcing AI coding assistants]] by allowing users to choose their Large Language Model (LLM) and engage in collaborative development <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Enhancements to the Bolt.new Fork

The primary motivation for this fork was to address limitations in the original Bolt.new, specifically its restriction to a single LLM <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The forked version allows users to select their preferred LLM, including local LLMs via tools like Ollama, enabling free and unlimited code generation <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

The project has fostered significant community engagement, with users providing suggestions, feedback, and direct contributions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This collaborative approach aims to build a truly incredible tool, potentially evolving into its own distinct entity beyond just a fork <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It also serves as an excellent platform for learning how to leverage AI for building new things <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Implemented Features

The following features have been implemented in the fork, many of them driven by community requests and contributions:

*   **Selectable LLM Provider** Users can now choose their LLM provider, such as OpenAI or OpenRouter, a feature not available in the official Bolt.new version <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This includes integration with OpenRouter to access its wide range of models <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a> and Google Gemini (Flash and Pro versions) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Dynamic Ollama Model List** Previously, Ollama models were hardcoded, but now the list of available models is dynamically generated based on what a user has pulled locally via Ollama, preventing selection errors <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Model Filtering by Provider** The model dropdown now allows filtering by provider, making it easier to navigate the extensive list of available models <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Download Generated Code** A highly requested feature, users can now download the generated code as a zip file, eliminating the need to manually copy and paste each file <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

> [!NOTE] Demonstration of Features
> During a demonstration, the process of generating a to-do application was shown, including file creation, running npm commands, and previewing the application within the browser <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The ability to download the entire project as a `.zip` file was also highlighted <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Future Work and Requested Additions

The project maintains a public list of requested features, encouraging continued [[opensource_ai_coding_assistant_development|opensource AI coding assistant development]] and community contributions <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Future planned or requested features include:

*   **LM Studio Integration** To support users who prefer LM Studio over Ollama for local models <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **DeepSeek API Integration** To leverage powerful DeepSeek Coder models, particularly the 236 billion parameter version <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Improved Prompting for Smaller Models** Addressing issues where smaller LLMs might not always generate code in the intended web container format <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. A workaround currently exists where stopping and re-prompting can help trigger the web container <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Image Attachment to Prompts** Adding the ability to include images in prompts, a feature present in the paid version of Bolt.new but not its open-source counterpart <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Backend Agent Integration** A significant potential enhancement involves running agents in the backend, enabling multiple LLMs to work together for more robust code generation <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This could utilize frameworks like LangGraph, LangChain, or OpenAI Swarm, representing a potential "game-changer" for [[open_source_ai_agent_development|open source AI agent development]] in code generation <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   **Direct GitHub Publishing** Allowing users to publish projects directly to GitHub, similar to the paid Bolt.new feature <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Loading Local Projects** The ability to import local projects (e.g., from VS Code) into the Bolt.new environment for continued development <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **General Prompting Improvements** Enhancing the core Bolt.new prompts to yield better results, especially regarding UI/UX quality, as the open-source version sometimes lags behind the paid one in this aspect <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

> [!INFO] Project Philosophy
> The project emphasizes its community-driven nature, aiming to be a shared effort rather than a monetized product <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. The core goal is collaborative learning about AI and building amazing things together <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.