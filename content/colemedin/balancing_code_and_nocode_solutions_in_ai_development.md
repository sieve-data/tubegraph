---
title: Balancing code and nocode solutions in AI development
videoId: 8hAMASB-RpM
---

From: [[colemedin]] <br/> 

AI agents are large language models capable of interacting with the outside world through various means such as APIs, web scraping, and code generation <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Building these agents can be done with both code and [[role_of_no_code_tools_and_ai_coding_assistants_in_ai_development | no-code solutions]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Advantages of No-Code Solutions

[[Nocode AI Automation Platforms | No-code solutions]] like Flowise and n8n offer incredible ease in [[developing_ai_agents_without_coding | building AI agents]] without the need for debugging and maintaining extensive code <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Advantages of Code-Based Solutions

Coding AI agents, typically using languages like Python and libraries such as LangChain, provides maximum customization and control <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Often, custom code is necessary for production environments when [[transitioning_from_no_code_to_custom_code_in_ai_projects | no-code solutions]] lack sufficient features for specific requirements <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This often leads developers to start with no-code and transition to custom code out of necessity <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Perfect Trifecta: Combining Code and No-Code

A powerful approach to [[building_ai_agents_with_nocode_tools | AI agent development]] involves combining both code and [[nocode_ai_automation_platforms | no-code]] to achieve quick, easy development alongside power and adaptability <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The secret lies in using n8n for agent tools and Python with LangChain for the AI agent itself <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This combination leverages the strengths of both:
*   **n8n** simplifies setting up credentials for services and connecting them into workflows that can be exposed as API endpoints for agents <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Python + LangChain** allows for easy creation of AI agents with any LLM using minimal lines of code, and seamless integration with n8n workflows <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Custom tools can also be created in Python for functionalities not supported by n8n <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Practical Example: A Hybrid AI Agent

A demonstration agent combining n8n workflows with Python and LangChain showcases this hybrid approach <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This agent is capable of:
*   Sending messages in Slack <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
*   Summarizing conversations in Slack <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>
*   Uploading files to Google Drive <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>

The key takeaway is the extensibility of this setup; virtually any workflow created in n8n can be integrated into the agent <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### N8n Workflows as Tools

The n8n workflows serve as the tools for the AI agent <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Each workflow starts with a webhook, which provides a URL invoked by the Python code to trigger the tool <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

#### 1. Summarize Slack Conversation Tool
This workflow pulls Slack messages from a specified channel, aggregates them, and passes them to a large language model (e.g., GPT-4o mini) with a prompt to summarize the conversation <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The summary is then returned to the Python code via the webhook response <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

#### 2. Post Message to Slack Tool
This simpler workflow accepts message text as an argument via the webhook payload and sends it to a hardcoded Slack channel <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The result of sending the message is then returned <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

> [!NOTE] Slack Credentials in n8n
> When setting up Slack credentials in n8n, navigate to "OAuth & Permissions" at `api.slack.com` to find the redirect URL and set user token scopes. Essential scopes for reading messages include `channels:history` and `groups:history` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

#### 3. Create File in Google Drive Tool
This workflow takes a file name and text content as parameters via the API call <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. It creates a file in a specified Google Drive folder, with an option to convert the text to a Google Document instead of a raw `.txt` file <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. The outcome is returned via the webhook <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Python and LangChain Agent Integration

The Python component utilizes LangChain to interact with the large language model and invoke the n8n workflows as tools.

#### Accessing the Code
The code for this setup is available in a GitHub repository, including `requirements.txt` for package versions and `.env.example` for credentials (API keys, n8n webhook URLs, Bearer token for n8n authorization) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

#### Utility Python Script for Tools
A utility script defines the tools that interact with the n8n API endpoints <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Imports**: Essential packages like `dotenv` and the `tool` decorator from LangChain are imported <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Environment Variables**: Loads environment variables, including the n8n Bearer token for authorization and the production URLs for each n8n workflow <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   `invoke_n8n_webhook` **Helper Function**: This reusable function simplifies making API requests to n8n workflows. It handles `GET` and `POST` requests, includes authorization headers, and incorporates error handling <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Defining Tools with `@tool` Decorator**: LangChain's `@tool` decorator turns Python functions into tools that the LLM can use <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Each tool function includes a docstring that describes its purpose, example usage, arguments, and return values. This allows the LLM to understand when and how to invoke each tool <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
    *   `summarize_slack_conversation`: A `GET` request to the n8n summary webhook URL <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
    *   `send_slack_message`: A `POST` request to the n8n send message webhook URL, including the message text in the payload <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   `create_google_doc`: A `POST` request to the n8n Google Drive webhook URL, with file name and text in the payload <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
The simplicity of these tool definitions (often just a few lines of code) demonstrates how n8n handles most of the operational complexity <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

#### Streamlit UI and LLM Interaction
The main Python script sets up a Streamlit UI for user interaction and manages the LLM conversation <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Imports**: Includes `streamlit`, LangChain components, and the defined tools <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   `available_tool_mapping`: A dictionary mapping tool names to their corresponding functions <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **System Message**: Provides initial context to fine-tune the LLM's responses, e.g., formatting for Google Docs links <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   `get_llm_chain` Helper: A helper function to support both Anthropic and OpenAI models despite their slightly different response formats <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   `prompt_ai` Function:
    *   Initializes the chatbot model (OpenAI or Anthropic) <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
    *   Uses LangChain's `bind_tools` to integrate the available tools with the chatbot <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
    *   Streams the LLM's output for a "typewriter" effect <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   Checks for and executes tool calls: When the LLM decides to use a tool, its choice is added to the conversation history. The tool is then invoked, and its result is added back to the conversation as a "tool message" to provide context for the AI's reasoning <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
    *   Recursively calls itself to continue the conversation based on tool outputs <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Main Streamlit Function**: Sets up the UI, manages chat input, displays messages, and processes prompts <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.

### Demonstration

The AI agent is run using `streamlit run n8n_langchain_agent.py` <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. In a demonstration, the agent successfully:
1.  **Summarized a Slack conversation**: The agent called the n8n workflow to retrieve and summarize messages, displaying the summary in the UI <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Debug messages in the terminal confirmed the tool invocation and response <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.
2.  **Created a Google Doc**: Based on internal knowledge about tech stack pros and cons, the agent generated a Google Doc with its findings, linking it in the chat <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. The document, titled "Tech Stack Research," was created in Google Drive <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
3.  **Sent a Slack message**: The agent sent a Slack message containing the link to the newly created Google Doc <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>, confirming the successful use of the third n8n workflow <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.

This demonstration highlights how [[integration_of_nocode_tools_with_local_ai_agents | n8n facilitates interactions]] with external services, making the setup convenient and efficient <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.

The combination of n8n, Python, and LangChain offers an effective method for [[no_code_ai_agent_builders | building powerful and controllable AI agents]] by balancing the simplicity of no-code with the flexibility of code <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.