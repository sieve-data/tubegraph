---
title: agentic RAG setup
videoId: mQt1hOjBH9o
---

From: [[colemedin]] <br/> 

Retrieval Augmented Generation (RAG) is a popular tool for providing [[Enhancing AI agents with RAG technology | AI agents]] access to a knowledge base, making them domain experts for specific documents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While RAG is easy to implement in no-code tools like n8n due to its widespread adoption <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, it often has [[limitations_of_rag_and_solutions | limitations]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. [[agentic_rag_strategy_and_implementation | Agentic RAG]] emerges as a powerful solution to overcome these common challenges <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## [[limitations_of_rag_and_solutions | Limitations of Traditional RAG]]

Traditional RAG relies on a lookup mechanism that frequently misses key context and related information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Specific issues include:
*   **Incomplete Context Retrieval**: When analyzing trends in a spreadsheet, RAG might only pull a fraction of the necessary data chunks for a table, making comprehensive analysis impossible <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Incorrect Document Retrieval**: RAG can struggle to retrieve information from the correct document, even when key identifiers like dates are present in the title <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Lack of Cross-Document Connection**: RAG often fails to connect information across different documents, which is crucial for broader context <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

These issues stem from two core problems <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
1.  RAG's inability to "zoom out" to entire documents or sets of documents unless the context is very small <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  RAG's lack of a concept for proper data analysis <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## What is [[agentic_rag_strategy_and_implementation | Agentic RAG]]?

[[agentic_rag_strategy_and_implementation | Agentic RAG]] is defined as giving [[Enhancing AI agents with RAG technology | AI agents]] the ability to reason about how they explore the knowledge base <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Instead of a single RAG tool, it provides multiple tools and enables agents to:
*   Improve RAG lookup queries <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Choose different tools to answer diverse user questions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

This approach significantly enhances an [[RAG AI agent development | AI agent's]] capability to navigate and understand complex knowledge bases <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Building an [[agentic_rag_ai_agent_template | Agentic RAG Agent]] in n8n

A typical [[agentic_rag_ai_agent_template | agentic RAG agent]] setup in n8n involves a comprehensive workflow <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This setup is considered a version three of the n8n RAG agent, improving upon simpler, previous implementations that struggled with tabular data and limited tool access <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Supabase Database Setup

The first step involves setting up the Supabase database with three distinct tables <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>:

1.  **Documents Table**: Stores embeddings for RAG, metadata, and the contents of each file <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
2.  **Document Metadata Table**: Holds higher-level information for documents, such as URLs for citing sources and titles. This allows the agent to analyze documents at a higher level and decide whether to inspect an entire file <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. It also stores schemas for spreadsheet-type files, informing the agent about available fields for querying <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
3.  **Document Rows Table**: Stores data for each row of CSV and Excel files in a `jsonb` column. This enables SQL-like querying of tabular data without requiring a new SQL table for each file <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### RAG Pipeline (Document Ingestion)

This pipeline is responsible for taking documents from sources like Google Drive and ingesting them into the Supabase knowledge base <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

*   **Google Drive Trigger**: Polls every minute for newly created or updated files in a specific folder <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. The workflow handles multiple files simultaneously within the same polling minute <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Clear Old Data**: Before ingesting new content, the system clears any existing data for the file in Supabase. This ensures no outdated chunks from previous versions of the file remain in the knowledge base <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Initial Metadata Insert/Upsert**: Inserts or updates the initial metadata (title, URL) for the document. This step doesn't require file content yet <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Content Extraction**: The workflow downloads the file and uses a switch node to determine the appropriate extraction method based on file type (e.g., CSV, Google Doc, PDF) <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. n8n supports various extract nodes for different file types like JSON or HTML <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
*   **Handling CSV and Excel Files**:
    *   Contents are converted into rows within n8n <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
    *   The data follows two paths in parallel <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>:
        1.  **Document Rows Insertion**: Each row is inserted into the `document_rows` table for SQL-like querying <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.
        2.  **Text Document Transformation**: The data is aggregated and summarized into a single string, effectively becoming a text document that can be chunked for RAG <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
    *   **Schema Definition**: Headers from the CSV/Excel file are extracted to define the schema, which is then updated in the `document_metadata` record. This schema informs the agent on how to write SQL queries for the tabular data <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   **Supabase Integration (Chunking and Embeddings)**:
    *   A Supabase Vector Store node handles inserting the chunked data <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   An embedding model (e.g., OpenAI's `text-embedding-3`) generates embeddings <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.
    *   Default data loaders chunk documents and define metadata, including `file_id` and `file_title`, which are crucial for querying and source citation <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
    *   A character text splitter is used for basic chunking, which can be customized based on specific use cases <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>.

### [[RAG AI agent development | AI Agent Configuration]]

The [[RAG AI agent development | AI agent]] setup is simpler than the RAG pipeline, leveraging the prepared knowledge base <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.

*   **Triggers**: Includes a webhook to expose the agent as an API endpoint and a chat trigger for direct interaction within n8n <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
*   **System Prompt**: Describes the agent's tools and provides instructions on how to leverage them, such as starting with RAG and using other tools if RAG fails <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. Encouraging honesty (telling the user if an answer isn't found) can reduce hallucinations <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
*   **Conversation History**: Utilizes a simple PostgreSQL table for conversation history, which is automatically created on the first conversation <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
*   **Tools**:
    *   **RAG Lookup Tool**: An improved version that can cite its sources by including metadata (file ID, title) in the results <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It uses the same embedding model as the ingestion pipeline <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.
    *   **List Documents Tool**: Queries the `document_metadata` table to pull all document titles and IDs. This allows the agent to reason about which files to inspect <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. For large corpora, filtering documents might be necessary <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.
    *   **Get File Contents Tool**: Given a file ID, it pulls the content of all chunks for that document from the `documents` table and combines them to provide the full text <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. The agent typically calls the "list documents" tool first to get the necessary file ID <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>.
    *   **Query Excel/CSV Files as SQL Tables Tool**: This [[advanced_rag_implementation_techniques | advanced RAG implementation technique]] allows the agent to write and execute SQL queries against tabular data stored in the `document_rows` table. The tool description provides explicit instructions and examples on how to use `jsonb` for selecting columns, grouping, and filtering <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. This enables the agent to perform calculations like sums and maximums over tables, which RAG alone cannot <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### [[agentic_rag_advantages_and_future_applications | Agentic RAG Advantages and Future Applications]]

This [[agentic_rag_strategy_and_implementation | agentic RAG]] setup significantly [[improving_rag_accuracy_with_additional_strategies | improves RAG accuracy]] and utility. For example, when asked to find the month with the most new customers from a spreadsheet, the agent can use the SQL query tool to precisely fetch the answer, even if the table is too large for a full RAG lookup <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. If a RAG lookup fails, the agent can pivot to listing documents and then retrieving the full contents of the relevant file, such as meeting notes based on their title <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The ability to cite sources with direct links to documents further enhances reliability <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

Tools like UnRaid are highlighted as critical for handling complex, unstructured documents (e.g., PDFs, images, receipts) by extracting structured data, which can then be ingested into the knowledge base <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. UnRaid's Prompt Studio allows for prompt engineering to extract specific information, and workflows can be deployed as data APIs or ETL pipelines <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

This template provides a strong starting point for [[rag_ai_agent_development | RAG AI agent development]] and can be extended by adjusting prompting, tools, and the pipeline to fit specific knowledge bases <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. Future developments include a completely local version of this [[agentic_rag_strategy_and_implementation | agentic RAG]] agent built with the local AI package <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, contributing to [[agentic_rag_setups_with_deepseek_r1 | agentic RAG setups with DeepSeek R1]].