---
title: Capabilities of AI in task creation and management
videoId: s3SY_2a3Woo
---

From: [[colemedin]] <br/> 

An [[building_an_ai_agent_for_task_management | AI agent]] can be developed into a comprehensive [[planning_and_task_management_in_ai_development | task management]] system, offering the potential to save significant work hours <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This powerful [[agentic_workflows_and_ai_technology | AI technology]] allows users to interact with their task management platforms, such as Asana, through a chatbot interface <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Core Task Management Capabilities

The Asana chatbot demonstrates a wide range of [[advantages_of_ai_agents | advantages of AI agents]] in managing daily tasks <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. It can perform virtually any action required within Asana, including:
*   Creating projects, which represent the highest level of task organization <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Searching through existing projects <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Searching for tasks across multiple projects <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Creating new tasks <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Deleting tasks <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Updating task details <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Marking tasks as complete <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

This functionality means users can manage their day entirely through conversational commands, bypassing the need to directly use the Asana user interface <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Advanced AI Functionalities

### Research and Task Planning
AI agents can assist with research, providing information like lists of top technologies to learn for specific fields <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Beyond simple information retrieval, the AI can then [[using_ai_for_research_and_personalized_task_planning | create tasks and projects]] based on this research <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For example, it can take a list of 10 suggested technologies and:
*   Create a new project in Asana (e.g., "AI learning") <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   Add each technology as a distinct task within that project <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Automatically assign due dates for all new tasks based on a given timeframe <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This complex process involves the AI making a project, populating it with tasks, titling each task, and determining due dates based on the current date and user input, all from a single prompt <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Natural Language Processing and Implicit Actions
The AI agent is sophisticated enough to understand and execute commands given in natural language, even when instructions are not explicit <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Examples include:
*   Responding to "I have learned python now" by marking the "Learn Python" task as complete in Asana <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Interpreting "I don't want to learn mathematics and statistics anymore" as a command to delete the corresponding task <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   Allowing explicit commands such as "create another task to learn GPT" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Underlying Mechanisms
The development process involves [[building_applications_with_ai_assistance | building applications with AI assistance]] by adding new tools to the AI agent <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. These tools, which are functions interacting with the Asana API, include:
*   `get_asana_projects`: Retrieves projects within the Asana workspace <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   `create_asana_project`: Creates new projects, optionally with due dates <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   `get_asana_tasks`: Fetches tasks from a specific project <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   `update_asana_tasks`: Modifies task details, such as completion status or due dates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   `delete_asana_task`: Removes a task given its ID <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

Each tool requires a "doc string" that precisely informs the AI agent when and how to use the function, including expected parameters and the format of the response <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The AI dynamically fetches and binds these available tools, simplifying the process of [[creating_tools_and_dependencies_for_ai_agents | creating tools and dependencies for AI agents]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Instructions can also be added to the system prompt to guide the agent on how to manage and present information (e.g., not exposing internal IDs to the user) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## Future Developments

Further enhancements to these [[integrating_ai_agents_with_asana_for_task_creation | AI agents integrating with Asana]] include the incorporation of [[retrieval_augmented_generation | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This will allow the AI to access and utilize external knowledge, such as files in Google Drive or databases <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Future capabilities planned include:
*   Recording meetings and uploading them to Google Drive <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
*   Creating transcripts from meeting recordings <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   Extracting action items from these transcripts <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   Automatically creating tasks in Asana based on the identified action items <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.