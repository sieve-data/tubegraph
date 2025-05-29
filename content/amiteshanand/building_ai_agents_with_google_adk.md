---
title: Building AI agents with Google ADK
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The [[Agent Development Kit introduction and usage | Google Agent Development Kit (ADK)]] is a flexible and modular framework designed for developing and deploying AI agents <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. It supports popular Large Language Models (LLMs) and open-source tools, focusing on tight integration with the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The ADK can be installed using `pip install Google ADK` <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Key Features of Google ADK
The [[Features of Google Agent Development Kit | Google ADK]] offers several features including:
*   Multi-agent architecture <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
*   Rich tool ecosystem, allowing the addition of multiple tools, third-party libraries, and integrations with frameworks like LangChain <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>
*   Deployment readiness <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>
*   Built-in evaluation capabilities <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>

## Understanding AI Agents in ADK
In the context of the [[Understanding AI Agents | Agent Development Kit]], an agent is defined as a self-contained execution unit designed to autonomously achieve specific goals <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

The ADK categorizes agents into three core types <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>:
1.  **LLM-based Agents:** These agents utilize LLMs as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding how to proceed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. They are suitable for tasks requiring specific answers or queries <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
2.  **Workflow Agents:** These agents specialize in controlling the execution flow of agents in predefined, deterministic patterns <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. They include:
    *   **Sequential Agents:** Execute sub-agents in a specified order <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. An example is summarizing a webpage, where content must be retrieved before it can be summarized <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   **Parallel Agents:** Execute multiple agents simultaneously <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
    *   **Loop Agents:** Execute agents in a loop until a condition is met <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    Workflow agents may or may not use an LLM <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
3.  **Custom Agents:** These agents are created by directly extending the base agent and allow for unique operational logic, specific control flow, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Google Agent-to-Agent (A2A) Protocol
Google announced its [[Agent to Agent protocol by Google | Agent-to-Agent (A2A) protocol]] on April 9, 2025 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It is an open protocol designed to enable secure collaboration between AI agents, allowing them to interact and perform multiple tasks together <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The A2A protocol facilitates:
*   Secure collaboration <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   State management <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   User experience management <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   Negotiation and capability discovery <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

A high-level diagram of the A2A protocol involves a main agent (Agent One) with local agents utilizing Google-specific tools like Vertex AI and Gemini APIs. This agent interacts with a [[Agent Development Kit introduction and usage | Google ADK]], an open-source agent building framework. An MCP (Model Context Protocol) server acts as an intermediary for fetching APIs and enterprise applications. A second main agent (Agent Two) with its own local agents might use LLMs from different providers (e.g., Navius) and other agent frameworks like LangChain or [[Building AI Agents with OpenAI Agent SDK | OpenAI Agent SDK]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Both Agent One and Agent Two interact to perform tasks <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

The A2A protocol is distinct from MCP; while MCP focuses on tool and resource collaboration, A2A is specifically for agent-to-agent collaboration, enabling dynamic multi-model communication between different agents without saving memory, resources, or tools <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. It's an open standard that allows the use of any framework or LLM <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Building a Sequential Agent Demo with Google ADK
A full-fledged [[Sequential agent demo with Google ADK | agent demo]] was built using [[Google Agent Development Kit introduction and usage | Google ADK]] to create a multi-agent AI trend analyzer <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This pipeline utilized a [[Setting up a sequential agent workflow using Google ADK | sequential agent workflow]], coordinating five individual agents <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### Tools and Models Used
*   **Inference Studio:** Navius AI Studio <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, which provided:
    *   LMAN Demo Ultra model by Nvidia <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
    *   Meta Llama 3.1 8B Instruct model <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Search APIs:**
    *   XA: Adds search APIs and functionalities to AI apps for better LLM context <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   DEI/Table: Similar to XA, used for different purposes in the demo <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Web Scraping:** Firecrawl: Scraps data from various sites, with features like crawling, mapping, extraction, and agent features <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The system also leveraged [[Integrating multiple AI tools with Google ADK | Light LLM]] to support various LLM providers beyond Google's ecosystem <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

### Sequential Agent Pipeline
The demo consisted of a chain of five agents working in sequence:
1.  **XA Agent:** Fetches the latest news and updates from Twitter (X.com) related to AI advancements <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
2.  **Table Agent (DEI):** Gathers benchmark data and specific data points related to various models from the Artificial Analysis website <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
3.  **Summary Agent:** Combines and formats the results obtained from the XA and Table agents into a coherent summary <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This agent is powered by Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
4.  **Firecrawl Agent:** Scrapes content from the Navius AI website <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This agent also uses Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
5.  **Analysis Agent:** Uses the Nvidia Neotron Ultra model to analyze the combined summary from Agent 3 and the scraped data from Agent 4, providing insights and recommendations <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This agent provides insights on trends, notable stats, and comparisons between models <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

This entire sequence of five agents is orchestrated by a main sequential agent named "AI pipeline agent" <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

## Google ADK Web UI
The [[Agent Development Kit introduction and usage | Google ADK]] also provides a web UI for running and visualizing agents <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>. Agents can be set up in a VS Code environment and then executed using the `ADK web` command to launch the web interface, typically at `localhost:8000` <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

The web UI allows users to select an agent and provide input <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>. For example, a "multi-tool search agent" can delegate tasks to other agents like an XA search agent, which then performs searches using models like Meta Llama 3.1 8B Instruct and provides answers <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. A key feature of the web UI is its ability to visualize the agent workflow as a flowchart, showing how a root agent transfers tasks to sub-agents and how they interact to achieve the final result <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.