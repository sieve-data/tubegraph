---
title: Setting up and optimizing chat memory for AI agents
videoId: PEI_ePNNfJQ
---

From: [[colemedin]] <br/> 

Most online tutorials for Retrieval Augmented Generation (RAG) often demonstrate basic "chat with your PDF" concepts that are not suitable for real-world production use, requiring significant changes for scalability and robustness <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These basic setups can encounter issues as the knowledge base grows, documents are updated, and users ask unexpected questions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

A more robust RAG [[building_ai_agents | AI agent]] can be built with no code using n8n for workflow automation and Superbase for database and vector storage <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Superbase is highlighted as an excellent and cost-effective database platform that supports vectors for RAG using PG Vector <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This combination allows for the creation of a production-ready, cost-effective, no-code, and easily understandable RAG [[understanding_ai_agents | AI agent]] capable of using any documents as a knowledge base <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Demonstration of Agent's Learning Capability

Initially, the RAG knowledge base in Superbase's documents table is empty, preventing the [[understanding_ai_agents | AI agent]] from answering questions that require document knowledge <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For example, asking about "action items from the 825 meeting" yields no answer <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

To enable the agent to answer, a new Google Doc with the relevant meeting notes is created in a designated knowledge base folder <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. An n8n workflow then triggers, processing the new document and adding it to the RAG knowledge base <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Within approximately a minute, the document content is inserted into the Superbase documents table, including its metadata and embedding vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Once the document is in the knowledge base, the agent can correctly answer the previously unanswerable question <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This system also handles updates to Google Drive files <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Setting up the RAG AI Agent Workflow

A pre-built n8n workflow for this RAG [[understanding_ai_agents | AI agent]] is available via a GitHub repository, allowing users to download the JSON file and import it into their n8n instance <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. After importing, users only need to provide credentials for services like Google Drive and Superbase, and customize the knowledge base folder <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Superbase Configuration for AI Chat Memory and Vector Database

Superbase is utilized for both [[implementing_longterm_and_shortterm_memory_in_ai_agents | chat memory]] and as a vector database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

1.  **Account Setup**: Sign in to Superbase with a GitHub account. A generous free tier is available, sufficient for getting started and scaling an [[building_ai_agents | AI app]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  **Getting Credentials**:
    *   **Postgres Connection**: Navigate to "Project settings" > "Database" to find host, database name, port, user, and password for Postgres connection, used for [[using_postgres_and_superbase_for_ai_chat_memory | chat memory]] <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
    *   **API Connection**: Go to the "API" tab to retrieve the custom URL and service role secret, needed for the vector database <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
3.  **Database Setup**: Superbase needs to be configured with PG Vector and specific tables. n8n documentation provides SQL code to set up the vector store, including creating the PG Vector extension, a `documents` table, and a function for RAG matching <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This SQL code is run in Superbase's SQL editor <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. The `documents` table stores metadata, content, and embeddings for all documents in the knowledge base <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Additionally, n8n automatically creates a table for [[implementing_longterm_and_shortterm_memory_in_ai_agents | chat history]] <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### n8n Workflow Details

The n8n workflow begins with a "Chat Message Received" trigger <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This trigger provides a chat widget within n8n, enabling easy testing and debugging of [[building_ai_agents | AI agents]] without external deployments <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The output of this trigger includes a session ID for chat memory and the user's input to the [[understanding_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

The [[understanding_ai_agents | AI agent]] node receives the chat input and uses a system message for setup <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. It connects to:
*   **Chat Model**: GPT-4 Mini (or other GPT/Anthropic options) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Credentials for OpenAI API keys are straightforward to set up <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **[[implementing_longterm_and_shortterm_memory_in_ai_agents | Chat Memory]]**: This is a critical component for scalable [[understanding_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

#### Scalable Chat Memory with Postgres and Superbase

Unlike many tutorials that use windowed buffered memory (which stores chat memory locally and can overload the server) <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, using Postgres with Superbase for [[implementing_longterm_and_shortterm_memory_in_ai_agents | chat memory]] makes the [[understanding_ai_agents | AI agent]] truly scalable and production-ready <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

To set up [[using_postgres_and_superbase_for_ai_chat_memory | Postgres-based chat memory]], use the Superbase host, database, user, and password obtained from the Superbase dashboard <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. n8n can automatically create the necessary table in Superbase if it doesn't already exist <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

*   **Tools for RAG**: The agent uses a "Retrieve Documents" tool, specifically connecting to Superbase as the vector store <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Credentials for this require the host and service role secret from Superbase <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Optimizing for Document Updates (Avoiding Duplicates)

A key optimization for the RAG knowledge base is handling document updates to prevent duplicates <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. When a Google Drive file is created or updated, a separate n8n workflow triggers <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

1.  **Extract File ID**: The workflow first extracts the file ID from the Google Drive trigger <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
2.  **Delete Old Vectors**: Crucially, before inserting new content, all existing vectors in the Superbase database associated with that specific file ID are deleted <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This is vital because vector databases, including Superbase when used via n8n's integrations, typically perform inserts, not upserts (update if exists, otherwise insert). Without this deletion step, each update to a document would create a duplicate vector, leading to corrupted knowledge and poorer RAG performance <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. The file ID is stored in the metadata of each vector for this purpose <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
3.  **Download and Extract Content**: The file is downloaded locally, and its text content is extracted (e.g., converting Google Docs to text or Sheets to CSV) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
4.  **Insert New Vector**: Finally, the extracted text content is inserted into the Superbase vector database <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This step utilizes OpenAI embeddings and a recursive character text splitter for efficient chunking of larger documents <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

This end-to-end setup results in a fully functioning and production-ready RAG [[understanding_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. While further enhancements like better semantic or keyword search can be added, this provides a very solid foundation <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.