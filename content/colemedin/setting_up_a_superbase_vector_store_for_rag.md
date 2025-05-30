---
title: Setting up a Superbase vector store for RAG
videoId: c5dw_jsGNBk
---

From: [[colemedin]] <br/> 

[[using_supabase_as_a_vector_database | Supabase]] can be utilized as a vector database for building a Retrieval Augmented Generation (RAG) knowledge base for an AI agent, allowing for a no-code approach when integrated with tools like `n8n` <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>. This setup enables an AI agent to become an expert on specific documentation, such as Pydantic AI <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## Supabase Vector Store Integration in `n8n`

The integration of [[using_supabase_as_a_vector_database_for_ai_agents | Supabase as a vector database for AI agents]] within `n8n` involves configuring the Supabase credentials and setting up the necessary database table to store the knowledge base <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

### Connecting Your Supabase Account
To connect your Supabase account within `n8n`, you need to provide:
*   Your Supabase host (URL) <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   Your service role secret <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

These credentials can be found in your Supabase project settings under the API tab <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

### Setting Up the Knowledge Base Table
Supabase provides a starter template for setting up your vector store table <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
1.  Navigate to the `Supabase` SQL editor <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
2.  Copy the SQL script provided in the `Supabase` vector store node documentation (starting from line 4, as the vector extension is usually enabled by default) <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.
3.  Paste and run the SQL script <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This automatically creates the `documents` table and the `match_documents` function, which performs the RAG retrieval on your knowledge base <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

After execution, the `documents` table will be available in your table editor <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

### Configuring the `n8n` Supabase Vector Store Node
Within the `n8n` workflow, the Supabase vector store node is configured as follows:
*   **Embedding Model**: OpenAI `text-embedding-3-small` is used for creating embeddings <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. API key connection is straightforward via `n8n`'s credential system <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
*   **Data Loader**: The default data loader is used <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.
*   **Data Source**: The content for the knowledge base is extracted from `json.res.markdown`, which is the markdown content scraped from web pages <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
*   **Metadata**: Optional metadata, such as the source page URL, can be added to the database for better [[contextual_retrieval_in_rag | contextual retrieval]] <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **Text Splitter**: A text splitter with a chunk size of 5,000 is used, though optimal chunking strategies may vary by use case <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

## Knowledge Base Ingestion and Agent Interaction
Once configured, the workflow can ingest data into the Supabase vector store. For example, crawling 30 pages of documentation can result in 148 vectors inserted into the database <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

The AI agent, using a `GPT-4o Mini` model, leverages this [[creating_and_utilizing_a_vector_database_for_rag | knowledge base for RAG]]. When asked a question, it uses the Supabase vector store tool to retrieve relevant chunks, and the LLM then reasons about these chunks to provide a final response <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. The agent successfully retrieves information from specific documentation pages, demonstrating effective [[contextual_retrieval_in_rag | retrieval]].

This setup provides a foundational, no-code approach to building a RAG system by combining `crawl4ai` for web scraping, `n8n` for workflow automation, and [[choosing_vector_databases_for_rag_applications | Supabase as a vector database]] <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. Further enhancements could include implementing [[agentic_rag_setup | agentic RAG setup]] techniques for more advanced functionality <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.