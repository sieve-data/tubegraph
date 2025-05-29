---
title: AI voice character apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

AI voice character apps are emerging as a significant new category, with some "printing money" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These applications, which allow users to interact with AI personalities via voice, are considered the "new apps" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The technology allows for rapid development, making it possible to create a functional app quickly <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Characters as the New Apps

The concept of "characters as the new apps" presents a significant opportunity <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This idea is gaining traction, especially in the tech scene <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Nikita Bier, a notable figure in tech, initially thought AI character chat apps were a fad but changed his view after observing their strong retention graphs, concluding they are not going away <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

AI characters are expected to be the future of highly retentive and engaging consumer and non-consumer apps <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This applies to both B2B and B2C sectors, fundamentally changing how people interact with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Building AI Voice Character Apps

[[building_apps_using_ai_tools | Building apps using AI tools]] and [[building_voice_ai_agents_with_vappy | building voice AI agents]] is now easier than ever due to available tools <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Even without extensive coding knowledge, individuals can pick up concepts like GitHub, cloning a repository, and deploying applications <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Key Tools and Technologies

*   **Code Editor**: Cursor is recommended as a code editor, integrated with LLMs for coding assistance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Voice AI Backend**: Daily.co is a company that handles the heavy lifting for voice and backend processes <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   Daily Bots is a specific product from Daily.co that simplifies LLM calls <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   Pipcat is another library from Daily.co, more developer-focused, offering more control over AI interfaces and voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Framework**: Next.js is a framework used to set up a server that runs React, allowing for the specification of routes and pages that run code <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Deployment**: Vercel provides a platform to host Next.js apps online, making deployment simple, often with a single command (`vercel`) <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### The Development Process

The process typically involves:
1.  **Setting up the Environment**: Cloning a demo repository from Daily.co <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This means downloading it to your system and opening it <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
2.  **Connecting to Daily.co**: Obtaining an API key from the Daily.co dashboard and pasting it into a `.env.local` file <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Running the Server**: Starting the server using a command like `yarn dev` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
4.  **Configuring Personality**: The character's personality is defined in a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This file specifies the prompt for the LLM and instructions on how the character should speak <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. Pre-built characters exist, but custom characters can be created by editing this file <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
5.  **Implementing Function Calling**: This allows the AI character to perform actions beyond just outputting text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   **LLM Role**: The LLM understands instructions and outputs a response in a specific format that the system can interpret <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. The LLM itself only outputs text; the surrounding system performs the actions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
    *   **Tool Definition**: A tool (e.g., a "weather tool") is defined to the LLM, specifying its name and necessary parameters (e.g., `location` for weather) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
    *   **Action Definition**: The system defines what actually happens when the AI "calls" a function (e.g., making an API call to a `/api/weather` route) <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
    *   **Example: The Weatherman App**: A fully working weatherman character app was created during the demonstration <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The character responds with whimsical weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. This quirky output serves as a viral element <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
6.  **Deployment**: Once configured, the app can be deployed live using Vercel, making it accessible via a URL on any device <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>.

## How Voice AI Agents Work

The underlying mechanism involves several steps <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT)**: The Daily bot system takes audio from the microphone and converts it into text using a Speech-to-Text provider <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **LLM Processing**: This text is then fed into an LLM (Large Language Model), such as Llama 3.1 70B via Together AI <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The LLM processes the input and generates a text response <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
3.  **Text-to-Speech (TTS)**: Daily takes the LLM's text response and pipes it into a Text-to-Speech provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is then streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire system handles complexities like performance and error handling, allowing developers to focus on the assistant's behavior <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## [[ai_app_startup_ideas | AI App Startup Ideas]] and Strategy

The ability to create these [[aipowered_mobile_apps | AI-powered mobile apps]] and voice characters quickly opens up many [[voice_ai_applications_in_startups | AI app startup ideas]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   **Ideation**: Focus on ideating new characters and figuring out what will resonate with users <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Virality**: Design characters with "TikTok moments" in mind, such as humorous or unexpected responses, to encourage free distribution through user recordings and shares <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Iteration**: When [[ai_app_development_strategies | building apps using AI tools]], it's crucial to make small, understandable changes and build incrementally off existing demos rather than attempting to "one-shot" an entire app <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. This approach aids learning and development <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

## Advanced Examples of AI Voice Character Apps

Eric, the developer, has created advanced applications using these principles.
*   **Vtuber Facetime App**: One example is an app that allows users to have a "FaceTime" call with a Vtuber (a virtual YouTuber who uses an avatar instead of their real face) <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. Vtubers are popular content creators, especially in Japan, with large followings and significant income <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
    *   This app uses Pipcat for more granular developer control, as opposed to Daily Bots <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.
    *   The Vtuber models are purchased from marketplaces like Booth (booth.pm) <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>.
    *   The app allows for a personal, interactive voice call experience with the Vtuber character <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.

This demonstrates how a complex application that previously required a large team and significant capital can now be built by an individual <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.

### [[tips_for_developers_using_ai_in_app_development | Tips for Developers Using AI in App Development]]
*   **Read Documentation**: Develop the habit of reading and understanding documentation <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Ask AI**: If you don't understand something, ask ChatGPT or Claude for clarification <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Build Incrementally**: Start with existing demo repositories and add small, understandable changes <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.
*   **Understand Core Concepts**: Gain insight into how things actually work, rather than viewing AI as a "blackbox" <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. For example, understanding that an LLM only outputs text, and a surrounding system enables actions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.

For more information, follow Eric on Twitter at sx.com <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>.