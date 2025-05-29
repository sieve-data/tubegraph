---
title: Using ThirdParty Tools in AI Development
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

Developing AI applications often involves integrating various third-party tools and services to enhance functionality, provide context, and manage different aspects of the AI pipeline <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The [[building_ai_agents_with_google_adk | Google Agent Development Kit (ADK)]] is designed to be a flexible and modular framework that supports integration with popular Large Language Models (LLMs) and open-source tools, despite its focus on the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a><a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a><a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a><a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Integration Frameworks and Protocols

*   **[[building_ai_agents_with_google_adk | Google Agent Development Kit (ADK)]]**
    *   A flexible and modular framework for developing and deploying [[applications_and_implementation_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Allows for [[applications_and_implementation_of_ai_agents | multi-agent architecture]] and a rich tool ecosystem, enabling the addition of multiple tools, third-party libraries, and integrations <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a><a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   Installation is done via `pip install Google-ADK` <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a><a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   Supports [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | external tool and database integration]] with LLM providers like [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI]] (Nebius AI Studio) using Light LLM <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a><a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Offers a web UI for running agents, accessible via `ADK web` command <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a><a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

*   **Agent to Agent Protocol (A2A)**
    *   Announced by Google on April 9, 2025, as an open protocol for building agents that can interact and perform multiple tasks together <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a><a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a><a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Facilitates secure collaboration, state management, user experience, negotiation, and capability discovery between client and remote agents <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   Allows for dynamic multimodel communication between different agents without saving memory, resources, and tools <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a><a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

*   **Model Context Protocol (MCP)**
    *   Distinguished from A2A protocol, MCP focuses on tool and resource collaboration <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a><a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Specific Third-Party Tools Used

Several tools are utilized for different purposes within an [[applications_and_implementation_of_ai_agents | AI agent]] pipeline:

*   **[[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI Studio (Nebius AI)]]**
    *   Used for inference, providing LLM models <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
    *   Models include LMAN demo ultra model by Nvidia <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, Meta Lama 3.18 instru <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, and Nvidia Lama 3.1 253B <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
    *   Integrated using Light LLM by setting a specific API base and key <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

*   **XA (formerly XAR)**
    *   A tool that enables adding search APIs and functionalities to [[generating_ai_apps_using_boltdiy | AI apps]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a><a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
    *   Helps LLMs gain better context from search results <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
    *   Example use: Fetching the latest news from Twitter/X <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a><a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

*   **DEI Table (formerly `dei` in the context of the demo)**
    *   A platform similar to XA, used for different purposes in the demo <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a><a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   Example use: Getting benchmarks and specific data points from artificial analysis websites <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a><a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

*   **Firecrawl**
    *   A tool for scraping data from various websites <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a><a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
    *   Features include scraping, crawling, mapping, extraction, agent features, and LLM.txt features <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a><a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   Example use: Scraping the [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI]] website for content <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a><a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

*   **Light LLM**
    *   A library that allows the use of various LLM providers (e.g., [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI]], OpenAI, Anthropic) by providing a unified interface, often with an `openai` prefix <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a><a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a><a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a><a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
    *   Enables maximum control over costs and privacy or offline use cases by integrating open-source models run locally <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a><a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

*   **Python-dotenv**
    *   Used for managing API keys and other environment variables <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

## Example [[applications_and_implementation_of_ai_agents | AI Agent]] Pipeline with Third-Party Tools

A sequential agent pipeline using [[building_ai_agents_with_google_adk | Google ADK]] can integrate multiple tools to achieve a complex task, such as a multi-[[applications_and_implementation_of_ai_agents | agent]] [[ai_tools_for_content_creation | AI]] trend analyzer <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

The pipeline can involve:
1.  **XA Agent:** Fetches latest news about [[ai_tools_for_content_creation | AI]] advancements from X (Twitter) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a><a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
2.  **DEI Table Agent:** Gathers benchmarks and data from artificial analysis websites <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a><a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
3.  **Summary Agent:** Combines and formats results from the XA and DEI agents <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a><a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
4.  **Firecrawl Agent:** Scrapes content from the [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI]] website <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a><a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
5.  **Analysis Agent:** Utilizes a powerful LLM (e.g., Nvidia Neotron Ultra model or Lama 3.1 253B) to analyze the combined summary and scraped data, providing insights <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a><a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a><a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This agent is powered by models from [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | Navius AI]] Studio <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

This sequential pipeline is orchestrated by a main "pipeline" agent within [[building_ai_agents_with_google_adk | Google ADK]] <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a><a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.