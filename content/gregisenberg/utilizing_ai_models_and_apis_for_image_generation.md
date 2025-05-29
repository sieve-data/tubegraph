---
title: Utilizing AI models and APIs for image generation
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details the process of building applications using AI, specifically focusing on creating an AI image generator from scratch and deploying it. The workflow heavily relies on Cursor, an AI-first code editor, and various external APIs and services <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Core Tools and Workflow

The primary tool for development is **Cursor**, which is used for building apps with AI <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Other notable AI tools in the coding space include V0, Windsurf, Replit, and Lovable <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The traditional workflow involved starting with frontend design on VZ, then importing it into Cursor, and using Replit for live web view and deployment <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Replit is praised for its ease of use with templates and deployment <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, a new feature in Cursor, **Agent**, has significantly simplified the process <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. With Agent, the need for Replit's live web view has diminished, now primarily using GitHub for templates and running locally <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Building an AI Image Generator with Cursor Agent

### Initial Setup and Local Execution
The first step is to open Cursor and create a new project by opening a blank folder on your computer <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. From within Cursor, you can access the Composer feature <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

To get started, you can use a pre-made Next.js template hosted on GitHub <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. A simple prompt like "clone the repo and run it locally in one command" with the GitHub link allows Cursor Agent to set up the project locally <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Cursor Agent can automatically handle cloning the repository and installing dependencies for Next.js projects <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Cursor offers a "YOLO mode" which automatically confirms commands without requiring repeated "yes" clicks, though users are advised to trust the source of any cloned repository <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Once set up, the app runs on a local host (e.g., `localhost:3001`), allowing for live changes <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Integrating APIs for Image Generation
To add [[ai_content_generation | AI content generation]] features, such as image generation, you need to integrate external APIs. The process involves:
1.  **Finding Code Examples**: Use tools like Perplexity to search for Next.js code examples for specific AI image models (e.g., Flux on Replicate) <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. These examples act like "instruction manuals" for Cursor, as it doesn't inherently understand API rules <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
2.  **Providing API Tokens**: Most APIs require an API token or key, as using them incurs costs <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. You obtain these from the API provider's dashboard (e.g., Replicate.com) <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. You then instruct Cursor to place this token in the correct `.env` file <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
3.  **Prompting Cursor**: The general pattern for API integration is: Instructions (what you want to build), Examples (code snippets from docs or playgrounds), and API Token <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

```
I want to create a simple AI image generator. I want to use Replicate and I want to use Flux.
[Paste code examples from Perplexity]
This is my API token: [Your API Token]. Please put it in the correct place.
```
This comprehensive prompt allows Cursor to generate the necessary code <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

### Troubleshooting and Iteration
It's common to encounter errors during development <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. When an error occurs, paste the error message back into Cursor. To help Cursor, provide additional information:
*   **API Documentation (Docs)**: Find the official documentation for the API (e.g., Replicate docs) <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Playground Examples**: Many AI services offer "playgrounds" where you can test models and get working code examples <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. Copy these examples and provide them to Cursor <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Detailed Observations**: Explain exactly what happened (e.g., "it failed immediately," "it loaded for a bit then failed") because Cursor doesn't see your web view <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

This iterative process of providing more context and examples helps Cursor debug and fix the code <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. This highlights that [[automating_software_creation_with_ai | automating software creation with AI]] is often an iterative process, not a one-shot solution <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.

### Enhancing Features and Design
Once the basic image generation works, you can add more features:
*   **Model Selection**: Implement a toggle or dropdown to switch between different AI image models (e.g., initial model, Flux Pro, Ideogram) <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a>. Ideogram is noted for its ability to add text within images <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
*   **Generation Details Pop-up**: Create a user interface element (e.g., an info icon bubble) that displays the model used and all parameters for the generated image upon click <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This aids in testing and understanding model performance <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **Design Improvements**: After core functionality, focus on [[using_ai_for_creating_production_ready_designs | redesigning the interface]] to look more modern, ensuring no functionality is broken <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. You can specify elements like a title in the top bar <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. This is an example of [[asset_generation_with_ai_for_app_design | asset generation with AI for app design]].

## Integrating a Database (Firebase)
To save generated images and user data, a database is essential. The template used was preconfigured with Google Firebase authentication and storage <a class="yt-timestamp" data-t="00:42:54">[00:42:54]</a>.

The steps to set up Firebase manually after prompting Cursor to implement it are:
1.  **Create Firebase Project**: Go to the Firebase console and create a new project (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. Do not enable Google Analytics to simplify initial setup <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
2.  **Add Web App**: Register a web app within your Firebase project to get its API tokens <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>. Provide these API tokens to Cursor to place in the `.env` file <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.
3.  **Firestore Database**: In the "Build" section, enable Firestore Database, starting in test mode for easier development <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>.
4.  **Storage**: Enable Storage to save images. It's recommended to set a spending limit (e.g., $20) to prevent unexpected bills <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.
5.  **Authentication**: Enable Google Authentication. Localhost is automatically authorized <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

After setup, users can sign in with Google, and generated images will automatically save to their storage. A "My Images" tab can be added to the top bar to display all saved images <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## Deployment (Vercel)

The final step is to deploy the app to the internet. Vercel is used for deployment <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.

1.  **GitHub Repository**: Create a new public repository on GitHub for your project <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.
2.  **Deploy with Cursor Agent**: Instruct Cursor Agent to "deploy this app to Vercel and commit it to GitHub" with the GitHub repo link <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Cursor can often create the GitHub repo automatically <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
3.  **Vercel Setup**: If not already logged in, Cursor Agent will prompt you to sign in to Vercel <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>. You select personal or business, choose not to link to an existing project (if new), name the project, and confirm directory settings <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
4.  **Environment Variables**: A common deployment failure is missing API keys. Navigate to your Vercel project settings, then "Environment Variables," and add all necessary API keys (e.g., `REPLICATE_API_TOKEN`) <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. After adding, redeploy the project <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.
5.  **Firebase Authorized Domains**: For authentication to work on the deployed site, you must add the Vercel domain to the "Authorized Domains" list in your Firebase Authentication settings <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

Once deployed, the app will be live on a Vercel domain <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>. This process showcases how [[using_ai_for_app_development | AI for app development]] can lead to a fully functional, deployed application in a relatively short time <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.

## Conclusion and Tips
The entire process, from setting up a blank project to deploying a full-stack AI image generator with user authentication and image saving, can be completed efficiently using Cursor Agent <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>.

*   **Learning Mindset**: Approach AI development with the expectation that it will be challenging and iterative, rather than a single prompt solution <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. Learning comes most from struggling through problems <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.
*   **Templates**: Using pre-configured templates (e.g., with Firebase) significantly speeds up development <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.
*   **Iterative Building**: It's more enjoyable and effective to iteratively build and test features rather than trying to create a complete app from scratch in one go <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Cursor History**: Cursor's new feature allows viewing and rolling back project history, effectively replacing the need for manual Git saves <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.
*   **Prototyping**: Building "absurd" tools or simple prototypes can be a great way to learn and "sketch" ideas without immediate commercial pressure <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>. This is part of the broader field of [[using_ai_in_content_creation | using AI in content creation]].

This detailed walk-through demonstrates the power of [[productized_services_using_ai | productized services using AI]] and how developers can leverage these tools to build complex applications relatively quickly.