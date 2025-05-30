---
title: Using vector databases with AI agents
videoId: 50wqKgEHQtc
---

From: [[customaistudio]] <br/> 

[[introduction_to_vector_databases | Vector databases]] serve as the contextual master database for [[building_and_deploying_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. They provide a knowledge base of information that is constantly updated with business data, enabling agents to accurately, reliably, and quickly complete tasks, objectives, or workflows <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This process can be achieved without coding <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, and the way they are set up ensures agents work as expected <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

The article will cover an overview of [[introduction_to_vector_databases | vector databases]], why they are used, [[setting_up_a_vector_database | setting up a vector database]] from scratch, preparing data for it, and attaching it to an [[building_and_deploying_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Overview of [[introduction_to_vector_databases | Vector Databases]]

[[introduction_to_vector_databases | Vectors]] are numerical representations of data <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For example, a sentence like "[[building_and_deploying_ai_agents | AI agents]] are powerful" might be converted into a 300-dimensional vector, where each dimension represents a feature of the sentence <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Text is broken down by tokens (approximately four characters per word) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, and each token is then vectorized by attaching a number to it <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. These numbers are placed in a multi-dimensional database, similar to a graph, where each vector is related to others <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

When performing similarity searches, the system looks for vectors that are closely related in this multi-dimensional space <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. These vectors are not just numbers; they have words attached to them, which the [[building_and_deploying_ai_agents | agent]] can read to pull necessary information <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Indexing and Namespaces

To efficiently retrieve data, it must be properly indexed and structured with appropriate namespaces <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This ensures that when an [[building_and_deploying_ai_agents | agent]] queries the database, it does so accurately and efficiently, pulling relevant batches of information <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

*   **Indexing**: Allows searching through large sets of [[introduction_to_vector_databases | vectors]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Different types of data can be broken down into different indexes <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. For instance, contact information is often in its own index <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Namespaces**: Within a larger index (e.g., "projects"), namespaces can be created for individual subcategories, like specific project names <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This allows for filtering data related to a particular client or project <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. New data, such as emails about a specific project, can be added to its dedicated namespace <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This structure enables searching across various projects by querying the main index or narrowing down to specific project details by querying a namespace <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Why [[using_vector_databases_for_ai_agent_tasks | Use Vector Databases]] with [[building_and_deploying_ai_agents | AI Agents]]?

[[using_vector_databases_for_ai_agent_tasks | Vector databases]] offer several benefits for [[understanding_and_implementing_ai_agents_in_businesses | AI agents]]:

*   **Contextual Understanding**: Agents gain a contextual understanding of user requests <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. They can query stored data points like past emails, calendar events, or documents to identify the correct context based on similarity, ensuring accurate responses <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This eliminates the need for massive prompts with all necessary context every time <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Semantic Search**: Unlike traditional keyword-based searches, [[introduction_to_vector_databases | vector databases]] enable semantic search, allowing [[building_and_deploying_ai_agents | AI]] to understand the meaning and intent behind a query, similar to how a human would <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This is crucial when keywords might not be explicitly coded <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Unstructured Data Storage**: [[building_and_deploying_ai_agents | AI agents]] frequently deal with unstructured data like emails, calendar events, chat logs, and documents <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Storing this data as [[introduction_to_vector_databases | vectors]] allows agents to handle and query it efficiently, ensuring quick retrieval of relevant information without requiring specific fields or column names <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Agents are adept at reading and extracting information from "a wall of text" <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Scalability**: Data can be continually added to [[introduction_to_vector_databases | vector databases]] without significant cost increases, especially when properly indexing and using namespaces <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This eliminates concerns about token limits as data grows <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Personalization**: [[building_and_deploying_ai_agents | AI agents]] can personalize interactions based on users' previous behavior and preferences stored as [[introduction_to_vector_databases | vectors]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This leads to more tailored and relevant experiences <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. For example, a customer success agent can be given access only to a specific client's namespace, containing all relevant project, contact, and account information for that client <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Adaptive Learning**: [[building_and_deploying_ai_agents | AI agents]] can continue to improve over time, especially as more data is effectively added to the database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## [[setting_up_a_vector_database | Setting Up a Vector Database]] (Pinecone Example)

The process of [[setting_up_a_vector_database | setting up a vector database]] is straightforward and quick, taking only a few minutes <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Pinecone is a recommended choice due to its cost-effectiveness and ease of setup <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

1.  **Sign Up**: Go to Pinecone.io and create an account <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
2.  **Create an Index**:
    *   Navigate to the "Create Index" option <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   Give the index a name (e.g., "data") <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
    *   Select a configuration. The recommended choice is OpenAI's `text-embedding-3-small` due to its effectiveness and cost-efficiency <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
    *   Choose "Serverless" for the environment <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   Click "Create Index" <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
3.  **Namespaces**: Once the index is created, namespaces can be added to break down the database into smaller segments <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. This allows for organizing data by contact information, account information, projects, or internal team data <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Adding namespaces usually requires a coding environment <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
4.  **API Key**: An API key will be needed later for integration <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. It can be found under "API keys" and created if needed <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>.

## [[data_management_and_prompt_engineering_for_ai_agents | Preparing Your Data]]

To make the database immediately useful, it needs to be filled with past data, typically 3 to 6 months' worth <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This is often the longest part of the setup process <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

An automation is typically set up to pull data, such as emails, from the past six months <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The relevant pieces of this data are extracted, vectorized (embedded), and then added to the database <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

An example automation workflow using N8N for continuous data addition is:
1.  Receive a new email <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
2.  Extract and parse only the necessary information (name, email, message, subject line, date sent) <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
3.  Embed this information (transform it into [[introduction_to_vector_databases | vectors]]) <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. This involves splitting information into tokens and attaching a vector (number) to each token <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
4.  Add the embedded data to the [[introduction_to_vector_databases | vector database]] <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

## [[integrating_ai_agents_with_business_tools | Attaching to Your Agent]]

To integrate the [[introduction_to_vector_databases | vector database]] with an [[building_and_deploying_ai_agents | AI agent]], N8N, a no-code automation software, can be used <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

1.  **Select AI Agent**: Choose the "Advanced [[building_and_deploying_ai_agents | AI]]" node and then "[[building_and_deploying_ai_agents | AI agent]]" <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. The "Conversational [[building_and_deploying_ai_agents | agent]]" type is recommended <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
2.  **Add Chat Model**: This model powers the agent <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. GPT-4o is a suitable choice <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. Memory (like window buffer memory for chat history) can also be added <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.
3.  **Add Vector Store Tool**:
    *   Under "Tools," select "Vector Store Tool" <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
    *   Give it a name (e.g., "database") <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
    *   Provide a clear description that informs the agent of the tool's purpose (e.g., "Call this tool to access your knowledge base. It contains contact information such as email addresses, conversations, account info, etc.") <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
    *   Adjust the "limit" parameter, which determines the chunk size of data the agent pulls during retrieval <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. A larger limit is generally more accurate, though potentially less cost-efficient <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
4.  **Connect Vector Store**:
    *   Select Pinecone as the [[introduction_to_vector_databases | vector database]] <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
    *   Configure the Pinecone account by providing the API key retrieved earlier <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
    *   Select the created index (e.g., "data") <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.
    *   Specify the desired namespace if the agent should only pull information from a specific segment (e.g., a client's account name for a customer success agent) <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.
5.  **Add Embedding Model**: This model is responsible for creating [[introduction_to_vector_databases | vectors]] from the data <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. Use the same model chosen during index creation, such as `text-embedding-3-small` <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.
6.  **Add Model for Embedding**: Select the main language model, e.g., GPT-4o <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

## Key Considerations

While the physical setup of the [[introduction_to_vector_databases | vector database]] is quick, the critical aspects involve:
*   How data is broken up <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
*   Which indexes to create <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
*   Which namespaces to create within indexes <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   Which specific indexes and namespaces are needed for different [[building_and_deploying_ai_agents | agent]] functions <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

Starting by simply adding data and allowing the [[building_and_deploying_ai_agents | agent]] to retrieve information is a good approach <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.

## Next Steps

Future videos will cover [[data_management_and_prompt_engineering_for_ai_agents | data capture]] (ensuring continuous data addition to the database) <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a> and [[data_management_and_prompt_engineering_for_ai_agents | prompt engineering]] for [[building_and_deploying_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. A full step-by-step tutorial for [[building_and_deploying_ai_agents | building a personal AI agent]] will follow, assuming the [[introduction_to_vector_databases | vector database]] and initial [[data_management_and_prompt_engineering_for_ai_agents | data capture]] are already handled <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.