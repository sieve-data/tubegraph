---
title: Building MCP servers
videoId: lbyPJqCI-tw
---

From: [[colemedin]] <br/> 

Anthropic's Model Context Protocol (MCP) is gaining recognition as the first standard for connecting Large Language Models (LLMs) to various services like Gmail, Slack, GitHub, and [[web_search_with_mcp_servers | web search]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This protocol enhances LLM capabilities, including long-term memory <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. While many [[setting_up_and_using_mcp_servers | existing MCP servers]] are available for common services, the true power lies in [[building_and_using_mcp_servers | building your own MCP servers]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This allows users to connect their agents to any desired service with simplicity and power <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Key Resources for Building MCP Servers

To learn about MCP and [[building_and_using_mcp_servers | building MCP servers]], key resources include:
*   The official MCP documentation <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   A list of [[setting_up_and_using_mcp_servers | existing MCP servers]] on GitHub, useful for reference and examples <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   Anthropic's official GitHub repository for the MCP Python SDK <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Python is generally the simplest and most used language for [[building_and_using_mcp_servers | MCP servers]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Understanding Custom MCP Servers

[[building_and_using_mcp_servers | Building your own MCP server]] involves creating a server that integrates with an MCP client, such as Windsurf Cursor, N8N, Claw Desktop, or custom AI agents <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### How Existing Servers Work
Existing [[setting_up_and_using_mcp_servers | MCP servers]] are configured by copying their details (e.g., from GitHub) into an MCP client's configuration, often requiring API keys <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. For example, a Brave Search MCP server can provide LLMs with powerful [[web_search_with_mcp_servers | web search]] capabilities, allowing them to answer questions requiring up-to-date information <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Multiple [[mcp_servers_for_ai_coding | MCP servers]] can be combined to add various capabilities to an LLM <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### The Need for Custom Servers
While existing servers are useful, they have limitations <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. If an existing server's interaction with a service isn't desired, or if there's no existing server for a particular service or capability, [[building_and_using_mcp_servers | building your own MCP server]] becomes necessary <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Custom servers provide full customization and control over how agents interact with services <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Example: Memory MCP Server
A custom [[building_and_using_mcp_servers | MCP server]] can integrate with a library like Mem (Mem Zero) to give AI agents long-term memory <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This allows an LLM client, such as Claw Desktop, to remember past conversations <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The configuration for a custom server is set up in a JSON file, similar to other [[mcp_servers_for_ai_coding | MCP servers]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Such a server can be connected to various MCP-supported clients, including custom Pydantic AI agents or N8N workflows <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

## MCP Server Template (Python)

A Python MCP template is available, incorporating best practices and supporting different transport protocols <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This template can serve as a concrete and practical foundation for [[building_and_using_mcp_servers | your own MCP server]], allowing users to remove Mem Zero-specific parts and implement their own tools <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Using the Template with AI Coding Assistants
The template is highly useful for [[musthave_mcp_servers_for_ai_coding | AI coding assistants]] <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Instead of feeding general documentation, copying the template's main function into a prompt can significantly improve the AI's ability to build an MCP server <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. AI coding assistants, like Windsurf, can also natively support MCP documentation or allow pasting it directly into the prompt <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

### Comparison to Other Servers
Many existing [[mcp_servers_for_ai_coding | MCP servers]] may not be built optimally <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. For instance, some may not handle client instantiation ideally (e.g., Chromobb) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a> or fully understand how MCP works, only supporting one transport protocol or duplicating tool descriptions (e.g., Mem's own MCP server) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The provided template aims to overcome these common [[challenges_and_solutions_in_mcp_server_development | challenges and solutions in MCP server development]], offering a robust and adaptable starting point <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Core Components of an MCP Server

### 1. Lifespan Definition
A crucial, often overlooked, concept for [[building_and_using_mcp_servers | MCP servers]] is defining their lifespan <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Most servers require a client (e.g., a database connection or a Mem Zero client for managing memories) that should be defined only once for the server's entire lifetime <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. The lifespan also allows for cleanup at the end, such as gracefully shutting down database connections <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. This client instance is then available as part of a `context` argument for all subsequent tool calls <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

### 2. Server Instantiation
After defining the lifespan, the `fast_mcp` server instance is created <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. Parameters include a name, description, the defined lifespan, and host/port for SSE transport <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

### 3. Tool Definition
Tools are attached to the server using a decorator like `@mcp.tool` <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. Each decorated function represents a capability given to the server <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

*   **Parameters**: The `context` is implicitly the first parameter, providing access to the client defined in the lifespan <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. Subsequent parameters are chosen by the LLM <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   **Docstrings**: The function's docstring is crucial as it serves as the description for the tool, informing the LLM when and how to use it <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. Descriptive docstrings are very important <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **Functionality**: Tools typically use the client (from the `context`) to perform actions, such as saving or retrieving memories in a database like Supabase (for [[managing_databases_with_mcp_servers | managing databases with MCP servers]]) <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. They return responses to the LLM, indicating success or errors <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Customization**: Users can easily replace the example tools (e.g., Mem Zero tools) with their own, integrating with services like Brave, Supabase, or Light RAG <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>.

## Transport Protocols: Standard IO vs. SSE

Understanding transport types (SSE or Standard IO) is the most technical aspect of MCP, as it defines how clients and servers communicate <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. A well-built [[building_and_using_mcp_servers | MCP server]] should support both <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

### Standard IO
*   **Mechanism**: The client starts the server instance as a subprocess, effectively managing it <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
*   **Use Case**: Ideal for local processes where the MCP server and client run on the same machine due to its speed <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.

### SSE (Server-Sent Events)
*   **Mechanism**: Similar to HTTP, where a client connects to a server's API endpoint, and this connection can be over the internet <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.
*   **Use Case**: Crucial when the MCP server is not running on the same machine as the client, especially for remote hosting or monetization <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Certain clients, like N8N, only support SSE <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

The provided template is adaptable to both transport types, controlled by an environment variable <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. The MCP instance handles the underlying hosting (e.g., using Starlette for SSE) <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.

## Running and Connecting

After completing the [[building_and_using_mcp_servers | MCP server]] (Python script), the server can be run. Instructions for installation and running are typically found in the project's README, covering both Python and Docker <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. Docker is recommended for its standardization and ease of use <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. Environment variables, such as API keys and transport type, need to be set <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

The instructions also detail how to connect to the server from an MCP client, providing configuration examples for all four combinations: Python/Docker with Standard IO/SSE <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. Once running, clients can connect and utilize the tools defined in the server, with requests visible in the server's logs <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.

[[building_a_new_rag_mcp_server | Building an MCP server]] makes it easy to take a server and apply it to literally anything you want <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.