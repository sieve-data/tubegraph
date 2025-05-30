---
title: Setting up a Docker Compose for local AI services
videoId: E2GIZrsDvuM
---

From: [[colemedin]] <br/> 

This article outlines how to set up a comprehensive local AI stack using Docker Compose, leveraging the Local AI Starter Kit. This kit bundles various AI services into a single, easily deployable package, allowing for local execution of LLMs, vector databases, and agent workflows <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Core Components of the Local AI Stack

The self-hosted AI starter kit provides a Docker Compose file that combines containers from several services, offering a streamlined package for local AI development <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:

*   **n8n**: Used for building workflow automations and creating AI agents <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Ollama**: Manages large language models (LLMs) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Qdrant**: Serves as the vector database for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **PostgreSQL**: A SQL database for handling aspects like chat memory for AI agents <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Open Web UI**: An open-source, ChatGPT-like interface for chatting with local AI setups, typically used with Ollama LLMs <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, and can be integrated with n8n workflows for custom agent interactions <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

All these services run as containers packaged together, enabling a fully local AI environment <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Setting up the Docker Compose

The process involves configuring environment variables and executing Docker commands.

### .env File Configuration

Before running Docker Compose, you must configure the `.env.example` file. Rename this file to `.env` after making your changes <a class="yt-timestamp" data-t="00:05:54">[00:06:01]</a>. This file defines settings for:
*   **PostgreSQL**: User, password, and database name <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Encryption Keys**: Can be any relatively long alphanumeric string, as operations are local <a class="yt-timestamp" data-t="00:06:09">[00:06:18]</a>.

### Modifying the Docker Compose File

The `docker-compose.yml` file orchestrates the services. Open Web UI is added as a fifth container service within this file <a class="yt-timestamp" data-t="00:03:08">[00:03:18]</a>.

You can also customize which Ollama models are pulled by editing the `docker-compose.yml` file. Look for the line specifying the Ollama models (e.g., `llama3.1`, `nomic-embed-text`) and adjust as needed <a class="yt-timestamp" data-t="00:07:33">[00:07:50]</a>. Additional models can also be pulled directly from the Ollama container while it's running <a class="yt-timestamp" data-t="00:08:02">[00:08:06]</a>.

### Running Docker Compose

To start the services:
1.  **Clone the Repository**: Use `git clone` commands to obtain the project files, which have been customized for this setup <a class="yt-timestamp" data-t="00:04:50">[00:04:56]</a>.
2.  **Execute the Command**: Run the appropriate Docker Compose command based on your system (Nvidia GPU, Mac, or CPU-only) <a class="yt-timestamp" data-t="00:05:44">[00:05:51]</a>.
    *   Example for Nvidia GPU: `docker compose --profile gpu --profile local-ai up` <a class="yt-timestamp" data-t="00:06:33">[00:06:38]</a>
    *   This command will pull all necessary containers and begin logging output from services like PostgreSQL, Open Web UI, Qdrant, and Ollama <a class="yt-timestamp" data-t="00:06:40">[00:06:49]</a>. The terminal will remain open, continuously displaying logs from the running services <a class="yt-timestamp" data-t="00:06:50">[00:06:57]</a>.

It is recommended to use Docker Desktop for managing Docker containers, though other Docker setups will also work <a class="yt-timestamp" data-t="00:07:01">[00:07:12]</a>.

## Accessing and Configuring Local Services

Once the Docker Compose stack is running, you can access and configure the individual services.

### n8n Access and Workflow

*   **URL**: Access n8n at `localhost:5678` <a class="yt-timestamp" data-t="00:08:15">[00:08:19]</a>.
*   **Account Setup**: You'll create a local account, which does not require an internet connection or real credentials <a class="yt-timestamp" data-t="00:08:26">[00:08:44]</a>.
*   **Pre-packaged Workflow**: The setup includes a "Local RAG AI agent" workflow automatically in your n8n instance <a class="yt-timestamp" data-t="00:08:49">[00:08:56]</a>. This workflow demonstrates how Qdrant, PostgreSQL, n8n, and Ollama are combined <a class="yt-timestamp" data-t="00:09:02">[00:09:08]</a>.
*   **Webhook Configuration**: The workflow starts with a webhook (e.g., path `/invoke-n8n-agent`). It's crucial to set the webhook to "respond to web hook node" instead of "immediately" to ensure the AI agent processes the request <a class="yt-timestamp" data-t="00:10:06">[00:10:47]</a>.

#### n8n Credentials for Services

*   **Ollama**: Set the base URL to `http://ollama:11434` <a class="yt-timestamp" data-t="00:11:40">[00:11:51]</a>. Note that `ollama` is used instead of `localhost` for inter-container communication <a class="yt-timestamp" data-t="00:11:40">[00:11:51]</a>.
*   **PostgreSQL**: Set the host to `postgress` (the container name) and use the user/password defined in your `.env` file <a class="yt-timestamp" data-t="00:12:15">[00:12:28]</a>.
*   **Qdrant**: The API key can be anything when running locally, as it's typically for hosted versions. The URL is `http://quadrant:6333` <a class="yt-timestamp" data-t="00:13:09">[00:13:38]</a>. Again, `quadrant` is the container name <a class="yt-timestamp" data-t="00:13:39">[00:13:41]</a>. A Qdrant dashboard is available at `localhost:6333/dashboard` to interact with your vector database <a class="yt-timestamp" data-t="00:14:57">[00:15:13]</a>.

### Open Web UI Access and Configuration

*   **URL**: Access Open Web UI at `localhost:3000` <a class="yt-timestamp" data-t="00:15:31">[00:15:36]</a>.
*   **Account Setup**: Similar to n8n, this is a local account creation <a class="yt-timestamp" data-t="00:15:38">[00:15:52]</a>.
*   **Connecting to Ollama Container**: If Open Web UI pulls models from a local Ollama installation outside the container, you need to change its API URL. Go to `Admin Panel > Settings > Connections` and set the Ollama API URL to `ollama` <a class="yt-timestamp" data-t="00:16:16">[00:16:33]</a>. This ensures it uses the Ollama instance running within your Docker Compose setup <a class="yt-timestamp" data-t="00:16:40">[00:16:46]</a>.
*   **Integrating with n8n (Functions/Pipes)**: Open Web UI uses "functions" (or "pipes") to implement custom functionality, like chatting with n8n webhooks <a class="yt-timestamp" data-t="00:17:00">[00:17:13]</a>.
    *   A custom `n8n pipe` function has been developed and published on the Open Web UI functions page <a class="yt-timestamp" data-t="00:18:25">[00:18:27]</a>.
    *   This function allows you to specify the n8n webhook URL, bearer token (optional), input field name (e.g., `chatInput`), and output response property name for dynamic integration <a class="yt-timestamp" data-t="00:18:48">[00:19:16]</a>.
    *   **Crucial for Inter-container Communication**: When setting the n8n webhook URL within Open Web UI, replace `localhost` with `n8n` (the container name) to enable proper communication between containers <a class="yt-timestamp" data-t="00:19:53">[00:20:07]</a>.
    *   Once enabled, the `n8n pipe` appears as a selectable "model" in Open Web UI, allowing you to chat with your n8n AI agents <a class="yt-timestamp" data-t="00:21:58">[00:22:06]</a>.
    *   Open Web UI also offers voice-to-chat capabilities with your n8n AI agents <a class="yt-timestamp" data-t="00:00:47">[00:00:49]</a>, accessible via the call button <a class="yt-timestamp" data-t="00:24:06">[00:24:21]</a>.

This [[running_docker_compose_for_ai_services | running Docker Compose for AI services]] setup provides a robust and accessible way to [[setting_up_a_local_ai_cloud_stack | set up a local AI cloud stack]] for development and experimentation, integrating various components for a complete local AI environment.