---
title: Sequential agent demo with Google ADK
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The Google Agent Development Kit (ADK) is a flexible and modular framework designed for developing and deploying AI agents <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This article demonstrates how to build a team of agents using [[Building AI agents with Google ADK | Google ADK]] to create a multi-agent AI trend analyzer <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Tools and Models Used in the Demo

The demo leverages several tools and models for its functionality:
*   **Navius AI Studio**: Used for inference with models like Nvidia's LMAN Demo Ultra Model and Meta Llama 3.1 8B Instruct <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **XA**: A tool that adds search APIs and functionalities to AI applications, providing better context for LLMs from search results <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Table (API)**: Another platform similar to XA, used for different purposes within the demo, such as searching artificial analysis websites <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Firecrawl**: A tool for scraping and crawling data from various sites, offering features like crawling, mapping, extraction, and agent capabilities <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## [[Agent Development Kit introduction and usage | Google Agent Development Kit (ADK)]]

[[Agent Development Kit introduction and usage | Google ADK]] is designed to work with popular LLMs and open-source tools, focusing on tight integration with the Google ecosystem and Gemini models, though it can integrate with other LLMs as well <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a> <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Installation
The framework can be installed via `pip install Google ADK` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a> <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### [[Features of Google Agent Development Kit | Features of Google ADK]]
[[Features of Google Agent Development Kit | Key features]] include <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>:
*   Multi-agent architecture <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   Rich tool ecosystem, allowing integration of multiple tools, third-party libraries, and LangChain UI <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   Deployment readiness <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   Built-in evaluation capabilities <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### [[Understanding AI Agents | Types of Agents]] in ADK
In Google ADK, an agent is a self-contained execution unit designed to act autonomously to achieve specific goals, capable of performing tasks, interacting with users, utilizing external tools, and coordinating with other agents <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a> <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

ADK agents can be extended by three core categories <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>:
1.  **LLM-based Agents**: These agents use an LLM as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding how to proceed <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a> <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  **Workflow Agents**: These specialized agents control the execution flow of other agents in predefined patterns, including sequential, parallel, and loop agents <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a> <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. They may or may not use LLMs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
3.  **Custom Agents**: Created by directly extending the base agent, these allow implementing unique operational logic, specific control flow, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a> <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Sequential Agent

A sequential agent is a type of workflow agent that executes its sub-agents in the order they are specified in a list <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a> <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. For example, to summarize a webpage, a sequential agent would first call a "get page content" tool and then a "summarize page" tool, ensuring the correct order of operations <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

The process involves an input given to the main sequential agent, which then executes Sub-agent 1, followed by Sub-agent 2, and so on, until a final result is produced as output <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a> <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## [[Setting up a sequential agent workflow using Google ADK | Sequential Agent Demo: Multi-Agent AI Trend Analyzer]]

This demo showcases a multi-agent AI trend analyzer built using a sequential agent pipeline within [[Building AI agents with Google ADK | Google ADK]] <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. It's a chain of five agents working in sequence <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a> <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

### Pipeline Overview
The sequential agent orchestrates the following five sub-agents:
1.  **XA Agent**: Fetches the latest news and advancements related to AI from Twitter (x.com) using the XA search API <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a> <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
2.  **Table Agent**: Searches the Artificial Analysis website to get benchmarks and specific data points related to various models <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a> <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a> <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
3.  **Summary Agent**: Combines and formats the results from the XA Agent and Table Agent into a summary <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a> <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This agent uses the Meta Llama 3.1 8B Instruct model <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
4.  **Firecrawl Agent**: Scrapes content from the Navius AI Studio homepage using Firecrawl to get detailed information about models and services <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a> <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
5.  **Analysis Agent**: Analyzes the combined summary from Agent 3 and the scraped data from Agent 4, providing insights and recommendations <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a> <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This agent utilizes the Nvidia Neotron Ultra model for its analysis <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

### [[Integrating multiple AI tools with Google ADK | Integration with Light LLM]]
Google ADK allows [[Integrating multiple AI tools with Google ADK | integration]] with other LLM providers using `light LLM` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a> <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. `light LLM` enables using any LLM provider by simply providing `openai` as a prefix <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a> <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. This flexibility allows using models like those from Navius, which are open-source and cost-effective <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a> <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.

### Demo Execution
The demo starts by installing necessary libraries, including `Google ADK`, `light LLM`, and `python-dotenv` for API key management <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Each agent and its tools are defined with specific instructions and API keys <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a> <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a> <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The entire sequence is controlled by a main "pipeline" sequential agent <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a> <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

During execution, the agents perform their tasks sequentially:
*   XA Agent fetches recent news about AI advancements from X/Twitter <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   Table Agent retrieves information from Artificial Analysis <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   Summary Agent combines these findings <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   Firecrawl Agent scrapes content from the Navius website <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. While the scraping successfully extracts data like model pricing and quality metrics, the accuracy can vary, sometimes leading to non-accurate or hallucinated content <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a> <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   Analysis Agent provides a final analysis of AI trends, growth areas, notable services, and recommendations based on the combined information, comparing models like OpenAI, Llama, and Nvidia Neotron Ultra <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a> <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a> <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.

## Google ADK Web UI
[[Building AI agents with Google ADK | Google ADK]] supports a web UI for running agents <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a> <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. This UI can be accessed locally, typically on `localhost:8000` <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a> <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

A simple multi-tool search agent demonstration using the web UI shows a "root agent" delegating tasks to an "XA search agent" <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a> <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. The XA agent performs searches (e.g., for IPL match winners) using the Meta Llama 3.1 8B Instruct model <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a> <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>. The web UI also provides a visual flowchart, illustrating how tasks are transferred and executed between agents, such as the root agent transferring to the XA search agent, which then performs searches and returns content <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a> <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a> <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.