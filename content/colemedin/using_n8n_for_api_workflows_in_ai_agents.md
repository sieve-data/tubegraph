---
title: Using n8n for API workflows in AI Agents
videoId: 8hAMASB-RpM
---

From: [[colemedin]] <br/> 

AI is fundamentally transforming the current decade, largely due to the emergence of [[building_ai_agents_with_n8n | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These agents are large language models capable of interacting with the external world via APIs, web scraping, and code generation, among other methods <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While there are numerous ways to build [[building_ai_agents_with_n8n | AI agents]] using both code and no-code solutions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, a "perfect trifecta" combines the strengths of both approaches <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## The Perfect Trifecta for AI Agent Development

Traditional no-code solutions, such as Flowise and [[N8N in creating AI agents | n8n]], offer ease of development for powerful [[building_ai_agents_with_n8n | AI agents]] without extensive debugging or code maintenance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Conversely, coding [[building_ai_agents_with_n8n | AI agents]] with languages like Python and libraries such as LangChain provides unparalleled customization and control <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Often, no-code tools may lack the feature richness required for specific production needs, leading developers to transition from no-code to code-based solutions <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The secret to combining the best of both worlds lies in using [[N8N in creating AI agents | n8n]] for agent tools and Python with LangChain for the [[building_ai_agents_with_n8n | AI agent]] itself <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This combination leverages the strengths of both code and no-code <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:
*   **[[N8N in creating AI agents | n8n]]**: Simplifies credential setup and the creation of workflows that can be exposed as API endpoints for agents <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Python + LangChain**: Enables easy creation of [[building_ai_agents_with_n8n | AI agents]] with minimal code, allowing integration with [[N8N in creating AI agents | n8n]] workflows in just a few lines of code and the ability to create custom Python tools for functionalities not supported by [[N8N in creating AI agents | n8n]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Building the AI Agent: Two Main Parts

Building an [[building_ai_agents_with_n8n | AI agent]] using this combined approach involves two primary stages <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>:
1.  **[[creating_custom_ai_workflows_with_n8n | n8n Workflows]]**: These provide the necessary tools for the agent to interact with various services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Python + LangChain Coding**: This involves developing the agent's logic and integrating it with the [[N8N in creating AI agents | n8n]] workflows <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

The example [[building_ai_agents_with_n8n | AI agent]] created can perform the following actions:
*   Send messages in Slack <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Summarize conversations in Slack <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Upload files to Google Drive <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

This setup is highly extensible, with the potential to integrate any workflow created in [[N8N in creating AI agents | n8n]] into the agent <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## [[creating_custom_ai_workflows_with_n8n | n8n Workflows]] as Agent Tools

The [[N8N in creating AI agents | n8n]] workflows serve as external tools that the [[building_ai_agents_with_n8n | AI agent]] can invoke via API endpoints. Each workflow typically starts and ends with a webhook, enabling the Python code to trigger and receive responses from the workflow <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Summarize Slack Conversation Workflow
This workflow is designed to summarize a Slack conversation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
1.  It begins with a webhook to receive the invocation from the Python code <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
2.  It pulls Slack messages from a specified channel <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
3.  Messages are aggregated into a single field <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
4.  This combined text is passed into a large language model (e.g., GPT-4o mini) with a prompt to summarize the conversation <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
5.  The summary from the LLM is then returned to the webhook, which the Python agent can then utilize <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Post Message to Slack Workflow
This simpler workflow is for sending a message to Slack <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
1.  It uses a webhook to receive the message text from the Python code <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
2.  The workflow includes a Slack node configured to send the dynamically referenced message text to a hardcoded channel <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
3.  The result of sending the message is returned via the webhook <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

> [!NOTE] Slack Credentials in [[N8N in creating AI agents | n8n]]
> Setting up Slack credentials in [[N8N in creating AI agents | n8n]] requires navigating to `oAuth & Permissions` within `api.slack.com` to find the redirect URL and set user token scopes. Essential scopes for reading messages include `channels:history` and `groups:history` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Create File in Google Drive Workflow
This workflow is for creating a Google Doc <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
1.  It receives parameters for the file name and content text via a webhook <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
2.  A Google Drive node creates the file in a specified folder (e.g., "meeting notes folder") <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
3.  Crucially, the "Convert to Google Document" option is enabled in extra options to ensure the text is formatted as a Google Doc, not a raw `.txt` file <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
4.  The workflow's outcome is returned via the webhook <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

The simplicity of setting up these workflows in [[N8N in creating AI agents | n8n]] for various actions highlights how easily new tools can be integrated into a Python and LangChain agent <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Coding the AI Agent with Python and LangChain

The Python portion of the agent manages interaction with the LLM and the invocation of [[N8N in creating AI agents | n8n]] workflows. The code is available in a GitHub repository <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Environment Setup
The project includes a `requirements.txt` for Python package versions and an `.env.example` file for credentials. This includes API keys for LLMs (Anthropic or OpenAI), production [[N8N in creating AI agents | n8n]] webhook URLs, and a Bearer token for [[N8N in creating AI agents | n8n]] webhook authorization <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### `invoke_n8n_webhook` Helper Function
This helper function is central to simplifying interactions with [[N8N in creating AI agents | n8n]] workflows <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. It wraps API requests to [[N8N in creating AI agents | n8n]] endpoints, handling:
*   **Parameters**: `method` (GET/POST), `url` (the [[N8N in creating AI agents | n8n]] workflow URL), `function_name` (for AI reasoning), and optional `payload` (e.g., message text) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Headers**: Includes the Bearer token for authorization <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Request Handling**: Supports both GET and POST requests <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Error Handling**: Catches any API errors and returns an error message to the agent, allowing it to self-correct <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

This function significantly streamlines the creation of new tools, as each tool can leverage this wrapper <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Defining Agent Tools
Using LangChain's `@tool` decorator, Python functions are transformed into callable tools for the [[building_ai_agents_with_n8n | AI agent]] <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Docstrings provide descriptions, example calls, arguments, and return values, allowing the LLM to understand when and how to use each tool <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

*   **`summarize_slack_conversation()`**: A GET request to the [[N8N in creating AI agents | n8n]] summary workflow, returning the conversation summary <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   **`send_slack_message(message_text)`**: A POST request to the [[N8N in creating AI agents | n8n]] message workflow, with `message_text` as the payload <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **`create_google_doc(file_name, text)`**: A POST request to the [[N8N in creating AI agents | n8n]] Google Drive workflow, with `file_name` and `text` as parameters <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

The Python code for each tool is minimal (around five lines) because [[N8N in creating AI agents | n8n]] handles the underlying complexity of interacting with external services <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This provides both simplicity and flexibility, allowing custom code for functionalities [[N8N in creating AI agents | n8n]] might not support <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Interacting with the LLM and Streamlit UI
The main Python script handles the user interface (using Streamlit) and the logic for interacting with the LLM.

*   **Model Setup**: Configures the chatbot instance based on whether an Anthropic or OpenAI model is chosen, ensuring compatibility despite their slightly different response formats <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **System Message**: Defines initial context for the LLM, guiding its responses (e.g., how to format links) <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **`prompt_ai` Function**:
    *   Binds all defined tools to the chatbot using LangChain's `bind_tools` function <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
    *   Streams the LLM's output for a "typewriter" effect in the UI <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   **Tool Call Handling**: After the LLM generates a response, it checks for any tool calls. If tools are invoked, the agent adds a message to the conversation history, loops through each tool call to execute it, and then adds the tool's result as a "tool message" to the conversation, providing context for the LLM to reason about the output <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. The `prompt_ai` function then recursively calls itself to get a new response from the LLM, which might involve further tool calls or a final user-facing response <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Streamlit UI**: Sets up the web interface, including a title, initial system messages, and a chat input field. User prompts are added to the conversation history, and the LLM's streamed responses are displayed <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.

## Demonstration

To run the [[building_ai_agents_with_n8n | AI agent]], navigate to the script directory and execute `streamlit run n8n_langchain_agent.py` <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

The demonstration showcases the agent's capabilities:
1.  **Summarize Slack Conversation**: The user asks the agent to summarize a hardcoded Slack channel. The agent calls the [[N8N in creating AI agents | n8n]] workflow, retrieves the summary, and displays it in the UI <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Debug messages in the terminal show the tool invocation and the response received from the [[N8N in creating AI agents | n8n]] workflow <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
2.  **Create Google Doc**: The user requests research on the pros and cons of a tech stack and asks the agent to create a Google Doc with the findings <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. The agent invokes the [[N8N in creating AI agents | n8n]] Google Drive workflow, creates the document (e.g., "Text Stack Research" with markdown content), and provides a link to it in the chat <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
3.  **Send Slack Message**: Finally, the user instructs the agent to send the Google Doc link to Slack, informing them about the research <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. The agent triggers the [[N8N in creating AI agents | n8n]] Slack message workflow, successfully sending the message with the link to the specified channel <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

This demonstration illustrates how the agent seamlessly interacts with external services (Slack, Google Drive) without direct user intervention, leveraging [[N8N in creating AI agents | n8n]] for all external API calls <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. This combination of [[N8N in creating AI agents | n8n]], Python, and LangChain provides a convenient and powerful framework for building controllable [[building_ai_agents_with_n8n | AI agents]] <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.