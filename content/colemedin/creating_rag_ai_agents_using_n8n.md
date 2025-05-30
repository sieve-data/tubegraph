---
title: Creating RAG AI agents using n8n
videoId: T1ZKEmDN8AA
---

From: [[colemedin]] <br/> 

## Overview

[[n8n_in_creating_ai_agents | Making RAG AI agents with n8n]] is straightforward using the AI agent node, combined with vector store retrieval and document inserter tools <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This setup makes it intuitive to create a simple RAG pipeline for chatting with documents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The primary challenge typically lies in extracting text from documents for the knowledge base, especially for file types like PDFs or Excel documents that don't easily convert to raw text <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

While the vector database setup (e.g., using Superbase) generally works well <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, the difficulty arises when extending workflows to handle diverse document types <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This article outlines how to integrate different file types for RAG in n8n, enabling the use of PDF and Excel documents in minutes <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Core Components for RAG AI Agents in n8n

An [[ai_automation_with_n8n | n8n]] RAG AI agent workflow consists of two main parts: the agent that interacts with the user and the workflow that ingests documents into the knowledge base <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Chatting with the Agent Workflow

The top portion of the workflow facilitates interaction with the AI agent <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Triggers**:
    *   **Chat Input**: Provides a chat option within the n8n user interface for direct interaction <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   **Webhook**: Allows the n8n agent to be used as an API, enabling integration with external applications like Streamlit or Next.js <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Tools Agent**: This node defines the user prompt, system message, and integrates the AI model (e.g., GPT-4o mini, Groq, Mixol, Claude) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   **Chat History**: A Superbase PostgreSQL database is used for chat history <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   **Retrieve Documents Tool**: This is the sole tool linked to the agent, provided by n8n to perform RAG <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   **Vector Store**: A Superbase vector store handles document retrieval, using OpenAI for embeddings and processing document chunks <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Document Ingestion Workflow

The bottom part of the workflow is responsible for populating the agent's knowledge base <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>:
*   **Triggers**:
    *   **File Created**: Activates the workflow when a new file is added to a specific Google Drive folder <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   **File Updated**: Activates the workflow when an existing file in the same folder is modified (e.g., renamed, content added/deleted) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. n8n polls this folder every minute <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Data Processing**:
    *   **Identify File Type**: The `mime type` parameter from the Google Drive trigger output is crucial for identifying the file type (e.g., `application/pdf` for PDFs, `application/vnd.google-apps.document` for Google Docs) <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This parameter is used to determine the correct extraction path <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   **Delete Old Records**: Before ingesting new data, old records for the specific document are deleted from the vector store to ensure a fresh set of vectors and prevent confusion from old versions <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
    *   **Download File**: The file is downloaded to the n8n instance for text extraction <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Handling Diverse File Types

The key to extending [[prototyping_ai_agents_using_n8n | AI agents]] to work with various document types lies in branching the workflow based on file type <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### The Problem with Single Extract Nodes

The original workflow used a single node to extract document text <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, which only works for simple raw text files like Google Docs, markdown files, or CSVs <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Complex file types like Excel or PDFs require specific extraction methods <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### Implementing Branching Logic

n8n offers various `Extract from File` nodes tailored for different document types (HTML, JSON, PDF, Excel, etc.) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. A `Switch` node is used to direct the workflow to the correct extract node based on the `mime type` of the ingested file <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

#### Switch Node Conditions:
*   **PDF Documents**: If the file type is `application/pdf`, the workflow branches to the `Extract from PDF` node <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Excel Documents**: For Excel documents (e.g., `.xlsx` files), the mime type is `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, and the workflow goes to the `Extract from XLSX` node <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Google Docs/Raw Text**: As a fallback, if the file type is a Google Doc (`application/vnd.google-apps.document`) or another simple format (like `.csv`, `.md`, raw text), the workflow uses the general `Extract Document Text` node <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Mime Type Reference

Google Workspace documentation provides a comprehensive list of mime types, which is a valuable resource for extending the workflow to support even more file types <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Alternatively, one can upload a file, trigger the workflow, and inspect the `mime type` in the input data <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Handling Varying Output Fields

A critical "golden nugget" for [[building_ai_agents_with_n8n | building AI agents]] is that different extract nodes output text to different fields <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>:
*   `Extract Document Text` (for Google Docs/raw text) outputs to `json.data` <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   `Extract from PDF` outputs to `json.text` <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   The final step for `Extract from XLSX` (after aggregation/summarization) outputs to `concatenatedData` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

To accommodate this, the document loader (which splits text into chunks) must be configured to check for these different attribute names using JavaScript's logical OR operator (e.g., `json.text || json.data || json.concatenatedData`) <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

### Specific File Type Extraction Details

*   **Google Doc**: A simple `Extract Document Text` node is sufficient <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **PDF Document**: The `Extract from PDF` node handles extraction <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Excel Document**: Processing Excel files for RAG can be complex due to their tabular nature. A simple approach is to extract everything into a table format, aggregate records into a single item, and then summarize it into a single string for chunking, similar to a raw text file <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. More advanced methods could involve creating a vector database record for every row, depending on the use case <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Testing and Verification

After setting up the ingestion workflow, test by uploading different document types to Google Drive (e.g., PDF, Excel).
*   The workflow will automatically detect the file type and branch to the correct extraction path <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   The extracted content will be inserted into the vector database (e.g., Superbase documents table) <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   Finally, query the RAG AI agent with questions based on the content of the newly ingested documents to verify that the agent can retrieve relevant information from the knowledge base <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

For instance, asking about "action items for Chris" (from a sample PDF) should yield accurate results based on the extracted and vectorized PDF content <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. The agent successfully fetches the relevant chunks from the knowledge base to answer the question <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

## Conclusion

This approach provides a robust method for [[building_a_nocode_rag_ai_agent | building a nocode RAG AI agent]] in n8n that can handle various document types beyond simple text files. By strategically utilizing n8n's diverse extract nodes and conditional branching based on mime types, users can easily populate their AI agent's knowledge base with PDFs, Excel files, and more, making for powerful and versatile AI workflows <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Further exploration into how to best chunk and ingest tabular data for different use cases can enhance the system even more <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.