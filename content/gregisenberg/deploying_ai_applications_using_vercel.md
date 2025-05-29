---
title: Deploying AI Applications Using Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

[[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] has become a primary tool for building apps with AI due to its recent features, particularly the Agent within its Composer tool <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. This Agent capability has significantly improved over time, simplifying the process of [[building_ai_apps_with_cursor_firebase_and_vercel | building AI apps]] to the point where external tools like Replit are less necessary for initial development <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. The focus now is on using [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] with GitHub for templates and then [[deploying_ai_applications_using_vercel_and_nextjs | deploying]] to platforms like Vercel <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Setting Up the Local Development Environment

To begin [[building_apps_using_ai_tools_like_claude_and_cursor | building an AI app]] locally with [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]]:

1.  **Open Cursor and Create a Project:** Start by opening [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] and selecting "Open a folder" <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. Create a new, blank folder on your computer to serve as your project directory <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
2.  **Utilize GitHub Templates:** Instead of starting from scratch, leverage existing GitHub repositories as templates. For example, a Next.js template provided has over 15,000 uses on Replit <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
3.  **Clone and Run with Cursor Agent:** Instruct [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] Agent to clone the repository and run it locally in one command. This initiates the project, installs dependencies, and prepares it for live viewing <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>, <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>, <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
    *   *YOLO Mode:* [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] offers a "YOLO mode" which automatically accepts commands without repeated confirmation prompts, accelerating the development process <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>, <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>. However, caution is advised when downloading from untrusted sources <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.
4.  **Local Host Access:** Once running, the application is accessible via a local host URL (e.g., `localhost:3001` or `localhost:3002`), allowing live changes to be observed instantly <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>, <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>, <a class="yt-timestamp" data-t="24:42:00">[24:42:00]</a>.

## Integrating APIs for AI Features

[[using_apis_in_ai_app_development | Using APIs]] is crucial for adding AI functionality to applications. The process involves providing instructions, code examples, and API tokens to [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] <a class="yt-timestamp" data-t="15:29:00">[15:29:00]</a>.

*   **Finding Code Examples:**
    *   **Perplexity:** Can be used to request Next.js code examples for integrating specific AI models or platforms, such as Flux on Replicate <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>, <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
    *   **Replicate:** A platform that offers a wide array of creative AI models <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>, <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. It provides documentation (docs) and a "playground" feature that generates working code examples for integration <a class="yt-timestamp" data-t="18:15:00">[18:15:00]</a>, <a class="yt-timestamp" data-t="19:12:00">[19:12:00]</a>, <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.
*   **API Tokens:** Most APIs require tokens to track usage and manage costs. These tokens need to be securely stored, typically in an `.env` file, and provided to [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] for correct integration <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>, <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>, <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.
*   **Debugging:** Errors are common. When an API call fails, provide the error message and additional documentation or playground examples to [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] for it to diagnose and fix the issue <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>, <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>. It's important to give [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] full context, including what you see in the web view <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>.

## Adding Advanced Features and Design

Once core AI functionality is established, further enhancements can be made:

*   **User Interface (UI) Design:** After getting the core features working, focus on design <a class="yt-timestamp" data-t="38:03:00">[38:03:00]</a>. Instruct [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] to modernize the interface while maintaining functionality <a class="yt-timestamp" data-t="38:16:00">[38:16:00]</a>.
*   **Model Selection:** Implement a toggle or selection mechanism for users to choose between different AI models (e.g., various image generation models like Flux Pro, Ideogram) <a class="yt-timestamp" data-t="32:48:00">[32:48:00]</a>.
*   **Database Integration with Firebase:**
    *   Firebase is a user-friendly database solution, easier to use than alternatives like Supabase <a class="yt-timestamp" data-t="44:25:00">[44:25:00]</a>.
    *   **Setup:** Create a new project in the Firebase console, enable Firestore Database, Storage (if storing images), and Authentication (e.g., Google Sign-in) <a class="yt-timestamp" data-t="43:50:00">[43:50:00]</a>, <a class="yt-timestamp" data-t="46:35:00">[46:35:00]</a>, <a class="yt-timestamp" data-t="47:12:00">[47:12:00]</a>, <a class="yt-timestamp" data-t="48:25:00">[48:25:00]</a>.
    *   **Firebase API Keys:** Provide Firebase API keys to [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] to connect the app to the database <a class="yt-timestamp" data-t="45:35:00">[45:35:00]</a>.
    *   **User Authentication & Storage:** Implement features allowing users to sign in (e.g., with Google) and automatically save generated content (like images) to their personal storage within the database <a class="yt-timestamp" data-t="43:22:00">[43:22:00]</a>, <a class="yt-timestamp" data-t="43:27:00">[43:27:00]</a>. Add a "My Images" tab to display saved items <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>.

## [[deploying_ai_applications_using_vercel_and_nextjs | Deploying to Vercel]]

[[deploying_ai_applications_using_vercel_and_nextjs | Deploying the AI app]] to a platform like Vercel makes it accessible online <a class="yt-timestamp" data-t="53:03:00">[53:03:03]</a>.

1.  **GitHub Repository:** Create a new public repository on GitHub <a class="yt-timestamp" data-t="55:10:00">[55:10:00]</a>. [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] Agent might even be able to create the repository directly <a class="yt-timestamp" data-t="57:08:00">[57:08:00]</a>.
2.  **Instruct Cursor for Vercel Deployment:** Provide [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] with the GitHub repo link and instruct it to deploy the app to Vercel <a class="yt-timestamp" data-t="56:01:00">[56:01:00]</a>, <a class="yt-timestamp" data-t="56:13:00">[56:13:00]</a>.
3.  **Vercel CLI and Login:** [[building_apps_using_ai_tools_like_claude_and_cursor | Cursor]] can use the Vercel CLI. It will prompt for login, which can be done with one click <a class="yt-timestamp" data-t="58:16:00">[58:16:00]</a>, <a class="yt-timestamp" data-t="58:28:00">[58:28:00]</a>.
4.  **Project Setup on Vercel:** Follow the prompts to set up the project on Vercel, linking it to the GitHub repository and specifying the project name <a class="yt-timestamp" data-t="58:45:00">[58:45:00]</a>.
5.  **Environment Variables on Vercel:** A common cause of deployment failure is missing API keys. You need to manually add your API tokens (e.g., Replicate, Firebase) as environment variables within the Vercel project settings <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>, <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>, <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
6.  **Redeploy:** After adding environment variables, redeploy the project from the Vercel dashboard <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.
7.  **Authorize Domains in Firebase:** For a [[building_ai_apps_with_cursor_firebase_and_vercel | Firebase-integrated app]] deployed on Vercel, the new Vercel domain needs to be added to Firebase's authorized domains list under Authentication settings <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>.

With these steps, the AI application becomes a fully functional, publicly accessible web app <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>.

> [!NOTE]
> Building applications with AI tools is an iterative process. It's often not a "one-shot" success and requires persistence through errors and adjustments <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>, <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>. This iterative approach fosters learning and is considered more enjoyable than instant solutions <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.

### Related Topics
*   [[building_ai_apps_with_cursor_firebase_and_vercel | Building AI Apps with Cursor, Firebase, and Vercel]]
*   [[using_apis_in_ai_app_development | Using APIs in AI App Development]]
*   [[building_apps_using_ai_tools_like_claude_and_cursor | Building apps using AI tools like Claude and Cursor]]