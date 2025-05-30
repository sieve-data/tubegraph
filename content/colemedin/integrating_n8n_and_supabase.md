---
title: Integrating n8n and Supabase
videoId: PEI_ePNNfJQ
---

From: [[colemedin]] <br/> 

Most RAG (Retrieval-Augmented Generation) tutorials on platforms like YouTube, especially those focusing on "chat with your PDF" documents, often fail to demonstrate how to build systems that are truly production-ready <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These basic setups can encounter issues as a knowledge base expands, documents are updated, or users ask unexpected questions <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This article outlines how to construct a robust RAG AI agent using a no-code approach with [[ai_automation_with_n8n | n8n]] and [[supabase_as_an_opensource_platform | Supabase]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Why n8n and Supabase?

The combination of [[ai_automation_with_n8n | n8n]] and [[supabase_as_an_opensource_platform | Supabase]] allows for the creation of a production-ready, cost-effective, no-code, and easily understandable RAG AI agent that can utilize virtually any document as a knowledge base <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### n8n: Workflow Automation for AI

[[ai_automation_with_n8n | n8n]] is described as an "incredible and cost-effective" [[workflow_automation_with_n8n | workflow automation]] tool, often compared to platforms like make.com and Zapier <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Its user-friendly interface makes it ideal for building [[using_n8n_to_build_an_ai_knowledge_base | AI knowledge bases]] and [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]] without needing to write code <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. [[ai_automation_with_n8n | n8n]] provides a chat widget within its environment, simplifying the testing and debugging of AI agents during development <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This widget can also be embedded directly onto a website without additional coding <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Supabase: The Backend for AI

[[supabase_as_an_opensource_platform | Supabase]] is highlighted as an excellent database platform that supports vectors for RAG applications using PG vector <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. A key advantage of [[supabase_as_an_opensource_platform | Supabase]] is its versatility, allowing it to serve both as a chat memory store and a vector database simultaneously <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. It offers a free tier that is sufficient for initial development and scaling <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Setting Up Supabase

To integrate with [[ai_automation_with_n8n | n8n]], a [[supabase_as_an_opensource_platform | Supabase]] account is necessary. After signing in, users gain access to a dashboard <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Key credentials needed from [[supabase_as_an_opensource_platform | Supabase]] are:
*   **Postgres Connection (for chat memory):** Found under `Project Settings` > `Database`, this section provides the host, database name, port, user, and password <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **API Connection (for vector database):** Located under `Project Settings` > `API`, users can find their unique URL and reveal/copy their `service_role secret` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

For RAG functionality, specific SQL commands need to be run in the [[supabase_as_an_opensource_platform | Supabase]] SQL editor <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. These commands set up:
1.  The PG Vector extension, enabling vector storage <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
2.  A `documents` table to store metadata, content, and embeddings for knowledge base documents <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
3.  A function to match documents for RAG <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

[[ai_automation_with_n8n | n8n]] can automatically create the chat history table in [[supabase_as_an_opensource_platform | Supabase]] if it doesn't already exist <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Building the RAG AI Agent Workflow in n8n

The [[ai_automation_with_n8n | n8n]] workflow for this RAG AI agent is designed to be easily downloadable and importable via a JSON file from a GitHub repository <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Once imported, users only need to configure credentials for services like Google Drive and [[supabase_as_an_opensource_platform | Supabase]], and customize their knowledge base folder in Google Drive <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The workflow consists of two main parts: the AI agent (for answering questions) and the document ingestion process (for updating the knowledge base).

### 1. AI Agent Workflow

The AI agent workflow is triggered when a chat message is received <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
It comprises several key nodes:

*   **Chat Trigger Node:** This node initiates the workflow when a user sends a message through the [[ai_automation_with_n8n | n8n]] chat widget <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. It provides the session ID (for chat memory) and the user's input query <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **AI Agent Node:** This central node orchestrates the AI's response <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. It takes the chat input and a system message as input.
    *   **Chat Model:** Configured to use a model like GPT-4o mini, though other options like Anthropic are available <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Requires an OpenAI API key <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   **Chat Memory:** Crucially, this uses a Postgres connection to [[supabase_as_an_opensource_platform | Supabase]] instead of local memory (which can overload the server) <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This ensures scalability for production readiness <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Credentials are the host, database, user, and password obtained from [[supabase_as_an_opensource_platform | Supabase]] <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. [[ai_automation_with_n8n | n8n]] can even create the necessary table in [[supabase_as_an_opensource_platform | Supabase]] automatically <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   **Tools for RAG:** A "retrieve documents" tool is used, specifically connecting to the [[supabase_as_an_opensource_platform | Supabase]] vector store <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This requires the [[supabase_as_an_opensource_platform | Supabase]] host and `service_role secret` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. The `documents` table and `match_documents` query are selected <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

### 2. Document Ingestion Workflow

This workflow automatically updates the knowledge base when files are created or modified in Google Drive <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This demonstrates [[integrating_google_drive_with_n8n_for_document_management | integrating Google Drive with n8n for document management]].

*   **Google Drive Trigger Node:** This node polls a specified Google Drive folder (e.g., "meeting notes") for new or updated files <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Google credentials need to be set up, with [[ai_automation_with_n8n | n8n]] providing documentation for this <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Code Node:** [[extracting_and_processing_data_in_n8n | This node extracts the file ID]] from the Google Drive trigger output, passing it to subsequent steps <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Supabase Node (Delete Old Vectors):** A critical step that many tutorials omit is managing duplicates <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Before inserting new data, this node deletes any existing vectors in the [[supabase_as_an_opensource_platform | Supabase]] database that correspond to the file being updated <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This prevents duplicate knowledge from accumulating, which would negatively impact RAG performance <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. The file ID is stored in the metadata of the vectors for this purpose <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Google Drive Download Node:** Downloads the file locally using its ID <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. It converts documents to text and Google Sheets to CSV for raw text extraction <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. [[extracting_and_processing_data_in_n8n | This ensures the content is in a usable format for embedding]].
*   **Supabase Node (Insert New Vector):** The final step inserts the processed raw text into the [[supabase_as_an_opensource_platform | Supabase]] vector database <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. It uses the same [[supabase_as_an_opensource_platform | Supabase]] credentials and targets the `documents` table with the `match_documents` query <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. The workflow automatically handles chunking for larger files using an OpenAI embeddings model and a recursive character text splitter <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

This comprehensive workflow provides a robust, no-code solution for a RAG AI agent, capable of handling dynamic knowledge bases and delivering accurate answers based on document content <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. While enhancements like better semantic or keyword search can always be added, this setup provides a very solid foundation for a production-ready application <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.