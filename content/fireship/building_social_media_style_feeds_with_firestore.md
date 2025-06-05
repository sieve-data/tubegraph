---
title: Building social media style feeds with Firestore
videoId: 35RlydUf6xo
---

From: [[fireship]] <br/> 

Building a social media-style follower feed, where users can see the most recent posts from the users they follow, is a common but challenging requirement for applications <a class="yt-timestamp" data-t="00:08:47">[08:47:00]</a>. This section outlines a strategy for building such a feed efficiently and scalably using Firebase Firestore. The primary goal is to retrieve the most recent posts from followed users, order them by date, and maintain the user-to-user follow relationships <a class="yt-timestamp" data-t="00:08:53">[08:53:00]</a>.

## Core Concept: Data Duplication for Scale

The only way to effectively scale a system like a social media feed to a significant number of users in Firestore is by [[Firestore data modeling techniques | duplicating some data]] <a class="yt-timestamp" data-t="00:09:21">[09:21:00]</a>.

## Data Model

This approach utilizes three main collections <a class="yt-timestamp" data-t="00:09:26">[09:26:00]</a>:

*   **Users**: Stores user profiles.
*   **Posts**: Contains all posts made by users.
*   **Followers**: Manages the relational data for follows <a class="yt-timestamp" data-t="00:09:34">[09:34:00]</a>.

The `followers` collection is central to this model. Each document in this collection represents the "followed user" <a class="yt-timestamp" data-t="00:09:42">[09:42:00]</a>. This document contains:

*   An array of `followers` (user IDs of those following this user) <a class="yt-timestamp" data-t="00:09:43">[09:43:00]</a>.
*   Duplicated recent posts from the "followed user" <a class="yt-timestamp" data-t="00:09:48">[09:48:00]</a>. Only necessary data for the feed (e.g., title, text preview) is duplicated <a class="yt-timestamp" data-t="00:09:55">[09:55:00]</a>.
*   A `lastPost` timestamp, indicating the most recent post from the followed user <a class="yt-timestamp" data-t="00:10:00">[10:00:00]</a>.

Most of the data displayed in the UI for the feed will be derived from queries to the `followers` documents <a class="yt-timestamp" data-t="00:09:36">[09:36:00]</a>.

### Scalability Consideration

The `followers` document, being a single document, has a maximum size limit of 1MB <a class="yt-timestamp" data-t="00:10:13">[10:13:00]</a>. For applications with extremely large numbers of followers for a single user, this document may need to be broken up into multiple documents as the app grows <a class="yt-timestamp" data-t="00:10:19">[10:19:00]</a>.

## Querying the Feed

To build the feed for a logged-in user, the following query is performed <a class="yt-timestamp" data-t="00:10:04">[10:04:00]</a>:

1.  **Reference the `followers` collection** <a class="yt-timestamp" data-t="00:10:29">[10:29:00]</a>.
2.  **Filter by `array-contains`**: Use `array-contains` to find `followers` documents where the current logged-in user's ID is present in the `followers` array <a class="yt-timestamp" data-t="00:10:30">[10:30:00]</a>. This means we're looking for users *being followed* by the logged-in user.
3.  **Order by `lastPost` timestamp**: Apply an `orderBy` clause on the `lastPost` timestamp to retrieve the most recent posts first <a class="yt-timestamp" data-t="00:10:37">[10:37:00]</a>. This constitutes a compound query and will require a composite index in Firestore <a class="yt-timestamp" data-t="00:10:41">[10:41:00]</a>.
4.  **Limit results**: Optionally, limit the query to a specific number of documents (e.g., 10 documents) to make it highly efficient. Each document can provide data for potentially dozens of posts <a class="yt-timestamp" data-t="00:10:48">[10:48:00]</a>.

### Client-Side Data Processing

After retrieving the query results, some client-side data wrangling is necessary <a class="yt-timestamp" data-t="00:10:25">[10:25:00]</a>:

1.  **Map to document data**: The initial array of query snapshots needs to be mapped to their raw document data <a class="yt-timestamp" data-t="00:10:57">[10:57:00]</a>.
2.  **Extract recent posts**: Each document will contain an array of the followed user's most recent posts. This array of documents should be reduced to a new array containing only these recent posts <a class="yt-timestamp" data-t="00:11:01">[11:01:00]</a>.
3.  **Sort posts**: Finally, sort this new array of posts based on their `publishedDate` to ensure they are presented in chronological order across all followed users <a class="yt-timestamp" data-t="00:11:15">[11:15:00]</a>.