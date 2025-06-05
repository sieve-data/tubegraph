---
title: User authentication with Firebase
videoId: 9kRgVxULbag
---

From: [[fireship]] <br/> 
This article provides an overview of Firebase, focusing on its core features for application development, particularly **User authentication with Firebase**. It covers initial setup, deployment, database management, cloud storage, and serverless functions, all demonstrated with basic JavaScript.

### What is Firebase?
Firebase is a platform that abstracts away the complexities of backend development, allowing developers to focus on building applications more efficiently <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It's considered an excellent platform for building apps due to three main reasons:
*   **Developer Experience**: Firebase is well-documented, easy to use, and its team is responsive to developer feedback <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Minimization of Cost**: It offers a free tier for small, experimental projects and scales linearly with user growth, avoiding sudden, high charges often seen in other platforms <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Maximization of Time**: Firebase helps developers create significant value in the least amount of time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Getting Started with Firebase
To follow along with Firebase development, you'll need a code editor like VS Code and Node.js installed locally <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

#### Firebase Project Setup
A Firebase project acts as a container for various Google Cloud Platform resources, including your database, file storage, and web hosting <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. All app resources can be managed from the Firebase admin console <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. A single project can span multiple platforms, as Firebase provides SDKs for web, iOS, Android, Unity, and more <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. These projects are identified by credentials and integrate seamlessly with other Google Cloud Platform APIs like Cloud Vision or Google Maps <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

To begin, install the Firebase command-line tools globally:
```bash
npm install firebase-tools -g
```
<a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

#### Creating and Deploying a Project
You can quickly create and deploy a project from the command line:
1.  Open an empty folder in VS Code.
2.  Run `firebase init hosting` in the terminal <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This command generates:
    *   `firebase.json`: Contains hosting rules <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   `.firebaserc`: A script to identify your project <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   `public/index.html`: Your actual web application <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
3.  The `index.html` imports the Firebase web SDK in the head of the document <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. You can import modules one by one (e.g., only the database module) to improve page load performance <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Script tags typically use `defer` to ensure the page loads before script execution <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  To serve the app locally, run `firebase serve`. This spins up a web server on port 5000 <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  To deploy the app to a live URL, run `firebase deploy` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Deployed apps automatically include an SSL certificate for HTTPS support and leverage Google's Content Delivery Network (CDN) for highly performant static resource serving <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

After initial setup, you'll typically remove boilerplate code and point your main script tag to a new file, `app.js`, where your application's logic resides <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. You can create this file by running `touch public/app.js` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### User Authentication with Firebase
Firebase significantly simplifies **User authentication with Firebase** compared to traditional methods, often requiring only a few lines of code <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

#### Setting up Google Login
1.  **HTML Setup**: Add a simple HTML button that calls a Google login function when clicked <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
2.  **JavaScript Structure**: Ensure your Firebase code runs after the document content has loaded, as Firebase resources become available then <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. You can access Firebase resources under the `firebase` namespace <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
3.  **Enable Authentication Method**: Before logging in, go to the Firebase console under "Authentication" and enable the desired sign-in methods. For Google login, enable Google as the OAuth provider. Other options include email/password, anonymous, Twitter, Facebook, and GitHub <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
4.  **Login Function**:
    *   Define the provider: `new firebase.auth.GoogleAuthProvider()` <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   Call `firebase.auth().signInWithPopup(provider)` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This is an asynchronous operation that returns a Promise <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
    *   Attach a `.then()` block to handle the resolved promise, which provides the user object <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. The user information comes directly from the Google account <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

#### JSON Web Tokens (JWT)
Firebase uses JSON Web Tokens (JWTs) for authentication, which are encrypted tokens stored in the browser that identify the user <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. JWTs are generally easier to work with than cookies, especially for JavaScript applications like Angular and React <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

#### Managing Users in the Firebase Console
Once a user logs in, their account is created in the Firebase authentication tab in the console <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. From here, you can:
*   Disable accounts <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Update email templates (for email/password authentication) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Perform text message verification <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   View basic analytics <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### Firebase Databases: Cloud Firestore vs. Realtime Database
Firebase offers two NoSQL database options <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>:
1.  **Realtime Database**: Charged $5 per gigabyte stored and $1 per gigabyte downloaded <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Best for simple, frequently read datasets <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
2.  **Cloud Firestore**: Charged 18 cents per gigabyte stored, but also for each individual document read and write operation <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Preferred for larger, more complex, relational datasets <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Cloud Firestore is generally the better choice in most cases <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

#### Cloud Firestore Structure and Operations
Cloud Firestore is structured as collections of documents, similar to MongoDB <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Each document has a unique ID (either self-created or auto-generated) <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a> and contains data as fields, akin to a JavaScript object <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

One of the key benefits of Firebase is the direct tie between the [[user_authentication_with_decentralized_apps | user authentication system]] and the database <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Under the "Rules" tab, you can write expressive statements to define backend security logic, such as restricting document access to logged-in users <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Firestore also automatically builds indices for every field, and custom indices can be created for queries involving multiple fields <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

##### Reading Documents
To retrieve a document:
1.  Make a reference to Firestore: `const db = firebase.firestore()` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
2.  Reference a collection: `db.collection('posts')` <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
3.  Reference a specific document by its ID: `.doc('first-post')` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
4.  Call `.get()` on the document reference. This is an asynchronous operation that returns a promise, resolving with the document data <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

##### Real-time Updates
A major advantage of Firebase is its ability to listen to data changes in real time. If data shared among users changes, all users are instantly notified <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Instead of `.get()`, use `.onSnapshot()` on a document reference <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This returns a real-time stream that can be listened to with a callback function. Every time the document changes, a new snapshot is emitted to this function <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

##### Updating Documents
Documents can be updated from client-side code using the `.update()` method on a document reference, passing the fields to update <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Firestore performs "optimistic updates" or "latency compensation" which means the view updates immediately on the client side without waiting for a server response, improving user experience <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

##### Querying Collections
To query a collection of documents:
1.  Reference the collection: `db.collection('products')` <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
2.  Use `.where()` to filter documents based on conditions. It takes three arguments: the field name, an operator (e.g., `==`, `>`, `>=`, `<`), and the value <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
3.  Use `.orderBy()` to sort documents (e.g., `orderBy('price', 'desc')`) <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
4.  Use `.limit()` to cap the number of documents returned in the array <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
5.  Call `.get()` on the query, which returns an array of documents <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

### Firebase Storage
Firebase Storage provides a cloud storage bucket tied to your Firebase project, ideal for user-generated content like images and videos <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **Rules**: By default, only authenticated users can upload files <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. These rules can be modified to allow public uploads if desired <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   **Uploading Files**: In JavaScript, make a reference to the storage library and a specific path (e.g., `storageRef.child('image.jpg')`) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Then, call `.put()` on the reference with the file data <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. The `.then()` block can be chained to process the upload completion, such as retrieving the `snapshot.downloadURL` to display the uploaded image <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### Firebase Cloud Functions
Cloud Functions are serverless Node.js environments that run on demand <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. Instead of a monolithic backend, you write microservices that perform specific functions. Anything executable in Node.js can be done in a function, including installing NPM packages <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

#### Setting up Firebase Cloud Functions
1.  Initialize functions in your project by running `firebase init functions` <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. This creates a `functions` directory, isolating backend code <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
2.  **Triggers**: Functions can be triggered in various ways. A common method is a Firestore database trigger, where a function runs when a new document is created (or updated/deleted) in a specific collection <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
3.  **Code Structure**:
    *   The `functions` directory contains `package.json` for NPM dependencies and `index.js` for defining functions <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
    *   Cloud Functions can use the `firebase-admin` SDK, which bypasses any security rules defined in your app <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
    *   Define a function using `exports.functionName = firestore.document('collection/{docId}').onCreate(...)` <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. The `{docId}` creates a wildcard for new documents <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   Inside the trigger, you receive an `event` object containing information about the incoming request, including document ID (`event.params`) and data (`event.data.data()`) <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
    *   Functions should return a promise (e.g., from an update operation) to signal completion <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
4.  **Deployment**: Deploy functions by running `firebase deploy functions` <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Deployed functions appear in the Firebase console under the "Functions" tab, along with basic analytics <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

### Additional Features for Native Mobile Apps
Beyond the core development resources, Firebase offers powerful features for native mobile applications:
*   **Testing and Stability**:
    *   **Robo Testing**: Upload your app build, and Firebase runs a suite of tests to identify common crash issues in mobile apps, providing screenshot results for each test <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Analytics**:
    *   **StreamView**: Provides a global geographic representation of your user base in real-time <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   **User Engagement**:
    *   **Push Notifications**: Easily send push notifications based on user segments, specific topics, or to single devices <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
    *   **A/B Testing**: Set up A/B tests for notifications and track their conversion rates <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.