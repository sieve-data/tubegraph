---
title: Agent protocols like MCP and A2A
videoId: BFWviieMyGw
---

From: [[colemedin]] <br/> 

2025 has been a significant year for AI agents and, more specifically, agent protocols <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. These protocols aim to simplify the connection and interaction between various components within AI systems <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Anthropic's MCP Protocol

[[model_context_protocol_mcp | Anthropic's Model Context Protocol (MCP)]] is designed to facilitate the easy connection of tools to AI agents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Although developed by Anthropic, its use is not restricted to specific LLMs like Claude <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a> <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Integration and Applications of MCP
Lutra, a platform for creating automations with natural language, has integrated with [[model_context_protocol_mcp | MCP]] <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This integration allows users to incorporate [[mcp_servers_for_ai_coding | MCP servers]] into their automations <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

Users can connect to any [[implementing_mcp_servers_in_ai_agent_systems | MCP server]], whether self-built and running remotely or one of the recommended options <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a> <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. For instance, Lutra can leverage an [[model_context_protocol_mcp | MCP server]] to generate custom code for using various tools and integrating with other services simultaneously <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a> <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Evolution of MCP
[[model_context_protocol_mcp | MCP]] was initially released in November of the previous year <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. It took approximately four to five months, until around March of the current year, for [[model_context_protocol_mcp | MCP]] to gain widespread adoption <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a> <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Early challenges for [[model_context_protocol_mcp | MCP]] included less-than-optimal documentation, a lack of maturity in the protocol itself, and initial struggles with security handling <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a> <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a> <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a> <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.

## Google's A2A Protocol

[[googles_a2a_protocol_for_ai_agents | Google's A2A protocol]] focuses on enabling seamless connections between different AI agents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Compared to [[model_context_protocol_mcp | MCP]], [[googles_a2a_protocol_for_ai_agents | A2A]] has not yet achieved widespread adoption <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a> <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.

## The Missing Piece: AGUI

Despite the power of protocols like [[model_context_protocol_mcp | MCP]] and [[googles_a2a_protocol_for_ai_agents | A2A]], a significant gap existed in connecting AI agents to user frontends to create full applications <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a> <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This gap has been addressed by the introduction of AGUI <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

AGUI is a protocol designed to standardize the connection between AI agents and frontends, enabling users to interact with agents in a seamless manner <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Similar to [[model_context_protocol_mcp | MCP]] and [[googles_a2a_protocol_for_ai_agents | A2A]], AGUI acts as a middleman to facilitate smooth connections <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. It is viewed as a "game-changer" for transforming agents into full applications <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a> <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

The development of AGUI was undertaken by the CopilotKit team <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, which specializes in open-source front-end libraries for building agentic applications <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. AGUI is open-source and does not rely on a specific framework <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a> <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This allows developers to build any frontend with any framework and connect it to any agent <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Comparison between A2A, MCP, and AGUI
The table below highlights key aspects of [[comparison_between_a2a_and_mcp_protocols | A2A]], [[model_context_protocol_mcp | MCP]], and AGUI:

| Protocol | Primary Function | Developer | Open Source | Adoption Status | Key Benefit |
|---|---|---|---|---|---|
| [[model_context_protocol_mcp | MCP]] | Connect tools to agents | Anthropic | Yes | Growing | Easy tool integration |
| [[googles_a2a_protocol_for_ai_agents | A2A]] | Connect agents to other agents | Google | N/A | Not widely adopted | Seamless agent-to-agent communication |
| AGUI | Connect agents to frontends/users | CopilotKit | Yes | New, promising | Standardized user interaction, real-time streaming, framework agnostic |

### Current State of AGUI
AGUI is a very new protocol <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. While it's recommended to explore and learn it, it is not yet fully mature for all applications <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a> <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a> <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. However, the CopilotKit team has done a commendable job with AGUI's initial documentation and setup, outperforming [[model_context_protocol_mcp | MCP]] in its early stages <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a> <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a> <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>. The structured event-based communication AGUI employs for agent-frontend interactions is considered intuitive and powerful <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a> <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a> <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.