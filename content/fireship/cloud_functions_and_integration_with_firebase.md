---
title: Cloud functions and integration with Firebase
videoId: 9kRgVxULbag
---

From: [[fireship]] <br/> 

[[building_serverless_backends_with_firebase_and_flutter | Cloud Functions]] are a powerful part of [[introduction_to_firebase_and_benefits | Firebase]], allowing you to run backend code in response to events triggered by [[introduction_to_firebase_and_benefits | Firebase]] features and HTTPS requests <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. They function as a Node.js server that runs on demand <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

## Key Concepts and Benefits

Instead of building a monolithic backend framework, [[building_serverless_backends_with_firebase_and_flutter | Cloud Functions]] enable the creation of microservices that perform specific tasks <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. Any operation possible in Node.js can be executed within a function <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. Developers can install any NPM packages into their functions environment, leveraging the vast Node.js ecosystem for various functionalities <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

[[enhancing_applications_with_firebase_extensions_and_integrations | Cloud Functions]] can be used for advanced operations such as:
*   Interacting with machine learning APIs <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>
*   Handling payments <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>
*   Sending emails <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>
*   Backend chatbot integration <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>

## Setting Up Cloud Functions

To initialize [[setting_up_firebase_cloud_functions | Cloud Functions]] in a [[introduction_to_firebase_and_benefits | Firebase]] project, run `firebase init functions` from the command line <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. This command creates a new `functions` directory, which segregates all the backend code <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

Inside the `functions` directory:
*   A `package.json` file defines all third-party NPM dependencies <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   The `index.js` file is where functions are defined <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

### Firebase Admin SDK

[[enhancing_applications_with_firebase_extensions_and_integrations | Cloud Functions]] can utilize the [[enhancing_applications_with_firebase_extensions_and_integrations | Firebase]] Admin SDK <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This SDK is exclusively for backend environments and can bypass any security rules defined in the [[introduction_to_firebase_and_benefits | Firebase]] app <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

## Triggering Cloud Functions

Functions can be triggered in various ways <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. A common method is using a [[introduction_to_firebase_and_benefits | Firestore]] database trigger <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. This involves listening to a specific document or collection, and the function code executes when a new document is created, updated, or deleted <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

For example, to trigger a function when a new document is created in the `products` collection:
`exports.sendMessage = functions.firestore.document('products/{productId}').onCreate((event) => { /* function logic */ });` <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>

*   `{productId}` acts as a wildcard, causing the function to run for any new document created in the `products` collection <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
*   The `event` object provides information about the incoming request <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>, including the document ID from `event.params` <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a> and the document data from `event.data.data()` <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

### Example: Sending Data Back to the Database

A [[enhancing_applications_with_firebase_extensions_and_integrations | Cloud Function]] can receive data and send it back as an update to the same document in [[introduction_to_firebase_and_benefits | Firebase]] [[introduction_to_firebase_and_benefits | Firestore]] <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. This demonstrates how information can be shared between backend code and the database <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

```javascript
// Example in index.js within the functions directory
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

exports.sendMessage = functions.firestore
  .document('products/{productId}')
  .onCreate((snapshot, context) => { // 'event' was 'snapshot' in newer Firebase functions
    const productData = snapshot.data();
    const productId = context.params.productId;
    const productName = productData.name;

    // Send data back as an update to the same document
    return admin.firestore().collection('products').doc(productId).update({
      message: `Product "${productName}" was created via a Cloud Function.`
    });
  });
```

The function must return a promise, and it terminates once that promise resolves <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

## Deploying Cloud Functions

After defining functions, deploy them to [[introduction_to_firebase_and_benefits | Firebase]] by running `firebase deploy functions` <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Deployment can be verified in the [[introduction_to_firebase_and_benefits | Firebase]] console under the "Functions" tab, where basic analytics are also available <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. Once deployed, adding a document to the specified [[introduction_to_firebase_and_benefits | Firestore]] collection will trigger the function and show the update after a short latency <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.