---
title: Using external knowledge in AI coding
videoId: MBaTuJfICP4
---

From: [[colemedin]] <br/> 

The workflow for [[using_ai_coding_assistance | coding anything with AI]] has evolved with new MCP (Multi-Modal Compute Platform) servers. A current efficient workflow revolves around three core MCP server types, which can transform any [[effective_use_of_ai_coding_assistants | AI coding workflow]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These servers are used to build applications effectively <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

The process for [[using_ai_coding_assistance | AI coding assistance]] to build anything has been updated, particularly in the section on using MCP servers <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. While there are other useful servers, these three are consistently used regardless of what is being built <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For each category, there are multiple options, though only one primary recommendation is focused on <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Core MCP Server Categories

### 1. External Knowledge / RAG Knowledge Base Servers

These servers are crucial for bringing [[external_knowledge_issues_in_ai_coding_tools | external knowledge]] into your [[using_ai_coding_assistance | AI coding assistant]], especially for things like library and tool documentation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

*   **Problem**: Many common libraries and tools (e.g., Superbase, Pyantic AI) are not well-known by [[limitations_of_current_ai_coding_assistants | AI coding assistants]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Even built-in documentation support in AI IDEs like Windsurf and Cursor doesn't always work optimally <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Solution**: Use an MCP server as a RAG (Retrieval Augmented Generation) knowledge base for the AI coder <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Recommendations**:
    *   **Crawl for AI**: A free, open-source server that allows crawling any website or documentation and using it as a RAG MCP server <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Knowledge is stored in a private Superbase instance, giving users their own managed knowledge base <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   **[[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | Context 7]]**: Another good option that comes out-of-the-box with thousands of libraries already ingested in its knowledge base <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### 2. Database Management Servers

These servers help the AI coding assistant manage databases, allowing it to create new functions, tables, and other database elements as part of a project <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   **Recommendations**:
    *   **Superbase MCP server**: Can create tables, list projects, and write almost any SQL query using natural language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This allows the AI to build all necessary tables as part of the application development process <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   **Neon**: A serverless Postgress platform with a similar MCP server <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Future Outlook**: It's anticipated that most databases will eventually have an MCP server for natural language management <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### 3. Web Search Servers

These servers enable the AI to search the web for additional information and supplemental resources <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

*   **Recommendation**:
    *   **Brave MCP server**: Utilizes the Brave API, which is powerful and affordable <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. It offers an AI-centric web search that summarizes information perfectly for LLMs <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Usage**: Typically used in tandem with the RAG MCP server <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. It helps find documentation not included in the knowledge base or community forum posts with examples relevant to the build <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. While the knowledge base provides specific library usage, Brave search can show how different libraries are used together <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

## Configuring MCP Servers

To integrate these MCP servers into your [[using_ai_coding_assistance | AI coding workflows]], detailed instructions are provided for each in the video description <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

*   **Crawl for AI**: The readme outlines installation, project setup, database configuration, and website crawling <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Brave**: Requires creating an API key and following instructions for setup in AI IDEs like Cloud Desktop, Windsurf, or Cursor <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Brave offers a generous free tier <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Superbase**: Requires setting up an access token, with instructions available in the readme <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Superbase also has a very generous free tier <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

The configuration process across different MCP servers is generally very similar <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. In Windsurf, the configuration is accessed via the hammer icon for MCP servers in cascade mode, opening a JSON file <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Similar configurations exist for Cursor, Rue Code, or Claude <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Once configured and saved, refreshing the MCP servers loads all the exposed tools and their descriptions, effectively giving "superpowers" to AI coders <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## Live Build Example: RAG AI Agent

A live demonstration involves building a RAG AI agent using Pyantic AI and Superbase, integrating all three MCP server types <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The agent features a local folder for file ingestion into a Superbase knowledge base and a Streamlit interface for interaction <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Preparation and Prompting Strategy

Before starting the build, several elements are set up according to a full [[effective_use_of_ai_coding_assistants | AI coding assistant process]]:

*   **Windsurf Rules**: Workspace rules are created to provide high-level direction, telling the AI how to leverage planning and task files and how to use the Crawl for AI MCP server <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Planning File**: An overview of the project and desired components is provided, allowing the AI to understand the build without excessively specific prompts <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Task File**: Individual tasks are listed for the agent to complete <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

The prompt instructs the AI to build a simple RAG AI agent with Pyantic AI and Superbase, starting by reading the planning and task files <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

*   **Leveraging Examples**: A powerful technique is to provide examples. For the Streamlit UI, a previous example of a streaming interface made for Pyantic AI agents is referenced, guiding the AI on how to build the new interface <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Similarly, pre-prepared SQL from a previous RAG AI agent project is provided as a reference for the Superbase MCP server to create necessary database tables and enable the RAG extension <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Explicit Server Usage**: The prompt explicitly tells the AI to use:
    *   **Crawl for AI**: To perform RAG queries on pre-crawled documentation for Pyantic AI and Superbase <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
    *   **Brave MCP server**: As a supplemental resource for knowledge base lookups, searching for forum posts and examples <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Timing of Lookups**: It's explicitly stated to use these servers at the very start of the process, ensuring the AI has all documentation before attempting to write code <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### Build Process and Outcome

Upon receiving the prompt, the AI first checks the planning and task documents <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. It then utilizes the MCP servers, performing multiple RAG queries for Pyantic AI documentation and leveraging the Brave MCP server to find examples of Superbase and Pyantic AI integration <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

The AI successfully created a full AI agent, including a readme describing the project structure, numerous files for the RAG pipeline, the agent, and its dependencies <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. The generated code for the Pyantic AI agent, prompts, tools for RAG, and document processing was clean <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. It also generated tests as instructed in the workspace rules <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The user interface was clearly inspired by the provided example <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

While the AI made a new task file and had a couple of bugs to fix (e.g., initially not creating Superbase tables despite being prompted, and issues with document embedding logic not related to Superbase or Pyantic AI), it still did a "really, really good job getting me started" <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. The Superbase and Pyantic AI-related code, including the setup script for the client and functions for inserts and lookups, was perfect <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

The final working application included a Streamlit interface for uploading text or PDF files, which are processed into embeddings and inserted into a Superbase `rag_pages` table <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Users can then interact with the agent, asking questions that leverage the knowledge base <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This entire process, including minor iterations, took less than an hour to create a full application using these three core MCP servers <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>. The AI handled the knowledge lookups, web search, and database setup (including the RAG function under the hood) without manual intervention in Superbase <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.