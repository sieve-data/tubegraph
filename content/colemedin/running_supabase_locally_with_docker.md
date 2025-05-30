---
title: Running Supabase locally with Docker
videoId: pOsO40HSbOo
---

From: [[colemedin]] <br/> 

Supabase is an [[supabase_as_an_opensource_platform | open-source platform]] that serves as a popular database for [[using_supabase_for_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It uses PostgreSQL under the hood <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, allowing it to manage conversation history and state for agents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. With the PG Vector extension, Supabase can be transformed into a [[using_supabase_as_a_vector_database | vector database]] for RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Beyond database functionalities, it offers features like authentication and object storage out-of-the-box <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

Due to its utility, Supabase has been integrated into a local AI package <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Since [[supabase_as_an_opensource_platform | Supabase is open-source]] and provides instructions for [[selfhosting_supabase_with_docker | self-hosting with Docker]], it can be easily incorporated into local AI services <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This article outlines the steps to get [[selfhosting_supabase_with_docker | Supabase running locally with Docker]] as part of a revamped local AI package <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Supabase in the Local AI Package

The local AI package now has a dedicated GitHub repository <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Initially, the package included n8n, Ollama, Quadrant, and PostgreSQL <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Flowise (for low-code AI agent building) and Open Web UI (for a ChatGPT-like interface) were later added <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Supabase now replaces PostgreSQL entirely, as it is also based on PostgreSQL <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Quadrant remains in the package because it offers faster vector storage for certain use cases, though Supabase can also be used as a vector store <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Prerequisites

Before installation, ensure the following are installed <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>:
*   **Python**: Required to run a script for [[postgresql_and_docker_configuration | Supabase setup]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Git or GitHub Desktop**: For cloning the repository <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. GitHub Desktop is recommended for personal machines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Docker or Docker Desktop**: All local AI services run as Docker containers <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Docker Desktop is recommended for personal computers <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Installation Steps

### 1. Clone the GitHub Repository
Clone the `local-ai-package` GitHub repository <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a> and change your directory into `local-AI-package` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The `docker-compose.yaml` file within this repository defines the Docker containers for n8n, Ollama, Flowise, and Open Web UI <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Supabase is not directly included in this `docker-compose.yaml` because it consists of multiple containers and uses its own Docker Compose file <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### 2. Set Environment Variables
Create a `.env` file in your IDE <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> by copying the contents from `env.example` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. While the example file contains many variables, only a few are crucial for basic Supabase setup <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The following variables need to be set <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:
*   **n8n credentials**: Define `N8N_JWT_SECRET` and `N8N_ENCRYPTION_KEY` with random alphanumeric strings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **PostgreSQL password**: Set `POSTGRES_PASSWORD` for your database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Supabase Dashboard Login**: Set `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` for accessing the local Supabase dashboard <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Pooler Tenant ID**: Set `POOLER_TENANT_ID` to an arbitrary number <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **JWT Secret, Anonymous Key, Service Role Key**: These can be generated directly from the [[selfhosting_supabase_with_docker | Supabase self-hosting documentation]] <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    *   The JWT secret is generated by refreshing the page <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   The anonymous key and service role key can be generated by clicking on the respective options and then "generate JWT" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Copy these generated values into your `.env` file <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

> [!info] For more advanced Supabase configurations, such as email authentication, refer to the official Supabase self-hosting guide <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### 3. Run the Services
Use the `start_services.py` script to spin up the local AI stack <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   **For Nvidia GPU users**: `python start_services.py --profile gpu-nvidia` <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **For AMD GPU (Linux) users**: `python start_services.py --profile gpu-amd` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **For Mac users (CPU only)**: `python start_services.py` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **To exclude Ollama (e.g., if already running outside Docker)**: `python start_services.py --profile none` <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

This Python script performs several key functions <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>:
1.  **Clones/Updates Supabase Repository**: It clones the Supabase repository or pulls the latest changes if it already exists <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
2.  **Combines Docker Compose Files**: It merges the Supabase Docker Compose file (which runs many different Supabase containers like Studio, Kong, Auth, Realtime, etc.) with the local AI package's `docker-compose.yaml` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
3.  **Ensures Shared Docker Network**: It ensures all services run on the same Docker network, allowing containers like n8n to easily connect to Supabase <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Managing the Stack

*   **Restarting/Updating**: To restart the stack or apply changes to environment variables, simply run the `start_services.py` script again <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. Data in workflows (n8n, Flowise) or Supabase tables will persist <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Upgrading Containers**: To upgrade containers (e.g., n8n, Supabase), follow these steps <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>:
    1.  Spin down everything: `docker-compose down` (specific command not shown, but implied by context of "spin down everything with this First Command" and later `docker-compose down`).
    2.  Pull latest updates: `docker-compose pull` (specific command not shown, but implied by context of "pull the latest updates").
    3.  Rerun `start_services.py` with your desired profile <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   **Docker Desktop**: You can monitor and interact with the running containers in Docker Desktop <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. For Windows users, ensure "Expose daemon on tcp://localhost:2375 without TLS" is checked in Docker Desktop settings for troubleshooting <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

## Accessing Local Services

Once the stack is running, you can access various services locally:
*   **Quadrant**: `http://localhost:6333/dashboard` <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>
*   **Flowise**: `http://localhost:3000` <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>
*   **Supabase Dashboard**: `http://localhost:8000` <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. Log in using the dashboard username and password configured in the `.env` file <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. The local dashboard is familiar to the remote Supabase instance <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **n8n**: `http://localhost:5678` <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. You will create a local n8n account upon first access <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. A "Local RAG AI Agent" workflow is automatically imported <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

## Setting Up a RAG AI Agent with n8n and Local Supabase

This section demonstrates [[using_supabase_for_ai_agents | building a RAG AI agent]] in n8n, using [[integrating_local_ai_services_with_supabase | local Supabase as a vector store]] and chat memory <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

### 1. Configure n8n Credentials
*   **Ollama**: Create a new credential <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
    *   Base URL: `http://ollama:11434` <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
    *   If containers are running correctly, the connection test should succeed <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
*   **Supabase (Postgres Node)**: Create new credentials <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
    *   Host: `db` <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a> (This refers to the primary database container name in the Supabase Docker Compose file <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. Since n8n and Supabase are on the same Docker network, they can connect by referencing container names <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>).
    *   Database: `postgres` <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Username and Password: Use values from your `.env` file <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
*   **Supabase (Vector Store Node)**:
    *   Host: `host.docker.internal` <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a> (This tells n8n to go outside to your local machine and then back into Port 8000, which maps to the Supabase container <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>).
    *   Service Role Secret: Use the `SUPABASE_SERVICE_ROLE_KEY` from your `.env` file <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.

### 2. Set Up Supabase Vector Store
Before using the Supabase node for vector storage, you need to configure your database:
1.  Navigate to the Supabase dashboard (`http://localhost:8000`) <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.
2.  Go to the "Docs" tab, then "Quick Start" for setting up a vector store <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.
3.  Copy the provided SQL script <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.
4.  In the Supabase SQL editor, create a new snippet and paste the SQL <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
5.  **Important**: Change the `vector size` to `768` as it corresponds to the `nomic-embed-text` model used with Ollama <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
6.  Run the SQL script <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>. This creates the `documents` table for your vector store <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.

### 3. Local File Ingestion Pipeline (n8n Workflow)
An n8n workflow for ingesting local files into the Supabase vector store is automatically imported <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
*   **Local File Trigger**: This node watches for files added or changed in the `/data/shared` folder <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This folder is mapped to a shared folder on your personal computer <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   **Workflow Logic**:
    *   When a file is changed, the workflow first cleans the vector database of any existing vectors for that file using a metadata filter based on the file path <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>.
    *   It then pulls the file contents <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a> and extracts the text <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
    *   Finally, the text is inserted as vectors into the Supabase `documents` table <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### 4. Test the RAG Agent
After setting up the workflow and inserting data, you can interact with your local RAG agent <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>. The agent will use Ollama (running locally with your GPU if configured) and retrieve information from your local Supabase vector store <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.

## Troubleshooting

A troubleshooting section is available in the local AI package's README, addressing common issues encountered when [[selfhosting_supabase_with_docker | running Supabase locally]] <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.