---
title: Web search with MCP servers
videoId: MBaTuJfICP4
---

From: [[colemedin]] <br/> 

Web search functionality, facilitated by [[building_and_using_mcp_servers | MCP servers]], is a crucial component of modern AI coding workflows <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It allows AI coding assistants to access external, real-time information beyond their pre-trained knowledge bases, enhancing their ability to build applications effectively <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## The Brave MCP Server

One highly recommended [[musthave_mcp_servers_for_ai_coding | must-have MCP server]] for web search is the Brave [[setting_up_and_using_mcp_servers | MCP server]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
It stands out due to its:
*   **Affordability and Power** The Brave API is described as both affordable and very powerful <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. There is a generous free tier available, allowing users to get started without immediate payment <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **AI-Centric Search** It offers a web search experience superior to standard searches found in tools like ChatGBT or Claude <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Its design focuses on summarizing information specifically for AI, pulling data in a format ideal for Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Role in AI Coding Workflows

The Brave [[setting_up_and_using_mcp_servers | MCP server]] is typically used in tandem with a RAG (Retrieval-Augmented Generation) [[opensource_crawl_for_ai_rag_mcp_server | MCP server]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. While the RAG server accesses an existing knowledge base, the Brave server supplements this by searching the broader web for additional resources <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

This dual approach is beneficial for:
*   **Missing Documentation** Finding documentation not included in the existing knowledge base <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Community Resources** Discovering community forum posts or other examples that provide solutions or approaches similar to the desired build <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Inter-library Integration** While a knowledge base might explain how to use a specific library, web search helps understand how to integrate multiple libraries together <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

It's recommended that the AI coding assistant uses these servers at the very start of the process to gather all necessary documentation before writing any code <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Setup and Configuration

Integrating the Brave [[setting_up_and_using_mcp_servers | MCP server]] into your AI coding workflow involves creating an API key and following instructions provided by Brave for setup in your chosen AI IDE, such as Cloud Desktop, [[using_windsurf_and_cursor_with_mcp_servers | Windsurf]], or [[using_windsurf_and_cursor_with_mcp_servers | Cursor]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The configuration process is generally similar across different [[building_and_using_mcp_servers | MCP servers]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Within an AI IDE like [[using_windsurf_and_cursor_with_mcp_servers | Windsurf]], you can configure [[building_and_using_mcp_servers | MCP servers]] by accessing the "hammer" icon for [[building_and_using_mcp_servers | MCP servers]] and then clicking "configure," which opens a JSON file for configuration <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Live Build Example

During a live build of a RAG AI agent with Pydantic AI and [[managing_databases_with_mcp_servers | Superbase]], the Brave [[setting_up_and_using_mcp_servers | MCP server]] was leveraged alongside a RAG [[opensource_crawl_for_ai_rag_mcp_server | MCP server]] <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The AI assistant was explicitly instructed to use the Brave [[setting_up_and_using_mcp_servers | MCP server]] as a supplemental resource for knowledge base lookups, searching for forum posts and examples related to integrating [[managing_databases_with_mcp_servers | Superbase]] and Pydantic AI <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This ensured a comprehensive understanding of the libraries and their combined usage <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.