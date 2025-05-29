---
title: Agent to Agent Protocol
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The Agent to Agent (A2A) Protocol is an open standard announced by Google for how AI agents can operate and work together to perform tasks <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Announced on April 9, 2025, this protocol enables agents to interact with each other to complete multiple tasks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## How it Works
The A2A protocol involves a client agent and remote agents collaborating to achieve tasks <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This collaboration includes aspects such as:
*   Secure collaboration <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   State management <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   User experience <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   Negotiation <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Capability discovery <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>

### Architectural Overview
The protocol outlines an open standard for connecting various agents <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. A high-level diagram depicts:
*   **Agent One (Main Agent)**: This agent can have local agents and utilize Google-specific APIs like Vertex AI and Gemini <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **[[google_agent_development_kit | Agent Development Kit]] (ADK)**: An open-source agent building framework developed by Google <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **MCP Server**: An intermediary server used to fetch APIs and enterprise applications <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Agent Two (Main Agent)**: This agent can have its own local agents and run Large Language Models (LLMs) from various providers (e.g., Navius) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It can also utilize other agent frameworks like Q or OpenAI Agent SDK <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

These agents, whether leveraging [[google_agent_development_kit | Google ADK]] and specific AI tools or using LLMs from other providers and various agent frameworks, are designed to interact with each other to perform tasks <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## A2A Protocol vs. MCP
While related, the Agent to Agent Protocol differs from the Model Context Protocol (MCP):
*   **MCP** focuses on tool and resource collaboration, bringing elements together to perform tasks <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **A2A Protocol** specifically targets agent-agent collaboration, enabling dynamic multi-model communication between different agents without necessarily saving memory, resources, or tools <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Key Features
*   **Open Standard**: It is an open protocol, allowing the use of any framework or LLM to perform tasks <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Dynamic Multimodel Communication**: Facilitates interactions between diverse agents <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Samples Available**: Examples and resources using Google AD Lang and UI are provided for developers to explore <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.