---
title: Standardization in AI tool usage
videoId: v_6EXt6T83I
---

From: [[colemedin]] <br/> 

The Model Context Protocol (MCP) is a significant development in the AI space, designed to standardize how tools are provided to large language models (LLMs) for interacting with services <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Developed by Anthropic, MCP aims to boost productivity and build better [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Unlike fleeting trends in AI, MCP is seen as a "kindling log" that will continue to grow in importance, having been around since November of last year but gaining wider recognition for its utility <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Leveraging MCP provides an "unfair advantage" for enhancing LLMs and [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## What is MCP?

MCP can be thought of as the "USBC ports for AI applications," standardizing how tools are connected to LLMs, similar to how USB standardizes device connections to peripherals <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Another analogy describes MCP as "API endpoints for our [[Frameworks and tools for AI agent development | AI agents]]" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Just as companies use APIs to expose backend services, MCP exposes tools for [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## The Need for Standardization

Before MCP, developing [[Frameworks and tools for AI agent development | AI agents]] involved creating individual functions as tools (e.g., for file creation, Git commits, database table listing) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. While powerful, this approach led to significant challenges:
*   **Lack of Reusability**: Tools created for one [[Frameworks and tools for AI agent development | AI agent]] framework (like Pydantic AI) could not easily be reused with others (like n8n, Claude Desktop, Windsurf, or Cursor), leading to redundant code <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Difficulty in Sharing**: Packaging and sharing these individual functions between different developers was not straightforward <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This situation highlighted the critical need for standardization – a structured way to package tools for individual services, allowing for easy sharing and reuse across different applications and [[Frameworks and tools for AI agent development | AI agent]] frameworks <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## How MCP Works

MCP provides a standardized middleman layer through "MCP servers" that expose services and their associated tools to [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This ensures that regardless of the framework used for building the agent (e.g., n8n, Cursor, Pydantic AI), the tools can be consumed in the same way <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

[!IMPORTANT]
MCP does not fundamentally change how LLMs use tools <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Tools are still communicated to the LLM as part of the prompt, allowing the agent to decide when and how to call them <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The core innovation of MCP is making these tools more accessible and easier to reuse and package for sharing <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## MCP Clients and Servers

### MCP Clients
Many AI IDEs and frameworks support MCP, including:
*   AI IDEs: Klein, Rhyme, Windsurf, Cursor, Claude Desktop <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>
*   Applications: n8n <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>
*   Frameworks: Pydantic AI, Crew AI, LangChain <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

These clients allow users to configure and integrate MCP servers to expand the capabilities of their [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### MCP Servers
A wide array of MCP servers are available, either officially developed by Anthropic, by companies integrating their services, or by the community <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Examples include:
*   **Web Search**: Brave Search (for LLMs that don't have built-in web search like Claude or local LLMs) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>
*   **Database Management**: Redis, PostgreSQL, [[Open Source AI Tools for Database Management | Supabase]] <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
*   **Browser Automation/Web Scraping**: Browserbase's Stagehand (enabling agents to crawl websites and extract information using natural language) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
*   **Retrieval Augmented Generation (RAG)**: Qdrant, Chroma Vector Database (eliminating the need for custom RAG tool implementations) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>
*   **File System**: Manage files locally <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>
*   **Memory**: Basic implementations for agent memory <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>

MCP servers can be built with JavaScript or Python and run using tools like Docker, NPX (for JavaScript), or UVX (for Python) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Building with MCP

Users can create their own MCP servers and clients to tailor [[Creating tools and dependencies for AI agents | AI agent]] capabilities.

### Creating Custom MCP Servers
The official MCP documentation provides guides for server development, including simple examples like a weather server <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. SDKs are available for different languages, like Python, with examples on GitHub <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

[[Effective use of AI coding assistants | AI coding assistants]] like Claude in Windsurf can be used to generate MCP server code by providing the MCP documentation as context <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This allows for rapid development of custom servers that might combine different tools or work with local LLMs <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### Integrating MCP with n8n
n8n, a workflow automation tool, supports [[Integration of mCP in AI tools | integrating MCP]] servers through a community-developed node <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. After installing the `nn-node-mcp` community node, users can set up credentials for MCP servers within n8n workflows, defining the command, arguments, and environment variables <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This allows n8n [[Frameworks and tools for AI agent development | AI agents]] to list tools, prompts, and execute tools provided by MCP servers <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. For example, an n8n agent can use a Brave MCP server to search the web, a task an LLM alone might not accomplish <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

### Creating Custom Python Clients
Python developers can create custom MCP clients to use servers within [[Frameworks and tools for AI agent development | AI agents]] built with frameworks like Pydantic AI <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. The Python SDK allows connection to MCP servers and gathering lists of tools as Pydantic AI tool definitions (including descriptions and arguments) <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. These definitions are then fed into the Pydantic AI agent as tools, similar to how tools defined directly in code would be used <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This approach can be adapted for other frameworks like Crew AI or the OpenAI SDK <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

## Future of MCP

While new standardization protocols might emerge, understanding MCP is crucial as it represents a significant step in how tools are integrated with LLMs <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Anthropic has outlined an ambitious [[Future Work and Feature Requests for AI Tools | roadmap for MCP]], aiming to make it a dominant standard for [[Frameworks and tools for AI agent development | AI agents]] <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Key [[Future Work and Feature Requests for AI Tools | future features]] include:
*   **Remote MCP Support**: Hosting servers in the cloud for clients to connect remotely <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   **Authentication and Authorization**: Implementing secure access to MCP servers <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Monetization**: Potentially allowing for the monetization of MCP servers <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
*   **Advanced Agent Support**: Incorporating complex agentic workflows, support for sub-agents as MCP servers, and hierarchical agent systems <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

The goal is to make powerful [[Frameworks and tools for AI agent development | AI agent]] capabilities more accessible to less technical users and facilitate easier sharing of tools and ideas <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.