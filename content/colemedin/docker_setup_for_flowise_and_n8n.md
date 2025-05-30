---
title: Docker setup for Flowise and n8n
videoId: 23s2N3ug8B8
---

From: [[colemedin]] <br/> 

The future of AI involves running large language models (LLMs), RAG pipelines, and [[workflow_automation_with_n8n | workflow automations]] locally on your machine <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This article details how to set up Flowise and n8n using Docker within a local AI starter kit.

## The Local AI Starter Kit

A few months prior, an [[setting_up_a_local_ai_starter_kit_with_flowise | n8n team-developed local AI starter kit]] was introduced as a proof of concept for running AI needs locally <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This kit demonstrates that running everything locally, with sufficient power on your computer, is very close to reality <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The primary limitation currently is that open-source LLMs are not as powerful as closed-source ones, but this gap is rapidly closing <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

More recently, Open Web UI was added to the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] to facilitate interaction with [[prototyping_ai_agents_using_flowise_and_n8n | n8n agents]] via a locally hosted UI <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Now, Flowise has also been integrated into the mix <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Flowise is a free, open-source, low/no-code AI automation tool built on LangChain <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It pairs exceptionally well with [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] remains a favored no-code AI automation platform due to its integration with hundreds of applications, it has a steeper learning curve, especially for building AI agents <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Flowise, on the other hand, is simpler and ideal for rapidly [[prototyping_ai_agents_using_flowise_and_n8n | prototyping AI agents]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Flowise integrates with [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] by using [[workflow_automation_with_n8n | n8n workflows]] as agent tools for interacting with services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This combination allows for quickly building powerful AI agents that can perform various tasks <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. The entire setup, including Flowise and [[overview_of_n8n_as_a_workflow_automation_tool | n8n]], runs within the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Prerequisites for Docker Setup

To run Flowise and the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]], the primary prerequisites are:
*   **GitHub Desktop** <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>
*   **Docker Desktop** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

Flowise itself can be run with npm or Docker <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, but Docker is utilized for the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Setting up the Local AI Starter Kit with Flowise

The setup process is straightforward, requiring only a few commands <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

1.  **Clone the Repository**: Use `git clone` to get the repository <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    ```bash
    git clone [repository_url]
    ```
2.  **Navigate to the Directory**: Change into the `Local AI package` directory <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    ```bash
    cd Local AI package
    ```
3.  **Configure Environment Variables**:
    *   Rename the `env.example` file to `.env` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   You can modify PostgreSQL settings or leave them as default <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   For [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] encryption, set a random alphanumeric string for the environment variable <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   The Docker Compose file within the kit defines the Flowise service <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. It typically runs Flowise on Port `3001` (as Port `3000` is used by Open Web UI) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

4.  **Start Services with Docker Compose**:
    *   Run the `docker compose up` command.
    *   For Linux, use `docker-compose` instead of `docker compose` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
    *   Options are available to specify NVIDIA GPU usage, Mac, or CPU-only modes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    ```bash
    docker compose up -d # (or docker-compose for Linux, and add flags for GPU/Mac)
    ```
    This command will pull all necessary Docker images and spin up the services <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

Once installed, Docker Desktop will show your Compose stack with all services running, including [[overview_of_n8n_as_a_workflow_automation_tool | n8n]], Quadrant, PostgreSQL, and Flowise <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Debugging Docker Containers

Docker Desktop provides tools to debug containers in real-time <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. By clicking on any container, you can view logs and execute commands within the image <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This visibility is crucial for building and debugging your local AI stack <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Accessing Local AI Services

Once running, you can access the services in your browser:
*   **Flowise**: `http://localhost:3001` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
*   **n8n**: `http://localhost:5678` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
*   **Open Web UI**: `http://localhost:3000` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>

The specific ports can be referenced in the Docker Compose file within the repository <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Container Communication and Ollama

When one Docker container needs to communicate with another, you must reference the **container name** (as defined in the Docker Compose file) rather than `localhost` <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. For example, to reference the Ollama instance running *within* the starter kit container, you would use `ollama` as the base URL <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

If you want Flowise to use an Ollama instance running directly on your host machine (outside the Docker container), the base URL should be `host.docker.internal` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This is standard Docker notation for referencing the host machine <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

When configuring Ollama models, it's important to adjust the **context window size** <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. By default, Ollama models often cap at 2048 tokens, which can lead to truncation of conversation history or tool output <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Increasing this to a larger value, such as 32,000, prevents models from hallucinating or missing tool calls due to truncated context <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Integrating n8n Workflows as Flowise Tools

[[using_flowise_and_n8n_for_local_ai_automation | Using Flowise and n8n for local AI automation]] is achieved by exposing [[setting_up_local_ai_workflows_with_n8n | n8n workflows]] as API endpoints that Flowise can call <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Setting up n8n Workflows as Tools

1.  **Web Hook Trigger**: Every [[using_n8n_for_api_workflows_in_ai_agents | n8n tool]] workflow starts with a Web Hook trigger (either GET or POST) to receive API calls from Flowise <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
2.  **Authentication**: While optional, you can set up basic test header authentication for your Bearer token <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
3.  **Respond to Web Hook**: Each [[using_n8n_for_api_workflows_in_ai_agents | n8n tool]] should end with a "Respond to Web Hook" node <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
4.  **Example: Get PostgreSQL Tables**: A simple example tool queries tables in a locally hosted PostgreSQL database, demonstrating integration with another service in the [[setting_up_a_docker_compose_for_local_ai_services | local AI starter kit]] <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

### Setting up Flowise Custom Tools for n8n

Flowise uses "Custom Tool" nodes to make API requests to [[overview_of_n8n_as_a_workflow_automation_tool | n8n workflows]] <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

1.  **Custom Tool Node**: Drag a "Custom Tool" node into your Flowise chat flow <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
2.  **Name and Description**: Give the tool a name and a descriptive purpose. The description helps the LLM determine when to use the tool <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
3.  **Input Schema**: Define the properties (like database name or message content) that the tool requires as input, along with their types and descriptions. This guides the LLM on how to call the tool <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
4.  **Custom Code (JavaScript)**:
    *   The "Custom Tool" contains basic JavaScript code to make an API request to the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] workflow <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
    *   Reference the [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] container using its name (e.g., `n8n`) and port (`5678`) for the `workflowUrl` <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
    *   The specific web hook URL from [[overview_of_n8n_as_a_workflow_automation_tool | n8n]]'s production URL is appended <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
    *   **Important**: Do not hardcode credentials like bearer tokens in the tool code <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. Instead, define them as **variables** within Flowise's dedicated "Variables" tab <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. These can then be referenced in the code using `$` `vars.variableName` <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.

### Examples of Integrated Tools

Beyond the PostgreSQL example, [[creating_powerful_ai_workflows_with_n8n | n8n workflows]] can serve as tools for various actions:
*   **Summarize Slack Conversation**: Fetches messages from a Slack channel, summarizes them using an LLM (e.g., GPT-4 Mini), and returns the summary <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.
*   **Create Google Doc**: Creates a Google Drive file based on provided text and title <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.
*   **Send Message in Slack**: Sends a message to a hardcoded Slack channel (or could be parameterized) <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.

**Note on HTTPS**: For [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] to integrate with services like Google Drive and Slack, it needs to be hosted with HTTPS <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. A purely local setup using only `localhost` might not support setting up these credentials, requiring a self-hosted [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] instance with a real domain for such integrations <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

This [[using_flowise_and_n8n_for_local_ai_automation | integration of Flowise and n8n]] within the [[setting_up_a_docker_compose_for_local_ai_services | Docker Compose setup]] allows for rapid [[prototyping_ai_agents_using_flowise_and_n8n | prototyping AI agents]] that can combine web search, internal database queries, and external service interactions <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>.