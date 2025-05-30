---
title: Extracting text from various document types
videoId: T1ZKEmDN8AA
---

From: [[colemedin]] <br/> 

Creating RAG (Retrieval Augmented Generation) AI agents with n8n is straightforward, utilizing the AI agent node alongside vector store retrieval and document inserter tools. However, the most challenging aspect is often [[extracting_and_processing_data_in_n8n | extracting text from documents]] for the knowledge base, especially for complex file types like PDFs or Excel documents that do not easily convert to raw text <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This article details how to extend an n8n workflow to handle various file types for RAG, enabling the use of PDF and Excel documents in minutes <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## The Challenge: No Single Extraction Node in n8n

n8n does not provide a single node to extract text from any file type, making the problem non-trivial <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The solution involves breaking down the process and using specific nodes for different file types.

## Core RAG Agent Workflow in n8n

An existing RAG AI agent workflow in n8n can be extended to support diverse document types <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

The agent's interaction flow typically starts with two triggers:
*   **Chat Input**: Allows interaction with the agent within the n8n user interface <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Webhook**: Enables the n8n agent to be used as an API for external applications like Streamlit or Next.js <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

The workflow then uses an AI agent node to define the user prompt, system message, and integrate an LLM (e.g., GPT-4o mini, Groq, Mixtral, Claude) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Chat history is managed using a [[efficient_document_management_with_a_vector_database | Superbase Postgres database]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. The agent's only tool is the "retrieve documents" tool, provided by n8n, which facilitates RAG using a [[efficient_document_management_with_a_vector_database | Superbase vector store]] and OpenAI models for embeddings and document processing <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

The document ingestion workflow involves:
1.  **Triggers**: Monitoring a specific Google Drive folder for file creation or updates <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. n8n polls this folder every minute for changes <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
2.  **Deleting Old Records**: Before ingesting a new version of a document, old records in the [[efficient_document_management_with_a_vector_database | vector store]] are deleted to ensure a fresh set of vectors and prevent confusion for the LLM <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
3.  **Downloading File**: The file is downloaded to the n8n instance for text extraction <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Key to File Type Extraction: Mime Type

The crucial element for determining how to extract text is the file's **mime type** <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This parameter, available in the trigger output, indicates the file type (e.g., `application/pdf` for PDFs, `application/vnd.google-apps.document` for Google Docs) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Branching for Different File Types with n8n Nodes

The traditional workflow uses a single node to extract text, which only works for simple file types like text files, Google Docs, Markdown, or CSVs <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. For more complex types like Excel or PDF documents, this is insufficient <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

n8n provides various "extract from file" nodes designed for different file types, including HTML, JSON, PDF, and Excel <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

A **switch node** is used to branch the workflow based on the `mime type` parameter <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>:
*   If `application/pdf`, it goes to the "extract from PDF" node <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   If `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (for Excel documents), it goes to the "extract from XLSX" node <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   As a fallback (for Google Docs, CSVs, raw text, etc.), it uses the standard "extract document text" node <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

A valuable resource for identifying specific mime type strings for Google Workspace documents is the Google Workspace documentation <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Handling Output Variations from Extract Nodes

A critical point to remember is that different extract nodes output the extracted text to different attributes <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>:
*   "Extract document text" nodes (for raw text, Google Docs) output to `json.data` <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   "Extract from PDF" nodes output to `json.text` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   "Extract from XLSX" nodes output to `concatenatedData` <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

When loading text into the document loader for chunking, the data input must correspond to the correct output field from the respective extract node <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This can be managed using JavaScript in n8n to check for different attributes <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## Demonstrations

### Google Doc Extraction
For Google Docs, the workflow proceeds to the simpler "extract document text" node, which extracts the raw text <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

### PDF Document Extraction
When a PDF document is uploaded, its mime type (`application/pdf`) directs the workflow to the "extract from PDF" node <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. After extraction, the text is chunked and inserted into the [[efficient_document_management_with_a_vector_database | vector database]] <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

### Excel Document Extraction
An Excel file (mime type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) is processed via its dedicated branch <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. For simplicity, the entire Excel file can be treated as raw text, extracting everything into a table format and then aggregating records into a single string for chunking and insertion into the database <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. Different [[extracting_and_processing_data_in_n8n | strategies]] exist for processing tabular data, depending on the specific use case <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

Once documents from various types are ingested into the [[efficient_document_management_with_a_vector_database | vector database]], the RAG agent can effectively answer questions using the context provided by these documents <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. This setup allows for the robust [[implementing_rag_with_local_text_and_pdf_documents | implementation of RAG with local text and PDF documents]] and other file types in n8n.