---
title: Developing AI tools with Streamlit and GPT
videoId: s3SY_2a3Woo
---

From: [[colemedin]] <br/> 

This article details the development of a powerful AI agent designed for comprehensive task management within Asana, utilizing [[using_streamlit_and_python_for_web_development | Streamlit]] for the user interface and GPT (or Claude) as the underlying language model <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This [[developing_ai_agents_using_python | AI agent]] aims to save significant time by automating task management workflows <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Overview of the Asana Task Management AI Agent

The Asana chatbot is an AI agent that hooks into Asana, a popular task management platform <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It's designed to manage daily tasks efficiently <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Core Capabilities
The agent can perform a wide range of actions within Asana through natural language commands <a class="yt-timestamp" data-t="00:01:00">[01:00:00]</a>:
*   **Project Management**: Create projects (the highest level of organization in Asana) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> and search through existing projects <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Task Management**: Search for tasks across projects, create new tasks, delete tasks, update task details, and mark tasks as complete <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Intuitive Interaction**: The chatbot allows users to manage Asana without directly using the Asana UI, by simply having conversations with the AI agent <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Demonstration of Functionality

The AI agent showcases its power through complex, multi-step commands:

### Research and Task Creation
1.  **Information Retrieval**: The agent can be asked to research and list information, such as "What are the top 10 technologies to learn as a software developer getting into AI?" <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. It provides a list based on its knowledge <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
2.  **Automated Project and Task Creation**: Following the research, the agent can be prompted to create an Asana project, for example, "AI learning", and then add each technology from the research list as a distinct task within that project, with a specified due date like "Wednesday" <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.
    *   This involves a complex sequence of actions: creating a project, entering it, creating multiple tasks, titling each task appropriately, and determining the correct due date based on the current date and the requested day <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
    *   Upon completion, the agent provides links to each created task within the new project <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
    *   The project "AI learning" appears in Asana with all specified tasks and due dates <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Task Management via Chat
The agent understands natural language for task updates:
*   **Marking Complete**: A command like "I have learned Python now" is understood as an instruction to mark the "Learn Python" task as complete in Asana <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. The agent confirms the action <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
*   **Deleting Tasks**: Stating "I don't want to learn mathematics and statistics anymore" implicitly tells the agent to delete the corresponding task <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. The agent processes this natural language request and removes the task <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.
*   **Creating New Tasks**: Users can explicitly request new tasks, such as "create another task to learn GPT" <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>, which the agent adds to the relevant project <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

All these changes are reflected instantly in the Asana UI <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

## Technical Implementation

The AI agent's development involves an existing codebase that includes a [[using_streamlit_and_python_for_web_development | Streamlit]] UI with a chatbot powered by GPT or Claude, capable of creating Asana tasks <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. The new enhancements focus on adding a suite of new tools to expand its Asana management capabilities.

### Project Structure and Setup
*   **GitHub Repository**: The code is available on GitHub in a folder named `task_management_agent` <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.
*   **Environment Variables**: An `example_environment_variable` file guides setup. A key change is the use of a whole Asana workplace ID instead of just a single project ID, allowing management of different projects <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
*   **Requirements**: The `requirements.txt` file lists necessary Python packages and their versions, including an updated Asana package version required for task deletion to function correctly <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

### Core Components
*   **Streamlit UI**: Provides the conversational interface for the user <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **`prompt_AI` Function**: Handles the streaming of responses and interacts with the AI model <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Asana Client**: An Asana client instance is initialized to interact with the Asana API <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **Tools (Functions)**: The core of the enhancement lies in creating new Python functions, each representing a specific Asana action. These functions interact with the Asana SDK.

#### Key Asana Tools Developed:
*   **`create_asana_task`**: Modified to accept a `project_id` parameter, enabling the bot to create tasks in various projects <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   **`get_asana_projects`**: Fetches all projects within the defined Asana workplace <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.
*   **`create_asana_project`**: Creates a new project in Asana, optionally with a due date <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
*   **`get_asana_tasks`**: Retrieves tasks from a specified `project_id` <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. It's noted that this currently does not handle pagination for more than 50 tasks <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
*   **`update_asana_task`**: Updates a single task given its ID and a data dictionary. This function can update the task's completion status (true/false) or due date <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. The AI uses the doc string to understand how to format this generic `data` dictionary specifically <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   **`delete_asana_task`**: Deletes a task using its ID <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>. The AI often correlates task names from previous queries with their IDs to call this function <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

### Tool Integration and Prompting
*   **Dynamic Tool Binding**: All created tools are dynamically added to a mapping of available functions. The `prompt_AI` function automatically binds these tools to the chatbot, making it easy to add new functionalities <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.
*   **Doc Strings**: The doc strings for each function are crucial. They instruct the [[integrating_large_language_models_like_gpt_with_custom_tools | AI agent]] on when and how to use the function, what parameters to provide, and what type of response to expect <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. Well-defined doc strings are essential for the AI to effectively utilize the tools <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.
*   **System Prompt Adjustments**: The system prompt is augmented with instructions for the AI agent on how to manage and present information to the user. For example, it's instructed not to display internal IDs to the user <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.

## Running the Agent

The AI agent can be run using the `streamlit run` command <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.

## Future Enhancements

The next steps in the master class will involve incorporating [[using_langchain_and_streamlit_for_rag_development | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>. This will allow the chatbot to integrate external knowledge, such as files from Google Drive or databases, to provide richer and more informed responses <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

A specific future application highlighted is the ability to:
1.  Record a meeting <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.
2.  Upload the recording to Google Drive <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
3.  Create a transcript from the recording <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
4.  Extract action items from the transcript <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
5.  Create tasks in Asana based on these action items, linking the RAG functionality with the Asana chatbot <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.