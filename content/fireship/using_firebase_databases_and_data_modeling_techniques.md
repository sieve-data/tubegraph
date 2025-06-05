---
title: Using Firebase databases and data modeling techniques
videoId: iWEgpdVSZyg
---

From: [[fireship]] <br/> 

Firebase provides two fully managed NoSQL databases: Cloud Firestore and the Realtime Database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Understanding their differences and how to model data within them is crucial for application development.

## Choosing a Firebase Database

When selecting a database, Cloud Firestore is generally the default choice due to its more powerful query capabilities and lower cost per gigabyte stored <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. However, the Realtime Database does not charge for writes, making it a strong option for data that updates very frequently, such as from an IoT sensor <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Generally, Firebase databases are very inexpensive, and it takes a significant number of monthly active users to exceed the free tier <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## [[working_with_firebase_firestore_and_realtime_updates | Working with Firebase Firestore]]

### Initial Setup and Queries

When creating a new database, it's safer to start in "locked mode" and then incrementally allow operations as needed <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

You can make queries directly from the Firebase console using the filter icon, which also provides code snippets for your query <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Importing Firebase in Code

When importing Firebase into your JavaScript application, import from the `firebase/app` namespace and then import only the specific services you plan to use to avoid creating a large JavaScript bundle <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. For web applications loading Firebase via a script tag, use the `defer` keyword to ensure it loads after the DOM is parsed <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Frameworks like Angular should use AngularFire, while React apps can use ReactFire for hooks and Suspense support <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. RxFire is available for RxJS integration, common in frameworks like Svelte <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Data Retrieval Strategies

*   **One-Time Retrieval:** To optimize pricing and avoid real-time updates, use `query.get()` to retrieve data once <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Real-time Updates:** For features where the UI should react to changes in real-time, use `query.onSnapshot()` to run a callback function anytime the underlying data changes <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
    *   `docs` provides a new array on data change <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   `docChanges` provides an array indicating which documents were added, modified, or removed, along with their old and new indexes and change type <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Offline Capabilities

Firestore can work offline <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. If the internet goes out, Firestore updates the UI and sends writes to the database once the connection is restored <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This can also be synchronized across multiple browser tabs by setting the `synchronizedTabs` option to `true` <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Advanced Query Techniques

*   **Emoji Support:** Emojis are UTF-8 characters and can be used in Firestore documents and queried <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Wildcard String Matching:** To query documents starting with a specific string (e.g., "The Fast and the Furious"), create a starting point and an ending point using a tilde character (e.g., `the_fast_and_the_furious~`) <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
*   **Compound Queries and Indexing:** Compound queries require an index <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. If an index is missing, the app will throw an error, and you can click the provided link to the Firestore console to create it automatically <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Array Queries:** Use the `array-contains` operator in `where` clauses to query documents based on whether an array field contains a specific value <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Fetching Related Documents from an Array of IDs:** Map an array of document IDs to an array of promises that fetch each document, then use `Promise.all` to run them together <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

### Data Manipulation

*   **Arrays:**
    *   Add items to a list on a document using a JavaScript array <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    *   Use `arrayUnion()` to ensure an array includes exactly one instance of a specific value <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   Use `arrayRemove()` to remove a specific value from an array without needing to know its index <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Timestamps:** Avoid setting timestamps from frontend code as the user's clock might be unsynchronized <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. Instead, use `FieldValue.serverTimestamp()` to ensure all users share the same accurate timestamp <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Counters:** Increment a counter atomically without knowing its current value using `FieldValue.increment()` <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   **Distributed Counters:** Firestore supports one write per document per second, with burst capability <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. For high write volumes on a single document, use a distributed counter, which is simplified by a Firebase extension <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Batch Writes:** For operations that need to succeed or fail together (atomic writes), use batch writes <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. A batch commit ensures all writes happen together but rolls back to the previous state if any write fails <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

## [[firestore_data_modeling_techniques | Data Modeling Techniques]]

Firestore offers flexible ways to manage relational data within its NoSQL structure <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### One-to-One Relationships

For a one-to-one relationship, a user might have one document in Firestore <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Retrieve the user ID, then set the document ID in a collection as the user ID, guaranteeing uniqueness <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Use the `merge: true` option with `set()` to ensure existing data is not overwritten, performing a non-destructive update <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### One-to-Many Relationships (Subcollections)

A common one-to-many relationship (e.g., a user having many orders) is best handled using subcollections <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. A subcollection under a user's document is owned by that user <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Querying Across Subcollections

If you need to query across all subcollections of the same name (e.g., all "orders" across all users), Firebase provides a special method called `collectionGroup()` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This groups all collections with the specified name, allowing a single query against them <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### [[data_modeling_in_firestore_chat_applications | Many-to-Many Relationships]]

For many-to-many relationships (e.g., multiple users in a single chat), embed user IDs on the chat document using a map of key-value pairs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The key can be the user ID, and you might duplicate display names for UI convenience <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Data Duplication ([[normalized_data_models_and_document_joining_in_firestore | Denormalization]])

Data duplication (denormalization) is acceptable in NoSQL databases like Firestore <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. It can optimize for performance and cost, especially when dealing with values that are immutable or don't need frequent updates <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Once you have a map object where each key is a user ID, you can query it using dot notation in your queries, such as `orderBy('members.userId')` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Database Management and Best Practices

### Cost Management

While Firebase is generally inexpensive, it's essential to monitor costs <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Upgrade to the Blaze (pay-as-you-go) plan to access all features while still getting the free tier benefits <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Set up budget alerts in the GCP console and monitor monthly usage from the reports panel to identify costly services <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Backups

Regularly back up your data <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Set up a dedicated Cloud Storage bucket for backups, potentially using Coldline storage for cost savings <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a><a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. An entire database can be backed up with a single command or via the REST API for scheduled cron jobs <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a><a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

### Security Rules

Set up robust security rules before deploying to production to prevent data compromise and destructive writes <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Simulator:** Use the simulator in the Firebase console to pass mock requests and see how rules are evaluated <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Emulator:** For serious production apps, use the Firestore emulator to simulate the database locally and test rules comprehensively <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Operation Types:** Define fine-grained rules for five operation types: `get` (single document), `list` (querying documents), `create`, `update`, and `delete` <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. Combine rules using `read` or `write` keywords if they share the same logic <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   **Request and Resource:** Rules evaluate based on the `request` (user's auth state, incoming data) and `resource` (existing data at the path) <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Cross-Document Reads:** Use the `get()` keyword to look up data elsewhere in the database to determine if a rule should be allowed <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. Be aware that this incurs a read charge each time the rule is evaluated <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Functions:** Extract complex logic into functions (e.g., `isAdmin()`) for cleaner, reusable rules <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Backend Operations (Admin SDK, REST API)

*   **Admin SDK:**
    *   Set up a command-line utility for Firebase by downloading the service account for your project <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Install `firebase-admin` and initialize it with your service account <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. The safest way to use service accounts locally is via an environment variable (`GOOGLE_APPLICATION_CREDENTIALS`) <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. If included in source code, add it to `.gitignore` <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   Use the Admin SDK to seed the database with dummy data, for example, by integrating with `faker.js` <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **REST API:** The Firebase REST APIs offer additional techniques beyond the Admin SDK, including database backups via cron jobs <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. The `google-api-nodejs-client` NPM package can help interact with Google APIs <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.
*   **Cloud Functions:**
    *   Cloud functions are commonly used with Firebase Admin SDK <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. Use TypeScript for setup and error catching <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
    *   **Performance:** Minimize dependencies for faster cold starts <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Use global variables for values shared across multiple function invocations <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
    *   **Idempotency:** Design functions to be idempotent, meaning multiple calls produce the same result, as functions can be retried <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. Use `context.eventId` to help achieve this <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
    *   **Resources:** Increase memory (to 2GB) and timeout (to 540 seconds) using `runWith()` for more demanding functions <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
    *   **Infinite Loops:** Avoid accidental infinite loops, especially in Firestore `onWrite` functions that update the same document that triggered them <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Prevent this by checking `after.isEqual(before)` to ensure the document path and data haven't changed <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.
    *   **Promises:** Background cloud functions must always return a promise <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Use `async/await` for cleaner, synchronous-looking code <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
    *   **Inter-Service Communication:** Use Pub/Sub functions to pass messages securely between internal services, a better alternative than exposing HTTP endpoints <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
    *   **Callable Functions:** Simplify backend and frontend code for authenticated endpoints by using callable functions, which include the user's auth context without needing custom middleware <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
    *   **Deleting Collections:** Deleting entire Firestore collections should always be done on the backend via a recursive batch delete function to avoid memory issues with millions of documents <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
    *   **Modularity:** Break down backend logic into small JavaScript functions for code reuse and easier testing <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. Cloud functions act as a gateway to interact with other third-party APIs <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.
    *   **Deployment:** Deploy all functions with a single command or specify a function name to deploy individually <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
    *   **Debugging:** Run the Cloud Functions shell locally to invoke functions with mock data <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. Firebase provides a unit testing library <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. Production bugs can be investigated using Firebase logs or Stackdriver for custom dashboards and alerts <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.

### Machine Learning Integration

Firebase can be used to leverage machine learning within an app:
*   Use Predictions to estimate user purchasing behavior <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.
*   Implement AI-driven features with ML Kit, offering out-of-the-box capabilities like object detection and smart reply <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
*   Build custom image classification models with AutoML <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
*   Export analytics and Firestore data to BigQuery to train custom TensorFlow models <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.