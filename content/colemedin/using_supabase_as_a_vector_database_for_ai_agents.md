---
title: Using Supabase as a vector database for AI agents
videoId: pOsO40HSbOo
---

From: [[colemedin]] <br/> 

[[superbase_integration_for_ai_projects | Supabase]] is an open-source platform that has become a popular database choice for [[Using Supabase for AI agents | AI agents]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Built on PostgreSQL, it can be used for managing conversation history and state for agents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Crucially, the PG Vector extension allows [[Using Supabase as a vector database | Supabase to function as a vector database]] for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

Beyond its core database and vector store capabilities, [[superbase_integration_for_ai_projects | Supabase]] offers features like authentication and object storage out-of-the-box <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Its versatility makes it suitable for a wide range of [[Using Supabase for AI agents | AI projects]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Local AI Package Integration

[[superbase_integration_for_ai_projects | Supabase]] is entirely open source and provides self-hosting instructions with Docker <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, making it relatively straightforward to [[integrating_local_ai_services_with_supabase | integrate it into local AI services]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It has been integrated into a revamped local AI package <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, which now has its own dedicated GitHub repository <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Previously, the local AI package included n8n, Olama, Quadrant, and PostgreSQL <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. With the integration of [[superbase_integration_for_ai_projects | Supabase]], PostgreSQL has been entirely replaced, as [[superbase_integration_for_ai_projects | Supabase]] itself runs PostgreSQL under the hood <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. While Quadrant also functions as a vector store, [[superbase_integration_for_ai_projects | Supabase]] is generally preferred due to its dual functionality as both a SQL database and a vector store for RAG <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Quadrant remains in the package for use cases where its speed is advantageous <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Prerequisites for Setup

To set up the revamped local AI package with [[superbase_integration_for_ai_projects | Supabase]], the following prerequisites are required:
*   **Python:** Needed to run a script that automates much of the [[superbase_integration_for_ai_projects | Supabase]] setup <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Git or GitHub Desktop:** For cloning the repository <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Docker or Docker Desktop:** All local AI services run as Docker containers <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Environment Variable Configuration

Configuring environment variables is a key step. While the `env.example` file shows many variables, only a few are crucial for foundational [[superbase_integration_for_ai_projects | Supabase]] setup <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>:
*   **n8n credentials:** Define a JWT secret and encryption key <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **PostgreSQL password:** The password for the [[database_setup_and_management_for_ai_agents | database]] <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Dashboard login:** Set a username and password for the locally hosted [[superbase_integration_for_ai_projects | Supabase]] dashboard <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Pooler tenant ID:** For transaction Pooler connections to the [[superbase_integration_for_ai_projects | Supabase database]] <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **JWT secret, Anonymous key, and Service Role key:** These can be conveniently generated using a tool provided in [[superbase_integration_for_ai_projects | Supabase]]'s self-hosting guide <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

### Running the Local AI Stack

[[superbase_integration_for_ai_projects | Supabase]] is composed of multiple Docker containers, including the studio interface, Kong, authentication, and real-time services <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. To simplify management, a Python script ( `start_services.py`) is used <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This script:
*   Clones or updates the [[superbase_integration_for_ai_projects | Supabase]] repository <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   Combines the [[superbase_integration_for_ai_projects | Supabase]] Docker Compose file with the local AI package's own file <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   Ensures all containers run on the same Docker Network, enabling seamless connections between services like n8n and [[superbase_integration_for_ai_projects | Supabase]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   Facilitates easy restarts and updates of the entire stack; existing data and workflows persist even when containers are torn down <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### Building a RAG AI Agent with Local Supabase

The local AI package includes a pre-configured workflow in n8n for a RAG [[Using Supabase for AI agents | AI agent]] that uses a local [[superbase_integration_for_ai_projects | Supabase]] instance <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This agent utilizes:
*   Olama chat model <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
*   [[using_postgres_and_superbase_for_ai_chat_memory | Supabase for chat memory]] (via PostgreSQL node) <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   [[Using Supabase as a vector database | Supabase for vector retrieval]] <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

To set up the RAG pipeline to ingest local files into the [[superbase_integration_for_ai_projects | Supabase]] vector store:
1.  **Configure Credentials:**
    *   Olama: Base URL `http://olama:11434` <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
    *   [[superbase_integration_for_ai_projects | Supabase]] (PostgreSQL node): Host `db` <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>, database `postgres`, and the username/password defined in environment variables <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
    *   [[superbase_integration_for_ai_projects | Supabase]] Vector Store node: Host `host.docker.internal:8000` <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>, and the service roll secret from environment variables <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
2.  **Set up [[Using Supabase as a vector database | Supabase Vector Store]]:** In the [[superbase_integration_for_ai_projects | Supabase]] dashboard's SQL editor, execute the SQL snippet from the [[superbase_integration_for_ai_projects | Supabase]] docs to create the `documents` table and set the vector size (e.g., 768 for nomic-embed-text model) <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.
3.  **Local File Trigger:** The n8n workflow uses a local file trigger to watch for files added or changed in a specified shared folder (e.g., `/data/shared` in the n8n container) <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.
4.  **Ingestion Process:** When a file is added or changed, the workflow determines the event type. For changes, it cleans the vector [[database_setup_and_management_for_ai_agents | database]] of existing vectors for that file using a metadata filter <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. Then, it pulls the file, extracts the text, and inserts the new vectors into the [[superbase_integration_for_ai_projects | Supabase]] vector store <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.

Once set up, the RAG agent can answer queries based on the locally ingested documents, demonstrating a fully local [[Integration with tools like Superbase and Pyantic AI | AI pipeline]] using [[superbase_integration_for_ai_projects | Supabase]] <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.