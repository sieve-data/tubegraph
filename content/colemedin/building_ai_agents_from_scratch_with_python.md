---
title: Building AI agents from scratch with Python
videoId: zaNIvRllycM
---

From: [[colemedin]] <br/> 

Artificial intelligence is currently the top focus for developers <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. To fully unleash the power of AI, developers should focus on [[building_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This article outlines a step-by-step process for [[building_ai_agents | building AI agents]] from scratch using Python, starting with a basic understanding of Python <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## [[understanding_ai_agents | Understanding AI Agents]]

An [[building_ai_agents | AI agent]] is a large language model given the ability to interact with the outside world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This interaction can include drafting emails, creating tasks, or adding contacts to a CRM <a class="yt-timestamp" data=t="00:00:22">[00:00:22]</a>. Agents can be developed to work together on complex tasks or function as autonomous customer support <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up Your Development Environment

All code demonstrated in this master class will be available on GitHub <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

### Prerequisites
*   A basic understanding of Python is required <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   Familiarity with environment variables.

### Required Packages
The first step is to import all necessary packages, such as Asana and OpenAI <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Installation instructions for these packages are provided in the GitHub repository <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

### Environment Variables
Environment variables are used to store secrets and configuration data, like your OpenAI API key and Asana access token, preventing them from being directly pasted into code <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   Create a `.env` file in the same directory as your Python script <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. An example is in the GitHub repo <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
*   API keys for Asana and OpenAI can be easily obtained by searching online <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   These variables are loaded using the `dotenv` package, allowing access via `os.env` <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

### Initializing Clients
*   **OpenAI Client:** The GPT model (e.g., `gpt-4o`) is defined, potentially defaulting if an environment variable is not set <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
*   **Asana Client:** The Asana client is created using an environment variable for the access token <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. The `tasks` API is specifically instantiated since the agent will be creating tasks <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

## Core Logic for the [[building_ai_agents | AI Agent]]

### Defining Messages for the Chatbot
Interaction with GPT models in Python is managed through a list of messages <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. Each message has one of three roles <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>:
*   **System Role:** Provides background context for the AI (e.g., "You are a personal assistant who helps manage tasks in Asana" and the current date) <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
*   **User Role:** A message from the user <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
*   **Assistant Role:** The response from the AI <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

Tools are also used, which allow the GPT model to interact with the outside world <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

### Main Application Loop
The application runs in the command line, continuously asking the user for input <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. Typing "Q" breaks the loop and ends the application <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.
1.  User input is added to the messages list with a "user" role <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
2.  A `prompt_ai` function is called with the chat history (list of messages) <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
3.  The AI's response is printed to the terminal <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
4.  The AI's response is added to the messages list with an "assistant" role <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.

### The `create_asana_task` Function
This function allows the agent to add tasks to Asana <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Parameters:** Takes `task_name` (required) and `due_on` (optional, defaults to today) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   **Docstring:** A docstring is added to explain the function to the AI <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   **Due Date Logic:** If `due_on` is the default "today", it's set to the current date <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   **Data Structure:** Defines the data for Asana's API, including task name, due date, and a `project_id` to specify where the task should be added <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
*   **API Call:** Calls the Asana `tasks` API to create the task and returns the response or an error <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. The AI can parse the JSON response, even extracting a link to the created task <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

### The `get_tools` Function
This function defines the tools that the AI can use to interact with the outside world <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
*   `tools` is an array of objects, each defining a callable function for the AI <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.
*   **`description`:** Tells the AI when to use the function <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
*   **`parameters`:** Defines what arguments the AI should pass into the function, including data types and formats (e.g., date format for `due_on`) <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
*   **`required`:** Specifies which parameters are mandatory <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

The AI intelligently determines the task name and due date from the conversation, converting natural language into the required date format <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.

### The `prompt_ai` Function
This function handles the interaction with the GPT model <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.
1.  **GPT Call:** Uses `client.chat.completions.create` and passes:
    *   The defined model <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.
    *   The list of messages (full chat history) <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
    *   The tools returned by `get_tools()` <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.
2.  **Response Format:** The AI's response is an object with a `choices` section, containing a `message` attribute <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. This message contains `role`, `content`, and potentially `tool_calls` <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.
3.  **Tool Calls Handling:**
    *   If `tool_calls` exist, the agent needs to perform the specified actions <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. An agent can perform multiple tool calls, though in this example, there's only one (creating an Asana task) <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
    *   A mapping is created from the tool's string name (output by AI) to the actual Python function object <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
    *   The tool request is added to the messages history as context for the AI <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
    *   For each tool call, the arguments decided by the AI are extracted, and the corresponding function is invoked <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.
    *   The result of the function call (e.g., Asana's response) is appended to the message history <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.
    *   The AI is queried again with the updated history, prompting it to generate a final message for the user based on the tool's outcome <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. This allows the AI to provide details like a link to the created task <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.

## Running the Agent
Once the `.env` file is populated with API keys, the script can be run using `python agents.py` <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.

### Demonstration
*   The agent initially functions as a regular GPT chatbot, building chat history <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.
*   When a request like "create a task for me to make a thumbnail for my next video and I need this done by Wednesday" is given, the agent intelligently decides to make the tool call and create the task in Asana <a class="yt-timestamp" data-t="15:13:00">[00:15:13]</a>.
*   The agent confirms task creation, including the due date and a direct link to the task in Asana, demonstrating its ability to parse the function's return <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.
*   The task appears in the specified Asana project, confirming the agent's external interaction <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.

This basic agent can be further expanded to add priority, status, assignments, or even prompt the user for missing information <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. This example demonstrates the power of [[building_ai_agents | AI agents]] to understand natural language and translate it into actionable code <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.

## Next Steps
Future tutorials will explore easier and more powerful ways to create [[building_productiongrade_ai_agents | production-grade AI agents]] <a class="yt-timestamp" data-t="16:36:00">[16:36:00]</a>.