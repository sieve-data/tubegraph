---
title: n8n RAG AI Agent
videoId: mQt1hOjBH9o
---

From: [[colemedin]] <br/> 

[[RAG AI agent development | Retrieval Augmented Generation]] ([[RAG AI agent development | RAG]]) is a popular tool used to provide [[n8n_in_creating_ai_agents | AI agents]] access to a knowledge base, effectively making them domain experts for specific documents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[RAG AI agent development | RAG]] is straightforward to implement in no-code tools like [[n8n_in_creating_ai_agents | n8n]] due to its widespread adoption and support <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Limitations of Traditional [[RAG AI agent development | RAG]]

Despite its popularity, [[RAG AI agent development | RAG]] can sometimes fall short <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The primary reason for this is its reliance on a lookup mechanism that may miss crucial context and related information <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Common issues include:
*   **Incomplete Data Retrieval**: [[RAG AI agent development | RAG]] lookups might only pull a fraction of necessary data, like a fourth of the chunks for a table, making trend analysis difficult <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Contextual Errors**: It can incorrectly pull information, such as meeting notes from the wrong date, even when the correct date is in the document title <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Lack of Broader Context**: [[RAG AI agent development | RAG]] often struggles to connect different documents to provide a necessary broader context <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

These limitations stem from two core problems:
1.  [[RAG AI agent development | RAG]]'s inability to "zoom out" to entire documents or sets of documents, unless the context is very small <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  [[RAG AI agent development | RAG]]'s lack of concept for proper data analysis <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Overcoming Limitations with [[Agentic RAG AI agent template | Agentic RAG]]

To address these limitations, [[Agentic RAG AI agent template | Agentic RAG]] is introduced as a preferred method <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. [[Agentic RAG AI agent template | Agentic RAG]] empowers [[n8n_in_creating_ai_agents | AI agents]] with the capability to reason about how they explore their knowledge base, rather than being confined to a single tool <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

This approach includes:
*   The ability for [[n8n_in_creating_ai_agents | agents]] to improve their [[RAG AI agent development | RAG]] lookup queries <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   The option to choose different tools to answer diverse user questions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## [[Building a nocode RAG AI agent | Building an Agentic RAG Agent in n8n]]

A comprehensive workflow template is available for [[building_a_nocode_rag_ai_agent | building an agentic RAG agent]] in [[n8n_in_creating_ai_agents | n8n]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This template is designed as a version three of previous [[n8n_in_creating_ai_agents | n8n]] [[RAG AI agent development | RAG]] [[n8n_in_creating_ai_agents | agents]], significantly improving on earlier implementations that struggled with tabular data and had only [[RAG AI agent development | RAG]] as a tool <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Database Setup

The first step in the workflow involves setting up a Superbase database with three key tables:
1.  **Documents Table**: Stores embeddings for [[RAG AI agent development | RAG]], metadata, and the contents of each file chunk <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. This is typically part of standard Superbase [[RAG AI agent development | RAG]] setup instructions <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
2.  **Document Metadata Table**: Holds high-level information for documents, such as URLs for citing sources and titles <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. This allows the [[n8n_in_creating_ai_agents | agent]] to understand documents at a higher level <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. It also defines the schema for spreadsheet-type files, which is crucial for querying data <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
3.  **Document Rows Table**: Stores data for each row of CSV and Excel files in JSONB format within a `row_data` column <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This enables SQL-like queries for tabular data without requiring a dedicated SQL table for each file <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

When connecting to Postgres nodes in [[n8n_in_creating_ai_agents | n8n]], it's essential to use the transaction pooler method (port 6543) in Superbase, not direct connection parameters <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### [[Creating RAG AI agents using n8n | RAG Pipeline]]

The [[creating_rag_ai_agents_using_n8n | RAG pipeline]] is responsible for ingesting documents from sources like Google Drive into the Superbase knowledge base <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

Key steps in the pipeline include:
*   **Google Drive Trigger**: Polls every minute for newly created or updated files in a specified folder <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. While it supports creation and updates, there isn't a trigger for file deletions <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
*   **Handling Multiple Files**: The workflow is designed to process multiple files simultaneously by looping through each one <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Setting the Stage**: Extracts important information like file IDs, types, titles, and URLs for further processing <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
*   **Clearing Old Data**: Before ingesting new content, all old data for the specific file (document rows and data rows) is deleted from Superbase to ensure a clean slate and prevent outdated information from remaining <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Initial Metadata Upsert**: Inserts or updates initial metadata (title, URL) in the `document_metadata` table <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. Postgres nodes are used for upserts due to their capabilities <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Content Extraction**: Downloads the file from Google Drive <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. A switch node directs the workflow to different extraction branches based on the file type (e.g., CSV, PDF, text document, Google Doc) <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. [[n8n_in_creating_ai_agents | n8n]] supports various extract nodes, and custom workflows can be created for unsupported types <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   **Handling Tabular Data (CSV/Excel)**:
    *   Contents are converted into rows within the [[n8n_in_creating_ai_agents | n8n]] workflow <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
    *   The data follows two paths:
        1.  Rows are inserted into the `document_rows` table for SQL querying <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.
        2.  Data is aggregated and summarized into a single text document, which is then chunked for [[RAG AI agent development | RAG]] <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
    *   The headers from CSV/Excel files are used to define the schema, which is updated in the metadata record, allowing the [[n8n_in_creating_ai_agents | agent]] to understand how to query the tabular data <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   **Superbase Integration**: Uses [[n8n_in_creating_ai_agents | n8n]] nodes to chunk documents, create embeddings (e.g., OpenAI's `text-embedding-3`), and insert them into the Superbase vector store <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. The file ID and title are included in the metadata, which is crucial for querying and source citation <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>. A simple character text splitter is used for chunking <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>.

### [[Building AI Agents with n8n | AI Agent Setup]]

[[Building AI Agents with n8n | Creating the AI agent]] in [[n8n_in_creating_ai_agents | n8n]] is simpler than the [[creating_rag_ai_agents_using_n8n | RAG pipeline]], as it primarily involves defining tools and a system prompt <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.

Components of the [[n8n_in_creating_ai_agents | AI agent]] setup:
*   **Triggers**: Includes a webhook to expose the [[n8n_in_creating_ai_agents | agent]] as an API endpoint and a chat trigger for direct interaction within the [[n8n_in_creating_ai_agents | n8n]] workflow <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
*   **Edit Fields Node**: Standardizes outputs from different triggers for consistent input to the [[n8n_in_creating_ai_agents | agent]] node <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.
*   **Agent Node**: Contains the core logic:
    *   **System Prompt**: Instructs the [[n8n_in_creating_ai_agents | agent]] on available tools and how to leverage them, e.g., starting with [[RAG AI agent development | RAG]] and using other tools if [[RAG AI agent development | RAG]] fails <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. A key tip for [[improving_rag_ai_agent_accuracy | improving RAG AI agent accuracy]] and reducing hallucinations is to instruct the [[n8n_in_creating_ai_agents | agent]] to be honest if it cannot find an answer <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
    *   **Model**: Typically uses an affordable and fast LLM like GPT-4o mini, though more powerful models can be used depending on the use case <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.
    *   **Conversation History**: Utilizes a simple Postgres conversation history table, which is automatically created if it doesn't exist <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

### Key Tools in [[Enhancing AI agents with RAG technology | Agentic RAG]]

The power of [[Agentic RAG AI agent template | Agentic RAG]] in [[n8n_in_creating_ai_agents | n8n]] comes from the diverse set of tools available to the [[n8n_in_creating_ai_agents | agent]]:

1.  **Improved [[RAG AI agent development | RAG]] Lookup Tool**: This is an enhanced version of the Superbase vector store tool <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. It includes the option to return metadata (file ID, file title) along with the [[RAG AI agent development | RAG]] results, enabling the [[n8n_in_creating_ai_agents | agent]] to cite its sources <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. The embedding model used for retrieval must be the same as the one used for inserts to ensure compatible dimensions <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
2.  **List Documents Tool**: Uses a simple Postgres query to pull all documents from the `document_metadata` table <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. This allows the [[n8n_in_creating_ai_agents | agent]] to read high-level information about available files, including their IDs and, for tabular files, their schemas, and reason about which files to investigate further <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.
3.  **Get File Contents Tool**: Takes a file ID (obtained from the `list documents` tool) and queries the `documents` table to retrieve all chunks for that document <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. It then combines these chunks to provide the full text of the document to the [[n8n_in_creating_ai_agents | agent]] <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>.
4.  **Query Excel/CSV Files as SQL Tables Tool**: This more advanced tool enables the [[n8n_in_creating_ai_agents | agent]] to write and execute SQL queries against tabular data stored in the `document_rows` table <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. The tool description provides explicit instructions and examples to the LLM on how the `document_rows` table is structured, how to use the `row_data` JSONB column, and how to query specific columns or perform group-bys <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>. The [[n8n_in_creating_ai_agents | agent]] specifies the file (dataset) ID for the query <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

## Demonstrating the [[Improving RAG AI agent accuracy | Agentic RAG Agent]]

The [[improving_rag_ai_agent_accuracy | Agentic RAG agent]] can effectively utilize its tools to answer complex questions <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, when asked "which month did we get the most new customers?" from a CSV file, the [[n8n_in_creating_ai_agents | agent]] will invoke the tool to write a SQL query to fetch the correct answer, demonstrating its ability to analyze tabular data <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

When asked to find "areas for improvement" in a text document, the [[n8n_in_creating_ai_agents | agent]] can successfully use its [[RAG AI agent development | RAG]] tool to pull the relevant information, even with slightly different phrasing <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

If a [[RAG AI agent development | RAG]] lookup fails, the [[n8n_in_creating_ai_agents | agent]] can instead list available documents and then get the file contents of specific ones. For instance, if asked for action items from meeting notes, and [[RAG AI agent development | RAG]] fails, the [[n8n_in_creating_ai_agents | agent]] can identify the correct document by title, retrieve its full contents, and answer the question <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. The [[n8n_in_creating_ai_agents | agent]] can also cite its source by providing a link to the original document <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Unracked: A Helper Tool for Complex Documents

Unracked is an open-source, no-code LLM platform that assists in [[n8n_in_creating_ai_agents | creating AI APIs]] and ETL pipelines to convert unstructured documents into structured data <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This is vital for [[n8n_in_creating_ai_agents | AI agents]] with [[RAG AI agent development | RAG]], especially when dealing with complex document types beyond simple CSVs and text files <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

Unracked consists of three parts:
1.  **Prompt Studio**: For engineering prompts to extract information from unstructured documents using LLMs <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
2.  **Workflows**: Where flows are built to automate information extraction from documents <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
3.  **Data APIs and ETL Pipelines**: Deploys workflows as data APIs and ETL pipelines <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

It simplifies extracting specific tables from PDFs or information from images (e.g., receipts) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Workflows can be deployed as API endpoints and integrated into [[n8n_in_creating_ai_agents | n8n]] workflows to handle more complicated documents <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Future Developments

A completely local version of the [[Agentic RAG AI agent template | agentic RAG agent]], built with the local AI package, is planned for release <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This further expands the possibilities for [[prototyping_ai_agents_using_n8n | prototyping AI agents]] in [[n8n_in_creating_ai_agents | n8n]] <a class="yt-timestamp" data-t="00:33:44">[00:33:44]</a>.