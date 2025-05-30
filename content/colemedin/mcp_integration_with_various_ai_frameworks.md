---
title: mCP integration with various AI frameworks
videoId: v_6EXt6T83I
---

From: [[colemedin]] <br/> 

The Model Context Protocol (mCP) is a significant development in the AI space, designed by Anthropic to standardize how tools are provided to Large Language Models (LLMs) for interacting with various services <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is described as the "USBC ports for AI applications," standardizing the connection of tools to LLMs similarly to how USB standardizes device connections <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Another analogy is that mCP serves as API endpoints for AI agents, exposing tools for their use <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Need for Standardization

Before mCP, AI agents (built with frameworks like [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]], CrewAI, or n8n) required developers to create individual functions as tools (e.g., to create a file, make a Git commit, or list database tables) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. While powerful for allowing agents to reason and act, this approach led to significant challenges in tool reusability <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. If an agent was built with one framework and later needed to be adapted for another (e.g., from [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] to n8n), or if tools needed to be used in different AI IDEs like Claude Desktop or Windsurf, developers often had to rewrite much of the functionality <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This resulted in redundant code development and difficulty sharing tools as neat packages between individuals and different frameworks <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

## How mCP Provides Standardization

mCP addresses these issues by providing a standardized way to package and share tools <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Instead of defining individual functions, mCP uses "mCP servers" to expose services and their associated tools to AI agents <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. These servers act as a middleman, standardizing how tools are presented to the agent, regardless of the framework or application being used (e.g., n8n, Cursor, [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]]) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

It is important to note that mCP does not fundamentally change how AI agents use tools; it merely standardizes their accessibility and reusability <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. The tools exposed by mCP servers are still provided as part of the prompt to the LLM, allowing the agent to decide when and how to call them <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This standardization makes it easier to create packages of tools and share them effectively <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## mCP Client Support

The [[integration_of_mcp_in_ai_tools | integration of mCP in AI tools]] is rapidly expanding across various platforms. Many AI IDEs, applications, and frameworks now support the Model Context Protocol <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Examples of supported clients include:

*   **AI IDEs**: Klein, Rin, Windsurf, Cursor <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>
*   **Applications**: Claude Desktop, n8n <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
*   **Frameworks**: [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]], CrewAI, LangChain <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

While the primary focus of mCP is tool standardization, it also supports other features like exposing real-time data resources, sharing prompt templates, and enabling LLMs to request completions as a tool <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. However, these experimental features are not yet widely supported across most clients <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

## Available mCP Servers

A wide array of mCP servers are already available for use, developed by Anthropic, integrated companies, and the open-source community <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. These servers allow AI agents to interact with various services and databases:

*   **Web Search**: Brave Search mCP server can provide web search capabilities to LLMs like Claude or local LLMs that lack built-in search <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Databases**: Servers are available for managing Redis, PostgreSQL, and Supabase databases <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Browser Automation**: Browserbase's Stagehand offers a headless browser service as an mCP server, enabling AI agents to crawl websites and extract specific information using natural language <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Retrieval Augmented Generation (RAG)**: Qdrant, a vector database, offers an mCP server that allows for RAG without needing to implement custom RAG tools <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Vector Databases**: The Chroma Vector Database also has an mCP server <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

mCP servers can be built with different languages, primarily JavaScript or Python, and run using tools like Docker, NPX (for JavaScript), or Uvicorn/uvx (for Python) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Building with mCP

Developers can create their own mCP servers to package custom tools or build custom mCP clients to leverage existing mCP servers within their AI agents <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

### Creating Custom mCP Servers

Documentation and SDKs are available for building mCP servers <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. For Python mCP servers, specific SDK documentation on GitHub provides examples <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. AI coding assistants, such as Claude within AI IDEs like Windsurf, can also assist in generating mCP server code by referencing the mCP documentation <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This allows for rapid development of servers for services not yet available as mCP servers or for combining different tools <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.

### [[integrating_mcp_with_ai_agents | Integrating MCP with AI Agents]]

#### n8n Integration
[[integrating_mcp_with_ai_agents | Integrating MCP with AI agents]] built in n8n is possible through a community node <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This node can be installed via the n8n community nodes tab <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. Once installed, users can configure mCP servers by defining commands, arguments, and environment variables within the mCP nodes <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. These nodes allow agents to list available tools, list prompts, and execute tools exposed by the mCP server <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

#### Python and [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] Client Integration
Custom mCP clients can be created in Python to be used within AI agents built with frameworks like [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. The Python SDK documentation offers guidance for this <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

The process typically involves:
1.  Importing necessary components from the mCP library <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
2.  Defining the mCP server to connect to <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.
3.  Creating a client session to interact with the server <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
4.  Using a helper function to gather a list of tools from the mCP server <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
5.  Packaging these tools as [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] tool definitions (including descriptions and arguments) <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
6.  Feeding these definitions directly into the [[building_ai_agents_with_pantic_ai_and_mcp | Pydantic AI]] agent as its available tools, similar to how tools defined directly in code would be used <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

This approach is highly adaptable and can be extended to other frameworks like CrewAI or the OpenAI SDK <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

## The Future of mCP

Anthropic's roadmap for mCP suggests a strong vision for its future as a dominant standardization protocol for AI agents <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Future developments include:

*   **Remote mCP Support**: Allowing mCP servers to run in the cloud, with clients connecting remotely <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   **Authentication and Authorization**: Implementing robust security measures <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Monetization**: Exploring possibilities for monetizing mCP servers <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
*   **Advanced Agent Support**: Enhancing support for complex agentic workflows, including sub-agents directly supported as mCP servers and hierarchical agent systems <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

The continued development of mCP aims to make powerful AI concepts and agentic workflows more accessible, particularly for less technical users, by simplifying the sharing of tools and ideas <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This focus on standardization is crucial for the ongoing evolution of AI development <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.