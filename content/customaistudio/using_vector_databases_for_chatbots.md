---
title: Using vector databases for chatbots
videoId: 1g0MQamOXoY
---

From: [[customaistudio]] <br/> 

[[using_vector_databases_for_ai_agent_tasks | Using vector databases with AI agents]] is a key component for building effective chatbots. This article outlines the process of creating a chatbot designed to help renters navigate the [[handling_eviction_processes_with_chatbots | eviction process]] in Massachusetts, transitioning from Voiceflow to N8N. The project involves setting up a vector database, uploading data, and configuring an AI agent to interact with that data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Setting Up the Vector Database

The first step in building the chatbot is to set up a [[setting_up_a_vector_database | vector database]]. For this project, Pinecone was used <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Pinecone Index Configuration
1.  **Create Index**: An index named "data" was created <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  **Embedding Model**: The "text embedding three small" model was selected for the index <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
3.  **API Key**: Existing API credentials were used <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Data Preparation and Upload

A robust knowledge base is crucial for the chatbot to provide informed answers <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Data Structuring
Prior to uploading, some data structuring is performed to ensure the best results <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:
*   Relevant documents were downloaded <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   English versions of documents were extracted <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   All extracted documents were converted into `.txt` files <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Automation with N8N
N8N is used to automate the process of extracting data from Google Drive and uploading it to Pinecone <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:
1.  **Google Drive Search**: An N8N workflow was set up to search for files in a specific Google Drive folder <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  **Download Files**: Files were downloaded from Google Drive into N8N using their IDs and names <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  **Vector Store Integration**: The downloaded files are then prepared for insertion into Pinecone <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>:
    *   **Credential**: The "demo" account was used <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   **Index**: The "data" index was selected <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   **Namespace**: A namespace called "all data" was created to store all documents <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
        *   **Namespace Strategy**: While namespaces can segment data (e.g., by topic), an agent can only pull data from the specific namespace it's directed to <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. To allow the agent to search across all data, it's common practice to duplicate data into an "all data" namespace <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   **Embedding Model**: OpenAI's "text embedding three small" model was specified for embedding the documents, matching the Pinecone index configuration <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   **Chunk Sizes**: Chunk sizes for the documents were set to be large to accommodate the amount of data <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Looping for Upload**: A loop was implemented in N8N to process and upload each file individually to the vector store, preventing the process from breaking due to too many files at once <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Building the AI Agent

With the vector database populated, the next step is to configure the AI agent in N8N <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Agent Configuration
*   **Agent Type**: A "conversational agent" was chosen, which is suitable for chatbot interactions <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Return Immediate Steps**: This option was enabled to show step-by-step logs, aiding in troubleshooting <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Chat Model**: OpenAI's GPT-4o (Omni) was selected as the primary chat model <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Window Buffer Memory**: A five-window buffer was set up to give the model context from past messages in the conversation <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Vector Store Tool**: This tool allows the agent to access the Pinecone database <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>:
    *   **Tool Name**: "database" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   **Description**: "to provide relevant and useful answers to the users questions about navigating their eviction process" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
    *   **Limit**: A limit of five was set for retrieved results, though further testing is needed for optimal performance <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
    *   **Vector Store**: Pinecone (demo account) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   **Index**: "data" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
    *   **Dynamic Namespace (Future Consideration)**: The ability to dynamically understand which part of the data the user is asking about and identify the correct namespace for efficient searching is a potential future improvement <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   **Embedding Model**: OpenAI's "small" embedding model was added <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Testing the Chatbot

The chatbot was tested by asking questions related to the eviction process in Massachusetts.

### Example Queries and Responses
*   **Query**: "I received a summons and complaint what should I do now?" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
    *   **Response**: The chatbot provided a step-by-step guide, including advice to read carefully and note deadlines <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
*   **Query**: "the document I received says I need to move out in seven days what do I do?" <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>
    *   **Response**: The chatbot advised reviewing the notice, knowing rights, seeking legal advice, communicating with the landlord, preparing to move, documenting everything, and considering filing a court motion <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### Log Review
The "immediate steps" feature allowed for detailed log review, showing the agent's process <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>:
1.  The model first read the message and the window buffer memory <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  It then triggered the vector store, sending the query <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
3.  The vector store model retrieved the relevant data (e.g., from Pinecone) <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
4.  Finally, the agent's main model processed this response and generated the user-facing output, adding it to the window buffer memory <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Future Improvements

While the basic setup was quick and effective <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>, several areas for improvement were identified:
*   Adding details on how to respond and communicate with people <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   Incorporating personalization <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   Segmenting the database more effectively for better responses <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   Designing a more refined conversational flow <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   Adding actions, such as connecting users with attorneys or sending follow-up emails with contact information <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   Allowing users to upload documents for the system to read and identify the type of legal notice received <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

The initial setup of the database and agent took approximately 18 minutes, demonstrating the speed at which a functional chatbot can be spun up <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. The real challenge lies in refining the details to achieve a highly efficient and effective system <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.