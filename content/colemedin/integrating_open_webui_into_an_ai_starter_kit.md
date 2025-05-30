---
title: Integrating Open WebUI into an AI starter kit
videoId: E2GIZrsDvuM
---

From: [[colemedin]] <br/> 

This article details the process of integrating [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] into a local AI starter kit, allowing users to chat with their locally hosted AI setups and [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n workflows]] through a feature-rich interface <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Local AI Starter Kit

Previously, a local AI starter kit was developed by the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] team to run AI components locally, including LLMs, vector databases for RAG, and [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] for [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agent]] workflows <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The kit provides a Docker Compose file to combine various services into a single package for local hosting <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The original [[running_ai_locally_with_n8n_and_open_webui | self-hosted AI starter kit]] repository includes the following services:
*   **n8n**: For building workflow automations and creating [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]] <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Olama**: For large language models (LLMs) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Qdrant**: For the vector database used in RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **PostgreSQL**: For SQL database needs, such as handling chat memory for [[integrating_ai_agents_in_n8n_using_open_web_ui | agents]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

All these services run completely locally as packaged containers <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Adding Open WebUI
[[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] was integrated into the local AI starter kit by adding its container to the Docker Compose file <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This addition allows for direct chat interaction with [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] workflows within [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]], similar to interacting with an Olama model <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Installation and Setup

To set up the extended local AI starter kit with [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]]:

1.  **Repository Cloning**: Clone the repository which is a fork of the original local AI starter kit with [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] added <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Environment Configuration (`.env` file)**:
    *   Go to the `env.example` file <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   Customize settings for PostgreSQL (username, password, database name) <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Set encryption keys (can be any relatively long alphanumeric string as it runs locally) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   Rename the file to `.env` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  **Docker Compose Execution**:
    *   Run the appropriate Docker Compose commands based on your system (Nvidia GPU, Mac, or CPU) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   It is recommended to use Docker Desktop for managing Docker containers <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   The command will pull all necessary Docker containers and start the services (PostgreSQL, [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]], Qdrant, Olama, [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]]) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
4.  **Olama Model Configuration**:
    *   The Docker Compose file specifies which Olama models are pulled by default (e.g., `llama3.1` for LLM, `nomic-embed-text` for embedding) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   You can modify the `docker-compose.yml` file to change or add other Olama models <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   Additional models can also be pulled from within the Olama container while it's running <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## n8n Workflow Integration

Once the setup is complete, [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] can be accessed at `localhost:5678` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. A local account needs to be created upon first access <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

A pre-packaged demo workflow called "Local RAG AI Agent" is automatically included in the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] instance <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This workflow integrates all the services: Qdrant, PostgreSQL, [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]], and Olama <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Workflow Components and Credentials

*   **Webhook**: The workflow starts with a webhook node configured as a POST request with a specific path (e.g., `/invoke-n8n-agent`) <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This URL acts as the endpoint for [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] to communicate with the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
    *   The webhook should be configured to "Respond to Webhook Node" instead of "Immediately" <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   Incoming requests have a `session ID` for chat history and `chatInput` for the user's prompt <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **AI Agent Node**: This node generates responses based on the prompt from the webhook <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
    *   **Olama Credentials**:
        *   Base URL: `http://olama:11434` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
    *   **PostgreSQL Credentials**:
        *   Host: `postgress` (container name) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
        *   Database user and password are from the `.env` file <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Respond to Webhook Node**: Returns the LLM's output (`output` attribute) back to [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **Vector Store Tool**: Hooked into the [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] for RAG capabilities <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
    *   Uses **Qdrant Vector Store** to retrieve documents based on queries <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
    *   **Qdrant Credentials**:
        *   API Key: Not required for local instances <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
        *   URL: `http://quadrant:6333` (Qdrant container name) <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
*   **Knowledge Base (Example)**: An example uses Google Drive to ingest documents <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   This can be replaced with a local file trigger to keep everything entirely local <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
    *   The Qdrant dashboard is accessible at `localhost:6333/dashboard` to view collections and vectors <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

## Open WebUI Integration

[[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] can be accessed at `localhost:3000` <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. A local account needs to be created on first access <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### Configuring Olama Models in Open WebUI
If [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] pulls models from a local Olama instance on your computer instead of the container, navigate to:
*   `Admin Panel` > `Settings` > `Connections` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
*   Change the Olama API URL to `http://olama:11434` and save <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   Reload the page to see the correct models from the Docker container <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

### Integrating n8n Workflows with Open WebUI Functions

[[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] uses a feature called "functions" (or "pipes") to implement custom functionality and interact with external [[integrating_ai_agents_in_n8n_using_open_web_ui | agents]] or API endpoints <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. These functions are typically Python scripts specific to [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]]'s requirements <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

The custom "n8n pipe" for this integration is available on the [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] function list <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

#### n8n Pipe Configuration
*   **Valves (Parameters)**: The function includes customizable parameters called "valves" <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>:
    *   `n8n URL`: The URL of your [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] webhook. Importantly, use `n8n` instead of `localhost` (e.g., `http://n8n:5678/webhook/invoke-n8n-agent`) for inter-container communication <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
    *   `bearer_token` (optional): For authentication if configured <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
    *   `input_field`: The name of the property that contains the user's prompt in the webhook payload (e.g., `chatInput`) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
    *   `response_field`: The name of the property in the JSON response from the webhook that contains the LLM's reply <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **`pipe` Function**: This is the primary function logic:
    *   It extracts the last question from the user's input <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
    *   It makes an HTTP POST request to the specified [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] URL, passing the `session ID` (derived from user ID and first prompt) and user input <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
    *   It extracts the LLM's output from the response using the `response_field` valve <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
    *   The extracted output is appended to the conversation and returned <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

### Using the n8n Pipe

1.  Enable the n8n pipe in [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]]'s function settings <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
2.  In a new chat, select the "n8n pipe" from the model dropdown <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
3.  Chat with the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] [[integrating_ai_agents_in_n8n_using_open_web_ui | agent]] as you would with any Olama model <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
4.  The interaction can be verified in the [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] execution history, showing the requests and responses <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

### Customization and Advanced Features

The function allows for significant customization to interact with various types of [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]], including those hosted with LangServe, swarm [[integrating_ai_agents_in_n8n_using_open_web_ui | agents]], or LlamaIndex <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.

[[using_open_webui_features_like_voice_chat_and_functions | Open WebUI]] also includes a **voice chat** feature, enabling users to speak directly to their [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n AI agents]] <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. This can be activated by clicking the call button and enabling the microphone <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.

Furthermore, the "pipelines" feature in [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] is similar to functions but allows for the installation of more external dependencies, such as LangChain or LlamaIndex directly within the code running in [[setting_up_open_web_ui_for_ai_agent_communication | Open WebUI]] <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.