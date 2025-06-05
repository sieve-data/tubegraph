---
title: Core Features and Capabilities
videoId: ucmbO2lWC2A
---

From: [[fireship]] <br/> 

Firebase and AWS Amplify are platforms designed to simplify the management and scaling of cloud infrastructure for app developers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. They allow developers to dramatically simplify their backend development <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. While Amplify runs on Amazon's cloud infrastructure, Firebase runs on Google's, leading to some degree of vendor lock-in <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The choice between them often comes down to using the right tool for the job <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Frontend Framework Support

Both platforms offer official support for iOS, Android, and the web <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

*   **AWS Amplify**: Provides official support for React Native, React Web, Angular, and Vue <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. At the time of the video, it did not support Flutter or bundling with Rollup, though open issues exist for these <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Firebase**: Offers official support for Flutter, Angular, and Vue, with official libraries under their mono repos <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. There are also good community-maintained projects for React and React Native <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Shared Core Features

Both Firebase and AWS Amplify provide several key capabilities:

*   User authentication <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Analytics <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Real-time data management <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Push notifications <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   File storage <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Serverless functions <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Web hosting <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

## Unique Features

### AWS Amplify Specific Features

*   **Dedicated Environments**: Allows setting up dedicated environments for development and production in a streamlined manner, which is more integrated than Firebase's approach of setting up multiple projects <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Continuous Deployment**: Simplifies continuous deployment by taking an approach similar to Netlify, where a hosting account connects to a GitHub repo for automatic code deployment <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. While possible with Google Cloud Build and Firebase, it requires more configuration steps <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **GraphQL Integration**: Features deep integration with GraphQL <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Amazon Sumerian Integration**: Integrates with Amazon Sumerian, useful for building Augmented or Virtual Reality (AR/VR) applications <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Firebase Specific Features

*   **Dedicated Database**: Offers a dedicated database service (Firestore), which provides a simpler real-time data experience compared to Amplify's GraphQL setup <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Callable Functions**: Provides powerful callable functions, which are serverless functions that can be invoked from the frontend with authentication context, simplifying backend authorization logic compared to setting up an API Gateway <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Quality Control Tools**: Includes tools for quality control like Crashlytics, Performance Monitoring, and Test Lab <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Analytics-driven Features**: Builds upon analytics with features such as Predictions and Remote Config <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **ML Kit**: Offers ML Kit for easily implementing machine learning features both in the cloud and on device <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## User Authentication Capabilities

Both platforms offer well-organized JavaScript libraries that allow developers to achieve results with very few lines of code <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

### AWS Amplify Authentication

[[AWS Computer Services and Tools | User authentication]] in Amplify is handled by [[AWS Computer Services and Tools | AWS Cognito]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

*   **Flexibility and Customization**: Cognito offers significant advantages in flexibility and customization over Firebase <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Multi-Factor Auth**: Supports features like multi-factor authentication (MFA) via text message or email <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Custom Attributes**: Allows setting up custom attributes on user authentication records <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Serverless Triggers**: Provides additional triggers for serverless code, extending beyond user creation or deletion events found in Firebase <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Implementation**: Initial setup involves `amplify init` and `amplify add auth` via the CLI, followed by `amplify push` to provision resources <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Code Example**: Checking if a user is logged in uses `Auth.currentAuthenticatedUser()`, and signing in uses `Auth.signIn(username, password)` <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

### Firebase Authentication

Firebase authentication is generally simpler and faster to set up but offers less flexibility compared to Amplify <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

*   **Simplicity**: For example, setting up password-less authentication can be done by clicking a button, whereas it would require several Lambda functions on [[AWS Computer Services and Tools | AWS]] <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Code Example**: The code for user authentication is almost identical to Amplify's, using `auth.currentUser` and `signInWithEmailAndPassword` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

## Real-time Data Capabilities

### Firebase Real-time Data with Firestore

Firebase provides a dedicated database service, Firestore, which excels at real-time data syncing <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

*   **Simplicity**: It offers simplicity without boilerplate code, making it easy to work with, especially for complex real-time features, as the difficult real-time aspects are handled automatically <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Real-time Syncing**: To query a collection and listen for real-time changes, `onSnapshot` is called, which provides a callback with a snapshot of the document data <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Data Mutation**: Updating a document involves making a reference to its location and calling `update()` with the new data <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Drawback**: The main drawback is being tied to a single NoSQL database, which can present [[AWS Database Offerings | challenges for data modeling]] and migration <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### AWS Amplify Real-time Data with GraphQL and AppSync

Amplify integrates with GraphQL via [[AWS Computer Services and Tools | AWS AppSync]], which connects to a [[AWS Database Offerings | DynamoDB]] instance (a NoSQL database similar to MongoDB or Firestore) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

*   **Provisioning**: Resources are provisioned using `amplify add api` with GraphQL and API authentication <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Boilerplate Generation**: The Amplify CLI generates much of the boilerplate code needed for GraphQL, including queries, mutations, and subscriptions, and deploys a GraphQL API endpoint with an API key <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Data Fetching**: Data can be queried using `GraphQL.listToDos` which returns a promise resolving to an array of items <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Real-time Updates**: Real-time changes are handled via GraphQL subscriptions. To update data, `client.mutate` is used, and to listen for changes, `client.subscribe` points to an `onUpdate` subscription <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Complexity vs. Flexibility**: While GraphQL is powerful, it can introduce significant complexity and boilerplate code for relatively simple real-time data needs compared to Firestore. However, it offers much more flexibility to customize code behavior <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Conclusion: Ease of Use vs. Flexibility

Both platforms are valuable, saving time and money in product development <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

*   **Ease of Use**: Firebase is generally easier to use, with fewer decisions needed for configuration. This is particularly noticeable when comparing Firestore to Amplify's GraphQL and [[AWS Database Offerings | DynamoDB]] setup <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **Flexibility**: [[AWS Computer Services and Tools | AWS]] Amplify is superior in flexibility, offering more customization options to tailor the experience to specific needs <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.