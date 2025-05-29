---
title: Couchbase as a distributed NoSQL database
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

Couchbase is highlighted as a robust and powerful NoSQL database that offers distributed capabilities and support for vector storage and search functionalities <a class="yt-timestamp" data-t="01:23:05">[01:23:05]</a>. It is a key component in a [[retrieval_augmented_generation_application | retrieval augmented generation application]] built using Hono.js, Nebius AI, and Cloudflare <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Key Features and Capabilities

*   **Distributed NoSQL Database**: Couchbase is described as a "powerful NoSQL distributed NoSQL database" <a class="yt-timestamp" data-t="01:23:05">[01:23:05]</a>.
*   **Vector Store and Vector Search Support**: A significant feature of Couchbase is its built-in support for vector store and vector search <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This enables the database to store and efficiently query embeddings <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Role in the Retrieval Augmented Generation (RAG) Application

In the demonstrated Star Wars-themed application, Couchbase serves as the main database <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

### Data Storage
The application stores approximately 30 documents within Couchbase, with each document containing details about a specific Star Wars planet, such as rotation period, orbital period, and importantly, pre-generated embeddings <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. These embeddings, generated using OpenAI's `text-embedding-ada-002` model <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>, have a dimension of 1500 <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### Vector Search for Similarity
Couchbase's vector search capability is crucial for finding planets similar to a user's query <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
The process involves:
1.  Converting the user's input query (e.g., "find planets similar to Alderant") into an embedding using an OpenAI embedding model <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.
2.  Utilizing Couchbase's `vector_search` functionality to find the nearest vectors to the input query embedding <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. The application specifies an index name and the embedding length (1500) for this search <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
3.  The principle of vector search dictates that if two embeddings are closer to each other, their real-world features are also closer <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Therefore, Couchbase identifies the list of planets whose embeddings are the closest to the queried planet <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
4.  These relevant documents (planets) are then populated into the search results and displayed to the user <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

## Integration within the Hono.js Project

Couchbase integration within the Hono.js application is handled primarily through a `server.ts` file and functions within `index.tsx` <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

### Connection
The `server.ts` file is responsible for initiating the Couchbase connection <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. It includes functions to connect to the Couchbase cluster, requiring a connection string, username, and password <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. This connection is then used by the Hono application <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

### `getRelevantDocuments` Function
A key function, `getRelevantDocuments`, is defined to perform the vector search <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. This function takes the user's input question, converts it to an embedding using OpenAI, and then uses Couchbase's vector search to find relevant documents <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

This [[external_tool_and_database_integration_with_nebius_ai_and_couchbase | integration of Couchbase]] allows the application to act as a backend, providing a server-like experience without needing a dedicated Node.js server <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.