---
title: Model Context Protocol MCP
videoId: soC4n-nKWF8
---

From: [[colemedin]] <br/> 

The [[Anthropics Model Context Protocol MCP | Model Context Protocol (MCP)]] is a significant development in AI, standardizing the process of providing tools to Large Language Models (LLMs) and enabling the creation of powerful AI agents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This standardization makes building AI agents that can perform various tasks on behalf of users more accessible <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Limitations of Native MCP Support

While powerful, [[Anthropics Model Context Protocol MCP | MCP]]'s native support in applications like Claude desktop, Windsurf, or Cursor can be limiting <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. These applications often force users to utilize all tools a server provides, even if only a subset is desired <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

## Advantages of Custom AI Agents with MCP

The true potential of [[Anthropics Model Context Protocol MCP | MCP]] lies in building custom AI agents <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Integrating [[Anthropics Model Context Protocol MCP | MCP]] servers with custom agents offers several benefits:
*   **Custom Frontends and Applications:** Developers can build their own frontends and applications <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, allowing for integration into various platforms like SaaS products, portfolio websites, or YouTube channels via API endpoints <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
*   **Integration with Other Tools:** [[Anthropics Model Context Protocol MCP | MCP]] servers can be integrated with other tools built for the agent <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Selective Tool Usage:** Users can pick and choose specific tools from these servers <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, preventing LLM bloat from unnecessary tools <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. This level of control is not available with natively supported applications <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   **Reusability:** [[Anthropics Model Context Protocol MCP | MCP]] standardizes tools, allowing developers to reuse tools created by others rather than defining them from scratch <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Integrating MCP Servers with AI Agents

Integrating [[Anthropics Model Context Protocol MCP | MCP]] servers with a custom AI agent is straightforward and applicable across different frameworks, even if no framework is used <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The process can be completed in less than half an hour using a provided GitHub template <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Documentation References

The implementation of [[Anthropics Model Context Protocol MCP | MCP]] clients follows best practices laid out by Anthropic's official documentation <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>:
*   **Quick Start for Client Developers:** Provides a high-level overview of creating an [[Anthropics Model Context Protocol MCP | MCP]] client with Python <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Python SDK GitHub Repo:** Offers a more in-depth example on setting up an [[Anthropics Model Context Protocol MCP | MCP]] client and configuring servers similarly to Claude desktop's `cla_config.json` file <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Quick Start Steps for Pydantic AI (Example)

A GitHub repository provides a template for connecting [[Anthropics Model Context Protocol MCP | MCP]] servers to custom AI agents, demonstrated using Pydantic AI <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

1.  **Copy `mcp_client.py`:** This custom client script can be integrated into any project <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  **Install Dependencies:** The main dependencies are Pydantic AI (or your chosen framework) and the [[Anthropics Model Context Protocol MCP | MCP]] Python SDK <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
3.  **Set Up Configuration:** Configure [[Anthropics Model Context Protocol MCP | MCP]] servers using a JSON file, identical to how it's done for applications like Claude desktop <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Instructions for individual servers (e.g., Brave search [[Anthropics Model Context Protocol MCP | MCP]] server) can be found in their respective GitHub repositories <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

    > [!NOTE] Example `mcp_config.json`
    > ```json
    > {
    >   "servers": [
    >     {
    >       "name": "brave-search",
    >       "config": {
    >         "command": "python -m mcp_servers.brave_search.brave_search",
    >         "args": [],
    >         "env": {
    >           "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"
    >         }
    >       }
    >     },
    >     {
    >       "name": "file-system",
    >       "config": {
    >         "command": "python -m mcp_servers.file_system.file_system",
    >         "args": []
    >       }
    >     }
    >   ]
    > }
    > ```
4.  **Integrate into Python Code:**

    ```python
    from mcp_client import MCPClient
    from pydantic import BaseModel, Field # or your framework

    # Initialize MCP client
    mcp_client = MCPClient()

    # Load servers from configuration file
    # Ensure the path is correct for your mcp_config.json
    mcp_client.load_servers("path/to/your/mcp_config.json")

    # Start connections to servers and get tools
    tools = mcp_client.start()

    # Pass the tools to your Pydantic AI agent (or other framework agent)
    # agent = PydanticAIAgent(tools=tools, ...)
    ```

    This four-line process creates an [[Anthropics Model Context Protocol MCP | MCP]] client instance, loads server configurations, starts connections to each server, and retrieves a list of tools formatted for the agent <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Comparison: With vs. Without MCP

Without [[Anthropics Model Context Protocol MCP | MCP]], integrating tools requires defining individual Python functions for every capability an agent needs <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This leads to cumbersome code, especially when dozens of tools from different services are desired <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

With [[Anthropics Model Context Protocol MCP | MCP]], this is significantly simplified. The agent leverages the custom client to hook into [[Anthropics Model Context Protocol MCP | MCP]] servers, acquiring many more tools with substantially less code <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The way an agent interacts remains the same, but tool setup becomes much easier <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Example Usage

An [[Anthropics Model Context Protocol MCP | MCP]]-enabled agent can dynamically use various tools. For instance, it can "search the web to find the newest local LLMs" using the Brave [[Anthropics Model Context Protocol MCP | MCP]] server <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>, or interact with a file system, Git, or SQLite databases <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The descriptions for each tool are provided to the agent as part of its prompt <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Building the Custom MCP Client

The provided `mcp_client.py` script serves as a starting point for building a custom [[Anthropics Model Context Protocol MCP | MCP]] client <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Key Components

1.  **`MCPServer` Class:** Represents an individual [[Anthropics Model Context Protocol MCP | MCP]] server <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   **Initialization:** Takes a server name and configuration (e.g., command, arguments, environment variables) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
    *   **Resource Cleanup:** Includes lower-level code for managing resources and tearing down [[Anthropics Model Context Protocol MCP | MCP]] servers when the application ends or crashes <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   **Initialize Connection:** Creates the command based on server type (Python, Docker, JavaScript) and sets up parameters (command, arguments, environment variables like API keys) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
    *   **Establish Session:** Uses the `studio_server_parameters` object from [[Anthropics Model Context Protocol MCP | MCP]] to create a protocol, connect to the server via the client, and initialize a session <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
    *   **`create_pydantic_ai_tools` Function:** Retrieves tools from the [[Anthropics Model Context Protocol MCP | MCP]] server using `session.list_tools()` and converts them into the format required by Pydantic AI <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. This conversion function can be adapted for other frameworks like CrewAI or LangChain <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. The converted tool includes an execution function, name, description, and JSON schema for parameters <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

2.  **`MCPClient` Class:** Manages all server connections <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.
    *   **Initialization:** Creates a list of `MCPServer` instances, holds the overall configuration, and stores the list of collected tools <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
    *   **`load_servers` Function:** Reads the server configurations from the JSON file, creating an `MCPServer` instance for each entry <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
    *   **`start` Function:** Loops through all loaded servers, initializes their connections, calls `create_pydantic_ai_tools` for each to gather and convert tools, and builds a comprehensive list of tools <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This function is the primary entry point for fetching tools for the agent <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
    *   **Cleanup Functions:** Ensure proper termination and resource management for the [[Anthropics Model Context Protocol MCP | MCP]] servers <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Example in Action

When running the agent, the [[Anthropics Model Context Protocol MCP | MCP]] servers are loaded at the beginning <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. For Docker-based servers (e.g., Brave, Git, SQLite), Docker containers will be running <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. Importantly, if the program is crashed, the [[Anthropics Model Context Protocol MCP | MCP]] servers are instantly cleaned up, ensuring proper resource management <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

> [!INFO]
> The flexibility to extend agent functionality by adding more servers to the configuration file, rather than writing new Python functions for each, highlights the significant ease-of-use brought by [[Anthropics Model Context Protocol MCP | MCP]] <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

The ability to create custom implementations offers lower-level control, allowing for tailored applications and precise management over tool usage and invocation <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.