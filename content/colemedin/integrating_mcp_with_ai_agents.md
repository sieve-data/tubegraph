---
title: Integrating MCP with AI agents
videoId: soC4n-nKWF8
---

From: [[colemedin]] <br/> 

The Model Context Protocol (MCP) is a significant development because it standardizes how tools are provided to Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This standardization makes [[building_ai_agents_with_pantic_ai_and_mcp | creating powerful AI agents]] more accessible <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While powerful, MCP is limiting when restricted to applications that natively support it, such as Claw Desktop, Wind Surf, or Cursor <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The true power of MCP lies in [[creating_custom_ai_agent_frameworks_with_mcp | building custom AI agents]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## [[benefits_of_mcp_for_ai_development | Benefits of Custom MCP Integration]]

[[integration_of_mcp_in_ai_tools | Integrating MCP servers with custom AI agents]] unlocks numerous possibilities:
*   Building custom frontends and applications <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   [[integration_of_a2a_and_mcp_in_ai_systems | Integrating MCP servers with other tools]] developed for the agent <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   Selecting specific tools from MCP servers, rather than being forced to use all of them <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.
*   It simplifies the process of adding functionality to agents, making tools highly accessible <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   Developers can reuse tools created by others, which is not easily possible without MCP's standardization <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a> <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## How to [[implementing_mcp_servers_in_ai_agent_systems | Implement MCP Servers in AI Agent Systems]]

The process of [[implementing_mcp_servers_in_ai_agent_systems | integrating MCP servers with custom AI agents]] is straightforward <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This method applies to any AI agent framework, even if no framework is used <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. An example using Pantic AI as the framework is available on GitHub <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a> <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Quick Start Guide

To integrate MCP servers with your custom AI agent:
1.  **Copy `mcp_client.py`:** This script provides the custom client needed <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  **Install Dependencies:** The only dependencies are your chosen AI framework (e.g., Pantic AI) and the MCP Python SDK, installable via pip <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a> <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
3.  **Set Up Configuration:** Configure MCP servers using a JSON file, similar to how it's done for applications like Claw Desktop <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Instructions for individual server configuration (e.g., Brave search MCP server) can be found in their respective GitHub repositories <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a> <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
4.  **Integrate in Python Code:**
    *   Import necessary components from MCP and your framework <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   Create an instance of the custom MCP client <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Load servers from your configuration file <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Start connections to each server to get a list of tools <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
    *   Pass this list of tools to your AI agent's instantiation (e.g., Pantic AI agent) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   Fetch the agent in your main function to use it <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

This process enables an AI agent to access tools from defined MCP servers <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Code Comparison: Without vs. With MCP

Before MCP, developers had to define individual Python functions for every capability they wanted to give an agent, leading to verbose and cumbersome code for multiple tools <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a> <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. With MCP, the implementation for an AI agent is significantly shorter and provides access to far more tools by leveraging the MCP client to hook into servers <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Demonstration

An AI agent using [[mcp_integration_with_various_ai_frameworks | MCP integration with Pantic AI]] can dynamically use various tools, such as Brave web search, GitHub, RAG through Chroma, local file systems, and SQLite <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. When the agent is run, it loads the MCP servers at the beginning <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Tool descriptions are given to the AI agent as part of the prompt, allowing it to understand and utilize them effectively <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Building a Custom MCP Client

The custom MCP client script is a starting point that can be modified to work with other frameworks <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Building this client involves handling resources to ensure MCP servers are properly torn down when the application crashes or ends <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Key Components

1.  **`MCP_Server` Class:** Represents an individual MCP server.
    *   **Initialization:** Takes the server's name and configuration (command, arguments, environment variables) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a> <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   **Connection:** Initializes a session for the client to connect to the specific server, handling different server types (Python, Docker, JavaScript) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a> <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
    *   **Tool Conversion:** A function to get tools from the MCP server session and convert them into the format required by the AI agent framework (e.g., Pantic AI) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a> <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This involves defining execution and preparation functions, and the tool's name, description, and JSON schema parameters <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

2.  **`MCP_Client` Class:** Manages all server connections.
    *   **Initialization:** Creates a list to manage `MCP_Server` instances, stores configuration, and lists all tools pulled from servers <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
    *   **Loading Servers:** Opens the configuration JSON file and creates an `MCP_Server` instance for each server defined <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
    *   **Starting Servers:** Loops through the configured servers and initializes each connection, then collects and converts their tools into the format needed for the AI agent <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a> <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
    *   **Cleanup:** Includes functions to properly tear down MCP servers when the application exits <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

When the application runs, the `MCP_Client` instantiates, connects to all MCP servers, and makes their tools available to the agent <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.

## Advanced Possibilities with Custom [[creating_custom_ai_agent_frameworks_with_mcp | AI Agent Frameworks]]

By [[creating_custom_ai_agent_frameworks_with_mcp | building your own AI agent]] and custom client, the possibilities become limitless <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

*   **[[integrating_ai_agents_with_live_platforms | Integration with Live Platforms]]**: Agents can be [[integrating_ai_agents_with_live_platforms | integrated into custom applications]] or frontends, for example, by exposing them as Fast API endpoints <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a> <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. This allows them to power Software as a Service (SaaS), portfolio websites, or other custom frontends <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
*   **Custom Tool Filtering**: Developers can implement custom filtering to pull only specific tools from an MCP server, avoiding bloating the LLM with unnecessary functionalities <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. This level of control is not available when using pre-built applications like Wind Surf, Cursor, or Claw Desktop, which force the use of all tools from a server <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a> <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

This custom implementation provides greater control over tool usage and invocation within your AI application <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.