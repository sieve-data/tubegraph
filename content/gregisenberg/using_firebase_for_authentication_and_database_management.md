---
title: Using Firebase for Authentication and Database Management
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details the process of integrating [[googles_ecosystem_and_firebase_integration | Firebase]] into an application, focusing on authentication and database management. The demonstration primarily uses Cursor Agent for building an AI image generator app locally, then deploying it to the internet, leveraging [[integration_with_firebase_for_realtime_applications | Firebase]]'s capabilities.

## Why Integrate Firebase?
[[integration_with_firebase_for_realtime_applications | Firebase]] provides a robust backend solution for applications, offering services like user authentication and data storage. Templates used in this demonstration come pre-configured with [[googles_ecosystem_and_firebase_integration | Firebase]] integration, simplifying the setup process for developers [00:39:52](<a class="yt-timestamp" data-t="00:39:52">[00:39:52]</a>.

## Setting Up Firebase
Integrating [[googles_ecosystem_and_firebase_integration | Firebase]] requires some manual steps within the [[googles_ecosystem_and_firebase_integration | Firebase]] console [00:43:50](<a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

1.  **Create a Project**:
    *   Navigate to the [[googles_ecosystem_and_firebase_integration | Firebase]] console [00:43:57](<a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.
    *   Create a new project (e.g., "Mount Cursor") [00:44:38](<a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>.
    *   Disable Google Analytics initially for simplicity, as it can be set up later [00:44:44](<a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.

2.  **Register a Web App**:
    *   Within your [[googles_ecosystem_and_firebase_integration | Firebase]] project, register a web app [00:45:11](<a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.
    *   Name the web app (e.g., "Mount web app") [00:45:17](<a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
    *   Copy the provided API tokens, which are essential for connecting your application to [[googles_ecosystem_and_firebase_integration | Firebase]] services [00:45:30](<a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>. These tokens should be placed in your project's `.env` file [00:45:44](<a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.

### Database Setup: Firestore
Firestore is used for storing basic user information, while image data requires separate storage [00:46:02](<a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.

1.  **Create Database**:
    *   Navigate to the "Build" section in the [[googles_ecosystem_and_firebase_integration | Firebase]] console and select "Firestore Database" [00:46:36](<a class="yt-timestamp" data-t="00:46:36">[00:46:36]</a>.
    *   Click "Create database" and select "Start in test mode" for easier development [00:46:48](<a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>. Test mode offers fewer rules, which is beneficial during the initial development phase [00:46:53](<a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.

### Storage Setup
Storage is necessary when your app handles files like images [00:46:14](<a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.

1.  **Upgrade Project**:
    *   Go to the "Storage" section in [[googles_ecosystem_and_firebase_integration | Firebase]] [00:47:12](<a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.
    *   You'll need to upgrade your project to a paid plan, even though it's free to start. This allows setting a spending limit (e.g., $20) to prevent unexpected charges, especially from potential attacks [00:47:21](<a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.
    *   Start in test mode for development purposes [00:48:17](<a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.

### Authentication Setup
[[googles_ecosystem_and_firebase_integration | Firebase]] authentication handles user sign-in processes.

1.  **Enable Google Sign-in**:
    *   Go to the "Authentication" section and click "Get started" [00:48:20](<a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.
    *   Enable the Google sign-in provider [00:48:42](<a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   Select your support email and save [00:48:49](<a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>. Localhost is automatically authorized for development [00:48:25](<a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

## Integrating Firebase with the Application
The application is pre-configured with [[integration_with_firebase_for_realtime_applications | Firebase]] authentication and storage. The goal is to allow users to sign in with Google, see a sign-in page if not authenticated, and save generated images to their storage. A "My Images" tab should display all generated images [00:42:49](<a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.

1.  **User Authentication Flow**:
    *   The app redirects to a sign-in page if the user is not authenticated [00:43:16](<a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>.
    *   Upon successful Google sign-in, the user is redirected to the main app interface where they can generate images [00:43:22](<a class="yt-timestamp" data-t="00:43:22">[00:43:22]</a>.

2.  **Saving Images to Storage**:
    *   After an image is generated, it is automatically saved to the user's [[googles_ecosystem_and_firebase_integration | Firebase]] storage [00:43:27](<a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
    *   The user's generated images are displayed on a dedicated "My Images" tab [00:43:37](<a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

## Deployment to the Internet
To make the application publicly accessible, it needs to be deployed. This process involves using GitHub and Vercel.

1.  **GitHub Repository**:
    *   A new public GitHub repository is created for the project (e.g., "Mount cursor") [00:55:10](<a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.
    *   Cursor Agent can automatically create and commit the project to GitHub [00:57:08](<a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.

2.  **Deploying with Vercel**:
    *   Vercel is used for deployment, which can be mostly managed through Cursor Agent [00:55:46](<a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.
    *   Link Vercel to your GitHub account [00:58:33](<a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>.
    *   Initiate deployment, selecting personal or business account, and linking to the project (e.g., "Riley Greg pod 4") [00:58:51](<a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
    *   Crucially, [[googles_ecosystem_and_firebase_integration | Firebase]] API keys must be added as environment variables in Vercel's project settings under "Environment Variables" [01:05:12](<a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
    *   After adding the keys, redeploy the project [01:07:04](<a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.

3.  **Authorizing Domain in Firebase**:
    *   For the deployed app to authenticate users, its domain must be authorized in [[googles_ecosystem_and_firebase_integration | Firebase]] [01:09:03](<a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>.
    *   Go to [[googles_ecosystem_and_firebase_integration | Firebase]] Authentication settings, add the Vercel domain to "Authorized domains" [01:09:43](<a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.
    *   Once authorized, the deployed app will allow user sign-ins and save data [01:10:04](<a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

## Conclusion
This process demonstrates [[building_an_ai_app_with_cursor_and_firebase | building an AI app with Cursor and Firebase]], covering initial setup, authentication, database storage, and deployment. The iterative nature of [[development_and_troubleshooting_in_app_creation | development and troubleshooting in app creation]] and using powerful AI tools like Cursor Agent significantly streamlines the process. [[googles_ecosystem_and_firebase_integration | Firebase]] is noted for its ease of use compared to alternatives like [[implementing_leaderboards_and_databases_with_superbase | Supabase]] [00:44:25](<a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

> [!NOTE] Firebase Cost Model
> [[googles_ecosystem_and_firebase_integration | Firebase]] is free to start, but costs increase as your app gains popularity and usage [00:44:03](<a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. Implementing spending limits is crucial for managing potential costs and preventing unexpected charges [00:47:30](<a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>.