---
title: Recent updates and features in Bolt new fork
videoId: jm007pw2v1A
---

From: [[colemedin]] <br/> 

Two weeks ago, a fork of Bolt.new, a leading AI coding assistant, was released with the primary goal of enabling the use of any Large Language Model (LLM), particularly local ones, as the official version only supported a single model <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. What began as a simple release quickly garnered significant community interest, leading to the development of additional features and the vision to build the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Community Growth and Commitment

In just the last week, the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]] has received 20 pull requests, indicating strong community engagement and contributions <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The project maintainer is committed to long-term maintenance, aiming to build something larger for the community rather than just content for their channel <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

An upcoming development is the release of a Discourse community, which will serve as a central place for discussions, planning upcoming changes, and project maintenance, fostering the collaborative effort to build the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This community will also be part of a larger initiative for the channel's audience <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## [[core_contributor_opportunities_for_the_bolt_new_fork_project | Core Contributor]] Opportunities

Applications are now open to become a [[core_contributor_opportunities_for_the_bolt_new_fork_project | core contributor]] to the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. While anyone can contribute via pull requests, core contributors gain maintainer access to the repository, allowing them to approve and merge pull requests, and implement emergency bug fixes <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This initiative is crucial for scaling the project as it rapidly grows, with dozens of pull requests anticipated weekly <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Interested individuals with experience in generative AI and open-source projects are encouraged to apply via a Google Form link provided in the description <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Content and Tutorial Plans

Due to the project's rapid growth, regular content will be produced on the channel, including a tutorial on how to get the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]] up and running locally <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Weekly updates on the project are also being considered to ensure it continues to move quickly <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Recent Feature Additions

The [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]] has seen several significant additions recently, all contributing to its functionality and accessibility:

*   **Improved Main Bolt.new Prompt** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>: Kofi added a Chain of Thought prompting mechanism to the main Bolt.new prompt, encouraging the LLM to "think a little bit" before generating code, which enhances performance <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Deep Seek API Integration** <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>: Zenith integrated the Deep Seek API, providing direct support for Deep Seek Coder, a highly regarded model for coding projects <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Mistral API Integration** <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>: Aru added support for Mistral models via API integration, a popular choice among users <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **OpenAI-like API Integration** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>: Xery implemented a generic OpenAI-compatible API integration, allowing the use of various providers (e.g., Groq, Fireworks, Together) by simply changing the base URL <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This significantly expands [[integrating_various_models_with_bolt_new | model integration]] options at once <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   **Sync Files to a Local Folder** <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>: Mfer added a one-way sync feature, enabling users to push generated project files from the web container directly to a local folder on their computer, offering an alternative to downloading a zip file for immediate use in tools like VS Code <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Docker Containerization** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>: Aaron added Docker support, making it easier to set up and run the application locally. This will be the method demonstrated in future tutorials <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Publish Projects Directly to GitHub** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>: Gonzalo introduced the ability to publish generated projects directly to GitHub, streamlining the sharing and version control process <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Pending Pull Requests and Maintenance

The maintainer is actively reviewing and providing feedback on pending pull requests, ensuring that every contribution is considered, tested, and properly integrated into the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Specific recent fixes include:

*   **Llama 3.1 Model Fix** <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>: David implemented a fix that reduced the max tokens for Llama 3.1 models, preventing crashes when used with services like Groq <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Ollama API Base URL Support** <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>: Noob y DP addressed an issue where the Ollama API base URL wasn't working correctly unless hosted on a local machine, enabling use with Ollama instances on other machines <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
*   **Ollama Model Integration Enhancement** <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>: TK enhanced the Ollama model integration, including TypeScript improvements for cleaner code <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

## [[future_enhancements_and_highpriority_items_for_bolt_new | Future Enhancements and High-Priority Items]]

Several [[future_enhancements_and_highpriority_items_for_bolt_new | high-priority items]] are planned to significantly improve the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt new fork]]:

*   **Rewrite File/Project Issue Fix** <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>: A pull request has already been implemented to address a major issue where Bolt.new sometimes rewrites entire files or projects, and it's pending merger <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Better Prompting for Small/Large LLMs** <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>: A crucial goal is to improve prompting to ensure the code window consistently opens, especially for smaller LLMs (e.g., less than 30 or 70 billion parameters), making the project more accessible to users with limited hardware <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Image Attachments** <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>: Adding support for image attachments, a feature currently closed-source in the official Bolt.new version, is a desired enhancement <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Backend Agent Workflow** <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>: A highly anticipated feature is the implementation of agents in the backend. Instead of a single model request-response cycle, this would allow for multi-model interactions, Chain of Thought processes, self-reflection, and self-improvement before a response is given, opening up millions of possibilities <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Contributions using frameworks like LangChain, Swarm, LlamaIndex, or CrewAI are welcome <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

Additional planned features and [[integrating_various_models_with_bolt_new | LLM integrations]] include:

*   LM Studio, Together, Azure OpenAI, Hugging Face, and Perplexity integrations <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   Direct deployment to platforms like Vercel or Netlify <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   Ability to load projects into the app and potentially a two-way sync with local folders <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   Functionality to revert code to an earlier version <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   Prompt caching for improved speed <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   Option to enter API keys directly in the UI, eliminating the need for `.env` files <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   Having the LLM plan the project in a Markdown file, providing insight into its thought process and potentially leading to better results <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

The project is moving forward rapidly, with a focus on integrating these [[future_enhancements_and_highpriority_items_for_bolt_new | high-priority items]] soon <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.