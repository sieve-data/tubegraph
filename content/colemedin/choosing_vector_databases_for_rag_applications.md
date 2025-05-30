---
title: Choosing vector databases for RAG applications
videoId: z_LGan-t2Mo
---

From: [[colemedin]] <br/> 

Vector databases are a crucial component for [[creating_and_utilizing_a_vector_database_for_rag | Retrieval Augmented Generation (RAG)]] applications, enabling AI agents to effectively leverage external knowledge, such as documents <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. They serve as a storage mechanism for document information converted into vector representations, allowing for efficient searching by AI agents <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Core Functionality in RAG
When files are created or updated from a document source, such as Google Drive, their text is extracted and inserted into a vector database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. An embedding model (e.g., OpenAI) creates vector representations of this knowledge, which are then stored <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. When a user query comes in, it is also embedded and used to match against the knowledge base to retrieve the most relevant chunks, aiding the agent in answering the question <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This process makes RAG powerful by allowing agents to use documents to aid in answering questions <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Database Options
Several vector databases can be used for RAG applications. Examples include:
*   Neon Postgres <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
*   [[using_supabase_as_a_vector_database | Supabase]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>
*   Qdrant <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>

Many of these, like Neon and [[using_supabase_as_a_vector_database | Supabase]], run Postgres under the hood, making them largely interchangeable by simply changing the underlying Postgres database connection <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

## Advantages of Specific Platforms

### Neon
Neon offers several distinct advantages for RAG applications:
*   **Serverless Postgres** <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>: This enables autoscaling, where the database infrastructure adjusts based on the load, removing the need for manual scaling management typically required with other platforms <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. This can be crucial for scaling applications <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
*   **Database Branching**: Allows for easy management and testing of different database schema changes across various environments (dev, test, prod) <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **AI Coding Assistance (MCP server)**: Neon features an MCP server that enables natural language management of the database, allowing users to create new tables, manage records, and perform database migrations using AI coding assistance <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   **Strong Foundation**: Neon powers platforms like Vzero, Replit, and Highkey, and one of its co-founders has over 20 years of experience contributing to Postgres <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

### Supabase
[[using_supabase_as_a_vector_database | Supabase]] is also a viable option, often used in self-hosted configurations, and like Neon, it leverages Postgres <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

## Database Management in RAG Workflows
Regardless of the chosen vector database, effective [[efficient_document_management_with_a_vector_database | efficient document management]] is vital. When updating or adding new files, it's good practice to delete existing records for a specific file ID to ensure a "blank slate" before inserting new data, preventing leftover information from previous versions <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

For improved RAG accuracy, retrieved chunks of information are often prepended with additional context before being embedded and stored <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This ensures that when the LLM retrieves a record, it has both the original content and helpful contextual information, making the overall process more accurate <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Metadata, such as file ID, title, and URL, is also stored to allow the LLM to cite its sources <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

It is critical to use the same embedding model for both the data ingestion pipeline (when creating and storing vectors) and the AI agent's retrieval process (when embedding user queries) to ensure accurate matching <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.