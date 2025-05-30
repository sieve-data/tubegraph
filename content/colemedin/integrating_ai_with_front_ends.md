---
title: Integrating AI with Front Ends
videoId: yRIEpNlacd0
---

From: [[colemedin]] <br/> 

This article details the process of [[creating_custom_frontends_for_ai_agents | building custom front ends]] for AI agents, moving beyond basic terminal interactions or platform-provided interfaces. It outlines a multi-tool approach combining various AI coding assistants to achieve a polished, functional, and easily maintainable front end. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Why Custom Front Ends?

Previously, AI agents were integrated with platforms like Live Agent Studio's Agent Zero to quickly gain a polished front end, replacing the need for an "ugly terminal" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. However, for a more tailored and flexible user experience, [[creating_custom_frontends_for_ai_agents | rolling your own fully custom front end]] is preferred <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Leveraging AI Coding Assistants

[[creating_custom_frontends_for_ai_agents | Building custom front ends]] for AI agents can be significantly accelerated using AI coding assistants. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> The video highlights a strategy that combines different tools to leverage their individual strengths <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>:

*   **Lovable / Bolt.new (In-Browser Editors):** These platforms are optimized for a single Large Language Model (LLM) and are excellent for starting a project and establishing a solid foundation <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. They excel at quickly getting a project started <a class="yt-timestamp" data-t="01:07:59">[01:07:59]</a> and are particularly good for certain application styles, such as chat applications <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Lovable also provides free credits to begin <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Bolt.DIY (Open-Source and Self-Hosted):** This tool allows users to run it on their own computer and utilize completely free LLMs <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. It addresses the common issue of running out of credits when making continuous tweaks in commercial platforms <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. While it might not provide the best performance for initial foundation creation, it enables free and unlimited iteration <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **AI IDEs (e.g., Windsurf, Cursor):** These integrated development environments run directly on the user's computer and are highly effective for making more "directed changes" to applications <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. They are ideal for applying final touches to a nearly finished project <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Windsurf also offers free credits <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

The recommended process is to start with a platform like Lovable or Bolt.new for the initial foundation, then move to Bolt.DIY for extensive, free tweaking, and finally use an AI IDE for precise, directed changes before deployment <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Step-by-Step Process for [[creating_custom_frontends_for_ai_agents | Custom Front End Development]]

### 1. Preparing the AI Agent as an API Endpoint

Before [[connecting_ai_agents_to_frontend_applications | connecting an AI agent to a frontend application]], the agent must be exposed as an API endpoint <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This ensures compatibility with any front end, regardless of the platform used to build it <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. A Python-based AI agent, for example, can be turned into an API endpoint using Pydantic <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Initial Front End Creation with Lovable

The first step in [[building_and_deploying_custom_ai_front_ends | building and deploying custom AI front ends]] is to use Lovable (or Bolt.new) to generate the initial project structure. <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>

#### Prompting Strategy

The prompt given to Lovable needs to be highly specific about the AI agent's functionality and data handling, while being more general about the UI <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>:

*   **UI Specification:** General requests for a "beautiful dark theme" with specified colors are sufficient, as these tools are good at creating interfaces <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Agent URL:** The API endpoint URL of the AI agent must be provided to dictate the application's flow and ensure connection <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Input/Output Schema:** Detailed payload schema for inputs and outputs is crucial for the front end to correctly handle messages and display conversations <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Superbase Integration:**
    *   The Superbase project URL and public key are embedded directly into the code, avoiding `.env` files for simplicity <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. These are public keys and can be safely shared <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   The schema for the `messages` table in Superbase is provided, as it's used to store and display conversation history <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   Real-time capabilities for the `messages` table must be specified so the front end can subscribe to changes and immediately pull new messages from the agent <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Instructions for setting up Superbase, including the `messages` table and real-time communication, are available in developer guides <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Additional Requirements:** A section for various smaller UI/UX requirements like markdown handling, loading indicators, and Superbase email/password authentication is included <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

Lovable can generate a full front end, including Superbase authentication and conversation history, from a single detailed prompt <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. The generated app can immediately communicate with a locally running AI agent <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

### 3. Refining the Front End with Bolt.DIY

After the initial generation, the project is moved to Bolt.DIY for free and iterative refinement.

#### Transferring to GitHub

The project is first published to GitHub from Lovable <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. It's recommended to make the repository public for easier import into Bolt.DIY without needing to sign in <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

#### Installing and Running Bolt.DIY

Bolt.DIY is installed locally, typically requiring Node.js and Git <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. The process involves cloning the Bolt.DIY repository, installing dependencies (`pnpm install`), and starting the development server (`pnpm run dev`) <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. Bolt.DIY runs on a local server, usually accessible via `localhost:5173` <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

API keys for LLMs (e.g., Google's Gemini 2.0 Flash) are set directly within Bolt.DIY's interface, avoiding manual `.env` file modifications <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

#### Importing and Tweaking

The GitHub repository containing the Lovable-generated code is cloned directly into Bolt.DIY <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Bolt.DIY then installs dependencies and starts the application, displaying the same front end as Lovable <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

```ad-warning
title: Localhost Communication Limitation
Chatting with the AI agent will not work within Bolt.new or Bolt.DIY because their web containers block requests to localhost agents. The focus here is solely on UI/UX improvements. <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>
```

When making changes in Bolt.DIY, it's advised to request one UI/UX adjustment at a time to improve the LLM's understanding and accuracy <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. Bolt.DIY, when used with models like Gemini, supports image input, allowing users to screenshot problematic areas for visual reasoning by the AI <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. This iterative process allows for significant improvements to the user interface, such as better button appearance, chat input fields, and conversation display <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.

### 4. Finalizing with an AI IDE

The final step involves moving the project to an AI IDE for precise, "directed changes" and preparation for deployment <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.

#### Downloading and Running Locally

The refined code is downloaded as a zip file from Bolt.DIY <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. After unzipping, the project is run locally using `npm install` and `npm run dev` to install dependencies and start the development server (e.g., `localhost:8080`) <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

#### Using AI IDEs for Directed Changes

AI IDEs like Windsurf or Cursor are ideal for making granular adjustments after the initial bulk of the UI/UX work is done in in-browser editors <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. This also helps when in-browser editors might "get stuck" after numerous tweaks <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. The locally running application can be tested to ensure the AI agent integration is fully functional <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

## Conclusion

This multi-tool approach to [[creating_custom_frontends_for_ai_agents | building custom front ends for AI agents]] combines the strengths of various AI coding assistants to achieve a "perfect blend of free, flexible, and fast" development <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. The process allows for initial rapid prototyping, followed by extensive free iteration, and concludes with precise refinements, leading to a production-ready and monetizable AI agent <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.