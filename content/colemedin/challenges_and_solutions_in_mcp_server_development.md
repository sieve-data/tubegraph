---
title: Challenges and solutions in MCP server development
videoId: lbyPJqCI-tw
---

From: [[colemedin]] <br/> 

Anthropic's Model Context Protocol (MCP) is a significant standard for connecting Large Language Models (LLMs) to various services such as Gmail, Slack, GitHub, and web search <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It enables LLMs to gain higher-level capabilities like long-term memory <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. While many [[setting_up_and_using_mcp_servers | MCP servers]] already exist, the true power lies in [[building_mcp_servers | building your own]] to connect custom agents to any desired service using MCP's simplicity and power <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

## Why [[building_mcp_servers | Build Your Own]] MCP Server?

Although existing [[setting_up_and_using_mcp_servers | MCP servers]] are useful, they come with limitations <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. For instance, the way an existing server interacts with a service like Brave Search might not align with a developer's specific needs <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. Furthermore, there might not be an existing [[setting_up_and_using_mcp_servers | MCP server]] for particular services or capabilities required <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. This necessitates [[building_mcp_servers | building custom MCP servers]] to achieve full customization and control over how agents interact with services <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.

## Key Resources for [[building_and_using_mcp_servers | Building and Using MCP Servers]]

To learn about MCP and [[building_mcp_servers | build custom MCP servers]], three main resources are recommended:
*   **Official MCP Documentation:** Provides a general understanding of MCP, including guides for [[building_mcp_servers | building servers]] and clients <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>, <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **List of Existing [[setting_up_and_using_mcp_servers | MCP Servers]] on GitHub:** Serves as a reference point, offering examples for [[building_mcp_servers | custom servers]] and a repository of useful existing servers <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>, <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
*   **Anthropic's Official GitHub Repo for the MCP Python SDK:** Essential for [[building_mcp_servers | MCP servers]] using Python, which is considered the simplest and most used language for this purpose <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>, <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

## Challenges in [[building_mcp_servers | MCP Server Development]]

Despite the resources, several challenges can arise during [[building_mcp_servers | MCP server development]]:

*   **AI Coding Assistant Limitations:** While AI coding assistants can generate server code, it may not always work perfectly from the start <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>, <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>, <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.
*   **Suboptimal Existing Servers:** Many existing [[setting_up_and_using_mcp_servers | MCP servers]] are not built with best practices.
    *   **Poor Client Instantiation:** Some servers, like Chromobb, have less than ideal client instantiation methods <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
    *   **Lack of MCP Understanding:** Even official or prominent servers, such as Mem's own [[setting_up_and_using_mcp_servers | MCP server]], might not fully grasp how MCP operates, leading to issues like supporting only one transport protocol or duplicating tool descriptions <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>, <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.
    *   **Monetization Constraints:** Some servers might require API keys or paid services, restricting free use <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.
*   **Understanding Transport Protocols:** The most technical and difficult aspect of MCP is understanding the underlying communication methods between clients and servers: Standard IO and Server-Sent Events (SSE) <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>, <a class="yt-timestamp" data-t="21:52:00">[21:52:00]</a>.
    *   **Standard IO:** Ideal for local processes where the server and client run on the same machine, with the client managing the server as a subprocess <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.
    *   **SSE:** More akin to HTTP, allowing connections over the internet, crucial for remotely hosted [[setting_up_and_using_mcp_servers | MCP servers]] <a class="yt-timestamp" data-t="22:31:00">[22:31:00]</a>. Some clients, like N8N, only support SSE <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>. Most [[setting_up_and_using_mcp_servers | MCP servers]] may only work with one transport type, limiting their adaptability <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>.

## Solutions and Best Practices for [[building_mcp_servers | MCP Server Development]]

To overcome these challenges, a structured approach with best practices is crucial:

*   **Utilize a Robust Template:** A well-prepared template incorporating best practices can save significant development time and effort <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>, <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   **Guide AI Coding Assistants:** When using AI coding assistants, provide the template as an example alongside official documentation. This helps the AI better understand how to [[building_mcp_servers | build MCP servers]] correctly <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>, <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
*   **Define Server Lifespan:** Implement a lifespan for the [[building_mcp_servers | MCP server]] to manage client connections (e.g., database connections) throughout its lifecycle, ensuring a single instance and proper cleanup at shutdown <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>, <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. This concept is vital but often missing in other [[setting_up_and_using_mcp_servers | MCP servers]] <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.
*   **Descriptive Tool Docstrings:** Ensure that docstrings for tools are highly descriptive, as this text is provided to the LLM to inform it when and how to use specific tools in the server <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>, <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.
*   **Support Multiple Transport Protocols:** Design the [[building_mcp_servers | server]] to support both SSE and Standard IO <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>. This adaptability is critical, allowing connections from various clients and catering to both local and remote hosting scenarios <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>. The choice of transport can be made via an environment variable <a class="yt-timestamp" data-t="23:21:00">[23:21:00]</a>.
*   **Utilize Docker for Deployment:** Using Docker is recommended for [[building_mcp_servers | MCP servers]] as it standardizes the environment and simplifies deployment <a class="yt-timestamp" data-t="24:22:00">[24:22:00]</a>.
*   **Refer to the README:** A comprehensive `README` file in the repository should detail installation instructions (Python and Docker), environment variable setup, and commands for running the server with different transport types (SSE and Standard IO) for various clients <a class="yt-timestamp" data-t="24:13:00">[24:13:00]</a>, <a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>.

By adhering to these best practices, developers can successfully [[building_a_new_rag_mcp_server | build a new RAG MCP server]] and custom [[mcp_servers_for_ai_coding | MCP servers for AI coding]] that effectively connect AI agents to desired services, providing full control and customization <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>. This approach makes it easy to integrate new capabilities like long-term memory via [[managing_databases_with_mcp_servers | Mem Zero]] <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>, <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

> [!NOTE]
> The speaker plans to release more content on [[future_improvements_and_vision_for_the_rag_mcp_server | future improvements and vision for the RAG MCP server]], specific use cases, and further ways to leverage this powerful protocol for AI agents <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.