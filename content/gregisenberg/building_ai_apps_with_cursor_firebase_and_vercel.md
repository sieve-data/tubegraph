---
title: Building AI Apps with Cursor Firebase and Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

The process of [[building_apps_with_ai_tools | building apps with AI tools]] has evolved, with a significant shift towards using Cursor as a primary development environment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach streamlines development, particularly for full-stack AI applications <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Evolution of the Development Workflow

Initially, [[building_apps_with_ai_tools | building apps with AI]] involved multiple tools:
*   **VZ (V0) for front-end design:** This tool was used to conceptualize and build the user interface (UI) of an application, such as the "Sip or Spit" app <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The UI from VZ would then be imported into Cursor <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Cursor for coding:** Once the front end was designed, Cursor was used for the underlying code <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Replit for live web view and deployment:** Replit was favored for its easy-to-use templates, simplified deployment, and a straightforward web view to see live changes <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Cursor's codebases were synced with Replit via SSH <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### The Rise of Cursor Agent

The introduction of Cursor's "Agent" feature within Composer significantly simplified the development process <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Agent is considered a highly legitimate and continuously improving AI agent for coding <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. With Agent's advancements, the reliance on Replit for local development has decreased, allowing developers to directly use GitHub for templates and run projects locally <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

> "Cursor releases Agent, and I was like, oh here we go again. Agent is a buzzword. No, this thing is legit, like it is the most legit agent on the market in my opinion." <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>

## Building an AI Image Generator: A Step-by-Step Example

This section outlines how to [[building_apps_with_ai_tools | build an app]] using Cursor Agent, a GitHub template, external APIs, and cloud services.

### 1. Project Setup in Cursor

1.  **Open a new folder:** Start by opening a blank folder in Cursor, which serves as the project directory <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  **Clone a GitHub repository:** Use Cursor Agent to clone a Next.js template repository from GitHub and run it locally with a single command <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This leverages pre-configured templates, some of which have over 15,000 uses on Replit <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
3.  **Local server access:** Once cloned, the app runs on a local server (e.g., `localhost:3001`), allowing for live changes and immediate feedback <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### 2. Integrating APIs and Models

*   **Understanding APIs:** APIs (Application Programming Interfaces) act like instruction manuals for Cursor, defining how different services or models communicate <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Cursor needs explicit examples of API usage to integrate them correctly <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Finding AI Models:** Platforms like Replicate and Foul offer a wide range of creative AI models <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Initial Image Generator Implementation (Flux):**
    *   Use Perplexity to find Next.js code examples for using a specific AI image model, such as Flux on Replicate <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   Provide Cursor with the prompt (e.g., "create a simple AI image generator"), the copied code examples, and the necessary API token <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. API tokens are crucial for tracking usage and billing, as API calls incur costs <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
    *   Cursor automatically places the API token in an `env.local` file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
*   **Debugging and Iteration:**
    *   Errors are common; provide Cursor with error messages, additional documentation (from API docs), and working code examples from playgrounds <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
    *   Playgrounds allow testing model behavior before coding, ensuring the desired output <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
    *   It's essential to give Cursor full context, as it doesn't "see" the web view; relay all observed information to aid debugging <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.
*   **Adding Multiple Models (Ideogram):**
    *   Once a model is integrated, adding others is easier by providing Cursor with the new model's examples and API information <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
    *   For example, Ideogram, known for generating images with text, can be added as an option <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
*   **Enhancing UI for Debugging:** Add elements like an info popup to display the model used and parameters, making it easier to test and compare outputs <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

### 3. Designing the User Interface (UI)

*   While some prefer to start with design, integrating core functionality first and then refining the UI is an alternative approach <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
*   Cursor can be prompted to create an "absolutely amazing design" for the app while maintaining existing functionality <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>. This includes adding a title to the top bar <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.

### 4. Integrating Firebase for Authentication and Storage

This step enables user sign-in and persistence of generated data, transforming the app into a full-stack experience. The process leverages a template preconfigured with Firebase <a class="yt-timestamp" data-t="00:42:54">[00:42:54]</a>.

1.  **Firebase Project Setup:**
    *   Go to the Firebase console and create a new project (e.g., "Mount Cursor") <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>.
    *   Do not enable Google Analytics initially to simplify the setup <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
    *   Register a web app within the Firebase project <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.
2.  **Connecting API Tokens:**
    *   Copy the Firebase API tokens provided in the Firebase web app setup <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
    *   Paste these tokens into Cursor's prompt, instructing it to place them in the correct `.env` file <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>. The template may include additional environment variables for other AI models (e.g., OpenAI, Anthropic) even if not currently used <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a>.
3.  **Firebase Services Configuration:**
    *   **Firestore Database:** Create a new database in "test mode" for initial development ease <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.
    *   **Storage:** Set up storage for images, upgrading the project and optionally setting a spending limit to prevent unexpected charges <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.
    *   **Authentication:** Enable Google Sign-In, which is automatically configured for local host when using Cursor <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
4.  **Integrating Features:**
    *   Prompt Cursor to implement user sign-in (displaying a sign-in page if not authenticated) <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Ensure generated images are automatically saved to the user's Firebase storage <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Add a "My Images" tab to the top bar, leading to a new page displaying all generated images for the signed-in user <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
    *   Display relevant image generation details (model, prompt, parameters) next to each saved image <a class="yt-timestamp" data-t="00:52:17">[00:52:17]</a>.

### 5. Deployment with Vercel

Deploying the application to a public domain makes it accessible to others.

1.  **GitHub Repository:**
    *   Create a new public repository on GitHub for the project <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>. Cursor Agent can often create the repository directly, simplifying the process <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
2.  **Vercel Deployment:**
    *   Instruct Cursor Agent to deploy the app to Vercel and commit changes to GitHub <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
    *   Follow Vercel CLI prompts to set up the project (e.g., link to GitHub, define project name and directory) <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>.
    *   **Environment Variables on Vercel:** Crucially, Firebase API tokens and other environment variables must be manually added to Vercel's project settings (under `Settings > Environment Variables`) <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>. A common deployment failure occurs if these are missing <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>.
    *   **Authorize Domain in Firebase:** For the deployed app to work, its domain (e.g., `*.vercel.app`) must be added to Firebase's authorized domains under `Authentication > Settings > Authorized domains` <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

> "The thing is I just moved off Replit and so I'm learning with everybody else which is fun." <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>

## Conclusion

This comprehensive workflow, predominantly managed within Cursor, enables the rapid development and deployment of full-stack [[building_ai_apps_for_organic_growth | AI apps]] with features like image generation, user authentication, and data storage. The iterative nature of building, debugging, and deploying is a core part of the learning process <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.

> "In conclusion, we started off in Cursor. We created a new project with an empty folder... then we used a GitHub repo which was one of my templates... From there we asked you to create an AI image generator... we added additional documentation and examples until it got it... we also added the ability to see all of the parameters... and then we used the template again to connect it to Firebase really quickly and now you can sign in and all of your images get saved... and then we deployed it to the Internet." <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>

## Additional Resources

*   **Yap Thread:** A social app featuring a "composer" feature for saving notes, chatting with AI, and managing bookmarks/sources <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>. This represents an example of [[building_a_social_app_with_ai | building a social app with AI]].
*   **Software Composers Community:** A free community focused on [[building_ai_apps_for_organic_growth | building AI apps]] and sharing templates <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.