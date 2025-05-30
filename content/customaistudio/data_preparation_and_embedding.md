---
title: Data preparation and embedding
videoId: 50wqKgEHQtc
---

From: [[customaistudio]] <br/> 

[[using_vector_databases_for_ai_agent_tasks | Vector databases]] are crucial for [[AI implementation strategies | AI agents]], serving as their contextual master database or knowledge base <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This knowledge base needs to be constantly updated with business information to enable agents to complete tasks accurately, reliably, and quickly <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Overview of Vectors and Data Conversion

Vectors are numerical representations of data <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For example, a sentence like "AI agents are powerful" can be converted into a multi-dimensional vector, where each dimension represents a feature of the sentence <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The process of converting text to vectors involves:
1.  **Tokenization**: Breaking down text into "tokens," which are typically about four characters per word <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  **Vectorization**: Attaching a number (vector) to each token <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  **Placement**: Placing these numbers in a multi-dimensional database, often visualized like a graph, where vectors are related to each other <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
4.  **Retrieval**: When performing similarity searches, the system looks for closely related vectors in this multi-dimensional space <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. These vectors are not just numbers; they have words attached, allowing the agent to read and extract the necessary information <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Structuring Data: Indexing and Namespaces

To efficiently pull data, it must be indexed properly and structured using namespaces <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   **Indexing**: Allows searching through large sets of vectors by breaking down different types of data into separate indexes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For instance, contact information might be one index <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, or a "projects" index could contain all information about various projects <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Namespaces**: Sub-segments within an index that further break down the database into smaller chunks <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. For a customer success agent, a namespace could be created for each client, containing only data related to that specific client (e.g., project information, contact information, account information) <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This allows for personalized experiences where an agent only accesses data relevant to a specific client <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

This hierarchical structure (index > namespace) allows for efficient searching across all data or specific segments <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Why Vector Databases are Used

[[using_vector_databases_for_ai_agent_tasks | Vector databases]] are preferred for several reasons:

*   **Contextual Understanding**: They provide agents with contextual understanding of user requests <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Instead of a massive prompt, the agent can query the database to identify context based on similarity to stored data points like emails, calendar events, or documents <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Semantic Search**: Enables a more human-like understanding of queries compared to traditional keyword-based searches <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. AI agents can understand nuanced requests even if exact keywords aren't present <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Unstructured Data Storage**: Agents often handle unstructured data such as emails, chat logs, and documents <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Storing this data as vectors allows efficient querying without needing to pre-structure it into traditional database fields or columns <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Agents are adept at reading large blocks of text and extracting information from them <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Scalability**: [[using_vector_databases_for_ai_agent_tasks | Vector databases]] can scale easily by adding more data, and they are generally cost-effective, especially when properly indexed and namespaced <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. They also help in avoiding [[data_management_and_prompt_engineering_for_ai_agents | token limits]] as data grows <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Personalization**: [[AI implementation strategies | AI agents]] can personalize interactions by storing user behavior and preferences as vectors, leading to more tailored and relevant experiences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Adaptive Learning**: Agents can continuously improve over time as more data is effectively added to the database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## Preparing Your Data for the Database

To make agents immediately useful, the database needs to be filled with past data, typically 3 to 6 months' worth <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

*   **Initial Data Ingestion**: This is often the most time-consuming part <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. A common approach is to set up [[building_and_managing_data_workflows_for_ai | automation]] to pull emails (e.g., from the past six months), extract necessary pieces of information (like name, email, message, subject line, date sent), vectorize/embed it, and then add it to the database <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Continuous Data Capture**: After initial ingestion, it's vital to have [[building_and_managing_data_workflows_for_ai | automation]] in place to consistently add any new data happening within the business to keep the database up to date <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. For ongoing email additions, information is parsed and then embedded (vectors are created) and added to the vector store <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

## Attaching Data to the AI Agent

In [[tools_and_resources_for_building_ai_agents | no-code automation software]] like N8N, attaching a vector database to an [[AI implementation strategies | AI agent]] involves:

1.  **Setting up the Vector Store Tool**: Within the [[AI implementation strategies | AI agent]]'s configuration, a "Vector Store Tool" is added <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. This tool is given a name (e.g., "database") and a description that informs the agent about its purpose (e.g., "call this tool to access your knowledge base; it contains contact information, email addresses, conversations, account info, etc.") <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
2.  **Configuring the Vector Store**: The specific vector database (e.g., Pinecone) is selected <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>. An API key from the vector database platform is required to connect it <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
3.  **Selecting an Index**: The relevant index (e.g., "Data") created in the vector database is chosen <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. If applicable, a specific namespace can be defined for the agent to access, ensuring it only pulls information from that particular segment <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.
4.  **Adding an Embedding Model**: An embedding model (e.g., OpenAI's text-embedding-3-small) is added. This model is responsible for actually creating the vectors from the raw data that the agent will store and retrieve <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.
5.  **Setting a Limit**: The "limit" defines how much data the agent pulls in a chunk when retrieving information from the database <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. A larger limit can increase accuracy, though it might be less cost-efficient <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

This setup allows the [[AI implementation strategies | AI agent]] to access and leverage its knowledge base for informed decision-making and task completion <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. While the initial setup is quick, the conceptual work of determining how to break up and organize data (indexes, namespaces) is crucial for effective agent function <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.