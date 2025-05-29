---
title: Implementing and deploying AI voice applications with Nextjs
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

[[Voicedriven AI applications | AI voice character applications]] are emerging as a significant opportunity, with creators developing engaging experiences that are generating revenue and gaining viral traction on social media <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide outlines how to implement and deploy these applications using tools like Next.js, Daily, and Vercel.

## The Rise of AI Voice Characters

Characters are seen as the "new apps," representing a significant, under-discussed opportunity <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The core concept involves building "audio ChatGPT" or voice chat apps <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. While seemingly a "toy," many successful startups begin with simple, engaging concepts <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Research indicates that [[building_a_social_app_with_ai | AI character chat apps]] are not a passing fad, with high retention rates suggesting they are the future of highly engaging consumer applications <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This trend applies to both B2B and B2C sectors, as voice interaction becomes a new form of content consumption <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Core Tools and Technologies

Several key tools facilitate the development of [[building_apps_with_ai_tools | AI voice applications]]:

*   **Cursor**: A code editor integrated with LLMs to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily**: The primary platform responsible for voice processing and backend operations <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **[[creating_ai_voice_character_apps_with_daily_bots | Daily Bots]]**: A specific offering from Daily that simplifies the process by handling LLM calls directly, allowing developers to focus on configuration <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **[[using_ai_tools_like_daily_and_pipcats_for_voice_apps | Pipcats]]**: Another library from Daily, more developer-focused, providing greater control for interfacing with AI and building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Together AI**: A provider of various AI models, including Llama 3.1 70B, used for the LLM backend <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Next.js**: A React framework that enables server-side rendering and API routes, serving as the foundation for the web application <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Vercel**: A platform created by the developers of Next.js, offering seamless hosting and deployment for Next.js applications <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.
*   **GitHub**: Used for cloning repositories, which essentially means downloading project code to a local system <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Implementing a Voice Character App

The process involves configuring an existing demo project to create a custom voice character.

### Initial Setup

1.  **Clone the Demo Repository**: Start by cloning the Daily Bots demo repository from GitHub <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This downloads the project files to your local machine <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Obtain Daily API Key**: Sign up for Daily and retrieve your API key from their dashboard. This key unlocks access to Daily's services <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Configure Environment**: Paste the API key into the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
4.  **Run Locally**: Execute the command `yarn dev` in your terminal to start the local server. The application will then be accessible via a local host URL in your browser <a class="yt-timestamp" data-t="00:05:46">[00:06:01]</a>.

At this stage, no custom code has been written; it's purely setup <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Understanding Bot Configuration

The core of customizing the AI voice character lies in its configuration file.

*   **Prompt Engineering**: The character's behavior is dictated by its "prompt," which is the instruction set given to the LLM (e.g., "You are an assistant called Example Poot. You can ask me anything.") <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Instructions on how the bot should speak are crucial for correct audio output <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Voice Processing Pipeline**:
    1.  Audio from the microphone is converted into text via a Speech-to-Text (STT) provider <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    2.  This text is sent to the LLM (AI model), which processes it and generates a text response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    3.  Daily then takes the LLM's text response and converts it into speech using a Text-to-Speech (TTS) provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    4.  The generated speech is streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    This complex system is handled by Daily, allowing developers to focus on the character's role and personality <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Customizing Characters**: The demo comes with preset characters (e.g., "Gen Z middle schooler," "skateboard meme guy") <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. To create your own character, simply edit or add entries to the configuration file, and the changes will reflect directly in the app <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Implementing Function Calling (Tools)

Function calling enables the AI to interact with external systems and perform actions beyond just generating text.

*   **Concept**: An LLM only outputs text <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Function calling is a system built around the LLM that takes its specially formatted text output and uses it to trigger specific code functions, such as calling APIs or retrieving data <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. The AI is "smart enough" to understand instructions and format its response to trigger these functions <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Weather Tool Example**:
    1.  **Define the Tool**: In the `config` file, define the "weather tool" with a clear name (e.g., `get_weather`) and necessary parameters (e.g., `location`). This tells the AI what function it can access and what information it needs to provide <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
    2.  **Handle Tool Calls**: In the `page.tsx` file, define what happens when the AI "calls" the `get_weather` function. This involves making an API call to a backend route (e.g., `/api/weather`) <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
    3.  **Backend Route (Next.js API)**: Within the `api/weather` directory in Next.js, the `route.ts` file specifies the actual code that runs when the API is accessed <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. For demonstration, this route can be configured to return "nonsense weather" conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

*   **Designing for Virality**: Intentionally incorporating "wacky" or unexpected responses (like "singing rainbows") into the function's output can create "TikTok moments" that encourage users to screen-capture and share the experience, leading to free distribution <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Weather Bot Demonstration

Upon being asked for the weather in New York City, the configured weather bot responds with a unique forecast:
> "Folks, it's your lucky day! I've got the forecast for the Big Apple and it's looking like a real treat! We've got Cloudy Skies, but don't let that fool you. There's a chance of whimsical singing rainbows! That's right, you heard me right! It's going to be a day of magic and wonder in New York City. So grab your umbrella and your best singing voice and get ready to take on the day!" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>

This demonstration confirms that the function calling and custom responses are working as intended <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>.

## Deployment

Deploying your Next.js [[framework_for_developing_ai_saas_solutions | AI SaaS solution]] to the web is streamlined with Vercel.

*   **Vercel Integration**: Vercel makes it incredibly easy to host Next.js applications online <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>.
*   **Command Line Deployment**: After logging into your Vercel account via the command line interface (CLI), deploying your app is as simple as typing `vercel` <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>. This command triggers the deployment process, making your application live on the internet <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>.
*   **Accessibility**: Once deployed, the application is accessible via a unique URL on any device, allowing users to share and interact with the character <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

## Advanced Application: The Vtuber Face-Call App

As an example of a more complex [[building_ios_apps_using_ai | iOS app]] that can be built, Eric demonstrates a personal project: a FaceTime-like call with a "vtuber" <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>.

*   **Vtuber Concept**: Vtubers are content creators who stream using a digital avatar instead of their real face, often anime characters. This trend started in Japan and has gained immense popularity, with many vtubers amassing millions of followers and significant income <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.
*   **App Functionality**: This app allows users to have a one-on-one "personal call" with an AI-powered vtuber character <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
*   **Technology Choice**: Unlike the simpler Daily Bots demo, this app uses the [[using_ai_tools_like_daily_and_pipcats_for_voice_apps | Pipcats]] library because it offers developers more control over data flow, which is beneficial for complex interactions <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.
*   **Model Acquisition**: The vtuber models (avatars) can be purchased from marketplaces like Nzima, where illustrators and riggers sell models for streamers <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.
*   **Demonstration**: The app is shown interacting with a user, describing a drink as "so sweet and creamy," highlighting the advanced conversational capabilities <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.

This project showcases the potential for individuals to create sophisticated applications with AI tools, a feat that would have previously required a large team and significant capital <a class="yt-timestamp" data-t="00:36:58">[00:37:05]</a>.