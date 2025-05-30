---
title: Bolt new fork introduction and its community engagement
videoId: jm007pw2v1A
---

From: [[colemedin]] <br/> 

Two weeks prior, a fork of Bolt.new, a prominent AI coding assistant, was released <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The initial goal was to enable the use of any Large Language Model (LLM), particularly local ones, with Bolt.new, as the official version only supported a single model <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The creator's intent was simply to release a "cool and practical" project <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Community Growth and Vision

After its release, many users began contributing additional features, leading to the rapid formation of a community within about 10 days <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The collective vision is to build the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. The project maintainer has committed to long-term maintenance and building the project for the community, aiming for it to be more than just content for their channel <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Engagement Metrics
*   **Pull Requests:** In just one week, 20 pull requests were submitted to the Bolt.new fork, indicating strong community engagement <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Upcoming Community Initiatives
*   **Discourse Community:** A Discourse community is being launched to provide a dedicated space for discussing the project, planning future changes, and ensuring the continued development of the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This community will also be part of a larger channel community <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **[[core_contributor_opportunities_for_the_bolt_new_fork_project | Core Contributor Opportunities]]**: Applications are open for core contributors who will act as maintainers, with access to the repository to approve and merge pull requests, and make emergency bug fixes <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This is crucial as the project is growing rapidly and requires more help to manage dozens of weekly pull requests <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Experienced developers, especially those with generative AI and open-source project experience, are encouraged to apply <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Regular Content & Tutorials:** The project's significant growth will lead to regular content on the creator's channel, including a tutorial on how to set up and run the fork locally <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Weekly updates are also being considered to maintain the project's fast pace <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## [[recent_updates_and_features_in_bolt_new_fork | Recent Additions and Contributions]]

The project's GitHub repository lists all added and upcoming features <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Key recent additions include:

*   **Improved Main Bolt.new Prompt:** Implemented Chain of Thought prompting to enhance LLM performance, particularly for the open-source version of Bolt <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Contributed by Kofi <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Deep Seek API Integration:** Added support for Deep Seek API, useful for coding projects, contributed by Zenith <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Mistral API Integration:** Mistral models were integrated due to popular demand, contributed by Aru <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **OpenAI-like API Integration:** This generic integration allows connection to various providers (e.g., Groq, Fireworks, Together) that offer OpenAI-compatible APIs, significantly expanding model compatibility by allowing users to change the base URL <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Contributed by Xery <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **Sync Files to Local Folder:** Enables a one-way sync to push created project files from the web container to a local computer folder, providing an alternative to downloading as a zip file <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Contributed by mfer <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Docker Containerization:** Allows the application to be containerized with Docker, simplifying the setup process on a local machine for future tutorials <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Contributed by Aaron <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Publish Projects Directly to GitHub:** Users can now directly publish generated projects to GitHub repositories, enhancing project sharing and collaboration <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Contributed by Gonzalo <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Fix for Llama 3.1 Models:** Addressed an issue where Llama 3.1 models were crashing by slightly reducing max tokens <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Contributed by David <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **Ollama API Base URL Support:** Resolved an issue where Ollama only worked with localhost hosting, now supporting Ollama hosted on other machines <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Contributed by Noob y DP <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## [[future_enhancements_and_highpriority_items_for_bolt_new | Upcoming Changes and High-Priority Items]]

Several key enhancements are planned, with some identified as high-priority:

### High Priority
*   **Addressing File Rewriting:** A pull request has already been submitted to address a significant issue where Bolt tends to rewrite files or entire projects <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Better Prompting for Small/Large LLMs:** A critical challenge is ensuring the code window starts correctly for all LLMs, especially smaller ones. Currently, smaller models may act as regular chat widgets without opening the web container, hindering the goal of using any LLM, including local ones compatible with various hardware <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Image Attachment Implementation:** The open-source version currently lacks image attachment functionality, which is part of the official, closed-source Bolt.new <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Agentic Back-end Workflow:** The most exciting upcoming feature is the ability to run agents in the back-end instead of just calling a single model <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This would allow for complex workflows involving multiple models, Chain of Thought processes, self-reflection, and self-improvement before a response is generated <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Contributions using frameworks like LangChain, Swarm, LlamaIndex, or CrewAI are highly encouraged <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

### Other Planned Features
*   **Additional LLM Integrations:** Further integrations with LLMs such as LM Studio, Together, Azure OpenAI, Hugging Face, and Perplexity are planned <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Direct Deployment:** Ability to deploy projects directly to platforms like Vercel or Netlify <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **Project Loading:** Functionality to load existing projects into the application, potentially with a two-way sync to a local folder <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **Code Reversion:** Ability to revert code to an earlier version if errors occur <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Prompt Caching:** For improved speed <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **UI API Key Entry:** Allowing users to enter API keys directly in the UI, removing the need for `.env` files <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **LLM Project Planning in Markdown:** Having the LLM plan the project in a markdown file that becomes part of the file structure, providing insight into its thought process and potentially leading to better results <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.