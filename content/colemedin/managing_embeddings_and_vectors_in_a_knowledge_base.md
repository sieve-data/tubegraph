---
title: Managing embeddings and vectors in a knowledge base
videoId: T1ZKEmDN8AA
---

From: [[colemedin]] <br/> 

Creating [[AI agents and tool integration for effective knowledge retrieval | AI agents]] using n8n for Retrieval Augmented Generation (RAG) is straightforward with the AI agent node, [[efficient_document_management_with_a_vector_database | vector store retrieval]], and document inserter tools <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This setup allows for an intuitive RAG pipeline to facilitate chatting with your documents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Challenge of Document Ingestion

The primary challenge in this setup is accurately extracting text from various document types for insertion into the [[Setting up and running a local knowledge base | knowledge base]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This is particularly difficult for formats like PDFs or Excel documents, which do not convert to raw text easily <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. While using [[Using Supabase as a vector database for AI agents | Supabase as a vector database]] has proven effective, extending workflows to handle diverse document types like PDFs or Excel files can be tricky <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

n8n does not offer a single node to extract text from all file types, making the problem non-trivial <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, a structured approach allows for a simple setup capable of handling virtually any file type <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This enables uploading PDF, Excel, and other document types to a Google Drive, ready for your RAG [[AI agents and tool integration for effective knowledge retrieval | AI agent]] within minutes <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## n8n Workflow for RAG AI Agents

An n8n workflow for a RAG [[AI agents and tool integration for effective knowledge retrieval | AI agent]] involves both the agent's interaction and the document ingestion process <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Agent Interaction

The agent part of the workflow typically starts with two triggers:
*   **Chat Input** for interaction within the n8n user interface <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Webhook** to expose the n8n agent as an API, allowing integration with external applications like Streamlit or Next.js <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

The core of the agent is the **Tools Agent** node, where:
*   The user prompt and system message are defined <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   A language model (e.g., GPT-4o mini, Groq, Mixtral, Claude) is hooked in <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   [[Using Supabase as a vector database for AI agents | Supabase PostgreSQL]] is used for chat history <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   The "retrieve documents" tool (provided by n8n) enables RAG, utilizing a [[Using Supabase as a vector database for AI agents | Supabase vector store]] with OpenAI for embeddings and document processing <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Document Ingestion Workflow

The bottom part of the workflow is dedicated to putting documents into the [[Setting up and running a local knowledge base | knowledge base]] to provide context for the agent <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

1.  **Triggers**: The workflow is triggered when a file is created or updated in a specific Google Drive folder <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. n8n polls this folder every minute for changes <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
2.  **File Type Identification**: The `mime type` parameter from the trigger output is crucial for identifying the file type <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For example, a Google Doc has a mime type of `application/vnd.google-apps.document`, while a PDF is `application/pdf` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This mime type is then used to branch the workflow <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   > [!info] Tip: Google Workspace provides documentation detailing the exact string for every mime type, which is useful for extending the workflow to new file types <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
3.  **Delete Old Records**: Before ingesting a new version of a document, existing records in the [[efficient_document_management_with_a_vector_database | vector store]] associated with that document are deleted <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This ensures a fresh set of vectors and prevents the LLM from being confused by old versions <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
4.  **Download File**: The file is downloaded to the n8n instance as a binary file, ready for text extraction <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Extract Text**: This is where the workflow differentiates based on file type <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    *   **Single Node Limitation**: The "extract document text" node only works for simpler file types like raw text, Google Docs, Markdown, or CSVs <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   **Specialized Extract Nodes**: For complex types like Excel or PDF documents, n8n offers various "extract from file" nodes (e.g., "Extract from HTML," "Extract from JSON," "Extract from PDF," "Extract from Excel") <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   **Switch Node for Branching**: A "switch" node uses the `file type` (derived from the mime type) to direct the workflow to the appropriate extract node <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
        *   If `application/pdf`, it goes to the "Extract from PDF" node <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
        *   If `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (Excel), it goes to the "Extract from XLSX" node <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
        *   If `application/vnd.google-apps.document` (Google Doc) or other simple formats (CSV, Readme, raw text), it defaults to the basic "extract raw text" node <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
6.  **Document Loader Output Fields**: A critical point is that different extract nodes output to different fields <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
    *   Raw text/Google Docs: `json.data` <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>
    *   PDF: `json.text` <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>
    *   Excel: `concatenatedData` (after processing) <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>
    *   The document loader needs to be configured to access these different attributes using JavaScript logic (e.g., `json.text || json.data || json.concatenatedData`) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
7.  **Ingest into Vector Database**: After extraction, the processed text (chunks) is inserted into the [[efficient_document_management_with_a_vector_database | vector database]] <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Handling Table Formats (Excel/CSV)

When processing table formats like Excel or CSV, there are various strategies for splitting records for RAG <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. A simple approach is to extract everything into a table format, aggregate all records into a single item, and then summarize it into a single string for chunking, treating the entire document as raw text <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. More advanced methods could involve creating a record for every row in the [[efficient_document_management_with_a_vector_database | vector database]] or defining specific chunking rules based on the use case <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

This robust workflow allows for seamless ingestion of diverse document types into a [[Setting up and running a local knowledge base | knowledge base]], enabling effective RAG for [[AI agents and tool integration for effective knowledge retrieval | AI agents]] <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.