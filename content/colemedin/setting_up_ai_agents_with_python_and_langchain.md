---
title: Setting up AI Agents with Python and LangChain
videoId: 8hAMASB-RpM
---

From: [[colemedin]] <br/> 

AI agents are large language models capable of interacting with the outside world through APIs, web scraping, code generation, and other methods <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. There are numerous ways to [[building_ai_agents_with_no_code_using_n8n_and_langchain | build AI agents]], utilizing both code and no-code solutions <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Code vs. No-Code Solutions

*   **No-Code Solutions:** Tools like Flowise and [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] simplify the creation of powerful [[setting_up_ai_agents_with_langchain_and_streamlit | AI agents]] without extensive debugging or code maintenance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Code Solutions:** [[developing_ai_agents_using_python | Coding your own AI agents]] with languages like [[developing_ai_agents_using_python | Python]] and libraries such as [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] offers maximum customization and control, which no-code tools may lack <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. For production environments, [[building_ai_agents_using_python | coding AI agents]] is often necessary when specific feature requirements arise <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Many developers begin with no-code tools and transition to code out of necessity <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Perfect Trifecta: n8n, Python, and LangChain

A powerful combination leverages the strengths of both code and no-code: using [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] for agent tools and [[developing_ai_agents_using_python | Python]] plus [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] for the [[setting_up_ai_agents_with_langchain_and_streamlit | AI agent]] itself <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This approach allows for quick and easy development of robust [[benefits_of_ai_agents_using_n8n_and_langchain | AI agents]] that can meet diverse needs <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Why this combination works:

*   **n8n for Tools:** [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] simplifies setting up credentials for various services and connecting them in workflows that can be exposed as API endpoints for [[setting_up_ai_agents_with_langchain_and_streamlit | agents]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Python + LangChain for Agent:** [[developing_ai_agents_using_python | Python]] combined with [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] enables easy [[building_ai_agents_using_python | creation of AI agents]] with any Large Language Model (LLM) using minimal code <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. These agents can then seamlessly hook into [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows and even create custom tools in [[developing_ai_agents_using_python | Python]] for functionality not natively supported by [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Building the AI Agent: Two Main Parts

The process of [[building_ai_agents_using_python | building this AI agent]] involves two primary components <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>:

1.  **n8n Workflows:** These provide the tools for interacting with services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Python and LangChain Code:** This integrates the agent with the [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Example Agent Capabilities

This example [[setting_up_ai_agents_with_langchain_and_streamlit | AI agent]] can:
*   Send messages in Slack <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Summarize conversations in Slack <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Upload files to Google Drive <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

The key takeaway is the extensibility of this setup; the sky is the limit for workflows you can create in [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] and integrate into the agent <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Part 1: n8n Workflows as Tools

[[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows serve as API endpoints that the [[setting_up_ai_agents_with_langchain_and_streamlit | AI agent]] can invoke <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Each workflow typically starts and ends with a webhook node to enable interaction from external code <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Example n8n Workflows:

*   **Summarize Slack Conversation:**
    *   Starts with a webhook to receive requests <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   Pulls Slack messages from a specified channel <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Aggregates messages into a single field <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   Passes the combined messages to an LLM (e.g., GPT-4o mini) with a prompt to summarize <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   Responds to the webhook with the generated summary <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Post Message to Slack:**
    *   Starts and ends with a webhook <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   Accepts the message text as an argument in the payload of the webhook call <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   Sends the message to a hardcoded Slack channel (can be made dynamic) <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   Responds to the webhook with the result of sending the message <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   **! A Golden Nugget for Slack Credentials in n8n:** When setting up Slack credentials, navigate to "OAuth & Permissions" instead of "Add Features and Functionality" and "Permissions" in api.slack.com <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Required user token scopes (e.g., for reading messages) are found under "User Token Scopes" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Create File in Google Drive (Google Doc):**
    *   Starts and ends with a webhook <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   Accepts file name and text content as parameters from the API call <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   Uploads to a hardcoded Google Drive folder <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   Crucially, uses the "Convert to a Google Document" toggle in extra options to ensure the text is formatted as a Google Doc, not a `.txt` file <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

## Part 2: Coding the AI Agent with Python and LangChain

This section focuses on [[building_ai_agents_using_python | building the AI agent]] and integrating with the [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The code is available in a GitHub repository <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Environment Setup

*   **`requirements.txt`**: Specifies [[developing_ai_agents_using_python | Python]] packages and their versions for consistent environment setup <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **`.env.example`**: A template for environment variables, including API keys (Anthropic, OpenAI), [[deploying_an_ai_agent_using_langserve | n8n]] production webhook URLs, and [[deploying_an_ai_agent_using_langserve | n8n]] Bearer tokens for authorization <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This file should be renamed to `.env` and filled with personal credentials <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### Defining Agent Tools

Tools are defined in a utility [[developing_ai_agents_using_python | Python]] script. Key components include:

*   **Importing Packages:** Includes `dotenv` for environment variables and `Tool` from [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] for defining callable tools <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Loading Environment Variables:** Retrieves necessary [[deploying_an_ai_agent_using_langserve | n8n]] URLs and the Bearer token <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **`invoke_n8n_webhook` Helper Function:** This function simplifies making API requests to [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
    *   Accepts parameters: `method` (GET/POST), `url` (n8n workflow URL), `function_name` (how the AI identifies the tool), and an optional `payload` <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Includes the Bearer token in the authorization header <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
    *   Handles both GET and POST requests <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
    *   Raises for status on success and returns the API response <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
    *   Catches errors and returns an error message to the agent for self-correction <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

#### Example Tool Definitions using `tool` Decorator:

The `@tool` decorator from [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] converts a [[developing_ai_agents_using_python | Python]] function into a tool for the LLM <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. Docstrings within these functions are crucial as the LLM uses them to understand when and how to use each tool, including descriptions, example calls, arguments, and expected return values <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

*   **`summarize_slack_conversation()`**:
    *   A simple, five-line function that calls `invoke_n8n_webhook` with a GET request to the Slack summary URL <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **`send_slack_message(message_text)`**:
    *   A function that calls `invoke_n8n_webhook` with a POST request, including `message_text` in the payload <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **`create_google_doc(file_name, file_text)`**:
    *   Calls `invoke_n8n_webhook` with a POST request, providing `file_name` and `file_text` <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

This setup significantly reduces code complexity in [[developing_ai_agents_using_python | Python]] by offloading most of the action logic to [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflows <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

### Streamlit UI and LLM Interaction

The agent's frontend is built using Streamlit, allowing browser-based interaction <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

*   **Tool Mapping:** A dictionary maps tool function names to their actual instances <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **System Message:** Defines initial context to fine-tune LLM responses, including formatting guidelines (e.g., for Google Docs links) <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **`get_llm_response_content` Helper Function:** Handles the slight differences in response formats between Anthropic and OpenAI models, normalizing output for consistent processing <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **`prompt_ai` Function:**
    *   Initializes the chatbot instance (OpenAI or Anthropic based on the model) <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   Uses a [[building_ai_agent_workflows_with_langgraph | LangGraph]] function to bind the defined tools to the chatbot <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
    *   Streams the LLM's output, showing responses in a typewriter format <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   **Tool Calls:** After receiving a full response, it checks for tool calls <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
        *   If tool calls are present, it logs them and loops through each one, invoking the corresponding [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflow via the `invoke_n8n_webhook` helper <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
        *   The result of each tool call is added as a "tool message" to the conversation history, giving the AI context on the outcome <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
        *   Recursively calls `prompt_ai` to get a new response from the LLM based on the tool call results <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Main Function (`main()`):**
    *   Sets up the Streamlit UI title <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
    *   Manages message history and redisplays it on UI refresh <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.
    *   Handles user input, adds it to the message state, prompts the AI, streams the response, and updates the internal message state <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

## Demonstration

To run the [[setting_up_ai_agents_with_langchain_and_streamlit | AI agent]] with Streamlit, navigate to the script directory and execute `streamlit run n8n_langchain_agent.py` <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

### Example Interaction

The agent demonstrates its capabilities through a series of commands:

1.  **Summarize Slack Conversation:** The user asks the agent to summarize a Slack conversation <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. The agent invokes the [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflow, fetches the summary, and displays it <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. Debug messages in the terminal show the tool invocation and the response from the [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflow <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
2.  **Research and Create Google Doc:** The user then asks the agent to research pros and cons of certain technologies and create a Google Doc with its findings <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. The agent generates the research and then calls the [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflow to create a Google Doc. It automatically titles the document (e.g., "Text Stack Research") and provides a direct link to the newly created document <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
3.  **Send Slack Message:** Finally, the user instructs the agent to send the Google Doc link to Slack, along with a message <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. The agent uses the relevant [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]] workflow to send the message to the specified Slack channel, confirming successful delivery <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

This demonstration highlights how the combination of [[building_ai_agents_with_no_code_using_n8n_and_langchain | n8n]], [[developing_ai_agents_using_python | Python]], and [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] enables complex interactions with external services without direct manual intervention in those platforms <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. This stack facilitates the creation of powerful and controllable [[setting_up_ai_agents_with_langchain_and_streamlit | AI agents]] with ease <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.