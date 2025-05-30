---
title: Introduction to oTToDev and the Boltnew fork
videoId: _YzTntvUWN4
---

From: [[colemedin]] <br/> 

oTToDev is an AI coding assistant that originated as a fork of Bolt.new [00:00:41]. The project was initiated approximately a month prior to the stream to incorporate the functionality of chatting with various large language models (LLMs), including local models via Ollama [00:01:26].

Within its initial weeks, a significant community formed around oTToDev, propelling its development beyond the scope of its original creator [00:01:35].

## Community and Development Engagement

A primary goal for oTToDev is to foster and grow its community [00:01:45]. This involves establishing dedicated platforms for organized communication and collaboration.

### The Think Tank: A Discourse Community

The official Discourse community, named "The Think Tank," has been launched to serve as the central hub for oTToDev organization and community interaction [00:05:17].

*   **Access:** The community is accessible at thinktank.automator.ai [00:05:28] and is free to use [00:05:48].
*   **Purpose:** It aims to provide a structured environment for discussions, moving away from fragmented conversations in YouTube comments, GitHub issues, and pull requests [00:06:01].
*   **Platform Choice:** Discourse was selected over alternatives like Discord or Slack due to its professional interface, native support for plugins (including AI integration for conversation summarization), and superior organizational and search capabilities crucial for long-term project management and [[Troubleshooting and debugging oTToDev | troubleshooting]] [00:06:09].
*   **Engagement Incentive:** To encourage early adoption, a giveaway is being held: users who create an account and make a non-spam post by Tuesday, November 12th, will be entered to win a $200 Amazon gift card [00:08:06].

### Automator.ai: A Broader Vision

The oTToDev Discourse community is part of a larger, overarching project called Automator.ai [00:10:00]. This platform is designed to be an expansive extension of the creator's YouTube channel, focusing on in-depth AI education [00:10:32].

Automator.ai aims to fill gaps in the learning process that are difficult to address via typical YouTube video formats, such as providing content that leads to production-ready applications or caters to highly specific use cases [00:11:57].

Key areas of depth Automator.ai will provide:
*   **Community and Networking:** A more robust environment for interaction than YouTube comments [00:12:33].
*   **Production-Ready Content:** Advanced courses for building production-ready AI applications [00:13:39].
*   **Specific Use Cases:** Resources for implementing generative AI solutions for niche business problems [00:14:14].
*   **Latest AI Tools:** A platform to stay updated on new and important AI tools like Cursor, which may not fit into the regular content calendar [00:15:05].

The platform emphasizes providing significant value for free while offering optional investment opportunities, striving to avoid the impression of excessive monetization [00:15:45]. It also seeks to connect developers with business owners needing AI implementation [00:16:22].

A notable future component of Automator.ai is the [[Bolt DIYs roadmap and future features | AI Agent Studio]] [00:20:47]. This will be a space to test, learn, and collaborate on various AI agents, aiming to become a comprehensive library of industry solutions [00:21:25]. This includes the possibility of hosting oTToDev itself as an agent on the platform [00:21:48].

## oTToDev Updates and Future Goals

### Recent Enhancements

[[Recent updates and features in Bolt new fork | Recent updates and features in oTToDev]] include:
*   **Increased Maintainer Support:** A team of talented individuals is being formed to help manage the project's growing demands, including handling issues and pull requests [00:26:00]. This collaboration is already yielding results [00:26:36].
*   **Application Containerization:** Aaron implemented Docker containerization, simplifying installation [00:27:37]. The Discourse community will also serve as a resource for [[Troubleshooting and debugging oTToDev | troubleshooting Docker-related issues]] [00:27:57].
*   **UI API Key Entry:** A significant feature enabling users to enter API keys directly within the UI, eliminating the need to modify files and facilitating self-hosting [00:28:44]. This is crucial for future deployment on the [[Bolt DIYs roadmap and future features | Agent Studio]] [00:29:27].
*   **xAI Grok Beta Integration:** Grok is now integrated as a usable model within oTToDev [00:29:36].
*   **Provider Choice Respect:** A fix was implemented to ensure the application correctly uses the selected provider and model, preventing defaults to other providers with similar model names [00:30:18].
*   **Ollama Context Setting:** Automatic context setting for Ollama models addresses an issue where they often default to a limited 2,000-token context, which prevented code generation in the web container [00:30:50].
*   **Integrated Terminal:** A forthcoming major update will add a terminal directly into the interface, allowing users to see commands run by oTToDev during application creation [00:31:31]. This is expected to significantly reduce hallucinations, especially with local LLMs, by providing visibility into execution errors [00:31:43]. This feature was originally part of the commercial Bolt.new version but not the open-source one [00:32:01].

### Short-Term and Long-Term Goals

The project aims to establish a clear [[Bolt DIYs roadmap and future features | roadmap]] for future development, potentially using tools like Roadmap.sh, to manage short-term and long-term goals [00:34:01].

High-priority features include:
*   **Local Project Interaction:** The ability to load and interact with local projects, possibly with Git integration or VS Code-style IDE integration [00:35:17].
*   **Agent Integration:** Incorporating AI agents into the backend for improved code generation, potentially as optional extensions [00:48:47].

Long-term visions involve creating an "extension marketplace" where developers can implement and share extensions for oTToDev without directly modifying the core codebase [00:36:11]. This would allow for features like agent-based backend code generation to be toggled on or off by users. The goal is to facilitate both large-scale features and smaller fixes to ensure a stable and powerful application [00:37:40].

There is also a desire to improve prompting strategies, creating model-specific system prompts that yield optimal results for different LLMs, such as DeepSeek Coder or Qwen 2.5 [00:59:32].

The community is encouraged to contribute through coding via pull requests and, in the future, through crowdfunding to support developers tackling high-priority features [00:45:12].