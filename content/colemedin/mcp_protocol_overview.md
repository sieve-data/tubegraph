---
title: mCP protocol overview
videoId: v_6EXt6T83I
---

From: [[colemedin]] <br/> 

The [[model_context_protocol_mcp|Model Context Protocol (MCP)]] is a significant development in the AI space, primarily championed by [[anthropics_model_context_protocol_mcp|Anthropic]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Its core purpose is to standardize how tools are provided to large language models (LLMs), enabling them to interact with various services and perform actions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Unlike many fleeting trends in AI, [[model_context_protocol_mcp|mCP]] is described as a "kindling log" rather than a "dwindling spark," indicating its lasting importance <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It has been around since November of last year, with its utility becoming increasingly recognized over time <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## What is [[model_context_protocol_mcp|mCP]]?

[[model_context_protocol_mcp|mCP]] can be conceptualized in several ways:
*   **USBC for AI applications**: Just as USB standardizes device connections, [[model_context_protocol_mcp|mCP]] standardizes the connection of tools to LLMs <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **API endpoints for [[agent_protocols_like_mcp_and_a2a|AI agents]]**: Similar to how companies expose backend services via APIs, [[model_context_protocol_mcp|mCP]] exposes tools for [[agent_protocols_like_mcp_and_a2a|AI agents]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a> <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a> <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

It's important to note that [[model_context_protocol_mcp|mCP]] does not fundamentally change *how* LLMs use tools; instead, it standardizes the *process* of making those tools available, making them more accessible and shareable <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a> <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Why [[model_context_protocol_mcp|mCP]] is Useful: Before and After

To understand the utility of [[model_context_protocol_mcp|mCP]], it's helpful to consider the challenges faced by [[agent_protocols_like_mcp_and_a2a|AI agents]] before its widespread adoption <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Before [[model_context_protocol_mcp|mCP]]
Prior to [[model_context_protocol_mcp|mCP]], [[agent_protocols_like_mcp_and_a2a|AI agents]] (built with frameworks like Pydantic AI, Crew AI, n8n) relied on individually defined functions as tools (e.g., creating files, making Git commits, listing database tables) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. While powerful for a single agent, reusing these tools across different agents or frameworks (e.g., from Pydantic AI to n8n, Claude Desktop, or other AI IDEs) was challenging <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This often led to:
*   **Redundant code development**: Developers would rewrite similar functionalities for different applications <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a> <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Difficulty in sharing**: There was no easy way to package and share tools as a neat unit with other developers, regardless of their chosen framework <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a> <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### With [[model_context_protocol_mcp|mCP]]
[[model_context_protocol_mcp|mCP]] introduces standardization by packaging tools for individual services in a reusable and shareable way <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This is achieved through [[setting_up_and_using_mcp_servers|mCP servers]] that act as a middleman, exposing tools to [[agent_protocols_like_mcp_and_a2a|AI agents]] in a standardized format <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

Key benefits of using [[model_context_protocol_mcp|mCP]]:
*   **Framework Agnostic Tool Use**: [[agent_protocols_like_mcp_and_a2a|AI agents]], whether built with n8n, Cursor, or Pydantic AI, can consume [[setting_up_and_using_mcp_servers|mCP servers]] in the same way <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a> <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Reduced Redundancy**: The same [[setting_up_and_using_mcp_servers|mCP servers]] can be used by multiple agents or instances without recreating the underlying tool code <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a> <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Enhanced Productivity**: Developers gain an "unfair advantage" by leveraging [[model_context_protocol_mcp|mCP]] for better AI agent development and increased productivity <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Where to Use [[model_context_protocol_mcp|mCP]]

[[model_context_protocol_mcp|mCP]] is rapidly gaining adoption across various platforms and frameworks.

### [[comparison_between_a2a_and_mcp_protocols|mCP Clients]]
Many applications and frameworks now support the [[model_context_protocol_mcp|Model Context Protocol]] <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>:
*   **AI IDEs**: Klein, Rine, Windsurf, Cursor <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Apps**: Claude Desktop, n8n <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Frameworks**: Pydantic AI, Crew AI, LangChain <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

While [[model_context_protocol_mcp|mCP]] has other features like resources (exposing real-time data), prompts (sharing templates), and sampling (requesting LLM completions as tools), the primary focus and most widely supported aspect currently is tool standardization <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a> <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a> <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a> <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a> <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### [[mcp_servers_for_ai_coding|mCP Servers]]
A wide array of [[mcp_servers_for_ai_coding|mCP servers]] are already available, developed by [[anthropics_model_context_protocol_mcp|Anthropic]], integrated by companies, or created by the community <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a> <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Examples include:
*   **Search**: Brave Search (for LLMs without built-in web search) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Databases**: Redis, Postgres, Superbase, Chroma Vector Database <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a> <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Browser Automation**: Browserbase's Stagehand (for web crawling and scraping using natural language) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a> <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **RAG (Retrieval-Augmented Generation)**: Qdrant (eliminates need for custom RAG tools) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a> <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **File System**: Basic file system operations <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Memory**: Basic memory implementations similar to mZero or Zep <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

[[mcp_servers_for_ai_coding|mCP servers]] are built with JavaScript or Python and can be run using tools like Docker, MPX (for JavaScript), or UVX (for Python) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a> <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a> <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## [[setting_up_and_using_mcp_servers|Setting up and Using [[model_context_protocol_mcp|mCP]] Servers]]

Integrating [[setting_up_and_using_mcp_servers|mCP servers]] into applications like Claude Desktop is a straightforward process <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. For Claude Desktop, users can configure [[setting_up_and_using_mcp_servers|mCP servers]] by editing a JSON configuration file, specifying the server details <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a> <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a> <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. Once configured, all available tools are listed within the application's interface <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

Using an example with Claude Desktop, an [[agent_protocols_like_mcp_and_a2a|AI agent]] can combine Brave Search and Stagehand [[mcp_servers_for_ai_coding|mCP servers]] to, for instance, search for documentation, navigate to the relevant page, and even take a screenshot <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a> <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a> <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a> <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

## [[building_and_using_mcp_servers|Building and Using [[model_context_protocol_mcp|mCP]]]]

[[model_context_protocol_mcp|mCP]] allows for both the creation of custom servers and the integration of [[model_context_protocol_mcp|mCP]] servers into custom [[agent_protocols_like_mcp_and_a2a|AI agents]] or workflows.

### Building Your Own [[building_and_using_mcp_servers|mCP Server]]
The official [[model_context_protocol_mcp|mCP]] documentation provides resources for developers looking to build their own [[building_and_using_mcp_servers|mCP servers]], including examples like a simple weather server <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a> <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. SDKs for different languages (e.g., Python) are available on GitHub <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a> <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

[[mcp_servers_for_ai_coding|AI coding]] assistants, such as Claude and Windsurf, can leverage the entire [[model_context_protocol_mcp|mCP]] documentation (available as Markdown) to help users build custom [[mcp_servers_for_ai_coding|mCP servers]], significantly accelerating development <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a> <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a> <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a> <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

### [[mcp_integration_with_various_ai_frameworks|mCP Integration with n8n]]
[[mcp_integration_with_various_ai_frameworks|n8n]], a workflow automation tool, supports [[mcp_integration_with_various_ai_frameworks|mCP integration]] through a community-developed node <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a> <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. This node allows users to configure and interact with [[mcp_servers_for_ai_coding|mCP servers]] within their n8n workflows, enabling agents to dynamically list and execute tools like web search <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a> <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a> <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

### [[mcp_integration_with_various_ai_frameworks|Creating Custom [[model_context_protocol_mcp|mCP]] Clients in Python]]
Developers can also create custom [[mcp_integration_with_various_ai_frameworks|mCP clients]] in Python to integrate [[mcp_servers_for_ai_coding|mCP servers]] with [[agent_protocols_like_mcp_and_a2a|AI agents]] built using frameworks like Pydantic AI <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a> <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This involves using the Python SDK to define server connections, gather available tools, and feed them into the agent's tool definitions <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a> <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a> <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This approach makes it easy to incorporate [[model_context_protocol_mcp|mCP]]-exposed tools into agents, just as if they were locally defined functions <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

## Future of [[model_context_protocol_mcp|mCP]]

While future standards might emerge, understanding [[model_context_protocol_mcp|mCP]] is crucial because any future standardization for integrating tools with LLMs is likely to resemble it closely <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a> <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. [[anthropics_model_context_protocol_mcp|Anthropic]] has an ambitious roadmap for [[model_context_protocol_mcp|mCP]], which includes:
*   **Remote [[model_context_protocol_mcp|mCP]] support**: Enabling [[mcp_servers_for_ai_coding|mCP servers]] to run in the cloud and clients to connect to them remotely <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Authentication and authorization**: Securely managing access to [[mcp_servers_for_ai_coding|mCP servers]] <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Monetization**: Potentially allowing for paid [[mcp_servers_for_ai_coding|mCP servers]] <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
*   **Agent support**: Advanced features for complex agentic workflows, including sub-agents directly supported as [[mcp_servers_for_ai_coding|mCP servers]] and hierarchical agent systems <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a> <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a> <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

These future developments aim to make powerful AI concepts, already achievable with advanced agentic workflows, significantly more accessible to a broader range of users <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a> <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.