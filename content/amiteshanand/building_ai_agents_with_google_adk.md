---
title: Building AI Agents with Google ADK
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

This article explores the [[google_agent_development_kit | Google Agent Development Kit (ADK)]], a framework for building and deploying AI agents. It also showcases a full-fledged agent demo built using [[google_agent_development_kit | Google ADK]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Google Agent to Agent (A2A) Protocol

Google announced the Agent to Agent (A2A) Protocol on April 9, 2025 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This open protocol allows agents to interact with each other and perform multiple tasks <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. It facilitates secure collaboration, state management, user experience, negotiation, and capability discovery between client agents and remote agents <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The A2A protocol is an open standard for connecting agents <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. A high-level diagram illustrates how a main agent (Agent One) can have local agents, use Google-specific Gemini APIs via Vertex AI, and connect to a [[google_agent_development_kit | Google ADK]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Another main agent (Agent Two) can use LLMs from different providers (e.g., Navius) and other agent frameworks like QI or [[building_ai_agents_with_openai_sdk_and_lyzr_ai | OpenAI Agent SDK]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. These agents interact with each other to perform tasks <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### A2A vs. Model Context Protocol (MCP)

While MCP is for tool and resource collaboration <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, A2A Protocol is specifically for agent-to-agent collaboration, enabling dynamic multi-modal communication between agents without saving memory, resources, or tools <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It's an open protocol, allowing the use of any framework or LLM <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Google Agent Development Kit (ADK)

The [[google_agent_development_kit | Google Agent Development Kit (ADK)]] is a flexible and modular framework for developing and deploying AI agents <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It can be used with popular LLMs and open-source tools, focusing on integration with the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. However, it can also integrate with other LLMs, [[using_thirdparty_tools_in_ai_development | third-party tools]], and APIs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Features

[[google_agent_development_kit | Google ADK]] offers several features:
*   Multi-agent architecture <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
*   Rich tool ecosystem for adding multiple tools and [[using_thirdparty_tools_in_ai_development | third-party libraries]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>
*   Deployment readiness <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
*   Built-in evaluation capabilities <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>

### Installation

[[google_agent_development_kit | Google ADK]] can be installed via pip: `pip install Google-ADK` <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Agent Definition within ADK

In [[google_agent_development_kit | Google ADK]], an agent is a self-contained execution unit designed to act autonomously to achieve specific goals <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

Agents can be extended into three core categories <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>:

1.  **LLM-Based Agents**: Utilize an LLM as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding how to proceed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
2.  **Workflow Agents**: Specialized agents that control the execution flow of other agents in a predefined, deterministic pattern <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. They can be:
    *   **Sequential Agents**: Execute sub-agents in the order they are specified in a list <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. An example is summarizing a webpage, where content must first be retrieved before it can be summarized <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   **Parallel Agents**: Execute sub-agents concurrently.
    *   **Loop Agents**: Execute sub-agents repeatedly based on a condition.
3.  **Custom Agents**: Created by extending the base agent directly, allowing for unique operational logic, specific control flow, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Multi-Agent AI Trend Analyzer Demo

A demo of a multi-agent AI trend analyzer was built using [[google_agent_development_kit | Google ADK]], Navius AI, XA, DEI, and Firecrawl <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This system is a [[building_multiagent_systems_using_google_collab | multi-agent pipeline]] orchestrated as a sequential agent chain <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Tools and Models Used

*   **Navius AI Studio**: Used for inference <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
    *   Models: NVIDIA LMAN Demo Ultra model (253B) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **XA**: Adds search APIs and functionalities to AI apps for better LLM context <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **DEI**: Similar to XA, used for different purposes in the demo <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Firecrawl**: Scrapes data from various sites, offering features like crawling, mapping, extracting, agent features, and LLM.txt <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **LightLLM**: Allows [[google_agent_development_kit | Google ADK]] to use any other LLM provider supported by LightLLM <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Python-dotenv**: For API key management <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

### Sequential Agent Pipeline

The demo utilized a chain of five sequential agents <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:

1.  **XA Agent**: Fetches the latest news about AI advancements from Twitter (X.com) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a> using the `XA search AI` tool <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. It prefixes its response with "XAR agent" <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
2.  **DEI Agent**: Gets benchmarks and specific data points related to various models from the artificial analysis website <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a> using the `table search analysis` tool <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. It prefixes its response with "table agent" <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
3.  **Summary Agent**: Combines and formats the results from the XA and DEI agents <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
4.  **Firecrawl Agent**: Scraps content from the Navius AI studio homepage <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> using the `Firecrawl scrap NS` tool to fetch markdown content <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
5.  **Analysis Agent**: Analyzes the combined summary from agent 3 and the scraped data from agent 4 to provide insights <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This agent uses the NVIDIA Llama 3.1 253B model <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a> and prefixes its response with "analysis agent" <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

The entire pipeline is controlled by one orchestrator agent named `AI pipeline agent` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

## Google ADK Web UI

[[google_agent_development_kit | Google ADK]] supports a web UI for running agents <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>. This UI can be accessed at `localhost:8000` <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

### Multi-Tool Search Agent Example

A simple multi-tool search agent demo using the web UI showcases the `XA search agent` to perform searches with Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. This agent is orchestrated by a `root agent` that delegates tasks to the `XA search agent` <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

When a query like "who won the IPL on 12th April and who was the big scorer" is entered <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>, the root agent transfers the task to the XA agent, which performs searches and provides the answer <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.

The web UI also provides a flowchart visualization, showing the flow of tasks from the root agent to the XA search agent and how the search is performed <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.