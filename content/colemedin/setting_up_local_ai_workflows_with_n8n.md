---
title: Setting up local AI workflows with n8n
videoId: T2QWhXpnT5I
---

From: [[colemedin]] <br/> 

[[workflow_automation_with_n8n | n8n]] is a powerful tool for [[creating_custom_ai_workflows_with_n8n | creating custom AI workflows]]. Retrieval Augmented Generation (RAG) is a widely adopted method to give AI agents access to a knowledge base, making them domain experts on documents for Q&A <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, RAG by itself is often not powerful enough <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. To address this, [[building_ai_agents_with_n8n | agentic RAG]] has emerged as a way to level up RAG, making it more powerful and flexible for various document types <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

A free [[ai_automation_with_n8n | n8n agentic RAG]] AI agent template is available, providing a starting point for building a no-code agentic RAG system <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Due to popular demand, a local AI version of this template has been developed <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Why Local AI?

Local AI, where users control their data and Large Language Models (LLMs), is considered the future direction for generative AI <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This local version of the [[building_ai_agents_with_n8n | n8n agentic RAG]] template provides a 100% offline, secure, and powerful RAG agent <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Understanding Agentic RAG

To understand the [[building_ai_agents_with_n8n | n8n agentic RAG]] workflow, it's helpful to first understand naive (traditional) RAG and how it evolves into [[building_ai_agents_with_n8n | agentic RAG]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Naive (Traditional) RAG

In traditional RAG:
1.  Documents are split into chunks <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  An embedding model converts these chunks into vectors, which are stored in a vector database (e.g., Superbase, Qdrant, Pinecone) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  A user's question is also converted into a vector using the same embedding model <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
4.  Vector mathematics are used to match the question with the most relevant document chunks <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
5.  The system prompt, user question, and relevant chunks are combined into a single prompt for the LLM <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
6.  The LLM hopefully provides an answer based on the provided chunks <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

The limitation of traditional RAG is that it's a "one-shot" process; the LLM doesn't have the opportunity to reason about how it explores the knowledge base, rewrite questions, or search different databases <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Agentic RAG

[[building_ai_agents_with_n8n | Agentic RAG]] introduces an "agent" first, which then has tools available to perform RAG and explore the knowledge base in other ways <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This allows for more reasoning baked into the retrieval process. For example, an agent can:
*   Search through multiple vector databases and decide when to use each <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Use other tools like web search <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Look at the knowledge base in different ways, not just based on vector mathematics <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

This provides an "endless amount of possibilities" for exploring a knowledge base by using the agent to reason <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## The n8n Agentic RAG Template (Local Version)

The local [[ai_automation_with_n8n | n8n agentic RAG]] template is very similar to its cloud counterpart, but it switches to local AI services like Olama and a self-hosted Superbase (or Postgres) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

What makes this agentic RAG is the agent's ability to explore the knowledge base in different ways using tools that interact with Postgres (or self-hosted Superbase) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For testing, the local LLM used is Quen 2.51 14b, with an 8,000-token context limit <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Examples of Tool Usage:

*   **Basic RAG Lookup**: For simple questions like "Who is the CEO of the company?", the agent performs a straightforward RAG lookup <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Reading Document Contents**: For questions that might confuse naive RAG, like "Who was in the Feb 12th meeting?", the agent uses a tool to list available documents and then reads the full content of relevant documents to answer the question <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Tabular Data Query**: RAG typically struggles with tabular data, especially for analytical tasks like computing averages <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The agentic template allows the agent to treat Excel and CSV files as SQL tables, enabling it to write SQL queries to compute values like the average overall rating from customer feedback <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This is particularly impressive for smaller LLMs like Quen 2.51 14b <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

> "Your results will be inconsistent depending on the local large language model that you use because as you're using these really really tiny ones of course the results are going to be a lot different than if you're using the cloud version of this template we're using all of these super powerful llms like Claude 3.7 Sonet or gbt 40 but it still is so cool the kind of power we can have with local Ai and with this whole setup we are 100% secure and offline that's the advantage of local Ai" <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>

## Setting Up the Workflow

The [[ai_automation_with_n8n | n8n]] workflow is built as part of a local AI package, but setup instructions are provided for both scenarios <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### Database Setup

The database is crucial for storing conversation history and the entire knowledge base <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Postgres Credentials**: Set up credentials for your Postgres instance. If using the local AI package, the host is typically `DB`, and default user/database is `postgres`, port `5432` <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. Otherwise, use your local host address <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Table Creation**:
    *   **`document_metadata`**: Stores high-level information for documents, allowing the LLM to list available documents and know which ones to pull full content from <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. It also includes a `schema` column for table files, informing the LLM about available columns for SQL queries <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
    *   **`document_rows`**: Stores records for all tabular files in a single table using a `row_data` JSONB column, accommodating different table structures <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This allows querying based on this column when the agent creates SQL queries <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   **`documents` (PG Vector)**: This table stores embeddings for RAG <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The Postgres PG Vector store node automatically creates this table <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. Note that the text column is named `text` (different from Superbase's `content` column), requiring recreation if migrating from Superbase <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Postgres is used to avoid limiting users to Superbase and for its lightweight nature <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

### Knowledge Base Setup (RAG Pipeline)

This pipeline adds local files into the knowledge base <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Local File Trigger**: Watches a specified local folder for files that are added or changed <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. The path is typically a shared folder mounted to the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] container in the local AI package <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. Important options like `polling` and `files and folders` must be included <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   **Looping**: The workflow loops to process multiple documents uploaded simultaneously <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **Set Metadata**: Extracts file ID (using path), file type, and title from the file path <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **Clean Slate**: Deletes old document records from `documents_PG` and `document_rows` tables if the file was previously added <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This prevents the LLM from hallucinating with outdated information <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   **Insert Document Metadata**: Adds the initial record (ID, title, created_at) into the `document_metadata` table <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
*   **Read File to Disk**: Brings the file into the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] instance <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Extract Content**: Uses a switch statement to extract text based on file type (e.g., PDF, CSV, text/markdown) <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] supports various file types for extraction <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **PG Vector Store Node (RAG)**: Takes the extracted text, splits it into chunks, and stores it in the `documents_PG` table <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
    *   Uses an Olama embedding model (e.g., `namic-embed-text`) <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
    *   Adds metadata (file ID, file title) to each record, enabling the LLM to cite its source <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
    *   Uses a recursive character text splitter with a chunk size of 400 <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.
*   **CSV/Excel File Handling**:
    *   Extracts data from the files <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
    *   **Insert Table Rows**: Inserts all row data into the `document_rows` table as JSONB, storing column data for each row <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
    *   **Add to RAG Knowledge Base**: Aggregates and summarizes all rows to create a text representation of the entire table, which is then inserted into the RAG knowledge base like other text documents <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.
    *   **Set Schema**: Extracts all columns from the file and updates the `document_metadata` record with this schema <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. This helps the LLM understand how to write SQL queries against the `row_data` <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

Once the RAG pipeline is set up, files dropped into the watched folder will be quickly loaded into the knowledge base, ready for interaction with the agent <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.

### AI Agent Setup

This section covers the core of the AI agent <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
*   **Triggers**:
    *   **Chat Trigger**: Allows interaction directly within the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] UI <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
    *   **Webhook Trigger**: Exposes the agent as an API endpoint <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.
    *   An "Edit Fields" node standardizes input from both triggers <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>.
*   **Tools Agent**:
    *   **System Prompt**: Informs the agent it's a personal assistant with tools for agentic RAG and provides instructions on tool usage <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.
    *   **Chat Memory**: Uses basic Postgres chat memory, which automatically creates an `n8n_chat_histories` table <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
    *   **Chat Model**: The setup uses the OpenAI chat model node, but the base URL is redirected to the local Olama container <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>. This workaround is necessary due to a glitch in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]]'s dedicated Olama chat model node that causes errors when invoking the RAG tool <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>. It can dynamically load models pulled in Olama <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.
*   **Agent Tools**:
    *   **RAG (Postgres PG Vector)**: Provides a basic description for the agent to know when to use it, limits to four results, and includes metadata (title, file ID) so the LLM can cite sources <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. Uses the same Olama embedding model as the RAG pipeline <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>. Credentials reference the Olama service or `Local Host` <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
    *   **List Documents**: Queries the `documents_metadata` table to provide a simple list of available documents <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.
    *   **Get File Contents**: Queries the `documents_PG` table to combine all chunks for a single document, getting its full text content <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>. It's parameterized so the LLM decides the file ID <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
    *   **Query Tabular Data**: Allows the LLM to fully generate SQL queries against the `document_rows` table. The tool's description includes examples to guide the LLM in writing effective queries, especially when referencing JSONB data <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>.

## Addressing the Olama Context Length Headache

By default, Olama models have a context length of 2,000 tokens <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. This is often insufficient for AI agents, as longer prompts (including RAG lookups, system prompts, and tool instructions) can exceed this limit, causing information loss <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.

Since the `Chat Olama Model` node in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] cannot be used with RAG due to a glitch, and the `OpenAI` node (used as a workaround) does not offer a direct context length setting, a solution is to create custom Olama models with extended context lengths <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

**Steps to create a custom Olama model with extended context:**
1.  Ensure your Olama container is running (or Olama is running locally) <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.
2.  Create a "model file" using the `ollama create` command. This file inherits from a base model and changes the context length parameter (e.g., to 8,000) <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.
    ```bash
    # Example command to create a model file (replace "base_model" and "new_model_name")
    ollama create new_model_name -f MyModelFile
    ```
    The `MyModelFile` would contain:
    ```
    FROM base_model
    PARAMETER num_ctx 8000
    ```
3.  Run the `ollama create` command pointing to your model file <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This creates a new version of the model without redownloading the base model <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
4.  Verify the new model using `ollama list` <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

This extended context length prevents the LLM from hallucinating when tool invocations and data from the knowledge base increase prompt length <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.

The local [[ai_automation_with_n8n | n8n agentic RAG]] template provides a powerful way to leverage local AI and no-code tools for specific use cases <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.