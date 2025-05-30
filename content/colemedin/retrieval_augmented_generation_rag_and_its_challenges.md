---
title: Retrieval Augmented Generation RAG and its challenges
videoId: _R-ff4ZMLC8
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation | Retrieval augmented generation (RAG)]] has been the primary method for feeding external knowledge into Large Language Models (LLMs) since the advent of generative AI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is considered the classic approach for transforming an LLM into an expert on a specific domain, such as an agent framework or an e-commerce store <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Common Pitfalls of Basic RAG

Despite its logical soundness in theory, implementing basic [[retrieval_augmented_generation | RAG]] often encounters several common pitfalls that can make it fall apart in practice <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
*   **Irrelevant Search Results:** The system might return the wrong text from the search <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **LLM Disregard:** The LLM may completely ignore the extra content provided to it <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

These issues highlight the need for improved [[retrieval_augmented_generation | RAG]] strategies, leading to extensive research in the industry <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Some strategies mentioned include reranking, query expansion, and rank normalization <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Agentic RAG: An Advanced Approach

Among various strategies, Agentic [[retrieval_augmented_generation | RAG]] is highlighted as the most effective solution for enhancing AI agents with RAG technology <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It aims to transform standard [[retrieval_augmented_generation | RAG]] into an agentic approach that delivers more reliable results <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### What is Basic RAG?

Basic [[retrieval_augmented_generation | RAG]] involves a straightforward process <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>:
1.  **Knowledge Base:** A knowledge base consists of various documents <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Chunking:** Documents are split into smaller, bite-sized chunks to efficiently feed information to the LLM <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This prevents overwhelming the LLM with massive pages <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
3.  **Vectorization (Embeddings):** These chunks are converted into their mathematical representations (vectors) using an embedding model and stored in a vector database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  **Query Processing:** When a user query comes in, it is also converted into a vector representation using the same embedding model <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
5.  **Retrieval:** Vector mathematics are used to match the query to the most relevant document chunks in the database <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
6.  **Context Augmentation:** The retrieved relevant chunks are then provided as additional context to the LLM, effectively expanding the prompt <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
7.  **Response Generation:** The LLM uses this augmented information to generate the final response <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

The main limitation of basic [[retrieval_augmented_generation | RAG]] is its "one-shot" nature <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The agent cannot reason about the context it received; it cannot decide if the context was insufficient or if it needs to search in a different way <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### How Agentic RAG Works

Agentic [[retrieval_augmented_generation | RAG]] addresses the shortcomings of basic [[retrieval_augmented_generation | RAG]] by integrating [[retrieval_augmented_generation | RAG]] capabilities as **tools** that an AI agent can interact with <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This approach allows the agent to:
*   **Intelligent Exploration:** Reason about where and how to find knowledge <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Multiple Tools:** Utilize different tools to search the knowledge base in various ways <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Iterative Improvement:** The agent can decide if more context is needed or if a new search strategy should be employed <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

Instead of just retrieving context for a single query, the agent itself can use tools to:
*   Search across different vector databases <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   List and visit specific URLs within a knowledge base, reasoning about page titles or summaries to find relevant information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   Access other tool and action functions that work with the knowledge base in alternative ways <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

This empowers the AI agent to reason about how it is searching for answers, making the process much more powerful and yielding more consistent and accurate results <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.

### Key Components for Agentic RAG Implementation

A practical implementation of Agentic [[retrieval_augmented_generation | RAG]] involves several moving parts <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>:

1.  **Knowledge Base Ingestion:**
    *   **Crawling:** Using tools like Crawl for AI, content from websites (e.g., Pydantic AI documentation) is scraped <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   **Chunking:** The scraped content is divided into smaller, manageable chunks <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This process respects structural elements like code blocks and paragraphs to maintain contextual integrity within each chunk <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   **Processing Chunks:** For each chunk, additional information is generated:
        *   **Title and Summary:** An LLM (e.g., GPT-4o mini) extracts a concise title and summary, providing extra context for the agent to reason about <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
        *   **Embedding:** A vector representation of the chunk content is created using an embedding model (e.g., OpenAI's `text-embedding-3-small`) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
        *   **Metadata:** Additional information like the source (e.g., "pantic AI docs") is attached to enable specific filtering and segregation of knowledge within a single database table for multiple agents <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
    *   **Storage:** The processed chunks, along with their embeddings, titles, summaries, and metadata, are stored in a database, such as Superbase <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Superbase is favored for its ability to handle both [[retrieval_augmented_generation | RAG]] (embeddings) and structured data (metadata) in one platform, although dedicated vector databases like Qdrant can offer faster performance for embeddings alone <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>.

2.  **AI Agent Foundation (Pydantic AI):**
    *   An AI agent is built using a framework like Pydantic AI <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
    *   **Dependencies:** The agent is configured with necessary clients, such as Superbase and OpenAI <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.
    *   **System Prompt:** A system prompt defines the agent's role and available tools <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.

3.  **Agentic RAG Tools:**
    *   **Retrieve Relevant Documentation (Basic RAG Tool):** This tool performs vector similarity search in the knowledge base, filtering by metadata (e.g., `pantic_ai_docs`) to retrieve the most relevant chunks <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. It's often the initial step in the agent's reasoning process <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
    *   **List Documentation Pages (Agentic Tool):** This tool queries the database to retrieve a list of all relevant URLs from the knowledge base, allowing the LLM to reason about which pages to visit <a class="yt-timestamp" data-t="00:37:19">[00:37:19]</a>.
    *   **Get Page Content (Agentic Tool):** Once the agent identifies a promising URL, this tool fetches the full content (title, content, chunk number) of that specific page, providing a more comprehensive context than just individual chunks <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>. This allows the agent to "read from an entire page" to answer complex questions <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

### Demonstration and Benefits

Basic [[retrieval_augmented_generation | RAG]] can effectively answer straightforward questions like "what are the supported models" by retrieving direct relevant chunks <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. However, for more complex queries, such as requesting a full code example (e.g., the "weather agent example" from Pydantic AI documentation), basic [[retrieval_augmented_generation | RAG]] may fail to provide a complete and accurate answer <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

Agentic [[retrieval_augmented_generation | RAG]] resolves this by allowing the agent to:
1.  Initiate with basic [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
2.  If the initial retrieval is insufficient, reason to use other tools like listing documentation pages to identify relevant URLs <a class="yt-timestamp" data-t="00:41:13">[00:41:13]</a>.
3.  Subsequently use the "get page content" tool to retrieve the full content of the identified page, leading to a much more complete and accurate response <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>.

This multi-step, reasoning-driven approach makes the agent capable of handling complex information retrieval tasks <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### User Interface (Streamlit)

A user interface, such as one built with Streamlit, allows seamless interaction with the Pydantic AI agent <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. This UI converts agent responses for display and manages the conversation history, allowing the agent to reference previous tool calls and retrieved context without re-querying <a class="yt-timestamp" data-t="00:42:10">[00:42:10]</a>.

### Expanding Agentic RAG

Agentic [[retrieval_augmented_generation | RAG]] can be further expanded by adding more specialized tools and knowledge bases <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>. For example:
*   **Dedicated Knowledge Bases:** Creating separate knowledge bases specifically for "Pydantic AI examples" could lead to more accurate results when a user asks for code examples, preventing the agent from looking in less suitable parts of the documentation <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.
*   **Code Repository Integration:** Tools could be added to access and fetch content directly from the Pydantic AI GitHub repository, allowing the agent to dive into the actual code <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>.

By giving the LLM the ability to reason about where and how to obtain the correct information from its knowledge base, [[retrieval_augmented_generation | Agentic RAG]] provides more consistent and accurate results, moving beyond the limitations of one-shot queries <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.