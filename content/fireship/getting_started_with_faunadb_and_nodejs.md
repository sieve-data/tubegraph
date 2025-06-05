---
title: Getting started with FaunaDB and Nodejs
videoId: 2CipVwISumA
---

From: [[fireship]] <br/> 
One of the primary challenges in app development is managing the database, which often leads to debates between SQL and NoSQL approaches <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. SQL offers safety, security, and consistency, while NoSQL provides flexibility, scalability, and productivity <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. FaunaDB aims to resolve this by combining the strengths of both <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

[[features_and_benefits_of_faunadb | FaunaDB]] is a cloud database that is entirely serverless, meaning no provisioning is required, and users only pay for actual usage beyond the free tier <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It offers the ease of use of a document database, with data management available via its web interface or command line <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. [[features_and_benefits_of_faunadb | FaunaDB]] is designed for extreme speed and infinite scalability in the cloud, being the first database to implement the Calvin model for partitioned database systems <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Crucially, it excels at handling complex data modeling use cases typical of relational, graph, or time series databases <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

This guide will focus on modeling data relationships, such as a user having many tweets, users following each other, and retrieving a feed of tweets from followed users, all implemented using [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Getting Started with FaunaDB

To begin, you'll need a free [[features_and_benefits_of_faunadb | FaunaDB]] account <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Creating a Database

Once logged in, navigate to the [[features_and_benefits_of_faunadb | FaunaDB]] dashboard and create a new database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This is considered a "top-level" database <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. [[features_and_benefits_of_faunadb | FaunaDB]] supports multi-tenancy, allowing a database to have an unlimited number of child databases to scope data and privileges for specific organizations or teams <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. However, for most applications, a single database will suffice <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Collections and Documents

After creating a database, the next step is to create a collection <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

*   **Collections**: Similar to SQL tables or folders, collections store many documents <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. They function like other document-oriented databases such as MongoDB or Firestore <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. When creating a collection, it's typically named in the plural, like "users" to store user data <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   **History Option**: A unique feature in [[features_and_benefits_of_faunadb | FaunaDB]] is the "history" option for collections, which retains all changes to a document over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Instead of altering a stored document, [[features_and_benefits_of_faunadb | FaunaDB]] creates a new copy with changes and archives the original to history <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This is highly beneficial for time series data and "time traveling" through data changes <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   **TTL (Time to Live)**: Collections can also have a TTL option to automatically delete ephemeral data after a specified period <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Documents**: Documents are represented as plain JavaScript objects and do not require a rigid structure <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. When querying multiple documents, the query relies on consistent key names within the objects <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Upon creation, each document is automatically assigned a unique ID <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Each document includes a `ref` property that points to its collection and unique ID <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This reference is crucial for joining data across multiple collections, similar to foreign keys in SQL databases <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Querying Data with FaunaDB's FQL

[[faunadbs_functional_query_language_and_api_integration | FaunaDB]] offers multiple native APIs, including GraphQL, where uploading a schema can automatically create collections and indexes <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. However, to deeply understand [[faunadbs_functional_query_language_and_api_integration | FaunaDB]], it's recommended to learn its custom query language, [[faunadbs_functional_query_language_and_api_integration | FQL]] (Fauna Query Language) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

[[faunadbs_functional_query_language_and_api_integration | FQL]] is a functional, intuitive, and flexible language <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. You can execute [[faunadbs_functional_query_language_and_api_integration | FQL]] directly in the [[features_and_benefits_of_faunadb | FaunaDB]] console or using `faunash` locally <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Basic FQL Functions

*   **`Get`**: Retrieves a single document based on its reference <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **`Ref`**: Creates a reference, taking a collection and document ID as arguments <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

When executing queries, [[features_and_benefits_of_faunadb | FaunaDB]] provides detailed information, including bytes transferred <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Indexes

Indexes are essential for efficiently querying documents when the document ID isn't readily available <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Definition**: An index defines how to query documents from a collection, e.g., fetching a user by email or username <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Structure**:
    *   **Name**: A descriptive name for the index, like "users by name" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   **Terms**: One or more fields on the document that can be searched <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   **Values**: Allows you to specify which fields from the document should be returned, optimizing data transfer <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **`Match`**: Used within `Get` to search across an index <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It takes the index as the first argument and an array of search terms as the second <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Building a REST API with Node.js and FaunaDB

This section details how to build a simple REST API using [[setting_up_a_nodejs_and_express_environment | Express.js]] to interact with [[features_and_benefits_of_faunadb | FaunaDB]].

### Environment Setup

1.  **Prerequisites**: Ensure [[nodejs_runtime_and_basic_operations | Node.js]] is installed <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The [[features_and_benefits_of_faunadb | FaunaDB]] VS Code extension is also recommended for easier management of collections and indexes <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
2.  **Initialize Project**:
    *   Create an empty directory <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Run `npm init -y` to create a `package.json` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   Install [[faunadbs_functional_query_language_and_api_integration | `faunadb`]] and `express`: `npm install faunadb express` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
    *   Create a `src` directory and an `index.js` file within it <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Connecting to FaunaDB

1.  **Import and Initialize**:
    ```javascript
    const express = require('express');
    const faunadb = require('faunadb');
    const {
        Get, Ref, Collection, Index, Create, Select, Match, Call, Function: Fn, Paginate, Join
    } = faunadb.query;

    const client = new faunadb.Client({ secret: 'YOUR_FAUNA_SECRET_KEY' });
    const app = express();
    app.listen(5000, () => console.log('Server running on port 5000'));
    ```
2.  **API Secret Key**:
    *   Go to the [[features_and_benefits_of_faunadb | FaunaDB]] dashboard, find the `Security` tab, and create a new key <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   Choose a `Server` key for server-side operations <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   [[features_and_benefits_of_faunadb | FaunaDB]] allows for fine-grained access control to adhere to the principle of least privilege <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   Copy and paste the secret key into the `faunadb.Client` initialization <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  **FQL Functions in Node.js**: [[faunadbs_functional_query_language_and_api_integration | FQL]] functions can be imported from the `faunadb.query` namespace and composed like JavaScript functions <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### CRUD Operations and Data Modeling

#### Reading a Single Document

To read a single tweet by its ID:

```javascript
app.get('/tweet/:id', async (req, res) => {
    try {
        const tweet = await client.query(
            Get(Ref(Collection('tweets'), req.params.id))
        );
        res.status(200).send(tweet);
    } catch (error) {
        res.status(500).send(error);
    }
});
```

*   A `GET` endpoint handles requests to `/tweet/:id` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   The `client.query` method takes an [[faunadbs_functional_query_language_and_api_integration | FQL]] expression <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   `Get` and `Ref` functions are used to retrieve the document <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   Queries return promises, so `async/await` is used <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Error handling with `try/catch` is recommended <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

#### Creating a Document and Modeling One-to-Many Relationships

To create a tweet and link it to a user (one-to-many relationship: a user has many tweets):

```javascript
app.post('/tweet', async (req, res) => {
    try {
        const tweet = await client.query(
            Create(Collection('tweets'), {
                data: {
                    text: req.body.text,
                    user: Select(['data', 'ref'], Call(Fn('get_user'), req.body.username))
                }
            })
        );
        res.status(200).send(tweet);
    } catch (error) {
        res.status(500).send(error);
    }
});
```

*   A `POST` endpoint is created for `/tweet` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   The `Create` function is used to add a new document to the `tweets` collection <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   To establish a relational link, the `user` field in the tweet document stores a reference to the user document <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   The `Select` function extracts the `ref` property from the user document, which is retrieved using an [[faunadbs_functional_query_language_and_api_integration | FQL]] function (explained next) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   [[features_and_benefits_of_faunadb | FaunaDB]] is 100% ACID compliant, ensuring global consistency for transactions <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

#### Querying Multiple Documents

To retrieve all tweets by a specific user:

1.  **Create an Index**: In the [[features_and_benefits_of_faunadb | FaunaDB]] dashboard, create a new index named `tweets_by_user`.
    *   Set the `terms` to `user` (the reference field) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    *   Set the `values` to `text` (to return only the tweet text for efficiency) <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
2.  **Node.js Endpoint**:
    ```javascript
    app.get('/tweetsByUser/:username', async (req, res) => {
        try {
            const tweets = await client.query(
                Paginate(Match(Index('tweets_by_user'), Call(Fn('get_user'), req.params.username)))
            );
            res.status(200).send(tweets);
        } catch (error) {
            res.status(500).send(error);
        }
    });
    ```
*   Instead of `Get`, use `Paginate` to return a set of documents <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   `Match` is used with the `tweets_by_user` index and the `get_user` function to find tweets associated with a specific user <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

#### FaunaDB Functions for Code Reusability

[[faunadbs_functional_query_language_and_api_integration | FaunaDB]] functions allow you to extract and reuse [[faunadbs_functional_query_language_and_api_integration | FQL]] code <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

1.  **Create Function in Dashboard**:
    *   Go to the `Functions` tab in the [[features_and_benefits_of_faunadb | FaunaDB]] dashboard <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Create a new function, e.g., `get_user`.
    *   Set the role to `server` <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
    *   The function body uses a `Query` followed by a `Lambda` function (similar to an anonymous arrow function in JavaScript) <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
        ```fql
        Query(Lambda("username", Select(["data", "ref"], Get(Match(Index("users_by_name"), Var("username"))))))
        ```
2.  **Call Function in Node.js**:
    *   Import `Call` and `Function` (renamed as `Fn` to avoid collision with JavaScript's built-in `Function`) from `faunadb.query` <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
    *   Replace duplicated code with `Call(Fn('function_name'), argument)` <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

#### Modeling Many-to-Many and Graph Relationships

[[using_faunadb_for_relational_and_graph_data_modeling | FaunaDB]] excels at modeling complex relationships like social graphs where users can follow and be followed by many others <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

1.  **Create a `relationships` Collection**: This collection stores "edges" in the graph, with each document containing `follower` and `followee` fields, both being user document references <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
2.  **Create a Relationship Endpoint**:
    ```javascript
    app.post('/relationship', async (req, res) => {
        try {
            const relationship = await client.query(
                Create(Collection('relationships'), {
                    data: {
                        follower: Call(Fn('get_user'), req.body.followerUsername),
                        followee: Call(Fn('get_user'), req.body.followeeUsername)
                    }
                })
            );
            res.status(200).send(relationship);
        } catch (error) {
            res.status(500).send(error);
        }
    });
    ```
    This endpoint creates a `relationships` document, linking two users via their references obtained from the `get_user` function <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

3.  **Create an Index for Followed Accounts**: In the [[features_and_benefits_of_faunad_b | FaunaDB]] dashboard, create an index named `followers_by_followee`. It will take the `followee` user reference and return all accounts that user is following <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

4.  **Retrieve a User's Feed (Joining Indexes)**: To get a feed of tweets from all users a given user follows:

    ```javascript
    app.get('/feed/:username', async (req, res) => {
        try {
            const feed = await client.query(
                Paginate(
                    Join(
                        Match(Index('followers_by_followee'), Call(Fn('get_user'), req.params.username)),
                        Index('tweets_by_user')
                    )
                )
            );
            res.status(200).send(feed);
        } catch (error) {
            res.status(500).send(error);
        }
    });
    ```
    *   The `Join` function is used to combine two indexes <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   The first argument to `Join` is the initial query: all users followed by a specific user (using `followers_by_followee` index) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    *   The second argument is the `tweets_by_user` index, which then retrieves all tweets from those followed users <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. This allows for complex relational queries akin to joins in traditional databases.

[[features_and_benefits_of_faunadb | FaunaDB]] is a powerful database solution, especially suitable for new projects due to its features and flexibility <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.