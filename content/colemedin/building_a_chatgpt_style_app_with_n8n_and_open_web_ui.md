---
title: Building a ChatGPT Style App with n8n and Open Web UI
videoId: 6zn8vVTeFE0
---

From: [[colemedin]] <br/> 

This article details how to elevate your [[ai_automation_with_n8n | n8n]] AI agents by integrating them with Open Web UI, an open-source platform that provides a user-friendly, ChatGPT-like interface. This approach overcomes the limitations of [[overview_of_n8n_as_a_workflow_automation_tool | n8n]]'s native chat UI, offering a more scalable, configurable, and robust solution for [[building_ai_agents_with_n8n | building AI agents]].

## Limitations of n8n's Native UI <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

When [[building_ai_agents_with_n8n | building AI agents]] in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]], the typical setup involves a chat trigger at the start of the workflow <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While convenient for testing directly within the workflow builder via a chat button <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, this built-in interface has significant limitations:

*   **Poor Aesthetics**: It doesn't look visually appealing <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **No Conversation History**: Users cannot view or continue past conversations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Limited Customization**: The publicly available chat page is very basic and offers little room for customization <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

While [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] is praised as an excellent no-code tool for building automations and AI agents <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, its UI for agents can be significantly improved <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## The Solution: Open Web UI <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

Open Web UI is an open-source platform that provides a full, ChatGPT-like interface for interacting with [[ai_automation_with_n8n | n8n]] agents <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. It offers:

*   **Beautiful UI**: A highly aesthetic and functional interface <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Advanced Features**: Includes voice interaction with [[ai_automation_with_n8n | n8n]] agents <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Conversation History**: Ability to view and continue past conversations <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Rich Formatting**: Supports markdown for formatted responses, including highlighted text <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **No Code Required**: Achieved without building a custom application or coding <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

Under the hood, Open Web UI connects to the AI agent hosted in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Setting Up Open Web UI <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

Open Web UI is a self-hostable interface for chatting with LLMs and AI agents <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. It can even run entirely offline on your computer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Installation Options <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>

1.  **Python**:
    *   **Prerequisite**: Python installed on your machine <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Installation**: `pip install open-webui` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   **Run**: `open-webui serve` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   **Access**: `localhost:8080` in your browser <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  **Docker**:
    *   **Installation**: Single command (pick the top one if unsure, as it's a good default when not directly using Olama or Open Web UI) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **[[running_ai_locally_with_n8n_and_open_webui | Local AI Package]]**:
    *   This package bundles self-hosted [[overview_of_n8n_as_a_workflow_automation_tool | n8n]], Olama, and Open Web UI together <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. It's often the most convenient way to get everything running from scratch <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

Once installed, access Open Web UI via `localhost:3000` or `localhost:8080` and create a local admin account <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## [[integrating_ai_agents_in_n8n_using_open_web_ui | Integrating n8n Agents in n8n using Open Web UI]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>

[[integrating_ai_agents_in_n8n_using_open_web_ui | Integrating AI Agents in n8n using Open Web UI]] is achieved through a custom function within Open Web UI called "functions" <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Importing the Custom Function <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

A pre-built function is available to simplify the integration <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

1.  **Direct Import**: Go to the function's URL and click "Get". Type your Open Web UI URL (e.g., `localhost:3000`) and click "Import to Web UI" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
2.  **Manual Import**: Click "Copy" on the function page to get the Python code <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. In Open Web UI, go to the admin panel (bottom left) > Functions tab > Plus icon (top right) to add a new function. Paste the code, add a Function ID and description, then click "Save" <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

This makes the "N8N Agent Connector" function available as an LLM option in your Open Web UI workspace <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Configuring the Function <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>

The custom function requires specific values to connect to your [[ai_automation_with_n8n | n8n]] agent. These are set within the function's settings icon:

*   **N8N URL**: The public URL of your [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] agent <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Bearer Token**: For securing your agent <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Input Field**: The expected name of the input field in your [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] workflow <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Output Field**: The name of the field where your [[ai_automation_with_n8n | n8n]] agent's response is outputted <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Emit Interval**: Interval in seconds for status updates (can usually be left as default) <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

## [[prototyping_ai_agents_using_n8n | Building AI Agents with n8n]] for Open Web UI <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>

A template [[creating_powerful_ai_workflows_with_n8n | n8n workflow]] is available to simplify setting up your agent for Open Web UI integration.

### Web Hook Trigger <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>

Instead of a chat trigger, use a **Web Hook Trigger** node. This provides a public URL for communication with the workflow and the AI agent <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

1.  **Copy Production URL**: Copy the production URL from the Web Hook Trigger node <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This URL is pasted into the "N8N URL" field in Open Web UI <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
2.  **Header Authentication (Bearer Token)**:
    *   **Recommendation**: Protect your webhook endpoint with header authentication, especially if [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] is hosted in the cloud <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
    *   **Setup**: Select "Header Authentication" and create custom credentials <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
        *   **Name**: `Authorization` <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
        *   **Value**: `Bearer YOUR_CUSTOM_TOKEN` (e.g., `Bearer testauth`) <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
    *   **Open Web UI Configuration**: In Open Web UI's function settings, only paste `YOUR_CUSTOM_TOKEN` (e.g., `testauth`) into the "Bearer Token" field, as the function assumes the "Bearer " prefix <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
    *   **Local Hosting Note**: If [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] is running completely locally (e.g., via the [[running_ai_locally_with_n8n_and_open_webui | Local AI Package]]), header authentication might not be necessary, but it's good practice <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
3.  **Input and Output Fields**:
    *   These values map to the "Input Field" and "Output Field" in Open Web UI's function settings <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
    *   **Input Field**: The expected name of the field containing the user's message in the webhook body. In the template, it's `chat_input` <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. The AI agent node is configured to receive the user prompt from `chat_input` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    *   **Output Field**: The name of the field where the AI agent's response is placed at the end of the workflow. In the template, it's `output` <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. This ensures Open Web UI knows where to find the response <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

### AI Agent Node and Tools <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>

The core of your [[building_ai_agents_with_n8n | AI agent]] in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] remains standard. The template provides a simple agent with:

*   An LLM (you can choose your provider) <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.
*   Postgres for chat memory <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   A single tool (e.g., Brave API for web searching) <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   No system prompt (for simplicity in the template) <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

> [!INFO] Customization
> You can build any complex [[building_ai_agents_with_n8n | AI agent]] you want in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] with multiple tools, agents, or chains, as long as the initial Web Hook Trigger and final output mapping are correctly configured <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

### Conditional LLM Calls for Metadata Generation <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>

Open Web UI performs multiple LLM calls for the *first message* in a conversation to generate metadata like conversation titles and tags <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

*   **Purpose**:
    *   Generates an AI-driven title for the conversation <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
    *   Generates tags for the conversation (e.g., "education" and "technology") <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Workflow Logic**:
    *   The `session ID` in the webhook input differentiates metadata calls from primary agent calls <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
    *   If `session ID` is `none`, it's a metadata generation call, routing to a separate, typically cheaper and faster LLM <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
    *   If `session ID` is defined, it's a primary agent call, routing to your main [[ai_automation_with_n8n | AI agent]] <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. This `session ID` is also used for chat memory nodes (like Postgres) <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Cost Management**: You can use a very fast and cheap LLM (e.g., GPT-4 Mini) for metadata generation while using a more powerful, expensive LLM (e.g., Claude 3.7 Sonnet) for the primary agent <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. If running locally with Olama, these calls are free <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.

> [!WARNING] Optional Metadata
> If you don't want these extra AI calls for metadata generation, you can delete the nodes associated with the "metadata" path in the workflow <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>. Connect the Web Hook directly to the agent node instead <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

By following these steps, you can easily [[creating_powerful_ai_workflows_with_n8n | create powerful AI workflows]] in [[overview_of_n8n_as_a_workflow_automation_tool | n8n]] that interact seamlessly with a sophisticated ChatGPT-style interface via Open Web UI.