---
title: Normalized data models and document joining in Firestore
videoId: 35RlydUf6xo
---

From: [[fireship]] <br/> 
While [[using_firebase_databases_and_data_modeling_techniques | data modeling in Firestore]] ideally promotes denormalization, where data is embedded directly onto a single document to maximize performance and minimize costs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, there are instances where a more normalized data model becomes necessary or practical <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Normalized Data Models in Firestore

In a normalized model, data might be spread across multiple collections, with documents referencing each other via IDs <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. For example, a `sizes` array could contain strings referencing documents in a different collection <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This approach differs significantly from relational SQL databases, which rely on server-side joins to combine fragmented data <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Joining Documents (Client-Side)

Unlike SQL databases, Firestore does not support server-side joins <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. However, data can be efficiently "joined" on the client-side by sending multiple read requests concurrently to the database <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

#### Helper Function for Joining IDs

A helper function can be used in client-side code (e.g., JavaScript) to facilitate joining an array of document IDs to a collection <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

Here's how such a function works:
1.  It takes a collection reference and an array of IDs as arguments <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  It maps each ID to a document read operation, which results in an array of promises <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
3.  `Promise.all` is then used to resolve all these promises concurrently <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
4.  Finally, the document snapshots are mapped to their raw data, returning an array of the requested document data <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

This method allows for a more normalized, SQL-style approach to [[data_modeling_in_firestore_chat_applications | data modeling]] in Firestore when direct denormalization is not feasible <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. While some perceive NoSQL databases as not good for relational [[firestore_data_modeling_techniques | data modeling]], it's truly a matter of rethinking the approach, which can lead to faster, less expensive, and more flexible solutions compared to traditional SQL methods <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.