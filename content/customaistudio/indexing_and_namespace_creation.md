---
title: Indexing and namespace creation
videoId: 50wqKgEHQtc
---

From: [[customaistudio]] <br/> 

[[introduction_to_vector_databases | Vector databases]] serve as the contextual master database for [[using_vector_databases_for_ai_agent_tasks | AI agents]], providing a knowledge base of constantly updated information essential for accurate, reliable, and quick task completion <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. To effectively manage and retrieve this data, particularly in [[nocode_ai_platforms_for_building_agents | no-code environments]], proper indexing and the creation of namespaces are crucial <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## What are Vectors and Vector Databases?
Vectors are numerical representations of data <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For example, a sentence like "AI agents are powerful" might be converted into a 300-dimensional vector, with each dimension representing a feature of the sentence <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This process involves breaking down text into tokens (e.g., four characters in a word), vectorizing each token by attaching a number, and then placing these numbers in a multi-dimensional database where they are related to each other <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. [[using_vector_databases_for_chatbots | Similarity searches]] in these databases look for vectors closely related in multi-dimensional space, pulling up batches of related words that the [[using_vector_databases_with_ai_agents | AI agent]] can read and extract information from <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Structuring Data with Indexes and Namespaces
To retrieve data efficiently and accurately, it's essential to index it properly and create appropriate namespaces <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This structure ensures that when an agent queries the database, it pulls the exact information needed <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Indexes
Indexing allows for searching through large sets of vectors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Data can be broken down into different indexes based on its type <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Example:** For agents primarily retrieving contact information (e.g., finding an email address to send an email), a specific "contacts" index can be created <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Another index could be for "projects" containing all information about various ongoing projects <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Namespaces
Namespaces break down a database into smaller chunks or segments within a larger index <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Example: Customer Success Agents:** If creating a customer success agent for each client, a namespace could be created specifically for each client, typically named after the client <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. All data related to that specific client (project information, contact information, account information) would be added to their dedicated namespace within the broader index (e.g., "client information" index) <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This way, the agent for a particular client only accesses data relevant to them <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Example: Project Management:** Within a "projects" index, individual namespaces can be created for each specific project <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. As new data, like emails about a specific project, comes in, it's added to that project's namespace inside the larger "projects" index <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   If searching for information across *all* projects (e.g., "Which projects have a due date coming up on Friday?"), the agent can search the entire index <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   If asking about a *specific* project (e.g., "What was the last milestone for the XYZ project?"), the agent can specifically search that project's namespace within the index <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Benefits of Indexing and Namespaces
Using indexes and namespaces offers several advantages for [[using_vector_databases_with_ai_agents | AI agents]]:

*   **Contextual Understanding:** Agents gain a deeper contextual understanding of user requests without requiring massive, repetitive prompts <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. They can query across stored data points (emails, calendar events, documents) to identify the correct context based on similarity <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Efficiency and Accuracy:** Properly structured data allows agents to pull information accurately and efficiently <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Personalization:** By creating client-specific namespaces, AI agents can personalize interactions based on user behavior and preferences, providing more tailored experiences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This is particularly useful for applications like customer success, where each client can have their own agent with access only to their relevant data <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Scalability:** With proper indexing and namespaces, [[setting_up_a_vector_database | vector databases]] can scale easily over time, allowing for the addition of more data without concerns about token limits <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Setting Up Namespaces in Pinecone
When [[setting_up_a_vector_database | setting up a vector database]] in a platform like Pinecone, you create an index first <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. While namespaces can be seen, their creation typically occurs in a coding environment <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. The choice of namespaces depends on the specific use case, breaking down the database into logical segments like contact information, account information, projects, or internal team data <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

For attaching the database to an [[using_vector_databases_with_ai_agents | AI agent]], especially in a [[nocode_ai_platforms_for_building_agents | no-code platform]] like NocoDB, you select the created index and can specify a particular namespace <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>. This ensures that the agent primarily pulls information from that specific, relevant namespace <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Key Considerations
While setting up the database itself is relatively quick (a few minutes), the more time-consuming and critical aspect is determining how data should be broken up, which indexes to create, and which namespaces within those indexes are necessary for the specific functions of different agents <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. Starting with a basic setup and then refining the indexing and namespace strategy as you test and expand the agent's capabilities is a recommended approach <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. Future improvements can then focus on [[data_management_and_prompt_engineering_for_ai_agents | data capture]] for consistent updates and refining prompt engineering for agents <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.