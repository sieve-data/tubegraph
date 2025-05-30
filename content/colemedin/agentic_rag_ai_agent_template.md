---
title: Agentic RAG AI agent template
videoId: T2QWhXpnT5I
---

From: [[colemedin]] <br/> 

[[rag_ai_agent_development | Retrieval Augmented Generation (RAG)]] is the most widely adopted method for giving AI agents access to a knowledge base, essentially making them domain experts on specific documents for Q&A <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, RAG by itself is often not powerful enough <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This limitation led to the development of [[agentic_rag_strategy_and_implementation | agentic RAG]], which significantly enhances RAG's power and flexibility, allowing it to work with diverse document types <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

An [[creating_rag_ai_agents_using_n8n | n8n agentic RAG AI agent template]] is available, serving as a no-code starting point for [[agentic_rag_setup | building an agentic RAG system]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Following overwhelming community demand, a local AI version of this template has been introduced <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Why Local AI?

Local AI allows users to control all their data and Large Language Models (LLMs), which is seen as the future direction for generative AI <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The local version of the [[creating_rag_ai_agents_using_n8n | n8n agentic RAG template]] offers a 100% offline, secure, and powerful [[rag_ai_agent_development | RAG agent]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Understanding Agentic RAG vs. Traditional RAG

A clear way to understand [[agentic_rag_strategy_and_implementation | agentic RAG]] is by comparing it to traditional, or "naive," [[rag_ai_agent_development | RAG]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>:

### Naive/Traditional RAG

In traditional [[rag_ai_agent_development | RAG]], the process involves:
1.  **Document Processing**: Documents are split into chunks.
2.  **Embeddings**: An embedding model converts chunks into vectors.
3.  **Vector Database Storage**: Vectors are stored in a vector database (e.g., Superbase, Qdrant, Pinecone) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
4.  **Query Processing**: A user's question is also turned into a vector using the same embedding model <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
5.  **Retrieval**: Vector mathematics match the question to the most relevant document chunks <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
6.  **Prompt Combination**: The relevant chunks are combined with a system prompt and the user's question into a single prompt for the LLM <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
7.  **Response**: The LLM provides an answer based on the provided chunks <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

**Limitation**: This approach is "one-shot" – information is looked up only once. The LLM has no ability to reason, rephrase questions, search different databases, or explore data in varied ways <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Agentic RAG

[[agentic_rag_strategy_and_implementation | Agentic RAG]] introduces an agent that acts *before* retrieval <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This agent has access to various tools, enabling it to:
*   Perform [[rag_ai_agent_development | RAG]] <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Explore the knowledge base in different ways <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   Search through multiple vector databases and decide when to use each <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Utilize other tools like web search for external information <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Look at the knowledge base in ways other than just vector similarity, leading to an "endless amount of possibilities" for exploring the knowledge base <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. The agent reasons about how to explore the knowledge base <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## The Local [[creating_rag_ai_agents_using_n8n | n8n Agentic RAG Template]]

This template is very similar to its cloud counterpart, but utilizes local AI services like Ollama for LLMs and a self-hosted Superbase (or Postgres) for the database <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Its [[agentic_rag_strategy_and_implementation | agentic RAG]] capability stems from giving the agent various tools to interact with the Postgres database, allowing it to explore the knowledge base in different ways <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Demonstrating Agentic Capabilities

Using Qwen 2.5 14B as the local LLM <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>, the agent can demonstrate advanced reasoning:

*   **Basic RAG Lookup**: For a straightforward question like "Who is the CEO of the company?", the agent performs a simple [[rag_ai_agent_development | RAG]] lookup and correctly identifies the CEO, Dr. Alisa Vanderhoven <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Contextual Document Retrieval**: When asked "Who was in the Feb 12th meeting?", a question where naive RAG might fail due to pulling irrelevant chunks, the agent instead uses tools to:
    1.  List all available documents in the knowledge base <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    2.  Select and read the entire "meeting minutes" document for February 12th <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    3.  Extract the list of attendees, demonstrating its ability to explore documents beyond simple chunk retrieval <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Tabular Data Analysis (SQL Queries)**: Traditional [[rag_ai_agent_development | RAG]] often performs poorly with tabular data, especially for calculations like averages, because it might only pull partial table chunks and LLMs struggle with math on their own <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This template includes a tool that allows the agent to treat Excel and CSV files as SQL tables, enabling it to write and execute SQL queries <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. For example, when asked "What is the average overall score based on the customer feedback?", the agent generates and executes a SQL query to calculate the average, returning the correct value of 7.89 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

**Performance Note**: Results can be inconsistent depending on the local LLM used, as smaller models may not perform as well as powerful cloud LLMs like Claude 3.7 Sonnet or GPT-4o <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. However, the power of local AI for secure and offline operations is significant <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

## [[agentic_rag_setup | Setting Up the Template]]

The JSON workflow for this template is available for download as part of a local AI package repository <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Database Setup

The database is crucial for storing conversation history and the knowledge base <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Credentials**: Set up Postgres credentials (host, user, password, port 5432) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. If not using the local AI package, the host will differ from `DB` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Table Creation**:
    *   `document_metadata`: Stores high-level document information. This table allows the LLM to list available documents and provides schema information for tabular files, guiding SQL query generation <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
    *   `document_rows`: Stores all tabular data records using a `JsonB` column, enabling storage of files with different structures in one table <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Queries are performed on this `row_data` column <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   `documents_pg`: Stores embeddings for [[rag_ai_agent_development | RAG]]. This table is automatically created by the Postgres PG Vector store node <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. Note that the text column name differs from the Superbase vector node (`text` vs. `content`), requiring recreation if migrating <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### Knowledge Base Setup (RAG Pipeline)

This pipeline handles adding local files to the knowledge base <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>:
*   **Trigger**: A local file trigger watches a specified folder for added or changed files <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This folder is typically mounted onto the [[creating_rag_ai_agents_using_n8n | n8n]] container within the local AI package <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **Workflow per File**:
    1.  **Set Metadata**: Extracts file ID (using path), type, and title <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
    2.  **Clean Slate**: Deletes old document records and table rows from `documents_pg` and `document_rows` if the file has been previously added, ensuring only updated information is present and preventing LLM hallucinations <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
    3.  **Insert Document Metadata**: Adds a new record to the `document_metadata` table <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
    4.  **Read File**: The file's binary data is brought into the [[creating_rag_ai_agents_using_n8n | n8n]] instance <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
    5.  **Extract Text**: A switch statement handles different file types (PDF, CSV, TXT, with expandability for HTML/JSON) by using appropriate "extract from file" nodes <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
    6.  **Insert into Knowledge Base**: The extracted text is dumped into the `documents_pg` table using the PG Vector store node <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
        *   **Embedding Model**: Uses the Ollama embedding model (`nomic-embed-text`) <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
        *   **Text Splitter**: Employs a recursive character text splitter with a chunk size of 400 <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
        *   **Metadata Inclusion**: Includes file ID and title as metadata, allowing the LLM to cite its sources during [[rag_ai_agent_development | RAG]] lookups <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
    7.  **Special Handling for CSV/Excel**:
        *   **Insert Table Rows**: Data from each row is inserted into the `document_rows` table as `JsonB` <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
        *   **Add to RAG Knowledge Base**: The entire table is summarized into a text representation and also inserted into `documents_pg` for basic [[rag_ai_agent_development | RAG]] lookups <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
        *   **Set Schema**: The columns from the file are extracted and updated in the `document_metadata` table, providing the LLM with the table schema for SQL query generation <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

This process enables rapid ingestion of files into the knowledge base <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.

### AI Agent Setup

The agent is set up with triggers and tools:
*   **Triggers**: A chat trigger allows interaction within the [[creating_rag_ai_agents_using_n8n | n8n]] UI, and a webhook enables the agent to be used as an API endpoint <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
*   **System Prompt**: A basic system prompt defines the agent as a personal assistant with [[agentic_rag_strategy_and_implementation | agentic RAG]] tools and provides instructions on tool usage <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.
*   **Chat Memory**: Uses basic Postgres chat memory, which automatically creates an `n8n_chat_histories` table <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
*   **Chat Model**: Despite an OpenAI icon, the model uses Ollama. This workaround is necessary due to an [[creating_rag_ai_agents_using_n8n | n8n]] glitch where the native Chat Ollama model node produces errors when invoking the [[rag_ai_agent_development | RAG]] tool <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>. The base URL is changed to point to the Ollama container (or `localhost` if running locally) <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>.
*   **Tools**:
    *   **[[rag_ai_agent_development | RAG]] Tool**: Uses the Postgres PG Vector node with a basic description for the agent. It limits results to four, includes metadata (title, file ID) for source citation, and uses the Ollama embedding model (`nomic-embed-text`) <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
    *   **List Documents Tool**: Lists documents from the `document_metadata` table <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.
    *   **Get File Contents Tool**: Retrieves the full text of a specific document by combining all chunks from the `documents_pg` table based on a file ID determined by the LLM <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.
    *   **Query Tabular Data Tool**: Allows the LLM to completely generate SQL queries against the `document_rows` table. Examples in the tool's description help guide the LLM in writing effective queries, especially for smaller LLMs prone to hallucinating bad queries <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>.

### Addressing Ollama Context Length Limitations

By default, Ollama models have a context length of only 2,000 tokens <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. This is often insufficient for AI agents, as long prompts or [[rag_ai_agent_development | RAG]] lookups can exceed this limit, causing the LLM to lose crucial information like system prompts and tool instructions <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. While the native Chat Ollama node allows changing context length, the workaround using the OpenAI node (due to the [[rag_ai_agent_development | RAG]] glitch) does not offer this option <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

**Solution**: Users can create a custom Ollama model version with an extended context length (e.g., 8,000 tokens) using a Modelfile <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. This involves:
1.  Creating a Modelfile that inherits from the base model and sets the `parameter` for `context_length` <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
2.  Using the `ollama create` command to build the new model version, which instantly uses the already downloaded base model without re-downloading <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

This ensures the agent doesn't hallucinate when tool invocations and knowledge base data expand the context window, which can easily reach 5,000-7,000 tokens <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

This [[building_a_nocode_rag_ai_agent | no-code]] [[enhancing_ai_agents_with_rag_technology | RAG AI agent]] template showcases the significant power available with local AI <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.