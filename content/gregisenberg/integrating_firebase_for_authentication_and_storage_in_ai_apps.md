---
title: Integrating Firebase for Authentication and Storage in AI Apps
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

[[building_ai_apps_with_cursor_firebase_and_vercel | Building AI apps with Cursor, Firebase, and Vercel]] often involves integrating a backend database for user management and data storage. Firebase is a popular choice due to its ease of use and comprehensive features <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.

## Why Use Firebase?
Firebase is considered easier to use than alternatives like Supabase, even though some developers prefer Supabase because it's open-source <a class="yt-timestamp" data-t="00:42:28">[00:42:28]</a>. Using Firebase with templates can simplify the setup process significantly <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

### Cost Considerations
Firebase is free to start <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. However, costs can escalate rapidly if your app becomes popular, as your bill will increase <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. For storage, it's possible to set a spending limit to prevent unexpectedly high bills, especially if the app is attacked or overloaded <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.

## Setting Up Firebase with Cursor Agent
The process of [[integrating_ai_with_existing_frameworks | integrating AI with existing frameworks]] and services like Firebase is streamlined when using tools like Cursor Agent.

1.  **Project Creation**:
    *   Begin by asking Cursor Agent to implement Google Firebase <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.
    *   Navigate to the Firebase console and create a new project <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   When creating the project, disable Google Analytics initially to simplify setup <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>. It can be enabled later <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
    *   Register a web app within Firebase <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>. Firebase allows connecting to web, iOS, and Android apps <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.

2.  **API Keys/Tokens**:
    *   Firebase provides API tokens for your web app <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
    *   Copy these API tokens and instruct Cursor to place them in the correct `env` file <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.

3.  **Firestore Database Setup**:
    *   Go to the "Build" section in the Firebase console and select "Firestore Database" <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>.
    *   Create a database and choose "Start in test mode" <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. Test mode has fewer rules, making initial development easier <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>. Production mode is recommended before launching <a class="yt-timestamp" data-t="00:46:59">[00:46:59]</a>.

4.  **Storage Setup**:
    *   If your app handles non-text data like images, you will need Firebase Storage <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>. For text-only apps (e.g., a ChatGPT clone), storage isn't necessary <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.
    *   Within Firebase, go to "Storage" and upgrade your project to enable it <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>.
    *   Start Storage in test mode <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>.
    *   You can set a monthly spending limit (e.g., $20) to control costs <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.

5.  **Authentication Setup**:
    *   Go to "Authentication" in Firebase and click "Get started" <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.
    *   Enable the desired authentication method, such as Google Sign-in <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   Select a support email <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>.
    *   For local development, Firebase automatically authorizes your Local Host <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.
    *   When deploying to a custom domain, you *must* add that domain to the authorized domains list in Firebase Authentication settings <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

### Workflow Example: Image Generator with User Profiles
An example of [[integrating_ai_features_into_mobile_apps | integrating AI features into mobile apps]] is creating an AI image generator that allows users to sign in and save their generated images to a personal database <a class="yt-timestamp" data-t="00:42:38">[00:42:38]</a>.

1.  **User Authentication**:
    *   The app should present a sign-in page if the user is not authenticated <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>.
    *   After signing in, the user can access the image generation features <a class="yt-timestamp" data-t="00:43:22">[00:43:22]</a>.

2.  **Image Storage**:
    *   When an image is generated, it should automatically save to the user's Firebase Storage <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
    *   User-specific data is separated, ensuring each user's generated images are unique to their profile <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>.

3.  **Viewing Saved Images**:
    *   A "My Images" tab or page can be added to display all images generated by the signed-in user <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>. This involves storing image URLs and metadata in the Firestore database <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>.

## Deployment Considerations
When deploying an app with Firebase integration to a platform like Vercel, ensure that all necessary API tokens (e.g., Replicate API token, Firebase API keys) are correctly configured in the deployment environment's variables <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.
Additionally, remember to add the deployed domain to the authorized domains in your Firebase Authentication settings to allow sign-in from the live app <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.