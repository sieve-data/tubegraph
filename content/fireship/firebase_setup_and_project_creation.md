---
title: Firebase setup and project creation
videoId: 9kRgVxULbag
---

From: [[fireship]] <br/> 

Firebase is presented as an excellent platform for building applications, primarily used for its developer experience, cost minimization, and ability to maximize development time <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It abstracts away the backend, making development significantly easier <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The platform is well-documented, easy to use, and responsive to developer feedback <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. It offers a free tier for small, experimental projects and scales linearly with user growth <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The goal is to facilitate creating the most value in the least amount of time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Prerequisites

To follow along with Firebase development, you will need:
*   An editor like VS Code <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   Node.js installed on your local system <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   No prior coding experience is necessary to understand the basics <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## [[setting_up_and_managing_firebase_projects | Setting up and Managing Firebase Projects]]

A Firebase project serves as a container for resources on Google Cloud Platform, including your database, file storage, and web hosting <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Project Creation
To create a new project, navigate to the Firebase console and initiate a new project <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Management and Platform Support
*   All app resources can be managed from the Firebase admin console <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   A single project can span multiple platforms, as Firebase provides Software Development Kits (SDKs) for web, iOS, Android, Unity, and others <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Your project is identified by specific credentials, which integrate seamlessly with other APIs on Google Cloud Platform, allowing for easy implementation of services like Cloud Vision or Google Maps <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Firebase Command Line Tools

The Firebase command-line tools (CLI) allow for quick project setup and deployment directly from your terminal.

### Installation
Install the Firebase CLI globally by running the following npm command:
```bash
npm install firebase-tools -g
```
<a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>

### Project Initialization and Deployment
1.  **Initialize Hosting**: From an empty folder, open your terminal and run `firebase init hosting` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This command creates several essential files:
    *   `firebase.json`: Defines hosting rules <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   `.firebaserc`: Identifies your project <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   `public/index.html`: The main application file, which imports the Firebase web SDK in its head <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. You can selectively import Firebase modules to improve page load performance <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Script tags typically include `defer` to ensure they execute after the page loads <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
2.  **Serve Locally**: To test your application, run `firebase serve` <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This spins up a local web server, usually on port 5000, allowing you to view and test your app in a browser <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **[[deploying_and_hosting_applications_with_firebase | Deploy the Application]]**: To deploy your app to a live, hosted URL accessible on the internet, run `firebase deploy` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. This deployment includes:
    *   An SSL certificate for immediate HTTPS support <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Utilization of Google's Content Delivery Network (CDN) to cache and serve static resources efficiently <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Key Firebase Features

Firebase offers a comprehensive suite of features for application development:

### Authentication
Firebase simplifies user authentication, allowing implementation in just a few lines of code <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. It supports various OAuth providers like Google, email/password, anonymous, Twitter, Facebook, and GitHub <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Authentication uses JSON Web Tokens (JWTs), which are easier to work with for JavaScript applications than traditional cookies <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. The Firebase console allows management of user accounts, email templates, text message verification, and basic analytics <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Database
As of October 2017, Firebase offers two NoSQL database options <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>:
*   **Realtime Database**: Ideal for simple, frequently read data sets <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Cloud Firestore**: Generally preferred for larger, more complex, relational data sets <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. It's structured as collections of documents, similar to MongoDB <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
User authentication is directly tied to the database, allowing for expressive security rules to define backend logic <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Firestore also supports automatic and custom indexing for efficient querying <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. A major benefit of Firebase databases is the ability to listen to data changes in real-time, instantly notifying all users of updates <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Storage
Firebase Storage provides a cloud storage bucket integrated with your project for user-generated content like images and videos <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Access rules can be configured to allow specific users or anyone to upload files <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Files can be uploaded and their download URLs retrieved asynchronously <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### [[setting_up_firebase_cloud_functions | Cloud Functions]]
[[setting_up_firebase_cloud_functions | Firebase Cloud Functions]] allow you to run Node.js backend code on demand as microservices <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. Anything that can be done in Node.js, including installing NPM packages, can be done within a function <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. Functions can be triggered by various events, such as database triggers (e.g., creating a new document in Firestore) <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. The Firebase Admin SDK can be used within functions, bypassing security rules <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. Functions are deployed using `firebase deploy functions` <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

### Mobile App Specific Features
For native mobile applications, Firebase offers additional features for testing and stability:
*   **Robo Testing**: Upload your app build, and Firebase will run a suite of tests to identify common issues that cause crashes, providing screenshot results for review <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Analytics**: Includes tools like StreamView, which provides a real-time global geographic representation of your user base <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   **Push Notifications**: Easily send notifications to user segments, specific topics, or individual devices, with support for A/B testing and conversion rate tracking <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.