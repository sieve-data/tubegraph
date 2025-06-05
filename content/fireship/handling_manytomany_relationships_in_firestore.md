---
title: Handling manytomany relationships in Firestore
videoId: 35RlydUf6xo
---

From: [[fireship]] <br/> 

One of the most challenging aspects of building applications is determining the optimal data structure to maximize performance and minimize costs, especially with a NoSQL database like Firestore, which requires significant planning [00:00:05](<a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike relational SQL databases, where data is broken into small pieces and joined server-side, Firestore aims to pre-render data to fit the view, ideally requiring only one document read or query per view [00:00:53](<a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While some believe NoSQL databases are not suitable for relational data modeling, it's a matter of rethinking [[firestore_data_modeling_techniques | data modeling]], allowing for faster, less expensive, and more flexible solutions compared to SQL [00:01:17](<a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## User Mention System (Twitter-like)

This model, suggested by Samrat, addresses querying a collection based on whether a user was mentioned in a post, similar to Twitter's @mention feature [00:01:32](<a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Relationship Type
This is a many-to-many relationship: a tweet can mention many users, and a user can be mentioned in many tweets [00:01:49](<a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Data Modeling Strategy
It's generally best to have the document with the smaller side of the relationship manage the relational data [00:02:01](<a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. In this case, a post might mention 1-10 users, while a user could be mentioned in billions of tweets [00:01:56](<a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The strategy involves embedding an array of usernames or user IDs (e.g., `mentions`) directly on the tweet/post document [00:02:09](<a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This `mentions` array would be populated by extracting usernames from the post text using regex in your front-end code and then duplicating them onto the document [00:02:13](<a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Querying
To query all tweets a user is mentioned in, you can reference the post collection and use the `array-contains` operator with the user ID [00:02:22](<a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
```javascript
db.collection('posts').where('mentions', 'array-contains', 'some_user_id')
```
This allows for easy retrieval of relevant posts [00:02:28](<a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Cloud functions can also be used to send notifications (push or email) when a user is mentioned in a new post [00:02:33](<a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Limitation
The main limitation is that `array-contains` can only query for one item at a time [00:02:41](<a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Category/Tag System

This approach handles filtering posts by multiple categories (tags) with AND, OR, or NOT logic [00:02:45](<a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Data Modeling Strategy
Create a `tags` collection to hold metadata about each tag (description, URL, etc.), giving each tag a descriptive, unique ID [00:03:07](<a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Then, associate tags to a post by using a `map` field on the post document, named `tags` [00:03:21](<a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Each key in this map is the tag's ID, and its value can be a boolean (`true`) or other data [00:03:25](<a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Firestore automatically indexes the keys in a map, allowing queries without additional configuration [00:03:29](<a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Querying
*   **Logical AND Query:** To get items with *both* multiple tags, chain `where` statements using the `==` operator for each tag [00:03:37](<a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This works well for multiple boolean values.
    ```javascript
    db.collection('posts')
      .where('tags.tagId1', '==', true)
      .where('tags.tagId2', '==', true)
    ```
    If a range operator is included, a composite index is required, and only one range operator is allowed per query [00:03:52](<a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Logical OR Query:** To get items with *any* of multiple tags, make multiple concurrent queries for separate tags [00:04:01](<a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The results can then be joined together and duplicates filtered out in client-side code [00:04:08](<a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Logical NOT Query:** This is more difficult. If using boolean values, all tags would need to be added to every document and set to `false` by default, which is feasible for a finite set of known tags but challenging if tags are user-generated or potentially numerous [00:04:13](<a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    Alternatively, for numeric or string values with inherent ordering, a NOT query can be simulated using range operators (e.g., querying for values less than X and values greater than X to exclude X) [00:04:35](<a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
    For complex full-text search requirements, integrating with a dedicated search engine like Algolia is recommended [00:04:53](<a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

## Normalized Data Models and Document Joining

While [[using_firebase_databases_and_data_modeling_techniques | denormalizing data]] is often ideal in Firestore, it's not always practical [00:07:44](<a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Data Modeling Strategy
A more [[normalized_data_models_and_document_joining_in_firestore | normalized model]] can be used where a document contains an array of IDs (e.g., `sizes` array where each element is a string referencing a document in a different collection) [00:07:53](<a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Joining Data
Since Firestore does not have server-side joins, data must be joined client-side [00:08:02](<a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This can be done efficiently by sending multiple concurrent read requests to the database [00:08:07](<a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

A helper function can take a collection reference and an array of IDs. It maps these IDs to document read promises, then uses `Promise.all` to resolve them concurrently, and finally maps the document snapshots to their raw data [00:08:14](<a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
```javascript
// Example helper function (simplified from transcript)
async function joinIdsToCollection(collectionRef, ids) {
  const docReads = ids.map(id => collectionRef.doc(id).get());
  const snapshots = await Promise.all(docReads);
  return snapshots.map(doc => doc.data());
}

// Usage
// const sizesRef = db.collection('sizes');
// const productData = await joinIdsToCollection(sizesRef, ['size1Id', 'size2Id']);
```
This allows for modeling data in a more normalized, SQL-like style when necessary [00:08:42](<a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Social Media Follower Feed

This model, contributed by Troy, demonstrates how to build a social media-style follower feed where users see recent posts from those they follow, ordered by date [00:08:47](<a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This is a very challenging requirement and a classic many-to-many relationship.

### Relationship Type
This is a many-to-many relationship: a user follows many users, and many users can follow a single user [00:09:16](<a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Data Modeling Strategy
To scale this system effectively, data duplication is necessary [00:09:20](<a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Three collections are involved: `users`, `posts`, and `followers` [00:09:24](<a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

All relational data is handled by the `followers` collection, and the UI data for the feed comes from a query to this collection [00:09:32](<a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The `followers` document (which belongs to the user being followed) tracks all its followers in an array [00:09:40](<a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

Crucially, this `followers` document also duplicates some of the user's recent posts (e.g., title, text preview) and keeps a timestamp of the user's last post [00:09:47](<a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Querying
The query is made on the `lastPost` property along with the `followers` array [00:10:04](<a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

1.  **Reference `followers` collection:** `db.collection('followers')` [00:10:29](<a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  **Filter by logged-in user:** Use `array-contains` with the logged-in user's ID to find all `followers` documents where that user is a follower [00:10:30](<a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
3.  **Order by last post:** Chain an `orderBy` clause on the `lastPost` timestamp [00:10:35](<a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This creates a compound query that requires an index [00:10:41](<a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
4.  **Limit results:** Limit the query to a small number of document reads (e.g., 10), which can still provide data for dozens of posts due to the duplication [00:10:48](<a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Client-Side Processing
After retrieving the initial data:
1.  Map the query result to an array of document data [00:10:57](<a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
2.  Reduce this array of documents to a new array containing only the duplicated `recentPosts` [00:11:01](<a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
3.  Sort these `recentPosts` based on their `publishedDate` using `Array.sort` [00:11:13](<a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

This results in a sorted array of posts spanning multiple users that the current user is following [00:11:19](<a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Limitation
The `followers` array is kept on a single document, meaning it can only scale up to 1 MB of data [00:10:13](<a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. As the app grows, this data may need to be broken up into multiple documents [00:10:19](<a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

For more in-depth learning on [[data_modeling_in_firestore_chat_applications | data modeling techniques]] and how these specific models work, consider becoming a pro member at Fireship.io to access their course [00:11:25](<a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.