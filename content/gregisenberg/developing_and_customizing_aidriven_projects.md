---
title: Developing and customizing AIdriven projects
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

Developing and customizing AI-driven projects, particularly applications, has become more accessible with advanced AI coding tools. This guide outlines a practical approach using Cursor, focusing on its `Agent` feature for efficient development and deployment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Core Tools and Workflow

Initially, the workflow for building apps with AI involved using VZ for front-end development, then importing into Cursor, and utilizing Replit for live web view and deployment <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Replit was favored for its ease of use with templates and deployment <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, a significant shift occurred with Cursor's `Agent` feature <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The updated workflow primarily involves:
*   **Cursor with `Agent`:** This is considered a highly legitimate agent on the market for coding tasks <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **GitHub:** Used for storing and accessing code templates, replacing the need for Replit for templates <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Setting Up a Project Locally

To start an [[AIdriven app features and development | app development]] project locally with Cursor and GitHub:
1.  **Open Cursor:** Hit "open a folder" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  **Create a New Folder:** Choose a temporary location (e.g., desktop) and create a new, empty folder (e.g., "Riley Greg Pod 4") <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
3.  **Open Composer:** Access Cursor's composer feature from the blank folder <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
4.  **Clone and Run Repository:** Use a single command within Cursor to clone a GitHub repository (e.g., a Next.js template) and run it locally <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This step handles cloning the project and installing dependencies <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### YOLO Mode

Cursor offers a "YOLO mode" feature that automatically confirms commands without requiring repeated "yes" clicks <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. While convenient for experienced users, it is advised to use caution, especially when downloading or cloning from untrusted sources, as the user is responsible for vetting the code <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. For non-technical users, it can be easier to let Cursor take control <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Integrating AI Features with APIs

AI tools often rely on APIs (Application Programming Interfaces) to function <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. APIs have different coding rules, and Cursor needs examples to understand how to integrate them <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### Steps for API Integration

1.  **Instructions:** Provide Cursor with clear instructions on the desired functionality (e.g., "create a simple AI image generator") <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
2.  **Examples:** Obtain relevant code examples. Platforms like [[AIdriven coding platforms | Perplexity]] can provide Next.js code examples for specific AI models on services like Replicate <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Replicate is beneficial for accessing a wide range of creative and general AI models <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
3.  **API Token:** Most APIs require an API token for access, as using the models incurs costs (e.g., image generation might cost cents per piece) <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. This token helps track usage. These tokens should be placed in the `env.local` file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

### Debugging and Iteration

It is common to encounter errors during development. When an API integration fails, it's crucial to provide Cursor with:
*   The specific error message <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   Additional documentation (e.g., from the API provider's documentation) <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   Examples from API playgrounds, which simulate the desired functionality and provide working code examples <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

Communicating all observations to Cursor, including visual aspects from the web view (which Cursor doesn't inherently see yet), is vital for effective debugging <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

## Customizing and Enhancing the Application

Once core functionality is established, focus can shift to customization and design.
*   **Design First, Functionality Second (in this context):** It's often recommended to get the core feature working first, then apply design elements <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
*   **UI Enhancements:** Examples include adding a top bar title (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="00:38:22">[00:38:22]</a>, improving button aesthetics, and creating user interface (UI) info pop-ups to display parameters or models used <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   **Model Toggling:** Implement options to switch between different AI models (e.g., Flux Pro, Ideogram), understanding that each model may operate differently <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. Ideogram is noted for its ability to add text to images <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.

## Database Integration with Firebase

For applications that need to store user data, like generated images, integrating a database is essential. Firebase is a popular choice for its ease of use <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

### Firebase Setup Steps:
1.  **Create a Project:** Go to the Firebase console and create a new project <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
2.  **Web App Integration:** Register a web app to obtain API tokens <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>. These tokens are then pasted into Cursor's `env.local` file <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.
3.  **Firestore Database:** Enable and create a Firestore database, starting in test mode for easier development <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>.
4.  **Storage:** Enable storage (e.g., for images), and consider setting a spending limit to prevent unexpected costs <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.
5.  **Authentication:** Enable Google authentication for user sign-in <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. Firebase automatically sets up authentication for local hosts <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
6.  **Functionality:** Implement user sign-in to restrict homepage access to authenticated users and automatically save generated images to their storage <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. Add a "My Images" tab to view saved content <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

## Deployment to the Internet

Deploying an application makes it accessible to a wider audience. Vercel is a platform often used for this purpose.

### Deployment Steps:
1.  **GitHub Repository:** Create a new GitHub repository for the project <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>.
2.  **Deploy with Cursor Agent:** Instruct Cursor Agent to deploy the app to Vercel <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Cursor may even create the GitHub repository automatically <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
3.  **Vercel Configuration:** Sign in to Vercel via CLI, link the project, and confirm deployment settings <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>.
4.  **Environment Variables:** Crucially, API keys and other environment variables must be added to Vercel's project settings under "Environment Variables" <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
5.  **Authorize Domains:** In Firebase, add the Vercel deployment domain to the authorized domains list under authentication settings to allow sign-in on the live app <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.
6.  **Redeploy:** After adding environment variables and authorizing domains, redeploy the project on Vercel to apply changes <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.

## Mindset for AI-Driven Development

Developing with AI tools like Cursor requires a specific mindset:
*   **Embrace Iteration:** Building apps is an iterative process, not a one-shot solution <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Expect Challenges:** It's a "mountain to go uphill on," not a flat journey <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>. Learning is maximized during struggles <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.
*   **Provide Context:** Give AI tools as much correct and detailed information as possible <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Start Simple:** Begin with projects for fun or learning ("sketching") rather than immediately aiming for commercially valuable apps <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>.

## Related Resources

*   [[AIdriven startup ideas | Startup Empire]]: A private membership for individuals looking to build out [[AIdriven startup ideas | startup ideas]], offering content, potential co-founders, and tutorials on [[transition_from_traditional_to_aidriven_marketing_workflows | marketing]], audience building, and more <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   Yap Thread ([app.yapthread.com](https://app.yapthread.com)): A newly developed writing tool that includes features like saving notes, chatting with AI, and AI-powered composition from bookmarks/sources <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>.
*   Software Composers: A free community with over 10,000 members where individuals discuss building [[AIdriven app features and development | AI apps]] and access templates <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.