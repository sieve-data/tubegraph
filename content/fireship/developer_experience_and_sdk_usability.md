---
title: Developer Experience and SDK Usability
videoId: ucmbO2lWC2A
---

From: [[fireship]] <br/> 

Developing applications today often involves leveraging cloud platforms to manage and scale infrastructure efficiently <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Firebase and AWS Amplify are two such platforms designed to simplify [[Front End and Back End Development | back-end]] development for [[Design techniques in app development | app developers]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This article compares the developer experience and SDK usability of these platforms, highlighting their ease of use, flexibility, and the complexities involved in building common app features like authentication and real-time data handling.

## Platform Overview and Framework Support
Both Firebase (Google's cloud infrastructure) and AWS Amplify (Amazon's cloud infrastructure) simplify back-end processes, but involve a degree of vendor lock-in <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Choosing the right tool depends on the specific job and the [[Front End and Back End Development | front end framework]] being used <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

*   **Firebase**: Offers official support for [[Performance and developer experience in React Native and Flutter | Flutter]], iOS, Android, and the web <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. [[Implementing the JavaScript SDK in Angular | Angular]] and Vue also have official libraries under their mono repos <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Community-maintained projects exist for React and [[Performance and developer experience in React Native and Flutter | React Native]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **AWS Amplify**: Provides official support for iOS, Android, web, [[Performance and developer experience in React Native and Flutter | React Native]], React web, [[Implementing the JavaScript SDK in Angular | Angular]], and Vue <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. As of the video's creation, it doesn't support Water or bundling with Rollup, though open issues suggest future support <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Core Features and Developer Experience
Both platforms offer common features like user authentication, analytics, real-time data management, push notifications, file storage, serverless functions, and web hosting <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### AWS Amplify Unique Features
*   **Dedicated Environments**: Streamlined setup for development and production environments, unlike Firebase which requires setting up multiple projects <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Continuous Deployment**: Simplifies continuous deployment by connecting the hosting account to a GitHub repo for automatic code deployment upon commit <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Firebase can do this with Google Cloud Build, but with more configuration steps <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **GraphQL Integration**: Deep integration with GraphQL <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Sumerian Integration**: Useful for augmented or virtual reality apps <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Firebase Unique Features
*   **Dedicated Database**: Offers Firestore, a dedicated NoSQL database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Callable Functions**: Serverless functions that can be called with authentication context from the front-end, making it easy to determine if a user is logged in without setting up an API gateway or writing backend authorization logic from scratch <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Quality Control Tools**: Includes Crashlytics, Performance Monitoring, and Test Lab <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Analytics-driven Features**: Features like Predictions and Remote Config built on top of analytics <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **ML Kit**: Simplifies implementing machine learning features both in the cloud and on-device <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## Pricing Models
Both platforms feature generous free tiers, meaning developers typically only pay once they have a significant number of active users <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **AWS Amplify**: Generally slightly cheaper than Google Cloud Platform (GCP) for most services; for example, storage is 2.3 cents/gigabyte on AWS versus 2.6 cents on Firebase <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Firebase**: Offers some always-free services, such as user authentication and push notifications <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Database Costs**:
    *   **Firestore (Firebase)**: Billed for reads and writes; real-time syncing is automatic <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. 1 million read operations cost 60 cents, and 1 million write operations cost $1.80 <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   **AppSync/DynamoDB (AWS Amplify)**: AppSync costs $4 per 1 million query or write operations, with additional costs for the DynamoDB database itself <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Billing is calculated in chunks of 5 kilobytes <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Firestore appears significantly less expensive for scaling apps <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Serverless Functions**: AWS has an edge at 20 cents per million invocations compared to Firebase's 40 cents <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## SDK Usability: A Practical Comparison

To illustrate the [[Problemsolving skills in software development | developer experience]], a mini [[JavaScript and Frontend Development | JavaScript app]] with user authentication and a real-time to-do list was built on both platforms <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a> <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Authentication Setup and Code
#### AWS Amplify
1.  **CLI Setup**: Requires an AWS developer account and the Amplify CLI <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. `amplify init` sets up the project after answering basic questions <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. An `amplify` directory is created, referencing AWS resources <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
2.  **Adding Authentication**: `amplify add auth` allows choosing options like email/password authentication <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. `amplify push` provisions resources in the cloud, using AWS Cognito for user authentication <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **Flexibility**: Cognito offers extensive flexibility and customization, including multi-factor authentication, custom user attributes, and additional serverless code triggers beyond just user creation/deletion (unlike Firebase) <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
4.  **Code Example**:
    ```javascript
    import Amplify from 'aws-amplify';
    Amplify.configure(awsconfig); // Automatically generated config
    
    // Check if user is logged in
    Auth.currentAuthenticatedUser();
    
    // Log in with email and password
    Auth.signIn(username, password);
    ```
    The authentication code is very similar to Firebase, with minimal lines needed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

#### Firebase
1.  **Dashboard Setup**: Simpler and generally faster to set up via the Firebase dashboard <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. For example, passwordless authentication can be enabled with a single click <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  **Less Flexible**: Firebase is less flexible by comparison; tasks like passwordless authentication in AWS would require setting up multiple Lambda functions <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
3.  **Code Example**:
    ```javascript
    import firebase from 'firebase/app';
    import 'firebase/auth';
    
    firebase.initializeApp(firebaseConfig); // Credentials from console
    
    // Check if user is logged in
    firebase.auth().currentUser;
    
    // Sign in with email and password
    firebase.auth().signInWithEmailAndPassword(email, password);
    ```
    The code is almost identical to AWS Amplify, demonstrating well-organized [[JavaScript and Frontend Development | JavaScript]] libraries that simplify development <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Real-time Data Handling
#### Firebase Firestore
*   **Simplicity**: Firestore provides a simple, boilerplate-free way to manage real-time data <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Querying Data**: Using `onSnapshot` on a collection reference automatically listens for real-time changes, providing a snapshot of the data that can be mapped to JavaScript objects <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Mutating Data**: Updating a document involves referencing its location and calling `.update()` with the new data <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Drawback**: Developers are limited to a single NoSQL database, which can present challenges for data modeling and migration <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

#### AWS Amplify with GraphQL and AppSync
*   **Setup Complexity**: Requires running `amplify add api`, choosing GraphQL, and selecting API for authentication <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Boilerplate Generation**: The Amplify CLI generates much of the GraphQL boilerplate code, including a default schema <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. `amplify push` then generates the GraphQL API and provides an endpoint and API key <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. An AppSync console shows the uploaded schema, and DynamoDB is automatically set up as a NoSQL backend <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Querying Data**: Auto-generated GraphQL folders contain boilerplate for mutations, queries, and subscriptions <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. The Apollo client is typically used. For example, `client.graphql(listTodos)` fetches data, returning a promise <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Real-time Updates**: Requires setting up subscriptions. `client.subscribe` points to an `onUpdateTodo` subscription, allowing access to data whenever it changes <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Complexity**: While powerful, GraphQL can be overkill for simpler applications, introducing a lot of complexity in both automatically generated code and implementation details <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **Flexibility**: The trade-off for this complexity is much greater flexibility in making the code behave exactly as desired <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

### Bundle Size Impact
Both Amplify and Firebase SDKs add significant JavaScript to the final application bundle size <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Firebase**: With user authentication and Firestore, the bundle can be around 500 kilobytes <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **AWS Amplify**: With AppSync and GraphQL, the bundle can be close to a full megabyte <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## Conclusion
Both Firebase and AWS Amplify significantly improve the [[Problemsolving skills in software development | development]] speed and flexibility of applications, saving time and money compared to building a [[Front End and Back End Development | back-end]] from scratch <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

*   **Firebase**: Generally offers an easier and more straightforward developer experience with fewer decisions during configuration <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This is particularly noticeable when comparing Firestore to GraphQL and DynamoDB <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **AWS Amplify**: Provides superior flexibility, with more customization options to tailor the experience to specific project needs <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.