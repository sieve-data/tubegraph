---
title: Comparison of Firebase and its alternatives
videoId: SXmYUalHyYk
---

From: [[fireship]] <br/> 

The development landscape for real-time applications has seen significant evolution, moving from self-built backend infrastructure to managed Backend-as-a-Service (BaaS) solutions. While [[introduction_to_firebase_and_benefits | Firebase]] has long been a dominant player, several alternatives have emerged, each offering unique features, pricing models, and developer experiences <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This article compares [[introduction_to_firebase_and_benefits | Firebase]] with five of its leading alternatives: AWS Amplify, Supabase, Nhost, Appwrite, and MongoDB Realm.

A BaaS is a complex product that aggregates disparate cloud infrastructure pieces like databases and servers, provides SDKs for multiple platforms, and ensures security and documentation for developers <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[introduction_to_firebase_and_benefits | Firebase]]

[[introduction_to_firebase_and_benefits | Firebase]] is a Google-backed BaaS that offers a NoSQL database and a suite of features for app development <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It simplifies backend development, allowing for real-time apps with minimal code <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Key Features and Popularity
[[introduction_to_firebase_and_benefits | Firebase]]'s core features for app developers include:
*   User authentication <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
*   Database (Firestore) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   [[cloud_functions_and_integration_with_firebase | Server-side functions]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>

Other features include analytics, Crashlytics, and performance monitoring <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
[[introduction_to_firebase_and_benefits | Firebase]]'s infrastructure is hosted by Google Cloud Platform, providing SDKs for front-end applications like JavaScript, iOS, Android, [[flutter_app_integration_with_firebase | Flutter]], and Unity <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

Its web SDK sees over a million downloads per week, and it's even more popular on mobile, used by many game studios <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Pricing
[[introduction_to_firebase_and_benefits | Firebase]] offers a generous free tier <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Authentication is generally free, except for phone and multi-factor authentication <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. The Firestore database and [[cloud_functions_and_integration_with_firebase | Cloud functions]] scale up based on usage, which can become expensive at scale depending on the application <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Drawbacks and Developer Experience
A significant drawback of [[introduction_to_firebase_and_benefits | Firebase]] is vendor lock-in, as Firestore is a proprietary database. Migrating data to a different database can be a major undertaking <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Missing features include full-text search and the ability to return a table count <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

Despite this, [[introduction_to_firebase_and_benefits | Firebase]] offers a simple developer experience, enabling features like Google authentication and basic OAuth with a single line of code <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. It provides real-time updates where UI magically updates when server data changes <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## AWS Amplify

[[comparison_of_firebase_and_aws_amplify | AWS Amplify]] is Amazon's answer to [[introduction_to_firebase_and_benefits | Firebase]], offering a comprehensive list of features <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Key Features and Popularity
[[comparison_of_firebase_and_aws_amplify | AWS Amplify]] includes analytics, predictions, and notifications <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Its primary database is DynamoDB, though it automatically creates a GraphQL API for data, and it's possible to connect a relational database <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Data can be made searchable with Elasticsearch, a feature missing in [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. User authentication is handled by AWS Cognito, which allows creating user groups and controlling their access <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

[[comparison_of_firebase_and_aws_amplify | AWS Amplify]] has SDKs for all major web and mobile platforms and challenges [[introduction_to_firebase_and_benefits | Firebase]]'s popularity with about 400,000 weekly downloads <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Pricing and Drawbacks
Pricing is pay-as-you-go, requiring careful usage calculation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Vendor lock-in is a concern if proprietary AWS products are used <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Developer Experience
[[comparison_of_firebase_and_aws_amplify | AWS Amplify]] relies heavily on code generation for backend APIs, which dumps code into the project that needs syncing with AWS <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This creates a good developer experience for data fetching due to a GraphQL schema providing intellisense and simple one-liners for queries, similar to the [[introduction_to_firebase_and_benefits | Firebase]] SDK <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Supabase

Supabase, founded around Y Combinator season 20, provides core features like authentication, file storage, and serverless functions <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Key Features and Popularity
Supabase's distinguishing feature is its use of PostgreSQL, an open-source relational database <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This offers a more flexible and industry-standard way to model data and reduces vendor lock-in as PostgreSQL can be hosted anywhere <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Missing features include website hosting, requiring external services like Vercel or Netlify <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Its SDKs are primarily focused on the web, with some support for React Native, [[flutter_app_integration_with_firebase | Flutter]], and Ionic, but less emphasis on native iOS/Android <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

Supabase is popular on the web, with over 40,000 weekly downloads <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Pricing
Supabase has a free tier, but it limits users to two projects and projects may sleep after inactivity <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For serious projects, pricing starts at $25 per month, covering usage up to 100,000 monthly active users, then switches to pay-as-you-go <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This pricing is considered a good deal compared to other relational database hosting <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Developer Experience
Supabase makes relational databases easy to use, providing a browser-based tool to manage data and integrating with user authentication for row-level security policies <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Its JavaScript SDK is enjoyable, similar to the [[introduction_to_firebase_and_benefits | Firebase]] SDK with dot notation for data access <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. It also supports GraphQL and offers features like full-text search and table counts, which are lacking in [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Real-time data access requires manual opt-in but is easy to subscribe to via the SDK <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Nhost

Nhost is an open-source [[introduction_to_firebase_and_benefits | Firebase]] alternative focused on GraphQL, built on Hasura, a platform that turns a relational database into a GraphQL API <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Key Features and Popularity
Nhost's pricing is similar to Supabase, offering a free tier for experimenting and starting at $25 per month for serious projects <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. While its own npm downloads might not be high, Hasura's popularity suggests a broader reach <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

The UI is intuitive, allowing visualization of database records <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. A key feature is that the PostgreSQL database also functions as a GraphQL API, enabling in-browser query and mutation testing <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. However, some tasks, like updating database permissions, require accessing Hasura directly <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Developer Experience
Nhost has first-class support for React, providing hooks for authentication with a single line of code <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Database queries involve GraphQL and Apollo Client, which are powerful but have a learning curve and can be more verbose than [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This approach offers more robustness but can add friction for quick prototyping <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Nhost is a strong competitor to Supabase, especially for those who prefer GraphQL <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Appwrite

Appwrite is another open-source backend solution for web and mobile developers, sharing similar infrastructure pieces with Nhost and Supabase <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Key Features and Popularity
Appwrite provides SDKs for both web and mobile <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Currently, it's not a commercial product and requires self-hosting, which can be done with a one-click install on DigitalOcean <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. A fully managed service, Appwrite Cloud, is planned for the future <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

Being free and open source eliminates vendor lock-in, but self-hosting can paradoxically be more expensive without a startup covering infrastructure costs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. While its JavaScript SDK doesn't have many downloads, its Docker image has over 5 million pulls, indicating significant usage <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Appwrite boasts an impressive list of authentication methods <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Its database is a NoSQL document database, similar to MongoDB or Firestore, but it's based on MariaDB (a relational database and MySQL fork), offering a NoSQL API to work with a traditional SQL database <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Developer Experience
Appwrite offers easy one-liners for authentication and database management <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. However, it does not currently support GraphQL <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Appwrite is seen as a tool with significant potential <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## MongoDB Realm

MongoDB Realm leverages MongoDB, the most popular document-oriented database, to provide tools focused on mobile developers <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Key Features and Popularity
MongoDB Realm can sync data from MongoDB Atlas to any web or mobile platform <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. While its JavaScript SDK downloads are not high, its strong focus on mobile platforms indicates its primary audience <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Pricing
Pricing primarily depends on MongoDB Atlas usage (serverless or dedicated), with additional pay-as-you-go pricing for compute time for serverless functions <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Developer Experience
The dashboard features authentication, though it may feel limited compared to other options <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Its main strength lies in its database capabilities and the ability to sync with front-end applications <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. It can also generate a GraphQL API from the database <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

Accessing data is more complex than [[introduction_to_firebase_and_benefits | Firebase]], requiring developers to define a schema for Realm objects to translate MongoDB data for application use <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Once set up, it simplifies real-time subscriptions and supports GraphQL and Apollo <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. MongoDB Realm is a strong option, particularly for existing MongoDB users, though it might feel more advanced for newcomers <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Parse

Parse is an older platform, launched in 2013, which was acquired and then shut down by Facebook before becoming open source and actively maintained <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Conclusion

Ultimately, choosing a backend platform involves trade-offs. The most crucial factor is getting the application shipped <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. While some platforms offer quicker development, they might lead to vendor lock-in, which can be difficult to escape from later <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a> <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.