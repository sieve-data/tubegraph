---
title: Integrating local AI services with Supabase
videoId: pOsO40HSbOo
---

From: [[colemedin]] <br/> 

[[superbase_integration_for_ai_projects | Supabase]] is a popular open-source platform, widely used as a database for [[using_supabase_for_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Underneath, it utilizes PostgreSQL <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Why Supabase for AI Agents?

[[using_supabase_for_ai_agents | Supabase]] offers several advantages for AI agent development:
*   **Conversation History & State Management**: It can manage conversation history and state for AI agents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Vector Database**: With the PG Vector extension, [[using_supabase_as_a_vector_database_for_ai_agents | Supabase can be used as a vector database for RAG (Retrieval Augmented Generation)]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Additional Features**: It includes out-of-the-box features like authentication and object storage <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Dual Functionality**: It functions both as a SQL database and a vector store for RAG <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The platform is considered valuable and powerful, making it a fitting choice for various AI projects <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Its open-source nature and Docker-based self-hosting instructions simplify its integration into local AI services <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Local AI Package Revamp

The local AI package has been revamped to include [[superbase_integration_for_ai_projects | Supabase]] and now resides in its own dedicated GitHub repository <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
This package was initially created by the n8n team <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> and previously included n8n, Olama, Qdrant, and PostgreSQL <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Subsequent additions included Flowise (a low-code AI agent builder) and Open Web UI (a ChatGPT-like interface) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

[[superbase_integration_for_ai_projects | Supabase]] now replaces PostgreSQL entirely within the package, given that [[superbase_integration_for_ai_projects | Supabase]] is built on PostgreSQL <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Qdrant, another vector store, remains in the package because it offers faster performance for certain use cases compared to [[superbase_integration_for_ai_projects | Supabase]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Setting Up the Local AI Package

### Prerequisites
Before installation, ensure the following are installed <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>:
*   **Python**: Required to run a script for [[superbase_integration_for_ai_projects | Supabase]] setup <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Git or GitHub Desktop**: For cloning the repository <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. GitHub Desktop is recommended for personal machines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Docker or Docker Desktop**: All local AI services run as Docker containers <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Docker Desktop is recommended for personal computers <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    *   **Docker Desktop Settings for Windows**: Enable "Expose daemon on tcp://localhost:2375 without TLS" <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

### Installation Steps
1.  **Clone the Repository**: Clone the dedicated GitHub repository for the local AI package <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   `git clone https://github.com/dmaynard-ai/local-ai-package.git` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
    *   Change directory into `local-ai-package` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  **Configure `.env` File**:
    *   Copy contents from `env.example` into a new `.env` file <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   **n8n Credentials**: Set `N8N_JWT_SECRET` and `N8N_ENCRYPTION_KEY` to any random alphanumeric string <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   **Supabase Credentials**:
        *   `POSTGRES_PASSWORD`: Set a password for the PostgreSQL database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
        *   `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD`: Set login credentials for the local [[superbase_integration_for_ai_projects | Supabase]] dashboard <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
        *   `POOLER_TENANT_ID`: Set to any number for transaction Pooler connections <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
        *   **JWT Secret and Keys**: These can be generated using the [[superbase_integration_for_ai_projects | Supabase]] self-hosting guide <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
            *   `JWT_SECRET`: Copy from the guide's JWT secret generator <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
            *   `ANON_KEY`: Generate an Anonymous key from the guide <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
            *   `SERVICE_ROLE_KEY`: Generate a Service Role key from the guide <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Starting the Docker Compose Stack
The local AI package uses a `docker-compose.yaml` file to define various Docker containers like n8n, Olama, Flowise, and Open Web UI <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. [[superbase_integration_for_ai_projects | Supabase]] is handled separately because it consists of many containers (e.g., Studio, Kong, Auth, Realtime) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

A Python script, `start_services.py`, simplifies the setup <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>:
*   It clones or updates the [[superbase_integration_for_ai_projects | Supabase]] repository <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   It combines the [[superbase_integration_for_ai_projects | Supabase]] Docker Compose file with the local AI package's Docker Compose file <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   Ensures all containers run on the same Docker Network for easy communication <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

Run the appropriate command based on your system architecture <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>:
*   **Nvidia GPU**: `python start_services.py --profile nvidia` <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>
*   **AMD GPU (Linux)**: `python start_services.py --profile amd` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
*   **Mac/CPU only**: `python start_services.py --profile cpu` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a> (or `--profile none` to exclude Olama if already running natively) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

The script restarts existing containers and reboots them, preserving data in workflows and [[superbase_integration_for_ai_projects | Supabase]] tables <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Updating and Restarting the Stack
To update or restart services, especially after environment variable changes <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>:
1.  Spin down everything: `docker compose down` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
2.  Pull latest updates: `docker compose pull` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
3.  Run `start_services.py` with your profile <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Accessing Local Services
Once running, you can access the various services:
*   **Qdrant**: `localhost:6333/dashboard` <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>
*   **Flowise**: `localhost:3000/api/v1/flow-wise` <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>
*   **Supabase Dashboard**: `localhost:8000` (requires dashboard username/password from `.env`) <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>
*   **n8n**: `localhost:5678` (first-time setup requires local account creation) <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>

## Building a RAG AI Agent with Local Supabase in n8n

An example RAG AI agent workflow is automatically imported into your n8n instance <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>.
This agent uses:
*   Olama chat model <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   [[superbase_integration_for_ai_projects | Supabase]] for chat memory via the PostgreSQL node <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
*   [[superbase_integration_for_ai_projects | Supabase]] for vector retrieval <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

### Setting Up Credentials in n8n
*   **Olama Credentials**:
    *   **Base URL**: `http://olama:11434` <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. This connects to the Olama Docker container within the same network <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **Supabase (PostgreSQL Node) Credentials**:
    *   **Host**: `db` <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. This refers to the primary [[superbase_integration_for_ai_projects | Supabase]] database container name in its Docker Compose stack <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
    *   **Database**: `postgres` <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   **Username and Password**: Use values set in your `.env` file <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
*   **Supabase (Vector Store Node) Credentials**:
    *   **Host**: `host.docker.internal:8000` <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. Unlike the PostgreSQL node, using `db` for the host does not work here. This host directs n8n to connect back to the local machine's mapped port for [[superbase_integration_for_ai_projects | Supabase]] <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.
    *   **Service Roll Secret**: Use the `SERVICE_ROLE_KEY` from your `.env` file <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.

### Local RAG Pipeline Workflow
This workflow automatically imports files from a local folder into your local [[superbase_integration_for_ai_projects | Supabase]] vector store <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
1.  **Local File Trigger**: Monitors a specific local folder (`/data/shared`) for added or changed files <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This folder is mapped to `/data/shared` in the n8n container via Docker Compose <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
2.  **Determine Event Type**: Checks if the event is an 'add' or 'change'. For 'change' events, it cleans existing vectors for that file from the database <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>.
3.  **Pull File Content**: The workflow pulls the content of the triggered file <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.
4.  **Extract Text**: Extracts the text from the file <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
5.  **Set Up Supabase Vector Store**:
    *   In the [[superbase_integration_for_ai_projects | Supabase]] dashboard SQL editor, copy and run the SQL from the [[superbase_integration_for_ai_projects | Supabase]] documentation's "Quick Start for setting up your Vector Store" to create the necessary tables and extensions (e.g., `pg_vector`) <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.
    *   Adjust the vector size to `768` for the Nomic Embed text model from Olama <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
6.  **Insert Vectors**: Run the workflow in n8n to insert the processed text as vectors into the [[superbase_integration_for_ai_projects | Supabase]] `documents` table <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Testing the RAG Agent
Once the vectors are in [[superbase_integration_for_ai_projects | Supabase]], you can interact with your local AI agent. For instance, you can chat with the Olama model (e.g., Qwen 2.5) running locally on your GPU, asking questions that require retrieval from your vectorized documents <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>. The agent will invoke the [[superbase_integration_for_ai_projects | Supabase]] vector store tool to retrieve relevant information and answer your query based on the content <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

## Future Plans
This local AI package is envisioned as the "golden standard for local AI" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Future plans include expanding the package with more tools, services, and frameworks, and integrating it into other projects <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Community feedback is encouraged for its continued development <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.