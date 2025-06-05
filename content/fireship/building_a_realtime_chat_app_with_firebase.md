---
title: Building a realtime chat app with Firebase
videoId: LKAXg2drQJQ
---

From: [[fireship]] <br/> 

Building a real-time chat application traditionally required weeks of development time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, with Firebase, this process becomes almost trivial because its SDK handles all state management and data syncing between the client and server <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. An entire chat app can be built in as little as 24 hours using Angular, AngularFire, and Firestore <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## [[Data modeling in Firestore chat applications | Data Modeling]]

[[Data modeling in Firestore chat applications | Data modeling]] is crucial as there isn't a single solution for every chat feature <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Every application needs a user authentication system and public user profile information saved in a users collection in Firestore <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The relationship between users, chats, and individual messages offers several modeling options <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### Common Approaches to Chat Data

1.  **Sub-collection of Messages:** A common approach is to set up a collection of chats, with each chat having a sub-collection of messages <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    *   **Benefit:** Allows saving chat metadata on a small document and querying messages from the sub-collection <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Root Collection of Messages:** Messages can alternatively be a root collection, allowing queries across all chats <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
    *   **Benefit:** Enables querying all messages for a specific user across all their participating chats <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   **Drawback:** Requires a document read for every message displayed in the UI <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
3.  **Embedded Messages (Chosen Approach):** Each chat is modeled as its own document, with messages embedded directly within that document as an array <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   **Benefit:** This method is fast and simple for retrieval <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   **Limitations:**
        *   Individual messages cannot be queried; they can only be sorted client-side <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
        *   Documents are limited to 1 megabyte of data, conservatively allowing 250 to 1,000 messages per document <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Addressing Embedded Message Limitations

To handle the 1 megabyte document limit, a [[Optimizing chat app performance with cloud functions | Cloud Function]] can be set up to either archive or delete older messages <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This keeps document sizes small, ensuring initial loads are performant <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Database Structure

In the chosen embedded message model, each chat document contains an `owner` field and a `messages` array <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Each individual message within this array is an object containing:
*   `user ID` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   `created at` timestamp <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   `message content` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

When a user creates a new chat, a document is created with their user ID as the owner <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This generates a shareable URL, allowing other authenticated users to participate <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Application Structure (Angular & Firebase)

To build the chat app, an Angular application with [[Flutter app integration with Firebase | AngularFire]] and [[Flutter app integration with Firebase | Firebase]] installed is required <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The full source code is available on angularfirebase.com <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

The application primarily focuses on three main resources:
1.  **Authentication Service:** Handles user login and saves user information to Firestore <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
2.  **Chat Service:** Manages all interactions with chats, such as creating new ones and adding messages <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Chat Component:** Responsible for displaying the actual chat information in the UI <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

The chat component is loaded by the Angular router and is nested under a dynamic ID, allowing each chat to have its own unique URL <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Authentication Service Details

The authentication service listens to the AngularFire auth state (the currently authenticated user) and fetches their related user profile document from Firestore <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. It includes methods for signing users in with Google and signing out <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. A `getUser` method converts the user observable to a promise for easier use with async/await when writing data to Firestore <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Chat Service Details

The chat service utilizes AngularFireStore, the auth service, the router, and directly imports Firestore from the Firebase app <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

#### `getChat` Method

This method retrieves a chat document from the Firestore database as an observable <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. It's configured to map the document ID along with the data payload, making it easier to pass the document ID around <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

#### `create` Method

The `create` method is an async function that adds a new document to the database <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. It ensures the currently authenticated user's ID is available, then sets up a data payload including the user ID, a timestamp, and an empty array of messages <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. A reference is made to the `chats` collection, and the `add` method is called to create the new document <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Upon completion, the Angular router navigates to the URL of the new chat ID <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

#### `addMessage` Method

This async function takes the chat ID and message content as arguments <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. It determines the current user's ID and sets up a data payload with the user ID, content, and a `created at` timestamp <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The [[Firestore features and methods for handling chat data | `arrayUnion` method]] in Firestore is used to append the message object to the end of the messages array <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This ensures every message is unique and idempotent, meaning duplicate submissions won't result in duplicate messages in the array <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

#### Joining User Profiles to Messages

An advanced RxJS method is used to join user profiles to individual chat messages <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This ensures that chat messages always display the most recent user profile image and username <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. The process involves:
1.  Taking the original chat document and identifying all unique user IDs within its messages array <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
2.  Reading all unique user profiles concurrently using the `combinedLatest` method <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
3.  Recomposing the original messages object so that every message includes a `user` property with the corresponding user profile data <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
The result is a single object containing all chat messages and user profiles, synced in real-time <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Chat Component Details

The chat component depends on the chat service and `ActivatedRoute` from the Angular router <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. It has two main properties:
*   `chat` observable: The actual data to be displayed in the UI <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   `newMessage`: The form input where the user enters new messages <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

The component retrieves the document ID using `ActivatedRoute` and uses this ID to set up a source observable of the chat messages <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The `chat` property is set as the observable returned from the `joinUsers` method <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

For the form, the simplest type of Angular form, an `ngModel` (template-driven form), is used <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The value from the form input is sent to the `sendMessage` method, which updates Firestore <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. When looping over a real-time array in Angular, it's recommended to set up a `trackBy` method to only rerender changed items, significantly improving user experience and performance <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

#### HTML Structure

The HTML uses an `ngIf` statement on an `ng-container` to unwrap the `chat` observable, allowing the `chat` variable to be used throughout the template once data is ready <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. An `ngFor` loop iterates over the messages in the `chat.messages` array, utilizing the `trackBy` function <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Access to the message itself and user information is then available <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. The form uses `ngModel` to bind the `newMessage` property and includes handlers for the Enter key press and a submit button <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

## [[Optimizing chat app performance with cloud functions | Cloud Function]] for Message Management

The embedded message data model has a 1 megabyte limit, after which Firestore will reject new messages <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This limitation can be addressed with a simple [[Optimizing chat app performance with cloud functions | Cloud Function]] that listens for incoming messages <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

The Cloud Function, named `archiveChat`, points to the `chat` collection and runs only when the document is updated <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Its purpose is to check the current size of the `messages` array <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. If there are more than 50 messages, or if the messages' total characters exceed 10,000, it will start deleting or archiving the oldest messages by splicing items from the beginning of the array <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. While not explicitly implemented in the demo, `JSON.stringify` can be used to estimate the total size of the object as a string for a more precise check <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

The function sets up a batch write, which is important if deleted messages are to be added to another location, ensuring the delete operation and any other updates are atomic <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. If conditions are not met, no update is made to the document <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. The latency for these Cloud Function requests is very low, often finishing in a few hundred milliseconds <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.