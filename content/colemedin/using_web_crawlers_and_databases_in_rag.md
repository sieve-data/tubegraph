---
title: Using web crawlers and databases in RAG
videoId: _R-ff4ZMLC8
---

From: [[colemedin]] <br/> 

[[advanced_rag_implementation_techniques | Retrieval Augmented Generation (RAG)]] has become a primary method for incorporating external knowledge into Large Language Models (LLMs) since the advent of generative AI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as a classic approach to transform an LLM into an expert on a specific subject, such as an agent framework or an e-commerce store <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

However, implementing RAG often encounters common pitfalls, including the retrieval of irrelevant text and the LLM ignoring provided content <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While RAG seems logically sound in theory, these issues can cause it to fail in practice <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Significant research is dedicated to improving RAG, with various strategies like reranking, query expansion, and rank normalization being explored <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Among these, [[advanced_rag_implementation_techniques | agentic RAG]] stands out as an effective solution <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Agentic RAG vs. Basic RAG

The core difference between basic RAG and [[advanced_rag_implementation_techniques | agentic RAG]] lies in the agent's ability to reason and interact with its knowledge base <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Basic RAG Process
Basic RAG involves a "one-shot" retrieval process <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>:
1.  **Knowledge Base Creation:** Documents are split into bite-sized chunks to efficiently feed to the LLM <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Vectorization:** These chunks are converted into mathematical representations (vectors) using an embedding model <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **[[creating_and_utilizing_a_vector_database_for_rag | Vector Database Storage]]:** The vectors are stored in a [[choosing_vector_databases_for_rag_applications | vector database]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  **Query Processing:** A user query is also converted into a vector using the same embedding model <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
5.  **Retrieval & Augmentation:** Using vector math, the query is matched to the most relevant documents, which are then given as context to the LLM <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The prompt is expanded to include this relevant context, allowing the LLM to augment its response <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The downside of basic RAG is that the agent cannot reason about the context it receives; it cannot decide if more context is needed or if a different search approach is required <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Agentic RAG Approach
[[advanced_rag_implementation_techniques | Agentic RAG]] addresses this by turning RAG into a set of tools for the agent to interact with <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This enables capabilities like:
*   Searching through different [[choosing_vector_databases_for_rag_applications | vector databases]] <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Reasoning about where to find knowledge based on the user's question <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   Utilizing other tools to search knowledge in alternative ways <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

This approach gives the agent the ability to intelligently explore data, rather than just working with the initial retrieval <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. The LLM acts as a layer that has access to tools and retrieval functions, allowing it to reason about how to search for the answer <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Components of a RAG Solution

A robust [[rag_ai_agent_development | RAG AI agent development]] solution involves several key moving parts:

1.  **Web Crawler:** Used to scrape content from websites <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
2.  **Database:** Stores the scraped data as a knowledge base <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
3.  **AI Agent Framework:** Creates the foundation for the AI agent <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
4.  **User Interface (UI):** Provides a seamless way for users to interact with the agent <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Implementing the Knowledge Base

To build a knowledge base for RAG, a systematic process of data acquisition, processing, and storage is followed.

### 1. Web Scraping with [[crawl_for_ai_web_crawling_framework | Crawl for AI]]
The process begins by using a web crawler like [[crawl_for_ai_web_crawling_framework | Crawl for AI]], an open-source LLM-friendly web crawler, to scrape entire websites rapidly <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For example, the documentation pages for Pydantic AI can be scraped in parallel by fetching all URLs from the sitemap <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This yields the content of every page, typically in Markdown format <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### 2. Processing and Storing Documents
After crawling, the content is processed and stored in a database. This involves:

#### a. Chunking Text
Long web pages are split into smaller, manageable chunks to avoid overwhelming the LLM prompt <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The chunking process is designed to respect structural elements like code blocks, paragraphs, and sentences, ensuring that each chunk contains complete, coherent information <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This prevents splitting in the middle of a sentence or code example, preserving context <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

#### b. Processing Chunks
Each chunk undergoes further processing to prepare it for insertion into the database <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>:
*   **Data Class Definition:** A data class defines the information associated with each processed chunk, including URL, chunk number, title, summary, content, metadata, and embedding <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   **Title and Summary Extraction:** An LLM (e.g., GPT-4o mini) is used to extract a title and summary for each chunk <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This extra context helps the agent reason about when to use a specific piece of knowledge <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. The LLM is instructed to return a specific JSON object format for this <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   **Embedding Creation:** The chunk's content is converted into a vector representation (embedding) using an embedding model (e.g., OpenAI's `text-embedding-3-small` model) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This embedding is crucial for the retrieval aspect of RAG, enabling vector mathematics-based searches <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   **Metadata Creation:** Additional metadata, such as the source (e.g., "Pydantic AI docs") and ingestion time, is attached to each record <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. This allows for specific filtering, enabling a single database table to serve multiple agents by filtering results based on their source <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

#### c. Storing Chunks in Superbase
The processed chunks, complete with their content, embeddings, and metadata, are then inserted into the `site_pages` table in a database like Superbase <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This setup supports not only basic RAG (via embeddings) but also [[advanced_rag_implementation_techniques | agentic RAG]] by allowing the agent to explore knowledge using structured data like URLs, titles, and summaries <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

**Superbase vs. Quadrant for RAG:**
Superbase offers a unified platform for both RAG (vector database) and structured SQL data <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>. This simplifies the architecture by keeping embeddings and metadata in one place <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>. Quadrant, being solely a vector database, is faster for embedding searches <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. For maximum speed, one might use Quadrant for embeddings and Superbase for structured metadata <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>.

### 3. Database Setup
For Superbase, a SQL script is used to set up the `site_pages` table, including row-level security policies <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>. Necessary environment variables, such as the Superbase URL, service role secret, and OpenAI API key, are configured to allow the ingestion script to interact with the database and LLM <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. Once configured, the ingestion script is run to populate the knowledge base <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. For example, 42 Pydantic AI documentation pages might be transformed into 245 chunks, each with its URL, chunk number, LLM-generated title/summary, content, metadata, and embedding <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.

## Building the AI Agent with Pydantic AI

The AI agent is built using a framework like Pydantic AI, structuring it into three main parts: dependencies, the agent itself, and its tools <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

### 1. Basic RAG Implementation
Initially, the agent can be set up for basic RAG. This involves:
*   **Dependencies:** Defining access to clients like Superbase and OpenAI <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>.
*   **System Prompt:** A basic system prompt describes the agent's role and available tools <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.
*   **Agent Definition:** Using Pydantic AI's `Agent` class, specifying the LLM model, system prompt, and dependencies <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **`retrieve_relevant_documentation` Tool:** This tool handles basic RAG by:
    *   Getting the embedding for the user's query <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
    *   Calling a database function (e.g., `match_site_pages` in Superbase) to find the top N most similar records based on embeddings <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.
    *   Applying metadata filters (e.g., `source` is "Pydantic AI docs") to ensure context relevance <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
    *   Formatting the retrieved chunks into a coherent string for the LLM <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

### 2. Limitations of Basic RAG
Basic RAG works well for straightforward questions where the answer is contained within a single or few small chunks <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. However, it falls short when more extensive or specific information is required, such as a full code example spanning multiple parts of a document <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>. The agent might retrieve some relevant information but fail to provide a complete or accurate answer because it cannot reason about the best way to access the full context <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.

### 3. Enhancing with [[enhancing_ai_agents_with_rag_technology | Agentic RAG Tools]]
To overcome these limitations, [[advanced_rag_implementation_techniques | agentic RAG]] introduces additional tools that allow the agent to intelligently explore the knowledge base <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>:

*   **`list_documentation_pages` Tool:** This tool queries the database to retrieve a list of URLs from the knowledge base, often filtered by metadata <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. This allows the LLM to understand what documentation pages are available and reason about which ones might be relevant to the user's question <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **`get_page_content` Tool:** Once the agent identifies a potentially relevant URL, this tool retrieves the full content, title, and chunk numbers for that specific page from the database <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. It formats this content for the LLM, enabling the agent to read an entire page and improve its performance on complex questions <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>.

By combining basic RAG with these agentic tools, the agent gains the ability to reason about where to look for knowledge, such as identifying a specific "weather agent example" page and then retrieving its full content, leading to much more accurate and comprehensive responses <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

## Streamlit User Interface
A Streamlit UI can be used to interact with the Pydantic AI agent <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. This interface handles:
*   Converting Pydantic AI's internal text format to what Streamlit can display <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>.
*   Invoking the agent and passing necessary dependencies <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>.
*   Streaming responses in a typewriter style <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>.
*   Maintaining message history, including agent and tool messages, so the agent can reference past retrieved context without needing to pull the page again <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a>.

## Conclusion
[[advanced_rag_implementation_techniques | Agentic RAG]] provides a solution to common RAG problems by empowering LLMs to reason about how and where to retrieve information from a knowledge base <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. This leads to more consistent and accurate results compared to simple, one-shot RAG queries <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>. The framework can be further expanded by adding more specialized tools or dedicated knowledge bases (e.g., for code examples or specific repository sections), allowing the agent to intelligently select the best knowledge source for a given query <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.