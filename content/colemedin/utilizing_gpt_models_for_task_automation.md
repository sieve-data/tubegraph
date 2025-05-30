---
title: Utilizing GPT models for task automation
videoId: zaNIvRllycM
---

From: [[colemedin]] <br/> 

Artificial intelligence is a primary focus for developers, with particular emphasis on AI agents as the key to unleashing its full potential <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. An AI agent is a [[integrating_large_large_language_models_like_gpt_with_custom_tools | large language model]] granted the capability to interact with the outside world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Capabilities of AI Agents

AI agents can perform various tasks such as:
*   Drafting emails <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   Creating tasks <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Adding contacts to a CRM <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>

Agents can be developed to work collaboratively on complex tasks or function autonomously, for instance, as customer support <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The most useful and powerful AI applications are built using agents <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This approach allows for actually using AI to build practical applications <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Building an AI Agent: A Practical Example

To demonstrate agent development, a master class focuses on [[building_an_ai_agent_for_task_management | building an AI agent]] from scratch that operates as a [[using_llama_32_and_gpt_40_mini_for_generative_ai_tasks | GPT chatbot]] and interacts with the outside world to create tasks in Asana <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a> <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This process assumes a basic understanding of Python <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Project Setup and Configuration

1.  **Required Packages:** Import necessary packages like Asana and OpenAI. Installation instructions are available in the linked GitHub repository <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
2.  **Environment Variables:** Define environment variables (e.g., OpenAI API key, Asana access token) in a `.env` file to manage secrets and configurations <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. These variables are then loaded using the `dotenv` package <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
3.  **Client Initialization:**
    *   Initialize the OpenAI client, defining the model (e.g., `gpt-40`) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
    *   Create the Asana client using the access token and specifically set up the tasks API <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

### Chatbot Interaction Logic

The interaction with GPT involves maintaining a list of messages, each with one of three roles:
*   **System Role:** Provides background context for the AI <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. For this agent, the initial system message states: "You are a personal assistant who helps manage tasks in Asana" and includes the current date <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
*   **User Role:** Messages from the user <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
*   **Assistant Role:** The response from the AI <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

A continuous loop in the command line allows the user to input messages. User input is added to the messages list (chat history) <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. The AI is then prompted with this chat history, and its response is printed and added back to the messages list as an assistant message <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Core Agent Functionality: Tools

The concept of "tools" is fundamental to AI agents, allowing the GPT model to interact with the outside world by running Python functions <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a> <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.

#### 1. `create_asana_task` Function
This function adds tasks to Asana. It takes two parameters:
*   `name`: The task name (required).
*   `due_on`: An optional argument for the due date, defaulting to today <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
The function defines the data required by the Asana API (task name, due date, and project ID) and calls the task API to create the task <a class="yt-timestamp" data-t="07:07:00">[07:07:07]</a>.

#### 2. Defining Tools (`get_tools`)
To enable GPT to use functions, configuration is required:
*   **Description:** Tells the AI when to use the function <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
*   **Parameters:** Defines what inputs the function expects, including argument names, types, and crucial details like date format <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
*   **Required Parameters:** Specifies which parameters are mandatory <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
The AI can intelligently determine the task name and due date from natural language input, even converting it to the required date format <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. This ability to translate natural language into code for external interaction is a core strength of agents <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.

#### 3. Prompting the AI (`prompt_ai`)
This function takes the current list of messages (chat history) and calls `client.chat.completions.create`, passing the model, messages, and the defined tools <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

#### 4. Handling Tool Calls
When the AI's response indicates a tool call (via the `tool_calls` attribute), the agent performs the following steps:
1.  **Map Tool Name:** Maps the string name of the invoked function to its actual Python object <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
2.  **Append Tool Request:** Adds the AI's request to invoke the tool to the chat history for context <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
3.  **Execute Tool:** Loops through each tool call, extracts the arguments provided by the AI, and calls the corresponding function (e.g., `create_asana_task`) <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
4.  **Append Tool Result:** Adds the result of the function call to the chat history <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.
5.  **Final AI Query:** Queries the AI again with the updated chat history (including the tool request and its result). This prompts the AI to generate a human-readable response based on the tool's execution, which can include details like a link to the created task <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.

### Demonstration

After setting up the environment variables (off-camera for security) <a class="yt-timestamp" data-t="14:30:00">[01:30:00]</a>, the Python script can be executed. The agent initially functions as a regular chatbot <a class="yt-timestamp" data-t="14:51:00">[01:51:00]</a>. However, when prompted to create a task, such as "create a task for me to make a thumbnail for my next video and I need this done by Wednesday," the agent intelligently decides to make the tool call <a class="yt-timestamp" data-t="15:00:00">[01:51:00]</a>.

The agent confirms task creation, specifies the due date (e.g., Wednesday, June 26th), and provides a direct link to the task in Asana <a class="yt-timestamp" data-t="15:26:00">[01:56:00]</a>. This demonstrates the [[capabilities_of_ai_in_task_creation_and_management | AI's capability]] to understand natural language parameters (task name, due date) without requiring explicit function syntax <a class="yt-timestamp" data-t="16:23:00">[02:23:00]</a>. This basic agent can be further extended to include priority, status, assignments, or even prompt the user for missing information <a class="yt-timestamp" data-t="15:55:00">[02:55:00]</a>.

This example showcases how [[integrating_large_language_models_like_gpt_with_custom_tools | GPT models can be utilized for task automation]], transforming natural language commands into actionable steps in external applications. Future developments aim to simplify and enhance the creation of AI agents <a class="yt-timestamp" data-t="16:36:00">[03:36:00]</a>.