---
title: Agentic RAG strategy and implementation
videoId: _R-ff4ZMLC8
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation | Retrieval augmented generation (RAG)]] has been a primary method for feeding external knowledge into Large Language Models (LLMs) since the advent of generative AI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as a classic approach to transform an LLM into an expert on specific topics, such as an e-commerce store or an agent framework <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. However, basic [[retrieval_augmented_generation | RAG]] often faces common pitfalls, such as retrieving irrelevant text or the LLM ignoring provided context, leading to theoretical soundness but practical failures <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This has spurred significant research into [[improving_rag_accuracy_with_additional_strategies | advanced RAG implementation techniques]] like reranking, query expansion, and rank normalization <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Among these, [[agentic_rag_advantages_and_future_applications | agentic RAG]] stands out as a highly effective strategy <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## What is [[agentic_rag_advantages_and_future_applications | Agentic RAG]]?

Basic [[retrieval_augmented_generation | RAG]] operates as a "one-shot" process <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. A user query is converted into a vector representation, matched against vectors of document chunks in a knowledge base (vector database), and the most relevant chunks are provided as context to the LLM <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The LLM then generates a response augmented by this retrieved context <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The key limitation here is that the agent cannot reason about the context it receives; it cannot decide if more context is needed or if a different search approach is required <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

[[agentic_rag_advantages_and_future_applications | Agentic RAG]] addresses this by transforming [[retrieval_augmented_generation | RAG]] into a set of tools that an [[enhancing_ai_agents_with_rag_technology | AI agent]] can intelligently interact with <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This enables the agent to:
*   Search across different vector databases <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Reason about where to find knowledge based on the user's question <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   Utilize other tools to search the knowledge in varied ways, allowing for intelligent data exploration rather than relying on an initial retrieval <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Instead of a simple retrieval, the [[enhancing_ai_agents_with_rag_technology | AI agent]] (LLM layer) has access to various tool functions and action functions, which can include retrieval functions that query a vector database, or other functions that work with the knowledge base in different ways <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This provides the agent with the ability to reason about how it searches for an answer <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## [[agentic_rag_setup | Agentic RAG Setup]] and Implementation

The [[agentic_rag_setup | agentic RAG setup]] involves several moving parts: creating a knowledge base, developing the [[rag_ai_agent_development | RAG AI agent development]], and building a user interface.

### Step 1: Building the RAG Knowledge Base

The first phase involves collecting and preparing external knowledge for the LLM.

#### Data Scraping and Processing
Website content is scraped using tools like Crawl for AI, which can quickly scrape entire websites in parallel <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. For instance, the Pydantic AI documentation can be scraped by first fetching all URLs from its sitemap <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

#### Chunking Strategy
Once scraped, long documents are split into smaller, bite-sized chunks <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This is crucial because providing a massive page (e.g., 50,000 words) to an LLM can overwhelm its prompt and cause confusion <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Chunking ensures the LLM retrieves specific knowledge without pulling in an entire document <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

Sophisticated chunking methods are used to respect structural elements like code blocks, paragraphs, and sentences, preventing awkward splits in the middle of text <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. AI tools can assist in creating these complex chunking functions <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

#### Processing Chunks
Each chunk undergoes further processing to prepare it for the knowledge base <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. This involves:
*   **Extracting Title and Summary**: An LLM (e.g., GPT-4o mini) is used to generate a concise title and summary for each chunk, typically from its first 1,000 characters <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This extra context helps the agent reason about when to use a specific piece of knowledge <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Generating Embeddings**: Each chunk's content is converted into a vector representation (embedding) using an embedding model (e.g., OpenAI's `text-embedding-3-small` model) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. These embeddings are essential for the vector similarity search in [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Creating Metadata**: Additional information, such as the `source` (e.g., "Pydantic AI docs") and `created_at` timestamp, is attached to each record as metadata <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Metadata allows for specific filtering, enabling a single database table to serve multiple agents or to query based on ingestion time <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

#### Database Setup (Superbase)
The processed chunks, including their content, metadata, and embeddings, are stored in a database <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Superbase is a common choice, offering both vector database capabilities and structured SQL database functionalities within a single platform <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>.

To set up:
1.  Create a Superbase project <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.
2.  Use the SQL editor to run a script that creates the `site_pages` table, which will store the chunked data <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. This script can also include Row Level Security policies <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
3.  Configure environment variables with the Superbase URL, service role secret, and OpenAI API key <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
4.  Run the data ingestion script to populate the `site_pages` table <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. This process generates titles, summaries, and embeddings for all chunks in parallel batches <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.

> [!NOTE] Superbase vs. Qdrant
> Superbase is often recommended for its ability to handle both [[retrieval_augmented_generation | RAG]] (vector embeddings) and structured data within the same platform <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>. Qdrant, being solely a vector database, would necessitate using Superbase or another SQL database in parallel if structured data (like URLs, titles, summaries) also needs to be stored and accessed <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>. However, Qdrant is generally faster for vector searches, making it a choice for performance-critical applications <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>.

### Step 2: [[rag_ai_agent_development | AI Agent Development]] with Pydantic AI

The [[rag_ai_agent_development | RAG AI agent development]] uses a framework like Pydantic AI, typically structured into three parts:
1.  **Dependencies**: External clients required by the agent, such as Superbase and OpenAI <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
2.  **Agent Definition**: The core agent setup, including the LLM model (e.g., GPT-4o mini), system prompt, and access to dependencies <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
3.  **Tools**: Functions that the agent can call to perform specific actions <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. In Pydantic AI, functions are turned into tools using a decorator and a doc string that explains their purpose and arguments to the agent <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.

#### Basic RAG Tool
An initial tool for basic [[retrieval_augmented_generation | RAG]] is implemented to retrieve relevant documentation <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. This tool:
*   Generates an embedding for the user's query <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>.
*   Queries the `site_pages` table in Superbase to find the top (e.g., 5) most similar chunks based on vector embeddings <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.
*   Applies metadata filters (e.g., `source` equals "Pydantic AI docs") to ensure relevance <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
*   Formats the retrieved chunks into a clear string for the LLM <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

> [!EXAMPLE] Basic RAG Performance
> A basic RAG agent can effectively answer direct questions like "What are the supported models?" by retrieving precise information from its knowledge base <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>.
>
> However, for more complex requests, such as "Give me the weather agent example code from the documentation," basic RAG often falls short <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>. It might retrieve fragmented or incomplete information, failing to provide the full context needed for a comprehensive answer <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>. This highlights the limitations of one-shot retrieval for questions requiring broader context or deeper exploration <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

#### [[agentic_rag_ai_agent_template | Agentic RAG AI Agent Template]] - Adding Advanced Tools
To overcome the limitations of basic [[retrieval_augmented_generation | RAG]], [[agentic_rag_advantages_and_future_applications | agentic RAG]] introduces additional tools that allow the agent to reason and explore the knowledge base more intelligently <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.

1.  **List Documentation Pages Tool**: This tool queries the database to list all available URLs from the documentation, again using metadata filters to retrieve only relevant sources <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. This provides the LLM with a list of pages it can potentially visit <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
2.  **Get Page Content Tool**: This tool enables the agent to fetch the full content (title, content, chunk numbers) of a specific page given its URL <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. It combines all chunks belonging to that page into a single, well-formatted string for the LLM <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>.

These tools enable the agent to:
*   First, try basic [[retrieval_augmented_generation | RAG]] (embedding-based search) <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.
*   If basic [[retrieval_augmented_generation | RAG]] is insufficient, use the "list documentation pages" tool to identify potentially relevant URLs <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>.
*   Then, use the "get page content" tool to retrieve the full content of specific, intelligently chosen pages <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>.

> [!EXAMPLE] [[improving_rag_ai_agent_accuracy | Improving RAG AI Agent Accuracy]] with Agentic RAG
> When asked for the "weather agent example code," the [[agentic_rag_advantages_and_future_applications | agentic RAG]] solution first attempts basic [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>. Recognizing its initial answer is incomplete, the agent then uses its tools to list documentation pages, identify the specific "weather agent example" page by its URL, and fetch its complete content <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>. This multi-step, reasoned approach allows it to provide the full code example, which was previously unachievable with basic [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:41:23">[00:41:23]</a>.

### Step 3: Streamlit User Interface (UI)

Streamlit is used to create a simple chat interface for interacting with the Pydantic AI agent <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. The UI handles:
*   Converting Pydantic AI output to a displayable format <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a>.
*   Invoking the agent with necessary dependencies <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>.
*   Streaming the agent's response in a typewriter style <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>.
*   Maintaining a message history, including agent responses and tool messages, allowing the agent to reference past context and avoid re-fetching information <a class="yt-timestamp" data-t="00:42:44">[00:42:44]</a>.

## [[agentic_rag_advantages_and_future_applications | Agentic RAG Advantages and Future Applications]]

[[agentic_rag_advantages_and_future_applications | Agentic RAG]] significantly improves [[improving_rag_accuracy_with_additional_strategies | RAG accuracy]] and consistency by enabling the LLM to reason about where and how to retrieve information from its knowledge base <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>.

Further expansion of [[agentic_rag_advantages_and_future_applications | agentic RAG]] can include:
*   **Dedicated Knowledge Bases**: Creating separate knowledge bases for specific content types (e.g., one for examples, another for core documentation) <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. The agent can then intelligently choose which knowledge base to query based on the user's intent <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
*   **Code Repository Integration**: Adding tools to list and fetch content directly from a GitHub repository to allow the agent to dive into actual code <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>.

This approach transforms [[retrieval_augmented_generation | RAG]] from simple one-shot queries into an intelligent exploration process, leading to more robust and accurate AI agent performance <a class="yt-timestamp" data-t="00:45:23">[00:45:23]</a>.