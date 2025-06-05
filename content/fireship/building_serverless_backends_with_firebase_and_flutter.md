---
title: Building serverless backends with Firebase and Flutter
videoId: W_VV2Fx32_Y
---

From: [[fireship]] <br/> 

Serverless computing is a term used to describe servers in the cloud that require zero configuration or maintenance from the developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach allows developers to focus solely on writing code, without concerns about picking an operating system, configuring networking, patching improvements, or provisioning capacity for scale <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Cloud providers handle all backend infrastructure <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

Examples of serverless computing services include AWS Lambda, Google Cloud Functions, and Azure Functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These services allow backend code to run across global data centers, with billing factored down to the millisecond based on CPU and memory usage <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. From an architectural perspective, serverless computing enables the development and testing of each business requirement independently of a larger monolithic system <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Serverless Functions and Event-Driven Architecture

Serverless functions not only make servers easier to manage but can also be executed based on various events in the cloud, simplifying backend code <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Examples of event-driven triggers:
*   Creating a new database record (e.g., when a user places an order) can trigger a serverless function to send an email confirmation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   An IoT event on a home security system can invoke a function to send a push notification to a user's device <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Building Serverless Backends with [[setting_up_firebase_cloud_functions | Firebase Cloud Functions]]

One of the easiest ways to get started with serverless computing is using [[setting_up_firebase_cloud_functions | Firebase Cloud Functions]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The command-line tool provides a project resembling a Node.js backend <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Named functions can be exported and configured to run on different Google Cloud events <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. These events can include HTTP requests, file uploads, database writes, or analytics events <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. After writing the code, it can be deployed to production with a single command, resulting in a reliable and scalable backend <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

This guide leverages [[Firebase Cloud Functions | Firebase's]] strengths to build a structured and maintainable serverless backend for non-trivial applications <a class="yt-timestamp" data-t="02:53">[02:53]</a>.

### Types of [[cloud_functions_and_integration_with_firebase | Cloud Functions]]

The system can be broken down into two main types of functions <a class="yt-timestamp" data-t="03:00">[03:00]</a>:

1.  **Reactive Functions**: These functions run in reaction to data or state updates on the backend <a class="yt-timestamp" data-t="03:07">[03:07]</a>.
    *   Examples include when a file is uploaded to Cloud Storage or when a document in the database is updated <a class="yt-timestamp" data-t="03:15">[03:15]</a>.
2.  **Restful Functions**: These are traditional RESTful functions that run when a client makes an HTTP request to a specific URI <a class="yt-timestamp" data-t="03:24">[03:24]</a>.

### Code Structure

An enforced code structure helps with organization and overall maintenance as the backend grows <a class="yt-timestamp" data-t="03:35">[03:35]</a>.

Key structural principles:
*   **Dedicated Files**: Each function resides in its own dedicated file to prevent the `index` file from growing excessively <a class="yt-timestamp" data-t="03:47">[03:47]</a>. The file name should ideally match the endpoint or function name for easy management <a class="yt-timestamp" data-t="04:03">[04:03]</a>.
*   **Categorized Folders**: Functions are placed in a folder titled either `restful` or `reactive` <a class="yt-timestamp" data-t="04:13">[04:13]</a>.
*   **Resource Groups**: The backend is split into different resource groups (e.g., `orders`, `payments`, `users`) to ensure a structured backend in production <a class="yt-timestamp" data-t="04:18">[04:18]</a>. Each resource group will contain `reactive` and `restful` subfolders <a class="yt-timestamp" data-t="04:31">[04:31]</a>.

## Implementation Steps

### Initial Setup

1.  **Create Project Folders**: Create a new folder (e.g., `boxed_out`) and inside it, a `backend` folder <a class="yt-timestamp" data-t="04:53">[04:53]</a>.
2.  **Initialize Firebase**: Navigate into the `backend` folder and run `firebase init` <a class="yt-timestamp" data-t="05:01">[05:01]</a>.
    *   Select `firestore`, `functions`, and `emulators` <a class="yt-timestamp" data-t="05:09">[05:09]</a>.
    *   Choose to create a new project (e.g., `boxed-out-backend`) <a class="yt-timestamp" data-t="05:14">[05:14]</a>.
    *   If Firestore setup fails initially (which is common), go to the provided URL, click "Get started", then "Create database" (start in test mode) <a class="yt-timestamp" data-t="05:24">[05:24]</a>. Select a region (e.g., Europe West) <a class="yt-timestamp" data-t="05:40">[05:40]</a>.
    *   Run `firebase init` again <a class="yt-timestamp" data-t="05:49">[05:49]</a>. Select `firestore`, `functions`, and `emulators` <a class="yt-timestamp" data-t="05:54">[05:54]</a>. Use the existing project created earlier <a class="yt-timestamp" data-t="05:59">[05:59]</a>.
    *   Select default values for questions <a class="yt-timestamp" data-t="06:06">[06:06]</a>.
    *   For functions setup, use TypeScript <a class="yt-timestamp" data-t="06:11">[06:11]</a>. Decline ESLint for now <a class="yt-timestamp" data-t="06:13">[06:13]</a>. Confirm installation of dependencies <a class="yt-timestamp" data-t="06:15">[06:15]</a>.
    *   For emulators, select `functions` and `firestore` <a class="yt-timestamp" data-t="06:19">[06:19]</a>. Press Enter for default ports <a class="yt-timestamp" data-t="06:23">[06:23]</a>. Enable the emulator UI <a class="yt-timestamp" data-t="06:27">[06:27]</a>. If emulators aren't downloaded, select yes to download them <a class="yt-timestamp" data-t="06:30">[06:30]</a>.
3.  **Install `firebase-backend` Package**: Navigate into the `functions` folder and run `npm install firebase-backend` <a class="yt-timestamp" data-t="07:11">[07:11]</a>.
4.  **Modify `index.ts`**:
    *   Open `functions/src/index.ts` <a class="yt-timestamp" data-t="07:20">[07:20]</a>.
    *   Delete existing code <a class="yt-timestamp" data-t="07:22">[07:22]</a>.
    *   Import `FunctionParser` from `firebase-backend` <a class="yt-timestamp" data-t="07:27">[07:27]</a>.
    *   Set `exports` equal to a new `FunctionParser` instance, passing `__dirname` and `exports` <a class="yt-timestamp" data-t="07:31">[07:31]</a>. This minimalist `index.ts` handles all backend loading <a class="yt-timestamp" data-t="07:47">[07:47]</a>.

    ```typescript
    // functions/src/index.ts
    import { FunctionParser } from 'firebase-backend';

    exports = new FunctionParser(__dirname, exports);
    ```

### Creating a Restful Endpoint

1.  **Folder Structure**: Create a resource group folder (e.g., `users`) inside `functions/src/` <a class="yt-timestamp" data-t="08:01">[08:01]</a>. Inside `users`, create a `restful` folder <a class="yt-timestamp" data-t="08:07">[08:07]</a>.
2.  **Create Endpoint File**: Create a new file inside `users/restful/` called `addPaymentMethod.endpoint.ts` <a class="yt-timestamp" data-t="08:11">[08:11]</a>. The file must end in `.endpoint.ts` to be loaded as an HTTP endpoint <a class="yt-timestamp" data-t="08:16">[08:16]</a>.
3.  **Implement Endpoint**:
    *   Import `Request` and `Response` from `express`, and `Endpoint` and `RequestType` from `firebase-backend` <a class="yt-timestamp" data-t="08:26">[08:26]</a>.
    *   Export a default new `Endpoint` instance <a class="yt-timestamp" data-t="08:36">[08:36]</a>.
    *   The constructor takes:
        *   The endpoint name (e.g., `"addPaymentMethod"`) <a class="yt-timestamp" data-t="08:43">[08:43]</a>.
        *   The request type (e.g., `RequestType.POST`) <a class="yt-timestamp" data-t="08:50">[08:50]</a>.
        *   The Express endpoint handler function, which takes `request` and `response` objects <a class="yt-timestamp" data-t="08:56">[08:56]</a>.
    *   Inside the handler, read values from `request.body` and send a response <a class="yt-timestamp" data-t="09:11">[09:11]</a>.

    ```typescript
    // functions/src/users/restful/addPaymentMethod.endpoint.ts
    import { Request, Response } from 'express';
    import { Endpoint, RequestType } from 'firebase-backend';

    export default new Endpoint(
        'addPaymentMethod',
        RequestType.POST,
        async (request: Request, response: Response) => {
            const { cardNumber, cardHolder } = request.body;
            const paymentToken = `${cardNumber}_${cardHolder}`;
            return response.status(201).send({ token: paymentToken });
        }
    );
    ```

4.  **Test the Endpoint**:
    *   Run `npm run serve` in the `functions` folder <a class="yt-timestamp" data-t="10:00">[10:00]</a>. This builds TypeScript and serves functions locally via the emulator <a class="yt-timestamp" data-t="10:04">[10:04]</a>.
    *   The console will display the API URL, typically ending in `users-api` for the `users` resource group <a class="yt-timestamp" data-t="10:16">[10:16]</a>.
    *   Use a tool like Postman to make a POST request to `[API_URL]/addPaymentMethod` <a class="yt-timestamp" data-t="10:37">[10:37]</a>.
    *   Send a JSON body with `cardNumber` and `card_holder` <a class="yt-timestamp" data-t="10:56">[10:56]</a>. The expected response is a JSON object with a `token` key <a class="yt-timestamp" data-t="11:13">[11:13]</a>.

### Creating a Reactive Function

1.  **Folder Structure**: Stop the emulators (`Ctrl+C`) <a class="yt-timestamp" data-t="11:26">[11:26]</a>. Create a `reactive` folder inside `functions/src/users/` <a class="yt-timestamp" data-t="11:38">[11:38]</a>.
2.  **Create Function File**: Create a new file inside `users/reactive/` called `onUserCreated.function.ts` <a class="yt-timestamp" data-t="11:44">[11:44]</a>. The file must end in `.function.ts` to be loaded as a reactive cloud function <a class="yt-timestamp" data-t="11:53">[11:53]</a>.
3.  **Implement Function**:
    *   Import `firebase-functions` as `functions` <a class="yt-timestamp" data-t="11:58">[11:58]</a>.
    *   On the `exports` object, create a new function (e.g., `onUserCreated`) <a class="yt-timestamp" data-t="12:02">[12:02]</a>.
    *   Assign it to the `onCreate` function callback provided by a Firestore document trigger <a class="yt-timestamp" data-t="12:09">[12:09]</a>.
    *   Specify the document pattern to listen to (e.g., `users/{userId}`) <a class="yt-timestamp" data-t="12:22">[12:22]</a>.
    *   The `onCreate` callback provides a `userSnapshot` and `context` <a class="yt-timestamp" data-t="12:35">[12:35]</a>.
    *   Log a message indicating an email has been sent to the user's email address from the document data <a class="yt-timestamp" data-t="12:53">[12:53]</a>.

    ```typescript
    // functions/src/users/reactive/onUserCreated.function.ts
    import * as functions from 'firebase-functions';

    exports.onUserCreated = functions.firestore
        .document('users/{userId}')
        .onCreate(async (userSnapshot, context) => {
            const userData = userSnapshot.data();
            functions.logger.log(`Sent email to ${userData?.email}`);
        });
    ```

4.  **Test the Function**:
    *   Reactive functions require all emulators to be started. First, run `npm run build` in the `functions` folder <a class="yt-timestamp" data-t="13:04">[13:04]</a>.
    *   Once the build is complete, run `firebase emulators:start` <a class="yt-timestamp" data-t="13:17">[13:17]</a>. This starts functions and Firestore emulators <a class="yt-timestamp" data-t="13:22">[13:22]</a>.
    *   The console will show URLs for the functions and Firestore emulators, and confirm the `onUserCreated` function is deployed <a class="yt-timestamp" data-t="13:31">[13:31]</a>.
    *   Open the Firestore emulator URL <a class="yt-timestamp" data-t="13:51">[13:51]</a>.
    *   Click "Start collection", set collection ID to `users`, and add a field named `email` with a value (e.g., `dane@fullstacks.com`) <a class="yt-timestamp" data-t="13:54">[13:54]</a>.
    *   Click "Save". When the document is created, the `onUserCreated` function will fire, and logs indicating email sending will appear in the console <a class="yt-timestamp" data-t="14:13">[14:13]</a>.

## Improving Code Setup for Production

To ensure consistent deployments and easier debugging, especially as the project scales, additional scripts can be added to the `package.json` file <a class="yt-timestamp" data-t="14:44">[14:44]</a>.

1.  **Install `rimraf`**: Navigate into the `functions` folder and run `npm install -D rimraf` <a class="yt-timestamp" data-t="15:04">[15:04]</a>. This installs `rimraf` as a development dependency for cleaning directories <a class="yt-timestamp" data-t="15:11">[15:11]</a>.
2.  **Add Scripts to `package.json`**: Open `functions/package.json` and add the following scripts above the `build` script <a class="yt-timestamp" data-t="15:17">[15:17]</a>:

    ```json
    "scripts": {
        "clean": "rimraf lib",
        "pre-build": "npm run clean",
        "build": "tsc",
        "serve": "npm run build && firebase emulators:start --only functions",
        "shell": "npm run build && firebase functions:shell",
        "start": "npm run shell",
        "deploy": "firebase deploy --only functions",
        "logs": "firebase functions:log"
    }
    ```
    *   `clean`: Deletes the `lib` directory (where TypeScript output goes) <a class="yt-timestamp" data-t="15:24">[15:24]</a>.
    *   `pre-build`: Runs `clean` before every `build`, ensuring old code is removed before new code is compiled <a class="yt-timestamp" data-t="15:33">[15:33]</a>.

3.  **Deploy**: To deploy the functions to your [[deploying_and_hosting_applications_with_firebase | Firebase]] backend, run `npm run build` followed by `npm run deploy` <a class="yt-timestamp" data-t="15:46">[15:46]</a>. The API link will be printed upon successful deployment <a class="yt-timestamp" data-t="16:00">[16:00]</a>.

This structured approach to developing a backend on [[cloud_functions_and_integration_with_firebase | Firebase]] provides a clear path towards a large and maintainable [[deploying_and_hosting_applications_with_firebase | Firebase]] product <a class="yt-timestamp" data-t="16:08">[16:08]</a>.

---
*Based on content presented by Dane from the Filled Stacks YouTube channel <a class="yt-timestamp" data-t="01:54">[01:54]</a>.*