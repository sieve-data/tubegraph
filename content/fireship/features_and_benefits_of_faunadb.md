---
title: Features and benefits of FaunaDB
videoId: 2CipVwISumA
---

From: [[fireship]] <br/> 

FaunaDB is presented as a cloud database designed to address common pain points encountered during application development, specifically regarding database choices <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It aims to bridge the gap in the traditional [[comparison_of_sql_and_nosql_databases | SQL versus NoSQL]] debate by offering a database that combines the strengths of both <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Core Characteristics

### Serverless and Cost-Effective
FaunaDB is entirely serverless, meaning developers do not need to provision any infrastructure <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Beyond its free tier, users only pay for the resources they actually consume <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Scalability and Performance
The database is described as extremely fast and capable of scaling infinitely in the cloud <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It is also noted as the first database in the world to implement the Calvin model for partitioned database systems, which contributes to its performance characteristics <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### [[using_faunadb_for_relational_and_graph_data_modeling | Advanced Data Modeling Capabilities]]
A significant feature of FaunaDB is its ability to handle complex [[using_faunadb_for_relational_and_graph_data_modeling | data modeling]] use cases that are typically found in relational, graph, or time series databases <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This flexibility allows for modeling relationships, such as a user having many tweets, or users following each other, similar to a social graph <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Multi-Tenancy Support
FaunaDB supports multi-tenancy, allowing a top-level database to have an unlimited number of child databases <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This feature enables scoping data and privileges to specific organizations or teams <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Data Management Features

### Collections and Documents
FaunaDB organizes data into collections, which are analogous to SQL tables or collections in other document-oriented databases like MongoDB or Firestore <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Collections act like folders containing many documents, against which queries can be made to filter sets of documents <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

Documents are represented as plain JavaScript objects, and their data does not require a rigid structure <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. FaunaDB automatically assigns a unique ID to each document and includes a `ref` property that points to its collection and unique ID, which is crucial for joining data across multiple collections, akin to a foreign key in SQL <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### History and Time Travel
A unique aspect of FaunaDB is its history feature, which retains all changes made to a document over time <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. When a document is written, FaunaDB creates a copy with the changes and archives the original, making it extremely useful for working with time series data and for "time traveling" through data changes <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Time To Live (TTL)
Collections offer a Time To Live (TTL) option, allowing for the automatic deletion of ephemeral data that is no longer needed <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Querying and APIs

### Native GraphQL Support
FaunaDB provides native GraphQL support. Developers can upload a GraphQL schema to FaunaDB, and it will automatically create the necessary collections and indexes for data retrieval based on that schema <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### [[faunadbs_functional_query_language_and_api_integration | Fauna Query Language (FQL)]]
[[faunadbs_functional_query_language_and_api_integration | Fauna Query Language (FQL)]] is FaunaDB's custom, functional query language <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. It is described as intuitive and flexible, and can be executed directly from the FaunaDB console, the Fonichel command-line tool, or integrated into [[getting_started_with_faunadb_and_nodejs | Node.js]] applications <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. FQL allows for composing multiple functions, conceptually similar to component composition in UI frameworks <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

Common FQL functions mentioned include:
*   `Get`: Retrieves a single document based on a reference <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   `Ref`: Creates a reference to a document within a collection <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   `Match`: Searches across an index <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   `Select`: Selects a specific value from a document <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   `Create`: Creates a new document <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   `Paginate`: Returns a set of documents matching a query <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   `Join`: Joins two indexes or sets of data <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### Indexes for Efficient Queries
Indexes provide a mechanism to define how documents are queried from a collection, allowing for fetching documents based on internal data fields like email addresses or usernames rather than just document IDs <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Indexes create a lookup table for quick retrieval and can be configured to return specific values from a document instead of just the document reference <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Server-Side Functions
FaunaDB allows developers to create server-side functions by extracting FQL code <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. These functions can be used across any server or platform, ensuring atomic updates throughout the codebase if the function definition is changed. This promotes concise and maintainable code <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

## Transactional Guarantees
FaunaDB is 100% ACID (Atomicity, Consistency, Isolation, Durability) compliant <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This means that database transactions are globally consistent, and all future reads will reflect the value of a write, even when distributed across thousands of users worldwide <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

## Security and Access Control
The FaunaDB dashboard provides tools to implement fine-grained access control, allowing developers to grant access based on the principle of least privilege, ensuring only the bare minimum set of operations are allowed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Integration
FaunaDB offers a [[getting_started_with_faunadb_and_nodejs | Node.js]] client library, enabling developers to interact with the database using their own custom code, for example, by building a simple REST API with Express.js <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

FaunaDB is presented as a powerful and flexible database solution suitable for new projects, offering a compelling alternative in the database landscape <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.