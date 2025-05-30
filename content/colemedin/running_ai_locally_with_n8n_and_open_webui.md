---
title: Running AI locally with n8n and Open WebUI
videoId: E2GIZrsDvuM
---

From: [[colemedin]] <br/> 

This article details how to integrate Open WebUI into a local AI setup, allowing users to interact with their [[ai_automation_with_n8n | n8n]] agent workflows through a user-friendly chat interface <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This extends the existing [[setting_up_a_local_ai_cloud_stack | Local AI Starter Kit]] by adding custom functionality that enables chatting with [[building_ai_agents_with_n8n | n8n workflows]] directly within Open WebUI, similar to interacting with any [[running_ai_agents_on_local_machines | Ollama model]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The integration also supports voice interaction with [[ai_automation_with_n8n | n8n agents]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Components of the Local AI Stack

The foundation of this local AI setup is the [[setting_up_a_local_ai_cloud_stack | Local AI Starter Kit]], originally developed by the [[ai_automation_with_n8n | n8n]] team <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This kit provides a Docker Compose file that combines various services into a single package for local hosting <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>, making [[setting_up_local_ai_workflows_with_n8n | local AI]] accessible <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

The services included are:
*   **[[ai_automation_with_n8n | n8n]]**: Used for building workflow automations and creating [[building_ai_agents_with_n8n | AI agents]] <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
*   **Ollama**: Manages large language models (LLMs) <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Qdrant**: Serves as the vector database for Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **PostgreSQL**: Handles the SQL database for functionalities like chat memory for agents <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   **Open WebUI**: An open-source, ChatGPT-like interface primarily used for chatting with LLMs running with Ollama <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. It supports custom functionality through "functions" and "pipelines" <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

All these services run as containers packaged together, operating entirely locally <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Setting Up the Local AI Stack

The setup leverages a forked version of the [[setting_up_a_local_ai_cloud_stack | Local AI Starter Kit]] repository, with the primary addition being Open WebUI <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

### Docker Compose Configuration
Open WebUI is added as a fifth container service within the Docker Compose file <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. The project aims for simplicity, making it easy to get started with [[setting_up_local_ai_workflows_with_n8n | local AI]] <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

Users can modify the Docker Compose file to specify which Ollama models are pulled when the Docker Compose command is run <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. For example, `llama3.1` for the LLM and `nomic-embed-text` for the embedding model are default <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. More models can also be pulled from within the Ollama container while it's running <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

### Installation Steps
To install from scratch:
1.  **Configure `.env` file**: Before running installation commands, users must edit the `env.example` file to their preferences (e.g., PostgreSQL username, password, database name, and encryption keys), then rename it to `.env` <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
2.  **Run Docker Compose**: Execute the appropriate `docker compose up` command based on your system (Nvidia GPU, Mac, or CPU-only) as detailed in the README <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. This will pull all necessary containers and start the services locally <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>. Docker Desktop is recommended for managing containers <a class="yt-timestamp" data-t="07:01:00">[07:01:01]</a>.

## Configuring n8n for AI Agent Workflows

Once the Docker Compose setup is running, [[ai_automation_with_n8n | n8n]] can be accessed at `localhost:5678` <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>. Users will create a local account, which is not connected to the internet <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.

The setup includes a pre-packaged "local RAG AI agent" workflow <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>. This workflow demonstrates how to combine Qdrant, PostgreSQL, [[ai_automation_with_n8n | n8n]], and Ollama <a class="yt-timestamp" data-t="09:02:00">[09:02:02]</a>.

### Workflow Details
The demonstration workflow is designed as a webhook for [[integrating_ai_agents_in_n8n_using_open_web_ui | integration with Open WebUI]] <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.

*   **Webhook Node**:
    *   It is configured as a `POST` request with a path like `/invoke-n8n-agent` <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
    *   Authentication is optional for local use <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
    *   The "Respond from" option must be set to "Using respond to webhook node" to prevent immediate responses <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.
    *   The incoming request body is expected to contain a `session ID` (for chat history) and `chatInput` (the user's prompt) <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.
*   **AI Agent Node**:
    *   Takes the `chatInput` from the webhook as its prompt <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.
    *   Uses Ollama as its chat model <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
*   **Credentials Setup**:
    *   **Ollama**: The base URL for Ollama credentials is `http://ollama:11434` <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
    *   **PostgreSQL**: The host is `postgres` (the container name), and the user/password are defined in the `.env` file <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
*   **Respond to Webhook Node**: Returns the `output` attribute from the LLM back to Open WebUI <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.

### Workflow Tools
*   **Vector Store Tool (Qdrant)**: Integrated into the agent for RAG <a class="yt-timestamp" data-t="12:58:00">[12:58:00]</a>.
    *   Retrieves documents based on query <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.
    *   Credentials: API key is irrelevant for local setup, and the URL is `http://qdrant:6333` <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
    *   The Qdrant dashboard is available at `localhost:6333/dashboard` to interact with the vector database <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>.
*   **Knowledge Base (Google Drive Example)**: Demonstrates ingesting documents into the vector store <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
    *   Users can use a local file trigger instead to maintain a fully local setup <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>.
    *   Note: Google Drive OAuth redirect URL cannot be `localhost` for setup, requiring an actual domain <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

## Integrating Open WebUI with n8n

Open WebUI is accessible at `localhost:3000` <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>. Like [[ai_automation_with_n8n | n8n]], it requires a local account setup <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.

### Correcting Ollama API URL
A common issue is Open WebUI attempting to pull models from a locally installed Ollama instead of the containerized one. To fix this:
1.  Go to **Admin Panel** > **Settings** > **Connections** <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.
2.  Change the Ollama API URL to `ollama` (the container name) <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.
3.  Save and reload the page <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>. This ensures Open WebUI uses the Ollama models from the Docker container <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>.

### Using Open WebUI Functions for n8n Integration
The [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n integration]] is achieved using Open WebUI's "Functions" feature <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>.
1.  Navigate to **Workspace** > **Functions** in Open WebUI <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.
2.  The n8n pipe function is available and published on the Open WebUI function list <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. It can be easily installed by clicking "Get" <a class="yt-timestamp" data-t="21:45:00">[21:45:00]</a>.
3.  **Function Configuration**:
    *   Functions are Python scripts with a `pipe` class <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.
    *   "Valves" are parameters that users can customize without editing the code <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.
    *   Key valves include: `n8n_url`, `bearer_token` (optional), `input_field` (e.g., `chatInput`), and `json_response_field` (the property containing the LLM response) <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.
    *   **Crucially**, for the `n8n_url` in Open WebUI, use `n8n` as the host instead of `localhost` (e.g., `http://n8n:5678/webhook/invoke-n8n-agent`) to ensure containers communicate correctly <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.
    *   The `pipe` function extracts the last user question, makes a POST request to the [[ai_automation_with_n8n | n8n URL]], passes the `session ID` (derived from user ID and first prompt due to current Open WebUI limitations) and user input, and then appends the LLM response to the conversation <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.

### Chatting with the n8n Agent
Once the function is enabled, the "n8n pipe" will appear as a selectable model in Open WebUI, alongside other Ollama models <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. Users can then chat directly with their [[building_ai_agents_with_n8n | n8n AI agent]] <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>. The execution history in [[ai_automation_with_n8n | n8n]] confirms the workflow is being used for the chat <a class="yt-timestamp" data-t="22:48:00">[22:48:00]</a>.

### Customization and Future Potential
This function can be customized to interact with any type of agent (e.g., [[prototyping_ai_agents_using_n8n | LangChain]], LlamaIndex, or swarm agents) by modifying the HTTP request within the Python script <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>. Open WebUI's "Pipelines" feature offers even greater flexibility, allowing installation of external dependencies for more complex [[ai_automation_with_n8n | AI automation]] setups <a class="yt-timestamp" data-t="23:46:00">[23:46:00]</a>.

## Voice Chat with AI Agents
A significant feature of Open WebUI is the ability to use voice to chat with [[ai_automation_with_n8n | n8n AI agents]] <a class="yt-timestamp" data-t="24:06:00">[24:06:00]</a>. By clicking the call button and enabling the microphone, users can verbally interact with their agents <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>.

## Conclusion
This integration successfully extends the [[setting_up_a_local_ai_cloud_stack | local AI starter kit]] to include Open WebUI, allowing seamless chat interaction with [[ai_automation_with_n8n | n8n workflow agents]] as if they were standard Ollama models <a class="yt-timestamp" data-t="25:36:00">[25:36:00]</a>. The developer plans to continue extending this [[setting_up_a_local_ai_cloud_stack | local AI stack]] in the future <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>.