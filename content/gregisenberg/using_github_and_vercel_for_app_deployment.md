---
title: Using GitHub and Vercel for App Deployment
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article outlines the process of deploying applications using [[github_and_codex_integration | GitHub]] for code management and [[overview_of_vercel_and_vz | Vercel]] for hosting, primarily leveraging Cursor's Agent feature for automation.

## Evolution of Deployment Workflow

Initially, the preferred tools for app development and deployment included VZ for front-end, Cursor for coding, and [[deployment_and_cloud_integration_with_replit | Replit]] for live web views and simplified [[code_deployment_and_integration_with_tools | deployment]] <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>, <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>, <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. [[deployment_and_cloud_integration_with_replit | Replit]] was favored for its easy-to-use templates, straightforward [[code_deployment_and_integration_with_tools | deployment]], and live web view <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

With the release and significant improvements of Cursor Agent, the workflow has shifted. Now, instead of integrating Cursor with [[deployment_and_cloud_integration_with_replit | Replit]], the process can be streamlined by solely using [[github_and_codex_integration | GitHub]] for templates, with Cursor Agent handling local execution and [[code_deployment_and_integration_with_tools | deployment]] <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>, <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. A Next.js template maintained by the speaker has over 15,000 uses on [[deployment_of_nextjs_applications | Replit]], now primarily leveraged through [[github_and_codex_integration | GitHub]] <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Deployment Process with Cursor Agent, GitHub, and Vercel

The following steps outline how to deploy an app using this integrated approach:

### 1. Initialize Project in Cursor
*   Open Cursor and select "Open a folder" <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   Create a new, empty folder on your computer (e.g., on the desktop) for the project <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   Open this new folder within Cursor <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
*   Access the Composer within Cursor by pressing the designated button <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

### 2. Clone GitHub Repository and Run Locally
*   Provide a prompt to Cursor Agent to clone a [[github_and_codex_integration | GitHub]] repository and run it locally <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>, <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. This can be done with a single command <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.
*   Cursor Agent will identify it as a [[deployment_of_nextjs_applications | Next.js]] project, clone it, and install dependencies <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
*   The application will start running on a local host (e.g., `localhost:3001` or `localhost:3002`) <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>, <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   The files from the repository will be loaded into your local project folder in Cursor <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

### 3. Commit to GitHub
*   Create a new repository on [[github_and_codex_integration | GitHub]] <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   Instruct Cursor Agent to commit the app to the newly created [[github_and_codex_integration | GitHub]] repository <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>, <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.
*   **Note:** Cursor Agent can automatically create the [[github_and_codex_integration | GitHub]] repository, making manual creation unnecessary <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.

### 4. Deploy to Vercel
*   After the project is committed to [[github_and_codex_integration | GitHub]], instruct Cursor Agent to deploy the app to [[overview_of_vercel_and_vz | Vercel]] <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>, <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   Cursor Agent will use the [[overview_of_vercel_and_vz | Vercel]] CLI (Command Line Interface) for deployment, prompting you to log in if not already <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>, <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   During the [[code_deployment_and_integration_with_tools | deployment]] process, you will be asked to:
    *   Select whether to deploy on your personal or business account <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
    *   Specify if it should link to an existing project (typically 'no' if it's a new [[overview_of_vercel_and_vz | Vercel]] project) <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
    *   Provide a project name (e.g., "Riley Greg Pod 4") <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
    *   Confirm the code directory <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
    *   Confirm settings <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
*   The [[code_deployment_and_integration_with_tools | deployment]] will begin, and you can monitor its build status on the [[overview_of_vercel_and_vz | Vercel]] dashboard <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.

### 5. Managing Environment Variables in Vercel
*   If the [[code_deployment_and_integration_with_tools | deployment]] fails due to missing API tokens (e.g., Replicate API token), you'll need to add them manually in [[overview_of_vercel_and_vz | Vercel]] <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   Navigate to your project in [[overview_of_vercel_and_vz | Vercel]]:
    *   Go to "Projects" <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
    *   Click on your project name <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
    *   Go to "Settings" <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
    *   Select "Environment Variables" <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
    *   Add your API keys (e.g., `REPLICATE_API_TOKEN`) with their corresponding values <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>, <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>, <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   After adding the variables, trigger a redeploy from the [[overview_of_vercel_and_vz | Vercel]] dashboard <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>, <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### 6. Authorize Domain in Firebase (if applicable)
*   If your app uses Firebase for authentication (e.g., Google sign-in), you must authorize the [[overview_of_vercel_and_vz | Vercel]] domain in your Firebase project <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.
*   In Firebase Console:
    *   Go to "Authentication" <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>, <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
    *   Navigate to "Settings" <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
    *   Add the [[overview_of_vercel_and_vz | Vercel]] domain (e.g., `your-app-name.vercel.app`) to the "Authorized domains" list <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>, <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.

Once these steps are completed, your application will be successfully deployed to the internet on a [[overview_of_vercel_and_vz | Vercel]] domain <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>, <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. You can also set up a custom domain through [[overview_of_vercel_and_vz | Vercel]] settings by pasting in the code from your domain registrar <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>, <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.