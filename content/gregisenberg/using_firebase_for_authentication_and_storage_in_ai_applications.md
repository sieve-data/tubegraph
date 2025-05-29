---
title: Using Firebase for authentication and storage in AI applications
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

Firebase provides an easy-to-use backend service for applications, particularly useful for managing user authentication and storing data in AI-powered tools. It operates on a cost model that is free to start, with costs increasing only as the app gains popularity and usage <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. Its ease of use is often preferred over alternatives like Supabase, even though Supabase is open-source <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

## Setting Up a Firebase Project

To begin using Firebase for your application:

1.  **Create a Project**: Navigate to the Firebase console and initiate a new project <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. It's recommended to skip enabling Google Analytics during the initial setup to simplify the process; it can always be added later <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
2.  **Connect Your App**: After project creation, connect it as a web application <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>. Firebase also supports connecting iOS and Android applications to the same database <a class="yt-timestamp" data-t="00:45:23">[00:45:23]</a>.
3.  **Obtain API Keys**: Firebase will provide necessary API tokens. These keys should be copied and placed in the `.env` file of your project for secure access <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.

## Key Firebase Services for AI Apps

Firebase offers several services vital for developing AI applications:

### Firestore Database

Firestore is a NoSQL cloud database used for storing basic information, such as user data <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.
*   **Initial Setup**: When creating the database, start in "test mode." This simplifies development by reducing the number of stringent rules, which can prevent annoying errors. Rules can be adjusted to "production mode" before launch <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.

### Storage

Firebase Storage is crucial for apps that handle non-textual data, such as images.
*   **Purpose**: If your application generates or processes images, like an AI image generator, Firebase Storage is required to save these outputs <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>. For text-only applications, such as a ChatGPT clone, storage might not be necessary <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.
*   **Security and Limits**: Activating storage typically requires upgrading your project. It's highly recommended to set a budget limit to prevent potential overload attacks or unexpected high costs, capping potential expenses (e.g., at $20) <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.

### Authentication

Firebase Authentication provides secure user sign-in methods, such as Google Sign-In <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>.
*   **Localhost Compatibility**: A significant advantage of [[Firebase Studios features and limitations | Firebase Studio]] is its automatic setup to authenticate requests from `localhost`, eliminating the need to manually authorize development domains, which was often required with tools like Replit <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
*   **Domain Authorization**: For deployed applications, the deployed domain (e.g., `vercel.app`) must be added to the "authorized domains" list within Firebase Authentication settings <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

## Integration with AI Tools

Using a template pre-configured with Firebase can significantly streamline the setup process for authentication and storage <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>. Once the template is running locally and Firebase is configured, the application can:
*   Automatically save generated images to Firebase Storage upon creation <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
*   Require users to sign in before accessing the core functionality (e.g., image generation) <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>.
*   Display user-specific content (e.g., "My Images" tab showing previously generated images) <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

This integration allows for robust [[building_and_deploying_apps_with_ai_integration | building and deploying apps with AI integration]] that manage user data and generated content effectively.