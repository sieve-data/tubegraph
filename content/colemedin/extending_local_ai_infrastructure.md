---
title: Extending local AI infrastructure
videoId: V_0dNE-H2gw
---

From: [[colemedin]] <br/> 

The concept of running AI infrastructure locally is becoming increasingly accessible, with open-source models reaching a level of power comparable to closed-source alternatives like GPT and Claude <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. A key development in this area is a self-hosted AI starter kit developed by the n8n team, designed to provide a comprehensive [[setting_up_a_local_ai_cloud_stack | single package for local AI]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Components of the Local AI Stack

The n8n self-hosted AI starter kit bundles several powerful tools to create a robust local AI environment <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:

*   **Ollama**: For [[running_ai_agents_on_local_machines | large language models (LLMs)]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Qdrant**: A vector database for semantic search and retrieval-augmented generation (RAG) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **PostgreSQL**: A SQL database for structured data storage <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **n8n**: A workflow automation tool that ties all these components together <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Initial Setup and Core Extensions

To set up this local AI infrastructure, users need Git and Docker (including Docker Compose) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The core of the setup revolves around two main files in the GitHub repository: the `.env` file for credentials and the `docker-compose.yaml` file for orchestrating the services <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

While the starter kit provides a foundation, certain extensions to the `docker-compose.yaml` file are crucial for full functionality and flexibility <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>:

*   **Exposing PostgreSQL Port**: By default, the PostgreSQL container's port is not exposed, preventing external use of PostgreSQL as a database in n8n workflows (e.g., for chat memory) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Adding `ports: - "5432:5432"` maps the internal port to `localhost:5432`, making it accessible <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Pulling Ollama Embedding Models**: To utilize Ollama for embeddings in a vector database for RAG, an additional line in the `docker-compose.yaml` is needed to pull a specific Ollama embedding model <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This ensures the necessary model is available for vector generation.

Once configured, the stack can be started using a Docker Compose command tailored to the user's architecture, such as `docker compose --profile CPU up` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Building a Local RAG AI Agent with n8n

With the local AI infrastructure running, n8n can be accessed at `localhost:5678` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This environment enables the creation of a fully local RAG AI agent <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Agent Configuration

The RAG AI agent integrates the local services:

*   **LLM (Ollama)**: The Ollama chat model (e.g., Llama 3.1) is referenced by its name <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The base URL for Ollama should be `http://host.docker.internal:11434`, using `host.docker.internal` for inter-container communication <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Chat Memory (PostgreSQL)**: PostgreSQL is used for chat memory. The n8n instance automatically creates a table, referencing credentials set in the `.env` file (database name, user, password) and connecting via `host.docker.internal:5432` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Vector Store (Qdrant)**: Qdrant serves as the vector store for RAG. The Qdrant URL is `http://host.docker.internal:6333` <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. A notable extension is the ability to access the self-hosted Qdrant dashboard at `localhost:6333/dashboard`, providing visibility into collections and vectors <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Embeddings (Ollama)**: Ollama is also used for generating embeddings, utilizing the specific embedding model pulled during the Docker Compose setup <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Ingesting Files into the Knowledge Base

A crucial part of the RAG agent is the workflow for ingesting documents into the Qdrant knowledge base. This process can be triggered by file creation or updates in a service like Google Drive <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

#### Custom Code for Upsert Functionality

A significant extension to this workflow involves custom code to prevent duplicate vectors when a document is updated <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Unlike simple inserts, standard n8n nodes for vector stores (e.g., for Supabase, Qdrant, Pinecone) often only perform inserts, not upserts. This means re-ingesting an updated document would result in old and new vectors for the same document coexisting, confusing the LLM <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

To address this, a custom code node (using LangChain) connects to Qdrant, identifies all vectors associated with a specific file ID (stored as metadata), and deletes them before the updated document's new vectors are inserted <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. This ensures that the knowledge base remains clean and efficient <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

After ingesting, documents are chunked (e.g., into 100-character chunks) and inserted into the Qdrant vector store <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

## Future Extensions

While this stack provides an excellent starting point, further extensions are planned to enhance its robustness and functionality <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>:

*   **Redis**: For caching mechanisms <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   **Self-hosted Supabase**: As an alternative to vanilla PostgreSQL, offering additional features like authentication <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   **Complete Local AI Tech Stack**: Potentially [[building_and_deploying_custom_ai_front_ends | including a front-end]] component <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Best Practices Templates**: Incorporating best practices for RAG, LLMs, and n8n workflows to create easy-to-use templates <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.