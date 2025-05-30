---
title: Building a new RAG MCP server
videoId: ZoyPqXvnnZ8
---

From: [[colemedin]] <br/> 

AI coding assistants are powerful tools for building anything, but they are limited by their compatibility with specific tools and frameworks like MCP, Superbase, or Pyantic AI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To overcome this, there's a need for RAG (Retrieval Augmented Generation) capabilities to provide AI assistants with up-to-date documentation for various tools and frameworks <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Limitations of Context 7

Context 7, an existing MCP server, offers a RAG knowledge base for thousands of frameworks and tools, including Superbase and MCP <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It provides an [[mcp_servers_for_ai_coding|MCP server for AI coding]] that can be attached to AI coding assistants and a user interface to simulate searches, reducing hallucinations by providing up-to-date documentation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For example, it can provide tokens, examples, and code for Superbase authentication to an AI assistant <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

However, Context 7 has significant drawbacks:
*   **Overwhelming Knowledge Base**: It offers documentation for over 8,000 libraries, but users typically only care about a small subset. This can lead to AI coding assistants leveraging the wrong documentation and hallucinating <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Users often prefer a more private and limited knowledge base tailored to their specific tech stack <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Lack of Private Repositories**: It does not allow the inclusion of private GitHub repositories as part of the knowledge base, forcing users into an open, collective knowledge base <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Limited Open-Source Nature**: While the Context 7 [[mcp_servers_for_ai_coding|MCP server]] itself is open-source, its core logic and the product as a whole are not <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. The server's 68 lines of code primarily hit a private endpoint that handles the complex scraping and RAG operations <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This private API is likely to be monetized in the future, meaning it's not truly open-source and will eventually require payment <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

These [[challenges_and_solutions_in_mcp_server_development|challenges and solutions in MCP server development]] highlight the need for a more robust, private, and open-source solution.

## Introducing Crawl for AI RAG MCP Server

To address these limitations, a new mission was undertaken to [[building_mcp_servers|build MCP servers]] similar to Context 7, but completely open-source and self-hostable <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This led to the development of the [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### Key Features and Capabilities
The [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] allows users to:
*   Scrape any website and bring it into their own private knowledge base <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Instantly leverage this private knowledge base in any AI coding assistant or AI agent <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Handle different types of URLs for crawling, including:
    *   Single pages <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
    *   Smart crawls from sitemaps (`sitemap.xml`) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, LLM-structured text files (`llm-text.fold`) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, or recursive scraping from a base URL <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   Perform RAG lookups and manage crawling, all within one [[mcp_servers_for_ai_coding|MCP server]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Store information in Superbase, allowing for metadata filtering to separate RAG searches by specific tools or frameworks <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Demonstration: Building an AI Agent with Pyantic AI and Mem Zero
A demonstration using Windsurf illustrated the process of [[building_and_using_mcp_servers|building and using MCP servers]] like Crawl for AI.
1.  **Objective**: Build an AI agent using Pyantic AI as the framework and Mem Zero for long-term memory <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Initial State**: The Superbase knowledge base was initially empty <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Crawling Pyantic AI Documentation**: The `llm-text.fold` documentation for Pyantic AI was crawled using the `crawl` tool in the [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The server, running in a Docker container, scraped and embedded over 288,000 characters into 67 chunks in Superbase almost instantly <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
4.  **Crawling Mem Zero Documentation**: The sitemap for Mem Zero was then crawled, allowing the server to dynamically visit each URL <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This process took slightly longer due to fetching multiple URLs, but it collected markdown files and inserted them in batches into Superbase <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
5.  **Leveraging the Knowledge Base**: With both Pyantic AI and Mem Zero documentation in Superbase, the AI coding assistant (Windsurf) was instructed to use the [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] for RAG. It performed searches for "Pantic AI agent creation and setup" and "Mem Zero," retrieving relevant chunks <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
6.  **Agent Construction**: The AI agent successfully built a full agent structure, including imports, agent definition, tool setup, and a system prompt that reflected a deep understanding of Pyantic AI documentation <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. For Mem Zero, it even implemented a flexible memory setup to leverage both cloud and self-hosted versions via environment variables <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This demonstrated the AI's ability to understand documentation at a detailed level <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

This demonstration confirmed the server's ability to leverage a privately created knowledge base <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. The entire Superbase setup was self-hosted locally, and there are plans to use Olama for local embedding models to make the entire process 100% private and local <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Advantages over Existing Solutions
The [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] aims to be more powerful than native documentation search features in platforms like Cursor and Windsurf, offering a private knowledge base that can be built up using local LLMs <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This provides greater flexibility, privacy, and power for AI agents and coding assistants <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

***

> [!NOTE]
> An intermission introduces **Lindy**, an AI platform with a workflow builder similar to N8N, offering more integrations and a revolutionary "agent swarms" feature <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Agent swarms allow dedicated agents to run in parallel for each task, such as processing hundreds of leads simultaneously <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. Lindy has partnered with Pipere (5,000+ integrations) and Appify (4,000+ web scrapers) to expand automation possibilities <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. Users can get 400 free credits to start <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

***

## [[Future improvements and vision for the RAG MCP server|Future Improvements and Vision for the RAG MCP Server]]

The [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] serves as a proof of concept for the future direction of Archon, an open-source AI agent builder <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The vision is to transform Archon from an agent builder into a general knowledge engine to power agents and AI coding assistants, providing more flexibility and avoiding overlap with existing coding assistant workflows <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

Specific [[future_improvements_and_vision_for_the_rag_mcp_server|future improvements and vision for the RAG MCP server]] include:
*   **Embedding Models**: Support for different embedding models like Gemini, or local models like Olama for fully local operations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Advanced RAG Strategies**: Implementation of advanced RAG strategies such as contextual retrieval (by Anthropic), late chunking, or agentic RAG for more robust knowledge lookups <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Better Chunking Strategies**: Improving the current chunking strategy to keep paragraphs and sentences together more effectively <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Enhanced Performance**: Making the server even faster, especially for crawling dozens or hundreds of pages, to achieve a seamless, "instant RAG" experience <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

## [[Setting up and using MCP servers|Setting Up and Using MCP Servers]]: Technical Details and Tools

The [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] exposes four simple tools to AI IDEs <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>:

1.  `crawl_single_page`: Crawls a single URL and stores its content in Superbase <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
2.  `smart_crawl_url`: Accepts a URL (sitemap, LLM-text file, or regular web page) and intelligently crawls all necessary pages, inserting them in batches <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
3.  `get_available_sources`: Returns a list of available sources (e.g., Pyantic AI docs, Mem Zero docs) in the knowledge base, enabling metadata filtering for RAG searches <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
4.  `perform_rag_query`: Performs a RAG search on the knowledge base using a query and optionally filters by a specific source <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

These tools are described within the [[mcp_servers_for_ai_coding|MCP server]] code to guide the AI coding assistant on when and how to use them <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

### Prerequisites
To [[setting_up_and_using_mcp_servers|set up and use MCP servers]] like Crawl for AI, you will need <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>:
*   Docker or Python (for running the server) <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   Superbase (for the database, can be local or cloud-hosted) <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   OpenAI API key (with future support for Gemini and Olama) <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.

### Installation and Setup
1.  **Clone Repository**: Clone the [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] GitHub repository <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.
2.  **Run with Docker (Recommended)**:
    *   Build the container using the provided command <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. This handles Python package installation and Playwright configuration for crawling <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
3.  **Run with Python (Alternative)**:
    *   Install UV and activate environment <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
    *   Install all packages <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
    *   Run `crawl_for_ai setup` to install Playwright and configure <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.
4.  **Database Setup**:
    *   Copy the SQL script from `crawl_pages.sql` in the repository <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.
    *   Paste and run it in the Superbase SQL editor <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. This creates the `crawled_pages` table and the `match_crawled_pages` function for RAG lookups <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. This demonstrates [[managing_databases_with_mcp_servers|managing databases with MCP servers]].
5.  **Configure Environment Variables**:
    *   Create a `.env` file (using `env.example` as a guide) <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.
    *   Set `MCP_TRANSPORT_LAYER` (default SSE), `MCP_PORT` (default 8051), `OPENAI_API_KEY`, and Superbase credentials <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

### Execution and Client Integration
Once configured, run the server using the appropriate Docker or Python command <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. The server will run on port 8051 by default, making it ready to receive requests <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>. Logs can be viewed in Docker Desktop to monitor requests <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

#### Connecting to AI Coding Assistants
To hook the server into AI coding assistants like Windsurf or Cursor <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>:
*   Configure the JSON for the [[mcp_servers_for_ai_coding|MCP server]] in the client's settings (e.g., Windsurf's hammer icon > configure) <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.
*   The server URL will typically be `http://localhost:8051/sse` <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. Note that Windsurf requires `serverUrl` instead of `url` for the JSON key <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
*   Save the configuration and refresh <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

#### Connecting to Other Agents (e.g., N8N)
The server can also be used with other agent frameworks like N8N <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>. If N8N is running in a Docker container, the endpoint must reference the host machine's IP, using `host.docker.internal` instead of `localhost` <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. This allows N8N to use the [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] as a tool for tasks like retrieving available sources or performing RAG queries <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

## Conclusion

The [[opensource_crawl_for_ai_rag_mcp_server|Crawl for AI RAG MCP server]] offers a powerful, private, and flexible solution for providing RAG capabilities to AI coding assistants and agents <a class="yt-timestamp" data-t="00:26:59">[00:26:59]</a>. While currently focused on documentation for tools and frameworks, its potential extends to being a knowledge backbone for any AI agent across various websites, such as e-commerce stores, company documentation, or community platforms <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.