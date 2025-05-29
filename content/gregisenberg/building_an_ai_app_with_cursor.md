---
title: Building an AI app with Cursor
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details a process for [[using_ai_for_app_development | building an AI app]] primarily using Cursor AI, highlighting its recent advancements, particularly the Agent feature. It covers initial setup, API integration, debugging, feature additions, database implementation, and deployment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Why Cursor AI?

The speaker emphasizes a recent shift to exclusively using Cursor for [[using_ai_for_app_development | building apps with AI]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While many good AI tools exist for coding, such as Bolt, Vzero, Windsurf, Cursor, and Replit <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, Cursor's new Agent feature has made it a preferred choice <a class="yt-timestamp" data-t="02:02:08">[02:02:08]</a>.

Previously, a common workflow involved building the front end with Vzero, importing it into Cursor, and using Replit for live web views and easy deployment <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>. Replit was favored for its simple templates and deployment compared to other platforms <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>. Cursor was connected to Replit by syncing codebases via SSH for an easy process <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>.

However, Cursor's "Agent" feature within its composer has significantly improved over recent months <a class="yt-timestamp" data-t="02:02:08">[02:02:08]</a>. The speaker considers it the "most legit agent on the market" <a class="yt-timestamp" data-t="02:02:22">[02:02:22]</a>. This improvement means that external tools like Replit are no longer as necessary for running templates, as Cursor Agent can now run projects locally using GitHub templates <a class="yt-timestamp" data-t="02:02:36">[02:02:36]</a>.

## Getting Started with Cursor AI

The process of starting a new project in Cursor is straightforward and doesn't require leaving the application <a class="yt-timestamp" data-t="03:03:52">[03:03:52]</a>:

1.  **Open a Folder**: Click "Open a folder" within Cursor <a class="yt-timestamp" data-t="04:04:02">[04:04:02]</a>.
2.  **Create a New Folder**: Select a location (e.g., Desktop) and create a new, empty folder for the project <a class="yt-timestamp" data-t="04:04:07">[04:04:07]</a>.
3.  **Open Composer**: Once the blank folder is open, press the appropriate button (often indicated by a plus icon) to open Composer <a class="yt-timestamp" data-t="04:04:24">[04:04:24]</a>.
4.  **Clone a Repository**: Use a command in Composer to clone a GitHub repository and run it locally in one command. For example, using a Next.js template from GitHub (which has over 15,000 uses on Replit) <a class="yt-timestamp" data-t="02:02:54">[02:02:54]</a>.

> [!NOTE] YOLO Mode
> Cursor has a "YOLO mode" feature which automatically confirms commands without requiring repeated "yes" clicks <a class="yt-timestamp" data-t="06:06:49">[06:06:49]</a>. While convenient for experienced users, it's advised to use caution, especially for beginners or when dealing with untrusted code from GitHub <a class="yt-timestamp" data-t="08:08:13">[08:08:13]</a>. Senior developers might prefer not to use it as they may run different commands than Cursor recommends <a class="yt-timestamp" data-t="09:09:09">[09:09:09]</a>.

## Integrating APIs: Building an AI Image Generator

To add AI capabilities, external APIs are often required. The speaker likens [[using_ai_tools_like_cursor_and_claude_for_development | AI coding]] to "Legos," where APIs are the "instruction manuals" that Cursor needs to understand <a class="yt-timestamp" data-t="12:12:02">[12:12:02]</a>.

The example used is [[building_a_healthcarerelated_ai_app | building a simple AI image generator]] using Replicate and the Flux model <a class="yt-timestamp" data-t="13:13:02">[13:13:02]</a>:

1.  **Find Code Examples**: Use a tool like Perplexity to find Next.js code examples for using Flux on Replicate <a class="yt-timestamp" data-t="11:11:09">[11:11:09]</a>. Replicate is a platform that offers many AI models <a class="yt-timestamp" data-t="11:11:27">[11:11:27]</a>. Other useful platforms include Foul <a class="yt-timestamp" data-t="11:11:38">[11:11:38]</a>.
2.  **Provide Instructions and Examples to Cursor**:
    *   Clearly state the goal (e.g., "create a simple AI image generator" <a class="yt-timestamp" data-t="12:12:47">[12:12:47]</a>).
    *   Include the copied code examples, removing any source references if they confuse Cursor <a class="yt-timestamp" data-t="13:13:18">[13:13:18]</a>.
3.  **Include API Key/Token**: Most APIs require an API token because their usage costs money <a class="yt-timestamp" data-t="13:13:29">[13:13:29]</a>. Find the API token on the respective platform (e.g., Replicate) and provide it to Cursor, asking it to place it correctly (often in an `.env` file) <a class="yt-timestamp" data-t="14:14:03">[14:14:03]</a>.

## Debugging and Iteration

Errors are a normal part of the development process <a class="yt-timestamp" data-t="17:17:37">[17:17:37]</a>. When an error occurs, it's crucial to provide Cursor with as much information as possible <a class="yt-timestamp" data-t="21:21:34">[21:21:34]</a>.

*   **Provide Error Messages**: Paste the exact error message into Cursor <a class="yt-timestamp" data-t="17:17:43">[17:17:43]</a>.
*   **Consult API Documentation**: For API-related issues, always refer to the API's official documentation. Copy relevant sections or links into Cursor to provide more context <a class="yt-timestamp" data-t="18:18:15">[18:18:15]</a>.
*   **Use Playgrounds**: Many AI services offer "playgrounds" where you can test models and generate code examples <a class="yt-timestamp" data-t="19:19:12">[19:19:12]</a>. Copying code that worked in a playground provides Cursor with a reliable example <a class="yt-timestamp" data-t="19:19:37">[19:19:37]</a>.
*   **Explain Behavior**: Describe *what* happened, not just that it failed (e.g., "last time it failed immediately, this time it loaded for a little bit and then gave me this fail message" <a class="yt-timestamp" data-t="21:21:20">[21:21:20]</a>). Cursor doesn't see the web view, so it needs explicit details <a class="yt-timestamp" data-t="21:21:45">[21:21:45]</a>.
*   **Restart Server**: Sometimes, after code changes, the local server needs to be restarted (e.g., `npm run dev`) to reflect updates <a class="yt-timestamp" data-t="23:23:28">[23:23:28]</a>.

> [!NOTE] Mindset
> Building apps with AI is often an iterative process and not a "one-shot" solution <a class="yt-timestamp" data-t="23:23:48">[23:23:48]</a>. Expect challenges and embrace the learning that comes from struggling <a class="yt-timestamp" data-t="35:35:39">[35:35:39]</a>. The speaker encourages "sketching" ideas and [[planning_and_preparation_before_using_cursor_ai | building things]] for fun rather than immediately focusing on commercial value <a class="yt-timestamp" data-t="34:34:42">[34:34:42]</a>.

## Adding Features and Design

Once the core functionality is working, enhancements can be added:

*   **User Interface (UI) Information**: Build small UI elements (like info popups or displayed parameters) to make testing and development easier by providing real-time feedback on what the app is doing <a class="yt-timestamp" data-t="26:26:55">[26:26:55]</a>.
*   **Model Selection Toggle**: Implement a toggle or dropdown to allow users to select between different AI models <a class="yt-timestamp" data-t="32:32:48">[32:32:48]</a>. This requires providing Cursor with code examples and documentation for each model <a class="yt-timestamp" data-t="29:29:05">[29:29:05]</a>. For example, Ideogram is an AI image model on Replicate known for handling text well <a class="yt-timestamp" data-t="33:33:24">[33:33:24]</a>.
*   **Design Improvements**: After core features are stable, focus on design. Provide instructions to Cursor to create a more modern interface while ensuring functionality remains unchanged <a class="yt-timestamp" data-t="38:38:03">[38:38:03]</a>. You can even provide examples of interfaces you like <a class="yt-timestamp" data-t="38:38:50">[38:38:50]</a>.

## Implementing Firebase Database

Integrating a database allows for user authentication and data storage (e.g., saving generated images). The template used includes Firebase pre-built <a class="yt-timestamp" data-t="39:39:33">[39:39:33]</a>.

1.  **Request Cursor to Implement**: Prompt Cursor to add user sign-in functionality (e.g., with Google), restrict homepage access for non-signed-in users, and automatically save generated images to storage. Also, request a "My Images" tab to view saved images <a class="yt-timestamp" data-t="42:42:39">[42:42:39]</a>.
2.  **Manual Firebase Setup**:
    *   Go to the Firebase console and create a new project (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="43:43:50">[43:43:50]</a>.
    *   Add a web app to the Firebase project <a class="yt-timestamp" data-t="45:45:17">[45:45:17]</a>.
    *   Copy the Firebase API tokens and paste them into Cursor, instructing it to place them in the correct environment file (e.g., `.env`) <a class="yt-timestamp" data-t="45:45:35">[45:45:35]</a>.
    *   Set up **Firestore Database**: Create a database, starting in test mode for easier development <a class="yt-timestamp" data-t="46:46:39">[46:46:39]</a>.
    *   Set up **Storage**: This is needed for storing images. You might need to upgrade your Firebase project to a paid plan, but you can set a budget limit to prevent unexpected costs <a class="yt-timestamp" data-t="47:47:12">[47:47:12]</a>. Start in test mode <a class="yt-timestamp" data-t="48:48:12">[48:48:12]</a>.
    *   Set up **Authentication**: Enable Google authentication. Local Host is automatically authorized when running locally <a class="yt-timestamp" data-t="48:48:17">[48:48:17]</a>.
3.  **Test and Refine**: After setting up Firebase, test the sign-in and image saving features. If pages or functionalities aren't visible, inform Cursor to make necessary UI adjustments <a class="yt-timestamp" data-t="50:50:53">[50:50:53]</a>.

## Deployment to Vercel

To make the app publicly accessible, deploy it to a platform like Vercel:

1.  **Create GitHub Repository**: Create a new public repository on GitHub for the project <a class="yt-timestamp" data-t="55:55:07">[55:55:07]</a>.
2.  **Instruct Cursor to Deploy**: Tell Cursor Agent to deploy the app to Vercel and commit it to GitHub, providing the GitHub repository link <a class="yt-timestamp" data-t="55:55:57">[55:55:57]</a>.
3.  **Vercel CLI Interaction**: Cursor Agent will likely use the Vercel CLI. Follow the prompts in the terminal:
    *   Sign in to Vercel through the provided link <a class="yt-timestamp" data-t="58:58:28">[58:58:28]</a>.
    *   Confirm setup and deployment <a class="yt-timestamp" data-t="58:58:45">[58:58:45]</a>.
    *   Select personal or business scope <a class="yt-timestamp" data-t="58:58:51">[58:58:51]</a>.
    *   Choose to link to an existing project or create a new one <a class="yt-timestamp" data-t="58:58:56">[58:58:56]</a>.
    *   Provide the project name and confirm the code directory <a class="yt-timestamp" data-t="59:59:03">[59:59:03]</a>.
4.  **Add Environment Variables in Vercel**: After the initial deployment (which might fail if API keys are missing), you need to manually add the Firebase and Replicate API tokens to Vercel's environment variables:
    *   Navigate to your project in the Vercel dashboard.
    *   Go to **Settings** > **Environment Variables** <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.
    *   Add each API key (e.g., `REPLICATE_API_TOKEN`) with its corresponding value <a class="yt-timestamp" data-t="01:05:26">[01:05:26]</a>.
5.  **Redeploy**: Trigger a redeployment in Vercel.
6.  **Authorize Domain in Firebase**: For the deployed app to work with Firebase authentication, you must add the Vercel domain to Firebase's authorized domains list <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>:
    *   In Firebase Console, go to **Authentication** > **Settings** > **Authorized Domains**.
    *   Add the new Vercel domain (e.g., `your-app-name.vercel.app`) <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

The app will then be live on the internet <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a>.

## Resources and Tools Mentioned

*   **Yap Thread** (yapthread.com): An app the speaker built with a composer feature for notes, AI chat, and source management <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>.
*   **Software Composers**: A free community for [[implementing_ai_in_app_development_processes | building AI apps]] and accessing templates <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.
*   **GitHub Template**: A public Next.js template used in the demonstration, available for forking <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>.
*   **Other AI Tools**: Bolt, Vzero, Windsurf, Replit, Lovable (mentioned in [[comparison_of_boltnew_and_cursor_ai | comparison]]) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Perplexity**: An AI tool used to get code examples <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>.
*   **Replicate**: A platform for accessing and running various AI models <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>.
*   **Foul**: Another platform for AI models <a class="yt-timestamp" data-t="01:11:38">[01:11:38]</a>.
*   **Firebase**: Google's platform for backend services, including authentication, Firestore Database, and Storage <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.
*   **Vercel**: A cloud platform for deploying web applications <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.
*   **Instant DB**: An alternative database being used for Yap Thread <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>.
*   **Supabase**: Another open-source database alternative to Firebase <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

The speaker highlights that Cursor's ability to track and restore code history removes much of the manual effort of version control <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>, making it a highly valuable tool for [[best_practices_for_using_cursor_ai | AI-driven app development]] <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.