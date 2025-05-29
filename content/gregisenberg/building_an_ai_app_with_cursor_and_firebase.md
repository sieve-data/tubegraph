---
title: Building an AI App with Cursor and Firebase
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details the process of [[building_an_ios_app_using_ai | building an AI app]] from scratch, utilizing Cursor AI, integrating various APIs, and setting up a Firebase database for user management and image storage, before finally deploying it to Vercel.

## Why Choose Cursor AI?
Recently, the speaker has transitioned to predominantly using [[using_ai_and_cursor_to_build_mobile_apps | Cursor AI]] for app development <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While many excellent AI tools exist for coding, such as Bolt, [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]] for front-end development, Windsurf, and Replit, [[best_practices_for_using_cursor_ai | Cursor]] has become the preferred choice <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The AI coding space is considered highly enjoyable for development <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Previously, a common workflow involved building the front end with [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]] and then importing it into [[best_practices_for_using_cursor_ai | Cursor]] for running code locally <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Replit was used for its easy templates, deployment, and live web view, syncing codebases with Cursor via SSA <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. However, [[best_practices_for_using_cursor_ai | Cursor]] has introduced a new feature called Agent within Composer <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The Agent, significantly improved over the last month and a half, is considered the most legitimate agent on the market <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This advancement means developers no longer need Replit for templates; they can use GitHub and instruct [[best_practices_for_using_cursor_ai | Cursor]] to run projects locally <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Initial Setup with Cursor Agent
The full process for using [[best_practices_for_using_cursor_ai | Cursor]] Agent to run an app locally is straightforward:
1.  **Open Cursor and Create a Project**: Start by opening [[best_practices_for_using_cursor_ai | Cursor]] and selecting "Open a folder" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Create a new, blank folder (e.g., "Riley Greg Pod 4") in a temporary location <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
2.  **Access Composer**: Once the folder is open, press the composer button to access [[best_practices_for_using_cursor_ai | Cursor]]'s main interface <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
3.  **Clone and Run Repository**: Use a single command to clone a GitHub repository and run it locally. For example, `clone the repo and run it locally in one command` followed by the GitHub link <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   **YOLO Mode**: [[best_practices_for_using_cursor_ai | Cursor]] offers "YOLO mode," which automatically executes commands without confirmation prompts, streamlining the process <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. While convenient for ease of use, it's recommended to only use it with trusted sources from GitHub <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. More technical users might prefer manual control <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
4.  **Local Web View**: After running, [[best_practices_for_using_cursor_ai | Cursor]] will provide a local host link (e.g., `http://localhost:3001`). Command-clicking this link opens the project in a web view, allowing live changes to be observed <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Integrating APIs for AI Features
[[building_apps_using_ai_tools | Building apps using AI tools]] often requires integrating APIs (Application Programming Interfaces).
1.  **Understanding APIs**: APIs act as instruction manuals for how different coding rules apply <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. [[best_practices_for_using_cursor_ai | Cursor]] needs examples to understand how specific APIs function <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
2.  **Finding API Examples**:
    *   **Perplexity**: Can be used to find Next.js code examples for various AI models, such as Flux on Replicate for image generation <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    *   **Replicate & Foul**: These platforms offer a wide array of creative AI models, making it easier to integrate AI features into new applications <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
    *   **API Documentation (Docs)**: For troubleshooting, it's crucial to consult the API's official documentation. Asking AI questions about the documentation can also be helpful <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
    *   **Playgrounds**: Many AI services provide playgrounds (e.g., Replicate's playground) where users can test models and generate images, then get the exact code used to produce the output. This code serves as a reliable example for implementation <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
3.  **API Keys/Tokens**: Most APIs require an API token or key for authentication and billing purposes, as API usage often incurs costs (e.g., 2-3 cents per image generation) <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. These keys track usage <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. [[best_practices_for_using_cursor_ai | Cursor]] can be instructed to place these tokens in the correct `.env` file <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
4.  **Prompting Cursor for API Integration**: When using an API with [[best_practices_for_using_cursor_ai | Cursor]], provide:
    *   Clear instructions (e.g., "create a simple AI image generator") <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
    *   Code examples from documentation or playgrounds <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
    *   The API token <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

### Example: Building an AI Image Generator
An example of [[building_a_social_media_app_using_ai | building an AI image generator]] was demonstrated using Replicate. Initial attempts may fail, but by pasting the error messages back into [[best_practices_for_using_cursor_ai | Cursor]] and providing additional context, documentation links, and working playground examples, [[best_practices_for_using_cursor_ai | Cursor]] Agent can iteratively fix the issues <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. It's crucial to provide [[best_practices_for_using_cursor_ai | Cursor]] with all observed information, as it cannot see the web view <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

## Adding Features and Iteration
After the core functionality is established, additional features and design elements can be added:
*   **UI Enhancements**: Implement user interface (UI) elements like info popups to display generation details (model used, parameters) or toggles to switch between different AI models (e.g., Flux Pro, Ideogram) <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   **Iterative Development**: Embrace errors and delays as part of the development process <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. Iterative building is often more enjoyable than expecting a perfect one-shot solution <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. Challenges lead to deeper learning <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.
*   **Design First or Feature First**: Some developers prefer to start with design using tools like [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]], while others prefer to get core features working first before refining the design <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. [[best_practices_for_using_cursor_ai | Cursor]] can handle design changes like updating the interface to look more modern and adding app titles <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

## Integrating Firebase for User Management and Storage
To add user authentication and persistent storage, Firebase is an excellent choice.
1.  **Firebase Project Setup**:
    *   Go to the Firebase console and create a new project <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Disable Google Analytics initially for simplicity <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
    *   Register a web app within the Firebase project <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.
    *   Copy the Firebase API keys provided and paste them into [[best_practices_for_using_cursor_ai | Cursor]]'s composer, instructing it to place them in the correct `.env` file <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
2.  **Setting up Firebase Services**:
    *   **Firestore Database**: Navigate to "Build" -> "Firestore Database" and create a database, starting in test mode for easier development <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>.
    *   **Storage**: For apps storing images or files, enable Storage <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>. It's advisable to set a spending limit to prevent unexpected charges from potential attacks <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>.
    *   **Authentication**: Enable Google authentication <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. When running locally, Firebase automatically sets up authentication for `localhost` <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
3.  **Prompting Cursor for Firebase Integration**: Instruct [[best_practices_for_using_cursor_ai | Cursor]] to:
    *   Allow users to sign in with Google <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Restrict homepage access if the user isn't signed in <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Automatically save generated images to their storage <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Add a "My Images" tab in the top bar leading to a new page displaying all generated images <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

## Deployment with Vercel
Deploying the application to the internet involves pushing the code to GitHub and using Vercel.
1.  **GitHub Repository**: Create a new public repository on GitHub <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>. [[best_practices_for_using_cursor_ai | Cursor]] Agent can often create the repository directly, so manual GitHub creation might not be necessary <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
2.  **Deploying with Vercel CLI via Cursor Agent**:
    *   Instruct [[best_practices_for_using_cursor_ai | Cursor]] to deploy the app to Vercel and commit it to GitHub <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
    *   [[best_practices_for_using_cursor_ai | Cursor]] will use the Vercel CLI to manage the deployment process <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
    *   Follow the prompts in the terminal (e.g., confirm setup, project name, directory) <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>.
    *   Vercel will begin building the deployment, which can be monitored via the provided link <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>.
3.  **Vercel Environment Variables**: Deployment might fail initially if API keys aren't correctly configured in Vercel.
    *   Go to your Vercel project overview, then to "Settings" and "Environment Variables" <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.
    *   Add the necessary API keys (e.g., `REPLICATE_API_TOKEN`) <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
    *   After adding, redeploy the project <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.
4.  **Firebase Authorized Domains for Deployment**: For the deployed app to function correctly with Firebase authentication, the Vercel domain must be authorized.
    *   In the Firebase console, go to "Authentication" -> "Settings" -> "Authorized domains" <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>.
    *   Add the Vercel deployment URL (e.g., `rileygregpod.vercel.app`) to the list <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>.
    *   After authorizing the domain, the deployed app should allow user sign-in and function as expected <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

## Conclusion
In under two hours, an AI app was built using [[best_practices_for_using_cursor_ai | Cursor]] Agent, starting with an empty folder and a GitHub template <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. The process involved:
1.  Running a template locally with a single command <a class="yt-timestamp" data-t="01:10:52">[01:10:52]</a>.
2.  Developing an AI image generator, iteratively resolving errors by providing additional documentation and examples to [[best_practices_for_using_cursor_ai | Cursor]] <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>.
3.  Adding multiple AI image models and displaying image parameters <a class="yt-timestamp" data-t="01:11:28">[01:11:28]</a>.
4.  Integrating Firebase for Google authentication and image storage, ensuring user-specific data <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.
5.  Deploying the fully functional application to the internet via Vercel <a class="yt-timestamp" data-t="01:11:48">[01:11:48]</a>.

The speaker's current project, Yap Thread (`app.yapthread.com`), is a writing tool with AI features for note-taking, chatting with AI, and creating compositions <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>. Additionally, a free community for [[building_apps_using_ai_tools | building AI apps]], Software Composers, is available, offering templates and discussions <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>. The journey of building with AI, especially with tools like [[best_practices_for_using_cursor_ai | Cursor]], emphasizes the importance of a resilient mindset, embracing challenges, and continuous learning <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.