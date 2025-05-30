---
title: retrieval augmented generation
videoId: mQt1hOjBH9o
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation_for_ai | Retrieval augmented generation]] is a popular tool for providing [[enhancing_ai_agents_with_rag_technology | AI agents]] with access to a knowledge base, effectively making them domain experts for specific documents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is widely adopted and supported, making its implementation relatively easy in no-code tools like n8n <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Limitations of Standard [[retrieval_augmented_generation_for_ai | RAG]]

Despite its popularity, standard [[retrieval_augmented_generation_rag_and_its_challenges | RAG often faces challenges]] and limitations <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. These primarily stem from its reliance on a lookup mechanism that can:
*   Miss key context and related information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. For instance, it might only pull a fraction of the necessary data from a spreadsheet for trend analysis <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, or retrieve meeting notes from an incorrect date despite the date being in the document title <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Struggle to connect different documents to provide a broader, necessary context <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Lack the ability to "zoom out" to entire documents or sets of documents, unless the context is very small <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Have no inherent concept of proper data analysis <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

For example, a typical [[retrieval_augmented_generation_for_ai | RAG]] agent might be stuck if a lookup fails, unable to explore knowledge in alternative ways <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Agentic [[retrieval_augmented_generation_for_ai | RAG]]

To overcome the limitations of standard [[retrieval_augmented_generation_for_ai | RAG]], a more advanced approach called Agentic [[retrieval_augmented_generation_for_ai | RAG]] is used <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Definition and Purpose
Agentic [[retrieval_augmented_generation_for_ai | RAG]] gives [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]] the ability to reason about how they explore a knowledge base, rather than relying on a single tool <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This includes enabling agents to:
*   Improve their [[retrieval_augmented_generation_rag_methods | RAG lookup queries]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Choose different tools to answer diverse user questions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Benefits of Agentic [[retrieval_augmented_generation_for_ai | RAG]]
By providing multiple tools, Agentic [[retrieval_augmented_generation_for_ai | RAG]] allows agents to:
*   List available documents in the knowledge base <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   Get the full contents of specific files <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. If a [[retrieval_augmented_generation_for_ai | RAG]] lookup fails, the agent can reason about which document to access based on its title or other metadata <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Query Excel and CSV files as if they were SQL tables <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This enables functions like calculating sums or maximums over tables, which are difficult with standard chunk-based [[retrieval_augmented_generation_for_ai | RAG]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

Agentic [[retrieval_augmented_generation_for_ai | RAG]] allows the agent to switch between using [[retrieval_augmented_generation_for_ai | RAG]] for detailed lookups and accessing entire documents or performing data analysis depending on the query <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Implementation of Agentic [[retrieval_augmented_generation_for_ai | RAG]] in n8n

An Agentic [[retrieval_augmented_generation_rag_in_ai | RAG]] agent can be built in n8n, integrating various components and workflows <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Database Setup (Superbase)
The setup involves three main tables in a Superbase database:
1.  **Documents Table**: Stores embeddings for [[retrieval_augmented_generation_for_ai | RAG]], metadata, and the contents of each document chunk <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
2.  **Document Metadata Table**: Contains higher-level information about documents, such as URLs for citing sources and titles. This enables the agent to look at documents at a higher level and decide whether to analyze an entire file based on its title <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. For spreadsheet files, it also stores the schema, which defines the fields available for querying <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
3.  **Document Rows Table**: Stores data from CSV and Excel files, allowing them to be queried with SQL queries <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Each row's data is stored in a flexible JSONB format, eliminating the need for a dedicated SQL table per file <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### [[introduction_to_retrieval_augmented_generation_rag | RAG Pipeline]]
The pipeline handles ingesting documents from sources like Google Drive into the Superbase knowledge base <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Triggers**: Google Drive triggers poll for new or updated files in a specific folder <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. The workflow handles multiple files simultaneously using a loop <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   **Data Clearing**: Before processing, old data for an existing file is cleared from Superbase to ensure no outdated information remains in the knowledge base <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Content Extraction**: Files are downloaded, and content extraction varies by file type:
    *   **PDF/Text Documents**: Handled by single "extract" nodes <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
    *   **CSV/Excel Files**: Contents are converted into rows. These rows are then handled in two parallel paths <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>:
        1.  Inserted into the `document_rows` table for SQL-like querying <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.
        2.  Aggregated and summarized into a single text document, which is then chunked and prepared for [[retrieval_augmented_generation_rag_methods | RAG]] <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. The schema (headers) from CSVs are also extracted and updated in the `document_metadata` table to inform the agent how to query the data <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.
*   **Superbase Integration**: After extraction, documents are chunked and inserted into the Superbase Vector Store. This involves defining the table, query, embedding model (e.g., OpenAI's text-embedding-3) <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>, and using a data loader for chunking and metadata definition. Important metadata includes `file_ID` and `file_title` for querying and source citation <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

### Agent Setup
The [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] in n8n can be triggered via a webhook (as an API endpoint) or a chat interface <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **System Prompt**: A key component is the system prompt, which describes the agent's tools and provides instructions on how to use them (e.g., start with [[retrieval_augmented_generation_for_ai | RAG]], then use other tools if needed) <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. Encouraging honesty when answers aren't found can reduce hallucinations <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.
*   **LLM**: GPT-4o mini is used as the LLM for cost and speed, though more powerful models like GPT-4o or Claude 3.5 Sonnet can be substituted <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>.
*   **Conversation History**: A PostgreSQL table is used for conversation history, created automatically on the first interaction <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.

### Agent Tools
The agent is equipped with several tools to explore the knowledge base:
1.  **[[contextual_retrieval_in_rag | RAG]] Lookup Tool**: An improved version of the standard [[retrieval_augmented_generation_for_ai | RAG]] tool that includes metadata (file ID, file title) in its results, allowing the agent to cite sources <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. It uses the same embedding model as the ingestion pipeline to ensure consistent dimensions <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.
2.  **List Documents Tool**: Uses a PostgreSQL query to retrieve all documents from the `document_metadata` table. This allows the agent to see available files, their IDs, and schemas (for tabular data), enabling it to reason about which files to examine <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
3.  **Get File Contents Tool**: Given a `file_ID` (obtained from the List Documents tool), this tool pulls the content of all chunks for a specific document from the `documents` table and combines them to provide the full text <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.
4.  **Query Excel/CSV Files as SQL Tables Tool**: This advanced tool allows the agent to write SQL queries against the `document_rows` table. The tool description in the system prompt provides examples of how to use JSONB to select columns, perform group-bys, and filter data, allowing the agent to perform data analysis tasks like finding sums or maximums <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>.

The agent's ability to combine these tools allows it to handle complex queries, such as first attempting a [[retrieval_augmented_generation_for_ai | RAG]] lookup, and if unsuccessful, listing documents to identify relevant files, then retrieving their full contents to find the answer <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.