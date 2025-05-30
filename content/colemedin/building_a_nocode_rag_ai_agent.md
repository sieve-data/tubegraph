---
title: Building a nocode RAG AI agent
videoId: PEI_ePNNfJQ
---

From: [[colemedin]] <br/> 

Traditional RAG (Retrieval Augmented Generation) tutorials often focus on basic "chat with your PDF" applications that are not production-ready and would require significant changes to be usable for real-world scenarios <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These basic setups can encounter issues as knowledge bases grow, documents update, and unexpected user questions arise <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This article details how to build a robust [[rag_ai_agent_development | RAG AI agent]] using [[building_ai_agents_with_nocode_tools | nocode]] tools n8n and Superbase <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Key Tools: n8n and Superbase

This [[agentic_rag_ai_agent_template | RAG AI agent template]] leverages two powerful tools:
*   **n8n:** An effective and cost-efficient workflow automation tool, similar to Make.com or Zapier <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Superbase:** Described as an excellent database platform that supports vectors for RAG using PG vector <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Combining n8n and Superbase allows for [[creating_rag_ai_agents_using_n8n | creating a production-ready]], cost-effective, [[no_code_ai_agent_builders | nocode]], and easy-to-understand [[n8n_rag_ai_agent | RAG AI agent]] that can use any document as a knowledge base <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The setup process for this [[rag_ai_agent_development | RAG AI agent development]] can be completed in less than 15 minutes <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Agent Capabilities Demonstration

Initially, when the RAG knowledge base in Superbase's documents table is empty, the agent cannot answer specific questions, such as "what are the action items from the 825 meeting" <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

To enable the agent to answer, a new document (e.g., "825 meeting notes" from Google Docs) is added to the designated knowledge base folder <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. An n8n workflow automatically triggers, adds the document content, metadata (like Google Drive file ID), and the embedding vector into the Superbase documents table <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. After this update, the agent can accurately retrieve and answer the question using the newly added document <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The system also handles updates to Google Drive files automatically <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Setting Up the n8n Workflow

A pre-built n8n workflow for this [[rag_ai_agent_development | RAG AI agent]] is available as a JSON file, which can be easily imported into any n8n instance <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Users only need to provide their credentials for services like Google Drive and Superbase, and optionally customize the knowledge base folder in Google Drive <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Superbase Setup for Chat Memory and Vector Database

Superbase serves as both the chat memory and the vector database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
1.  **Account Setup**: Sign in to Supabase.com, often with a GitHub account. The free tier is sufficient for getting started <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  **Credentials for PostgreSQL (Chat Memory)**: Access project settings > Database to find the host, database name, port, user, and password for PostgreSQL connection <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
3.  **Credentials for API (Vector Database)**: Access project settings > API to find the URL and service role secret <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
4.  **SQL Setup for Vector Store**: n8n provides documentation with SQL code to set up the Superbase vector store <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This code creates the `PG Vector` extension, the `documents` table (for RAG knowledge base), and a function to match for RAG <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. This SQL can be pasted and run in Superbase's SQL editor <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. n8n will automatically create the table for chat history if it doesn't exist <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## n8n Workflow Walkthrough

### 1. Chat Message Trigger (User Interaction)

*   The workflow begins with a "Chat Message Received" trigger <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   This trigger creates a chat widget in n8n for easy testing and debugging of the [[rag_ai_agent_development | AI agent]] <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   The output from this trigger includes the session ID (for chat memory) and the input to the AI agent <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   The chat widget can also be embedded on a website without writing any code <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### 2. AI Agent Configuration

*   The [[rag_ai_agent_development | AI agent]] node receives the chat input from the trigger <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   A system message helps set up the agent's behavior <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Chat Model**: Uses GPT-4o mini, but any GPT option or alternatives like Anthropic can be used <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Credentials for OpenAI are set up via API key <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Chat Memory**: Uses PostgreSQL with Superbase for scalable chat memory <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This is more robust than local "windowed buffered memory" which can overload the server <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Tools for RAG**: Employs the "Retrieve Documents" tool, specifically the Superbase vector store, for RAG <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

### 3. Google Drive File Management Workflow

This part of the workflow handles adding or updating files in the knowledge base from Google Drive.
*   **Google Drive Trigger**: This trigger polls for files created or updated in a specific Google Drive folder (e.g., "meeting notes folder") <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. n8n provides documentation for setting up Google credentials <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Extract File ID**: Extracts the file ID from the Google Drive trigger's output to be used in subsequent steps <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Delete Old Vectors (Superbase)**: Crucially, this step deletes any existing vectors for the current file from the Superbase database using the file ID stored in the metadata <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This prevents duplicate knowledge entries when documents are updated, as vector databases like Superbase don't natively "upsert" (update if exists) vectors based on file IDs <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Download File**: Downloads the Google Drive file locally and converts documents to text (e.g., Google Docs to text, Google Sheets to CSV) to extract raw content <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Insert into Superbase Vector Database**: The final step inserts the raw text content into the Superbase vector database <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This uses OpenAI embeddings and a default document loader with a recursive character text splitter for chunking <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

## Conclusion

This [[enhancing_ai_agents_with_rag_technology | robust RAG AI agent]] built with [[building_ai_agents_with_lightrag | LightRAG]] principles, n8n, and Superbase provides a production-ready foundation for [[rag_ai_agent_development | AI agent development]] <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. While enhancements like better semantic or keyword search can be added, this setup offers a solid starting point for a scalable and efficient RAG application <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.