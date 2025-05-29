---
title: Using Couchbase for vector storage and search
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

Couchbase serves as a powerful NoSQL distributed database that also supports vector storage and search, making it a suitable choice for applications requiring efficient similarity searches, such as [[retrieval_augmented_generation_application_development | Retrieval Augmented Generation application development]] (RAG) <a class="yt-timestamp" data-t="01:23:05">[01:23:05]</a>.

## Role in a RAG Application Example

In a demonstration application designed to find similar Star Wars planets, Couchbase acts as the primary database <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.

### Data Storage

The application stores approximately 30 documents, each representing a Star Wars planet <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Each document contains details about a specific planet, such as its rotation period and orbital period <a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>. Crucially, these documents also store embeddings, which are numerical representations of the planet's characteristics <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. These embeddings, with a dimension of 1500, are generated using OpenAI's embedding models (e.g., `text-embedding-ada-002`) and are pre-stored in Couchbase alongside the planet data <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>, <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.

### Vector Search Functionality

When a user searches for planets similar to a given one (e.g., Alderaan), Couchbase's vector search capabilities are leveraged:

1.  **Query Embedding Generation**: The user's input query is first converted into an embedding using an OpenAI embedding model <a class="yt-timestamp" data-t="05:01:04">[05:01:04]</a>.
2.  **Nearest Vector Search**: Couchbase performs a vector search using the `C_VectorSearch` functionality <a class="yt-timestamp" data-t="05:28:09">[05:28:09]</a>. This process identifies the set of vectors (and thus, documents/planets) within the database that are closest to the input query embedding <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>. The principle behind this is that if two embeddings are numerically close, their real-world features are also closely related <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
3.  **Retrieval of Relevant Documents**: The search returns a list of planets whose embeddings are the closest match to the input query <a class="yt-timestamp" data-t="05:57:09">[05:57:09]</a>. These "relevant documents" are then used to populate the search results displayed to the user <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

For instance, when asked to "find planets similar to Alderaan," Couchbase's vector search identifies planets like Endor and Yavin IV based on their embedding similarity <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

## Integration Details

Connecting to Couchbase involves providing a connection string, username, and password <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. The application initiates its Couchbase connection in the `server.ts` file <a class="yt-timestamp" data-t="04:16:05">[04:16:05]</a>. The core logic for performing the vector search, specifically the `getRelevantDocuments` function, resides in the `index.tsx` file <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. This function defines the index name and embedding length required for the vector search request <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

Couchbase's role as a vector store is integral to the RAG application's ability to retrieve contextual information, which is then passed to a large language model for generating responses <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>, <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.