---
title: Features of Google Agent Development Kit
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The [[agent_development_kit_introduction_and_usage | Google Agent Development Kit (ADK)]] is a flexible and modular framework designed for developing and deploying AI agents <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It can be used with popular Large Language Models (LLMs) and open-source tools <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, with a focus on tight interaction with the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. However, it can also be integrated with other LLMs, third-party tools, and APIs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Installation <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>

The [[agent_development_kit_introduction_and_usage | Google ADK]] framework can be installed using `pip install Google ADK` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Core Features <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>

The [[agent_development_kit_introduction_and_usage | Google ADK]] offers several key features for developers:
*   **Multi-Agent Architecture:** Supports the development of multiple agents that can interact and collaborate <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Rich Tool Ecosystem:** Allows the addition of multiple tools, third-party libraries, LangChain UI, and other integrations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Deployment Ready:** Agents built with [[agent_development_kit_introduction_and_usage | Google ADK]] are ready for deployment <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Built-in Evaluation:** Includes functionalities for evaluating agent performance <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Understanding AI Agents within ADK <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

In the [[agent_development_kit_introduction_and_usage | Google ADK]], an agent is defined as a self-contained execution unit designed to act autonomously to achieve specific goals <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

The [[agent_development_kit_introduction_and_usage | Google ADK]] provides three core categories of agents that extend from a base agent <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>:

### 1. LLM-Based Agents <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
These agents utilize LLMs as their core engine to understand language, reason, plan, generate responses, and dynamically decide how to proceed <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. They are suitable for tasks requiring reasoning, tool use, or direct query answering <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### 2. Workflow Agents <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>
Workflow agents specialize in controlling the execution flow of agents in a predefined, deterministic pattern <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. They can be:
*   **[[setting_up_a_sequential_agent_workflow_using_google_adk | Sequential Agent]]:** Executes sub-agents in a specific order <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a> <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. An example is summarizing a webpage, where content must be retrieved before summarization <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Parallel Agent:** Executes multiple sub-agents concurrently <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Loop Agent:** Repeats a task or sequence of tasks <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

Workflow agents may or may not use LLMs, depending on the specific tasks they perform <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### 3. Custom Agents <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
These agents are created by directly extending the base agent, allowing developers to implement unique operational logic, specific control flows, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## Integration Capabilities <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>

The [[agent_development_kit_introduction_and_usage | Google ADK]] supports the integration of various LLM providers and third-party tools.

### Light LLM Support <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>
[[agent_development_kit_introduction_and_usage | Google ADK]] allows the use of other LLM providers through Light LLM, which enables compatibility by simply providing a prefix like `openai` <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a> <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. This allows for flexibility in model choice, including open-source models <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

### External Tool Integration <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
The framework can integrate with a variety of external tools and APIs, such as:
*   **Navius AI Studio:** Used for inference with models like LMAN demo ultra by Nvidia and Meta Lama 3.18 instruct <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **XA:** A tool that adds search APIs and functionalities to AI apps, providing LLMs with better context from search results <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Dei (Table):** Similar to XA, used for specific data points and analysis, such as searching artificial analysis websites for AI benchmarks or LLM statistics <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Firecrawl:** A tool for scraping and crawling data from various websites, offering features like data extraction, mapping, and LLM.txt features <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Agent to Agent Protocol by Google <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

[[agent_to_agent_protocol_by_google | Google's Agent to Agent (A2A) protocol]], announced on April 9, 2025, is an open protocol designed for building agents that can interact with each other to perform multiple tasks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This protocol involves a client agent and remote agents collaborating securely on tasks such as state management, user experience, negotiation, and capability discovery <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Web User Interface (UI) <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>

The [[agent_development_kit_introduction_and_usage | Google ADK]] supports a web UI to run and visualize agent workflows <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. It can be accessed locally by running the `ADK web` command, typically on `localhost:8000` <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a> <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. This UI allows users to select an agent, input queries, and visualize the agent's execution flow as a flowchart, showing how a root agent delegates tasks to sub-agents and how information is processed <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a> <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.