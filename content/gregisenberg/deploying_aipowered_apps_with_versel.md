---
title: Deploying AIpowered apps with versel
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

[[Deploying apps using Vercel | Deploying AI-powered applications]] has become significantly streamlined with modern tools and platforms. The process involves leveraging frameworks like Next.js and deployment services such as Vercel to bring voice-enabled or character-based [[ai_app_development | AI applications]] to life.

## Key Technologies Utilized

The development and deployment of these [[ai_app_development | AI-powered apps]] rely on a combination of specific technologies:

*   **Next.js**: This framework is used to build the applications. It integrates React for front-end development and allows for the specification of server-side routes, which is crucial for handling API calls and bot logic <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>. Next.js is an open-source framework, making it free to develop with <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.
*   **Daily**: This company provides the core services for the voice functionality and back-end processing of the [[ai_app_development | AI bots]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Daily handles complexities such as Large Language Model (LLM) calls, speech-to-text (STT) conversion, and text-to-speech (TTS) synthesis <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Vercel**: The platform created by the developers of Next.js, Vercel allows for easy hosting of Next.js applications online <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

## The Deployment Process

[[Deploying apps using Vercel | Vercel simplifies the deployment of Next.js applications]] to the web:

1.  **Preparation**:
    *   The application's code is typically organized in a repository (e.g., a Daily Bots demo repo) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   An API key from the Daily service is used to connect the front-end demo to the Daily backend <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This key is stored in a local `.env` file <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
    *   Initially, the application runs locally using a command like `yarn dev` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

2.  **Using Vercel CLI**:
    *   Vercel provides a command-line interface (CLI) tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
    *   After logging into your Vercel account through the CLI, the deployment process is initiated with a single command: `vercel` <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.
    *   Vercel then handles the building and deployment of the application, typically taking around a minute and a half <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>, <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>.

3.  **Accessibility**: Once deployed, the application is live on the internet and accessible via a unique Vercel URL <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>, <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>. This URL can be shared for others to access the [[ai_app_development | AI-powered app]] on any device <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>, <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## Benefits for AI App Development

[[Deploying apps using Vercel | Vercel's ease of use]] makes it an ideal platform for [[ai_app_development | AI app development]], particularly for developers looking to rapidly iterate and launch:

*   **Rapid Deployment**: The simple `vercel` command allows for quick iteration and deployment of changes <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   **Simplified Hosting**: Vercel abstracts away the complexities of server setup and maintenance, allowing developers to focus on the application logic and [[building_apps_with_ai | AI integration]] <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
*   **Scalability**: Vercel is designed to host applications that can scale to meet demand.
*   **Accessibility**: Once deployed, the app is instantly available globally on any device, making it easy to share and test <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## Example: The Weatherman Bot

A fully working weatherman character app was created using these tools. The app demonstrates how an [[introduction_to_ai_agent_platforms | AI agent]] can be configured to respond to queries and perform actions (like fetching weather data, albeit humorous "nonsense" weather in this demo) <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. The character's personality and tools are defined in a configuration file, which can be easily edited to create new characters <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>, <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This approach highlights the potential for creating viral [[ai_app_development | AI-powered apps]] through creative character design and unexpected responses <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.