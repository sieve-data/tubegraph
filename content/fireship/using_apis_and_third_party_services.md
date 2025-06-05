---
title: Using APIs and Third Party Services
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

APIs (Application Programming Interfaces) are tools used to connect the front-end to the back-end of an application <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. They facilitate communication between different parts of a system <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

## Types of APIs
APIs can be rolled out independently, such as through [[introduction_to_restful_apis | REST]] or GraphQL <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. For example, GraphQL can be integrated with a library like Apollo to provide code on both the front-end and back-end, allowing secure communication between them <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.

## Role of Third-Party Services
Beyond custom APIs, a tech stack often includes essential third-party services necessary to run an application <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. These services perform functionalities that are often too complex or specialized to handle from scratch <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. They can fall into both back-end and front-end categories <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

Common examples of such services include:
*   **Stripe**: For handling payments, providing SDKs for both server and front-end integration <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>, <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Twilio**: For sending text messages to users <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>, <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   **SendGrid**: For email functionalities <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   **Auth0**: For managing user authentication <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
*   **Amazon Rekognition**: For deep learning capabilities, such as image detection <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

## Simplification
While complex APIs and numerous third-party services can be part of an over-engineered tech stack <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>, simplifying API usage is often beneficial. For example, GraphQL might be more suited for complex applications that stitch together multiple APIs <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>. For simpler needs, services like [[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]] can handle server-side code without worrying about server configurations or complex API orchestration <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.