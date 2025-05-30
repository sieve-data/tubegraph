---
title: Building an AI agent for task management
videoId: s3SY_2a3Woo
---

From: [[colemedin]] <br/> 

An [[building_ai_agents | AI agent]] can be developed to serve as a comprehensive task management tool, capable of saving significant work hours <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This agent integrates with task management platforms like Asana, allowing users to manage their daily tasks through natural language conversations <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Capabilities of the AI Agent
The [[capabilities_of_ai_in_task_creation_and_management | AI agent]] is designed to interact with Asana and perform various actions related to [[planning_and_task_management_in_ai_development | task management]], including:
*   Creating projects <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
*   Searching through projects <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Searching for tasks across projects <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Creating new tasks <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Deleting tasks <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Updating tasks <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Marking tasks as complete <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

Essentially, the agent can perform "literally anything that I need to do in Asana" to manage tasks <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It removes the need to use the Asana user interface directly for many operations <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Demonstrations of the AI Agent in Action

### Research and Task Creation
The AI agent can assist with [[using_ai_for_research_and_personalized_task_planning | research]] and then convert research findings into actionable tasks. For example, a user can ask:
*   "What are the top 10 Technologies to learn as a software developer getting into AI?" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
Once the agent provides a list, the user can then instruct it to:
*   "Create a project in Asana for me called AI learning put each of these 10 techs as a task to learn them all due by Wednesday" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
This complex instruction requires the AI to:
*   Create a new project <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Enter the project <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Create a distinct task for each technology <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
*   Determine the correct due date ("next Wednesday") <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
The agent executes this flawlessly, providing links to each newly created task within the Asana project <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Task Management Operations
Beyond creation, the agent can manage existing tasks:
*   **Marking Complete**: A user can state, "I have learned Python now," and the agent will infer the intent to mark the corresponding task as complete <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Deleting Tasks**: Users can express, "I don't want to learn mathematics and statistics anymore," and the agent will understand to delete the task without explicit instruction <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Creating New Tasks**: Users can explicitly request, "create another task to learn GPT," and the agent will add it to the relevant project <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## [[step_by_step_process_for_building_ai_agents | Building AI Agents]]: Technical Implementation Details
The process of [[building_ai_agents | building the AI agent]] involves enhancing an existing chatbot that could previously only create tasks in Asana <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Core Architecture
The code utilizes a Streamlit UI with a chatbot powered by GPT or Claude <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The core of the agent's functionality comes from defining "tools" (functions) that interact with the Asana API.

### Transition to Workspace Management
Initially, the agent operated within a single Asana project <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. To enable full task management, it was upgraded to manage tasks across an entire Asana workplace, requiring a change in the environment variable to specify the workplace ID <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. The `create_asana_task` function was updated to accept a `project_id` parameter, allowing task creation in different projects <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### New Tools for Enhanced Functionality
Several new tools were developed using the Asana SDK:
*   `get_asana_projects`: Fetches all projects within the Asana workspace <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   `create_asana_project`: Creates a new Asana project, optionally with a due date <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   `get_asana_tasks`: Retrieves tasks from a specified project ID <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. (Note: This implementation does not handle pagination for more than 50 tasks <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>).
*   `update_asana_tasks`: Updates a single task given its ID and a data dictionary. This generic function can update completion status (true/false) and due dates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   `delete_asana_task`: Deletes a task given its ID <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This function requires an upgraded Asana package version <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### The Role of Docstrings
Crucially, each tool includes a detailed docstring that guides the [[understanding_ai_agents | AI agent]] on:
*   How to use the function <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   When to use it <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
*   What parameters to provide <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   The expected response format <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
These docstrings are the "most important part of the prompt to the AI" as they ensure the AI uses the tools correctly and effectively <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Environment and Setup
The code for this agent is available on GitHub <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, specifically in the `task_management_agent` folder <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Users should note the updated environment variable for the Asana workplace ID and the specific Python package versions listed in `requirements.txt` <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### System Prompt Refinement
The system prompt was refined to provide instructions to the agent on how to manage and present information to the user. For instance, the agent is instructed to "never give IDs to the user since those are just for you to keep track of" <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, preventing the display of unnecessary technical details to the user.

## Future Developments
Future enhancements to this [[building_fullscale_ai_agents | fullscale AI agent]] will include integrating [[using_ai_for_research_and_personalized_task_planning | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This will allow the chatbot to incorporate external knowledge, such as files from Google Drive or database information <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. One planned application is the ability to record meetings, upload them to Google Drive, generate transcripts, and then extract action items to automatically create tasks in Asana <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. This connects the [[implementing_ai_agents_to_interact_with_asana | AI agent]] with capabilities developed in later stages of the master class.