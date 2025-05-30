---
title: Opensource AI coding assistants and community building
videoId: jm007pw2v1A
---

From: [[colemedin]] <br/> 

The development of an [[opensource_ai_coding_assistant_development | open-source AI coding assistant]] fork of Bolt.new has rapidly evolved from a personal project into a community-driven initiative aimed at creating the best possible [[open_source_ai_code_generators | open-source AI coding assistant]] <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>.

## Project Origin and Vision
Initially released two weeks prior, the fork's primary goal was to enable the use of any large language model, particularly local ones, with Bolt.new, as the official version supported only a single model <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. After its release, significant community contributions emerged, transforming the project into a collaborative effort <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>. The vision is now to build the leading [[open_source_ai_code_generators | open-source AI coding assistant]] <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>.

## Community Growth and Commitment
In just one week, the Bolt.new fork received 20 pull requests, demonstrating strong community engagement <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This rapid growth has led to a long-term commitment to maintain and build the project for the community <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Community Initiatives
To foster collaboration and sustained development, several initiatives are underway:
*   **Discourse Community** A Discourse community is being launched to provide a platform for discussion, planning upcoming changes, and maintaining the project <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This will be part of a larger community for the entire channel <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Core Contributor Applications** Applications are open for core contributors who will act as maintainers, with access to the repository to approve and merge pull requests, and make emergency bug fixes <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This is crucial for scaling the project as it expects dozens of pull requests weekly <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Regular Content and Tutorials** Consistent content on the project, including a tutorial on how to set it up locally using Docker, will be released to make it more accessible <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Weekly updates are also being considered to keep the project moving fast <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Recent Feature Additions
The Bolt.new fork has seen numerous valuable contributions:
*   **Improved Bolt.new Prompt** Incorporated Chain of Thought prompting to encourage LLMs to "think" before generating code, leading to slightly better performance <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. (Added by Kofi <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>)
*   **Deep Seek API Integration** Added support for Deep Seek API, which is highly regarded for coding projects, particularly Deep Seek Coder <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. (Added by Zenith <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>)
*   **Mistral API Integration** Integrated Mistral models due to popular demand <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. (Added by Aru <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>)
*   **OpenAI-like API Integration** This unique addition allows the use of various providers (e.g., Groq, Fireworks, Together) that offer OpenAI-compatible APIs, by simply changing the base URL <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. (Added by Xery <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>)
*   **File Sync to Local Folder** Enables one-way synchronization of the project structure and files from the web container to a local computer folder <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This is an alternative to downloading as a zip, facilitating direct opening in tools like VS Code <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. (Added by Mfer <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>)
*   **Docker Containerization** Facilitates easier setup and running of the application on a local machine <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. (Added by Aaron <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>)
*   **Direct Project Publishing to GitHub** Users can now publish generated projects directly to GitHub repositories <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. (Added by Gonzalo <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>)
*   **Ollama API Base URL Fix** Resolved an issue where the Olama API was only working when hosted on `localhost` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. (Added by Noob y DP <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>)
*   **Llama 3.1 Model Fix** A fix was implemented to reduce max tokens for Llama 3.1 models, preventing crashes when used with providers like Groq <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. (Added by David <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>)
*   **Ollama Model Integration Enhancement** Included TypeScript improvements for cleaner integration <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. (Added by TK <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>)

## Upcoming Changes and Priorities
The project has several high-priority and desirable future developments:
*   **Addressing File Overwriting** A pull request has already been submitted to fix a significant issue where Bolt.new often rewrites files or entire projects <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

### High-Priority Items
*   **Better Prompting for Model Compatibility** Improving prompting to ensure that the code window and web container consistently open, even when using smaller LLMs (e.g., under 30 or 70 billion parameters), which currently often behave like a regular chat widget <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. This is crucial for enabling [[effective_use_of_ai_coding_assistants | AI coding assistance]] with local models on various hardware configurations <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Image Attachments** Implementing image attachment functionality, which is currently a closed-source feature in the official Bolt.new version <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **[[open_source_ai_agent_development | Agentic Workflows]] in the Backend** This is considered the most exciting upcoming feature, allowing the system to run [[open_source_ai_agent_development | agents]] in the backend instead of just calling a single model <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This would enable complex agentic workflows, multi-model interactions, and processes like Chain of Thought, self-reflection, and self-improvement before a response is given <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Other Planned Integrations and Features
*   **Additional LLM Integrations** Future integrations include LM Studio, Together, Azure OpenAI, Hugging Face, and Perplexity <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Direct Deployment** The ability to deploy projects directly to platforms like Vercel or Netlify <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **Project Loading and Two-Way Sync** Features to load projects into the app, potentially with a two-way sync with local folders <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **Code Reversion** Ability to revert code to an earlier version if the AI makes errors <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Prompt Caching** For improved speed <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **UI API Key Entry** Allowing users to enter API keys directly in the UI, removing the need for `.env` files <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **LLM Project Planning in Markdown** The LLM would plan the project in a Markdown file as part of the file structure, providing insight into its thought process and potentially enhancing results <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

The project is continually evolving with community support, and the creator is committed to ongoing updates and active maintenance <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.