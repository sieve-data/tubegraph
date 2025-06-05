---
title: Key serverless platforms AWS Lambda Google Cloud Functions Azure Functions
videoId: W_VV2Fx32_Y
---

From: [[fireship]] <br/> 

[[introduction_to_serverless_computing | Serverless computing]] describes servers in the cloud that require zero configuration or maintenance from the developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These services manage the CPU and memory required to run your code, sending a bill at the end of the month factored down to the millisecond <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

Key platforms offering [[introduction_to_serverless_computing | serverless computing]] services include:
*   AWS Lambda <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   Google Cloud Functions <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Azure Functions <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

The core [[benefits_of_serverless_architecture | benefit]] of this approach is that developers' only concern is writing code <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The cloud handles the operating system, network configuration, patch improvements, and provisioning capacity for scale <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

[[benefits_of_serverless_architecture | Serverless functions]] allow for the independent development and testing of each business requirement, rather than being part of a larger monolithic system <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. They can also be executed based on different events that happen in the cloud, simplifying backend code <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For example, a new database record might trigger a [[introduction_to_serverless_computing | serverless function]] to send an email confirmation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, or an IoT event could invoke a function to send a push notification <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Google Cloud Functions: Firebase Cloud Functions

One of the easiest ways to get started with [[introduction_to_serverless_computing | serverless]] is [[setting_up_firebase_cloud_functions | Firebase Cloud Functions]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The command-line tool provides a project structure similar to a Node.js backend <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Developers can export named functions configured to run on various Google Cloud events <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, including:
*   HTTP requests <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   File uploads <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Database writes <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Analytics events <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>

After writing the code, it can be deployed to production with a single command, resulting in a reliable backend ready to scale <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### [[structuring_and_deploying_serverless_applications | Structuring and Deploying Serverless Applications]] with Firebase

[[building_serverless_backends_with_firebase_and_flutter | Building a serverless backend for non-trivial apps]] with Firebase Cloud Functions requires a structured approach to manage dozens of functions <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The backend can be built around the strengths of Firebase, focusing on two main types of functions <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>:

1.  **Reactive Functions**: These functions run in reaction to data or state updates on the backend <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Examples include:
    *   A file being uploaded to [[AWS Storage Solutions | Cloud Storage]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   A document or entry in the [[AWS Database Offerings | database]] being updated <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  **Restful Functions**: These are traditional functions that run when a client makes an HTTP request to the URI assigned to the function <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

#### Code Structure for Firebase Cloud Functions

An enforced code structure helps with organization and maintenance as the backend grows <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>:
*   **Dedicated Files**: Each function resides in its own dedicated file, preventing the `index` file from growing excessively <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The file name should ideally be the exact name of the endpoint or function for easy management <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Categorized Folders**: Functions are placed in folders titled either `restful` or `reactive` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Resource Groups**: The backend is split into different resource groups (e.g., `orders`, `payments`, `users`) to ensure a structured backend in production <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Each resource group contains its own `reactive` and `restful` folders <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

#### Setting up a Firebase Functions Project

To set up a Firebase functions project, navigate to your backend folder and run `firebase init` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
1.  Select `firestore`, `functions`, and `emulators` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Choose to create a new project or use an existing one <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  For the functions setup, TypeScript is typically used <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
4.  Select `functions` and `firestore` for emulators, and enable the emulator UI <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

The functions code will reside in a folder named `functions` <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

#### Implementing Backend with `firebase-backend`

To implement the described backend system, install the `firebase-backend` package within the `functions` folder by running `npm install firebase-backend` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. In the `index.ts` file, import `functionParser` from `firebase-backend` and set `exports` to a new `functionParser` instance, passing the current directory name and `exports` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This minimalist `index.ts` file is sufficient regardless of backend size <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

#### Example: Creating a Restful Endpoint

1.  Create a resource group folder (e.g., `users`).
2.  Inside `users`, create a `restful` folder.
3.  Inside `restful`, create a new file, ensuring it ends with `.endpoint.ts` (e.g., `addPaymentMethod.endpoint.ts`) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
4.  Import `request` and `response` from `express`, and `endpoint` and `requestType` from `firebase-backend` <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
5.  Export a default new `endpoint` instance, providing the endpoint name (e.g., `addPaymentMethod`), the request type (e.g., `requestType.post`), and the Express endpoint handler function that processes requests and sends responses <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

To test Restful functions, run `npm run serve`, which builds the TypeScript code and serves functions locally through the emulator <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Each resource group's API endpoints will be found under a URL ending in `<resource-group>-api` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

#### Example: Creating a Reactive Function

1.  Create a new folder in the resource group (e.g., `users`) called `reactive` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
2.  Inside `reactive`, create a new file, ensuring it ends with `.function.ts` (e.g., `onUserCreated.function.ts`) <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
3.  Import `firebase-functions` as `functions` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
4.  On `exports`, create a new function (e.g., `onUserCreated`) and assign it to an `onCreate` function callback provided by Firestore, specifying the document pattern to listen to (e.g., `users/{userId}`) <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
5.  The callback function provides the user's snapshot and event context <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

To test a Reactive function, all emulators must be started <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. First, run `npm run build`, then `firebase emulators:start` <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This starts functions and Firestore emulators <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. Creating a document in the specified collection (e.g., `users`) within the Firestore emulator should trigger the reactive function, and its logs will appear in the console <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

#### Improving Deployment and Debugging

To ensure consistent deployments and debugging, it's recommended to add the `rimraf` package to the `functions` folder as a development dependency (`npm install -D rimraf`) <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   Add a `clean` script in `package.json`: `"clean": "rimraf lib"` <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   Add a `prebuild` script: `"prebuild": "npm run clean"` <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. This ensures old code is deleted before new code is built <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   To deploy, run `npm run build` followed by `npm run deploy` <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.