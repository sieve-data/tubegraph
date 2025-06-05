---
title: APIs and thirdparty services in web development
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

APIs (Application Programming Interfaces) constitute a crucial layer in a web application's technology stack. They act as the tools that [[frontend_and_backend_development_layers | connect the front end to the back end]] <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. This layer can involve custom-built APIs, but more commonly, it incorporates essential third-party services that are integral to the application's functionality <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. These services often provide functionalities that span both the frontend and [[backend_development_and_serverside_concepts | backend]] categories, positioning them as a central component of the stack <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Role in the Tech Stack

APIs and third-party services are considered the "third and final layer" of a tech stack <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. They enable applications to perform complex tasks that would be too difficult or time-consuming to build from scratch <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>, <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.

## Common Third-Party Services

Developers frequently integrate various third-party services to handle specific functionalities:
*   **Payments**
    *   Stripe: Provides SDKs for both server and frontend to collect payments <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>, <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.
*   **Messaging**
    *   Twilio: Used for sending text messages to users <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>, <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
    *   SendGrid: Used for email functionalities <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   **User Authentication**
    *   Auth0: Handles user authentication processes <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Content Moderation**
    *   Amazon Rekognition: Offers deep learning capabilities, such as image detection <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.

## API Communication Protocols

While developers can roll out their own APIs, common protocols and libraries are used to facilitate communication:
*   **[[understanding_restful_apis | REST]]** <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>
*   **GraphQL**
    *   Often described as "awesome" <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
    *   Can be added to a stack with libraries like Apollo, which provide code for both the frontend and [[backend_development_and_serverside_concepts | backend]] to build a GraphQL API <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>, <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>.
    *   Enables the frontend to securely communicate with the [[backend_development_and_serverside_concepts | backend]] <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.
    *   More suitable for complex applications that involve stitching together multiple APIs <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.

## Simplifying with Integrated Services (e.g., Firebase)

For simpler or rapidly developing applications, integrated platforms like Firebase can significantly streamline the API and [[backend_development_and_serverside_concepts | backend]] layers:
*   **Simplified [[backend_development_and_serverside_concepts | Backend]]**: Firebase provides a document database that scales without the need for a separate [[backend_development_and_serverside_concepts | backend]] server <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>, <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **Built-in Authentication**: It includes user authentication services <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
*   **Easy Integration**: Can be included by simply adding a script tag to the document <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
*   **Serverless Functions**: Firebase Cloud Functions offer a serverless option for writing [[backend_development_and_serverside_concepts | server-side]] code in Node.js, Python, or Go <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>, <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. These functions deploy with a single command and scale automatically without requiring concerns about server configuration, Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>, <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.