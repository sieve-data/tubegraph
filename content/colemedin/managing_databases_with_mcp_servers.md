---
title: Managing databases with MCP servers
videoId: MBaTuJfICP4
---

From: [[colemedin]] <br/> 

When using AI coding assistants for development, a crucial aspect is managing databases. This involves allowing the AI to not only write code but also create and manage database components like functions and tables <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This workflow revolves around core [[musthave_mcp_servers_for_ai_coding | MCP servers]] that can transform any AI coding workflow <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

## Key MCP Servers for Database Management

The primary recommendation for database management is the **Superbase MCP server** <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

### Superbase MCP Server
The Superbase MCP server is a powerful tool for managing databases using natural language <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. It can:
*   Create tables <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   List projects within a Superbase organization <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   Write almost any SQL query <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

This functionality enables the AI coding assistant to build all necessary tables as part of the application development process <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

### Alternatives
Another notable option mentioned is **Neon**, a serverless PostgreSQL platform that offers a similar [[building_mcp_servers | MCP server]] <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. The expectation is that most databases will eventually have their own [[building_mcp_servers | MCP server]] support <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

## Setting Up and Using Database MCP Servers

The process for [[setting_up_and_using_mcp_servers | setting up and using MCP servers]] generally involves:
1.  **Configuration:** Accessing the MCP configuration file (e.g., JSON file in Windsurf) to add individual servers <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
2.  **Authentication:** For Superbase, this requires setting up an access token, with detailed instructions provided in the server's readme <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.
3.  **Free Tier:** Superbase offers a generous free tier that allows users to spin up an instance indefinitely without payment <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.
4.  **Loading Servers:** After configuration, saving and refreshing the settings loads the [[building_mcp_servers | MCP servers]], exposing their available tools and descriptions to the AI coding assistant <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.

## Live Build Example: RAG AI Agent with Pydantic AI and Superbase

In a live demonstration, the Superbase MCP server was used to build a RAG (Retrieval Augmented Generation) AI agent <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. The goal was to create a local folder for file ingestion, automatically ingest documents into a Superbase knowledge base, and provide a Streamlit interface for interaction <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

### Initial Prompting and Iteration
The AI coding assistant was instructed to use the Superbase MCP server to create necessary database tables and ensure the RAG extension was enabled, using an existing SQL example as reference <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.

While the AI initially generated the application, it did not create the database tables as requested in the first prompt <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>. This highlights that AI coding assistants can sometimes be unpredictable, requiring re-prompting <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. Upon re-prompting, the AI successfully used the `apply migration` tool with the provided SQL query to create the tables <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

### Database Structure and Functionality
The created Superbase table, `rag_pages`, included columns for `ID`, `URL`, `chunk_number`, and `embeddings` (used for RAG) <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.

Although minor adjustments were needed for document embedding and ingestion (unrelated to Superbase or Pydantic AI), the Superbase-related code for creating the client, functions for inserts, and lookups was perfect <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. This demonstrates the effectiveness of the [[building_mcp_servers | MCP server]] in building robust database interactions <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>.

The final application allowed users to upload text or PDF files, which were then processed, chunked, and ingested as embeddings into the Superbase database <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>. The agent could then leverage this knowledge base to answer questions <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>. The entire application, including the database setup and an underlying function for RAG, was created with minimal manual intervention, showcasing the power of [[implementing_mcp_servers_in_ai_agent_systems | implementing MCP servers in AI agent systems]] <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.