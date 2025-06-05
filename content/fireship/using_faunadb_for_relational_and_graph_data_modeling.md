---
title: Using FaunaDB for relational and graph data modeling
videoId: 2CipVwISumA
---

From: [[fireship]] <br/> 

When building an application, managing a database is a common challenge, with debates often arising between [[comparison_of_sql_and_nosql_databases | SQL versus NoSQL]] databases [00:00:03]. [[Features and benefits of FaunaDB | FaunaDB]] is presented as a cloud database designed to address these challenges [00:00:17]. It is entirely serverless, meaning no provisioning is required, and users only pay for what they use beyond the free tier [00:00:20]. FaunaDB is designed to be as user-friendly as a document database, with data management possible via a web interface or command line [00:00:25]. It is noted for its extreme speed and infinite scalability in the cloud [00:00:30].

## Key Features and Concepts

FaunaDB is the first database globally to implement the Calvin model for partitioned database systems [00:00:33]. A key strength is its ability to handle complex data modeling use cases, similar to those found in relational, graph, or time series databases [00:00:38].

### Core Database Structure

*   **Top-Level Databases**: FaunaDB supports multi-tenancy, allowing a database to have an unlimited number of child databases. This enables scoping data and privileges to specific organizations or teams, though a single database is usually sufficient for an application [00:01:20].
*   **Collections**: Similar to an SQL table or collections in [[Using Firebase databases and data modeling techniques | document-oriented databases]] like MongoDB or [[Firestore data modeling techniques | Firestore]], a collection acts like a folder containing multiple documents [00:01:39]. Queries can be made against a collection to filter a set of documents for a frontend UI [00:01:50]. Collection names are typically plural [00:01:55].
*   **Documents**: A document is represented as a plain JavaScript object [00:02:32]. Data saved in a document does not require a rigid structure, but querying multiple documents relies on consistent key names [00:02:35]. Each document is automatically assigned a unique ID [00:02:54] and includes a `ref` property that points to its collection and unique ID [00:03:01]. This `ref` property is crucial for [[normalized_data_models_and_document_joining_in_firestore | joining data]] across multiple collections, akin to a foreign key in an SQL database [00:03:06].
*   **History and Time To Live (TTL)**: FaunaDB retains all changes to a document over time [00:02:05]. Instead of changing a stored document, it creates a copy with changes and archives the original to history, which is useful for time-series data and time-traveling through data changes [00:02:09]. A TTL option allows automatic deletion of ephemeral data [00:02:23].

### [[FaunaDBs functional query language and API integration | Data Access and Querying with FQL]]

FaunaDB offers multiple native APIs, including GraphQL, where uploading a schema can automatically create collections and indexes [00:03:27]. However, understanding FaunaDB's custom query language, **FQL (Fauna Query Language)**, is recommended [00:03:48]. FQL is a functional language that can be executed from the console, the `faunash` CLI, or in Node.js [00:03:50].

*   **`Get` Function**: Retrieves a single document based on its reference [00:04:12]. It takes a reference (created with the `ref` function, which uses a collection and document ID) as an argument [00:04:18].
*   **Indexes**: Indexes define how documents can be queried from a collection [00:04:45]. They provide a lookup table to quickly retrieve documents based on internal data, such as an email address or username, instead of the document ID [00:04:50]. An index can specify `terms` (fields to be searched) and `values` (specific data from the document to be returned) [00:05:08].
*   **`Match` Function**: Used inside `Get` (or `Paginate`) to search across an index [00:05:40]. It takes the index name as the first argument and an array of search terms as the second [00:05:44].

### [[Getting started with FaunaDB and Nodejs | Getting Started with Node.js]]

A simple REST API can be built with Express to read and write data in FaunaDB [00:06:03]. To connect, the `faunadb` NPM package is used, and a FaunaDB client is initialized with a secret server key obtained from the FaunaDB dashboard's security tab [00:06:28]. FaunaDB also supports fine-grained access control to adhere to the principle of least privilege [00:07:11]. FQL functions are imported into JavaScript from the `faunadb` query namespace for interaction with the database [00:07:46].

## Relational Data Modeling (One-to-Many)

To model a one-to-many relationship, such as a user having many tweets, a `tweet` document needs to reference the `user` document [00:09:59].

*   **Creating Documents**: The `create` function is used, pointing to the desired collection and passing in custom data [00:10:15]. This data can include regular JavaScript values or results from FQL functions that query the database [00:10:22].
*   **Referencing Related Data**: To link a tweet to a user, the user field within the tweet document can be a reference to a user document [00:10:30]. The `select` function can be used to extract a specific value (like a reference) from a document [00:10:37]. For instance, an index like `users_by_name` can be used to get a user's reference from their username [00:10:47]. This allows modeling relational data similarly to an SQL database with foreign keys [00:11:00].
*   **ACID Compliance**: FaunaDB is 100% ACID compliant, ensuring that database transactions are globally consistent; all future reads will reflect the value of the write, even across distributed users [00:11:05].
*   **Retrieving Multiple Documents**: The `paginate` function is used instead of `get` to return a set of documents that match a query [00:12:07]. To query tweets by a specific user, an index like `tweets_by_user` on the user reference field in the tweets collection is created [00:11:46]. The `values` option in the index can be used to return only specific fields (e.g., tweet text) for efficiency [00:11:56].

### FaunaDB Functions

Functions in FaunaDB allow for the extraction and reuse of FQL code across different servers or platforms [00:12:37]. This helps keep code concise and maintainable [00:13:48]. For example, a `getUser` function can be created to encapsulate the logic for retrieving a user's reference by name, using a `lambda` function to accept arguments [00:12:51]. This function can then be called from the Node.js application, with FaunaDB executing it remotely and atomically updating it if the code changes [00:13:50].

## Graph Data Modeling (Many-to-Many)

Modeling a social graph, where users can follow each other (a many-to-many relationship), involves creating a collection for `relationships` [00:13:57].

*   **Relationships Collection**: Each document in this collection represents an edge in the graph, containing a `follower` and a `followee`, both of which are user document references [00:14:12]. This creates a one-way graph where a follower points to the followed user [00:14:25].
*   **Creating Relationships**: A new endpoint creates the relationship document in the `relationships` collection, populating the `follower` and `followee` fields with user references obtained via the `getUser` function [00:14:30].
*   **Querying Interconnected Data with `Join`**: To get all accounts followed by a user, and then all tweets owned by those accounts (a feed), the `join` function is used [00:15:02].
    *   First, an index like `followers_by_followee` is created, which takes the followee's user reference and returns all accounts that user is following [00:15:15].
    *   The `join` function takes two arguments: the initial query (e.g., all users followed by "bob" using the `followers_by_followee` index) and the index to join with (e.g., `tweets_by_user`) [00:15:35]. This allows retrieving data from multiple interconnected indexes [00:15:50].

FaunaDB's capabilities make it a strong contender for the tech stack when starting new projects, especially for its handling of complex data models [00:16:15].