---
title: Integrating Google Drive with n8n for document management
videoId: T1ZKEmDN8AA
---

From: [[colemedin]] <br/> 

[[workflow_automation_with_n8n | n8n]] offers a straightforward approach to creating RAG (Retrieval Augmented Generation) [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]] by combining the [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agent]] node with vector store retrieval and document inserter tools <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This setup enables intuitive development of a RAG pipeline for document interaction <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. A primary challenge in this process is extracting text from various document types for the knowledge base, particularly non-raw text formats like PDFs or Excel files <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Workflow Overview

The core of the solution involves extending an existing RAG [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agent]] workflow in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. While the previous setup using [[integrating_n8n_and_supabase | Supabase]] for the vector database worked well for raw text <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, supporting different file types like PDFs or Excel documents requires specific adjustments <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The workflow begins with two triggers:
*   **Chat Input Trigger**: Allows interaction with the [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] directly within the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] user interface <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Webhook Trigger**: Enables the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] to be used as an API <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, allowing external applications to leverage its functionality <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] itself defines the user prompt, system message, and integrates a language model (e.g., GPT-4o mini) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It uses a [[integrating_n8n_and_supabase | Supabase]] PostgreSQL database for chat history <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> and the "retrieve documents" tool for RAG, supported by a [[integrating_n8n_and_supabase | Supabase]] vector store with OpenAI for embeddings and document processing <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

The critical "bottom part" of the workflow handles inserting documents into the knowledge base <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Google Drive Integration

The workflow is triggered by [[integrating_google_drive_as_a_knowledge_base | Google Drive]] events:
*   When a file is created in a specific [[integrating_google_drive_as_a_knowledge_base | Google Drive]] folder <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   When a file is updated in the same folder <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

[[overview_of_n8n_as_a_workflow_automation_tool | n8n]] polls the designated folder every minute for changes <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Dynamic File Type Processing

A key innovation in this workflow is the dynamic processing of different file types <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Unlike simpler workflows that use a single node for raw text extraction <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, this extended workflow incorporates branching logic <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Identifying File Types with MIME Types

The workflow identifies the document type using its **MIME type** <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This `mimeType` parameter is available from the [[integrating_google_drive_as_a_knowledge_base | Google Drive]] trigger output <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Google Doc**: `application/vnd.google-apps.document` <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>
*   **PDF**: `application/pdf` <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>
*   **Excel Document**: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

> [!info] Google Workspace MIME Types
> A comprehensive list of Google Workspace MIME types is available in Google's documentation, serving as a reference for extending the workflow to support more file types <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Branching for Extraction

Based on the MIME type, a **Switch node** directs the workflow to the appropriate "extract from file" node <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] provides specific extraction nodes for various formats:
*   **Extract from PDF Node**: For PDF documents <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Extract from Excel Node**: For Excel documents (`.xlsx`) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Extract Document Text Node**: Used as a fallback for simpler formats like Google Docs, CSVs, or raw text files <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

> [!warning] Output Field Differences
> Different extraction nodes output extracted text to different fields <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>:
> *   `Extract Document Text` node outputs to `json.data` <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
> *   `Extract from PDF` node outputs to `json.text` <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
> *   `Extract from Excel` node outputs to `json.concatenatedData` <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
>
> The "document loader" node, which prepares text for chunking, must be configured to check for these different attribute names using JavaScript's logical OR operator (`||`) <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

### Document Ingestion Process

1.  **Delete Old Records**: Before ingesting a new version of a document, all old records for that document are deleted from the vector store to ensure the knowledge base is fresh and avoids confusing the LLM <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
2.  **Download File**: The document is downloaded to the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] instance as a binary file <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  **Extract Text**: The appropriate extract node processes the downloaded file based on its MIME type <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
4.  **Insert into Vector Database**: Finally, the extracted text is inserted into the vector database (e.g., [[integrating_n8n_and_supabase | Supabase]]) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This process automatically splits the document into chunks and generates vectors <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

> [!info] Excel Document Handling
> For Excel documents, a simple approach is to extract all data into a table format, aggregate it into a single item, and then summarize it into a single string to be treated like raw text for chunking <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. More complex strategies (e.g., creating records per row) depend on the specific use case <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Verifying Document Integration

Once documents are ingested, the RAG [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] can answer questions based on the content of the newly added documents <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. The [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] will search the vector store, retrieve relevant chunks, and use them to formulate an answer <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.