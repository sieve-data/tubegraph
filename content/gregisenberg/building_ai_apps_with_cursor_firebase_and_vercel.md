---
title: Building AI Apps with Cursor Firebase and Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article details a streamlined process for building AI applications using [[using_cursor_ai_effectively | Cursor]], integrating [[integrating_firebase_for_authentication_and_storage_in_ai_apps | Firebase]] for authentication and storage, and deploying with [[deploying_ai_applications_using_vercel | Vercel]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The shift to primarily using [[using_cursor_ai_effectively | Cursor]] is attributed to its enhanced features, particularly the Agent composer <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Transition to Cursor AI
Initially, a workflow involved [[leveraging_ai_tools_like_v0_cursor_ai_and_replit | v0]] for front-end development, then importing into [[using_cursor_ai_effectively | Cursor]], and finally using [[leveraging_ai_tools_like_v0_cursor_ai_and_replit | Replit]] for live web view and easy deployment <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. [[leveraging_ai_tools_like_v0_cursor_ai_and_replit | Replit]] was favored for its easy templates and deployment compared to other platforms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

However, [[using_cursor_ai_effectively | Cursor]] released a new feature within Composer called "Agent" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. While the Agent wasn't initially strong, significant improvements over a month and a half have made it highly effective, eliminating the need for [[leveraging_ai_tools_like_v0_cursor_ai_and_replit | Replit]] for running local templates <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Now, a simple GitHub template and telling [[using_cursor_ai_effectively | Cursor]] to run it locally is sufficient <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Setting Up the Development Environment
To begin, open [[using_cursor_ai_effectively | Cursor]] and select "open a folder" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Create a new, blank folder on your computer (e.g., "Riley Greg Pod 4") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Once opened, you can access the [[using_cursor_ai_effectively | Cursor]] Composer <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

A key command used is: "clone the repo and run it locally in one command" with a provided GitHub link to a Next.js template <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### YOLO Mode
[[using_cursor_ai_effectively | Cursor]] offers a "YOLO mode" that automatically executes commands without needing repeated confirmations <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. While convenient for ease of use, it's recommended to only use it with trusted sources from GitHub <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Building an AI Image Generator
The process for building the image generator involves using an existing Next.js template and leveraging [[using_cursor_ai_effectively | Cursor]] Agent.

### Leveraging APIs with AI Tools
When integrating APIs, the general approach is to provide instructions, examples, and your API token <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
1.  **Instructions**: Clearly state what you want the AI to build (e.g., "create a simple AI image generator") <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
2.  **Examples**: Provide code examples for using the API. For an AI image model like Flux on Replicate, you can ask Perplexity for Next.js code examples <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Replicate and Fal.ai are platforms that simplify the use of AI models <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. API playgrounds are also useful for generating working code examples <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
3.  **API Token**: Most APIs require a token because their usage costs money <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. [[using_cursor_ai_effectively | Cursor]] can place this token in the correct `.env.local` file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

### Iterative Development and Troubleshooting
Errors are common and part of the development process <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. When an error occurs, paste the error message back into [[using_cursor_ai_effectively | Cursor]] and provide additional context or documentation, such as the API's official documentation <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. The Agent can read the provided links and process the information <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.

> "I've noticed that people who use these tools are getting lazier and they're expecting cursor to just like do everything for them when they're not even explaining to cursor everything that's going on like it you need cursor doesn't see this my prediction is by the end of the year it will but um cursor doesn't see your web View and so you need to give it all of the information that you see and the more correct information you give it the better" <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>

### Enhancing Features
Once the core functionality is established, additional features can be added:
*   **Model Toggles**: Implement a toggle to switch between different AI models (e.g., original Stability AI, Flux Pro, Ideogram) <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. Ideogram is noted for its ability to add text to images <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
*   **Generation Details Pop-up**: Add a user interface element (e.g., an info icon bubble) that, when clicked, displays the model used and all parameters of the generated image <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This helps in testing and understanding model performance <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **Design Improvements**: After core features, enhance the app's design to make the interface more modern <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.

## Integrating Firebase for Authentication and Storage
The Next.js template used comes preconfigured with Firebase authentication and storage <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

### Manual Firebase Setup Steps
1.  **Create a Firebase Project**: Go to the Firebase console and create a new project (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. Do not enable Google Analytics initially <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
2.  **Register a Web App**: Register a web app within your Firebase project <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>. Copy the provided Firebase API tokens and paste them into [[using_cursor_ai_effectively | Cursor]] (e.g., in the `.env` file) <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
3.  **Firestore Database**: In the Firebase console, go to "Build" -> "Firestore Database" and click "Create database" <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>. Start in "test mode" for easier development <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.
4.  **Storage**: Go to "Storage" in the Firebase console <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>. This is needed for storing images; text-only apps may not require it <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>. It's recommended to set a spending limit (e.g., $20) to prevent unexpected charges <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.
5.  **Authentication**: Go to "Authentication" in the Firebase console, click "Get started", and enable Google as a sign-in provider <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. Localhost is automatically authorized for development <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

After setup, instruct [[using_cursor_ai_effectively | Cursor]] to implement the following:
*   Users must sign in to see the homepage <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
*   Generated images should automatically save to the user's storage <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
*   A "My Images" tab in the top bar should lead to a page displaying all generated images <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

## Deploying the Application with Vercel
[[deploying_ai_applications_using_vercel | Vercel]] is used for deployment, with [[using_cursor_ai_effectively | Cursor]] Agent handling most of the work <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.

1.  **Create GitHub Repository**: Create a new public repository on GitHub (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.
2.  **Deploy Command**: Instruct [[using_ai_tools_like_cursor_ai_and_vzer_for_app_and_content_development | Cursor]] Agent: "I created this new GitHub repo and I want you to deploy this app to [[deploying_ai_applications_using_vercel | Vercel]] and save it to GitHub" <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
3.  **Vercel CLI Interaction**: The Agent will likely prompt for [[deploying_ai_applications_using_vercel | Vercel]] CLI authentication. Log in via the provided link <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>. Answer prompts like "set up and deploy" (yes), link to existing project (no), project name, and directory <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>.
4.  **Environment Variables in Vercel**: If deployment fails due to missing API keys, navigate to your project in the [[deploying_ai_applications_using_vercel | Vercel]] dashboard -> "Settings" -> "Environment Variables" <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>. Add the necessary `REPLICATE_API_TOKEN` and Firebase API keys <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
5.  **Redeploy**: After adding variables, redeploy the project in [[deploying_ai_applications_using_vercel | Vercel]] <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.
6.  **Authorize Domain in Firebase**: For the deployed app to function, add its [[deploying_ai_applications_using_vercel | Vercel]] domain (e.g., `rileygregpod4.vercel.app`) to the "Authorized domains" list under "Authentication" -> "Settings" in the Firebase console <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>.

## Mindset for AI App Development
*   **Iterative Process**: Development with AI tools is rarely a "one-shot" <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>. Expect to struggle and iterate, as this is where the most learning occurs <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.
*   **Context is Key**: Provide AI tools with as much correct and detailed information as possible, including errors and additional documentation <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.
*   **Sketching Ideas**: Focus on "sketching out ideas live" rather than solely building commercially valuable products initially <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>. This approach makes the process more enjoyable and fosters learning <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   **Embrace Difficulty**: Approach AI development with the mindset that it will be difficult, an "uphill mountain," not a flat journey <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.

The entire process of building an AI image generator with three models, Firebase integration, and [[deploying_ai_applications_using_vercel | Vercel]] deployment can be achieved in approximately an hour and fifteen minutes using this method <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.