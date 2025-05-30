---
title: Building AI agents with Pantic AI and MCP
videoId: soC4n-nKWF8
---

From: [[colemedin]] <br/> 
The Model Context Protocol (MCP) standardizes how tools are given to Large Language Models (LLMs), making it more accessible to create powerful [[Building AI Agents | AI agents]] capable of performing various tasks <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. While applications like Claude Desktop, Windswept, or Cursor natively support MCP, the true potential lies in [[Integrating MCP with AI agents | integrating MCP with custom-built AI agents]] <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

## Advantages of [[Implementing MCP servers in AI agent systems | Implementing MCP Servers in AI Agent Systems]]

[[Building AI Agents | Building AI agents]] with MCP offers "truly limitless" possibilities <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. Key advantages include:
*   **Custom Frontends and Applications** Users can [[Building fullscale AI agents | build their own frontends and applications]], integrating MCP servers directly into their systems <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. This allows for custom API endpoints for SaaS, portfolio websites, or YouTube channels <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.
*   **Integration with Custom Tools** MCP servers can be integrated with other tools developed for the agent <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **Selective Tool Usage** Users can choose which tools to pull from MCP servers, avoiding bloating the LLM with unnecessary functionalities <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>, <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>.
*   **Standardization and Reusability** MCP provides a standardized way to define tools, allowing for the reuse of tools developed by others instead of having to create individual Python functions for every capability <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>, <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>. This significantly reduces code complexity <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

## [[Building AI Agents with Pydantic AI | Building AI Agents with Pydantic AI and Lang graph]] and MCP

While this guide focuses on using Pydantic AI as the AI agent framework, the principles apply regardless of the framework chosen <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. The setup process is designed to be straightforward, taking less than half an hour with a provided GitHub template <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

For a comprehensive overview of MCP, it is recommended to review existing documentation <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

### Example Implementation

A custom AI agent built with Pydantic AI leveraging MCP can perform tasks like searching the web using the Brave MCP server <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>, accessing local files with the local file MCP server <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, or interacting with databases via SQLite MCP server <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. This demonstrates the ease of extending agent functionality <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

An example of a custom frontend for an MCP-powered agent is the Live Agent Studio platform <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>, which can be turned into an API endpoint <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.

### Resources and Best Practices

The methodology for [[Creating custom AI agent frameworks with MCP | creating custom AI agent frameworks with MCP]] clients is based on official Anthropic documentation:
*   **MCP Docs Quick Start for Client Developers** <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>
*   **Python SDK GitHub Repo Example** <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>

These resources guide on setting up an MCP client and configuring servers similarly to Claude Desktop using a `claude_config.json` file <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

### Step-by-Step Guide for [[Building AI Agents with Pydantic AI | Building AI Agents with Pydantic AI]]

A GitHub repository provides the necessary tools to connect MCP servers to a custom AI agent using Pydantic AI, with instructions for adapting it to other frameworks <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>, <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

#### Quick Start Steps:
1.  **Copy `mcp_client.py` script**: This custom client script can be integrated into any project <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
2.  **Install Dependencies**: Install `pydantic-ai` (or your chosen framework) and the `mcp-python-sdk` using `pip` <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
3.  **Configure MCP Servers**: The configuration method mirrors that for applications like Claude Desktop. An example `config.json` file is provided, and server-specific instructions can be found in the MCP server GitHub repository <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>, <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
4.  **Set up in Python Code**:
    *   Import necessary components from `mcp` and `pydantic_ai` <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
    *   Create an instance of the MCP client <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
    *   Load servers from the configuration file <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
    *   Get a list of tools by starting connections to each server <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
    *   Pass the list of tools to the Pydantic AI agent instance <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.
    *   Fetch the agent in the main function to use it <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

This setup allows a Pydantic AI agent to access all defined tools from the MCP servers <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.

### Custom MCP Client Architecture

The custom MCP client manages individual server connections and handles resource cleanup (e.g., tearing down Docker containers when the application crashes or exits) <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>, <a class="yt-timestamp" data-t="18:37:00">[18:37:00]</a>.

Key components and functions in the custom client:
*   **`MCPServer` Class**: Represents individual MCP servers. Initializes with a name and configuration, and stores the client connection session <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
    *   **`initialize_server_connection`**: Creates the command and arguments for the server (Python, Docker, JavaScript), defines environment variables (e.g., API keys), establishes the protocol connection, and initializes the session <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.
    *   **`create_pydantic_ai_tools`**: Lists tools from the MCP server session and converts them into the Pydantic AI format using a helper function <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.
    *   **`_convert_mcp_tool_to_pydantic_tool`**: Takes an MCP tool and returns a Pydantic tool. This involves defining an execution function, tool name, description, and a `prepare` function to get the JSON schema for parameters <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
*   **`MCPClient` Class**: Manages multiple server connections.
    *   **Initialization**: Creates a list of `MCPServer` instances <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.
    *   **`load_servers`**: Opens the `config.json` file, iterates through each server entry, and creates an `MCPServer` instance for each <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.
    *   **`start`**: Loops through all loaded servers, initializes their connections, calls `create_pydantic_ai_tools` for each, and builds a combined list of Pydantic AI tools <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. This list is then passed to the Pydantic AI agent <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.
    *   **Cleanup Functions**: Handle resource management to ensure MCP servers are properly terminated <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.

The process of interacting with the agent remains consistent, making it easier to set up tools without altering the core agent interaction <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. The agent dynamically uses the injected tools based on the query, providing descriptions of each tool as part of the prompt <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.

This custom implementation provides lower-level control, allowing developers to integrate agents into unique applications and precisely manage the tools they utilize <a class="yt-timestamp" data-t="20:35:00">[20:35:00]</a>.