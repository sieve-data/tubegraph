---
title: Introduction to vector databases
videoId: 50wqKgEHQtc
---

From: [[customaistudio]] <br/> 

Vector databases serve as a contextual master database for [[using_vector_databases_with_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Their primary function is to provide [[AI agents | AI agents]] with a constantly updated knowledge base of information relevant to a business, enabling them to complete tasks, objectives, and workflows accurately, reliably, and quickly <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Many implementations of vector databases can be done without coding <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## What Are Vectors and Vector Databases?

Vectors are numerical representations of data <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For instance, a sentence like "AI agents are powerful" might be converted into a 300-dimensional vector, where each dimension represents a feature of the sentence <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The process involves:
1.  **Tokenization** Text is broken down into tokens, typically around four characters per word <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  **Vectorization** Each token is assigned a number, effectively turning information into vectors <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  **Storage** These numbers are placed in a multi-dimensional database, often visualized as a graph, where each vector (number) is related to others <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

When performing similarity searches, the system looks for vectors that are closely related in this multi-dimensional space, pulling up batches of words or data that are relevant <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The [[AI agents | agent]] then reads these words to extract the needed information <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Indexing and Namespaces
To effectively retrieve data, vectors must be properly indexed and organized with appropriate namespaces <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This structuring ensures accurate and efficient data retrieval by [[AI agents | AI agents]] <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

*   **Indexing** Allows searching through large sets of vectors by breaking down different types of data into distinct indexes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For example, contact information for emails might be in one index <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Another index could be for "projects," containing all information about various ongoing projects <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Namespaces** Further segment data within an index, allowing for finer-grained organization <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. For instance, within a "projects" index, individual namespaces can be created for each specific project <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This allows [[AI agents | agents]] to search across all projects (index) or focus on data related to a specific project (namespace) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Why Use Vector Databases?

Vector databases offer several key advantages for [[AI agents | AI agents]]:

*   **Contextual Understanding** <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>: They provide [[AI agents | agents]] with the ability to understand user requests in context <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. For example, if a user asks to "schedule a meeting with John," the [[AI agents | agent]] can query stored data (emails, calendar events, documents) to identify the correct "John" based on similarity, ensuring accurate responses <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This eliminates the need for massive prompts containing all necessary context <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Semantic Search** <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>: Unlike traditional keyword searches, vector databases enable semantic search, allowing [[AI agents | agents]] to understand the meaning and intent behind a query, even if specific keywords aren't used <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This mimics human understanding of complex or descriptive queries <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Unstructured Data Storage** <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>: [[AI agents | AI agents]] frequently interact with unstructured data like emails, calendar events, chat logs, and documents <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Storing this data as vectors allows for efficient handling and querying without needing to structure it into tables with predefined fields, which is often difficult for [[AI agents | agents]] to process via traditional SQL searches <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. [[AI agents | Agents]] are more adept at extracting information from large blocks of unstructured text <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Scalability** <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>: Vector databases are designed to scale easily, allowing for continuous addition of data without significant cost increases, especially when properly indexed and utilizing namespaces <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This avoids issues like token limits that arise from continuously expanding prompts <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Personalization** <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>: By storing user behavior and preferences as vectors, [[AI agents | AI agents]] can personalize interactions, providing tailored and more relevant experiences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. For example, a customer success [[AI agents | agent]] could have access only to a specific client's namespace, containing only data relevant to that client, ensuring highly personalized support <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Adaptive Learning** <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>: [[AI agents | Agents]] can continually improve their performance over time as more relevant data is added to the database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## [[setting_up_a_vector_database | Setting up a Vector Database]]

The process of [[setting_up_a_vector_database | setting up a vector database]] can be relatively quick and straightforward <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

### Choosing a Platform
Pinecone is a recommended platform due to its ease of use and cost-effectiveness <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Other options include Superbase and Zep <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### Steps for Setup (e.g., in Pinecone):
1.  **Sign Up** Create an account on the chosen platform <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
2.  **Create an Index** In Pinecone, this involves creating a new index (e.g., named "data") <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
3.  **Configuration** Select an embedding model, such as OpenAI's `text-embedding-3-small`, which is noted for being cost-effective and efficient <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. Choose a serverless option if available <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
4.  **API Key** Obtain an API key from the platform, which will be used to connect the database to [[AI agents | AI agents]] or other tools <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
5.  **Namespaces (Optional but Recommended)** While not set up directly in the UI, namespaces can be defined programmatically to logically segment data within the index <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. This allows for breaking down the database into smaller chunks based on data type (e.g., contact info, account info, projects, team data) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## [[data_preparation_and_embedding | Data Preparation and Embedding]]

For an [[AI agents | agent]] to be effective from day one, the vector database needs to be pre-filled with past data, typically three to six months' worth <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

The [[data_preparation_and_embedding | data preparation and embedding]] process generally involves:
1.  **Data Extraction** Pulling relevant data from sources, such as emails over the past six months <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This is often the most time-consuming part <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
2.  **Parsing/Filtering** Extracting only the necessary pieces of data (e.g., name, email, message, subject line, date) and discarding unnecessary metadata <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
3.  **File Conversion** Converting the extracted raw data into a file format, typically a text file, before it can be added to the database <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
4.  **Embedding** The information is split into tokens, and each token is then transformed into a vector (number) <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
5.  **Adding to Database** The vectorized data is then added to the database <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

Automations can be set up to continually add new data to the database, ensuring it remains up-to-date <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

## [[integrating_ai_agents_with_business_tools | Integrating AI Agents with Business Tools]]

[[integrating_ai_agents_with_business_tools | Integrating AI agents with business tools]] involves connecting the vector database to the [[AI agents | agent]]'s environment, such as n8n (a no-code automation software) <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

Steps to integrate:
1.  **Agent Type Selection** Choose a suitable [[AI agents | agent]] type, with "Conversational Agent" often being the most effective <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
2.  **Chat Model** Select the underlying language model that powers the [[AI agents | agent]], such as GPT-4o <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.
3.  **Memory (Optional)** Add chat memory (e.g., Window Buffer Memory) to allow the [[AI agents | agent]] to recall past messages in a conversation <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.
4.  **Add Vector Store Tool** Connect the vector database via a "Vector Store Tool" <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
    *   **Name & Description** Give the tool a descriptive name (e.g., "database") and a clear description that informs the [[AI agents | agent]] of its purpose (e.g., "Call this tool to access your knowledge base. It contains contact information such as email addresses, conversations, account info, etc.") <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.
    *   **Limit** Set the retrieval limit, which determines the size of the data chunk the [[AI agents | agent]] pulls for a search <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. A larger limit can increase accuracy, though potentially at a higher cost <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
5.  **Connect Pinecone** Link the specific Pinecone account using its API key <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
6.  **Select Index & Namespace** Choose the relevant index (e.g., "Data") and specify a namespace if the [[AI agents | agent]] is dedicated to a particular segment of data (e.g., a specific client's account name for a customer success [[AI agents | agent]]) <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.
7.  **Embedding Model** Add the embedding model used to create the vectors (e.g., `text-embedding-3-small`) to the agent's configuration <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.

While the physical setup of the database and its connection to the [[AI agents | agent]] is quick, significant planning is required to determine how data will be broken down into indexes and namespaces, and which [[AI agents | agents]] need access to specific data segments for their functions <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. This strategic decision-making around [[indexing_and_namespace_creation | indexing and namespace creation]] is crucial for effective [[AI implementation strategies | AI implementation strategies]] <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.