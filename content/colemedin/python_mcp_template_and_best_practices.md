---
title: Python MCP template and best practices
videoId: lbyPJqCI-tw
---

From: [[colemedin]] <br/> 

The Python [[model_context_protocol_mcp | Model Context Protocol]] (MCP) template provides a robust foundation for [[building_mcp_servers | building custom MCP servers]] that follow best practices [07:23]. This template aims to simplify the process of connecting AI agents to various services with full customization and control [02:24]. It is particularly useful for [[building_mcp_servers | building custom MCP servers]] that might not have existing solutions [04:18], or for those seeking more control over how an MCP server interacts with a service [04:07].

## Motivation and Benefits
While many [[model_context_protocol_mcp | MCP servers]] are available to connect to services like Gmail, Slack, or GitHub [00:09], the true power of MCP lies in [[building_mcp_servers | building custom MCP servers]] to connect agents to any desired service [00:28]. The provided template saves significant development time by offering a "perfect foundation" [00:54], incorporating lessons learned from hours of research, documentation review, and trial and error [11:00].

### Addressing Common Issues
Many existing [[model_context_protocol_mcp | MCP servers]] are not built optimally [09:00]. The template addresses common shortcomings observed in other implementations, such as:
*   Incorrect client instantiation [09:09].
*   Lack of support for multiple transport protocols [09:31], often only supporting one [09:34].
*   Duplication of tool descriptions [09:36].
*   Requiring API keys for features that could be free [09:42].

The template ensures support for various [[model_context_protocol_mcp | MCP]] transport protocols, which is crucial for a robust server [07:58].

## Key Resources
The template's development was informed by three main resources [01:13]:
1.  **Official [[model_context_protocol_mcp | MCP]] Documentation**: Provides a general understanding of [[model_context_protocol_mcp | MCP]], including how to [[building_mcp_servers | build servers]] and clients [01:36].
2.  **List of Existing [[model_context_protocol_mcp | MCP servers]] on GitHub**: Serves as a reference for examples of how to [[building_mcp_servers | build custom servers]] [01:50].
3.  **Anthropic's Official GitHub Repo for the [[model_context_protocol_mcp | MCP]] Python SDK**: Offers guidance on [[building_mcp_servers | building MCP servers]] specifically with Python, the simplest and most used language for this purpose [02:07].

## Template Structure and Best Practices

The template provides a structured approach to [[building_mcp_servers | building custom MCP servers]] [10:49], embodying several best practices:

### 1. Defining the Lifespan (`@mcp.lifespan`)
A core concept often missing in other [[model_context_protocol_mcp | MCP servers]] is the definition of a lifespan [16:05].
*   **Purpose**: It ensures that client connections (e.g., database connections like Mem Zero or Supabase) are defined only once for the entire lifetime of the server [16:10].
*   **Cleanup**: It allows for graceful shutdown and cleanup, such as closing database connections when the server stops [16:35].
*   **Context Sharing**: The single client instance defined in the lifespan becomes available to all tool calls through a shared `context` argument [17:08].

### 2. Instantiating the `FastMCP` Server
The template demonstrates how to instantiate the `FastMCP` server, similar to the Python SDK documentation [17:30]. It includes parameters for naming, description, lifespan integration, and host/port definitions for SSE transport [17:37].

### 3. Defining Tools (`@server.tool`)
Tools are the capabilities granted to the [[model_context_protocol_mcp | MCP server]] [18:11].
*   **Structure**: Tools are defined as Python functions decorated with `@mcp.tool` (or `@server.tool`, depending on the server instance name) [18:03].
*   **Parameters**: The first parameter is implicitly the `context` from the lifespan, providing access to the server's client [18:24]. Subsequent parameters are determined by the [[model_context_protocol_mcp | LLM]] [18:31].
*   **Doc Strings**: Crucially, the doc string within each tool function serves as its description for the [[model_context_protocol_mcp | LLM]] [18:42]. Descriptive doc strings are vital for the [[model_context_protocol_mcp | LLM]] to understand when and how to use a specific tool [19:14].
*   **Response Handling**: Tools return a response to the [[model_context_protocol_mcp | LLM]], indicating success or error, which then bubbles up to the user via the [[model_context_protocol_mcp | MCP client]] [19:34].

### 4. Handling Transport Protocols
A key best practice implemented in the template is supporting both primary transport types for [[model_context_protocol_mcp | MCP servers]]: Standard IO and SSE [21:09].
*   **Standard IO**:
    *   **Mechanism**: The client starts an instance of the server as a subprocess, managing the server's lifecycle [22:06].
    *   **Use Case**: Ideal for local processes where the [[model_context_protocol_mcp | MCP server]] and client run on the same machine due to its speed [22:19].
*   **SSE (Server-Sent Events)**:
    *   **Mechanism**: Functions more like a traditional HTTP connection, allowing the client to connect to a server that could be hosted remotely [22:31].
    *   **Use Case**: Essential for remote hosting of [[model_context_protocol_mcp | MCP servers]] (e.g., for monetization or separation from the client) [22:41]. Some clients, like N8N, only support SSE [23:04].
*   **Adaptability**: The template allows setting an environment variable (`transport`) to choose between SSE or Standard IO, making it highly adaptable [23:21].

### 5. Main Function and Server Execution
The `main` function is where the server is initialized and run [20:53]. It handles the logic for starting the server based on the chosen transport protocol [21:01].

## Integrating with AI Coding Assistants
The template significantly improves the effectiveness of AI coding assistants when [[building_mcp_servers | building custom MCP servers]] [08:28].
*   **Providing Examples**: Developers can copy the template's main function and paste it into their prompt as an example for the AI [08:31]. This concrete example helps the AI understand how to [[building_mcp_servers | build MCP servers]] more effectively than just raw documentation [08:42].
*   **Combined Prompting**: A powerful prompt structure involves combining the full [[model_context_protocol_mcp | MCP]] documentation (available in Markdown format) [13:31] with the template example, then requesting the AI to [[building_mcp_servers | build a server]] for a specific integration (e.g., LightRAG) [14:26].

## Example: Mem Zero MCP Server
The template is demonstrated through a Mem Zero [[model_context_protocol_mcp | MCP server]] example [07:35]. This example allows [[creating_custom_ai_agent_frameworks_with_mcp | AI agents]] to have long-term memory capabilities [00:17].
*   **Functionality**: The server integrates with the Mem Zero library to save and retrieve memories, allowing [[model_context_protocol_mcp | LLMs]] to remember past conversations [05:11].
*   **Tool Examples**: Includes tools to `save_memory`, `get_all_memories`, and `search_memories` [19:14].
*   **Client Compatibility**: The server works seamlessly with various [[model_context_protocol_mcp | MCP clients]] such as Claw Desktop, custom Pydantic [[creating_custom_ai_agent_frameworks_with_mcp | AI agents]], and N8N [06:12].
*   **Deployment**: Instructions for [[setting_up_and_using_mcp_servers | setting up and running everything]] are included, supporting both Python and Docker deployment with detailed configurations for all transport types [24:16]. Docker is recommended for standardized and easy deployment [24:23].

This template is designed to be easily adaptable, allowing users to remove the Mem Zero-specific parts and integrate their own tools for any desired service [07:46].