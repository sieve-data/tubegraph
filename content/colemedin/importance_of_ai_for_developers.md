---
title: Importance of AI for developers
videoId: zaNIvRllycM
---

From: [[colemedin]] <br/> 

Artificial intelligence (AI) is unequivocally the top area of focus for all developers today <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. However, many developers may not be adequately focusing on [[importance_of_ai_agents_in_2025 | AI agents]], which are essential for unlocking the full potential of AI <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding AI Agents
An [[importance_of_ai_agents_in_2025 | AI agent]] is a large language model (LLM) that has the capability to interact with the external world <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This interaction allows agents to perform practical functions such as drafting emails, creating tasks, or managing CRM contacts <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

The true power of AI, including useful and powerful applications like customer support, is realized through the development of [[importance_of_ai_agents_in_2025 | AI agents]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Agents can be developed to collaborate on complex tasks or function autonomously <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. To leverage AI for [[building_applications_with_ai_assistance | building applications with AI assistance]], developers need to utilize [[importance_of_ai_agents_in_2025 | AI agents]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Building Your First AI Agent
Creating an [[importance_of_ai_agents_in_2025 | AI agent]] from scratch typically assumes a basic understanding of Python <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>. The foundational steps involve setting up the development environment and integrating necessary tools.

#### Key Development Steps
1.  **Project Setup**
    *   **Import Packages:** Begin by importing required packages such as `Asana` and `OpenAI` <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. Instructions for package installation are typically provided in associated GitHub repositories <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
    *   **Environment Variables:** Define environment variables in a `.env` file to store sensitive information like API keys (e.g., OpenAI API key, Asana access token) and configuration <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. These variables are loaded using packages like `python-dotenv` <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a> and accessed via `os.environ` <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

2.  **API Client Initialization**
    *   **OpenAI Client:** Create the OpenAI client, often with a default model like `gpt-4o` <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
    *   **Asana Client:** Initialize the Asana client using the access token from environment variables <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Specific APIs, such as the tasks API, need to be instantiated if the agent interacts with them <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

3.  **Chatbot Interaction Logic**
    *   **Message Structure:** Interaction with GPT models involves a list of messages, each with a defined role:
        *   `system`: Provides background context for the AI <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. For example, setting the agent's persona ("personal assistant who helps manage tasks in Asana") and current date <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
        *   `user`: Represents messages from the user <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
        *   `assistant`: The AI's response <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
    *   **Tool Integration:** The `tools` attribute is crucial for enabling the GPT model to interact with the outside world by running Python functions <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. This is how the [[incorporating_ai_agents_and_advanced_development_features | AI agent]] executes actions.
    *   **Interaction Loop:** A typical agent application runs in a loop, continuously prompting the user for input and adding user messages to the chat history <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.

#### Implementing External Tool Calls (e.g., Asana Task Creation)
A key aspect of an [[importance_of_ai_agents_in_2025 | AI agent]] is its ability to perform actions through external tools.

*   **Function Definition:** Create a Python function (e.g., `create_asana_task`) that encapsulates the logic for interacting with the external service. This function takes relevant parameters, such as task name and an optional due date <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Tool Configuration:** To allow the AI to use your function, you must define it as a tool. This involves providing:
    *   **Description:** Explains when the AI should use the function <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
    *   **Parameters:** Defines the input arguments the function expects (e.g., `task_name`, `due_on`), including their types and any specific formats (like date formats) <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
    *   **Required Parameters:** Specifies which parameters are mandatory for the function call <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
    *   The AI can intelligently determine parameters like task name and due date from natural language conversation and convert them to the required format <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>. This demonstrates the power of agents to translate natural language into executable code for external interactions <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.

#### AI Response and Tool Execution
When the AI is prompted:
*   It analyzes the chat history and the available tools <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   The AI's response (`completion.choices[0].message`) can include `tool_calls` if it decides to invoke a function <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   The `tool_calls` contain the name of the function to invoke and the arguments the AI has decided to pass to it <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.
*   The Python script then calls the corresponding function with these arguments <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.
*   After the tool is executed, its result is appended to the message history, providing the AI with context for its next response <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   Finally, the AI generates a human-readable response based on the tool's output and the conversation context <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>. For example, if a task was created, the AI can extract the task's link from the Asana response and provide it to the user <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.

## Advantages of AI Agents for Developers
This rapid development process demonstrates the [[advantages_of_ai_agents | advantages of AI agents]]:
*   They can engage in natural conversation like a standard GPT chatbot <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>.
*   They can perform external actions (like creating Asana tasks) based on natural language commands <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.
*   They intelligently interpret parameters, eliminating the need for users to provide exact code-specific inputs <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.

This basic [[importance_of_ai_agents_in_2025 | AI agent]] can be significantly expanded, for example, by adding priority, status, or assignee fields to tasks, or by making the agent prompt for missing information <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. Future developments in [[evolution_of_ai_ides | AI IDEs]] and simplified approaches will make creating [[importance_of_ai_agents_in_2025 | AI agents]] even easier and more powerful <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.