---
title: FaunaDBs functional query language and API integration
videoId: 2CipVwISumA
---

From: [[fireship]] <br/> 

FaunaDB addresses common database pain points by offering a flexible, scalable, and consistent solution that combines the strengths of SQL and NoSQL databases <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is a serverless cloud database, meaning users only pay for what they use beyond the free tier and don't need to provision infrastructure <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. FaunaDB is easy to use like a document database, scalable, and is the first database to implement the Calvin model for partitioned database systems <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Critically, it excels at handling complex data modeling use cases often found in [[using_faunadb_for_relational_and_graph_data_modeling | relational, graph, or time series databases]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Key FaunaDB Concepts

*   **Top-Level Databases and Multi-Tenancy**: FaunaDB supports multi-tenancy, allowing a top-level database to have an unlimited number of child databases. This enables scoping data and privileges to specific organizations or teams <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Collections**: Similar to SQL tables or MongoDB/Firestore collections, a collection acts as a folder containing many documents. Queries can be made against collections to filter out desired documents for a frontend UI <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Documents**: Documents are represented as plain JavaScript objects and do not require a rigid structure <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. When a document is created, FaunaDB automatically assigns it a unique ID <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **History and Time-to-Live (TTL)**: FaunaDB retains all changes made to a document over time <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Instead of changing a stored document, it creates a copy with updates and archives the original to history, which is useful for time series data and "time-traveling" through data changes <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. TTL options can automatically delete ephemeral data <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **References**: Each document includes a `ref` property that points to its collection and unique ID <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. References are crucial for joining data across multiple collections, akin to foreign keys in SQL databases <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Fauna Query Language (FQL)

While FaunaDB offers a [[graphql_query_language_and_schema | GraphQL]] API where a schema can be uploaded to automatically create collections and indexes <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, its custom functional query language, FQL, provides deep understanding and flexibility <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. FQL can be executed directly in the Fauna console or via the `fonichel` command-line tool <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Basic FQL Functions

*   **`Get`**: Retrieves a single document based on its reference <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **`Ref`**: Creates a reference by taking a collection and a document ID as arguments <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    ```fql
    Get(Ref(Collection("users"), "document_id")) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
    ```

### Indexes

Indexes allow defining how to query documents from a collection, such as fetching a user by email or username instead of their document ID <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Indexes create a lookup table for quick retrieval based on internal data <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

*   **Terms**: Fields on the document that can be searched <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Values**: Specify which values from the document should be returned by the index, allowing for optimized data retrieval for the UI <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **`Match`**: Used within `Get` or `Paginate` to search across an index <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It takes the index name and an array of search terms <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## API Integration with [[getting_started_with_faunadb_and_nodejs | Node.js]]

To integrate FaunaDB with a [[getting_started_with_faunadb_and_nodejs | Node.js]] application, one can build a REST API using frameworks like Express.

### Setup

1.  **Initialize Project**: Run `npm init -y` to create `package.json` <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
2.  **Install Dependencies**: Install `faunadb` and `express` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
3.  **FaunaDB Client**: Initialize the FaunaDB client using a server secret key obtained from the FaunaDB dashboard's security tab <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Server keys are recommended for server-side authentication, adhering to the principle of least privilege <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    ```javascript
    const faunadb = require('faunadb'); <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
    const q = faunadb.query; <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>
    const client = new faunadb.Client({ secret: 'YOUR_FAUNADB_SERVER_KEY' }); <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>
    ```
4.  **Import FQL Functions**: FQL functions can be imported from the `faunadb.query` namespace and used in JavaScript <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### CRUD Operations with FQL in [[getting_started_with_faunadb_and_nodejs | Node.js]]

*   **Reading a Single Document**: An Express `GET` endpoint can read a document by ID using `client.query(q.Get(q.Ref(q.Collection("tweets"), tweetId)))` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Creating a Document**: A `POST` endpoint uses `q.Create` to add data to a collection. FQL functions like `q.Select` and `q.Match` can be nested to retrieve references (e.g., a user reference) for [[using_faunadb_for_relational_and_graph_data_modeling | relational data modeling]] <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. FaunaDB is 100% ACID compliant, ensuring global consistency even with distributed users <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    ```javascript
    client.query(
        q.Create(q.Collection("tweets"), {
            data: {
                text: "Hello World",
                user: q.Select("ref", q.Get(q.Match(q.Index("users_by_name"), "Bob"))) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
            }
        })
    );
    ```
*   **Querying Multiple Documents**: The `q.Paginate` function returns a set of documents that match a query <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This is often combined with `q.Match` on an index (e.g., `tweets_by_user`) to fetch relevant data <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Advanced FQL Features

*   **FaunaDB Functions**: Reusable FQL code can be extracted into server-side functions in the FaunaDB dashboard <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. These functions are given a name (e.g., `getUser`) and can accept parameters via a `Lambda` function <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. They are called using `q.Call` in [[getting_started_with_faunadb_and_nodejs | Node.js]], making code concise and maintainable, and updates are atomic across the codebase <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    ```javascript
    // FQL Function definition (in FaunaDB dashboard)
    // Query(Lambda("user", Select("ref", Get(Match(Index("users_by_name"), Var("user")))))) <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>

    // In Node.js
    client.query(q.Call(q.Function("getUser"), "Bob")); <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>
    ```
*   **Joins for [[using_faunadb_for_relational_and_graph_data_modeling | Graph Data Modeling]]**: FaunaDB can model complex relationships like a [[using_faunadb_for_relational_and_graph_data_modeling | social graph data model]] (e.g., users following other users) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. A "relationships" collection can store connections with `follower` and `followee` references <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. The `q.Join` function allows combining results from multiple indexes, for example, to get a feed of tweets from followed users <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
    ```javascript
    client.query(
        q.Paginate(
            q.Join(
                q.Match(q.Index("followers_by_followee"), q.Call(q.Function("getUser"), "Bob")), <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>
                q.Index("tweets_by_user") <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>
            )
        )
    );
    ```

FaunaDB's functional query language combined with its robust API integration makes it a powerful choice for modern application development, especially for projects requiring flexible data modeling, strong consistency, and infinite scalability <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.