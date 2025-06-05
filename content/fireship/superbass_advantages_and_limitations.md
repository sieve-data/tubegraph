---
title: Superbass advantages and limitations
videoId: SXmYUalHyYk
---

From: [[fireship]] <br/> 

Superbass, launched during Y Combinator Season 20, is a platform offering core features such as authentication, file storage, and serverless functions <a class="yt-timestamp" data-t="03:59:44">[03:59:44]</a>.

## Key Features and Advantages

Superbass's main distinguishing feature is its use of PostgreSQL, an open-source relational database <a class="yt-timestamp" data-t="04:09:43">[04:09:43]</a>. This provides several benefits:
*   **Data Modeling Flexibility**: It offers a more flexible and industry-standard approach to model data <a class="yt-timestamp" data-t="04:14:83">[04:14:83]</a>.
*   **Reduced Vendor Lock-in**: Users don't have to worry as much about vendor lock-in, as a PostgreSQL database can be hosted anywhere <a class="yt-timestamp" data-t="04:19:93">[04:19:93]</a>.
*   **Ease of Use for Relational Databases**: Superbass simplifies working with relational databases, providing a browser-based tool for data management <a class="yt-timestamp" data-t="05:00:88">[05:00:88]</a>.
*   **Authentication Integration**: It integrates well with user authentication, allowing for the implementation of row-level security policies to control data access <a class="yt-timestamp" data-t="05:07:07">[05:07:07]</a>.
*   **Developer Experience**: The JavaScript SDK is designed to be enjoyable, similar to the original [[introduction_to_firebase_and_benefits | Firebase]] SDK, using dot notation for data access and operations <a class="yt-timestamp" data-t="05:12:87">[05:12:87]</a>.
*   **GraphQL Support**: Superbass also supports GraphQL as an alternative <a class="yt-timestamp" data-t="05:22:42">[05:22:42]</a>.
*   **PostgreSQL Capabilities**: PostgreSQL inherently supports features like full-text search and can return a table's count, which is a missing feature in [[introduction_to_firebase_and_benefits | Firebase]] <a class="yt-timestamp" data-t="05:26:95">[05:26:95]</a>.

## Limitations and Drawbacks

Despite its advantages, Superbass has some limitations:
*   **Missing Features**: It lacks certain features like website hosting, which means users might also need services like Vercel or Netlify <a class="yt-timestamp" data-t="04:23:44">[04:23:44]</a>.
*   **SDK Focus**: Its SDKs are primarily focused on the web, though they do support tools like React Native, Flutter, and [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | Ionic]]. There appears to be less focus on native iOS and Android development <a class="yt-timestamp" data-t="04:29:16">[04:29:16]</a>.
*   **Real-time Access**: Real-time access to data is not out-of-the-box and requires manual opt-in, though it can be easily subscribed to via the SDK once enabled <a class="yt-timestamp" data-t="05:32:48">[05:32:48]</a>.

## Pricing

Superbass offers a free tier, but it is limited to two projects and projects will "sleep" after inactivity <a class="yt-timestamp" data-t="04:41:92">[04:41:92]</a>. For more serious projects, pricing starts at $25 per month, which includes enough usage for up to 100,000 monthly active users before transitioning to a pay-as-you-go model <a class="yt-timestamp" data-t="04:47:11">[04:47:11]</a>. This pricing is considered a great deal compared to relational databases elsewhere <a class="yt-timestamp" data-t="04:55:06">[04:55:06]</a>.

## Popularity

Superbass has gained significant popularity on the web, with over 40,000 weekly downloads <a class="yt-timestamp" data-t="04:36:99">[04:36:99]</a>.