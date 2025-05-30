---
title: advanced RAG implementation techniques
videoId: mQt1hOjBH9o
---

From: [[colemedin]] <br/> 

While [[retrieval_augmented_generation | Retrieval Augmented Generation (RAG)]] is a popular tool for [[enhancing_ai_agents_with_rag_technology | enhancing AI agents]] with knowledge base access, traditional implementations often face significant [[limitations_of_traditional_rag_systems | limitations]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. These issues arise because RAG primarily relies on a lookup mechanism that can miss key context and related information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Limitations of Traditional RAG

Traditional [[retrieval_augmented_generation | RAG systems]] often struggle with:
*   **Missing Context** The lookup can frequently miss key context and related information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Partial Data Retrieval** When analyzing trends in a spreadsheet, RAG might only pull a fraction of the necessary chunks, making comprehensive analysis difficult or impossible <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Incorrect Information Retrieval** It can retrieve meeting notes from the wrong date, even when the correct date is explicitly in the document title <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Lack of Broader Context** RAG often struggles to connect different documents to provide a necessary broader context <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Limited Scope** It cannot "zoom out" to entire documents or sets of documents unless the context size is very small <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **No Data Analysis Concept** Traditional RAG lacks a concept of proper data analysis <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Ineffective Tabular Data Handling** It treats tabular data like CSVs and Excel files as simple text documents, preventing effective querying for sums, maximums, or trend analysis across the entire dataset <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Stuck State on Failure** If a RAG lookup fails, the agent has no alternative methods to explore the knowledge base and is forced to report that it cannot find an answer <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Overcoming Limitations with [[agentic_rag_strategy_and_implementation | Agentic RAG]]

The primary solution to these limitations is [[agentic_rag_strategy_and_implementation | Agentic RAG]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. [[agentic_rag_strategy_and_implementation | Agentic RAG]] empowers [[rag_ai_agent_development | AI agents]] with the ability to reason about how they explore the knowledge base, rather than being limited to a single tool <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This includes [[improving_rag_accuracy_with_additional_strategies | improving RAG lookup queries]] and dynamically choosing different tools to answer diverse user questions <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Key Components of [[agentic_rag_setup | Agentic RAG Setup]]

An advanced [[agentic_rag_setup | Agentic RAG setup]] involves a multi-faceted approach to both knowledge ingestion and agent tool utilization.

#### 1. Robust Data Ingestion Pipeline (RAG Pipeline)
The ingestion pipeline is crucial for preparing documents for the knowledge base. This "version three" of the n8n RAG agent handles both new file creation and updates <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

*   **Database Setup**: Requires setting up a Superbase database with three key tables <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>:
    *   **Documents Table**: Stores embeddings for RAG, metadata, and content chunks <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
    *   **Metadata Table**: Holds higher-level document information like URLs for citing sources and titles. This enables agents to reason about entire files based on titles <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
    *   **Document Rows Table**: Stores data from CSV and Excel files in JSONB format, allowing SQL-like querying without creating dedicated SQL tables for each file <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. The schema for tabular data is also stored in the metadata table <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

*   **Handling File Updates**: When a file is updated, all its old data is cleared from Superbase to ensure no outdated information remains in the knowledge base <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. This prevents issues like lingering chunks from a longer, older version of a document <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. Metadata is then upserted (updated if exists, inserted if new) <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

*   **Dynamic Content Extraction**: Different file types (CSV, Excel, PDF, Google Docs, etc.) require different extraction methods <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. The workflow uses a switch node to direct files to the appropriate extractor <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Tools like Unracy can be used for complex unstructured documents like PDFs with tables or images <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

*   **Tabular Data Processing**: For CSV/Excel files, data is processed in two parallel paths <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>:
    1.  **Row Insertion**: Each row is inserted into the `document_rows` table for SQL-like querying <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.
    2.  **Text Conversion and Chunking**: The entire table content is aggregated into a single text document, summarized, and then chunked for RAG retrieval <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. The column headers are extracted and defined as the schema in the document metadata, enabling the agent to understand and query the tabular data effectively <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

*   **Embedding and Chunking**: Documents are chunked using a character text splitter and embedded using models like OpenAI's `text-embedding-3` before insertion into the Superbase vector store <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. Metadata like `file_id` and `file_title` are included with each chunk to facilitate source citation and targeted deletion <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

#### 2. Enhanced Agent Tools

The [[rag_ai_agent_development | AI agent]] is equipped with multiple tools that allow it to reason and choose the best approach for information retrieval. The system prompt guides the agent to start with RAG and then use other tools if RAG doesn't provide the correct answer <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.

*   **Improved RAG Lookup Tool**: This tool now includes metadata (file ID, file title) in its results, allowing the agent to cite its sources accurately <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. It uses the same embedding model as the ingestion pipeline <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.

*   **List Documents Tool**: This tool queries the `document_metadata` table to list all available documents, their titles, IDs, and for tabular files, their schemas <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. This allows the agent to reason about which files might be relevant before performing a specific lookup <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

*   **Get File Contents Tool**: If a RAG lookup fails, the agent can use this tool to retrieve the entire content of a specific file by its ID <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. This is achieved by combining all chunks for that document from the `documents` table <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. The agent typically calls the "List Documents" tool first to obtain the necessary file ID <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>.

*   **Query Tabular Data Tool**: This advanced tool allows the agent to write SQL queries against the `document_rows` table for tabular data <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. It can perform operations like sums and maximums across tables, which is impossible with traditional RAG <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The agent uses the schema information from the metadata table to construct accurate queries, specifying the `file_id` as the `dataset_id` to target a specific file <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>, <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

*   **Conversation History**: A PostgreSQL database is used to maintain conversation history, allowing the agent to remember previous interactions <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

By combining these robust ingestion and multi-tool capabilities, [[agentic_rag_advantages and_future_applications | Agentic RAG]] significantly enhances the ability of AI agents to explore, analyze, and retrieve information from complex and diverse knowledge bases effectively <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.