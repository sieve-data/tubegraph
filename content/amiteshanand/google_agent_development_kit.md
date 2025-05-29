---
title: Google Agent Development Kit
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The Google Agent Development Kit (ADK) is a flexible and modular framework designed for developing and deploying AI agents <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It can be used with popular LLMs and open-source tools, focusing on tight integration with the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. However, it can also be integrated with other LLMs, third-party tools, and APIs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## [[agent_to_agent_protocol | Agent to Agent Protocol]] (A2A Protocol)

Google announced the [[agent_to_agent_protocol | Agent to Agent Protocol]] on April 9, 2025, as an open protocol for [[introduction_to_ai_agents | AI agents]] to interact with each other and perform multiple tasks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This protocol enables client agents and remote agents to collaborate securely, manage state, improve user experience, and discover capabilities <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

The A2A protocol is an open standard for connecting [[introduction_to_ai_agents | agents]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. A high-level diagram shows a main agent using Vertex AI and Google-specific Gemini APIs, connecting through an ADK (an open-source agent building framework similar to QI and other frameworks) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. It also involves an MCP (Model Context Protocol) server for fetching APIs and enterprise applications <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Another main agent might use LLMs from different providers (like Navius) and other agent frameworks (e.g., QI or OpenAI agent SDK) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. These agents interact to perform tasks <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

While MCP focuses on tool and resource collaboration, the [[agent_to_agent_protocol | Agent to Agent Protocol]] is specifically for agent-to-agent collaboration, enabling dynamic multi-model communication between different [[introduction_to_ai_agents | agents]] without saving memory, resources, or tools <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. It is an open protocol, allowing the use of any framework or LLM <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Features and Capabilities

The Google ADK offers several features for [[building_ai_agents_with_google_adk | building AI agents]]:
*   **Multi-agent architecture:** Supports the creation of systems with multiple interacting agents <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Rich tool ecosystem:** Allows the addition of multiple tools, third-party libraries, and integrations <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Deployment ready:** Designed for easy deployment <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Built-in evaluation:** Includes functionalities for evaluating agent performance <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Types of Agents in ADK

In the Google ADK, an [[introduction_to_ai_agents | agent]] is a self-contained execution unit designed to act autonomously to achieve specific goals <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. [[introduction_to_ai_agents | Agents]] can perform tasks, interact with users, utilize external tools, and coordinate with other agents <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

The ADK framework extends a base agent into three core categories:

### LLM-based Agents
These [[introduction_to_ai_agents | agents]] use LLMs as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding how to proceed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. They can be used for specific answers or performing queries <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Workflow Agents
Workflow agents specialize in controlling the execution flow of other [[introduction_to_ai_agents | agents]] in predefined, deterministic patterns <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. They may or may not use LLMs in all cases <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Types of workflow agents include:
*   **[[sequential_agent_workflows | Sequential Agent]]**: Executes its sub-agents in the order they are specified in a list <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. For example, summarizing a webpage would require first getting the page content and then summarizing it sequentially <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. The final result is obtained after all sub-agents execute their tasks <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Parallel Agent**: Executes multiple sub-agents concurrently.
*   **Loop Agent**: Executes sub-agents repeatedly based on certain conditions.

### Custom Agents
Created by directly extending the base agent, custom agents allow implementing unique operational logic, specific control flow, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Installation

The Google ADK framework can be installed using `pip install google-adk` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Demo: Multi-Agent AI Trend Analyzer

A demo application showcased a multi-agent AI trend analyzer built with Google ADK <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This [[building_multiagent_systems_using_google_collab | multiagent system]] utilized a [[sequential_agent_workflows | sequential agent]] pipeline <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. The demo also integrated `light-llm`, which allows Google ADK to use other LLM providers by providing a prefix like `openai` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Tools Used in Demo
*   **Navius AI Studio:** Used for inference with models like LMAN demo ultra model by Nvidia and Meta Lama 3.18 instruct <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Navius was chosen as a provider for its cost-effectiveness <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
*   **XA:** A tool for adding search APIs and functionalities to AI apps, providing LLMs with better context from search results <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Table:** Another platform similar to XA, used for different purposes in the demo <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Firecrawl:** A tool for scraping data from various sites, offering features like scraping, crawling, mapping, extraction, and agent features <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### [[sequential_agent_workflows | Sequential Agent]] Pipeline

The demo's [[sequential_agent_workflows | sequential agent]] pipeline consisted of five agents orchestrated by a main "AI pipeline agent" <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>:
1.  **XA Agent:** Fetches the latest news from Twitter (now X) using XA <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
2.  **Table Agent:** Gathers benchmarks and specific data points related to various models from the "artificial analysis" website <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
3.  **Summary Agent:** Combines and formats the results from the XA and Table agents <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
4.  **Firecrawl Agent:** Scrapes content from the Navius AI website <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
5.  **Analysis Agent:** Analyzes the summarized data from the previous agents, provides insights, and considers scraped data <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This agent utilized Nvidia's Neotron Ultra model for its analysis <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Other agents in the pipeline were powered by Lama 3.18 <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Web UI Support

Google ADK also supports a web UI for running [[introduction_to_ai_agents | agents]] <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>. The web UI can be accessed locally, typically on `localhost:8000` <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. It allows users to select agents, input queries, and visualize the workflow of agent interactions through a flowchart <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. For example, a "multi-tool search agent" demo showed a root agent delegating tasks to an XA search agent, which then performed searches and provided answers <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.