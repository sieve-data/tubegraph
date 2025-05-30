---
title: Secure Deployment of AI Agents
videoId: 6zn8vVTeFE0
---

From: [[colemedin]] <br/> 

When [[building_ai_agents | building AI agents]] in N8N, the default chat trigger for interacting with the agent within the workflow builder is convenient but has limitations, such as a basic appearance and no view of past conversations <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Making the chat publicly available via a web page further exposes these UI limitations, as it's not customizable and still lacks conversation history, unlike platforms like ChatGPT <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

To enhance the user interface and provide a secure deployment for N8N [[understanding_ai_agents | AI agents]], an open-source platform called Open Web UI can be used <a class="yt-timestamp" data-t="01:45">[00:01:45]</a>. This integration offers a full ChatGPT-like interface for N8N agents, complete with conversation history, formatted markdown, and features like voice interaction <a class="yt-timestamp" data-t="01:12">[00:01:12]</a>.

## Open Web UI Installation

Open Web UI is a self-hostable interface for chatting with LLMs and [[understanding_ai_agents | AI agents]] <a class="yt-timestamp" data-t="04:09">[00:04:09]</a>. It can run entirely offline on your computer and integrate with self-hosted N8N <a class="yt-timestamp" data-t="04:16">[00:04:16]</a>.

There are several installation options:
*   **Python:** If Python is installed, Open Web UI can be installed via `pip` and served using `open-webui serve` <a class="yt-timestamp" data-t="04:41">[00:04:41]</a>. It's typically accessible at `localhost:8080` <a class="yt-timestamp" data-t="04:55">[00:04:55]</a>.
*   **Docker:** Open Web UI can be easily installed with a single Docker command, offering various options based on machine configuration and whether you're using Ollama <a class="yt-timestamp" data-t="05:01">[00:05:01]</a>. For connecting directly to an N8N agent without Ollama, the default Docker command is sufficient <a class="yt-timestamp" data-t="05:21">[00:05:21]</a>. For information on [[deploying_and_scaling_ai_agents_with_docker | deploying and scaling AI agents with Docker]], consult the Open Web UI GitHub repository installation instructions <a class="yt-timestamp" data-t="04:32">[00:04:32]</a>.
*   **Local AI Package:** This package, which bundles services like a database, self-hosted N8N, Ollama, and Open Web UI, provides a convenient way to get everything running from scratch <a class="yt-timestamp" data-t="05:35">[00:05:35]</a>. Everything covered in this video can be accomplished using services included in this package <a class="yt-timestamp" data-t="05:56">[00:05:56]</a>.

After installation, Open Web UI is typically accessed via `localhost:3000` or `localhost:8080` <a class="yt-timestamp" data-t="06:24">[00:06:24]</a>.

## Integrating N8N Agents with Open Web UI

Connecting N8N [[understanding_ai_agents | AI agents]] to Open Web UI is done through a custom function within Open Web UI <a class="yt-timestamp" data-t="06:47">[00:06:47]</a>. This function handles the N8N integration <a class="yt-timestamp" data-t="06:54">[00:06:54]</a>.

The function can be imported by:
*   Visiting a specific URL and clicking the "get" button, then entering the Open Web UI URL (e.g., `localhost:3000`) and clicking "import to web UI" <a class="yt-timestamp" data-t="07:11">[00:07:11]</a>.
*   Manually copying the Python code from the function page and pasting it into the Open Web UI admin panel under the "functions" tab, then adding a function ID and description <a class="yt-timestamp" data-t="07:23">[00:07:23]</a>.

Once installed, this function acts as a custom LLM option in Open Web UI, allowing it to connect to N8N <a class="yt-timestamp" data-t="08:07">[00:08:07]</a>.

### Configuring the N8N Integration Function

The custom function requires specific configurations in Open Web UI's settings:
*   **N8N URL:** The public URL of your N8N agent's webhook trigger <a class="yt-timestamp" data-t="08:39">[00:08:39]</a>.
*   **Bearer Token:** A token used for header authentication to secure your agent <a class="yt-timestamp" data-t="08:40">[00:08:40]</a>.
*   **Input Field:** The name of the field in your N8N workflow where the user's message is expected (e.g., `chat input`) <a class="yt-timestamp" data-t="08:47">[00:08:47]</a>.
*   **Output Field:** The name of the field where the AI agent's response is outputted in the N8N workflow (e.g., `output`) <a class="yt-timestamp" data-t="08:47">[00:08:47]</a>.
*   **Emit Interval:** (Optional) The interval in seconds for status emissions from the function <a class="yt-timestamp" data-t="08:55">[00:08:55]</a>.

## Secure Deployment of N8N AI Agents

For [[configuring_ai_agents_for_cloud_deployment | configuring AI agents for cloud deployment]] and ensuring their security, especially when N8N is hosted in the cloud (e.g., Digital Ocean), it's crucial to protect the webhook endpoints <a class="yt-timestamp" data-t="12:39">[00:12:39]</a>. If N8N is running locally (e.g., via the Local AI package), this security might be less critical as external access is prevented <a class="yt-timestamp" data-t="12:31">[00:12:31]</a>. However, for cloud deployments, protecting endpoints prevents unauthorized calls that could incur significant LLM credits <a class="yt-timestamp" data-t="13:00">[00:13:00]</a>.

### Implementing Header Authentication

Instead of a chat trigger, N8N [[building_ai_agents | AI agents]] meant for Open Web UI integration use a Webhook trigger to provide a public URL <a class="yt-timestamp" data-t="11:47">[00:11:47]</a>. To secure this endpoint:

1.  **Set Authentication Type:** In the Webhook trigger settings, select "Header Authentication" <a class="yt-timestamp" data-t="12:50">[00:12:50]</a>.
2.  **Create Custom Credentials:**
    *   Set the credential name to `Authorization` <a class="yt-timestamp" data-t="13:13">[00:13:13]</a>.
    *   Set the value to `Bearer <your_custom_token>` (e.g., `Bearer testauth`). The `Bearer` prefix with a space is mandatory <a class="yt-timestamp" data-t="13:20">[00:13:20]</a>.
3.  **Configure Open Web UI:** In Open Web UI's function settings, paste *only* your custom token (e.g., `testauth`) into the "Bearer Token" field. The function automatically prefixes it with `Bearer ` <a class="yt-timestamp" data-t="13:41">[00:13:41]</a>.

This setup ensures that only Open Web UI, or any other authorized invoker with the correct bearer token, can call the N8N workflow <a class="yt-timestamp" data-t="13:59">[00:13:59]</a>.

### Input and Output Field Mapping

Proper mapping of input and output fields is essential for the seamless communication between Open Web UI and N8N:
*   **Input Field:** The N8N workflow expects the user's prompt in a specific field (e.g., `chat input` from the webhook body) <a class="yt-timestamp" data-t="15:13">[00:15:13]</a>. This exact field name must be entered in Open Web UI's function configuration for "Input Field" <a class="yt-timestamp" data-t="15:20">[00:15:20]</a>.
*   **Output Field:** The AI agent's response in N8N must be mapped to a specific output field (e.g., `output`) <a class="yt-timestamp" data-t="15:46">[00:15:46]</a>. This field name must match the "Output Field" in Open Web UI's function settings for Open Web UI to correctly retrieve the AI response <a class="yt-timestamp" data-t="15:57">[00:15:57]</a>.

### Considerations for AI Agent Workflow

A typical N8N [[building_ai_agents | building AI agents]] workflow for Open Web UI integration will consist of:
*   **Webhook Trigger:** As discussed for secure external access <a class="yt-timestamp" data-t="11:47">[00:11:47]</a>.
*   **LLM and Tools:** The core of your AI agent, including the LLM provider (e.g., OpenAI, Claude) and any tools (e.g., Brave API for web search) <a class="yt-timestamp" data-t="16:25">[00:16:25]</a>.
*   **Chat Memory:** A database (e.g., PostgreSQL) for maintaining conversation context <a class="yt-timestamp" data-t="16:30">[00:16:30]</a>.
*   **Conditional LLM Calls for Metadata:** Open Web UI performs additional LLM calls for the *first* message in a conversation to generate metadata like conversation titles and tags <a class="yt-timestamp" data-t="18:02">[00:18:02]</a>.
    *   These calls are identifiable by a `session ID` of `none` in the webhook payload <a class="yt-timestamp" data-t="20:00">[00:20:00]</a>.
    *   A conditional "if statement" in N8N checks for this `session ID`: if `none`, it routes the request to a separate, typically cheaper and faster LLM for metadata generation; otherwise, it routes to the primary [[understanding_ai_agents | AI agent]] <a class="yt-timestamp" data-t="20:28">[00:20:28]</a>.
    *   This feature is beneficial but incurs extra LLM credits <a class="yt-timestamp" data-t="19:10">[00:19:10]</a>. It can be disabled by removing the related nodes in the N8N workflow <a class="yt-timestamp" data-t="18:59">[00:18:59]</a>.

This integrated approach provides a robust and secure way to [[deploying_and_monitoring_ai_agents | deploy and monitor AI agents]] with an enhanced user experience.