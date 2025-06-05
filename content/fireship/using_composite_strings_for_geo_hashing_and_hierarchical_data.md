---
title: Using composite strings for geo hashing and hierarchical data
videoId: 35RlydUf6xo
---

From: [[fireship]] <br/> 

One challenging aspect of app development is determining the optimal [[firestore_data_modeling_techniques | data structure]] to maximize performance and minimize costs, especially with NoSQL databases like Firestore, which require advanced planning for [[firestore_data_modeling_techniques | data modeling]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

A useful technique for structuring and querying data in Firestore is the use of composite strings <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. This method is particularly relevant for [[implementing_gps_tracking_and_geolocation_queries | geolocation queries]], [[implementing_gps_tracking_and_geolocation_queries | geo hashing]], [[graph_traversal_algorithms | tree reversals]], and threaded comment systems <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Building a Hierarchical Data Structure

Consider a tree structure where each letter represents a document in the database <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. All documents can reside within the same collection <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Document Fields
*   **`parent`**: This field defines the relationship. A top-level comment (e.g., document 'A') would have `parent` set to `false` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. A response (e.g., document 'B') would have its `parent` set to 'A' <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. For deeper levels (e.g., 'C' and 'D' responding to 'B'), their `parent` would reference the IDs of the parent documents (e.g., 'A_B') <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Firestore's auto-generated IDs can be used, but the crucial aspect is that the composite string (e.g., `parent` value) is created in the same order as the parent elements appear in the tree <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **`level`**: An optional integer property that increases by one for each level, allowing for queries across the breadth of the tree <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Querying the Tree

### Querying the Top Level
To retrieve all top-level comments, you can query documents where the `parent` field equals `false` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Querying Breadth
If a `level` property is present, you can query all documents at a specific level or use a range operator to get everything above or below a certain level <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Querying Depth (Traversing Down)
This is where the composite key truly shines. As you go deeper into the tree, the composite key (the `parent` string) becomes larger <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. You can use an existing document ID as a starting point to query all its children whose composite `parent` string starts with that same ID <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

This query can be made using range operators:
```javascript
collection.where('parent', '>=', ID)
          .where('parent', '<=', ID + '\uf8ff') // '\uf8ff' is a high Unicode character
```
This approach allows you to start from any node in the tree and traverse downwards <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. This exact method is also how [[implementing_gps_tracking_and_geolocation_queries | geo hashing]] works and is a very powerful, though more advanced, feature <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.