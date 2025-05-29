---
title: Deploying Apps Using Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

Vercel serves as a deployment platform for web applications, offering features that simplify the process of getting applications live on the internet <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>. It is particularly useful for [[deployment_of_nextjs_apps_with_versel | Next.js projects]] <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>.

## Evolution of Deployment Tools

Initially, tools like Replit were favored for their ease of use in templates and deployment, providing an easy web view to see live changes <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>, <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. Developers would connect Cursor to Replit and sync codebases via SSH <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. However, with the advancements in Cursor's Agent feature, directly using GitHub for templates and then deploying with Vercel has become the preferred method <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>, <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. The speaker acknowledges that while Replit is still a good tool, they recently moved to Vercel <a class="yt-timestamp" data-t="01:06:35">[01:06:35]</a>, <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>.

## The Deployment Process with Cursor Agent and Vercel

The full process for deploying an application using Cursor Agent and Vercel, starting from a local setup, includes:

1.  **Setting up the GitHub Repository**
    *   Create a new public repository on GitHub <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>, <a class="yt-timestamp" data-t="00:55:15">[00:55:15]</a>.
    *   Copy the repository link <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>.
    *   In Cursor, instruct the Agent to "deploy this app to Vercel and commit it to GitHub" while pasting the repo link <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Cursor Agent can often create the repository itself, making the GitHub creation step potentially unnecessary <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>, <a class="yt-timestamp" data-t="00:57:11">[00:57:11]</a>.

2.  **Initiating Deployment via Vercel CLI**
    *   Cursor Agent will use the Vercel CLI to deploy <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
    *   This may require signing in to Vercel via a prompted link <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>.
    *   Confirm deployment settings like linking to an existing project (usually "no" for a new deployment) and project name <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>, <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>.
    *   Specify the directory where the code is located (often by pressing enter) <a class="yt-timestamp" data-t="00:59:15">[00:59:15]</a>.

3.  **Handling Environment Variables/API Tokens**
    *   A common issue during deployment is the failure to load environment variables, particularly API tokens <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>, <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>.
    *   To fix this, navigate to your Vercel project settings, then "Environment Variables," and add the necessary key-value pairs (e.g., `REPLICATE_API_TOKEN`) <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>, <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
    *   After adding variables, trigger a redeployment <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>, <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.

4.  **Firebase Domain Authorization**
    *   For applications integrated with [[building_ai_apps_with_cursor_firebase_and_vercel | Firebase]] (e.g., for authentication), the deployed Vercel domain needs to be authorized in your Firebase project settings <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.
    *   Go to Firebase console, navigate to "Authentication," "Settings," "Authorized domains," and add the Vercel domain <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>, <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>.

### Benefits of Deploying with Vercel

*   **Automatic Deployment**: Vercel can be configured to deploy every branch push automatically from your GitHub repository <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>.
*   **Live Updates**: Similar to [[using_vercels_v0_for_web_development | Vercel's v0]], Vercel allows you to see changes live as you develop, which is beneficial for iterative building <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>, <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.

### Challenges and Tips

*   **Debugging Deployment Failures**: It's common to encounter errors during deployment. The process involves identifying the issue (e.g., missing API tokens, incorrect configuration), providing additional context or documentation to Cursor Agent, and iteratively fixing <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.
*   **API Key Management**: Be diligent about managing API keys and environment variables, especially when sharing screens or code, to prevent unauthorized usage <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>, <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.
*   **Custom Domains**: Vercel makes it super easy to add custom domains by entering settings and pasting code from your domain provider (e.g., Namecheap) <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>, <a class="yt-timestamp" data-t="00:59:58">[00:59:58]</a>.

## Integration with Firebase

The deployment process often involves integrating with [[building_ai_apps_with_cursor_firebase_and_vercel | Firebase]] for backend services like authentication and storage. This requires manual setup in the Firebase console:
*   Creating a Firebase project <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>, <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>.
*   Connecting to a web app <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
*   Configuring Firestore Database for data storage <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>, <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.
*   Setting up Storage for assets like images <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>, <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>. It's advisable to set a spending limit to prevent unexpected charges <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>, <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>.
*   Enabling Google Authentication to allow user sign-ins <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>, <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>. Localhost is automatically authorized for development <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
*   Provide Firebase API tokens to Vercel's environment variables for the deployed app to access Firebase services <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>, <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.

This end-to-end process, from app generation to full stack deployment on Vercel, can be completed in about an hour and fifteen minutes <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.