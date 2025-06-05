---
title: Firestore data modeling techniques
videoId: 35RlydUf6xo
---

From: [[fireship]] <br/> 
## Firestore Data Modeling Techniques

One of the most challenging aspects of building any application is determining the optimal data structure, aiming to maximize performance while minimizing costs <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This is especially true with a NoSQL database like Firestore, where advance planning for data modeling is crucial <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While some might believe Firestore or NoSQL databases aren't suitable for relational [[using_firebase_databases_and_data_modeling_techniques|data modeling]], it's actually about rethinking your approach to [[secure_and_efficient_data_modeling_for_chat_applications|data modeling]] in general <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. You can solve the same problems as with SQL, but in a faster, less expensive, and more flexible way <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

The basic idea in Firestore is to "pre-render" your data so it fits the view or screen in your app as closely as possible <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Ideally, you should only need one document read or one query to a collection to fill the entire view with data <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This differs from relational SQL databases, where data is broken into small pieces and then joined server-side <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

Here are five different techniques for structuring and querying data in Firestore:

### 1. Handling Many-to-Many Relationships (User Mentions)

This technique addresses scenarios like Twitter, where a user can be mentioned in many posts, and a post can mention many users <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Problem**: Querying a collection based on whether a user was mentioned in a post <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Solution**: Embed an array of usernames or user IDs on the post document <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Front-end code can extract usernames using regex and duplicate them into this array <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Query**: Use the `array-contains` operator on the post collection to find all tweets with a specific user ID in the mentions array <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   *Example*: `db.collection('posts').where('mentions', 'array-contains', 'userId')`
*   **Notifications**: A Cloud Function can listen for new posts and send push notifications or emails when a user is mentioned <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Limitation**: `array-contains` can only query for one item at a time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### 2. Category/Tag Filtering (AND, OR, NOT Logic)

This method allows filtering posts by multiple categories or tags, including "AND", "OR", and "NOT" logic <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

*   **Data Model**:
    *   Have a `tags` collection to hold extra data about each tag (description, URL, etc.) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Tags should have a unique, descriptive ID <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Associate tags to a post using a map (`tags` field) on the post document. Each key in the map is the tag ID, and values can be booleans (e.g., `true` if tagged) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Firestore automatically indexes the keys in a map, allowing queries without extra configuration <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **AND Query**: Chain `where` statements using the "equal to" operator <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   *Example*: `db.collection('posts').where('tags.tag1', '==', true).where('tags.tag2', '==', true)`
    *   **Limitation**: If a range operator is used, only one is allowed per query, requiring a composite index <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **OR Query**: Make multiple concurrent queries for separate tags <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Run these queries concurrently, then join them and filter out duplicates in client-side code <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **NOT Logic**:
    *   **Boolean Values**: If tags are set as booleans, the most straightforward approach is to add all possible tags to every document and set them to `false` by default. This works for a finite set of tags but is challenging if tags are user-generated and potentially numerous <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **Numeric/String Values**: Simulate a "NOT" query using range operators. For example, to get items *not* equal to $20, query for items `< $20` AND items `> $20` <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Advanced Search**: For complex full-text search, consider integrating with a dedicated search engine like Algolia, which works well with Firebase <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### 3. Composite Strings for Tree Structures (Threaded Comments, Geolocation)

This technique uses composite strings to model hierarchical data, useful for threaded comments or geolocation queries <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Problem**: Traversing down one node of a tree structure, such as Reddit comments with multiple levels of threading or hierarchical categories <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Data Model**:
    *   All documents can reside in the same collection <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   Top-level comments can have a `parent` value set to `false` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
    *   Responses create a composite key where an item's ID references the IDs of its parent documents in order (e.g., `A/B/C`) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Firestore's auto-generated IDs can be used <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   An optional `level` property (integer increasing with depth) can be added for querying breadth <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Top-Level Query**: `where('parent', '==', false)` <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Depth Query (Traversing Downward)**: Take a document ID as a starting point and query all children whose composite parent string starts with that ID <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   *Example*: `where('parent', '>=', 'ID')` and `where('parent', '<=', 'ID' + '\uffff')` (where `\uffff` is a high Unicode character) <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Application**: This is the same principle used for geo hashing <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### 4. Normalized Data Models and Client-Side Joins

While denormalization is often ideal in Firestore, there are cases where a more normalized model is necessary <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Since Firestore lacks server-side joins, client-side techniques are used.

*   **Problem**: Querying a collection starting with an array of document IDs (e.g., a `sizes` array containing references to documents in a separate `sizes` collection) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Solution**: Store an array of string references (document IDs) in the main document <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Client-Side Join**: Efficiently send multiple read requests concurrently using `Promise.all` in JavaScript <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   A helper function can take a collection reference and an array of IDs, map the IDs to document reads (creating an array of promises), use `Promise.all` to resolve them, and then map the document snapshots to raw data <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   This allows modeling data in a more normalized, SQL-like style <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 5. Building Social Media-Style Feeds (Follower Feed)

This is a challenging requirement that involves showing the most recent posts from users a person follows, ordered by date <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

*   **Problem**: Scaling a social media follower feed efficiently while maintaining user-to-user follow relationships <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Solution**: Duplicate data across collections <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Data Model**:
    *   `users` collection
    *   `posts` collection
    *   `followers` collection: This collection handles all relational data <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
        *   Each `followers` document belongs to the user being followed <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
        *   It tracks all followers in an array <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
        *   Crucially, it duplicates *some* of the followed user's recent posts (e.g., title, text preview) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
        *   It includes a `lastPost` timestamp for the user's most recent post <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Query**:
    *   Query the `followers` collection using `array-contains` with the logged-in user's username <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   Make it a compound query by using `orderBy('lastPost', 'desc')` <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This requires an index in Firestore <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   Limit the query to a small number of document reads (e.g., 10) for efficiency <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Client-Side Processing**:
    *   Map the query result (an array of documents) to the document data <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Reduce this array of documents down to a new array containing only the recent posts <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   Sort these recent posts based on their `publishedDate` <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Scaling Consideration**: Keeping all followers on a single document limits scalability to 1MB of data. As the app grows, this might require breaking it into multiple documents <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

These techniques demonstrate how to approach various [[advanced_data_management_techniques_in_flutter_apps|data management techniques]] and [[secure_and_efficient_data_modeling_for_chat_applications|secure and efficient data modeling]] challenges in Firestore, particularly when [[data_modeling_in_firestore_chat_applications|data modeling in Firestore chat applications]] or [[building_social_media_style_feeds_with_firestore|building social media style feeds with Firestore]].