---
title: Integrating AI Agents in n8n using Open Web UI
videoId: 6zn8vVTeFE0
---

From: [[colemedin]] <br/> 

This article details how to enhance the user interface (UI) for [[building_ai_agents_with_n8n | AI agents]] built in [[n8n_in_creating_ai_agents | n8n]] by integrating them with [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]]. This integration allows for a more polished, ChatGPT-like interface, offering features such as conversation history and formatted markdown output, which are not readily available with [[n8n_in_creating_ai_agents | n8n]]'s default chat trigger UI <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Limitations of Default [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI Agent]] UI

When working with an [[building_ai_agents_with_n8n | AI agent]] in an [[n8n_in_creating_ai_agents | n8n]] workflow, the default chat trigger provides a convenient chat button within the workflow builder <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. However, this is very limiting <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>:
*   It doesn't look aesthetically pleasing <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   You cannot view past conversations to continue them <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   Making the chat publicly available deploys a web page that is "very ugly" and lacks customization options <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

While [[n8n_in_creating_ai_agents | n8n]] is praised as a top no-code tool for [[ai_automation_with_n8n | automations]] and [[building_ai_agents_with_n8n | AI agents]], its UI for these agents could be significantly improved <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Introducing [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]]

[[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] is an open-source platform that provides a full, self-hostable, ChatGPT-like interface for interacting with [[building_ai_agents_with_n8n | AI agents]] <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. It enables features such as <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>:
*   Beautiful UI with formatted markdown and highlighted text <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Voice interaction with [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI agents]] <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   Conversation history, allowing users to revisit and continue past discussions <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Ability to run entirely offline on your computer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Connects to [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI agents]] under the hood, even though it appears like a normal [[LLM]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] Installation

[[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] can be installed via several methods:

### Python Installation
If Python is installed on your machine, you can install [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] using `pip` and then run the `open-webui serve` command to start the application <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It can then be accessed via `localhost:8080` in your browser <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Docker Installation
Installation with Docker is straightforward, typically requiring a single command <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Various command options are available depending on your machine and configuration, with a default option suitable for connecting directly to an [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | agent]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Local [[LLM]] Package
For the most convenient setup, the Local [[LLM]] Package bundles services like a database, self-hosted [[n8n_in_creating_ai_agents | n8n]], [[LLM | Olama]], and [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This package allows you to run everything on your own computer, entirely offline <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

After installation, access the [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] interface in your browser (typically `localhost:3000` or `localhost:8080`) and create a local admin account <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Connecting [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] to [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI Agents]]

The connection between [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] and [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI agents]] is established through a custom function in [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Importing the Custom Function
The custom function, an [[integration_capabilities_of_n8n_with_ai_libraries | n8n]] integration, can be imported in two ways <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:
1.  **Direct Import**: Go to the provided URL for the function and click the "Get" button. Enter your [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] URL (e.g., `localhost:3000`), then click "Import to Web UI" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
2.  **Manual Import**: Copy the function code from the page <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. In [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]], navigate to the admin panel, select the "Functions" tab, click the plus icon to add a new function, paste the code, and add a function ID and description before saving <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

Once imported, this function, often called "[[n8n_in_creating_ai_agents | N8N]] [[building_ai_agents_with_n8n | Agent]] Connector," becomes available as an [[LLM]] option in your [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] workspace <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Configuring the Function
Before use, the function requires configuration in its settings <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>:
*   **[[n8n_in_creating_ai_agents | N8N]] URL**: This is the public URL of your [[n8n_in_creating_ai_agents | n8n]] workflow's webhook trigger <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Copy the "production URL" from the webhook node in [[n8n_in_creating_ai_agents | n8n]] <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Bearer Token**: To secure your [[building_ai_agents_with_n8n | AI agent]], protect the webhook endpoint with header authentication <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. In [[n8n_in_creating_ai_agents | n8n]], set header authentication with the name `Authorization` and a value of `Bearer YOUR_CUSTOM_TOKEN` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. In [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]], only input `YOUR_CUSTOM_TOKEN` (the function automatically prefixes with `Bearer `) <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This is crucial if [[n8n_in_creating_ai_agents | n8n]] is cloud-hosted; it's less critical if running locally <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Input Field and Output Field**: These define the expected field names for input to and output from your [[n8n_in_creating_ai_agents | n8n]] workflow <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. For example, if your [[n8n_in_creating_ai_agents | n8n]] webhook expects `chatInput` and outputs to `output`, these values must match <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Emit Interval**: This setting, usually left as default, determines the interval in seconds between status updates from the function during a chat <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Building [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI Agents]] for [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] [[integration_capabilities_of_n8n_with_ai_libraries | Integration]]

To build an [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI agent]] that seamlessly integrates with [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]], consider the following:

### Webhook Trigger Instead of Chat Trigger
Replace the default chat trigger with a webhook trigger in your [[n8n_in_creating_ai_agents | n8n]] workflow <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. This provides a public URL for communication with the workflow and [[building_ai_agents_with_n8n | AI agent]] <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Ensure the workflow is active and copy the production URL <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

### Protecting the Endpoint
If your [[n8n_in_creating_ai_agents | n8n]] instance is hosted in the cloud (e.g., Digital Ocean), it is essential to protect your webhook endpoint with header authentication to prevent unauthorized calls that could incur [[LLM]] costs <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Create custom credentials with an `Authorization` header and a `Bearer` token <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. If running [[n8n_in_creating_ai_agents | n8n]] locally, this security step is generally not required <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

### Input and Output Mapping
The input field name in your [[n8n_in_creating_ai_agents | n8n]] webhook (e.g., `chatInput` for the user message) must precisely match the "Input Field" setting in your [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] function <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Similarly, the name of the output field from your [[n8n_in_creating_ai_agents | n8n]] workflow (e.g., `output` for the [[LLM]] response) must match the "Output Field" setting in [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. This ensures [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] correctly locates the [[building_ai_agents_with_n8n | AI agent]]'s response.

### Handling [[LLM]] Calls for Metadata Generation
[[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] makes multiple [[LLM]] calls for the *first message* in a conversation to generate metadata like the conversation title and tags <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Purpose**: These calls are distinct from the primary [[building_ai_agents_with_n8n | AI agent]] interaction and are used to create descriptive titles <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a> and relevant tags (e.g., "education," "technology") <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a> for the conversation <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Workflow Logic**: In the provided [[n8n_in_creating_ai_agents | n8n]] template, an `if` statement checks the `session ID` from the webhook <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. If the `session ID` is `none`, it indicates a metadata generation call, and the workflow directs to a simpler, cheaper [[LLM]] <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. Otherwise, for actual primary agent communication, the `session ID` is defined, and the request goes to the main [[building_ai_agents_with_n8n | AI agent]] <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   **Cost Management**: You can use a fast and cheap [[LLM]] (e.g., GPT-4 mini) for metadata generation and a more powerful, potentially expensive [[LLM]] (e.g., Claude 3.7 Sonnet) for the primary [[building_ai_agents_with_n8n | agent]] <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Alternatively, if metadata generation is not desired, these nodes can be removed from the workflow <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

## Conclusion

By following these steps, you can significantly upgrade the user experience of your [[n8n_in_creating_ai_agents | n8n]] [[building_ai_agents_with_n8n | AI agents]] by integrating them with [[running_ai_locally_with_n8n_and_open_webui | Open Web UI]] <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. This provides a more professional, feature-rich interface comparable to commercial [[LLM]] platforms, without needing to code a custom application <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Downloadable resources, including an [[n8n_in_creating_ai_agents | n8n]] agent template, are often provided to help users get started quickly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.