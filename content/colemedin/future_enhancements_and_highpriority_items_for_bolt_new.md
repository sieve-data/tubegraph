---
title: Future enhancements and highpriority items for Bolt new
videoId: jm007pw2v1A
---

From: [[colemedin]] <br/> 

This section outlines upcoming changes and high-priority items for the [[bolt_new_fork_introduction_and_its_community_engagement | Bolt. new Fork]] project, aiming to make it a more robust and capable open-source AI coding assistant <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## High-Priority Items

Several key features are considered top priority for immediate implementation, as they would significantly improve the project <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>:

*   **Addressing File Rewriting Issues**
    *   A pull request has already been implemented to fix a major issue where Bolt tends to rewrite files or even entire projects <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This change is currently pending a merge <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Improved Prompting for LLMs**
    *   Better prompting is needed to ensure the code window consistently starts, especially when using smaller Large Language Models (LLMs) (e.g., those smaller than 30 billion or 70 billion parameters) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Currently, smaller LLMs may act like a regular chat widget without opening the web container, which is a significant problem for users with hardware limitations <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Image Attachments**
    *   The [[introduction_of_bolt_diy_as_the_official_opensource_version_of_bolt_new | open-source version of Bolt. new]] does not yet implement image attachments, which is a feature in the official closed-source version <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. This is a desired addition <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Backend Agent Integration**
    *   A highly anticipated feature is the ability to run agents in the backend, as opposed to simply calling a single model <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This would allow for agentic workflows with multiple models interacting, or processes like Chain of Thought, self-reflection, and self-improvement before a response is given <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Contributions using frameworks like LangChain, Swarm, LlamaIndex, or CrewAI, or entirely custom solutions, are welcome <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Additional LLM Integrations

Further integrations with other LLMs are planned <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>:

*   LM Studio <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>
*   Together <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>
*   Azure OpenAI <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>
*   Hugging Face <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>
*   Perplexity <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>
*   The existing "OpenAI-like API integration" may also apply to some of these services <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

## Other Desired Features

Other features that would enhance the project's usability include <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>:

*   **Direct Deployment**
    *   The ability to deploy projects directly to platforms like Vercel or Netlify <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **Project Loading and Syncing**
    *   Loading projects into the application <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
    *   Implementing a two-way sync with local folders <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **Code Reversion**
    *   The ability to revert code to an earlier version if the AI makes an error <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Prompt Caching**
    *   For improved speed <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **UI for API Keys**
    *   Allowing users to enter API keys directly within the UI, eliminating the need to create an `.env` file <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   **LLM Project Planning in Markdown**
    *   Having the LLM plan the project in a Markdown file that becomes part of the file structure <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This would provide insight into the AI's thought process and could lead to better results through a Chain of Thought enhancement <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.