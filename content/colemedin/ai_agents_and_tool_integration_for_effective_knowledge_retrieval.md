---
title: AI agents and tool integration for effective knowledge retrieval
videoId: _R-ff4ZMLC8
---

From: [[colemedin]] <br/> 

[[Retrieval Augmented Generation (RAG)|Retrieval Augmented Generation (RAG)]] has historically been the primary method for feeding external knowledge into Large Language Models (LLMs) since the advent of generative [[AI capabilities versus tools|AI]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as the classic approach to transforming an LLM into an expert on a specific subject, such as an [[AI agents and their development|agent framework]] or an e-commerce store <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

However, implementing RAG can present common pitfalls, including the retrieval of irrelevant text during searches and the LLM's failure to incorporate provided additional content <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While RAG appears logically sound in theory, these issues can cause it to "fall apart in practice" <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Consequently, significant industry research is dedicated to improving RAG <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, employing strategies like reranking, query expansion, and rank normalization <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Among various strategies, [[Agentic RAG|agentic RAG]] stands out as the most effective <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Understanding Basic RAG <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>

Basic RAG involves several steps:
1.  **Knowledge Base**: A collection of documents serves as the knowledge base <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Chunking**: Documents are split into smaller, bite-sized chunks to efficiently provide information to the LLM <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This prevents overwhelming the LLM with massive pages <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Chunking aims to preserve logical units like code blocks, paragraphs, and sentences <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
3.  **Embedding**: These chunks are transformed into vectors (mathematical representations) using an embedding model <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
4.  **Vector Database Storage**: The vectors are then stored in a vector database <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
5.  **Query Processing**: When a user submits a query, it is also converted into a vector using the same embedding model <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
6.  **Retrieval and Augmentation**: Vector mathematics are used to match the query to the most relevant documents in the database <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This relevant context is then provided to the LLM, expanding the original prompt <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The LLM then generates a final response augmented by this information <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

A significant limitation of basic RAG is its "one-shot" nature <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The [[AI agents and their development|agent]] cannot reason about the retrieved context; it cannot determine if the context is insufficient or if a different search approach is needed. This lack of opportunity to improve retrieval is a key drawback <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Agentic RAG: Enhancing Knowledge Retrieval with Tools <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>

[[Agentic RAG|Agentic RAG]] transforms RAG from a passive one-shot retrieval into an active process where RAG becomes a *tool* for the [[AI agents and their development|agent]] to interact with <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This approach grants the [[AI agents and their development|agent]] the ability to intelligently explore data, rather than merely working with the initial retrieval <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Key features of [[Agentic RAG|agentic RAG]]:
*   **Dynamic Tool Interaction**: The [[AI agents and their development|agent]] can reason about where to find knowledge, potentially searching through different vector databases or utilizing other tools to search knowledge in varied ways <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Intelligent Exploration**: It empowers the [[AI agents and their development|AI agent]] to reason about *how* it searches for an answer, leading to more powerful and accurate results <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This contrasts with basic RAG's inability to adapt if the initial context is incomplete or incorrect <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

## Building an Agentic RAG Solution: A Step-by-Step Approach

Developing an [[Agentic RAG|agentic RAG]] solution involves several moving parts:

### 1. Data Ingestion and Knowledge Base Setup <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>
The first step is to populate the knowledge base.
*   **Web Crawling**: Utilize an open-source LLM-friendly web crawler like Crawl4AI to scrape website content rapidly <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For example, the Pydantic AI documentation can be scraped by fetching all URLs from its sitemap <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Chunking**: After crawling, the raw markdown content is split into smaller chunks <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This ensures that the LLM receives specific, bite-sized information rather than being overwhelmed by large pages <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. The chunking process is designed to respect structural elements like code blocks and paragraphs to maintain contextual integrity <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Processing Chunks**: Each chunk undergoes further processing:
    *   **Title and Summary Extraction**: An LLM (e.g., GPT-4o mini) extracts a title and summary for each chunk <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This additional context aids the [[AI agents and their development|agent]] in reasoning about when to use a specific piece of knowledge <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
    *   **Embedding Creation**: The chunk content is converted into an embedding (vector representation) using an embedding model <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
    *   **Metadata Generation**: Metadata, such as the source (e.g., "Pydantic AI docs") and ingestion time, is created <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. This metadata enables specific filtering, allowing a single database table to serve multiple [[AI agents and their development|agents]] by segregating knowledge based on source <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Storage in Database**: The processed chunks, including their URL, chunk number, title, summary, content, metadata, and embedding, are then inserted into a database like Superbase <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

### 2. Database Setup with Superbase <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>
Superbase is used to store the knowledge base. This involves:
*   **SQL Editor**: Running SQL scripts to create necessary tables, such as a `site_pages` table, which includes fields for URL, chunk number, title, summary, content, metadata, and the embedding vector <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   **API Credentials**: Configuring environment variables with the Superbase URL and service key, along with the OpenAI API key and desired LLM model (e.g., `gpt-4o-mini`) <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

#### Qdrant vs. Superbase for RAG <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>
*   **Superbase**: Offers a simplified approach by combining RAG capabilities (vector storage) with structured data storage (SQL database) on a single platform <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>. This is beneficial for [[Agentic RAG|agentic RAG]] where [[AI agents and their development|agents]] need to query both embeddings and structured metadata like titles and URLs.
*   **Qdrant**: A dedicated vector database that excels in speed <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. If speed is a critical optimization factor, embeddings could be stored in Qdrant for faster RAG, while structured metadata remains in a relational database like Superbase <a class="yt-timestamp" data-t="00:39:08">[00:39:08]</a>.

### 3. Creating the [[AI Agents and their development|AI Agent]] with Pydantic AI <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>

Pydantic AI is used to build the [[AI agents and their development|agent]]. The typical setup involves three parts: dependencies, the agent itself, and its tools <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.

#### Basic RAG Tool Implementation <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>
Initially, a tool for basic RAG is defined. This tool:
*   Gets the embedding for the user's query <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   Uses a database function (e.g., `match_site_pages` in Superbase) to find the most similar records based on embeddings <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.
*   Filters results by source metadata (e.g., "Pydantic AI docs") <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
*   Formats the top relevant document chunks into a string for the LLM <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.

**Limitations of Basic RAG:** While effective for straightforward questions (e.g., "what are the supported models?"), basic RAG often fails when complex information or a complete example (like specific code from documentation) is needed, as it might only retrieve partial, fragmented content <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>.

#### Integrating Tools for Agentic RAG <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>
To overcome basic RAG's limitations, additional tools are introduced, allowing the [[AI agents and their development|agent]] to reason and dynamically explore the knowledge base. These tools leverage the metadata stored during ingestion:

1.  **Tool to List Documentation Pages**: This tool queries the database to retrieve a list of all relevant URLs, again filtered by source metadata <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. This gives the LLM knowledge of available pages it might visit to answer a user's question <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
2.  **Tool to Get Specific Page Content**: Once the [[AI agents and their development|agent]] identifies a potentially relevant URL from the list, this tool is called to fetch the title, content, and chunk numbers for that specific URL from the knowledge base <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>. The content from all chunks of that page is then combined and returned to the LLM <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.

This [[Integration of nocode tools with local AI agents|integration of tools]] allows the [[AI agents and their development|agent]] to reason: for example, if asked for a "weather [[AI agents and their development|agent]] example," it can list URLs, identify a page titled "example agent," visit that page, and retrieve its full content to provide a comprehensive answer <a class="yt-timestamp" data-t="00:40:09">[00:40:09]</a>.

### 4. User Interface (Streamlit) <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>
A Streamlit UI provides a seamless interface for interacting with the [[AI agents and their development|agent]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It handles the display of messages, user input, and streams the [[AI agents and their development|agent]]'s responses in a conversational format <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>. It also ensures that the [[AI agents and their development|agent]]'s tool calls and retrieved contexts are added to the message history, allowing the [[AI agents and their development|agent]] to reference past retrievals without re-fetching information <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>.

## Expanding and Optimizing Agentic RAG <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>

[[Agentic RAG|Agentic RAG]] can be further expanded and optimized:
*   **Dedicated Knowledge Bases**: Create specialized knowledge bases for specific types of information (e.g., one for Pydantic AI examples and another for its API documentation) <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>. The [[AI agents and their development|agent]] can then intelligently choose which knowledge base to query based on the user's request <a class="yt-timestamp" data-t="00:44:18">[00:44:18]</a>.
*   **External Data Sources**: Integrate external data sources, such as GitHub repositories for code, as additional knowledge bases with their own listing and fetching functions <a class="yt-timestamp" data-t="00:44:26">[00:44:26]</a>.

By giving the LLM the ability to reason about *where* and *how* to obtain the correct information from its knowledge base, [[Agentic RAG|agentic RAG]] delivers more consistent and accurate results, solving many common issues seen with basic RAG <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. This approach highlights the importance of equipping [[AI agents and their development|agents]] to intelligently leverage their knowledge bases beyond simple "one-shot" queries <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>.