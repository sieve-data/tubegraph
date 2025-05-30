---
title: Incorporating AI models and databases in a local setup
videoId: pOsO40HSbOo
---

From: [[colemedin]] <br/> 

Developing AI applications locally offers significant advantages, and an effective [[tech_stack_for_local_ai_applications | tech stack]] is crucial for this. This article details how to integrate AI models and databases into a local development environment, focusing on the powerful combination of Supabase and other open-source tools.

## Supabase: The Ideal Platform for Local AI Agents

Supabase is an open-source platform recognized as a popular database for [[running_ai_agents_on_local_machines | AI agents]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Underneath, it uses PostgreSQL, allowing it to manage conversation history and state for agents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Its PG Vector extension can turn it into a vector database for Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Beyond databases, Supabase also offers features like authentication and object storage out of the box <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

The open-source nature of Supabase and its Docker self-hosting instructions make it relatively easy to [[integrating_local_ai_services_with_supabase | integrate into a local AI services]] environment <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## The Local AI Package: A Revamped Stack

A comprehensive [[building_a_local_ai_package_with_supabase | local AI package]] has been developed and revamped to include Supabase, now residing in its own dedicated GitHub repository <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The initial [[tech_stack_for_local_ai_applications | local AI package]] began with four services:
*   n8n <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   Ollama <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   Qdrant <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   PostgreSQL <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>

Subsequent additions to the package included:
*   Flowise for another low-code AI agent builder <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>
*   Open Web UI for a ChatGPT-like interface <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>

In the latest revamp, Supabase replaces PostgreSQL entirely due to its underlying PostgreSQL database <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Qdrant is retained because it can function as a vector store, similar to Supabase, but it is faster for certain use cases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Setting Up the Local AI Package

To get the revamped [[setting_up_a_local_ai_cloud_stack | local AI stack]] up and running, follow these steps:

### Prerequisites
Ensure the following tools are installed on your machine:
*   **Python**: Necessary to run a script for Supabase setup <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Git or GitHub Desktop**: For cloning the repository <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. GitHub Desktop is recommended for personal machines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Docker or Docker Desktop**: All local AI services run as Docker containers <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Docker Desktop is recommended for personal computers <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Cloning the Repository
1.  Clone the GitHub repository for the local AI package <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
2.  Change your directory into `local-ai-package` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The repository primarily uses a `docker-compose.yaml` file to define all the Docker containers for the local AI package <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, including n8n, Ollama, Flowise, and Open Web UI <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Supabase, however, is not directly included in this file because it runs many different containers and requires a separate Docker Compose file <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Setting Environment Variables
Create an `.env` file from the `env.example` file in your IDE <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. While `env.example` contains many variables due to Supabase's configurability, only a few are critical for basic setup <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The essential variables to set are:
*   **n8n Credentials**: `N8N_JWT_SECRET` and `N8N_ENCRYPTION_KEY`. These can be set to any random alphanumeric string <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **PostgreSQL Password**: `POSTGRES_PASSWORD`. This defines the password for your Supabase database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Dashboard Login**: `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD`. These are for accessing your local Supabase dashboard <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Pooler Tenant ID**: `POOLER_TENANT_ID`. Set this to any number for transaction Pooler connections <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **JWT Secret**: This is generated from the Supabase self-hosting documentation <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Anonymous Key**: Also generated from the Supabase documentation, under "Anonymous key" then "generate JWT" <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Service Role Key**: Similarly, generated from the Supabase documentation, under "service key" then "generate JWT" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Starting the Local AI Stack
The `start_services.py` Python script is used to spin up the local AI stack <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This script handles:
*   Cloning the Supabase repository or pulling updates <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   Combining the Supabase Docker Compose file with the local AI package's Docker Compose file <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   Ensuring all containers run on the same Docker Network for easy inter-service communication <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   Restarting and updating services effortlessly <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. To update, spin down services (`docker compose down`), pull latest images (`docker compose pull`), then run `start_services.py` again <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. Data and workflows persist across restarts <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

Commands to run the script depend on your system's architecture:
*   **Nvidia GPU**: `python start_services.py --profile gpu-nvidia` <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>
*   **AMD GPU (Linux)**: `python start_services.py --profile gpu-amd` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
*   **Mac (CPU only)**: `python start_services.py --profile none` (This excludes the Ollama container) <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>
*   **No GPU**: `python start_services.py --profile cpu`

<p class="yt-timestamp" data-t="00:18:35">[00:18:35]</p>
> [!NOTE] Troubleshooting
> A troubleshooting section is available in the readme of the GitHub repository to address common issues with running Supabase locally <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

After successful setup, various services become accessible:
*   **Qdrant**: `localhost:6333/dashboard` <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>
*   **Flowise**: `localhost:3000` <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>
*   **Supabase Dashboard**: `localhost:8000` (requires dashboard username and password set in the .env file) <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>
*   **n8n**: `localhost:5678` (requires creating a local account) <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>

## Configuring Services for Local AI

Once the stack is running, you can configure the connections within n8n. An example workflow for a local RAG AI agent is automatically imported <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

### Ollama Credentials
In n8n, create a new credential for Ollama:
*   **Base URL**: `http://ollama:11434` <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. The name `ollama` is used because containers on the same Docker network can reference each other by their container names <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
*   Upon saving, the connection will be tested, and available Ollama models (defined in `docker-compose.yaml`) will load <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

### Supabase (PostgreSQL) Credentials
For the PostgreSQL node connection in n8n:
*   **Host**: `db` <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. Similar to Ollama, `db` is the name of the primary database container within the Supabase Docker stack <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
*   **Database**: `postgres` <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Username and Password**: Use the values set in your `.env` file <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

### Supabase Vector Store Connection
For the Supabase Vector Store node in n8n:
*   **Host**: `host.docker.internal` <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This tells n8n to connect to the host machine and then route to the mapped port for the Supabase container.
*   **Service Role Secret**: Use the `SERVICE_ROLE_KEY` defined in your `.env` file <a class="yt-timestamp" data-t="00:23:07">[0:23:07]</a>.

### Setting Up the Vector Store in Supabase
Before inserting vectors, you need to set up the vector store schema in your local Supabase instance:
1.  Go to the Supabase dashboard (`localhost:8000`).
2.  Navigate to the **SQL Editor** <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
3.  Copy the SQL script for setting up the vector store from the Supabase documentation (found under "Quick Start for setting up your vector store") <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
4.  Paste the SQL into a new snippet and **change the vector size to `768`** (for the Nomic Embed text model from Ollama) <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
5.  Run the SQL script to create the `documents` table <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

## Building a Local RAG AI Agent

A sample `Superbase RAG AI Agent` workflow is automatically imported into n8n <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. This agent utilizes:
*   An agent node in n8n <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.
*   Ollama chat model <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   Supabase (via PostgreSQL node) for chat memory <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   Supabase for vector retrieval (RAG) <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

The workflow to bring local files into the local Supabase vector store operates as follows:
1.  **Local File Trigger**: Watches for files added or changed in a specific shared folder (`/data/shared`) that is mapped from your personal computer to the n8n container <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.
2.  **Determine Event Type**: Checks if the event is an "add" or "change". For "change" events, it cleans the vector database of any existing vectors for that specific file (using its path as a file ID) <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>.
3.  **Pull File and Extract Text**: The workflow pulls the file's contents and extracts the text <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.
4.  **Insert Vectors into Supabase**: The extracted text is then inserted as vectors into the `documents` table in Supabase <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

Once vectors are in Supabase, you can interact with the RAG agent, for example, by asking questions related to the content of your local files <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>. The agent will use the Supabase vector store tool to retrieve relevant information and respond based on the retrieved context and the locally running LLM <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. This demonstrates a fully local RAG setup <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.

## Future Vision and [[extending_local_ai_infrastructure | Extending Local AI Infrastructure]]

This revamped [[building_a_local_ai_package_with_supabase | local AI package]] is designed to be a "golden standard" for [[comparison_of_local_and_cloudbased_ai_models | local AI]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It's intended to be expanded with more services and integrated into other projects <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Future plans include incorporating additional tools, services, or frameworks based on community feedback <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. This local AI package serves as a robust foundation for building and running any [[comparison_between_local_and_large_ai_models | AI agent]] locally <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>, with the potential to [[deploying_local_ai_package_to_cloud_instances | deploy to cloud instances]] or remain entirely on a local machine <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.