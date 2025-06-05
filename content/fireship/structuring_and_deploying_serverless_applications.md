---
title: Structuring and deploying serverless applications
videoId: W_VV2Fx32_Y
---

From: [[fireship]] <br/> 

[[introduction_to_serverless_computing | Serverless computing]] is a term used to describe servers in the cloud that require zero configuration or maintenance from the developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach is analogous to tapping into a city water supply rather than digging your own well; you pay only for the CPU and memory used by your code <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

Major service providers like [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | AWS Lambda]], [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | Google Cloud Functions]], and [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | Azure Functions]] allow you to run backend code globally, with billing factored down to the millisecond <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The primary [[benefits_of_serverless_architecture | benefit]] of this model is that developers can focus solely on writing code, without concerns for operating systems, networking, patching, or scaling capacity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Architecturally, it supports developing and testing individual business requirements independently of larger monolithic systems <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Event-Driven Functions
Serverless functions can be executed based on various events occurring in the cloud, simplifying backend code <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Examples include:
*   Triggering an email confirmation function when a new database record is created after a user places an order <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Invoking a function to send a push notification from an IoT event on a home security system <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Getting Started with Firebase Cloud Functions
One of the easiest ways to begin with serverless is by using [[setting_up_firebase_cloud_functions | Firebase Cloud Functions]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The command-line tool provides a project structure similar to a [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] backend <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Functions can be exported and configured to run on different Google Cloud events, such as HTTP requests, file uploads, database writes, or analytics events <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. After development, code can be deployed to production with a single command, creating a scalable backend <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Building a Serverless Backend for Complex Projects
For non-trivial applications, structuring dozens of functions to scale and maintain a backend requires careful consideration <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Dane from the Falstax YouTube channel demonstrates how to [[building_serverless_backends_with_firebase_and_flutter | build a serverless backend]] for a product/food delivery service called "Boxed Out," built with [[deploying_and_hosting_applications_with_firebase | Firebase]] and [[building_serverless_backends_with_firebase_and_flutter | Flutter]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Types of Functions
The backend structure leverages the strengths of [[deploying_and_hosting_applications_with_firebase | Firebase]] in a serverless Cloud Functions setup, categorizing functions into two types <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>:

1.  **Reactive Functions:** These functions run in response to data or state updates on the backend <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   *Examples:* When a file is uploaded to Cloud Storage, or a document in a database is updated <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
2.  **Restful Functions:** These are traditional functions that execute when a client makes an HTTP request to a specific URI <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Code Structure
To maintain organization and scalability, an enforced code structure is recommended <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:
1.  **Dedicated Files:** Each function should reside in its own dedicated file, preventing the common practice of continually adding functions to a single, growing `index` file <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The file name should ideally match the endpoint or function name for easier management and debugging <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
2.  **Categorized Folders:** Functions are placed in folders titled `restful` or `reactive` based on their type <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  **Resource Groups:** The backend is split into different resource groups, such as `orders`, `payments`, and `users`, to ensure a structured production environment <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Each resource group will contain both `reactive` and `restful` folders <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Implementation Steps

#### Initial Setup
1.  Create a project folder (e.g., `boxed-out`) and a `backend` subfolder <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
2.  Navigate into the `backend` folder and run `firebase init` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  Select `firestore`, `functions`, and `emulators` <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
4.  Create a new [[deploying_and_hosting_applications_with_firebase | Firebase]] project (e.g., `boxed-out-backend`) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
5.  If Firestore setup fails initially (often due to not having a database created), visit the provided URL, click "Get started," and create a database (e.g., in test mode and choose a region) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
6.  Run `firebase init` again, select `firestore`, `functions`, and `emulators`, then choose the existing `boxed-out-backend` project <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
7.  Select default values for most questions, use TypeScript for functions, and accept ESLint and dependency installation <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
8.  For emulators, select `functions` and `firestore`, press Enter for default ports, and enable the emulator UI <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Download emulators if prompted <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   This setup creates a `functions` folder where backend code will reside <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

#### Implementing the Backend System
1.  Navigate into the `functions` folder <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  Install the `firebase-backend` package: `npm install firebase-backend` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
3.  Open `index.ts` in the `src` folder, delete existing code, and import `functionParser` <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
4.  Set `exports` equal to a new `functionParser` instance, passing the current directory name and `exports` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This minimal `index.ts` file handles backend growth automatically <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

#### Creating a Restful Endpoint
1.  Create a resource group folder (e.g., `users`) inside the `functions/src` directory <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
2.  Inside `users`, create a `restful` folder <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
3.  In `restful`, create a new file named `addPaymentMethod.endpoint.ts` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. (The `.endpoint.ts` suffix is crucial for HTTP endpoint loading) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
4.  **Code Example (`addPaymentMethod.endpoint.ts`):**
    ```typescript
    import { Request, Response } from 'express';
    import { Endpoint, RequestType } from 'firebase-backend';

    export default new Endpoint(
        'addPaymentMethod',
        RequestType.POST,
        (request: Request, response: Response) => {
            const { cardNumber, cardHolder } = request.body;
            const paymentToken = `${cardNumber}_${cardHolder}`;
            response.status(201).send({ token: paymentToken });
        }
    );
    ```
5.  **Testing:**
    *   Run `npm run serve` to build TypeScript code and serve functions locally through the emulator <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   The console will display the API URL (e.g., ending in `users-api`) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Use a tool like Postman:
        *   Paste the API URL into the Postman URL field <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
        *   Append `/addPaymentMethod` to the URL <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
        *   Change request type to `POST` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
        *   In the body, send a JSON blob with `cardNumber` (e.g., `1234567`) and `card_holder` (e.g., `Falstax`) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
        *   Executing this request should return a token combining the card number and holder <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

#### Creating a Reactive Function
1.  Stop the emulators <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
2.  In the `users` folder, create a new folder called `reactive` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
3.  Inside `reactive`, create a new file named `onUserCreated.function.ts` <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. (The `.function.ts` suffix is essential for reactive Cloud Function loading) <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
4.  **Code Example (`onUserCreated.function.ts`):**
    ```typescript
    import * as functions from 'firebase-functions';

    export const onUserCreated = functions.firestore
        .document('users/{userId}')
        .onCreate((snapshot, context) => {
            const userData = snapshot.data();
            console.log(`Email sent to ${userData?.email}`);
            return null; // Important for Cloud Functions to indicate completion
        });
    ```
5.  **Testing:**
    *   Reactive functions require all emulators to be started.
    *   Run `npm run build` <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
    *   Then, run `firebase emulators:start` <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This will start both functions and Firestore emulators <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
    *   Confirm `onUserCreated` is listed as a deployed function <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
    *   Open the Firestore emulator URL <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   Click "Start collection," name it `users` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
    *   Add a document with a field named `email` (e.g., `dane@falstax.com`) <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   Upon saving, the `onUserCreated` function should fire automatically, and logs indicating "Email sent to..." will appear in the console <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

### Improving Code Setup for Consistent Deployments
To prevent old function code from lingering and ensure consistent deployments, some additional steps are recommended <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>:
1.  Navigate into the `functions` folder <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
2.  Install `rimraf` as a development dependency: `npm install -D rimraf` <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
3.  Open `package.json` in the `functions` folder and add two new scripts:
    ```json
    "scripts": {
        "clean": "rimraf lib",
        "pre-build": "npm run clean",
        "build": "typescript",
        // ... other existing scripts like "serve", "deploy"
    }
    ```
    *   `clean`: Deletes the `lib` directory (where compiled TypeScript code resides) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   `pre-build`: This script will always run before `build`, ensuring the `lib` folder is clean before new code is compiled <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
4.  To deploy, run `npm run build` (which will execute `clean` then TypeScript compilation) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
5.  Then, run `npm run deploy` to deploy the functions to your backend <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. The API link will be printed, and you can perform the same Postman tests as before <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

This structured approach using `firebase-backend` provides a clear path towards building large and maintainable [[deploying_and_hosting_applications_with_firebase | Firebase]] serverless products <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.