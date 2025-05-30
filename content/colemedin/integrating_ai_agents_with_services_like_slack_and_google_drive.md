---
title: Integrating AI Agents with services like Slack and Google Drive
videoId: 8hAMASB-RpM
---

From: [[colemedin]] <br/> 

AI agents, defined as large language models (LLMs) capable of interacting with the outside world through APIs, web scraping, and code generation, are a significant part of the current technological revolution <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These agents can be built using various methods, including no-code solutions and traditional coding <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Approach to Building AI Agents

There are two primary approaches to building AI agents:
*   **No-code Solutions**: Tools like Flowise and n8n simplify the creation of powerful AI agents without extensive debugging or code maintenance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. However, they may lack the feature richness required for highly specific production requirements <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Coding Solutions**: Using languages like Python and libraries such as LangChain offers complete customization and control, often necessary for production environments <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

A "perfect trifecta" approach combines both code and no-code to create powerful and flexible AI agents <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This method uses n8n for creating agent tools and Python with LangChain for the AI agent itself <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### The n8n + Python/LangChain Combination
This combination leverages the strengths of both approaches:
*   **n8n**: Simplifies setting up credentials for various services and connecting them into workflows that can be exposed as API endpoints for agents <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Python + LangChain**: Allows for easy creation of AI agents with any LLM, using minimal lines of code, and enabling seamless integration with n8n workflows <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This also provides the flexibility to create custom tools in Python for functionalities not available in n8n <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Example Integrations with AI Agents

A practical example of an AI agent built with this stack can perform the following actions:
*   Send messages in [[capabilities_of_ai_in_slack_chat_platforms | Slack]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Summarize conversations in [[implementing_ai_personal_assistants_in_slack | Slack]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Upload files to [[using_google_drive_as_a_knowledge_base_for_ai_agents | Google Drive]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

The extensibility of this setup means virtually any workflow created in n8n can be integrated into the agent <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### n8n Workflows for Tooling

n8n workflows serve as the tools that enable the AI agent to interact with external services. These workflows are exposed as API endpoints that the Python/LangChain agent invokes <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

1.  **Summarize Slack Conversation**:
    *   Starts with a webhook to be invoked by Python code <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   Pulls Slack messages from a specified channel <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Aggregates messages into a single field and passes them to an LLM (e.g., GPT-4o mini) with a prompt to summarize <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   The LLM's summary is then returned to the webhook, accessible by the Python agent <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

2.  **Post Message to Slack**:
    *   Also begins and ends with a webhook, invoked by Python code to send a message <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   A function in the Python code accepts the message text as an argument, which is then sent as part of the payload to the n8n webhook <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
    *   Slack credentials for n8n can be configured via `api.slack.com` under "OAuth & Permissions," where redirect URLs and necessary user token scopes (e.g., for reading and sending messages) are set <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

3.  **Create File in Google Drive**:
    *   A simple workflow that uses a webhook to receive parameters for file name and text content from the API call <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   Hardcodes the target folder (e.g., "meeting notes") <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   Includes an option to convert the uploaded text into a Google Document instead of a raw `.txt` file <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   Responds to the webhook with the result of the file creation <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Python and LangChain Implementation

The Python component utilizes LangChain to build the AI agent and integrate with the n8n workflows.
*   **Environment Setup**: Requires `requirements.txt` for Python packages and a `.env` file for credentials like API keys (Anthropic, OpenAI), n8n webhook URLs, and Bearer tokens for authorization <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **Tool Definition**:
    *   The `tool` decorator from LangChain is used to mark Python functions as tools for the agent <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   Each tool function includes a docstring that describes its purpose, example calls, arguments, and expected returns, which helps the LLM understand when and how to use it <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
    *   A helper function `invoke_n8n_webhook` abstracts the API requests to n8n, handling GET/POST methods, URLs, headers (including the Bearer token), and payloads <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This simplifies tool creation, reducing each tool to just a few lines of code <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   **AI Prompting and Tool Invocation**:
    *   A `prompt_ai` function initializes the chatbot (supporting Anthropic or OpenAI models) <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
    *   Tools are "bound in" using LangChain's functionality <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
    *   The output is streamed to provide a "typewriter" effect in the UI <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   After streaming, the agent checks for tool calls. If tool calls are detected, they are executed, and the results are added back into the conversation history as "tool messages" to provide context for the AI's subsequent reasoning <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. The `prompt_ai` function is then recursively called for the LLM to continue reasoning <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Frontend**: Streamlit is used to create a simple web UI for interacting with the agent <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

## Live Demonstration

A live demo showcases the integrated agent's capabilities:
*   The agent summarizes a Slack conversation about a startup's tech stack by invoking the n8n workflow for Slack summarization <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
*   The agent then conducts internal "research" (simulated by the LLM's knowledge) on the pros and cons of different tech stack options <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>.
*   Upon request, the agent creates a Google Doc containing its research findings, leveraging the n8n workflow for [[using_google_drive_as_a_knowledge_base_for_ai_agents | Google Drive]] file creation <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. The agent automatically names the document and links it <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
*   Finally, the agent sends a message to Slack, including the link to the newly created Google Doc, using the n8n workflow for [[integrating_ai_agents_with_services_like_slack | sending Slack messages]] <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

This demonstrates how the AI agent can seamlessly interact with external services like Slack and Google Drive without direct user intervention in those platforms <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The n8n + Python/LangChain stack provides a powerful yet convenient way to build controllable and robust AI agents <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.