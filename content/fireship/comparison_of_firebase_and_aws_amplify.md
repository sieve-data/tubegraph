---
title: Comparison of Firebase and AWS Amplify
videoId: ucmbO2lWC2A
---

From: [[fireship]] <br/> 

[[introduction_to_firebase_and_benefits | Firebase]] and AWS Amplify are platforms designed to simplify the management and scaling of cloud infrastructure for app developers <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While both aim to dramatically simplify backend development, they operate on different cloud infrastructures: AWS Amplify runs on Amazon's cloud, and [[introduction_to_firebase_and_benefits | Firebase]] runs on Google's cloud <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This means choosing one introduces a degree of vendor lock-in <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The choice between them depends on finding the right tool for specific project requirements <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Supported Front-end Frameworks

The first consideration for developers is whether their preferred front-end framework is supported <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

*   **AWS Amplify** offers official support for iOS, Android, web, React Native, React Web, Angular, and View <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. As of the video's creation, it did not support Water or bundling with Roll-up, though open issues suggest future support <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **[[introduction_to_firebase_and_benefits | Firebase]]** provides official support for [[building_serverless_backends_with_firebase_and_flutter | Flutter]], Angular, and View, with official libraries available in their mono repos <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Community-maintained projects exist for React and React Native <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Core Features

Both platforms share many core features essential for modern app development <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Shared Features

Both AWS Amplify and [[introduction_to_firebase_and_benefits | Firebase]] offer:
*   User authentication <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Analytics <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Real-time data management <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Push notifications <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   File storage <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Serverless functions <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Web hosting <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

### Unique Features of AWS Amplify

*   **Dedicated Environments:** Streamlined setup for development and production environments <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While [[introduction_to_firebase_and_benefits | Firebase]] can achieve this with multiple projects, Amplify's approach is more integrated <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Continuous Deployment (CD):** Similar to Netlify, it allows connecting a hosting account to a GitHub repository for automatic code deployments upon commit <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Google Cloud Build offers similar functionality for [[deploying_and_hosting_applications_with_firebase | Firebase]], but with more configuration steps <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **GraphQL Integration:** Features robust integration with GraphQL <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Sumerian Integration:** Useful for building Augmented Reality (AR) or Virtual Reality (VR) applications <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Unique Features of [[introduction_to_firebase_and_benefits | Firebase]]

*   **Dedicated Database:** Offers [[comparison_of_firebase_and_its_alternatives | Firestore]] and Realtime Database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Callable Functions:** These are serverless functions that can be invoked directly from the front-end with authentication context, simplifying backend authorization logic compared to setting up an API gateway <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Quality Control Tools:** Includes Crashlytics, Performance Monitoring, and Test Lab <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Analytics-driven Features:** Provides features built on top of analytics, such as Predictions and Remote Config <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **ML Kit:** Facilitates the implementation of machine learning features, both in the cloud and on-device <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## [[features_and_pricing_of_aws_amplify | Pricing]]

Both platforms offer generous free tiers, meaning users typically don't pay until they have a significant number of active users <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Generally, AWS is slightly cheaper than GCP for most services <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. For example, a gigabyte of storage is 2.3 cents on AWS versus 2.6 cents on [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

However, [[introduction_to_firebase_and_benefits | Firebase]] has some services that are always free, like user authentication and push notifications <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. On AWS, user authentication costs about half a penny per monthly active user above 50,000 <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Database Pricing

*   **[[introduction_to_firebase_and_benefits | Firestore]]:** Billed for reads and writes to the database, with real-time syncing happening automatically without additional cost <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. For 1 million read operations, it costs 60 cents; for 1 million write operations, it's $1.80 <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **AWS AppSync (with DynamoDB):** AppSync costs $4 per 1 million query or write operations <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Additional costs may apply for the DynamoDB backend itself, and billing is calculated in chunks of 5 kilobytes <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. [[comparison_of_firebase_and_its_alternatives | Firestore]] appears to be significantly less expensive for database operations as an application scales <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Serverless Functions Pricing

AWS has an edge in serverless function pricing, costing 20 cents per million function invocations, compared to 40 cents on [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Developer Experience

The primary reason to use these platforms is to increase development speed and flexibility <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Setting Up a Project

*   **AWS Amplify:** Requires an AWS developer account and the Amplify CLI. Initialization involves running `amplify init` and answering basic questions, which creates an `amplify` directory referencing AWS resources <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **[[introduction_to_firebase_and_benefits | Firebase]]:** Setting up a project typically involves initializing the SDK with credentials from the [[introduction_to_firebase_and_benefits | Firebase]] console <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Authentication

*   **AWS Amplify:** To add authentication, run `amplify add auth` and select options like email/password authentication <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Running `amplify push` provisions these resources in the cloud, handled by AWS Cognito <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Cognito offers high flexibility and customization, including multi-factor authentication, custom user attributes, and more serverless code triggers than [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. The code for checking current user and signing in is concise <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **[[introduction_to_firebase_and_benefits | Firebase]]:** The dashboard is more simplified, making setup faster and easier, though less flexible <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For example, passwordless authentication can be enabled with a single click, whereas in AWS it would require setting up several Lambda functions <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The authentication code is nearly identical in simplicity to Amplify <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Real-time Data (Databases)

*   **[[introduction_to_firebase_and_benefits | Firebase]] ([[comparison_of_firebase_and_its_alternatives | Firestore]]):**
    *   **Simplicity:** To query a collection and listen for real-time changes, `onSnapshot` is used, providing a callback function that updates whenever the collection changes <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Updating a document is done with a single line of code using an `update` call on a document reference <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   **Ease of Use:** [[comparison_of_firebase_and_its_alternatives | Firestore]] handles complex real-time syncing automatically, requiring minimal boilerplate code <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   **Drawbacks:** Users are limited to a NoSQL database, which can present challenges for data modeling and migration <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **AWS Amplify (GraphQL with AppSync and DynamoDB):**
    *   **Provisioning:** `amplify add api` is used to provision GraphQL resources, automatically generating a schema and boilerplate code <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This sets up a GraphQL API and an instance of DynamoDB (a NoSQL database similar to MongoDB or [[comparison_of_firebase_and_its_alternatives | Firestore]]) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   **Complexity:** While the CLI generates much of the GraphQL boilerplate, implementing real-time features like subscriptions requires more explicit code compared to [[comparison_of_firebase_and_its_alternatives | Firestore]] <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. For example, using Apollo client to fetch data and then setting up explicit `client.subscribe` calls for real-time updates <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
    *   **Benefits:** Offers greater flexibility in how the data behaves and is accessed <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. GraphQL provides powerful querying capabilities <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Conclusion

Both AWS Amplify and [[introduction_to_firebase_and_benefits | Firebase]] are valuable platforms that significantly reduce development time and costs for backend services <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

*   **[[features_and_pricing_of_aws_amplify | Pricing]]:** Largely equivalent, with minor differences depending on usage patterns. AWS tends to be slightly cheaper for most services, but [[introduction_to_firebase_and_benefits | Firebase]] offers some perpetually free services and potentially lower database costs at scale <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Ease of Use:** [[introduction_to_firebase_and_benefits | Firebase]] is generally easier to use, with fewer configuration decisions, especially when comparing [[comparison_of_firebase_and_its_alternatives | Firestore]] to GraphQL/DynamoDB <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **Flexibility:** AWS Amplify offers superior flexibility with more customization options and "knobs to turn" to tailor the experience to specific needs <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.