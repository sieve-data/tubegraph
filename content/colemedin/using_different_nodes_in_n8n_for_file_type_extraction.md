---
title: Using different nodes in n8n for file type extraction
videoId: T1ZKEmDN8AA
---

From: [[colemedin]] <br/> 

[[creating_rag_ai_agents_using_n8n | Creating RAG AI agents]] with [[ai_automation_with_n8n | n8n]] is straightforward, particularly with the AI agent node, vector store retrieval, and document inserter tools [00:00:00]. However, the most challenging aspect is often extracting text from various document types for your knowledge base [00:00:14]. This is especially true for PDFs or other formats that don't easily convert to raw text [00:00:23].

## The Challenge of File Type Extraction in n8n

While the general setup for [[creating_rag_ai_agents_using_n8n | RAG AI agents]] using a vector database like Superbase tends to work well, extending workflows to handle diverse document types such as PDFs or Excel files can be tricky [00:00:43]. [[ai_automation_with_n8n | n8n]] does not offer a single node to extract text from every file type, making the problem non-trivial [00:01:01].

## Solution: Branching Workflows for Different File Types

To overcome this, [[ai_automation_with_n8n | n8n]] workflows can be designed to branch based on the file type, directing each file to a specific extraction node [00:02:15]. This approach allows for working with PDF, Excel, and other document types, integrating them into a knowledge base for a [[creating_rag_ai_agents_using_n8n | RAG AI agent]] [00:00:52].

### Identifying File Types with Mime Type

The key to branching is identifying the file type using the `mime type` parameter, which is available from the trigger output when a file is created or updated in a source like Google Drive [00:05:11].
*   For a Google Doc, the mime type is `application/vnd.google-apps.document` [00:05:32].
*   For a PDF, it would be `application/pdf` [00:05:43].
*   For an Excel document, it is `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` [00:08:56].

The Google Workspace documentation provides a comprehensive list of mime types that can be used as a reference to extend workflows for other file types [00:09:44]. Alternatively, you can upload a file, trigger the workflow, and inspect the mime type directly from the trigger output [00:10:22].

### Specific Extraction Nodes in n8n

When adding a new node, searching for "extract" reveals various specialized nodes for different file types [00:07:35]:
*   **Extract from PDF:** Used for PDF documents [00:07:47, 00:08:42].
*   **Extract from XLSX:** Used for Excel documents [00:07:47, 00:09:03].
*   **Extract Document Text:** Suitable for simpler file types like text files, Google Docs, Markdown, or CSVs [00:07:14, 00:09:12]. This node also serves as a fallback for file types not explicitly handled by specific branches [00:09:21].

### Workflow Overview for Document Ingestion

The ingestion workflow for documents into a knowledge base typically begins with two triggers [00:04:06]:
1.  **File Created Trigger:** Activates when a new file is added to a specified Google Drive folder [00:04:21].
2.  **File Updated Trigger:** Activates when an existing file in the same folder is modified [00:04:30].

[[ai_automation_with_n8n | n8n]] polls this folder every minute for changes [00:04:36]. Upon a trigger event, the workflow proceeds as follows:
1.  **Delete Old Records:** All previous records for the document are deleted from the vector store to ensure a fresh set of vectors and prevent the LLM from being confused by old versions [00:06:32].
2.  **Download File:** The file is downloaded onto the [[ai_automation_with_n8n | n8n]] instance, ready for text extraction [00:06:51].
3.  **Switch Node for Branching:** A switch node evaluates the `file type` (derived from the mime type) to route the file to the appropriate extraction branch [00:08:12, 00:11:47].
    *   If `application/pdf`, it goes to the PDF extraction branch [00:08:36].
    *   If `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (Excel), it goes to the Excel extraction branch [00:08:59].
    *   If `application/vnd.google-apps.document` (Google Doc) or any other non-specified text-based format, it defaults to the `Extract Document Text` node [00:09:09, 00:09:21].

### Handling Varied Output Fields

A critical detail is that different extraction nodes output text to different fields [00:12:45]:
*   `Extract Document Text` outputs to a field called `data` (i.e., `json.data`) [00:12:51, 00:13:27].
*   `Extract from PDF` outputs to an attribute called `text` (i.e., `json.text`) [00:12:55, 00:13:39].
*   The Excel extraction process ultimately outputs to a field called `concatenatedData` [00:14:07].

When configuring the default document loader, it's crucial to reference these potential output fields to ensure the extracted text is correctly loaded for chunking and insertion into the vector database [00:13:08, 00:14:12]. This can be done using JavaScript's logical OR operator (e.g., `json.data || json.text || json.concatenatedData`) to prioritize existing attributes [00:14:48].

After extraction, the text is inserted into the vector database for the [[creating_rag_ai_agents_using_n8n | RAG AI agent]] to use [00:11:06].

### Example Demonstrations

*   **Google Doc:** A Google Doc (e.g., meeting notes) is processed via the default `Extract Document Text` node, and its content is inserted into the vector database [00:11:01].
*   **PDF Document:** A PDF document is uploaded, recognized by its `application/pdf` mime type, and routed to the `Extract from PDF` node. The extracted text is then chunked and inserted, potentially resulting in multiple records [00:11:16, 00:12:31, 00:14:24]. For example, a PDF might be split into four chunks [00:14:27].
*   **Excel Document:** An Excel file is uploaded, identified by its specific mime type, and processed through a sequence of nodes (`Extract from XLSX`, `Aggregate`, `Summarize`) to convert its structured data into a single string for chunking and insertion [00:14:34, 00:15:17]. The method of processing tabular data can vary based on the specific use case, such as creating a record for every row or aggregating multiple rows [00:16:03].

Once documents are ingested, the [[creating_rag_ai_agents_using_n8n | RAG AI agent]] can retrieve relevant information from the vector database based on user queries [00:16:49]. For instance, asking "what are the action items for Chris" based on a PDF document stored in the knowledge base will yield an accurate answer derived from the extracted chunks [00:17:10].