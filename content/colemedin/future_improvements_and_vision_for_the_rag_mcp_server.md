---
title: Future improvements and vision for the RAG MCP server
videoId: ZoyPqXvnnZ8
---

From: [[colemedin]] <br/> 

This article details the future improvements and overarching vision for the open-source RAG [[building_mcp_servers | MCP server]] introduced, aiming to overcome limitations of existing solutions like Context 7 <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. The goal is to provide a fully private, flexible, and powerful knowledge base for [[mcp_servers_for_ai_coding | AI coding assistants]] and agents <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

## Proof of Concept for Archon

The current [[opensource_crawl_for_ai_rag_mcp_server | RAG MCP server]] serves as a proof of concept for the future direction of Archon, an open-source AI agent builder <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a> <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. The vision is to transform Archon from solely an agent builder into a more general "knowledge engine" that powers AI agents and [[mcp_servers_for_ai_coding | AI coding assistants]] <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This shift aims to offer greater flexibility and complement existing AI coding assistant workflows rather than compete with them <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. The [[opensource_crawl_for_ai_rag_mcp_server | MCP server]] will evolve into a more robust version of this concept within Archon <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

## Specific Technical Improvements

The development roadmap for the [[opensource_crawl_for_ai_rag_mcp_server | MCP server]] includes several key technical enhancements:

*   **Embedding Model Support**
    *   Implementing support for various embedding models, including Gemini <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
    *   Enabling the use of Olama for local embeddings, allowing for an entirely private and local knowledge base setup <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a> <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **[[advanced_rag_implementation_techniques | Advanced RAG Implementation Techniques]]**
    *   Moving beyond traditional RAG lookups to incorporate more sophisticated strategies <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a> <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
    *   Implementing techniques such as contextual retrieval (recently released by Anthropic), late chunking, and agentic RAG <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a> <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **Better Chunking Strategies**
    *   Improving the current chunking strategy, which aims to keep paragraphs and sentences together <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
    *   Developing more effective ways to chunk content to optimize retrieval <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
*   **Enhanced Performance**
    *   Further increasing the crawling speed, even for dozens of pages or sitemaps <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
    *   The goal is to achieve near-instantaneous RAG capabilities, making the underlying crawling and embedding processes feel seamless <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## Broader Applicability

While currently focused on documentation for tools and frameworks, the [[opensource_crawl_for_ai_rag_mcp_server | RAG MCP server]]'s potential extends much further <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. It can serve as a versatile "knowledge backbone" for any AI agent or application, regardless of the website or content <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Examples include:

*   Powering AI agents for e-commerce stores <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
*   Integrating with a company's internal documentation, such as Confluence <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.
*   Creating expert agents for specific communities or datasets <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

This flexibility allows users to build and leverage private knowledge bases for diverse use cases <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.