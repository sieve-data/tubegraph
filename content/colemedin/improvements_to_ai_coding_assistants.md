---
title: Improvements to AI Coding Assistants
videoId: p1YvKuRfEhg
---

From: [[colemedin]] <br/> 

Recently, a user created a fork of Bolt.new, a popular [[ai_coding_assistants | AI code generator]], to introduce several needed improvements <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The primary enhancement allows users to choose the Large Language Model (LLM) for code generation, including the use of local LLMs via tools like Ollama, enabling free and unlimited code generation <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

The initial video detailing this Bolt.new fork received significant engagement, with many users providing suggestions, feedback, and even contributions, fostering a growing community around the project <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The project aims to become a truly incredible tool, potentially evolving beyond just a Bolt.new fork <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It also serves as an excellent way to learn how to leverage [[ai_coding_assistants | AI]] for building innovative applications <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Implemented Features and Contributions

The GitHub repository for this Bolt.new fork is actively maintained and ahead of the main open-source version due to continuous community contributions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Key requested features that have been implemented include:

*   **OpenRouter Integration**
    *   Integration with OpenRouter's vast range of models was a highly requested feature and has been added <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Users can select OpenRouter as a provider and choose from available models <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **Gemini Support**
    *   Support for Gemini 1.5 Flash and Pro models has been integrated. This contribution was made by Brijesh <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Dynamic Ollama Models**
    *   Originally, a hardcoded list of Ollama models was available. Now, the list of Ollama models dynamically populates based on which models a user has actually downloaded locally via Ollama <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This improvement prevents users from selecting models they don't have installed, resolving previous confusion <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This feature was contributed by Dmitri <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Provider Filtering**
    *   Users can now filter models by provider, making it easier to navigate the extensive list of available models <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This enhancement was contributed by Jason <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Code Download Functionality**
    *   One of the most requested features was the ability to download the generated code as a ZIP file <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This eliminates the need to manually copy and paste individual files from the web container <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This functionality was contributed by Mikhail <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Demonstration

The Bolt.new fork's UI now features dropdowns for selecting the LLM provider and model, which are not present in the official Bolt.new version <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Users can type in a prompt or select from predefined templates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The application generates files, runs npm commands, and provides a live preview of the app <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. For example, a simple to-do app can be generated in seconds, with full access to the source code and an interactive preview environment similar to Node.js running in the browser <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The ability to download generated code as a `.zip` file, complete with nested folder structures, is now available <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Future Work and Community Contributions

There is an extensive list of future improvements requested by the community. As the developer is busy with content creation, community help is crucial for implementing these features <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Requested additions include:

*   **LM Studio Integration**: Many users prefer LM Studio over Ollama for local models, necessitating an integration <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Deepseek API Integration**: The Deepseek Coder models, particularly the 36 billion parameter one, are highly regarded for coding, making their API integration desirable <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Improved Prompting for Smaller Models**: Smaller LLMs sometimes struggle with the default Bolt.new prompting, leading to a chat interface instead of the full web container and code generation <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. While a workaround exists (sending a prompt, stopping generation, opening the code container, and re-prompting) <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, improving the prompting for these models is a needed enhancement <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This relates to [[issues_with_current_ai_coding_assistants | issues with current AI coding assistants]] and [[limitations_of_current_ai_coding_assistants | limitations of current AI coding assistants]].
*   **Image Attachment to Prompts**: The official paid version of Bolt.new allows attaching images to prompts, a feature currently missing from the open-source version <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Backend Agent Execution**: A significant proposed feature is the ability to run agents in the backend, allowing multiple LLMs to collaborate on code generation, potentially using frameworks like LangGraph, LangChain, or OpenAI Swarm <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. This would be a "game-changer" for [[ai_coding_assistants | AI code generators]] <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
*   **Direct GitHub Publishing**: The ability to publish projects directly to GitHub, similar to the paid Bolt.new version <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Loading Local Projects**: Allowing users to load existing local projects (e.g., from VS Code) into Bolt.new for continued development, rather than starting from scratch <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **General Prompting Improvements**: Further improvements to the main Bolt.new prompt are needed to yield better results, especially regarding UI aesthetics and functionality <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

This project is being developed as a community effort, with no plans for monetization, focusing instead on collaborative learning and building an amazing tool together <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. This aligns with the concept of [[benefits_of_opensourcing_ai_coding_assistants | benefits of opensourcing AI coding assistants]].