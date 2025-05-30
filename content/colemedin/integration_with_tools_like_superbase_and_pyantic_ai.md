---
title: Integration with tools like Superbase and Pyantic AI
videoId: ZoyPqXvnnZ8
---

From: [[colemedin]] <br/> 

AI coding assistants often face limitations when integrating with specific tools and frameworks like MCP, [[Superbase integration for AI projects | Supabase]], or Pydantic AI <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A key challenge is providing these assistants with [[creating_tools_and_dependencies_for_ai_agents | RAG capabilities]] for the documentation of these tools <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Context 7

Context 7 is an MCP server that offers a [[creating_tools_and_dependencies_for_ai_agents | RAG knowledge base]] for thousands of frameworks and tools, including [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It provides up-to-date documentation, significantly reducing hallucinations when coding with tools like [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Users can simulate how an AI coding assistant would search the [[Superbase integration for AI projects | Supabase]] documentation for terms like "authentication" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

However, Context 7 has limitations:
*   **Overwhelming Knowledge Base** It offers documentation for over 8,000 libraries, but users typically only care about a small subset. This can lead to AI assistants leveraging the wrong documentation and hallucinating <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Users often prefer a private knowledge base limited to their specific tech stack <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Lack of Privacy** It does not support including private GitHub repositories or other private data as part of its knowledge base <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Not Fully Open-Source** While its MCP server appears open-source, the core logic of Context 7, including scraping and [[creating_tools_and_dependencies_for_ai_agents | RAG]] functionality, relies on a private API endpoint. This suggests future monetization and a lack of true open-source transparency <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Crawl for AI: An Open-Source Alternative

To address the limitations of Context 7, a new open-source "crawl for AI" [[creating_tools_and_dependencies_for_ai_agents | RAG MCP server]] has been introduced <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This server allows users to:
*   Scrape any website <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Build their own private knowledge base <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Leverage this knowledge instantly in any AI coding assistant or AI agent <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Potentially use local LLMs and self-hosted [[using_supabase_as_a_vector_database_for_ai_agents | Supabase]] for an entirely private and local setup <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Demonstration: Building an AI Agent with Pydantic AI and Mem Zero

The "crawl for AI" server was demonstrated by [[building_a_local_ai_package_with_supabase | building an AI package]] using Pydantic AI as the agent framework and Mem Zero for long-term memory <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

1.  **Populating the Knowledge Base**:
    *   The [[Superbase integration for AI projects | Supabase]] knowledge base was initially empty <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   The documentation for Pydantic AI (from an `llm-text.fold` URL) was copied and fed to the AI coding assistant via a `crawl` command <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   The server then scraped, embedded, and stored 288,000 characters across 67 chunks into [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   Next, the Mem Zero sitemap was crawled, which involved reading the sitemap and dynamically visiting each URL <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The server handles various URL types, including `llm-text.ext`, sitemaps, and recursive scrapes from base URLs <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   The scraped content from Mem Zero was inserted in batches into the [[Superbase integration for AI projects | Supabase]] database <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   Each chunk stored in [[Superbase integration for AI projects | Supabase]] includes metadata, such as the source, allowing for [[creating_tools_and_dependencies_for_ai_agents | RAG]] searches filtered by specific tools <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

2.  **Developing the Agent**:
    *   With the knowledge base established in [[Superbase integration for AI projects | Supabase]], the AI coding assistant (Windsurf was used in the demo) was prompted to [[creating_tools_and_dependencies_for_ai_agents | build]] an agent <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   The assistant leveraged the `crawlforai` MCP server to retrieve documentation for Pydantic AI and Mem Zero <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   It performed [[creating_tools_and_dependencies_for_ai_agents | RAG searches]] for "Pydantic AI agent creation and setup" and then for Mem Zero <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   The AI successfully structured a full agent using the documentation, demonstrating a detailed understanding of both Pydantic AI for agent definition and tool setup, and Mem Zero for memory implementation <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. It even implemented a switch for cloud vs. self-hosted Mem Zero versions <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   The server manages both crawling and [[creating_tools_and_dependencies_for_ai_agents | RAG]] lookups <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Features and Vision for Crawl for AI

The `crawl for AI` server is seen as a proof of concept for the direction of Archon, an open-source AI agent builder, aiming to transform it into a general "knowledge engine" for AI agents and coding assistants <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

Planned improvements include:
*   **Support for Multiple Embedding Models** Allowing use of different embedding models like Gemini or local models via Olama for fully local operations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Advanced [[creating_tools_and_dependencies_for_ai_agents | RAG]] Strategies** Implementing techniques such as contextual retrieval, late chunking, or [[integration_of_nocode_tools_with_local_ai_agents | agentic RAG]] for more robust knowledge lookups <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Better Chunking Strategies** Improving how scraped content is chunked for storage in [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Enhanced Performance** Making crawling even faster to achieve near-instant [[creating_tools_and_dependencies_for_ai_agents | RAG]] irrespective of the tool or framework <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

### Server Mechanics and Setup

The server exposes four primary tools to the AI IDE <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>:
1.  **`crawl`**: Crawls a single URL and stores its content in [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
2.  **`smart_crawl_URL`**: Handles various URL types (sitemap, `llm's.ext`, recursive web pages) and inserts content in batches <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
3.  **`get_available_sources`**: Returns a list of available documentation sources in the knowledge base (e.g., Pydantic AI docs, Mem Zero docs) <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
4.  **`perform_rag_query`**: Performs a [[creating_tools_and_dependencies_for_ai_agents | RAG lookup]] based on a query, with optional source filtering <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

### Getting Started

To run the `crawl for AI` MCP server:
*   **Prerequisites**: Docker or Python, [[Superbase integration for AI projects | Supabase]] (local or cloud), and an OpenAI API key <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   **Installation**: Clone the GitHub repository <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. Docker is recommended for ease of setup <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   **Database Setup**: A SQL script (`crawl_pages.sql`) is provided to create the necessary `crawled_pages` table and `match_crawled_pages` function in [[Superbase integration for AI projects | Supabase]] <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.
*   **Environment Variables**: Configure `.env` file with `OPENAI_API_KEY`, [[Superbase integration for AI projects | Supabase]] credentials, and MCP transport layer settings (SSE is default on port 8051) <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.
*   **Running the Server**: Execute the appropriate Docker or Python command <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Hooking into AI Coding Assistants/Agents**: Configure the MCP server URL (e.g., `http://localhost:8051/sse` for SSE transport) in clients like Windsurf or Cursor <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. It can also be integrated with tools like N8N as a client <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.

This open-source server allows for creation of an expert AI agent on any website, using it as a knowledge backbone for e-commerce, company documentation, or community platforms <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.