---
title: Implementing AI agents to interact with Asana
videoId: zaNIvRllycM
---

From: [[colemedin]] <br/> 

Artificial intelligence is a primary focus for developers, especially [[understanding_ai_agents | AI agents]], which unlock the full potential of AI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. An [[defining_ai_agents | AI agent]] is a large language model capable of interacting with the external world to perform actions like drafting emails, creating tasks, or adding contacts to a CRM <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These agents can work collaboratively on complex tasks or function autonomously for customer support <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

This article details a master class demonstrating how to [[building_an_ai_agent_for_task_management | develop AI agents]] from scratch to create a full application <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The immediate goal is to [[building_an_ai_agent_for_task_management | build an AI agent]] to create tasks in Asana <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Building the First AI Agent

The process of [[building_ai_agents | building AI agents]] assumes a basic understanding of Python <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. All code discussed in this master class will be available on GitHub <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The initial agent will function as a GPT chatbot that can interact with the outside world to [[integrating_ai_agents_with_asana_for_task_creation | create tasks]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Asana, a project and task management platform, is chosen for this external interaction <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The agent will be able to receive a command to create a task, execute it, and then verify its presence on the Asana website <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Setup and Configuration

1.  **Importing Packages**: Essential packages like Asana and OpenAI must be imported <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Installation instructions for these packages are provided in the GitHub repository <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  **Environment Variables**: Securely store sensitive information such as OpenAI API keys and Asana access tokens in a `.env` file, placed in the same directory as the Python script <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Example `.env` files and instructions for obtaining API keys are available on GitHub <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
3.  **Loading Environment Variables**: The `dotenv` package is used to load these variables, making them accessible via `os.env` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  **Client Initialization**:
    *   **OpenAI Client**: The OpenAI client is initialized, with the model specified (e.g., `gpt-4o`) retrieved from environment variables or defaulting if not defined <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   **Asana Client**: The Asana client is created using the access token from environment variables. The `tasks` API specifically needs to be instantiated, as the chatbot's primary function is to create tasks <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Chatbot Interaction Logic

GPT interaction involves maintaining a list of messages, each with one of three roles <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>:
*   **System Role**: Provides background context for the AI (e.g., "You are a personal assistant who helps manage tasks in Asana") and important dynamic information like the current date, which helps the AI set due dates <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **User Role**: Messages sent by the user <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Assistant Role**: Responses from the AI <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

The application runs in the command line, continuously looping to ask the user for input <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. If the user types 'Q', the application ends <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. User input is added to the messages list with the 'user' role <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. A `prompt_ai` function processes this list (maintaining chat history for context) and retrieves the AI's response <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. The AI's response is then printed to the terminal and added to the messages list with the 'assistant' role <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Core Functions for Asana Interaction

#### `create_asana_task` Function

This function handles the actual task creation in Asana <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   It takes `task_name` (required) and `due_on` (optional, defaults to today) as parameters <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   Logic sets the `due_on` date to the current date if it's not provided <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   Task data (name, due date, project ID) is defined according to Asana API documentation <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   The function calls the Asana `tasks` API to create the task and returns the response or an error <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The AI is intelligent enough to parse the JSON response from Asana, even extracting a link to the created task <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

#### `prompt_ai` Function

This function is responsible for prompting the AI and managing its responses and tool calls <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   It takes the `messages` list (including full chat history) and calls `client.chat.completions.create` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Parameters include the `model`, `messages`, and `tools` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

#### Defining Tools (`get_tools` Function)

The `tools` parameter is what makes the large language model an [[understanding_ai_agents | AI agent]], as it provides the ability to run specific Python functions that interact with the outside world <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   The `get_tools` function returns an array of objects, each defining a function the AI can call <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   Each tool definition includes:
    *   `description`: Tells the AI when to use the function <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   `parameters`: Defines the expected inputs for the function, including data types (e.g., `task_name`, `due_on`) and format (e.g., date format for `due_on`) <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
    *   `required`: Specifies which parameters are mandatory <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   The AI intelligently determines the `task_name` and `due_on` from natural language conversation, even converting dates into the required format <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This capability to convert natural language into executable code is a core strength of [[building_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

#### Handling AI Responses and Tool Calls

The AI's response from `client.chat.completions.create` follows a specific format, containing choices and message attributes <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Crucially, the response might include `tool_calls` if the AI decides to invoke one of the defined functions <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

If `tool_calls` are present:
1.  A mapping is created between the string name of the function (as output by the AI) and the actual Python function object <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
2.  The tool request (the AI's decision to call the tool) is added to the messages history <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
3.  Each tool call is iterated through <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
4.  The arguments determined by the AI for the function are extracted <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
5.  The actual Python function (e.g., `create_asana_task`) is called with these arguments <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
6.  The result of the function call (e.g., the Asana task creation response) is appended to the message history as a string <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This provides the AI with context on the outcome of its tool invocation <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
7.  Finally, the AI is queried *again* with the updated chat history to generate a human-readable response based on the tool call's outcome <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. The AI can then extract details like the task link from the tool's response and present it to the user <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

## Demonstration

After securely populating the `.env` file with API keys <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>, the script can be run using `python agent.py` <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

The agent functions as a regular chatbot, capable of answering general questions <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. However, when prompted with a request like "create a task for me to make a thumbnail for my next video and I need this done by Wednesday," the agent intelligently decides to invoke the Asana task creation tool <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

The agent's response confirms the task creation, including the due date (e.g., "Wednesday June 26th"), and provides a direct link to the newly created task in Asana <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. Verification in Asana shows the task (e.g., "create a thumbnail for next video") correctly added with the specified due date <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

## Conclusion

This demonstration highlights the power of [[integrating_ai_agents_with_services_like_slack | AI agents]]: they can chat like a standard GPT model while also performing external actions, such as [[integrating_ai_agents_with_asana_for_task_creation | creating Asana tasks]] <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. The agent's ability to understand natural language parameters (like task name and due date) and convert them into the required function arguments streamlines complex interactions <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

Future developments could involve enhancing the agent to ask for missing information (e.g., assignment details), add priorities, or manage task statuses <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. More advanced methods for [[developing_ai_agents_using_python | creating AI agents]] will be covered in subsequent tutorials <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.