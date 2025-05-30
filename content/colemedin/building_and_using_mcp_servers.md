---
title: Building and using mCP servers
videoId: v_6EXt6T83I
---

From: [[colemedin]] <br/> 

The Model Context Protocol (mCP) is a standardized protocol developed by Anthropic to enable Large Language Models (LLMs) to use external tools and services efficiently <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It's designed to be a long-lasting standard in the AI space, much like a "kindling log" that keeps getting hotter, rather than a fleeting "spark" of hype <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. By using mCP, LLMs and AI agents gain an "unfair advantage" over those that don't <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

mCP is likened to a USBC port for AI applications, standardizing how tools connect to LLMs <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Another analogy is that mCP provides API endpoints for AI agents, allowing companies to expose their backend services to other applications <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Why mCP Servers are Essential
Before mCP, if an AI agent needed to interact with services (e.g., make a file, commit to Git, list database tables), developers would create individual functions for each tool, coupled with documentation instructing the AI agent on when and how to use them <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. While powerful, this approach led to significant limitations <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>:
*   **Lack of Reusability**: Tools built for one AI agent framework (e.g., Pydantic AI) could not easily be reused in another (e.g., n8n, Claude Desktop, Windsurf) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Redundant Code**: Developers often had to rewrite the same functionality for different agents or share tools inefficiently <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **No Standardization**: There was no neat way to package and share tools for individual services, leading to repeated development <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

mCP solves this by providing a standardized way to package and expose tools, allowing AI agents to consume these services uniformly, regardless of the framework used <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This ensures reusability and eliminates redundancy <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. It's important to note that mCP doesn't change *how* tools are used by LLMs (they are still given as part of the prompt), but rather standardizes their accessibility and packaging <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

## Available mCP Servers
A wide array of services are already available as mCP servers, developed by Anthropic, official integrations, and the open-source community <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Notable examples include:
*   **Brave Search**: Allows LLMs like Claude or local LLMs without built-in web search capabilities to perform web queries <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Database Management**: Servers exist for managing databases like Redis, PostgreSQL, and Supabase <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Browserbase/Stagehand**: Provides a headless browser as a service, enabling AI agents to perform web crawling and scraping using natural language <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Quadrant**: Offers [[building_a_new_rag_mcp_server|RAG]] (Retrieval Augmented Generation) capabilities without requiring custom tool implementation <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Chroma**: An mCP server for the Chroma vector database <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **File System**: Basic servers for interacting with the local file system <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Memory**: Basic implementations for memory similar to mZero or Zep <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Archon**: An mCP server for an AI agent builder <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

## [[setting_up_and_using_mcp_servers|Setting Up and Using mCP Servers]]

### Running mCP Servers
mCP servers are typically built with JavaScript or Python <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Depending on their build language, they can be run using tools like:
*   **Docker**: For containerized environments <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **MPX**: For JavaScript-based servers (requires Node.js) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **UVX**: For Python-based servers (requires Python and `pip install uvx`) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Integrating mCP Servers with Clients

#### Claude Desktop
Claude Desktop supports mCP, allowing users to configure and use mCP servers directly <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
1.  Access settings: `File` -> `Settings` -> `Developer tab` -> `Edit your configuration` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
2.  Edit the JSON configuration file (e.g., in VS Code) to include your mCP servers <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
3.  Once configured, tools provided by these servers become available via the "Hammer icon" in the UI, complete with descriptions <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

An example of usage involves asking Claude Desktop to query for Pydantic AI docs using the Brave search server and then visiting the page using the Stagehand `navigate` tool <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

#### [[implementing_mcp_servers_in_ai_agent_systems|n8n Integration]]
n8n, a workflow automation tool, can integrate mCP servers directly into its AI agents using a community node <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
1.  **Installation**: Install the `nn-no-mcp` community node from n8n settings: `Settings` (bottom left) -> `Community nodes` -> `Install` -> search for `nn-no-mcp` <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
2.  **Configuration**: Within an mCP node in n8n, create credentials for each mCP server. This involves defining the main command (e.g., `npx`), arguments, and environment variables <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
3.  **Usage**: Once set up, you can list tools provided by the mCP server or execute specific tools. For example, an agent can use a Brave mCP server to search the web for Elon Musk's net worth <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

#### Python AI Agents (e.g., Pydantic AI)
Custom mCP clients can be created in Python to leverage mCP servers within AI agents built with frameworks like Pydantic AI <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
1.  **Python SDK**: Use the mCP Python SDK documentation for guidance <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
2.  **Client Session**: Import necessary components from mCP, define the server to connect to, and create a client session <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
3.  **Tool Integration**: A helper function can gather a list of tools from the mCP server via the client session, package them as Pydantic AI tool definitions (including descriptions and arguments), and then feed these directly to the Pydantic AI agent <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This process is similar to how tools are defined directly in code <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
4.  **Example**: A Python script can load a file system server via mCP, allowing the agent to list files in a directory using the mCP server's tools <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. This approach is also applicable to frameworks like Crew AI or the OpenAI SDK <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

## [[building_mcp_servers|Building Your Own mCP Server]]

To build custom mCP servers:
*   **Documentation**: Refer to the "for Server developers" section in the official mCP documentation, which provides examples like building a simple weather mCP server <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **SDKs**: Explore SDKs for specific languages (e.g., the Python SDK on GitHub) to find examples for the language of interest <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **[[mcp_servers_for_ai_coding|AI Coding Assistance]]**: Use LLMs in AI IDEs (like Windsurf or Cursor) to assist in building mCP servers <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. You can copy the entire mCP documentation in Markdown format (`llm.text`) and paste it into the IDE or reference it directly <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This allows the AI to generate well-coded mCP servers based on the documentation, complete with tool definitions, API endpoint usage, and even configuration examples for clients like Claude Desktop <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

Building custom servers is beneficial for services not yet available on the official GitHub repository, or for combining different tools and working with local LLMs <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.

## Future of the Model Context Protocol
Anthropic has an ambitious roadmap for mCP, aiming to make it the leading standardization for agents <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. Key future developments include:
*   **Remote mCP Support**: Running servers in the cloud and allowing clients to connect to them remotely <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   **Authentication and Authorization**: Enhancing security and access control <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Monetization**: Potential for monetizing mCP servers <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **Advanced Agent Support**: Incorporating complex agentic workflows, direct support for sub-agents as mCP servers, and hierarchical agent systems <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

These advancements aim to make powerful AI concepts and workflows more accessible, especially to less technical users, and foster easier sharing of tools and ideas <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. While the future of standardization is uncertain, getting acquainted with mCP offers a higher-level understanding vital for developers and builders in the AI space <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.