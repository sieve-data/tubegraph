---
title: RAG AI agent development
videoId: V_0dNE-H2gw
---

From: [[colemedin]] <br/> 

Developing powerful AI agents that leverage local infrastructure is becoming increasingly accessible due to the advancements in open-source models like Llama, which can now compete with proprietary models such as GPT and Claude <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Self-Hosted AI Starter Kit

A single package, developed by the n8n team, provides a complete environment for local AI <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This starter kit includes:
*   **Ollama**: For large language models (LLMs) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Qdrant**: For the vector database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Postgres**: For the SQL database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **n8n**: For workflow automations, tying everything together <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

The kit is available as a GitHub repository, primarily consisting of two files: `.env` for environment variables (e.g., Postgres credentials) and `docker-compose.yaml` for orchestrating the services <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Dependencies and Setup
Before setting up the kit, ensure you have Git and Docker (which includes Docker Compose) installed <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

To get started:
1.  Clone the repository using `git clone` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  Navigate into the new repository directory <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  Open the files in a code editor (e.g., VS Code with `code .`) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Customizing the Setup
The default setup requires a few modifications for full functionality, particularly for [[enhancing_ai_agents_with_rag_technology | enhancing AI agents with RAG technology]]:
*   **`.env` file**: Configure Postgres username, password, database name, and n8n secrets <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **`docker-compose.yaml`**:
    *   **Expose Postgres Port**: Add `ports: - "5432:5432"` to the Postgres service to allow n8n workflows to access it for chat memory <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   **Pull Ollama Embedding Model**: Include a line to pull an Ollama embedding model within the Ollama service initialization, as it's necessary for RAG <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. By default, it only pulls `llama3.1` <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

After making these changes, start the services using `docker compose up` with the appropriate profile (`--profile gpu` for Nvidia, `--profile mac` for Mac, or `--profile cpu` for general CPU usage) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

You can monitor the running containers in Docker Desktop, where you'll see four services: Ollama, Postgres, n8n, and Qdrant <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. It's also possible to execute commands within these containers, such as pulling new Ollama models in real-time <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Building a RAG AI Agent in n8n

The self-hosted n8n instance can be accessed at `localhost:5678` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This platform enables the creation of a fully local [[creating_rag_ai_agents_using_n8n | RAG AI agent]] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

The [[n8n_rag_ai_agent | n8n RAG AI Agent]] workflow consists of two main parts: the agent itself and a pipeline for ingesting files into the knowledge base <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Agent Configuration
The AI agent in [[n8n_rag_ai_agent | n8n]] integrates the locally hosted services:
*   **LLM**: The Ollama chat model is configured by referencing the model (e.g., `llama3.1:latest`) and setting the base URL to `http://host.docker.internal:11434` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Memory**: Postgres is used for chat memory. n8n automatically creates the necessary table, and credentials are based on the `.env` file, with the host `host.docker.internal` and port `5432` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **RAG Tool**: A vector store tool is attached to the agent, utilizing Qdrant for document retrieval <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Qdrant's URL is `http://host.docker.internal:6333` <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
    *   Qdrant also offers a self-hosted dashboard at `localhost:6333/dashboard` to visualize collections and vectors <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Embeddings**: Ollama is used for generating embeddings, leveraging the embedding model pulled during setup <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. Llama 3.1 is then used to parse the responses from RAG lookups <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Ingesting Files into the Knowledge Base
The ingestion workflow in n8n automates adding documents to the Qdrant vector database:
1.  **Triggers**: The workflow is triggered when a file is created or updated in a specified Google Drive folder <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
2.  **File ID Extraction**: Key information, including the file ID and folder ID, is extracted from the triggered event <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
3.  **Preventing Duplicates**: A crucial step involves custom code (using LangChain) to connect to Qdrant, retrieve all vector IDs associated with the current file ID, and delete them before re-insertion <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. This prevents duplicate vectors when a document is updated, which would otherwise confuse the LLM <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
4.  **Download and Extract Text**: The Google Drive file is downloaded, and its raw text is extracted (supporting PDFs, CSVs, Google Docs, etc.) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
5.  **Chunking**: The extracted text is split into smaller chunks (e.g., 100-character chunks using a recursive character text splitter) <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. Smaller chunks reduce context and manage local LLM processing efficiently <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
6.  **Insert into Qdrant**: The chunked text is then inserted into the Qdrant vector store <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. Metadata like the file ID is added during this process to link vectors to specific documents <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Testing the Agent
After the document is ingested, the [[n8n_rag_ai_agent | n8n RAG AI Agent]] can be tested via the chat widget. Asking questions that require information from the ingested document (e.g., "what is the ad campaign focusing on?") will prompt the agent to perform RAG lookups <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. Although local LLMs might take time to respond, the agent successfully retrieves and processes information from its knowledge base <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Response formatting can be improved by refining the system prompt <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.

## Future Enhancements
Future plans for this local AI stack include:
*   Adding Redis for caching <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   Integrating a self-hosted Superbase for authentication and other functionalities, replacing vanilla Postgres <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   Expanding into a full local AI tech stack, potentially including front-end components <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   Baking in best practices for RAG, LLMs, and [[n8n_rag_ai_agent | n8n]] workflows to create a comprehensive template for [[building_a_nocode_rag_ai_agent | building a nocode RAG AI agent]] <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
