---
title: Connecting LLMs to services using MCP
videoId: lbyPJqCI-tw
---

From: [[colemedin]] <br/> 

The [[model_context_protocol_mcp | Model Context Protocol (MCP)]], developed by Anthropic, is emerging as a significant standard for connecting Large Language Models (LLMs) to various services like Gmail, Slack, GitHub, and web search <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This protocol allows LLMs to gain higher-level capabilities, such as long-term memory <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While many [[setting_up_and_using_mcp_servers | MCP servers]] already exist to connect to different services, the true power lies in [[building_mcp_servers | building custom MCP servers]] for specific needs and full customization <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Key Resources for MCP Development

To learn about and [[building_mcp_servers | build MCP servers]], several key resources are available:
*   **Official MCP Documentation:** Provides a general understanding of MCP, including guides for [[building_mcp_servers | building servers]] and clients <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **List of Existing MCP Servers on GitHub:** Useful as a reference point and for examples of how to [[building_mcp_servers | build custom servers]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Anthropic's Official GitHub Repo for the MCP Python SDK:** Essential for guidance on [[building_mcp_servers | MCP servers]] specifically with Python, which is noted as the simplest and most widely used language for this purpose <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## How MCP Servers Operate

An [[model_context_protocol_mcp | MCP server]] provides capabilities to an LLM by exposing tools and other components that the LLM can call <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. These servers can be configured in various [[setting_up_and_using_mcp_servers | MCP clients]] or applications that support MCP, such as Windsurf Cursor, N8N, Claw Desktop, or custom AI agents <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Using Existing MCP Servers

To use an existing [[model_context_protocol_mcp | MCP server]], such as Brave Search for web search capabilities:
1.  Copy the server's configuration from its GitHub listing <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  Paste this configuration into your [[setting_up_and_using_mcp_servers | MCP client's]] configuration (e.g., Claw Desktop's config file), including any necessary API keys <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  Restart the client to enable the new capabilities <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Once configured, the LLM can use the server's tools to answer questions that would otherwise be beyond its knowledge cutoff, like current events through web search <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Multiple [[model_context_protocol_mcp | MCP servers]] can be combined to add various new capabilities to an LLM <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### Why Build Your Own MCP Server?

While existing [[model_context_protocol_mcp | MCP servers]] are useful, they have limitations <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. If an existing server's interaction method doesn't align with your needs, or if a specific service or capability lacks an [[model_context_protocol_mcp | MCP server]], [[building_mcp_servers | building your own]] provides:
*   Full customization over how the LLM interacts with services <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   The ability to integrate with any desired service <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

An example of a custom [[model_context_protocol_mcp | MCP server]] is one integrating with MemZero, a library for long-term memory, enabling LLMs like Claw Desktop to remember past conversations <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This custom server functions identically to Anthropic's own [[model_context_protocol_mcp | MCP servers]] and can be used across various clients like Claw Desktop, custom Pydantic AI agents, and N8N <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Building an MCP Server with Python

A Python [[building_mcp_servers | MCP template]] can serve as a foundational starting point for [[building_mcp_servers | custom MCP servers]], incorporating best practices and supporting different transport protocols <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The template's readme provides setup and running instructions <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Leveraging AI Coding Assistants

AI coding assistants like Windsurf Cursor can assist in [[building_mcp_servers | MCP servers]]. By feeding them the official MCP documentation (available in Markdown) and the Python [[building_mcp_servers | MCP template]] as an example, they can generate initial server code <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Some assistants natively support MCP documentation, allowing direct access <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This method can provide a robust starting point, often more effective than documentation alone <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Core Components of an MCP Server

A robust [[building_mcp_servers | MCP server]] typically includes the following components:

#### 1. Lifespan
The lifespan defines the server's lifecycle, managing client connections like database instances (e.g., a MemZero client or Supabase instance) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. It ensures that a client is defined only once for the entire server lifetime and allows for graceful cleanup (e.g., closing database connections) <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This client instance is then implicitly passed as `context` to all tools defined within the server <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

#### 2. Server Instantiation
The server is instantiated using `fast_mcp`, providing a name, description, and defining the lifespan <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. For SSE transport, the host and port are also specified <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

#### 3. Tools
Tools are the primary way to add capabilities to an LLM <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. They are defined as Python functions decorated with `@mcp.tool` <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **Context:** The `context` object, containing the client defined in the lifespan, is implicitly passed as the first parameter to tool functions <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **LLM Parameters:** Subsequent parameters are chosen by the LLM (e.g., text to save as memory) <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   **Doc Strings:** The doc string of a tool function serves as its description for the LLM, guiding when and how to use the tool <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
*   **Responses:** Tool functions should return responses to the LLM, indicating success or errors, which can then be bubbled up to the user <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

For instance, a MemZero [[managing_databases_with_mcp_servers | MCP server]] might include tools to save new memories, retrieve all memories for a user, or search for specific memories <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

#### 4. Transport Protocols (Standard IO vs. SSE)
MCP servers support two primary transport protocols for client-server communication <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>:

*   **Standard IO:**
    *   **Mechanism:** The client starts the server instance as a subprocess, managing it directly <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
    *   **Ideal Use:** Best for local processes where the [[model_context_protocol_mcp | MCP server]] and client run on the same machine, offering fast communication <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.

*   **Server-Sent Events (SSE):**
    *   **Mechanism:** The client connects to the server like an HTTP API endpoint, which can be over the internet <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.
    *   **Ideal Use:** Crucial for scenarios where the [[model_context_protocol_mcp | MCP server]] runs remotely or separately from the client <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Certain clients, like N8N, only support SSE <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

A well-built [[building_mcp_servers | MCP server template]] should support both transport types, often through an environment variable, to maximize adaptability <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

### Running and Connecting to the Server

Once the [[building_mcp_servers | MCP server]] script is complete, it can be run using Python or Docker <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. Docker is recommended for standardized and easy deployment <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. Environment variables, such as those for MemZero API keys or the chosen transport type, need to be set up <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

After the Docker container is built and run, the [[model_context_protocol_mcp | MCP server]] becomes active on its specified port <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>. Clients like N8N can then be configured to connect to this local or remote server <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The server's logs can be monitored to confirm incoming requests from the client <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. This setup allows LLMs to utilize the custom tools (e.g., saving and retrieving memories) provided by the server <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.