---
title: Contextual retrieval in RAG
videoId: z_LGan-t2Mo
---

From: [[colemedin]] <br/> 

[[introduction_to_retrieval_augmented_generation_rag | Retrieval augmented generation (RAG)]] is a crucial strategy for making generative AI more accurate by leveraging external knowledge [00:00:02]. While [[basics_of_retrieval_augmented_generation_rag | basic RAG]] provides a way to incorporate external documents into [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]], it can often be inaccurate without additional strategies [00:01:51]. Contextual retrieval, a concept introduced by Anthropic, significantly enhances RAG accuracy [00:00:08].

## Limitations of Basic RAG <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>

In [[basics_of_retrieval_augmented_generation_rag | basic RAG]], documents are processed by extracting text, chunking it into smaller pieces, and then converting these pieces into vector representations stored in a [[creating_and_utilizing_a_vector_database_for_rag | vector database]] [00:00:44]. When a user query comes in, it's also embedded and used to find the most relevant chunks in the knowledge base to help the AI agent answer the question [00:04:56].

However, [[retrieval_augmented_generation_rag_and_its_challenges | basic RAG often fails]] to retrieve the necessary information from the knowledge base, leading to inaccurate answers [00:02:03]. This is because it struggles to provide the Large Language Model (LLM) with a broader understanding of how retrieved chunks relate to the overall knowledge base [00:02:16]. For example, studies show that with just regular RAG, the retrieval failure rate can be as high as 9.9% [00:03:00].

## What is Contextual Retrieval? <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>

Contextual retrieval aims to improve [[retrieval_augmented_generation_rag_in_ai | RAG accuracy]] by providing additional context to the retrieved chunks [00:05:10]. This helps the LLM "zoom out" and understand the broader meaning and relation of each chunk within the larger document and knowledge base [00:05:24]. By combining contextual retrieval with other [[retrieval_augmented_generation_rag_methods | RAG strategies]], the retrieval failure rate can be reduced from nearly 10% to less than 3% [00:03:30].

### How Contextual Retrieval Works <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>

The process of contextual retrieval builds upon [[basics_of_retrieval_augmented_generation_rag | basic RAG]]:
1.  **Document Chunking**: Documents are still split into smaller chunks [00:05:42].
2.  **Context Generation**: For each chunk, an LLM is prompted with the *entire document* and the *current chunk*. The prompt asks the LLM to generate a short, succinct context that situates the chunk within the document, describing what it's about and where it fits [00:05:50]. This extra context helps the LLM understand how the chunk aids in answering a user's question [00:06:17].
3.  **Context Prepending**: The generated extra context is prepended to the content of the original chunk, typically separated by a clear delimiter (e.g., "---") [00:06:35].
4.  **Embedding and Storage**: The combined text (context + chunk content) is then embedded and stored in the [[creating_and_utilizing_a_vector_database_for_rag | vector database]] [00:06:40].

When the [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] retrieves a chunk, it now receives both the specific information and the additional context, making the information significantly more useful [00:16:21].

### Cost Considerations with Prompt Caching <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>

A potential concern with contextual retrieval is the cost of sending the entire document for each chunk to the LLM [00:12:23]. However, this is mitigated by **prompt caching**:
*   **Reduced Cost**: LLMs like OpenAI, Gemini, and Anthropic offer reduced costs for repeated tokens in a prompt [00:12:48]. For OpenAI, it's a 50% reduction; for Anthropic and Gemini, it can be up to 90% [00:13:11]. This means that while the first prompt for a document is full price, subsequent prompts for chunks within the same document are much cheaper [00:13:04].
*   **Smaller LLMs**: A small, cheap LLM (e.g., GPT-4.1 Nano) can be used for generating the context, as it doesn't require extensive reasoning power [00:13:36].

## [[implementing_rag_with_contextual_embedding_in_n8n_and_python | Implementing RAG with Contextual Embedding in N8N and Python]]

The following sections detail how to build a RAG pipeline with contextual retrieval using N8N and Python.

### N8N Implementation <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

The N8N workflow for contextual retrieval is only slightly more complex than [[basics_of_retrieval_augmented_generation_rag | basic RAG]], primarily by adding an extra LLM call [00:08:11].

#### Workflow Steps:

1.  **Google Drive Trigger**: Watches for new or updated files in a specified Google Drive folder [00:08:31].
2.  **Loop Node**: Processes multiple files uploaded simultaneously, ensuring each file is handled individually [00:08:57].
3.  **Metadata Setting**: Sets important file metadata like ID, type, title, and URL [00:09:07].
4.  **Delete Existing Records**: Before inserting a new version of a file, existing records in the [[creating_and_utilizing_a_vector_database_for_rag | vector database]] associated with that file ID are deleted to ensure a clean slate [00:09:13].
5.  **Download and Extract Text**: The file is downloaded from Google Drive, and its text content is extracted [00:09:42].
6.  **Custom Chunking**: Instead of the default text splitter, custom JavaScript code is used to split the document into chunks (e.g., every 400 characters) [00:10:20]. This custom chunking is necessary to allow for the insertion of context before embedding [00:10:20]. The chunks are then converted into individual items in the N8N workflow [00:11:30].
7.  **LLM Call for Context**:
    *   An LLM node (e.g., OpenAI's GPT-4.1 Nano) is used [00:13:42].
    *   The prompt provides the *full document* and the *current chunk*, asking for a "short succinct context to situate this chunk" [00:11:51].
    *   Prompt caching (enabled by default for OpenAI) significantly reduces the cost of this repeated operation [00:12:31].
8.  **Data Transformation**: The output from the LLM (the generated context) is combined with the original chunk content, separated by "---" [00:14:53]. This combined string becomes the new "custom chunk" [00:14:55].
9.  **PostgreSQL (Neon/Supabase) Node**:
    *   The custom chunks with prepended context are inserted into the database [00:15:11].
    *   Metadata like file ID, title, and URL are also stored to allow the LLM to cite sources during RAG lookups [00:15:16].
    *   An embedding model (e.g., OpenAI's text-embedding-3-small) converts the combined text into vector representations for efficient searching [00:15:53].

#### Database Choice: Neon for PostgreSQL <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>

The workflow utilizes Neon, a serverless PostgreSQL offering, as its [[creating_and_utilizing_a_vector_database_for_rag | vector database]]. While other PostgreSQL options like Superbase (self-hosted) are also viable, Neon offers distinct advantages [00:16:33]:
*   **Autoscaling**: Database infrastructure automatically adjusts to demand, eliminating manual scaling management [00:17:14].
*   **Database Branching**: Easily manage and test different database schema changes across dev, test, and production environments [00:17:34].
*   **MCP Server**: A powerful feature allowing natural language management of the database for tasks like creating tables, managing records, and performing migrations [00:17:43].

#### AI Agent Setup in N8N <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>

The [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] itself remains a [[basics_of_retrieval_augmented_generation_rag | basic RAG]] implementation, but it benefits from the improved chunks [00:18:41]:
*   **Chat Trigger**: Initiates the AI agent's chat interface [00:18:57].
*   **AI Agent Node**: Uses a simple system prompt and an LLM (e.g., OpenAI) [00:19:01].
*   **PostgreSQL Chat Memory**: Stores conversation history in PostgreSQL [00:19:15].
*   **PostgreSQL Retrieve Documents Tool**: Configured to search the `documents_pg` table [00:19:21]. It limits retrieval to the top 4 most relevant chunks and includes metadata (title, URL) for source citation [00:19:37].
*   **Embedding Model Consistency**: Crucially, the same embedding model used in the RAG pipeline (e.g., text-embedding-3-small) must be used by the AI agent for consistent vector representation matching [00:20:01].

An example query about a "neural adaptation engine" from a quarterly report demonstrates how the agent retrieves the contextualized chunk, showing the prepended context and the content, which directly aids in answering the question accurately [00:20:26].

### Python Implementation <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>

Contextual retrieval can also be implemented in Python, often as part of a custom knowledge base or [[using_web_crawlers_and_databases_in_rag | web crawler]] server. An example is the open-source "crawl for AI RAG MCP server," which uses self-hosted Superbase for its PostgreSQL [[creating_and_utilizing_a_vector_database_for_rag | vector database]] [00:23:24].

The core logic remains the same:
*   A Python function takes the full document and a chunk as parameters [00:24:28].
*   It constructs the same prompt used in N8N, giving the LLM the document and chunk to generate additional context [00:24:33].
*   The generated context is then prepended to the chunk content with a "---" separator before being stored [00:24:46].

This Python implementation provides a flexible, open-source alternative for developers to integrate contextual retrieval into their [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]] and custom RAG pipelines [00:24:19].

## Beyond Contextual Retrieval <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>

While contextual retrieval significantly improves [[retrieval_augmented_generation_rag_in_ai | RAG accuracy]], it is one of several [[retrieval_augmented_generation_rag_methods | RAG strategies]]. Other advanced methods include:
*   **BM25 for Hybrid RAG**: Combines keyword search with semantic search for more robust retrieval [00:22:37].
*   **Re-ranking**: Re-ordering retrieved documents based on relevance to the query [00:22:42].
*   **Query Expansion**: Expanding or rephrasing the user's query to retrieve more relevant documents [00:25:47].
*   **Agentic RAG**: Integrating RAG with AI agentic reasoning for more complex tasks [00:25:48].

These strategies can be combined to create even more powerful and accurate RAG systems [00:25:51].