---
title: Using AI for research and personalized task planning
videoId: s3SY_2a3Woo
---

From: [[colemedin]] <br/> 

An advanced AI agent has been developed that transforms basic task creation into a comprehensive [[planning_and_task_management_in_ai_development | task management]] system, integrating with Asana to streamline daily workflows <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This agent is designed to save significant work hours by automating various aspects of [[building_an_ai_agent_for_task_management | task management]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Core Capabilities for Task Management
The AI agent, referred to as the Asana chatbot, offers extensive [[capabilities_of_ai_in_task_creation_and_management | capabilities of AI in task creation and management]] within Asana, a preferred [[planning_and_task_management_in_ai_development | task management]] platform <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. It can perform almost any action required to manage one's day in Asana, including:
*   Creating projects, which represent the highest level of organization in Asana <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.
*   Searching through existing projects <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   Searching for tasks across multiple projects <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   Creating new tasks <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
*   Deleting tasks <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.
*   Updating task details <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.
*   Marking tasks as complete <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

This functionality allows users to manage their daily tasks through natural language conversations with the AI agent, minimizing the need to interact directly with the Asana user interface <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

## Integrating Research with Task Planning
One powerful application of this AI agent is its ability to combine research with immediate task creation <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Users can ask the AI for information, and then use that information to populate their [[planning_and_task_management_in_ai_development | task management]] system.

### Example Workflow
1.  **Research Query**: A user can ask, "What are the top 10 technologies to learn as a software developer getting into AI?" The AI provides a list of technologies <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
2.  **Automated Task Creation**: Following the research, the user can then instruct the AI to create a project in Asana based on the research findings. For instance, "Okay great now create a project in Asana for me called AI learning, put each of these 10 texts as a task to learn them, all due by Wednesday" <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

This single, complex prompt demonstrates the AI's advanced capabilities:
*   It creates a new project <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   It generates individual tasks for each technology listed <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
*   It assigns appropriate titles to each task <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   It calculates and sets the due date for all tasks based on the given day (e.g., "next Wednesday") <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

The process provides links to each newly created task within the Asana project <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. As a result, an "AI learning" project appears in Asana, populated with tasks for each suggested technology, all with the correct due dates <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Personalized Task Updates
The agent also handles personalized task updates seamlessly through natural language:
*   **Marking Complete**: A user can say, "I have learned Python now," and the AI agent implicitly understands this as an instruction to mark the "Learn Python" task as complete in Asana <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **Deleting Tasks**: Users can express a desire not to learn a topic, such as "I don't want to learn mathematics and statistics anymore," and the AI will delete the corresponding task <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   **Adding New Tasks**: Explicit requests like "create another task to learn GPT" are also handled, adding the new task to the relevant project <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

All these changes are reflected in Asana, demonstrating the AI's ability to manage tasks without direct UI interaction <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

## Technical Implementation
The development of this AI agent involves [[building applications with ai assistance | building applications with AI assistance]] and leveraging [[using_ai_coding_assistance | AI coding assistance]]. The agent uses a Streamlit UI with a chatbot powered by GPT or Claude models <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.

Key aspects of its development include:
*   **Tools and Functions**: A set of new tools (functions) were created to interact with the Asana API, including `get_asana_projects`, `create_asana_project`, `get_asana_tasks`, `update_asana_tasks`, and `delete_asana_task` <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   **Workspace Integration**: The agent operates at the Asana workspace level, allowing it to manage tasks across different projects within that workspace <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   **Doc Strings for AI Guidance**: Each function includes detailed doc strings that instruct the AI agent on how and when to use the function, including expected parameters and response formats <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. The clarity of these doc strings is crucial for the AI's effective tool usage <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.
*   **Dynamic Tool Binding**: The tools are dynamically fetched and bound to the chatbot, making it easy to add new functionalities <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   **System Prompt Refinement**: The system prompt is enhanced with instructions, such as not displaying internal IDs to the user, to improve the user experience <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.

The code for this [[automator_enhancing_the_learning_and_application_of_ai | task management agent]] is available on GitHub <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## Future Enhancements
The capabilities of this AI agent are set to expand further through the integration of Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>. This will enable the chatbot to access external knowledge sources, such as files in Google Drive or databases, to provide richer responses and take more advanced actions <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

Future developments will include features like:
*   Recording and uploading meetings to Google Drive <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.
*   Generating transcripts from meeting recordings <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   Extracting action items from transcripts <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
*   Automatically creating tasks in Asana based on these action items <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.

This continuous development showcases the potential of [[agentic_workflows_and_ai_technology | agentic workflows and AI technology]] to create increasingly powerful and integrated [[examples_of_ai_agents_and_workflows | AI agents and workflows]] <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.