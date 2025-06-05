---
title: Working with Firebase Firestore and realtime updates
videoId: 9kRgVxULbag
---

From: [[fireship]] <br/> 

Firebase offers an excellent platform for building applications, primarily due to its strong developer experience, cost minimization, and ability to maximize development time <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>. It abstracts away much of the backend complexity, allowing developers to focus on the frontend <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

## Firebase Databases

As of October 2017, Firebase offers two NoSQL database options: Realtime Database and Cloud Firestore <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>. While both can be used together, most applications will choose one over the other <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.

### Realtime Database vs. Cloud Firestore

The choice between the two often comes down to pricing and data structure:
*   **Realtime Database** charges $5 per gigabyte stored and $1 per gigabyte downloaded <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>. It's suitable for simple data sets that are read frequently <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Cloud Firestore** charges 18 cents per gigabyte stored, but also for each individual document read and write operation <a class="yt-timestamp" data-t="00:53:54">[00:53:54]</a>. It's generally preferred for larger, more complex relational data sets <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

In the majority of cases, Cloud Firestore tends to be the better choice <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Cloud Firestore Fundamentals

To begin using Firestore, you enable the database and start it in test mode, which temporarily disables security rules <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

### Data Structure
Firestore is structured as collections of documents <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>, similar to MongoDB, the most widely adopted NoSQL database <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.

*   **Collections:** Containers for documents <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.
*   **Documents:** Each document has a unique ID, which can be created manually or automatically generated <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.
*   **Fields:** Data within a document is set as fields, resembling a JavaScript object <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. These fields are used to query a subset of documents based on specific conditions <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

For more in-depth information, you can explore [[using_firebase_databases_and_data_modeling_techniques | data modeling]] in Firestore <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

### Security Rules
Firebase links your [[user_authentication_with_firebase | user authentication]] system directly to your database <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>. Under the rules tab, you can write expressive statements to define backend security logic, for instance, limiting access to certain documents to only logged-in users <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

### Indices
By default, an index is created for every field on a document <a class="yt-timestamp" data-t="00:49:49">[00:49:49]</a>. However, for queries involving multiple fields, custom indices may need to be created <a class="yt-timestamp" data-t="00:56:58">[00:56:58]</a>.

## Working with Firestore in JavaScript

After replacing the Firebase database import with Firestore <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, you can interact with your database using JavaScript.

### Retrieving a Document
To retrieve a single document, you first make a reference to the Firestore database, then to the specific collection and document ID <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The `get()` method is then called, which is an asynchronous operation returning a promise that resolves with the document data <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.

### Realtime Updates with `onSnapshot()`
One of Firebase's major benefits is its ability to listen to data changes in real time <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. If data is shared between multiple users and changes, all users are notified immediately <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This is achieved by using `onSnapshot()` instead of `get()` <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. `onSnapshot()` returns a real-time stream that can be listened to with a callback function <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. Every time the document changes, a new document is emitted to this function, which can then update the user interface <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.

### Updating a Document
Documents can also be updated from client-side code. After making a document reference, the `update()` method is called, passing the new information <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Firestore performs **optimistic updates** (or latency compensation), immediately updating the view if a real-time listener is active, providing a smoother user experience <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

### Querying Collections
To query a collection of documents:
1.  Make a reference to the collection <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
2.  Use the `where()` method to get a subset of documents. It takes three arguments: the field to sort by, an operator (e.g., equal to, greater than), and the value <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
3.  Use `orderBy()` to return documents in a specific order, such as by price descending <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
4.  Chain the `limit()` method to cap the number of documents returned <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>.
5.  Call `get()` (or `onSnapshot()` for real-time queries) to return an array of documents, which then need to be looped over to extract data <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.

## Cloud Functions with Firestore Triggers

Cloud Functions provide a Node.js serverless environment where you can write microservices <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. They can be triggered in various ways, including by Firestore database events <a class="yt-timestamp" data-t="00:43:17">[00:43:17]</a>.

To set up a function triggered by Firestore:
1.  Initialize functions in your project <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.
2.  Define your function in `index.js` within the `functions` directory <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
3.  Use `firestore.onDocumentCreate()` (or similar triggers like `onUpdate`, `onDelete`) to listen for events on specific documents or collections <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. A wildcard can be used in the path (e.g., `{productID}`) to trigger for any document creation in a collection <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.
4.  Inside the trigger, you receive an event object with information about the incoming request, including document ID and data <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>.
5.  The Firebase Admin SDK can be used within functions, bypassing security rules, to perform operations like updating the original document based on the trigger <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.
6.  Deploy the function using `firebase deploy functions` <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.

This allows for backend logic to interact seamlessly with your Firestore data, facilitating complex operations like sending messages from a function back to the database after a document is created <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.