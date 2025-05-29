---
title: Using GitHub and Templates for App Development
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

The landscape of app development has rapidly evolved with the advent of AI tools, making it accessible to a broader audience, including those with limited coding experience <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. A key shift has been towards leveraging platforms like GitHub for project hosting and [[utilizing_templates_and_starter_kits_in_development | templates]] for accelerated development <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Evolution of the Development Workflow

Initially, a common workflow involved using VZ for frontend design, then importing that into Cursor for code development, and finally utilizing Replit for running and viewing code in a web view <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Replit was favored for its ease of use with [[utilizing_templates_and_starter_kits_in_development | templates]] and deployment, offering a convenient live web view <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Transition to Cursor Agent and GitHub

A significant advancement came with Cursor's Agent feature, which has become a highly effective tool for AI-assisted development <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This improvement means that developers can now primarily use Cursor Agent in conjunction with [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] directly, eliminating the need for additional tools like Replit for templates <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. [[utilizing_templates_and_starter_kits_in_development | Templates]], particularly those for Next.js, can be stored on [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] and easily run locally using Cursor <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Utilizing GitHub Templates with Cursor Agent

The process of starting a project with Cursor Agent and a [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] template is straightforward and requires no prior coding experience <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Step-by-Step Setup

1.  **Open Cursor and Create a Project:** Within Cursor, select "Open a folder" and create a new, empty folder on your computer to serve as your project directory <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Access Cursor Composer:** Click the "Composer" button to open the AI assistant <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
3.  **Clone the GitHub Repository:** Provide a prompt to Cursor Agent to clone your desired [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] repository and run it locally <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   Example Prompt: "clone the repo and run it locally in one command [GitHub_repo_link]" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
4.  **YOLO Mode (Optional but Recommended for Beginners):** For ease of use, enabling "YOLO mode" in Cursor automatically executes commands without requiring repeated confirmations <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. While convenient, users should ensure they trust the source of any [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] repository cloned with this mode <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
5.  **Local Host Access:** Cursor Agent will set up the project on a local host port, providing a link to view the running application directly <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Changes made in Cursor are instantly reflected in the live web view <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Integrating APIs for Enhanced Functionality

Integrating Application Programming Interfaces (APIs) is crucial for adding advanced features to apps <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Even without knowing what API stands for, AI tools make integration possible <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

#### Example: Building an AI Image Generator

To build an AI image generator using Replicate (a platform for creative AI models) <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>:

1.  **Gather Examples and Instructions:** Use a tool like Perplexity to get Next.js code examples for the desired AI model (e.g., Flux) on Replicate <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Think of these as "instruction manuals" for Cursor <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
    *   Prompt Example: "I want to create a simple AI image generator. I want to use Replicate and I want to use Flux. [Paste code examples]" <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
2.  **Provide API Key:** Most APIs require an API token for billing and tracking <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
    *   Prompt Example: "This is my API token: [Your_API_Token]. Please put it in the correct place." <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Cursor Agent will place this in an `env.local` file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
3.  **Troubleshooting:** If the initial attempt fails, provide the error message and additional documentation from the API provider's website (e.g., Replicate's docs or playground) back to Cursor Agent <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. The agent can read and process external links <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. Providing more context and details about the error helps the AI fix it <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

### Adding Design and Database Functionality

Once the core features are functional, focus on design and database integration:

1.  **Enhance User Interface (UI):** Prompt Cursor Agent to improve the app's design for a more modern look, specifying elements like a top bar title <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The live view allows immediate feedback on design changes <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>.
2.  **Implement Firebase for User Authentication and Storage:**
    *   Since the template includes Firebase configuration, you can prompt Cursor to integrate Google Firebase authentication and storage <a class="yt-timestamp" data-t="00:42:54">[00:42:54]</a>.
    *   Manual steps required:
        *   Create a new Firebase project in the console <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
        *   Add a web app and copy its API tokens <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.
        *   Provide these API tokens to Cursor Agent to place in the `env` file <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.
        *   Enable Firestore Database (start in test mode) <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>.
        *   Enable Storage (requires upgrading project to a paid plan, but can set limits to manage costs) <a class="yt_timestamp" data-t="00:47:12">[00:47:12]</a>.
        *   Enable Google Authentication in Firebase <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. Local host authentication is automatically set up <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
    *   Prompt Cursor to implement features like a sign-in page, image generation only for signed-in users, automatic saving of images to storage, and a "My Images" tab <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>.

## [[deploying_apps_using_vercel | Deploying Apps Using Vercel]]

To make the app publicly accessible, it needs to be deployed. [[deploying_apps_using_vercel | Vercel]] is a common choice for deployment <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.

1.  **Create a [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] Repository:** Create a new public repository on [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>. Cursor Agent may even be able to create the repository directly <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
2.  **Deploy with Cursor Agent:** Prompt Cursor Agent to deploy the app to [[deploying_apps_using_vercel | Vercel]] and commit changes to [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
    *   Cursor Agent will guide through the [[deploying_apps_using_vercel | Vercel]] CLI (Command Line Interface) process, including signing in and linking the project <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
3.  **Add Environment Variables in [[deploying_apps_using_vercel | Vercel]]:** For successful deployment, API keys and tokens (e.g., Replicate API Token) must be added as environment variables directly in the [[deploying_apps_using_vercel | Vercel]] project settings <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
4.  **Authorize Domain in Firebase:** Once deployed to [[deploying_apps_using_vercel | Vercel]], the new public domain must be added to the authorized domains in Firebase's authentication settings for sign-in functionality to work <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

The entire process, from setting up a blank project to deploying a full-stack application with user authentication and image storage, can be achieved iteratively within a relatively short timeframe using these tools <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>.

## Conclusion

Using [[nontechnical_guide_to_setting_up_and_using_github | GitHub]] with [[utilizing_templates_and_starter_kits_in_development | templates]] and Cursor Agent streamlines the app development process, making it more accessible and efficient. The ability to iterate quickly, troubleshoot with AI assistance, and deploy easily to platforms like [[deploying_apps_using_vercel | Vercel]] empowers individuals to build and launch their own applications <a class="yt-timestamp" data-t="01:11:48">[01:11:48]</a>. While challenges may arise, embracing the iterative nature of development and using AI as a powerful assistant can lead to successful outcomes <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.

# Additional Resources
*   Yap Thread App: [yapthread.com](https://yapthread.com) <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>
*   Software Composers Community (templates and AI app building discussions): Close to 10,000 members <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>