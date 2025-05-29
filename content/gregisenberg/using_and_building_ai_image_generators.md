---
title: Using and Building AI Image Generators
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details the process of [[using_ai_to_build_software_applications | building software applications]] with AI, specifically focusing on creating an AI image generator using Cursor and its Agent feature. The workflow emphasizes rapid prototyping, iterative development, and deployment of a full-stack application.

## Key Tools for AI App Development

Numerous AI tools are available for coding, making it a dynamic and engaging space <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Some notable tools include:
*   **Vercel** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Zero** (for front-end) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Wind Surf** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Cursor** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Replit** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Lovable** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

The primary tool for this demonstration is **Cursor**, particularly its recently released **Agent** feature within Composer <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Evolution of the Development Workflow
Initially, a workflow involved:
1.  Building the front end on **Vercel** <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Importing the front end into **Cursor** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
3.  Using **Replit** for a live web view and easy deployment <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Replit was favored for its easy-to-use templates and simplified deployment compared to other platforms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Codebases were synced via SSH <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

More recently, **Cursor Agent** has significantly improved, making the workflow simpler <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The Agent is considered "the most legit agent on the market" due to rapid improvements in the last month and a half <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. The new approach uses **GitHub** for templates, eliminating the need for Replit for web view as Cursor Agent can now run apps locally <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a> <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Building an App Locally with Cursor Agent
To start building an app locally using Cursor Agent:
1.  **Open Cursor** <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  **Open a Folder**: Select a location on your computer and create a new, empty folder for the project <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  **Access Composer**: Click the button to open Composer within Cursor <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
4.  **Clone and Run**: Use a single command to tell Cursor to clone a GitHub repository (e.g., a Next.js template) and run it locally <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. For example, "clone the repo and run it locally in one command" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   A template for Next.js has over 15,000 uses on Replit <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
5.  **YOLO Mode**: Cursor offers a "YOLO mode" which automatically confirms commands, eliminating the need to click "yes" repeatedly <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. While convenient, it's advised for informational purposes only, as it runs commands without explicit user confirmation <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a> <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
6.  **Live View**: Once the app is running, Cursor provides a local host link (e.g., Port 3001) to view changes live in a web browser <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a> <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a> <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Integrating APIs for Image Generation
APIs (Application Programming Interfaces) can be thought of as "instruction manuals" that allow different software components to communicate <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Cursor doesn't inherently understand how every API works, so examples and context are crucial <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

To integrate an AI image model:
1.  **Identify API Platforms**: Platforms like **Replicate** <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a> and **Vercel** <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a> offer a wide range of creative AI models and make it easier to add AI features to applications <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
2.  **Find Code Examples**:
    *   Use tools like **Perplexity** to request Next.js code examples for specific AI models (e.g., Flux on Replicate for image generation) <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a> <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
    *   Consult **API documentation (docs)** directly from the service (e.g., Replicate's docs) <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
    *   Utilize **Playgrounds**: Many AI apps have playgrounds where you can test models and generate code examples that worked successfully, which can then be provided to Cursor <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a> <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. This allows for diligent testing of model performance before coding <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
3.  **API Keys/Tokens**: Most APIs require an API token for usage, as using these services often incurs costs (e.g., 2-3 cents per image generation) <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a> <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   Find your API token on the service's website (e.g., replicate.com) <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
    *   Provide the API token to Cursor, instructing it to place it in the correct environment file (e.g., `.env.local`) <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a> <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
4.  **Prompting Cursor**: When working with an API, provide Cursor with:
    *   Clear instructions (e.g., "I want to create a simple [[ai_tools_for_generating_creative_assets | AI image generator]]") <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a> <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
    *   Code examples <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
    *   Your API token <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
    *   If errors occur, paste the error message and any additional relevant documentation or successful playground examples back into Cursor <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a> <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. The more context and information given, the better Cursor can debug and implement <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

### Iterative Development and Adding Features
AI coding is an iterative process; it's not always a "one-shot" success <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.
*   **Debugging**: Expect errors; it's common to restart servers or provide more context to Cursor for troubleshooting <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a> <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>. Cursor Agent can be compared to a junior or mid-level developer in its ability to understand and fix issues <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.
*   **Adding Functionality**:
    *   **Model Toggles**: Implement a toggle to switch between different AI image models (e.g., defaulting to Flux Pro, offering an older model, and adding advanced models like Ideogram for text in images) <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a> <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.
    *   **Generation Details**: Display model parameters and other information below generated images, which can help users understand and replicate results <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   **Mindset**: Approach AI coding with the expectation that it will be difficult and require persistent effort, as struggling leads to greater learning <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a> <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>. It's more fun to iteratively build and "sketch" ideas live than to focus solely on commercially valuable outcomes initially <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a> <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>.

### Design and User Interface
After establishing core features, focus on design <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. Cursor can redesign the interface while maintaining functionality, making it significantly more modern <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>. This includes adding elements like a title in the top bar <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.

## Integrating a Database (Firebase)
To save user data and generated images, integrate a database:
1.  **Firebase Project**:
    *   Go to Firebase console and create a new project <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>.
    *   Do not enable Google Analytics initially for simplicity <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
2.  **Web App Configuration**: Register a web app within Firebase <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a> <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
3.  **Firebase API Tokens**: Copy the generated Firebase API tokens and provide them to Cursor, instructing it to place them in the correct environment file <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a> <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.
4.  **Database Services**:
    *   **Firestore Database**: Create a Firestore database, starting in test mode for easier development (rules are relaxed) <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a> <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.
    *   **Storage**: Enable storage to save images <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a> <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>. It's recommended to set a spending limit to prevent unexpected charges from potential attacks or high usage <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>.
    *   **Authentication**: Enable Google authentication for user sign-in <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a> <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>. Local host environments are automatically authorized by Firebase, simplifying development <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
5.  **User Features**:
    *   Implement user sign-in: The app should only display the homepage after a user signs in <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>.
    *   Automatic image saving: Generated images should automatically save to the user's Firebase storage <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
    *   "My Images" Tab: Add a navigation tab to display all images generated by the signed-in user <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

## Deployment to Vercel
To make the app publicly accessible:
1.  **GitHub Repository**: Create a new public repository on GitHub <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a> <a class="yt-timestamp" data-t="00:55:15">[00:55:15]</a>. Cursor Agent may be able to create the repository automatically <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
2.  **Deploy with Cursor Agent**: Instruct Cursor Agent to deploy the app to Vercel and commit the code to GitHub <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a> <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>.
    *   Cursor uses the Vercel CLI for deployment <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
    *   Follow the CLI prompts to link the local project to a new Vercel project <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>.
3.  **Vercel Environment Variables**: Crucially, add all necessary API tokens (e.g., Replicate API token) to the Vercel project's environment variables in the settings tab <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a> <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a> <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.
4.  **Firebase Authorized Domains**: In Firebase Authentication settings, add the newly deployed Vercel domain to the list of authorized domains to enable sign-in on the live app <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.
5.  **Test Deployment**: Confirm that the app is accessible online, users can sign in, and images are saved <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a> <a class="yt-timestamp" data-t="01:10:15">[01:10:15]</a>.

This entire process, from setting up a local project to deploying a full-stack AI image generator with user authentication and image storage, can be achieved in a relatively short timeframe using Cursor Agent <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. It demonstrates the power of [[creating_content_with_ai_tools | AI tools for content creation]] and [[adapting_to_ai_for_content_creation | adapting to AI for content creation]].

## Resources
*   Yap Thread: app.yapthread.com <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>
*   Software Composers Community: A free community for building AI apps and accessing templates <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a> <a class="yt-timestamp" data-t="01:13:20">[01:13:20]</a>.