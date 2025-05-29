---
title: Integration with Firebase and Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

This article outlines a process for building and deploying an AI-powered application locally using Cursor and then integrating it with [[Working with Firebase and Google Ecosystem | Google Firebase]] for backend services and [[Deploying AI Apps Using GitHub and Vercel | Vercel]] for deployment. The workflow emphasizes using Cursor's Agent feature to streamline development and deployment.

## Shifting Development Workflow
The speaker has transitioned to primarily using Cursor for building AI applications, moving away from tools like Replit for certain tasks due to Cursor's new features.
Previously, the process involved building a front-end on Vercel (V0), then importing it into Cursor for development, and using Replit for live web view and easy deployment [01:15:20] [01:34:00]. Replit was favored for its ease of use with templates and deployment [01:41:00].
However, Cursor's new Agent feature within Composer has significantly improved, making it possible to run apps locally without needing Replit for live previews [02:08:00] [02:36:00]. Now, [[Deploying AI Apps Using GitHub and Vercel | GitHub]] is used for templates, and Cursor can run the code locally [02:44:00].

## Building an AI Image Generator App
The demonstration begins by building a simple AI image generator.

### Initial Setup with Cursor
1.  **Open Cursor**: Begin by opening the Cursor application [03:57:00].
2.  **Create a New Folder**: Select "Open a folder" and create a new, empty folder on your computer (e.g., on the desktop) [04:00:00]. This serves as the project directory [04:24:00].
3.  **Access Composer**: Once the folder is open, press the button to open Composer within Cursor [04:29:00].
4.  **Clone a GitHub Repository**: Use a single prompt to tell Cursor to clone a GitHub repository (a Next.js template) and run it locally [05:06:00] [05:53:00]. The speaker uses their own free template for this [03:47:00].
    *   **YOLO Mode**: The speaker uses "YOLO mode" in Cursor, which automatically confirms commands without requiring repeated manual confirmation. This is for advanced users and requires trust in the source code [06:49:00] [08:13:00]. For beginners, it's safer to manually confirm commands, especially when cloning from untrusted sources [08:24:00].
5.  **Live Web View**: After the command runs, Cursor provides a local host link (e.g., `localhost:3001`) to view the running application [07:10:00]. Changes made in Cursor are instantly reflected in the live web view [07:54:00].

### Integrating AI Features
The app is developed iteratively using Cursor's Agent and external APIs.
*   **API Concepts**: APIs (Application Programming Interfaces) are like instruction manuals for different coding rules, which Cursor needs examples of to integrate effectively [12:08:00] [12:14:00].
*   **Finding API Examples**: Perplexity is used to find Next.js code examples for integrating AI image models like Flux from Replicate [11:09:00] [11:16:00]. Other platforms like Replicate and Fal.ai make it easier to add [[Integrating AI features in app development | AI features in app development]] [11:38:00].
*   **API Keys**: Most APIs require an API token (key) for tracking usage and billing, as these services are not free [13:35:00] [13:50:00]. It's crucial to keep API keys secure and not expose them [14:28:00].
*   **Prompting Cursor for API Integration**:
    1.  Provide clear instructions (e.g., "create a simple AI image generator") [15:36:00].
    2.  Include code examples for the API (copied from Perplexity or API documentation) [15:54:00].
    3.  Provide the API token, instructing Cursor to place it in the correct environment file (e.g., `.env.local`) [15:57:00] [16:08:00].

### Iterative Problem Solving
Development often involves debugging and refinement:
*   **Error Handling**: If an API request fails, paste the error message back into Cursor and provide additional context, such as links to official API documentation or examples from a playground (e.g., Replicate Playground) [17:43:00] [18:15:00] [19:32:00].
*   **Context is Key**: Always provide Cursor with all visible information (e.g., web view errors, console outputs), as Cursor doesn't inherently "see" the live application [21:39:00].
*   **Restarting Server**: Sometimes, after major changes, restarting the local development server (e.g., `npm run dev`) is necessary to apply updates and resolve server errors [23:28:00] [24:35:00].
*   **Adding Model Options**: The app was enhanced by adding a toggle for different AI image models (Flux Pro, Ideogram), with the ability to provide new model examples and documentation to Cursor [28:48:00] [32:48:00].
*   **Displaying Model Details**: A feature was added to display the model used and its parameters in a pop-up, helping with testing and understanding [26:55:00].

### Design Enhancements
After core functionality is established, design improvements can be made:
*   Prompt Cursor to "create an absolutely amazing design" while specifying that functionality should remain unchanged and requesting a title for the app (e.g., "Mount Cursor") [38:03:00].

## [[Working with Firebase and Google Ecosystem | Firebase Integration]]
The pre-configured template makes [[Working with Firebase and Google Ecosystem | working with Firebase and Google Ecosystem]] straightforward.
1.  **Prompt Cursor**: Instruct Cursor to enable Google Firebase authentication and storage, requiring users to sign in to access the app and automatically saving generated images to their database. Also, request a "My Images" tab to view saved images [42:39:00].
2.  **Firebase Project Setup (Manual Steps)**:
    *   Go to the Firebase console and create a new project (e.g., "Mount Cursor") [43:59:00].
    *   **Disable Google Analytics** initially for simplicity [44:44:00].
    *   **Register as a Web App**: Select the web app option and copy the provided API keys [45:11:00] [45:30:00].
    *   **Paste API Keys in Cursor**: Provide these Firebase API keys to Cursor, instructing it to place them in the correct environment file (e.g., `.env`) [45:44:00].
    *   **Configure Firebase Services**:
        *   **Firestore Database**: Go to "Build" > "Firestore Database" and create a database in "test mode" for easier initial development [46:39:00] [46:53:00].
        *   **Storage**: Go to "Build" > "Storage" and enable it. It might require upgrading your Firebase project to a paid plan, but you can set a spending limit (e.g., $20) to prevent unexpected costs [47:12:00] [47:21:00].
        *   **Authentication**: Go to "Build" > "Authentication" > "Get Started" and enable "Google" as a sign-in provider, selecting a support email [48:17:00] [48:25:00]. Localhost is automatically authorized [48:25:00].
3.  **Verifying Integration**: After Cursor implements the changes and Firebase is configured, users can sign in with Google, generate images, and view them in a "My Images" tab, with data stored in Firebase Storage and Firestore [51:58:00] [54:50:00].

## [[Deploying AI Apps Using GitHub and Vercel | Deployment to Vercel]]
The final step is to deploy the app to the internet using [[Deploying AI Apps Using GitHub and Vercel | Vercel]].
1.  **Create GitHub Repository**: Create a new public repository on GitHub (e.g., "Mount Cursor") [55:07:00] [55:15:00]. Copy the repository link [55:32:00]. (Note: Cursor's Agent might be able to create the repo automatically, reducing this manual step [57:08:00]).
2.  **Prompt Cursor for Vercel Deployment**: Tell Cursor to deploy the app to Vercel and commit changes to GitHub, providing the GitHub repository link [56:01:00].
3.  **Vercel CLI Interaction**: Cursor will use the Vercel CLI.
    *   You might need to log in to Vercel via a browser link provided by Cursor [58:28:00].
    *   Answer prompts in the terminal (e.g., personal/business scope, link to existing project, project name, code directory) [58:45:00].
4.  **Troubleshooting Deployment Errors**:
    *   **Missing Environment Variables**: Deployments often fail if API keys and other environment variables (like the `REPLICATE_API_TOKEN`) are not configured in Vercel [01:01:04] [01:17:00].
    *   **Adding Environment Variables in Vercel**: Navigate to your project in Vercel, go to "Settings" > "Environment Variables," and add the necessary keys (e.g., `REPLICATE_API_TOKEN`) with their corresponding values [01:03:01] [01:05:03] [01:05:12] [01:05:22] [01:07:20].
    *   **Redeploy**: After adding variables, redeploy the project in Vercel [01:07:04] [01:07:20].
    *   **Firebase Authorized Domains**: For authentication to work on the deployed app, you must add the Vercel domain (e.g., `your-app-name.vercel.app`) as an authorized domain in Firebase Authentication settings [01:09:03] [01:09:43].
5.  **Successful Deployment**: Once these steps are completed, the app will be live on a Vercel URL, fully functional with authentication and image generation/storage [01:08:47] [01:10:04].

## Conclusion
The demonstration showcases a streamlined process for building and deploying a full-stack AI application using Cursor's capabilities, integrating external APIs, and leveraging [[Working with Firebase and Google Ecosystem | Firebase]] and [[Deploying AI Apps Using GitHub and Vercel | Vercel]]. This iterative approach allows for rapid development and problem-solving.

### Other Tools & Concepts Mentioned
*   Bolt [00:27:00]
*   V0 [00:27:00]
*   Windsurf [00:30:00]
*   Replit [00:34:00]
*   Lovable [00:34:00]
*   Next.js [02:54:00]
*   Perplexity API [10:33:00]
*   Flux (AI Image Model) [11:09:00]
*   Replicate (Creative AI Models) [11:27:00]
*   Fal.ai [11:38:00]
*   Claude (AI Model) [15:42:00]
*   Ideogram (AI Image Model) [33:32:00]
*   Mini-plex [38:50:00]
*   Firebase Studio [00:00:00] (not explicitly mentioned in this segment but in related topics)
*   Supabase [00:00:00] (not explicitly mentioned in this segment but in related topics)
*   Yap Thread (Speaker's project) [02:50:00] [02:54:00] [02:59:00]
*   Instant DB [00:00:00] (not explicitly mentioned in this segment but in related topics)
*   Namecheap [00:59:58]
*   Paul Graham (Essay on sketching) [34:54:00]
*   Devin (Company building an AI developer) [22:38:00]
*   OpenAI [18:04:00]
*   Anthropic [01:05:57]
*   Deepgram [01:05:57]
*   11 Labs [01:19:21]