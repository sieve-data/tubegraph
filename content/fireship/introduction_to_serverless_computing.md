---
title: Introduction to serverless computing
videoId: W_VV2Fx32_Y
---

From: [[fireship]] <br/> 

## What is Serverless Computing?

[[overview_of_cloud_computing_services | Serverless computing]] is a term used to describe servers in the cloud that require zero configuration or maintenance from the developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's considered a misnomer because servers still exist, but their management is abstracted away from the user <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Core Concept: Utility Model
The concept of serverless computing is similar to how a city water supply works <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Instead of digging a well, testing water quality, and plumbing it yourself, you tap into the city supply and pay a monthly fee based on usage <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. In serverless, instead of water, you pay for the amount of CPU and memory it takes to run your code <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Key Features and [[benefits_of_serverless_architecture | Benefits]]

*   **Zero Infrastructure Management** Developers only concern themselves with writing code <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You don't need to pick an operating system, configure networking, apply patches, or provision capacity <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The cloud provider handles all backend operations <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Pay-per-use Billing** Cloud providers like [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | AWS Lambda]], [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | Google Cloud Functions]], and [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | Azure Functions]] allow you to run backend code across their global data centers and bill you down to the millisecond of usage <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This contributes to [[cloud_computing_scalability_and_cost_management | cost management]] as you only pay for what you use.
*   **Architectural Flexibility** From an architectural standpoint, serverless allows for developing and testing each business requirement independently of a larger monolithic system <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Event-Driven Execution** Serverless functions can be executed based on different events that happen in the cloud, which can simplify backend code <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Examples include:
    *   A new database record (e.g., a user order) triggering a function to send an email confirmation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
    *   An IoT event (e.g., from a home security system) invoking a function to send a push notification <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Types of Serverless Functions

When [[structuring_and_deploying_serverless_applications | structuring and deploying serverless applications]] with platforms like [[building_serverless_backends_with_firebase_and_flutter | Firebase Cloud Functions]], functions can generally be categorized into two types:

*   **Restful Functions** These are traditional functions that run when a client makes an HTTP request to the URI assigned to the function <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Reactive Functions** These functions run in reaction to data or state being updated on the backend <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Common examples include file uploads to cloud storage or updates to database entries <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## [[structuring_and_deploying_serverless_applications | Structuring and Deploying Serverless Applications]] (Example with [[building_serverless_backends_with_firebase_and_flutter | Firebase Cloud Functions]])

One straightforward way to begin with serverless is through [[building_serverless_backends_with_firebase_and_flutter | Firebase Cloud Functions]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The command-line tool provides a project structure similar to other [[introduction_to_nodejs | Node.js]] backends <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Code Structure Principles
An enforced code structure helps with organization and maintenance as the backend grows <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

1.  **Dedicated Files for Functions** Each function should be in its own dedicated file to prevent the main `index` file from becoming too large <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The file name can optionally match the endpoint or function name for easier management <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
2.  **Categorization by Type** Functions are placed in folders titled `restful` or `reactive` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  **Resource Grouping** The backend is split into different resource groups (e.g., `orders`, `payments`, `users`) to ensure a structured backend in production <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Each resource group typically contains both `reactive` and `restful` folders <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Implementation Setup

1.  **Initialize Firebase Project**: Navigate into your backend folder and run `firebase init` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Select `firestore`, `functions`, and `emulators` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Choose to create a new project and configure Firestore <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
2.  **Language and Dependencies**: For functions setup, TypeScript is often used <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Install dependencies and enable emulators for functions and Firestore <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  **Core Package Installation**: Install `firebase-backend` within the functions folder (`npm install firebase-backend`) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
4.  **`index.ts` Configuration**: The main `index.ts` file needs only import `FunctionParser` from `firebase-backend` and export a new `FunctionParser` instance <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This minimal setup handles the parsing of all other functions regardless of backend size <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Example: Creating a Restful Endpoint
*   Create a folder for the resource group (e.g., `users`), then a `restful` subfolder <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   Inside `restful`, create a file named `addPaymentMethod.endpoint.ts` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The `.endpoint.ts` suffix is crucial for it to be loaded as an HTTP endpoint <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Export a default new `Endpoint` instance, specifying its name, request type (e.g., `RequestType.Post`), and the Express endpoint handler function that contains the logic <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Example: Creating a Reactive Function
*   Create a folder for the resource group (e.g., `users`), then a `reactive` subfolder <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   Inside `reactive`, create a file named `onUserCreated.function.ts` <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. The `.function.ts` suffix is important for it to be recognized as a reactive cloud function <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   Export a function (e.g., `onUserCreated`) that uses a Firebase `onCall` or `onCreate` (for Firestore documents) callback <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Specify the document pattern to listen to (e.g., `users/{userId}`) <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Testing and Deployment
*   **Local Testing**:
    *   For RESTful functions, run `npm run serve` to build TypeScript code and serve functions locally through the emulator <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   For reactive functions and full emulator setup, run `npm run build` then `firebase emulators:start` <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Deployment**: After building (`npm run build`), deploy functions to the backend using `npm run deploy` <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

### Improving Code Setup for Consistent Deployments
To prevent old function code from lingering and ensure consistent deployments:
1.  **Install `rimraf`**: `npm install -D rimraf` in the functions folder <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
2.  **Add Scripts to `package.json`**:
    *   Add a `clean` script: `"clean": "rimraf lib"` <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
    *   Add a `prebuild` script: `"prebuild": "npm run clean"` <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. This ensures `clean` runs automatically before `build`, deleting old code before new code is compiled <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.