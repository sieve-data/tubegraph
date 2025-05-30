---
title: Using Open WebUI features like voice chat and functions
videoId: E2GIZrsDvuM
---

From: [[colemedin]] <br/> 
[[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] is an open-source, ChatGPT-like interface primarily used for interacting with Large Language Models (LLMs) running with Ollama <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. It offers key features like functions and pipelines that enable the implementation of custom functionality <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This allows users to chat with their own [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]] and API endpoints <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>, even supporting [[ai_voice_systems_and_integration | voice]] communication with [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] agents <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

This article details how [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] has been integrated into the [[running_ai_locally_with_n8n_and_open_webui | local AI starter kit]] to facilitate chatting with [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] workflows directly <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

## Accessing Open WebUI
To access your [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] instance, navigate to `Local Host Port 3000` <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Upon first access, you'll be prompted to create a local account, which does not require an internet connection <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

### Correcting Ollama Connection Issues
If [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] pulls Ollama models from your local computer instead of the containerized Ollama instance within the [[running_ai_locally_with_n8n_and_open_webui | local AI starter kit]], you can resolve this by:
1.  Clicking on your name in the bottom left <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
2.  Going to the "Admin Panel" <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
3.  Clicking on "Settings" <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.
4.  Selecting "Connections" <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
5.  Changing the URL for your Ollama API to `ollama` from `localhost` or `host.docker.internal` <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
6.  Clicking "Save" and reloading the page <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This ensures that the model dropdown shows the models pulled for Ollama in the container <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## Integrating n8n with Open WebUI Functions
Integration with [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] is achieved using the "Functions" feature in [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This allows custom functionality for [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] to interact with custom agents and API endpoints, including an [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] webhook <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

### The n8n Pipe Function
A specific "n8n pipe" function has been developed and published on the [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] functions page <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>, <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This function is a Python script tailored for [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] integrations <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>, <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

#### Valves (Parameters)
The `n8n pipe` function includes "valves" (parameters) that users can customize without editing the code directly <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>, <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>:
*   **n8n URL**: The specific [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] webhook URL <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. For container communication, replace `Local Host` with `n8n` in the URL (e.g., `http://n8n:5678/webhook/invoke-n8n-agent`) <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Bearer Token**: Optional for authentication if using a bearer token <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **Input Field**: Defines the name of the property in the JSON payload that contains the user's prompt (e.g., `chatInput`) <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **JSON Response Property**: The name of the property in the JSON response from the webhook that contains the LLM's output <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

#### Function Logic
The Python script within the function performs the following:
*   **Status Messages**: Emits status messages to the [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] output to show updates during response generation <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   **Primary Pipe Function**:
    *   Takes the list of messages (conversation history) <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
    *   Extracts the last question from the user <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
    *   Makes an HTTP POST request to the specified [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] URL <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
    *   Passes an optional bearer token <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
    *   Includes a payload with a session ID (a combination of user ID and the first part of the first prompt due to current limitations in retrieving the chat ID from [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]]) and the user's last message <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>, <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
    *   Extracts the LLM's output from the response using the defined response field <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
    *   Appends the output to the conversation and returns it after error handling <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

#### Enabling the Function
After obtaining the function code (either by copying/pasting or using the "Get" button from the [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] site), ensure it is enabled in your [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] instance <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>, <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. The `n8n pipe` will then appear alongside other Ollama models in the "Select Model" dropdown <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### n8n Workflow Configuration for Open WebUI
The [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] workflow is set up to integrate with [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] via a webhook trigger <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.

Key configurations for the `Webhook` node:
*   **Method**: `POST` <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Path**: A custom path like `invoke-n8n-agent` <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>. This generates a URL that [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] will hit <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   **Authentication**: Can be set to `None` if running locally, or configured for bearer token authentication if desired <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
*   **Respond**: Crucially, change from "Immediately" to "Using Respond to Webhook node" <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>. This ensures the workflow processes the agent's response before sending it back to [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.

The webhook request body contains a `session ID` for chat history tracking and a `chatInput` field for the LLM's prompt <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. The `AI Agent` node uses `chatInput` as its prompt <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. The `Respond to Webhook` node then sends the agent's output back to [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.

### Customizing for Any Agent
The design of the `n8n pipe` allows for high customizability. Users can modify the Python code to make POST requests to any API endpoint hosting agents (e.g., LangServe, swarm agents, LlamaIndex), enabling interaction with virtually any type of agent through [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>, <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Open WebUI Pipelines
Similar to functions, [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] also offers a "Pipelines" feature <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. Pipelines allow for installing more external dependencies, such as LangChain or LlamaIndex, directly within the [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] code <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Voice Chat with n8n AI Agents
A significant feature of [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] is its ability to support [[ai_voice_systems_and_integration | voice]] chat with [[using_no_code_and_low_code_tools_like_n8n_and_voiceflow | n8n]] [[integrating_ai_agents_in_n8n_using_open_web_ui | AI agents]] <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. This is enabled by clicking the "call button" on the right-hand side and allowing microphone access in the browser <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. While the current [[voice_ai_advancements_and_applications | voice]] is somewhat robotic, the [[integrating_open_webui_into_an_ai_starter_kit | Open WebUI]] team is actively working on improvements like custom voices <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.