---
title: Retrieval Augmented Generation RAG methods
videoId: T2QWhXpnT5I
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation | Retrieval Augmented Generation (RAG)]] is the most widely adopted method to provide AI agents with access to a knowledge base, making them domain experts on documents for Q&A tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, [[retrieval_augmented_generation_rag_and_its_challenges | RAG]] by itself is often not powerful enough <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. To address this, [[advanced_rag_implementation_techniques | agentic RAG]] has emerged as a more powerful and flexible way to level up [[retrieval_augmented_generation | RAG]] for different document types <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[basics_of_retrieval_augmented_generation_rag | Naive/Traditional RAG]]

[[basics_of_retrieval_augmented_generation_rag | Naive RAG]], also known as traditional [[retrieval_augmented_generation | RAG]], involves a "one-shot" lookup process <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

The process is as follows:
1.  **Document Processing**: All documents are split into chunks, creating bite-sized information <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  **Embedding**: An embedding model converts these chunks into vectors <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  **Storage**: These vectors are stored in a vector database like Superbase, Qdrant, or Pinecone <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
4.  **Query Processing**: When a user's question comes in, the same embedding model converts it into a vector <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
5.  **Retrieval**: Vector mathematics are used to match the question's vector with the most relevant document chunks in the database <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
6.  **Prompt Construction**: The retrieved chunks, along with a system prompt and the user's question, are combined into a single prompt for the Large Language Model (LLM) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
7.  **Response Generation**: The LLM generates a response based on this prompt <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Limitations of [[basics_of_retrieval_augmented_generation_rag | Naive RAG]]
The primary problem with [[basics_of_retrieval_augmented_generation_rag | naive RAG]] is that it is a "one-shot" process <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The LLM only performs a single lookup in the vector database and lacks the ability to:
*   Rethink or reword the user's question <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Search different vector databases <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Look at the data in alternative ways <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   Reason about how it explores the knowledge base <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## [[advanced_rag_implementation_techniques | Agentic RAG]]

[[advanced_rag_implementation_techniques | Agentic RAG]] addresses the limitations of [[basics_of_retrieval_augmented_generation_rag | naive RAG]] by introducing an agent that comes *before* the LLM <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This agent is equipped with tools, allowing it to perform [[retrieval_augmented_generation | RAG]] and explore the knowledge base in more dynamic ways <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

With [[advanced_rag_implementation_techniques | agentic RAG]], the agent can:
*   Search through multiple vector databases and decide when to use each one <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This provides more reasoning in the retrieval process <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   Utilize other tools like web search to find information differently <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Look at the knowledge base in various ways, not just through vector mathematics-based retrieval <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   Reason about how it retrieves information from the knowledge base, offering endless possibilities for exploration <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## [[enhancing_ai_agents_with_rag_technology | N8N Agentic RAG Workflow Implementation (Local AI Version)]]

A local AI version of an N8N [[enhancing_ai_agents_with_rag_technology | agentic RAG]] template enables an entirely offline, secure, and powerful [[retrieval_augmented_generation | RAG]] agent <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This implementation uses local AI services like Ollama and a self-hosted Superbase or PostgreSQL database <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Database Setup

The database is crucial for storing conversation history and the entire knowledge base <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
1.  **PostgreSQL Credentials**: Set up PostgreSQL credentials, typically referencing `DB` for a Docker Compose stack or `Localhost` for a local setup <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. Default database and user are `postgres`, with port `5432` <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
2.  **Table Creation**:
    *   **Document Metadata Table**: Stores high-level information about documents, allowing the LLM to list available documents and their schemas <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
    *   **Document Rows Table**: Stores all records for tabular files (like CSV/Excel) in a `JsonB` column, enabling different structures to be stored in one table <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
    *   **Documents Table**: Stores embeddings for [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The PostgreSQL PG Vector store node automatically creates this table <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Knowledge Base Setup (RAG Pipeline)

This pipeline adds local files to the knowledge base <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
1.  **Local File Trigger**: Watches a specified local folder for added or changed files <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
2.  **Metadata Setting**: Extracts file ID (using the path), file type, and title <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
3.  **Clean Slate**: Deletes old document records and table rows associated with the file from the knowledge base to ensure only updated information is present <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
4.  **Document Metadata Insertion**: Inserts initial record into the document metadata table <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
5.  **File Reading and Content Extraction**: Reads the binary data of the file into the N8N instance <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. A switch statement handles different file types (PDF, CSV, text) for content extraction <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
6.  **Embedding and Storage (PG Vector Store)**:
    *   Takes the extracted text, splits it into chunks, and stores it in the `documents_PG` table <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
    *   Uses an Ollama embedding model (e.g., `namic-embed-text`) <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
    *   Adds metadata (file ID, title) to records, allowing the LLM to cite sources <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
    *   Employs a recursive character text splitter with a chunk size of 400 <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.
7.  **CSV and Excel File Specific Handling**:
    *   **Insert Table Rows**: Data for each row is extracted and inserted into the `document_rows` table as `JsonB` <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
    *   **Summarize for RAG**: All rows are aggregated and summarized to create a text representation of the entire table, which is then added to the knowledge base for regular [[retrieval_augmented_generation | RAG]] lookups <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
    *   **Set Schema**: The columns from the tabular file are extracted and updated in the `document_metadata` table, informing the LLM how to write SQL queries against the `row_data` <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

### AI Agent Setup

This part configures the agent for interaction and tool usage <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.
1.  **Triggers**:
    *   **Chat Trigger**: Enables interaction directly within the N8N UI <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.
    *   **Webhook**: Allows the agent to be used as an API endpoint <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.
2.  **Tools Agent**:
    *   **System Prompt**: Informs the LLM it's a personal assistant with [[advanced_rag_implementation_techniques | agentic RAG]] tools and provides instructions on when to use each tool <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.
    *   **Chat Memory**: Uses PostgreSQL chat memory to store conversation history, automatically creating the `n8n_chat_histories` table <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
    *   **Chat Model**: For Ollama, the Open AI credentials are used by changing the base URL to point to the Ollama container (e.g., `http://ollama:11434` or `http://localhost:11434`) <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>. This is a workaround for a known N8N glitch with the dedicated Chat Ollama model node and [[retrieval_augmented_generation | RAG]] tools <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
3.  **Agent Tools**:
    *   **[[retrieval_augmented_generation | RAG]] Tool**: A basic [[retrieval_augmented_generation | RAG]] lookup using the PostgreSQL PG Vector store node <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. It includes metadata like file title and ID to allow the LLM to cite sources <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
    *   **List Documents Tool**: Lists available documents from the `documents_metadata` table <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
    *   **Get File Contents Tool**: Queries the `documents_PG` table to combine all chunks for a single document to retrieve its full text <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.
    *   **Query Tabular Data Tool**: Allows the LLM to completely generate SQL queries to analyze tabular data in the `document_rows` table <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>. The tool's description provides examples of good SQL queries to guide the LLM <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

## Local AI Considerations: Ollama Context Length

A significant challenge with local LLMs, particularly Ollama models, is their default context length of 2,000 tokens <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. When prompts become longer due to [[retrieval_augmented_generation | RAG]] lookups, crucial information like system prompts and tool instructions can be overridden <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.

To resolve this, custom Ollama model files can be created to increase the context length (e.g., to 8,000 tokens) <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. This involves:
1.  **Creating a Modelfile**: Using a command-line interface to inherit from the base model and set the desired context length parameter <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.
2.  **Creating a New Model Version**: A command then creates a new version of the model based on this Modelfile, using the already downloaded base model to do so instantly <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>.

This ensures the LLM does not "hallucinate completely" when handling larger contexts from tool invocations and knowledge base data <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.