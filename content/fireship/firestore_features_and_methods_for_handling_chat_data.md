---
title: Firestore features and methods for handling chat data
videoId: LKAXg2drQJQ
---

From: [[fireship]] <br/> 

Building a real-time chat application, which traditionally took weeks, can be significantly expedited using Firebase due to its Software Development Kit (SDK) handling state management and data syncing between client and server <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article focuses on how Firestore, a part of Firebase, facilitates [[building_a_realtime_chat_app_with_firebase | building a real-time chat app]] through its features and various [[data_modeling_in_firestore_chat_applications | data modeling]] approaches.

## Data Modeling for Chat Applications

[[Firestore data modeling techniques | Data modeling]] is crucial for chat applications as there is no single solution for every chat feature <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. A basic requirement for any chat app is a user authentication system and public user profile information saved in a `users` collection in Firestore <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

Several options exist for [[secure_and_efficient_data_modeling_for_chat_applications | modeling the relationship]] between users, chats, and individual messages <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>:

### Common Data Modeling Approaches

*   **Chats Collection with Messages Sub-collection**: This approach involves a `chats` collection where each chat document has a sub-collection of `messages` <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
    *   **Advantage**: It allows saving chat metadata on a small document and querying messages from the sub-collection as needed <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

*   **Messages as a Root Collection**: An alternative is to make `messages` a root collection <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
    *   **Advantage**: This allows querying messages across all chats in the application, such as finding all messages for a specific user across different chats <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This is considered the most flexible approach <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
    *   **Drawback**: Requires a document read for every message displayed in the UI <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

### Embedding Messages in Chat Documents

A different approach models each chat as its own document and embeds the messages for that chat directly on the document <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

*   **Structure**: Each chat document has an `owner` field and a `messages` array, where each message is an object containing the `user ID`, `created at` timestamp, and `message content` <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Advantages**: This method is fast and simple for initial loading <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>, <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   **Limitations**:
    *   Individual messages cannot be queried when embedded; they can only be sorted client-side <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
    *   Firestore documents are limited to one megabyte of data, conservatively allowing between 250 and 1,000 messages per document <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

### Mitigating Document Size Limitations

To address the document size limitation, a [[optimizing_chat_app_performance_with_cloud_functions | Cloud Function]] can be set up to either archive or delete older messages <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. This keeps the document size relatively small, ensuring initial load performance <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

## Key Firestore Methods and Services for Chat

The implementation of a chat application leverages several Firestore capabilities and related Firebase services:

### Authentication and User Management

*   **Auth Service**: Manages user logins and saves their information to Firestore <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. It listens to the AngularFire `auth state` for the currently authenticated user and retrieves their related user profile document from Firestore <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **`getUser` Method**: Converts the user observable to a promise for easier use with `async/await` when writing data to Firestore <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Chat Document Operations

*   **`getChat` Method**: Retrieves a chat document from the Firestore database as an observable, useful for constantly changing data. It also maps the document ID along with the data payload <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **`create` Method**: An async function for adding new chat documents <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
    *   Ensures the currently authenticated user's ID is available <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
    *   Sets up a data payload with the user ID, a timestamp, and an empty `messages` array <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
    *   Uses the `add` method on the `chats` collection reference to create a new document <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
    *   Navigates to the new chat's URL using the Angular router upon completion <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.
*   **Adding Messages**: An async function that takes the chat ID and message content <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
    *   Determines the current user's ID using `getUser` <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
    *   Uses the `arrayUnion` method to append the new message object to the `messages` array <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. This ensures uniqueness and idempotency, meaning duplicate submissions of the same data payload result in only one addition to the array <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

### Advanced Data Handling

*   **Joining User Profiles to Chat Messages**: A complex operation to associate user profiles with individual chat messages, ensuring the most recent user profile image and username are displayed <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
    *   Involves finding unique user IDs within the chat document's messages array <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
    *   Reads all unique user profiles concurrently using the `combinedLatest` method <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
    *   Recomposes the original messages object so each message includes a `user` property with the profile data <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
    *   The result is a single object with all chat messages and synced user profiles, updated in real time <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

### Maintaining Document Size with Cloud Functions

*   **`archiveChat` Cloud Function**: This function listens for updates to chat documents in the `chat` collection <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
    *   **Purpose**: To prevent Firestore documents from exceeding the one-megabyte limit <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.
    *   **Logic**: If the `messages` array exceeds a certain size (e.g., 50 messages) or the total character length of messages is too large (e.g., 10,000 characters), it will splice items from the beginning of the array (oldest messages) <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
    *   **Batch Writes**: The function uses a batch write, which is important if deleted messages are to be added to another location. This ensures the delete and any subsequent update operations are atomic, preventing data loss <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.

<div class="callout is-info">
<div class="callout-title">
<div class="callout-icon">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-info"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="16" y2="12"/><line x1="12" x2="12" y1="8" y2="8"/></svg>
</div>
Info
</div>
<p>To roughly estimate the total size of a document, <code>JSON.stringify</code> can be used to check the total length of the object as a string <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.</p>
</div>