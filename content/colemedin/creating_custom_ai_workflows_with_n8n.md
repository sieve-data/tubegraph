---
title: Creating custom AI workflows with n8n
videoId: E2GIZrsDvuM
---

From: [[colemedin]] <br/> 

This article details how to set up a local AI environment using the [[setting_up_local_ai_workflows_with_n8n | local AI starter kit]] and integrate it with Open Web UI to enable conversational interaction with [[ai_automation_with_n8n | AI agents]] built in [[workflow_automation_with_n8n | n8n]]. The goal is to provide a user-friendly interface for local AI setups, allowing users to chat with their [[workflow_automation_with_n8n | n8n]] workflows directly [00:00:38](<a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## The Local AI Starter Kit

The [[setting_up_local_ai_workflows_with_n8n | local AI starter kit]], originally developed by the [[workflow_automation_with_n8n | n8n]] team, enables running all AI components locally, including LLMs, a vector database for RAG, and [[workflow_automation_with_n8n | n8n]] for agent workflows [00:00:00](<a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This kit packages various services together using a Docker Compose file [00:02:16](<a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

Key services included in the starter kit:
*   **[[overview_of_n8n_as_a_workflow_automation_tool | n8n]]**: Used for building workflow automations and [[building_ai_agents_with_n8n | AI agents]] [00:02:33](<a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Ollama**: For large language models (LLMs) [00:02:38](<a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Qdrant**: A vector database for [[creating_rag_ai_agents_using_n8n | RAG (Retrieval Augmented Generation)]] [00:02:41](<a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Postgres**: A SQL database for handling chat memory for [[building_ai_agents_with_n8n | AI agents]] [00:02:44](<a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

All these services run as Docker containers completely locally, offering a comprehensive package for local AI development [00:02:50](<a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Integrating Open Web UI

A significant enhancement to the local AI starter kit is the addition of Open Web UI, an open-source ChatGPT-like interface [00:00:18](<a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, [00:00:52](<a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This integration allows users to chat with their local AI setup through a feature-rich interface [00:00:21](<a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Open Web UI includes key features like "functions" and "pipelines" that enable custom functionality, such as chatting with [[building_ai_agents_with_n8n | AI agents]] and API endpoints [00:01:00](<a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This capability was leveraged to build the Open Web UI and [[workflow_automation_with_n8n | n8n]] integration [00:01:12](<a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The integration is even published on the Open Web UI function list [00:01:17](<a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Setup and Installation

The setup process involves cloning the customized repository, which includes the Open Web UI addition [00:04:47](<a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

1.  **Environment Configuration**: Before running Docker Compose, modify the `env.example` file to define settings for Postgres (username, password, database name) and encryption keys, then rename it to `.env` [00:05:54](<a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
2.  **Docker Compose**: Execute `docker compose` commands based on your system (Nvidia GPU, Mac, or CPU) [00:05:44](<a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This command pulls all necessary containers (Postgres, Open Web UI, Qdrant, Ollama, [[workflow_automation_with_n8n | n8n]]) and starts the services [00:06:40](<a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Ollama Models**: You can customize which Ollama models are pulled by editing the `docker-compose` file [00:07:33](<a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. For example, `llama3.1` for the LLM and `nomic-embed-text` for the embedding model [00:07:42](<a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
3.  **Accessing n8n**: Once services are running, [[workflow_automation_with_n8n | n8n]] can be accessed at `http://localhost:5678` [00:08:12](<a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. A local account needs to be created upon first access [00:08:26](<a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## [[creating_powerful_ai_workflows_with_n8n | Creating AI Workflows with n8n]]

The setup includes a pre-packaged "local RAG AI agent" workflow in your [[workflow_automation_with_n8n | n8n]] instance [00:08:49](<a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This workflow demonstrates how to combine Qdrant, Postgres, [[workflow_automation_with_n8n | n8n]], and Ollama [00:09:02](<a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Workflow Components and Credentials

*   **Webhook Node**:
    *   Starts the workflow, configured as a `POST` request with a specific path (e.g., `invoke-n8n-agent`) [00:10:06](<a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   Authentication can be set to `None` for local use, or `Header Auth` for a bearer token [00:10:26](<a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
    *   Crucially, `Respond from` must be set to `Using respond to web hook node` to avoid immediate responses [00:10:40](<a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   The webhook receives a `session ID` for chat history and `chat input` as the prompt for the LLM [00:11:11](<a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **AI Agent Node**:
    *   Generates a response based on the `chat input` from the webhook [00:10:56](<a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   Uses Ollama as the chat model [00:11:30](<a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Credential Setup**:
    *   **Ollama**: Base URL is `http://olama:11434` (default port) [00:11:40](<a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   **Postgres**: Host is `postgress` (container name), and credentials are set in the `.env` file [00:12:13](<a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
    *   **Qdrant**: API key is not required for local use, and the URL is `http://quadrant:6333` (container name and default port) [00:13:14](<a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Respond to Webhook Node**:
    *   Returns the `output` attribute from the LLM response back to Open Web UI [00:12:37](<a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### Tools and Knowledge Base

*   **Vector Store Tool**: Hooked into the agent for RAG [00:12:58](<a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. It uses the Qdrant Vector store to retrieve documents based on the query [00:13:03](<a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Knowledge Base (e.g., Google Drive)**: Documents can be ingested from various sources. An example uses Google Drive to ingest documents, delete old vectors, extract text, and then insert it into the Qdrant Vector store [00:13:51](<a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. Local file triggers can also be used [00:14:42](<a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Qdrant Dashboard**: Accessible at `http://localhost:6333/dashboard`, it allows interaction with the vector database outside of [[workflow_automation_with_n8n | n8n]] [00:14:57](<a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

## [[building_ai_agents_with_n8n | Integrating n8n with Open Web UI]]

### Accessing Open Web UI and Ollama Configuration

Open Web UI is accessed at `http://localhost:3000` [00:15:31](<a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Similar to [[workflow_automation_with_n8n | n8n]], a local account needs to be created [00:15:37](<a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

*   **Ollama API URL**: If Open Web UI pulls models from a locally installed Ollama instead of the containerized version, change the Ollama API URL in the Open Web UI admin panel settings (Connections) to `olama` [00:16:11](<a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### [[using_n8n_for_api_workflows_in_ai_agents | n8n Integration using Open Web UI Functions]]

The integration is achieved using Open Web UI's "functions" feature [00:16:53](<a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. Functions allow specifying custom functionality for interacting with agents and API endpoints, including [[workflow_automation_with_n8n | n8n]] webhooks [00:17:06](<a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

*   **`n8n_pipe` Function**: This Python script is designed specifically for Open Web UI integration [00:17:34](<a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
    *   **Valves (Parameters)**: Customizable settings include the [[workflow_automation_with_n8n | n8n]] URL, bearer token (optional), input field name (e.g., `chatInput`), and the JSON response property containing the LLM's output [00:18:48](<a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
    *   **n8n URL Convention**: For communication between Docker containers, `localhost` in the [[workflow_automation_with_n8n | n8n]] webhook URL must be replaced with `n8n` [00:19:53](<a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
    *   **`pipe` Function Logic**:
        *   Extracts the last user question from the conversation [00:20:41](<a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
        *   Makes an HTTP POST request to the [[workflow_automation_with_n8n | n8n]] URL [00:20:46](<a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
        *   Payload includes a session ID (derived from user ID and first prompt) and the user's last message [00:20:53](<a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
        *   Extracts the LLM's output from the response and appends it to the conversation [00:21:21](<a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
    *   The `n8n_pipe` function can be easily imported into Open Web UI or pasted as code [00:21:38](<a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>. Once enabled, it appears as a selectable "model" in new chats [00:21:56](<a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

### Interacting with the [[building_ai_agents_with_n8n | n8n]] Agent

When the `n8n_pipe` is selected, user inputs are sent to the [[workflow_automation_with_n8n | n8n]] workflow, and responses are returned, demonstrating seamless interaction [00:22:09](<a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. The [[workflow_automation_with_n8n | n8n]] execution history confirms that the workflow is actively processing requests from Open Web UI [00:22:48](<a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

### Customization and Voice Chat

*   **Extending to Any Agent**: The Open Web UI function can be easily customized to interact with any agent, whether it's hosted via Langserve, swarm agents, or LlamaIndex [00:23:25](<a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   **Pipelines Feature**: Open Web UI's "pipelines" feature allows installing more external dependencies, enabling direct integration of frameworks like LangChain or LlamaIndex within the Open Web UI code [00:23:46](<a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
*   **Voice Chat**: Open Web UI supports voice-to-chat interaction with [[ai_automation_with_n8n | n8n AI agents]], enhancing accessibility and user experience [00:24:06](<a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. This feature is enabled by clicking the call button and enabling the microphone [00:24:17](<a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.

The integration successfully extends the [[setting_up_local_ai_workflows_with_n8n | local AI starter kit]] to include Open Web UI, allowing users to chat with their [[creating_powerful_ai_workflows_with_n8n | workflow agents]] in [[workflow_automation_with_n8n | n8n]] just like any Ollama model [00:25:36](<a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.