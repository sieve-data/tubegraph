---
title: Building AI agents with n8n
videoId: 1g0MQamOXoY
---

From: [[customaistudio]] <br/> 

This article outlines the process of [[building_an_ai_agent_with_n8n | building an AI agent]] using n8n, specifically for a chatbot designed to help renters navigate the eviction process in Massachusetts. The demonstration focuses on setting up a vector database, uploading data, and configuring the AI agent chatbot from scratch <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Project Overview

The project involves transitioning a client's chatbot from Voiceflow to n8n <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core functionality is to provide informed answers to renters about the eviction process in Massachusetts <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The aim is to demonstrate how quickly and easily these components can be set up to enable experimentation <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Core Components for Building an AI Agent

The process involves three main phases:

1.  Setting up the vector database.
2.  Uploading data to the database.
3.  Configuring the AI agent chatbot.

### 1. Setting Up the Vector Database (Pinecone)

The first step is to establish the vector database. Pinecone is used for this purpose <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

*   **Create Index:** An index named "data" is created in Pinecone <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Embedding Model:** The "text embedding three small" model is selected for the index <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **API Key:** For first-time setup, the API key from Pinecone is required for n8n credentials <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### 2. Data Preparation and Ingestion

A robust knowledge base is crucial for the chatbot to provide accurate and informed answers <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

#### Data Structuring

*   **Source:** Documents were downloaded from Google Drive <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Extraction:** English versions of the documents were extracted <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Conversion:** Documents were converted into `.txt` files <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a> to optimize results when ingested into the vector database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

#### Automation in n8n for Data Ingestion

An n8n workflow is used to extract and upload data to Pinecone <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

*   **Trigger:** Manual trigger <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Google Drive Nodes:**
    *   **Search Files and Folders:** Configured to search for all files within a specified folder <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   **Download File:** Downloads the files from Google Drive into n8n using their ID and name <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Vector Store Node (Pinecone):**
    *   **Operation:** `Insert Documents` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   **Index:** "data" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   **Namespace:** `all data` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
        *   Namespaces segment data within the vector store. An agent configured to a specific namespace will only retrieve data from that namespace <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. To allow the agent to search all data, it's common to create a single "all data" namespace and individual namespaces for specific buckets of data <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   **Embedding Model:** Open AI's "text embedding three small" <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This must match the model used for the Pinecone index <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   **Type of Data:** Binary <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Chunk Sizes:** Set to a larger size to accommodate a decent amount of data efficiently <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Looping:** A `Loop` node is essential to process each file individually and prevent the workflow from breaking due to too much information being processed at once <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

> [!NOTE] Inefficiency during data ingestion: The current method downloads `.txt` files from Google Drive and then uploads them to the vector store. The speaker notes this feels redundant and inefficient, inviting suggestions for a more direct approach <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### 3. Setting Up the AI Agent Chatbot

After data ingestion, the AI agent is constructed.

*   **Agent Type:** Conversational Agent <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Return Immediate Steps:** Enabled to show step-by-step logs for easier troubleshooting <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Components:**
    *   **Chat Model:** Open AI's GPT-4o (Omni) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
    *   **Window Buffer Memory:** Set to 5, providing the model with context from past messages <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   **Vector Store Tool:** Configured to interact with the Pinecone database.
        *   **Name:** `database` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
        *   **Description:** "Tool to provide relevant and useful answers to the users questions about navigating their eviction process" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
        *   **Limit:** 5, for the number of results to retrieve <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
        *   **Vector Store:** Pinecone <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
        *   **Index:** "data" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
        *   **Embedding Model:** Open AI's "text embedding three small" <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

> [!NOTE] Dynamic Namespaces: In future implementations for more complex [[ai_agent_projects_and_learnings | AI agent projects]], the namespace could be dynamically set using an expression. This would allow the agent to understand the user's query and efficiently search the most relevant namespace <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Testing the Agent

The agent can be tested directly within n8n's chat interface <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

*   **Example Query 1:** "I received a summons and complaint, what should I do now?" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
    *   **Response:** The agent provided step-by-step advice, including reading carefully, checking deadlines, and the types of actions that can be taken <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Example Query 2:** "The document I received says I need to move out in seven days, what do I do?" <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>
    *   **Response:** The agent suggested reviewing the notice, knowing rights, seeking legal advice, communicating with the landlord, preparing to move, documenting everything, and considering filing a court motion <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

#### Interpreting Logs

The `Return immediate steps` setting provides logs that show the agent's thought process <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>:

1.  **Window Buffer Memory:** The model first checks the conversational context <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  **Model Trigger:** The main agent model is triggered <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
3.  **Vector Store Interaction:** The model sends the query to the vector store tool <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
4.  **Response from Vector Store:** The vector store's model retrieves and provides the answer <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
5.  **Final Output:** The agent model formulates the final response to the user <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
6.  **Context Saving:** The conversation is added to the window buffer memory <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

## Next Steps and Future Improvements

While this establishes a bare-bones AI agent, further improvements are necessary for real-world application <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. These include:

*   **Detailed Responses:** Adding specifics on how to respond and communicate <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Personalization:** Implementing features for tailored user experiences <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Database Segmentation:** Further segmenting the database for potentially better responses <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Flow Design:** Designing a more refined conversational flow <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Actions:** Adding actions such as:
    *   Connecting users with attorneys (e.g., providing contact information) <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
    *   Sending follow-up emails post-conversation <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Document Upload:** A crucial future functionality is allowing users to upload documents (e.g., summons and complaints) for the system to read and identify relevant information (e.g., type of document, deadlines) <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This would enable the system to suggest appropriate actions based on the specific document received (e.g., settling, going to court, moving out, paying) <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

[[challenges_in_ai_agent_integration | Challenges in AI agent integration]] often lie in perfecting the details to achieve peak performance, moving from 80% functionality to the crucial last 20% that makes a significant difference <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.