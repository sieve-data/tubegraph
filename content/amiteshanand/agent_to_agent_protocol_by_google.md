---
title: Agent to Agent protocol by Google
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

Google has introduced the Agent to Agent (A2A) Protocol, an open standard designed to enable AI agents to interact and collaborate on various tasks <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This protocol was announced on April 9, 2025 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Purpose and Functionality
The A2A Protocol facilitates secure collaboration, state management, user experience, negotiation, and capability discovery between different agents <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. It allows a client agent to work with remote agents to perform multiple tasks collectively <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. As an open protocol, it supports the use of any framework or LLM to achieve tasks <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### How it Works
A high-level diagram illustrates how the A2A Protocol operates <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>:
*   **Agent One (Main Agent):** This agent can utilize local agents and Google-specific tools like Vertex AI and Gemini APIs <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It can also integrate with an [[agent_development_kit_introduction_and_usage | Agent Development Kit (ADK)]], which is an open-source agent building framework developed by Google <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **MCP Server:** An MCP (Model Context Protocol) server acts as an intermediary to fetch APIs, enterprise applications, and other resources <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Agent Two (Second Main Agent):** This agent can have its own local agents and run LLMs from various providers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It can also use other agent frameworks like LangChain or [[Building AI Agents with OpenAI Agent SDK | OpenAI Agent SDK]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Both agent types interact with each other to perform tasks <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### A2A Protocol vs. MCP
While both relate to AI interactions, the A2A Protocol differs from MCP:
*   **MCP (Model Context Protocol):** Primarily focuses on tool and resource collaboration <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **A2A Protocol:** Designed specifically for agent-to-agent collaboration, enabling dynamic multimodal communication between different agents without needing to save memory, resources, or tools <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Relation to Google Agent Development Kit (ADK)
The [[agent_development_kit_introduction_and_usage | Google Agent Development Kit (ADK)]] is a flexible and modular framework used for developing and deploying AI agents <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It can be used with popular LLMs and open-source tools, with a focus on tight integration with the Google ecosystem and Gemini models <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The ADK supports multi-agent architectures and a rich tool ecosystem, allowing the addition of multiple tools, third-party libraries, and frameworks like LangChain <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. It is deployment-ready and includes built-in evaluation features <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Google ADK provides various agent types that can be part of A2A collaboration:
*   **LLM-based Agents:** Utilize LLMs as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding how to proceed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Workflow Agents:** Specialize in controlling the execution flow of agents in predefined patterns, including [[Setting up a sequential agent workflow using Google ADK | sequential]], parallel, and loop agents <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Custom Agents:** Created by extending the base agent directly, allowing for unique operational logic, specific control flows, or specialized integrations not covered by standard types <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

An example of a [[Setting up a sequential agent workflow using Google ADK | sequential agent]] would be summarizing a webpage, where the "get page content" tool must always be called before the "summarize page" tool <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The [[agent_development_kit_introduction_and_usage | Google ADK]] can be installed using `pip install google-adk` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It also supports using other LLM providers via `light-llm` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Additionally, [[Features of Google Agent Development Kit | Google ADK]] includes a web UI for running and visualizing agent flows <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.