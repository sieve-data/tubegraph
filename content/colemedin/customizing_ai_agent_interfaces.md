---
title: Customizing AI Agent Interfaces
videoId: 6zn8vVTeFE0
---

From: [[colemedin]] <br/> 

When [[building_ai_agents | building AI agents]] within N8N workflows, the default [[creating_user_interfaces_for_ai_agents | user interface]] can be limiting <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This article explores how to enhance the [[creating_custom_frontends_for_ai_agents | frontend]] experience for your N8N [[understanding_ai_agents | AI agents]] using Open Web UI.

## Limitations of Default N8N Chat UI

The standard chat trigger in an N8N workflow provides a chat button within the workflow builder for convenience <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. However, it is very limiting <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>:
*   It lacks aesthetic appeal <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   There's no ability to view or continue past conversations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Making the chat publicly available through the chat trigger option results in an "ugly" web page with minimal customization room and no past conversation history, unlike platforms such as chatgbt.com <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Introducing Open Web UI for Enhanced AI Agent Interfaces

While N8N is considered a leading no-code tool for [[building_ai_agents | AI agents]] and automations, its UI can be significantly improved <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Open Web UI offers a solution by providing a full ChatGPT-like interface for N8N agents <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

This open-source platform allows for a self-hostable interface to interact with LLMs and [[understanding_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Key features include:
*   A beautiful and user-friendly interface <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   Voice input capabilities for N8N agents <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   Formatted markdown output, including code highlighting <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Conversation history, allowing users to continue or revisit old chats <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The ability to run entirely offline on your computer <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Installing Open Web UI

Open Web UI can be installed via several methods:

1.  **With Python**: Requires Python on your machine. Install with `pip` and run the `open-webui serve` command <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Access it in your browser at `localhost:8080` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
2.  **With Docker**: Installable with a single Docker command, with various options depending on your machine configuration <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **Local AI Package**: A convenient way to get Open Web UI and N8N up and running together <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This package includes self-hosted N8N, Olama, and Open Web UI services <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Once installed, you can access the interface in your browser, typically at `localhost:3000` or `localhost:8080`, and create a local admin account <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Integrating N8N Agents with Open Web UI

[[Connecting_AI_agents_to_frontend_applications | Connecting AI agents to frontend applications]] like Open Web UI from N8N involves setting up a custom function for integration <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Setting Up the Custom Function

The N8N integration function can be imported into Open Web UI in two ways:
1.  **Direct Import**: Go to the provided URL for the function and click the "get" button. Type your Open Web UI URL (e.g., `localhost:3000`) and click "import to web UI" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
2.  **Manual Installation**: Copy the function code, then in Open Web UI, navigate to the admin panel -> functions tab -> click the plus icon to add a new function. Paste the code, add a function ID and description, then save <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

Once installed, this custom function will appear as an available LLM option when starting a new chat in Open Web UI <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Configuring the N8N Agent Template

The N8N agent template provided for integration is a basic [[understanding_ai_agents | AI agent]] with a web search tool (Brave API) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. To integrate it with Open Web UI, specific configurations are needed:

1.  **Webhook Trigger**: Instead of a chat trigger, use a webhook trigger to get a public URL for communication <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Copy the production URL of the webhook <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
    *   Paste this URL into the "N8N URL" field in the Open Web UI function settings <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
    *   Ensure the N8N workflow is toggled to active <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

2.  **Security with Header Authentication**: To protect your public N8N webhook endpoint, especially if running N8N in the cloud, enable header authentication <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
    *   In the N8N webhook node, select "header authentication" and create custom credentials <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
    *   Set the credential name to "authorization" <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
    *   Set the value as `bearer` followed by a space and your custom token (e.g., `bearer testauth`) <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
    *   In Open Web UI, add *only* your custom token (e.g., `testauth`) to the "bearer token" field in the function settings <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
    *   If running N8N entirely locally, header authentication may not be strictly necessary <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

3.  **Input and Output Fields**:
    *   **Input Field**: This determines the name of the field expected to come into the N8N workflow <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. For example, if the user message is `chat input`, ensure the "Input Field" in Open Web UI is set to `chat input` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
    *   **Response Field**: This is the name of the field outputted at the very end of the N8N workflow containing the AI response <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. For instance, if the agent response is in an `output` field in N8N, set the "Response Field" in Open Web UI to `output` <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

4.  **Emit Interval**: This setting, usually left as default, controls the interval in seconds between status updates received from the function during chatting <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### LLM Calls for Metadata Generation

Open Web UI performs multiple LLM calls for the *first message* in a conversation to generate metadata <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>:
*   **Conversation Title**: Generates a title based on the first two messages <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Conversation Tags**: Generates relevant tags for the conversation <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.

An N8N workflow template accounts for this by including a second, simpler LLM call branch <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This branch is triggered when the `session ID` from Open Web UI is `none`, indicating a metadata generation request <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. For actual conversations, the `session ID` is defined, and the primary [[understanding_ai_agents | AI agent]] handles the request <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

> [!info] Sponsor: ZAMS
> [[building_ai_agents | Building AI agents]] for enterprise use requires scalability, configurability, robustness, and security <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. ZAMS is an enterprise platform designed to [[building_ai_agents | build AI agents]] for automating back-office work, making them effortless, secure, and powerful <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. ZAMS provides a UI layer for agents, much like web browsers made the internet accessible, to make [[understanding_ai_agents | AI agents]] functional for businesses <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. It integrates knowledge AI, process AI, and predictive AI, all built with enterprise control, governance, and security <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

By using a fast and cheap LLM for metadata generation and a more powerful one for the primary agent, the cost of these extra calls can be minimized <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. If metadata generation is not desired, these specific nodes can be removed from the N8N workflow <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

This integration allows for advanced [[advanced_architecture_for_ai_agents | architecture for AI agents]], facilitating seamless interaction between N8N and a superior [[creating_custom_frontends_for_ai_agents | custom frontend]] like Open Web UI. You can incorporate [[creating_custom_ai_agent_frameworks_with_mcp | MCP servers]], multiple tools, and even multiple agents into your N8N workflow, as long as the initial webhook setup and final output mapping are maintained <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.