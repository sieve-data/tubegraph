---
title: Creating custom AI agent frameworks with MCP
videoId: soC4n-nKWF8
---

From: [[colemedin]] <br/> 

The Model Context Protocol (MCP) aims to standardize the process of providing [[creating_tools_and_dependencies_for_ai_agents | tools]] to Large Language Models (LLMs) to create powerful [[understanding_ai_agent_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This standardization makes [[understanding_ai_agent_frameworks | AI agent]] development more accessible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Limitations of Native MCP Applications <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>

While powerful, MCP can be limiting when restricted to applications that natively support it, such as Claw Desktop, Windsurf, or Cursor <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The true potential of MCP lies in [[creating_tools_and_dependencies_for_ai_agents | building our own AI agents]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Benefits of Custom MCP Integration <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

By [[integrating_mcp_with_ai_agents | integrating mCP servers]] with custom [[understanding_ai_agent_frameworks | agents]], the possibilities become virtually limitless <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This approach enables:
*   **Building Custom Frontends and Applications** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Integrating with Other Custom-Built Tools** for the [[understanding_ai_agent_frameworks | agent]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Picking and Choosing Specific Tools** from [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

This flexibility allows for greater control and customization than using pre-built applications like Claw Desktop or Windsurf <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. For instance, you can integrate your [[understanding_ai_agent_frameworks | AI agent]] as an API endpoint for a SaaS product, portfolio website, or YouTube channel <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

## Implementing MCP Servers in AI Agent Systems <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

The process of [[implementing_mcp_servers_in_ai_agent_systems | integrating mCP servers]] with your own [[understanding_ai_agent_frameworks | AI agent]] is relatively simple <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The approach demonstrated uses [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] as the [[understanding_ai_agent_frameworks | AI agent framework]], but the core principles apply to any [[frameworks_and_tools_for_ai_agent_development | framework]] or even a custom implementation without one <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Comparison: Custom MCP Agent vs. Non-MCP Agent <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

Without MCP, providing [[creating_tools_and_dependencies_for_ai_agents | tools]] to an [[understanding_ai_agent_frameworks | AI agent]] requires defining individual Python functions for each capability <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This becomes cumbersome when dealing with dozens of [[creating_tools_and_dependencies_for_ai_agents | tools]] from various services <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

In contrast, [[implementing_mcp_servers_in_ai_agent_systems | implementing mCP]] significantly reduces the code needed. By leveraging a custom client to hook into [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]], developers can access many more [[creating_tools_and_dependencies_for_ai_agents | tools]] with far less code <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This highlights the [[benefits_of_standardizing_ai_tools_with_mcp | beauty of standardizing things with mCP]], allowing reuse of existing [[creating_tools_and_dependencies_for_ai_agents | tools]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Quick Start Guide for [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] Integration <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>

1.  **Copy `mcp_client.py`**: This script contains the custom client necessary for [[integrating_mcp_with_ai_agents | mCP server integration]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  **Install [[creating_tools_and_dependencies_for_ai_agents | Dependencies]]**: Install [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] (or your chosen [[understanding_ai_agent_frameworks | framework]]) and the mCP Python SDK <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
3.  **Configure mCP Servers**: Use a `config.json` file, similar to how it's done for applications like Claw Desktop <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Configuration details for individual [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] can be found in their respective GitHub repositories <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
4.  **Integrate in Python Code**:
    *   Import necessary components from mCP and [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   Create an instance of your custom mCP client <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   Load servers from the configuration file <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Get a list of [[creating_tools_and_dependencies_for_ai_agents | tools]] by starting the connection to each server <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
    *   Pass this list of [[creating_tools_and_dependencies_for_ai_agents | tools]] to your [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI agent]] instance <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

This setup makes all defined [[creating_tools_and_dependencies_for_ai_agents | tools]] from the [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] accessible to the [[understanding_ai_agent_frameworks | AI agent]] <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Building the Custom mCP Client <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>

Creating the `mcp_client.py` script involves defining classes and functions to manage [[integrating_mcp_with_ai_agents | mCP server]] connections and tool conversion:

#### `MCP_Server` Class <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>
This class represents an individual [[implementing_mcp_servers_in_ai_agent_systems | mCP server]].
*   **Initialization**: Takes the server name and configuration (command, arguments, environment variables like API keys) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. It stores the client's connection session to the server <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **`initialize_server_connection`**: Creates the command based on the server type (Python, Docker, JavaScript) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. It then establishes the protocol and session to connect to the server <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This function also handles resource cleanup upon application termination <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **`create_pydantic_ai_tools`**: Retrieves [[creating_tools_and_dependencies_for_ai_agents | tools]] from the mCP server session using `list_tools()` <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a> and converts them into the format required by [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] using a helper function <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

#### Tool Conversion Function <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>
A dedicated function converts an mCP tool into a [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] tool (or for other [[frameworks_and_tools_for_ai_agent_development | frameworks]] like CrewAI or LangChain) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. This involves defining:
*   An execution function for the tool <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   The tool's name and description <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   A "prepare" function to provide the JSON schema for tool parameters (e.g., file path for a file system tool, query for web search) <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

#### `MCP_Client` Class <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>
This class manages all [[implementing_mcp_servers_in_ai_agent_systems | mCP server]] connections.
*   **Initialization**: Creates a list to hold `MCP_Server` instances, stores the overall configuration, and initializes a list for all collected [[creating_tools_and_dependencies_for_ai_agents | tools]] <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
*   **`load_servers`**: Opens the `config.json` file and creates an `MCP_Server` instance for each server defined in the configuration <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
*   **`start`**: Iterates through each loaded `MCP_Server` and calls its `initialize_server_connection` method to begin the connection <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. It then calls `create_pydantic_ai_tools` for each server to gather and convert its [[creating_tools_and_dependencies_for_ai_agents | tools]], building a master list of tools for the [[understanding_ai_agent_frameworks | agent]] <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   **Cleanup Functions**: Ensures that [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] are properly shut down when the application terminates, even if it crashes <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Practical Demonstration <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>

Running the custom [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] agent demonstrates its ability to load [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] (e.g., Brave web search, Git, SQLite) and dynamically use their [[creating_tools_and_dependencies_for_ai_agents | tools]] based on user prompts <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. The descriptions of these [[creating_tools_and_dependencies_for_ai_agents | tools]] are provided as part of the prompt to the [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI agent]], similar to how tools are defined in traditional code <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

## Conclusion: The Revolution of Standardized AI Tools <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>

MCP revolutionizes the way [[creating_tools_and_dependencies_for_ai_agents | AI tools]] are standardized, making it significantly easier to extend the functionality of [[understanding_ai_agent_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Instead of manually defining Python functions for every capability, developers can now easily add and manage [[creating_tools_and_dependencies_for_ai_agents | tools]] by simply configuring [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. This lower-level control provides immense value, allowing for bespoke applications and granular control over which [[creating_tools_and_dependencies_for_ai_agents | tools]] are used and how they are invoked <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>.