---
title: Local AI package setup
videoId: V_0dNE-H2gw
---

From: [[colemedin]] <br/> 

This article outlines the setup and use of a powerful local AI package, providing a comprehensive solution for running AI infrastructure on your machine. This package integrates several key open-source technologies to create a robust environment for developing AI agents, particularly those leveraging Retrieval Augmented Generation (RAG).

## Package Components

The self-hosted AI starter kit, developed by the n8n team, includes:
*   **Ollama**: For running Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Qdrant**: Serving as the vector database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Postgres**: Functioning as the SQL database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **n8n**: To connect everything with workflow automations <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

This package makes running your own AI infrastructure accessible, especially as open-source models like Llama become powerful enough to compete with closed-source alternatives like GPT and Claude <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Setting up a Local AI Cloud Stack

The foundation of this setup is a GitHub repository for the n8n self-hosted AI starter kit <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Prerequisites
Before starting, ensure you have Git and Docker installed <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Docker Desktop is recommended as it includes Docker Compose, which is necessary for orchestrating the services <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Installation Steps

1.  **Clone the Repository**:
    Copy the `git clone` command from the GitHub repository <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Open your terminal, paste the command, and execute it to download the code to your computer <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Then, change your directory into the newly cloned repository <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

2.  **Edit Environment Variables (`.env` file)**:
    Open the `.env` file (or rename `env.example` to `.env`) in your preferred code editor <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Set your PostgreSQL username, password, and database name <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Configure n8n secrets; these should be long, alphanumeric strings <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

3.  **Extend Docker Compose (`docker-compose.yaml` file)**:
    This file orchestrates the different services.
    *   **Expose PostgreSQL Port**: By default, the PostgreSQL container's port (5432) is not exposed, preventing external access (e.g., from n8n workflows) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Add the following lines under the `postgres` service to expose port 5432:
        ```yaml
        ports:
          - "5432:5432"
        ```
        This allows you to access PostgreSQL via `localhost:5432` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   **Pull Ollama Embedding Model**: To use Ollama for embeddings in your vector database, add a command to pull an embedding model (e.g., `nomic-embed-text`) during initialization of the Ollama service <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The base command pulls `llama3.1` <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

4.  **Run Docker Compose**:
    Execute the appropriate Docker Compose command based on your architecture <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>:
    *   **For CPU-only (recommended for simplicity)**:
        ```bash
        docker compose --profile CPU up
        ```
    *   **For Nvidia GPU users**:
        ```bash
        docker compose --profile GPU up
        ```
    This command will pull the necessary Docker images for Ollama, Postgres, n8n, and Qdrant, and then start all services <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Verifying the Setup

Open Docker Desktop to confirm that four containers are running: n8n, Ollama, Qdrant, and Postgres <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. You can inspect logs and even run Linux commands within each container via the `exec` tab <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. For example, you can pull additional Ollama models in real-time from within the Ollama container without restarting it <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

*   **Access n8n**: Navigate to `localhost:5678` in your web browser <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Access Qdrant Dashboard**: Visit `localhost:6333/dashboard` to view your Qdrant collections and vectors <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This dashboard provides visibility into your knowledge base, including metadata and chunk contents <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Incorporating AI Models and Databases in a Local Setup

With the local infrastructure established, you can now [[building_a_local_ai_package_with_supabase | build a local AI package with Supabase]] and a fully local RAG AI agent within n8n.

### Configuring AI Agents for Cloud Deployment

This section describes how to configure the RAG agent in n8n to use the locally hosted services.

#### AI Agent Configuration

1.  **Ollama Chat Model**:
    *   **Model**: Reference `llama3.1:latest` (or any other Ollama LLM you have pulled) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
    *   **Credentials**: The base URL for Ollama is `http://host.docker.internal:11434`. It's crucial to use `host.docker.internal` instead of `localhost` for inter-container communication <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

2.  **PostgreSQL for Chat Memory**:
    *   **Table Name**: n8n will automatically create a table in your PostgreSQL database <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
    *   **Credentials**: The host is `host.docker.internal`, and the port is `5432` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. The database name, user, and password should match what you set in your `.env` file <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. This enables [[database_setup_and_management_for_ai_agents | database setup and management for AI agents]] for chat memory.

3.  **Qdrant Vector Store for RAG**:
    *   **Retrieval**: Configure to retrieve documents based on the agent's query <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   **Credentials**: The Qdrant URL is `http://host.docker.internal:6333` <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. An API key is typically filled in by default <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
    *   **Embeddings**: Use the Ollama embedding model that was pulled during setup <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

#### Ingesting Files into the Knowledge Base

A workflow in n8n can be set up to ingest files into your Qdrant knowledge base, enabling RAG functionalities.

1.  **Triggers**: The workflow can be triggered when a file is created or updated in a specific Google Drive folder <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
2.  **Data Extraction**: Extract the file ID and folder ID from the Google Drive event <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
3.  **Preventing Duplicate Vectors (Crucial Step)**:
    When updating a document, merely inserting new vectors will lead to duplicates of older versions of the file in your vector database <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. Implement a custom code node (using Langchain) to:
    *   Connect to your Qdrant vector store <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
    *   Get all vector IDs where the `file ID` metadata matches the ID of the file being ingested <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   Delete those vectors to ensure zero duplicates before re-inserting <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This ensures your LLM is not confused by different versions of the same file <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
4.  **Download and Extract Text**: Download the file from Google Drive and extract its raw text, regardless of format (PDF, CSV, Google Doc) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
5.  **Insert into Qdrant**: Insert the extracted text into the Qdrant vector store <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
    *   **Chunking**: Documents are split into smaller chunks (e.g., 100 characters) using a recursive character text splitter. This helps keep context lower for local LLMs, especially on less powerful computers <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
    *   **Metadata**: Add `file ID` and `folder ID` as metadata to each vector chunk. The `file ID` is particularly important for managing documents and preventing duplicates <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

#### Testing the RAG AI Agent

After setting up the agent and ingesting documents, you can test its RAG capabilities through the n8n chat widget <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. Ask a question that requires information from the ingested document. While [[local_ai_agents_with_olama | local AI agents with Olama]] models like Llama 3.1 may take some time to respond due to local processing, the response should demonstrate that it successfully retrieved information from your knowledge base <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Initial responses might be awkward without specific formatting instructions, but this can be improved by adding system prompts to the LLM <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Extending Local AI Infrastructure

The described stack is an excellent starting point, and there are many ways to [[extending_local_ai_infrastructure | extend local AI infrastructure]] and enhance its robustness in the future:
*   **Caching**: Integrate Redis for caching <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   **Authentication**: Implement a self-hosted Supabase for authentication capabilities <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   **Full Tech Stack**: Expand to include a front-end for a complete local AI tech stack <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Templates**: Bake in best practices for RAG, LLMs, and n8n workflows to create easy-to-use templates for [[local_vs_managed_ai_solutions | local vs Managed AI Solutions]] setups <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.