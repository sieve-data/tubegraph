---
title: Setting up automation with Google Drive
videoId: 1g0MQamOXoY
---

From: [[customaistudio]] <br/> 

This article outlines the process of setting up an automation workflow to extract data from Google Drive and integrate it with a vector database to power an AI chatbot. The specific example focuses on building a chatbot to assist renters with the eviction process in Massachusetts <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Project Overview
The project involves transitioning from using Voiceflow to In8 (likely `n8n`) <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The goal is to create a chatbot that provides informed answers to users by leveraging a comprehensive knowledge base stored in a vector database <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Data Preparation
Before integrating data into the vector database, some data structuring is necessary to ensure the best results <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For this project, all English versions of necessary documents were extracted and converted into `.txt` files <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. These text files were then moved into a dedicated folder on Google Drive <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Setting Up the Vector Database (Pine Cone)
The first step is to configure the Pine Cone vector database.
1.  Create an index in Pine Cone, named "data" in this instance <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Set the text embedding to "three small" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
3.  Obtain the API key if setting up credentials for the first time <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Building the Data Extraction Automation in In8
The [[workflow_and_task_automation_using_ai_agents | automation workflow]] in In8 is designed to extract data from Google Drive and upload it to the Pine Cone vector database.

### Workflow Steps
1.  **Trigger**: Manually trigger the workflow <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
2.  **Google Drive Search**:
    *   Add a "Google Drive" node and select "Search Files and Folders" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Configure it to return "all" results and filter by the specific folder containing the `.txt` files <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Test this node to ensure it pulls the file data correctly for use in subsequent nodes <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
3.  **Google Drive Download File**:
    *   Add another "Google Drive" node, choosing "Download File" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   Map the "ID" from the previous node's output to download each file <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   This step downloads the files from Google Drive into In8 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  **Looping Mechanism**:
    *   To prevent the workflow from breaking when processing multiple files at once, a "Loop" node is added <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This ensures each file is processed individually <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
5.  **Vector Store (Pine Cone) Integration**:
    *   Add a "Vector Store" node for Pine Cone <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   **Credentials**: Use the demo account or your specific Pine Cone API key <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   **Index**: Select the "data" index <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   **Namespace**: Create a namespace called "all data" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This strategy allows the agent to search all data if needed, or specific namespaces if desired later <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   **Operation**: Set to "Insert Document" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   **Document**: Attach the file output from the "Download File" node <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   **Embedding Model**: Use Open AI's "text embedding three small" to match the Pine Cone index setting <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   **Data Type**: Set to "binary" and automatically detect MIME type <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Chunk Sizes**: Set chunk sizes to a large value (e.g., 2000) for better handling of the data <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

The completed [[building_and_managing_data_workflows_for_ai | data workflow]] extracts, processes, and uploads the `.txt` files to the vector database <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Building the AI Agent (Chatbot)
Once the data is in the vector store, the AI agent can be built to interact with it.

### Agent Setup
1.  **Agent Type**: Select "Conversational Agent" for ongoing dialogue <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
2.  **Return Immediate Steps**: Enable this option to view step-by-step logs for troubleshooting <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Chat Model**: Use OpenAI's `gpt-4o` (or `Omni`) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
4.  **Window Buffer**: Set a window buffer (e.g., 5) to provide the model with context from past messages <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
5.  **Vector Store Tool**:
    *   Add a "Vector Store Tool" <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   **Name**: "database" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   **Description**: "Tool to provide relevant and useful answers to the users questions about navigating their eviction process" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
    *   **Limit**: Set a limit (e.g., 5) on the number of results retrieved from the vector store <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This often requires testing for optimal results <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   **Vector Store**: Select "Pine Cone" and the "demo" credential <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   **Index**: Select the "data" index <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
    *   **Namespace**: For now, the agent searches the "all data" namespace <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. A future enhancement could involve dynamically identifying the correct namespace based on user queries for more efficient searching <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

This setup provides a [[automating_business_processes_with_ai_agents | Bare Bones]] agent capable of chatting with the data <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

## Testing the Agent
The agent can be tested directly within the In8 chat interface <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

### Example Interaction
*   **User Query**: "I received a summons and complaint, what should I do now?" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
*   **Agent Response**: Provides step-by-step instructions, including reading carefully, checking deadlines, seeking legal advice, and options like settling or going to court <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

### Log Analysis
The "immediate steps" log reveals the agent's process:
1.  The model reads the window buffer memory <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  The model is triggered and sends the input query to the vector store tool <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
3.  The vector store (Pine Cone) retrieves the relevant data <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
4.  The agent's model then processes the response from the vector store and generates the final output for the user <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Future Enhancements
While the current setup provides a basic, functional agent, several areas can be improved for greater efficiency and user experience:
*   **Document Upload**: Implement functionality for users to upload documents, allowing the system to identify document types (e.g., summons, motion hearing) and provide tailored advice <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Personalization**: Add details about how to respond and interact with different entities <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Database Segmentation**: Further segment the database to potentially yield better responses by fine-tuning data retrieval <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Conversation Flow Design**: [[designing_prompts_for_calendar_and_email_actions | Design a more structured flow]] for conversations <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
*   **Actions**:
    *   [[humanai_collaboration_and_workflow_integration | Integrate actions]] to connect users with attorneys, including retrieving contact information from the database <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
    *   [[integrating_ai_with_communication_tools_like_email_and_calendar | Add actions]] for follow-up emails after conversations to provide additional support or contact information <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

Developing the initial 80% of the solution is relatively quick, but the remaining 20% involves refining details to achieve a truly robust and efficient system <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. This process highlights the fundamentals involved in [[combining_ai_agents_with_traditional_automation_workflows | building and deploying AI agents]].