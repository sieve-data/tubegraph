---
title: Integration with Asana for project organization
videoId: s3SY_2a3Woo
---

From: [[colemedin]] <br/> 

An AI agent has been developed to serve as a comprehensive task management tool, capable of significantly reducing work hours <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This agent, initially designed to [[integrating_ai_agents_with_asana_for_task_creation | create tasks in Asana]], has evolved into a powerful Asana chatbot that can manage virtually any aspect of daily tasks and projects within the platform <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Key Capabilities

The Asana-integrated AI agent can perform a wide range of actions to streamline project and task management:
*   **Project Creation**: Create new projects, which are the highest level of task organization in Asana <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Project and Task Search**: Search through existing projects and find specific tasks across various projects <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Task Management**:
    *   Create tasks <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
    *   Delete tasks <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
    *   Update tasks (e.g., changing due dates) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>, <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>
    *   Mark tasks as complete <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>
*   **Natural Language Interaction**: Understand and execute commands given in natural language, reducing the need for explicit instructions <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   [[improvements_in_project_organization_and_contribution_management | Improvements in Project Organization]]: The agent manages projects at the workplace level, allowing for more complex organizational structures than just a single project <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## Demonstrated Use Cases

The AI agent showcases its utility through several practical examples:

### Research and Project Initialization
An example demonstrates the agent performing research, such as identifying the "top 10 technologies to learn as a software developer getting into AI" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Following this, with a single prompt, the agent can:
*   Create a new project in Asana named "AI learning" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   Populate this project with each of the 10 suggested technologies as individual tasks <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Automatically assign a due date (e.g., "all due by Wednesday") to all created tasks, calculating the specific date based on the current date <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Upon completion, the agent provides direct links to each new task within the Asana project <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Dynamic Task Management
The agent can manage tasks effortlessly through conversational commands:
*   **Marking Complete**: A command like "I have learned python now" automatically identifies the "Learn Python" task and marks it as complete in Asana <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **Deleting Tasks**: Stating "I don't want to learn mathematics and statistics anymore" leads the agent to understand the intent and delete the corresponding task without explicit deletion commands <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Creating New Tasks**: Users can explicitly request new tasks, such as "create another task to learn GPT... learn how to use the API" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, and the agent adds it to the relevant project <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

These capabilities mean users can manage their daily tasks and projects without needing to interact directly with the Asana user interface (UI) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Technical Implementation

The AI agent uses a Streamlit UI and integrates with large language models (LLMs) like GPT or Claude <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The development process involves:
*   **Tool Development**: Creating specialized Python functions for each Asana operation (e.g., `create_Asana_task`, `get_Asana_projects`, `create_Asana_project`, `get_Asana_tasks`, `update_Asana_tasks`, `delete_Asana_task`) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Asana SDK Integration**: These tools leverage the Asana Software Development Kit (SDK) to interact with the Asana API <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. An important note is that the Asana SDK version needs to be updated for task deletion functionality <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Docstrings for AI Instruction**: Each tool function includes a descriptive docstring that precisely informs the AI agent how and when to use the function, what parameters to provide, and what kind of response to expect <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This is crucial for the AI's effective decision-making <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Dynamic Tool Binding**: The system dynamically fetches and binds all available tools from a mapping to the chatbot, making it easy to add new functionalities <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>, <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **System Prompt Refinement**: The system prompt guides the AI on how to manage and present information to the user, for instance, by not exposing internal Asana IDs <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Future Enhancements

The AI agent's capabilities are continuously being expanded. Upcoming developments will focus on [[streamlining_meeting_notes_into_actionable_tasks | retrieval augmented generation (RAG)]] to integrate external knowledge, such as files from Google Drive or database information, into the chatbot <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>, <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This will enable advanced workflows like:
*   Recording and uploading meetings to [[integrating_ai_agents_with_services_like_slack_and_google_drive | Google Drive]] <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>, <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   Transcribing meeting audio <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
*   Extracting action items from transcripts <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   Automatically creating tasks in Asana based on these action items <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

This further integration aims to connect all components for an even more powerful and seamless task management experience <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.