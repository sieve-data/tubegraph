---
title: Setting up a local AI starter kit with Flowise
videoId: 23s2N3ug8B8
---

From: [[colemedin]] <br/> 

The future of AI involves running operations locally, including LLMs, RAG pipelines, and workflow automations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The [[local_ai_package_setup | local AI starter kit]], originally developed by the n8n team, provides a powerful proof of concept for running AI needs locally <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The biggest current limitation is that open-source LLMs aren't as powerful as closed-source ones, but this gap is rapidly closing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Recently, [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI was integrated into the local AI starter kit]] for interacting with n8n agents via a locally hosted UI <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Now, Flowise is being added to the mix <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## What is Flowise?
Flowise is a free, open-source, low/no-code AI automation tool built on LangChain <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It pairs well with n8n <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While n8n is a powerful no-code AI automation platform with extensive integrations, it has a steeper learning curve for building AI agents <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Flowise, on the other hand, simplifies the rapid [[prototyping_ai_agents_using_flowise_and_n8n | prototyping of AI agents]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The ideal combination involves using Flowise to build agents quickly and integrating it with n8n workflows as agent tools for interacting with services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Components of the Local AI Starter Kit with Flowise
The extended local AI starter kit, with Flowise, includes several services running in a Docker Compose stack <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>:
*   **n8n** <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
*   **Quadrant** <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>
*   **Postgres** <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>
*   **Flowise** <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
*   **Open WebUI** (optional, for interaction) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
*   **Ollama** (can be containerized or hosted on the local machine) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>

## Prerequisites for Setup
To run the local AI starter kit with Flowise, you primarily need:
*   **GitHub Desktop**: For cloning the repository <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Docker Desktop**: For running the services in containers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Installation Steps
The setup process involves a few commands to get everything running within the [[setting_up_a_local_ai_cloud_stack | local AI cloud stack]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>:

1.  **Clone the Repository**:
    ```bash
    git clone [repository-url]
    ```
    This step requires GitHub Desktop <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

2.  **Navigate into the Directory**:
    ```bash
    cd local-ai-package # or the name of the cloned repo
    ```
    This changes your current directory to the repository folder <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

3.  **Configure Environment Variables**:
    *   Rename the `env.example` file in the repository to `.env` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   You can customize PostgreSQL settings or use the defaults <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
    *   For n8n encryption, set a random alphanumeric string for `N8N_ENCRYPTION_KEY` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

4.  **Run Docker Compose**:
    ```bash
    docker compose up -d --build --pull always --remove-orphans --env-file .env # for CPU, or add --file docker-compose.cuda.yaml for Nvidia GPU
    ```
    This command starts all services defined in the `docker-compose.yaml` file <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Instructions for Nvidia GPU, Mac, and CPU-only setups are available <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The command will pull necessary Docker images if not already present <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Accessing Services
Once the Docker Compose command completes, services will be running:
*   **Flowise**: Accessible at `localhost:3001` (default) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **n8n**: Accessible at `localhost:5678` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Open WebUI**: Accessible at `localhost:3000` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

To confirm services are running, check Docker Desktop, which shows the compose stack and individual containers <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Docker Desktop also provides logs and an "exec" tab for debugging containers in real-time <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Building an AI Agent in Flowise

The primary goal is to build an AI agent that can search the web and interact with [[setting_up_local_ai_workflows_with_n8n | n8n workflows]] to perform tasks like creating Google Docs, summarizing Slack conversations, and sending Slack messages <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Step-by-Step Agent Creation in Flowise
1.  **Add a Tool Agent Node**: This is the starting point for connecting various components <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
2.  **Configure Memory**:
    *   Start with `Buffer Memory` for simplicity <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
    *   Postgres can also be used for more robust memory within the starter kit <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
3.  **Set up the Chat Model (Ollama)**:
    *   Drag in the `Chat Ollama` node <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   **Base URL**: This is crucial for local deployments <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
        *   To reference Ollama running *on your computer* (the host machine), use `host.docker.internal` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
        *   To reference Ollama running *within the Docker container* of the starter kit, use the container name, which is `ollama` <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
    *   **Model Name**: Specify the model name (e.g., `qwen:2.5-coder-32b`) obtained from the `ollama list` command in your terminal <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   **Context Window Size**: Critically, increase the default `2048` tokens to a larger value (e.g., `32000`) to prevent truncation of long conversations or tool outputs, which can lead to poor performance and hallucinations <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
4.  **Add a Caching Layer**: An in-memory cache can be used, with Redis recommended for robust applications <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Integrating Tools
Tools are essential for the agent's functionality <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

#### 1. Brave Search API
*   Drag in the `Brave Search API` tool node <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   Connect it to the `Tool Agent` <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   Set up credentials by providing your Brave Search API key, which will be saved for future use <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

#### 2. n8n Workflows as Custom Tools
Integrating [[setting_up_local_ai_workflows_with_n8n | n8n workflows]] as tools involves creating `Custom Tool` nodes in Flowise <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. These tools use API requests to interact with n8n workflows <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

*   **n8n Workflow Setup**: Each n8n tool workflow needs a `Webhook` trigger and a `Respond to Webhook` node <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Authentication (e.g., Bearer token) can be used <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Flowise Custom Tool Configuration**:
    *   **Name and Description**: The description is crucial as it tells the LLM when to use the tool <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
    *   **Input Schema**: Defines the properties (e.g., database name, message content) the tool expects, also used by the LLM to know how to call the tool <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
    *   **Code (JavaScript)**: Simple JavaScript code makes an API request to the n8n workflow <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
        *   **Workflow URL**: Reference the n8n container name (e.g., `n8n`) and its port (`5678`) when one container talks to another, instead of `localhost` <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
        *   **Bearer Token/Variables**: Use Flowise's "Variables" feature to store credentials securely and reference them with `$vars.variableName` in the code <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

### Example n8n-powered Tools:
*   **Get Postgres Tables**: Queries the local PostgreSQL database service within the starter kit <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Summarize Slack Conversation**: Fetches messages from a Slack channel and summarizes them using an LLM (requires n8n hosted with HTTPS and a domain for Slack credentials) <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Create Google Doc**: Creates a Google Drive file based on provided text and title (requires n8n hosted with HTTPS and a domain for Google Drive credentials) <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
*   **Send Message in Slack**: Sends a message to a specific Slack channel <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.

## Demonstration of Integrated Agent Capabilities
An agent built with Flowise, n8n, and Ollama can perform complex tasks:
1.  **Summarize Slack Conversation & Web Search**: The agent can summarize a Slack conversation about a problem (e.g., finding Elon Musk's net worth) and then use a web search tool to find the answer <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>. The agent can use multiple tools in one request <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
2.  **Create Google Doc with Findings**: Based on the summarized conversation and web search results, the agent can create a concise Google Doc outlining its findings, including a link to the new document <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
3.  **Send Slack Message**: Finally, the agent can send a Slack message containing the Google Doc link and a summary of its findings <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.

This demonstrates the powerful synergy of [[using_flowise_and_n8n_for_local_ai_automation | using Flowise and n8n together]] for rapid AI agent prototyping and robust local automation <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.