---
title: Setting up a vector database
videoId: 50wqKgEHQtc
---

From: [[customaistudio]] <br/> 

[[introduction_to_vector_databases | Vector databases]] serve as the contextual master database for [[building and deploying AI agents | AI agents]], providing them with an always-updated knowledge base of business information to help them accurately, reliably, and quickly complete tasks or objectives without coding <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Overview of Vector Databases
Vectors are numerical representations of data <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For instance, a sentence like "AI agents are powerful" might convert into a 300-dimensional vector <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The process involves breaking text into tokens (approximately four characters per word) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, attaching a number (vector) to each token <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, and then placing these numbers in a multi-dimensional database where they are related to each other <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

When performing similarity searches, the system looks for vectors closely related in this multi-dimensional space <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. These vectors aren't just numbers; they have words attached, allowing the agent to read and pull necessary information <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

To efficiently pull data, proper [[indexing_and_namespace_creation | indexing and namespace creation]] is crucial <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. [[indexing_and_namespace_creation | Indexing]] enables searching through large sets of vectors by breaking down different data types into separate indexes <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Namespaces further segment data within an index, allowing for organization by specific categories like client names or projects <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Why Use Vector Databases for AI Agents?
[[using_vector_databases_with_ai_agents | Vector databases]] are essential for:
*   **Contextual Understanding**: They provide [[using_vector_databases_with_ai_agents | AI agents]] with the contextual understanding needed to fulfill user requests <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This eliminates the need for massive prompts, as the agent can query stored data like emails, calendar events, or documents to identify the correct context <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Semantic Search**: Unlike traditional keyword searches, [[using_vector_databases_for_chatbots | vector databases]] enable semantic search, allowing [[using_vector_databases_with_ai_agents | AI agents]] to understand the meaning behind complex queries, similar to human comprehension <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Unstructured Data Storage**: [[using_vector_databases_with_ai_agents | AI agents]] frequently handle unstructured data (e.g., emails, chat logs, documents) <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Storing this data as vectors allows for efficient handling and querying, ensuring quick retrieval of relevant information without needing traditional structured database fields <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Scalability**: [[Vector databases]] can scale easily, allowing for continuous addition of data without significant cost increases, especially with proper [[indexing_and_namespace_creation | indexing and namespace creation]] <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Personalization**: They enable [[using_vector_databases_with_ai_agents | AI agents]] to personalize interactions by storing user behavior and preferences as vectors <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This is particularly useful for scenarios like dedicated customer success agents who only access client-specific data <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Adaptive Learning**: [[AI agents]] improve over time as more data is effectively added to the database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## Setting Up Your Vector Database (Pinecone)
The recommended platform for setting up a [[vector database]] is Pinecone, chosen for its cost-effectiveness and ease of setup <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Step-by-Step Setup
1.  **Sign Up/Login**: Go to Pinecone.io and sign up or log in to your account <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
2.  **Create an Index**:
    *   Navigate to the "Create Index" option <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   Give your index a name (e.g., "data") <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
    *   Choose a configuration for embedding. "OpenAI text-embedding-3-small" is recommended as it's effective and the cheapest option offered by OpenAI <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
    *   Select "Serverless" for now <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   Click "Create Index" <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
    *   Once created, the index will show available [[indexing_and_namespace_creation | namespaces]], which can be added later in a coding environment <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## [[data_preparation_and_embedding | Preparing Your Data]]
To ensure immediate usefulness, the [[vector database]] needs to be filled with past data, typically 3 to 6 months' worth <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This often involves:
1.  **Data Capture**: Setting up an automation to pull data (e.g., emails) <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
2.  **Extraction**: Extracting necessary pieces of information from the raw data <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
3.  **Vectorization/Embedding**: Transforming the extracted information into vectors <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
4.  **Adding to Database**: Uploading the embedded vectors to the [[vector database]] <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

> [!INFO] Historical Data
> Filling the database with historical data is crucial for an [[using_vector_databases_with_ai_agents | AI agent]] to be effective from day one <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This is often the most time-consuming part of the setup process <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

When continuously adding data, like new emails, the process involves receiving the email, parsing it down to essential information (name, email, message, subject, date), embedding this information into vectors, and then adding these vectors to the database <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. The information is split into tokens, and each token is assigned a vector <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

## Attaching the Database to an AI Agent (in N8N)
N8N is a no-code automation software used to [[building and deploying AI agents | build AI agents]] and their tools <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

### Building an Agent and Connecting the Database
1.  **Start a Workflow**: Initiate a new workflow in N8N with a manual trigger <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
2.  **Add AI Agent Node**: Select "Advanced AI" then "AI Agent" <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. The "Conversational Agent" type is generally the most effective <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
    *   *Note*: Do not modify the "Human Message" or "System Message" settings within the agent, as they contain hardcoded elements necessary for its function <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
3.  **Add Chat Model**: This model powers the agent's understanding <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. GPT-4o is a suitable choice <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
4.  **Add Memory (Optional)**: "Window Buffer Memory" can be added for chat memory, allowing the agent to recall past messages in a conversation <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.
5.  **Add Vector Store Tool**:
    *   Under "Tools," select "Vector Store Tool" <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
    *   Name the tool (e.g., "database") <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
    *   Provide a descriptive text for the tool, which tells the agent what it's for (e.g., "Call this tool to access your knowledge base. It contains contact information such as email addresses, conversations, account info, etc.") <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
    *   Adjust the "limit" setting, which determines the chunk size of data pulled from the database for a search <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. A larger limit can increase accuracy but may be less cost-efficient <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
6.  **Add Pinecone Vector Store**:
    *   Within the Vector Store Tool, select "Pinecone" <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
    *   **Configure Pinecone Account**: Create a new Pinecone account connection <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
    *   **Retrieve API Key**: Go back to Pinecone, navigate to "API Keys," and copy an existing key or create a new one <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
    *   Paste the API key into N8N and save the connection <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
    *   **Select Index**: Choose the index created earlier (e.g., "data") <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.
    *   **Specify Namespace (Optional but Recommended)**: For specific agents, such as a customer success agent for a particular client, enter the relevant namespace (e.g., the client's account name) <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This ensures the agent only pulls information from that specific data segment <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.
7.  **Add Embedding Model**: This model is responsible for creating the vectors from data <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. Use "OpenAI text-embedding-3-small" <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
8.  **Add Model**: Finally, select a model, such as GPT-4o <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

This completes the basic setup for attaching a [[vector database]] to an [[using_vector_databases_with_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. While the technical setup is quick, the conceptual work of determining how to break up data, which [[indexing_and_namespace_creation | indexes]] to create, and which [[indexing_and_namespace_creation | namespaces]] specific agents need for their functions takes more thought and testing <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.

> [!TIP] Start Simple
> Even if you haven't fully implemented [[indexing_and_namespace_creation | namespaces]] or refined your data types, you can start by adding data and experimenting with the agent's ability to retrieve information <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.

The process of [[building_and_managing_data_workflows_for_ai | data capture]] to keep the database updated and [[data_management_and_prompt_engineering_for_ai_agents | prompt engineering]] for [[AI agents]] are subsequent steps in building effective [[AI agents]] <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.