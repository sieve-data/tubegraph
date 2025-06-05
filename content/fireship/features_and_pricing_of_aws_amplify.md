---
title: Features and pricing of AWS Amplify
videoId: SXmYUalHyYk
---

From: [[fireship]] <br/> 

[[AWS Computer Services and Tools | AWS Amplify]] is Amazon's answer to Firebase, offering a comprehensive set of features for web and mobile developers <a class="yt-timestamp" data-t="02:30:46">[02:30:46]</a>.

## Key Features

[[AWS Computer Services and Tools | AWS Amplify]] provides an impressive array of features, some of which are not commonly found in other Backend-as-a-Service (BaaS) options <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>:
*   Analytics <a class="yt-timestamp" data-t="02:36:09">[02:36:09]</a>
*   Predictions <a class="yt-timestamp" data-t="02:37:19">[02:37:19]</a>
*   Notifications <a class="yt-timestamp" data-t="02:37:92">[02:37:92]</a>

## Database Integration

The primary database used by [[AWS Computer Services and Tools | AWS Amplify]] is [[AWS Database Offerings | DynamoDB]] <a class="yt-timestamp" data-t="02:42:75">[02:42:75]</a>. Although [[AWS Database Offerings | DynamoDB]] can be challenging to work with directly, Amplify automates the creation of a GraphQL API for your data <a class="yt-timestamp" data-t="02:47:76">[02:47:76]</a>.
It also includes a no-code tool for defining data relationships <a class="yt-timestamp" data-t="02:51:75">[02:51:75]</a>. Additionally, it's possible to connect a relational database to your API <a class="yt-timestamp" data-t="02:55:50">[02:55:50]</a>. A significant advantage over Firebase is the ability to make your data searchable with Elasticsearch <a class="yt-timestamp" data-t="02:58:36">[02:58:36]</a>.

## Authentication

User authentication in [[AWS Computer Services and Tools | AWS Amplify]] is handled by AWS Cognito, which is described as more mature than Firebase's offering <a class="yt-timestamp" data-t="03:02:64">[03:02:64]</a>. A key capability is the creation of user groups to control access within a project <a class="yt-timestamp" data-t="03:08:44">[03:08:44]</a>.

## [[Pricing Models and Cost Comparison | Pricing]]

[[AWS Computer Services and Tools | AWS Amplify]] operates on a pay-as-you-go [[Pricing Models and Cost Comparison | pricing model]], similar to Firebase <a class="yt-timestamp" data-t="03:13:20">[03:13:20]</a>. Users need to carefully calculate their anticipated usage to understand costs <a class="yt-timestamp" data-t="03:16:74">[03:16:74]</a>.

## Drawbacks

A potential drawback when using [[AWS Computer Services and Tools | AWS Amplify]] is vendor lock-in, especially if you utilize proprietary [[Introduction to Amazon Web Services AWS | AWS]] products <a class="yt-timestamp" data-t="03:19:35">[03:19:35]</a>.

## Developer Experience and Popularity

[[AWS Computer Services and Tools | AWS Amplify]] provides SDKs for all major web and mobile platforms <a class="yt-timestamp" data-t="03:23:67">[03:23:67]</a>. It is a strong competitor to Firebase in terms of popularity, with approximately 400,000 weekly downloads <a class="yt-timestamp" data-t="03:27:12">[03:27:12]</a>.

The developer experience with [[AWS Computer Services and Tools | AWS Amplify]] differs from Firebase <a class="yt-timestamp" data-t="03:32:41">[03:32:41]</a>. It relies heavily on code generation to create the backend API for your data, which means a significant amount of code is dumped into your project that requires constant synchronization with [[Introduction to Amazon Web Services AWS | AWS]] <a class="yt-timestamp" data-t="03:36:51">[03:36:51]</a>. However, this approach provides a positive developer experience for data fetching, as the GraphQL schema offers Intellisense <a class="yt-timestamp" data-t="03:44:81">[03:44:81]</a>. Developers can achieve simple one-liner data operations, similar to the Firebase SDK, without manually writing GraphQL queries <a class="yt-timestamp" data-t="03:51:19">[03:51:19]</a>.