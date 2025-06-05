---
title: Setting up and managing Firebase projects
videoId: iWEgpdVSZyg
---

From: [[fireship]] <br/> 

Firebase offers a comprehensive platform for building and managing applications, providing various tools and services to streamline development and operations.

## Initial Project Setup and Configuration

When beginning a new project with Firebase, it's recommended to create two separate Firebase projects: one for development and one for production <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This approach provides a secure sandbox for testing and experimentation, ensuring that customer data in the production environment remains pristine <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Core Integrations and Settings

*   **Google Analytics**: Link Google Analytics to your production project to automatically set up analytics for iOS, Android, and web platforms <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **User Permissions**: For team collaboration, navigate to the "Settings" tab and then "Users and Permissions" to assign roles. Adhere to the principle of least privilege, giving team members access only to the resources they truly need <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Data Privacy**: Update your contact information in the "Data Privacy" tab to ensure compliance with regulations like GDPR <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Adding Apps**: When you add a new app to your project, Firebase provides an object with credentials that are safe in your front-end code, provided security rules are properly configured <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Cost Management and Monitoring

*   **Upgrade to Blaze Plan**: It's advisable to upgrade to the Blaze (pay-as-you-go) plan. This tier includes all free features from the Spark tier while enabling access to more advanced services <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Budget Alerts**: To manage costs, set up budget alerts for your project in the Google Cloud Platform (GCP) console <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Monitor Usage**: Regularly monitor your monthly usage from the reports panel to identify which services are incurring the most costs <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Firebase is generally inexpensive, and significant monthly active users are typically required to exceed the free tier <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Command Line Tools

*   **Install CLI Tools**: Install the Firebase command-line tools globally on your system, along with the Google Cloud SDK <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A Firebase project is essentially a layer built on top of a Google Cloud Platform project <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This grants access to `firebase` and `gcloud` commands locally <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **NPM Scripts**: For web applications, install `firebase-tools` into the development environment to write NPM scripts that leverage the Firebase CLI <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Project Flags**: When using separate development and production projects, use the `--project` flag in your CLI commands to specify the target project for deployments <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Hosting and Deployment Management

Firebase hosting supports various deployment scenarios:

*   **Mobile App Distribution**: For iOS or Android apps, use Firebase App Distribution to streamline app delivery to testers, bypassing platforms like TestFlight or the Google Play Store <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Custom Domains**: After deploying a web application, you can connect your own custom domain to your Firebase-hosted site <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Multi-Site Hosting**: A single Firebase project can host multiple domains, such as an admin site and a customer-facing site, using multi-site hosting <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This is configured by changing the `hosting` value to an array in your `firebase.json` file and setting up different targets <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Dynamic Content and SSR**: Firebase hosting can rewrite traffic to Cloud Functions or Cloud Run instances, enabling Server-Side Rendering (SSR) with frameworks like Angular Universal or Next.js <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Headers and Caching**: Specify headers for static files in your hosting configuration (e.g., CORS settings) and manage caching behavior to improve performance <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   [[Continuous Deployment using Firebase | Continuous Deployment]]: Integrate Firebase hosting with Google Cloud Build to automatically deploy new site versions upon every Git commit <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Database Management

Firebase offers two fully managed NoSQL databases: Cloud Firestore and Realtime Database <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

*   **Firestore vs. Realtime Database**:
    *   **Cloud Firestore** is generally preferred due to its more powerful query capabilities and lower cost per gigabyte stored <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   **Realtime Database** doesn't charge for writes, making it suitable for frequently updated data, such as from IoT sensors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Data Backup**: Regularly back up your data. Set up a dedicated Cloud Storage bucket for backups, which can be done with a single command <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Consider using a "cold line" storage class for backups to save money <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Security Rules**: Initially set your database to "locked mode" when created <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Incrementally allow operations as needed <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. [[Using Firebase databases and data modeling techniques | Security rules]] are crucial before deploying to production to prevent data compromise and destructive writes <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
    *   **Simulator**: Use the simulator to test how rules are evaluated with mock requests <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
    *   **Emulator**: For serious production apps, use the Firestore emulator to simulate the database locally and thoroughly test rules <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
    *   **Rule Granularity**: Define fine-grained rules for `get`, `list`, `create`, `update`, and `delete` operations, or combine them with `read` or `write` keywords if logic is shared <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
    *   **Request and Resource**: Rules are evaluated based on the `request` (user auth state, incoming data) and `resource` (existing data at the path) <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
    *   **Cross-Database Checks**: Use the `get` keyword to check other parts of the database when evaluating a rule, but be aware that each `get` incurs a read charge <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
    *   **Functions for Rules**: Extract complex rule logic into functions for cleaner, more readable rules <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

## Storage Management

A Firebase storage bucket is used for storing files like images, videos, and raw data <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

*   **Default and Additional Buckets**: You have a default bucket for user-generated content and can create additional buckets, such as a cold line bucket for Firestore backups <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   **Storing File Information**: When uploading a file, save its storage location (file path) and download URL to the Firestore database for future access, replacement, or deletion <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. If the path is forgotten, `storage().refFromURL()` can be used with either the full path or download URL <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **Listing Files**: List all files in a directory using `listAll()` method on a directory reference <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.
*   **Upload Progress**: Track upload progress by listening to the `state_changed` event <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Concurrent Uploads**: Firebase automatically handles concurrency when uploading multiple files simultaneously <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Custom Metadata**: Save custom metadata with uploaded files, such as device type or user ID <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **Image Resizing**: Use the [[Enhancing applications with Firebase extensions and integrations | Firebase image resizer extension]] to automatically resize image files for different resolutions <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

## Backend and Admin Operations

Firebase Admin SDK allows for server-side interactions with your Firebase project.

*   **Command Line Utility**: Create custom command-line utilities using Firebase Admin SDK:
    1.  Download the service account key for your project from project settings <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    2.  Install `firebase-admin` as a development dependency in a Node.js project <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
    3.  Initialize the app, ensuring the service account key is kept private (e.g., via `GOOGLE_APPLICATION_CREDENTIALS` environment variable) and added to `.gitignore` <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Database Seeding**: Use an admin script with libraries like Faker.js to seed your database with dummy data for testing purposes <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **REST APIs**: Explore Firebase REST API documentation for advanced techniques, such as scheduling daily database backups via a cron job <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. The Google API NPM package facilitates interaction with various Google APIs, including Firebase <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Cloud Functions Management

[[Setting up Firebase Cloud Functions | Firebase Cloud Functions]] extend the capabilities of your application with backend logic.

*   **Setup**: Initialize cloud functions in your project by running `firebase init functions` <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Using TypeScript is recommended for setup and error prevention <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
*   **Performance Optimization**:
    *   Minimize dependencies to reduce cold start times <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
    *   Utilize global variables for values shared across multiple function invocations <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
    *   Design functions to be idempotent, ensuring consistent results even with multiple invocations <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
    *   Increase memory and timeout for more demanding functions using `runWith` <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   **Avoiding Infinite Loops**: Be cautious when updating the same document that triggered a Firestore function. Check if the `after` document is equal to the `before` document to prevent infinite loops <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
*   **Asynchronous Operations**: Background functions must return a promise, so use `async/await` for cleaner asynchronous code <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   **Inter-Function Communication**:
    *   For internal service communication, use Pub/Sub functions instead of HTTP functions to enhance security and simplify validation <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
    *   **Callable Functions**: Simplify authentication for endpoints by using callable functions, which include the user's `auth` context automatically <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
*   **Batch Operations**: For tasks like deleting large Firestore collections, implement recursive batch deletion in a callable function to avoid memory issues <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
*   **Code Organization**: Break down backend logic into small JavaScript functions for reusability and easier testing across multiple deployed functions <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   **Third-Party APIs**: Cloud Functions serve as a gateway to interact with other third-party APIs using Node.js libraries <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.
*   **Deployment**: Deploy all functions with a single command or append the function's name to deploy individually on larger projects <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
*   **Debugging**:
    *   Run the Cloud Functions shell locally to invoke functions with mock data and test their behavior <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
    *   Utilize the Firebase unit testing library <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
    *   Inspect Firebase logs or use Stackdriver for custom dashboards and alerts to identify production issues <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.

## User Engagement and Machine Learning

*   **Custom Analytics Events**: Track custom events and user properties in Firebase Analytics to gain deeper insights into user behavior, especially actions leading to conversion <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
*   **Audiences**: Create custom audiences based on user types to target marketing messages, A/B tests, and even customize UI elements based on analytics data <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Cloud Messaging**: Send targeted push notifications to specific user segments using Firebase Cloud Messaging <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.
*   **Machine Learning Integration**:
    *   Use Firebase Predictions to anticipate user behavior, like product purchases <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
    *   Implement AI-driven features with ML Kit for tasks like object detection and smart reply <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
    *   Build custom image classification models with AutoML <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.
    *   Export analytics and Firestore data to BigQuery for training custom TensorFlow models <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.