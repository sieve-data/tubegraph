---
title: Sequential Agent Workflows
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

A sequential agent is a type of workflow agent that executes its sub-agents in a predefined order <a class="yt-timestamp" data-t="08:27:14">[08:27:14]</a>. The output of one sub-agent typically feeds into the next, ensuring tasks are completed in a specific sequence <a class="yt-timestamp" data-t="08:28:30">[08:28:30]</a>.

## What is a Sequential Agent?

Within the [[google_agent_development_kit | Google Agent Development Kit]] (ADK), an agent is a self-contained execution unit designed to act autonomously to achieve specific goals <a class="yt-timestamp" data-t="09:09:59">[09:09:59]</a>. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents <a class="yt-timestamp" data-t="06:15:36">[06:15:36]</a>.

Sequential agents are specialized workflow agents that control the execution flow of other agents in a predefined, deterministic pattern <a class="yt-timestamp" data-t="07:22:42">[07:22:42]</a>. This means tasks are performed one after another in the order they are listed <a class="yt-timestamp" data-t="08:28:30">[08:28:30]</a>. A sequential agent can involve a chain of sub-agents, with a final response being generated after all sub-agents have completed their tasks <a class="yt-timestamp" data-t="08:35:46">[08:35:46]</a>.

## Why Use Sequential Agents?

Sequential agents are ideal when tasks have dependencies, meaning one task must be completed before another can begin <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.

For example, to summarize a web page, an agent must first retrieve the page's content (`get page content` tool) before it can summarize it (`summarize page` tool) <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. This ensures a logical progression of tasks <a class="yt-timestamp" data-t="08:50:49">[08:50:49]</a>.

## Sequential Agents in [[google_agent_development_kit | Google ADK]]

The [[google_agent_development_kit | Google Agent Development Kit]] allows for the creation of various [[types_and_features_of_ai_agents | types of AI agents]], including LLM-based agents, workflow agents (sequential, parallel, loop), and custom logic agents <a class="yt-timestamp" data-t="07:10:48">[07:10:48]</a>. Sequential agents fall under the workflow agent category <a class="yt-timestamp" data-t="07:20:20">[07:20:20]</a>.

A high-level diagram for an [[agent_to_agent_protocol | Agent to Agent Protocol]] often illustrates a primary agent orchestrating various sub-agents. With [[google_agent_development_kit | Google ADK]], a main agent (referred to as a `pipeline` in a demo) can control multiple sub-agents <a class="yt-timestamp" data-t="09:10:30">[09:10:30]</a><a class="yt-timestamp" data-t="09:15:22">[09:15:22]</a>. The sub-agents can use different Large Language Models (LLMs) and third-party tools <a class="yt-timestamp" data-t="03:45:30">[03:45:30]</a>.

### Key Features for Building Sequential Agents with [[google_agent_development_kit | Google ADK]]:
*   **Flexible and Modular Framework:** [[google_agent_development_kit | Google ADK]] is designed for developing and deploying AI agents <a class="yt-timestamp" data-t="04:54:19">[04:54:19]</a>.
*   **LLM Compatibility:** It can be used with popular LLMs and open-source tools <a class="yt-timestamp" data-t="04:58:36">[04:58:36]</a>. It supports other LLM providers via LightLLM, by adding an `openai` prefix to the model name <a class="yt-timestamp" data-t="10:48:47">[10:48:47]</a>.
*   **Tool Ecosystem:** Allows integration of multiple tools, third-party libraries, and APIs <a class="yt-timestamp" data-t="05:29:08">[05:29:08]</a>.
*   **Deployment Ready:** Facilitates deployment of agents <a class="yt-timestamp" data-t="05:35:05">[05:35:05]</a>.
*   **Web UI:** [[google_agent_development_kit | Google ADK]] supports a web user interface for running and visualizing agent flows, which can be accessed via `ADK web` command on localhost:8000 <a class="yt-timestamp" data-t="22:38:00">[22:38:00]</a><a class="yt-timestamp" data-t="23:37:06">[23:37:06]</a>. This UI provides a flowchart visualization of how root agents transfer tasks to sub-agents <a class="yt-timestamp" data-t="24:28:07">[24:28:07]</a>.

Installation of [[google_agent_development_kit | Google ADK]] is done via `pip install Google-ADK` <a class="yt-timestamp" data-t="05:21:49">[05:21:49]</a>.

## Demo: Multi-Agent AI Trend Analyzer

A demo of a multi-agent AI trend analyzer built with [[google_agent_development_kit | Google ADK]] showcases a sequential agent workflow involving a chain of five sub-agents <a class="yt-timestamp" data-t="09:44:27">[09:44:27]</a>. This pipeline orchestrates various tools and models to analyze AI trends <a class="yt-timestamp" data-t="09:51:30">[09:51:30]</a>.

The tools used in this demo include:
*   **Navius AI Studio:** Used for inference with models like Nvidia's LMAN demo ultra model and Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>.
*   **XA:** A tool for adding search APIs and functionalities to AI apps to provide LLMs with better context from search results <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>.
*   **DEI (Table):** Another platform similar to XA, used for different purposes in the demo <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>.
*   **Firecrawl:** A tool for scraping, crawling, mapping, and extracting data from various sites <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.

The sequential pipeline involves the following agents:
1.  **XA Agent:** Fetches the latest AI news and advancements from X (Twitter) using the XA search tool <a class="yt-timestamp" data-t="10:02:59">[10:02:59]</a><a class="yt-timestamp" data-t="12:51:41">[12:51:41]</a>.
2.  **Table Agent (DEI):** Searches for AI benchmarks, LLM statistics, or AI provider analysis from artificial analysis websites using the Table search tool <a class="yt-timestamp" data-t="10:07:33">[10:07:33]</a><a class="yt-timestamp" data-t="12:50:52">[12:50:52]</a>.
3.  **Summary Agent:** Combines and formats the results from the XA and Table agents into a cohesive summary <a class="yt-timestamp" data-t="10:23:44">[10:23:44]</a><a class="yt-timestamp" data-t="13:30:17">[13:30:17]</a>.
4.  **Firecrawl Agent:** Scraps content from the Navius AI Studio homepage <a class="yt-timestamp" data-t="10:15:10">[10:15:10]</a><a class="yt-timestamp" data-t="13:42:04">[13:42:04]</a>.
5.  **Analysis Agent:** Utilizes the Nvidia Neotron Ultra model to analyze the combined summary and scraped data, providing insights <a class="yt-timestamp" data-t="10:27:07">[10:27:07]</a><a class="yt-timestamp" data-t="14:10:08">[14:10:08]</a>. This agent also considers the scraped data from Navius AI Studio to compare models like Open AI 3.0/4.0 mini and Llama 3.1 Neotron Ultra <a class="yt-timestamp" data-t="20:26:01">[20:26:01]</a>.

The entire process is managed by a single orchestrator agent, a sequential agent named `AI pipeline agent` <a class="yt-timestamp" data-t="15:22:21">[15:22:21]</a>. The sub-agents are primarily powered by Meta Llama 3.1 8B Instruct, with the final analysis agent using the Nvidia Neotron Ultra model <a class="yt-timestamp" data-t="10:37:34">[10:37:34]</a><a class="yt-timestamp" data-t="14:40:48">[14:40:48]</a>. This multi-agent setup works together in sequence to perform trend analysis <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.