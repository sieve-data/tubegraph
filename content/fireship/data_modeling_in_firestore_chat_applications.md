---
title: Data modeling in Firestore chat applications
videoId: LKAXg2drQJQ
---

From: [[fireship]] <br/> 

[[Building a realtime chat app with Firebase | Building a real-time chat app]] traditionally required weeks of development time, but with Firebase, it becomes significantly simpler, as the SDK manages state and data syncing between the client and server <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This ease allows for rapid development, with an entire chat application being built in just 24 hours using AngularFire and Firestore <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A key aspect of [[building_a_realtime_chat_app_with_firebase | building a real-time chat app]] is [[secure_and_efficient_data_modeling_for_chat_applications | data modeling]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, as there isn't a single solution that fits every chat feature <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Core Data Modeling Requirements

Every chat application requires a user authentication system and public user profile information stored in a "users" collection within [[using_firebase_databases_and_data_modeling_techniques | Firestore]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Beyond this basic setup, there are various ways to model the relationships between users, chats, and individual messages <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## [[Firestore data modeling techniques | Data Modeling Strategies]] for Chat Applications

When designing [[secure_and_efficient_data_modeling_for_chat_applications | data models]] for chat, several approaches can be considered, each with its own advantages and limitations.

### 1. Chats as a Collection, Messages as Sub-collections

A common and logical approach is to establish a collection of `chats`, with each `chat` document containing a sub-collection of `messages` <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Pros**: This method allows for storing chat metadata in a small document while enabling querying an unlimited number of messages from its sub-collection <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### 2. Messages as a Root Collection

Alternatively, `messages` can be established as a root collection <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Pros**: This allows for querying messages across all different chats in the application <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, such as finding all messages for a specific user across all chats they participate in <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This approach offers significant flexibility <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Cons**: The drawback is that a document read operation is required for every message displayed in the UI <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### 3. Chats as a Document, Embedded Messages (Chosen Approach)

A different approach, implemented in the video, involves modeling each chat as its own document and embedding the messages for that chat directly onto the document <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   **Pros**: This method is fast and simple for retrieving chat data <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The initial load should always be very performant due to smaller document sizes <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Cons**:
    *   Individual messages cannot be queried because they are embedded; sorting must be done client-side <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Firestore documents have a 1MB data limit, which conservatively translates to 250 to 1,000 messages per document <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

#### Addressing the 1MB Limit with Cloud Functions

To mitigate the 1MB document size limitation, a Cloud Function can be set up to either archive or delete older messages when the document size or message count exceeds a certain threshold <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This strategy helps keep the document size manageable <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

#### Structure of Embedded Messages

In this model, each chat document contains an `owner` field and a `messages` array <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Each individual message within this array is an object containing:
*   `user ID` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   `created at` timestamp <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   `message content` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>

When a user creates a new chat, a document is created with their user ID as the owner ID, generating a unique URL that can be shared for other authenticated users to join <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Implementation Details for [[Firestore features and methods for handling chat data | Chat Data Handling]]

The implementation uses Angular, AngularFire, and Firebase. Key services and components include:
*   **Authentication Service**: Manages user login and saves user information to Firestore <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It listens to the AngularFire auth state for the current authenticated user and fetches their related user profile document from Firestore <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. It includes methods for signing in/out with Google <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, and a `getUser` method to convert the user observable to a promise for easier asynchronous operations when writing data <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Chat Service**: Handles all interactions with chat documents, including creating new chats and adding messages <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   **`getChat`**: Retrieves a chat document from the Firestore database as an observable, mapping the document ID with its data payload <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
    *   **`create`**: An asynchronous function that creates a new chat document. It awaits the currently authenticated user's ID, sets up a data payload with the user ID, a timestamp, and an empty `messages` array <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. The `add` method on the `chats` collection is used, and upon completion, the Angular router navigates to the new chat's URL <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   **`addMessage`**: An asynchronous function taking the chat ID and message content. It determines the current user's ID, sets up a data payload (user ID, content, timestamp), and uses the `arrayUnion` method from Firestore <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. `arrayUnion` ensures that if a unique object is provided, it's appended to the end of the array, making messages unique and idempotent (preventing duplicate additions if the same payload is submitted twice) <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Joining User Profiles to Messages ([[Normalized data models and document joining in Firestore | Firestore Joins]])

An advanced method is implemented to join user profiles to individual chat messages <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This ensures that chat messages always display the most recent user profile image and username <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. The process involves:
1.  Taking the original chat document and identifying all unique user IDs within its messages array <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
2.  Concurrently reading all identified user profiles using `combinedLatest` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  Recomposing the original messages object so that each message includes a `user` property with the corresponding user profile data <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
This results in a single object containing all chat messages and user profiles, all synced in real-time <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Managing Document Size with Cloud Functions

A Cloud Function (`archiveChat`) is set up to address the 1MB document size limit of Firestore for embedded messages <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

*   **Trigger**: The function points to the `chat` collection and runs only when a document is updated <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Logic**: It checks the current size of the `messages` array. If there are more than 50 messages, or if the total character length of the messages exceeds 10,000, it starts deleting or archiving the oldest messages by splicing items from the beginning of the array <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Safety**: If deleted messages are to be added to another location (e.g., an archive), this operation should be performed as an atomic batch write to prevent data loss in case of partial failures <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Performance**: Cloud Functions exhibit very low latency, with round-trip times finishing in just a few hundred milliseconds <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

This [[secure_and_efficient_data_modeling_for_chat_applications | data modeling]] strategy, combined with Cloud Functions for managing document size, provides a fast and efficient way to [[building_a_realtime_chat_app_with_firebase | build a real-time chat app]] using [[using_firebase_databases_and_data_modeling_techniques | Firebase Firestore]] <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.