---
title: Creating AI voice character apps with Daily Bots
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

## Introduction to AI Voice Character Apps
People are currently [[using_ai_tools_like_daily_and_pipcats_for_voice_apps | using AI to create voice character apps]] that are generating significant income [00:00:00]. These apps, which function similarly to an audio ChatGPT, allow users to quickly develop impressive applications [00:01:13]. The experience of talking to a voice-driven AI is described as a "10x improvement" over text-based interfaces like ChatGPT [00:01:40].

## The Rise of AI Character Apps
[[emerging_trend_of_ai_character_apps_in_tech_industry | AI character apps]] are seen as the "new apps," representing a significant, often overlooked, opportunity [00:00:13]. The industry is witnessing a trend where engaging consumer apps will likely involve creating characters that perform specific actions or behave in certain ways [00:14:17]. This applies to both B2B and B2C contexts, where characters become a new form of content interaction [00:14:30].

Initially, some believed [[emerging_trend_of_ai_character_apps_in_tech_industry | AI character chat apps]] were a fad, but their retention graphs indicate they are here to stay [00:14:02]. The potential for these characters to go viral through unique or "wacky" responses (like "raining pigs" or "singing rainbows") is also a key consideration for free distribution [00:23:01].

## Tools and Technologies for Building Voice Bots
The process of [[building_apps_with_ai_tools | building apps with AI tools]] can be straightforward, even for those without extensive coding knowledge, though some basic concepts like GitHub or deploying a repository might need to be learned [00:01:55].

Key tools and technologies used include:
*   **Cursor**: A code editor integrated with LLMs to assist with coding [00:03:25].
*   **Daily**: The primary platform for handling voice interactions and backend AI processes. Daily Bots simplify the development by managing LLM calls directly [00:03:36].
*   **Pipcats**: An older library from Daily, more developer-focused, for interfacing with AI and [[voicedriven_ai_applications | building voice assistants]] [00:04:00]. Daily Bots emerged after Pipcats, streamlining the process further [00:04:16].
*   **Next.js**: A framework used for setting up the server and running React applications, which helps in defining routes and pages for the app [00:20:21].
*   **Together AI**: A provider of various AI models, including Llama 3.1 70B, used for the LLM responses [00:08:24].
*   **Vercel**: A platform that allows developers to host their [[implementing_and_deploying_ai_voice_applications_with_nextjs | Next.js]] applications online, making deployment simple with a single command [00:29:21].

## Building an AI Voice Character App: A Tutorial

### Initial Setup and Project Structure
To start, developers can clone a demo repository provided by Daily [00:04:38]. This involves downloading the repository and opening it on your system [00:04:49]. No code needs to be written at this stage [00:05:31].

1.  **Get an API Key**: Sign up for Daily and obtain an API key from their dashboard [00:04:28].
2.  **Configure Environment**: Place the API key into an `.env.local` file within the cloned repository [00:05:13].
3.  **Run the Server**: Use the command `yarn dev` to start the server, which typically runs on a local host URL [00:05:46]. This allows you to interact with the basic setup [00:06:01].

### How the Voice Bot Works
The Daily Bot system orchestrates several processes for voice interaction:
1.  **Speech-to-Text (STT)**: Audio input from the microphone is converted into text by a Speech-to-Text provider [00:10:39].
2.  **LLM Processing**: This text is then fed into an LLM (Large Language Model), such as Llama 3.1 70B from Together AI [00:10:50].
3.  **Text-to-Speech (TTS)**: The LLM's text response is converted back into speech by a Text-to-Speech provider [00:11:00].
4.  **Audio Output**: The generated speech is streamed to the user's browser or device [00:11:09].

Daily handles the complexity of these interactions, including performance and error handling, allowing developers to focus on the assistant's behavior [00:11:14].

### Configuring Character Personality
The personality of the AI character is defined in a configuration file [00:08:40].
*   **Prompts**: Default characters come with preset prompts, such as "You are an assistant called Example Bot, you can ask me anything" [00:10:00].
*   **Customization**: Developers can edit this file to create their own custom characters by adding unique prompts and instructions on how the character should speak [00:12:26].

### Implementing Function Calling
Function calling allows the AI to perform external actions beyond just outputting text, such as calling APIs to get data or make an Instagram post [00:09:15].
*   **How it Works**: The LLM, if sufficiently intelligent, can follow instructions to output a specific text format that triggers a "function call" in the surrounding system [00:16:17]. The LLM itself only outputs text; the system built around it takes that output and executes predefined actions [00:16:55].
*   **Example (Weather Man)**: To create a weather man character, a "weather tool" is defined in the configuration [00:14:57].
    *   The tool is named `get_weather` [00:17:54].
    *   Parameters, like `location`, are specified so the AI knows what information to pass [00:18:11].
    *   The AI model is instructed to respond in a specific format (e.g., `<function> get_weather (...) </function>`) [00:19:02].
    *   In the `page.tsx` file, the actual code execution for the `get_weather` function is defined, typically by calling a route (e.g., `/api/weather`) [00:19:23].
    *   A `route.tsx` file within the `/api/weather` directory specifies what happens when that route is fetched (e.g., generating a "nonsense" weather report with "flying pigs" or "whimsical singing rainbows") [00:20:09].
*   **Testing**: The functionality can be tested by asking the AI character for the weather in a specific location and observing both the AI's response and server logs to confirm the API route was accessed [00:25:55].

### Deployment
Deployment of a [[implementing_and_deploying_ai_voice_applications_with_nextjs | Next.js]] app can be done easily using Vercel [00:29:10].
1.  **Install Vercel CLI**: Install the Vercel command-line interface tool [00:30:04].
2.  **Login**: Log in to your Vercel account via the command line [00:30:44].
3.  **Deploy**: Simply type `vercel` into the command line to deploy the app [00:30:35]. Vercel automatically deploys the app to a live URL, making it accessible on any device [00:31:07].

## Example of a Finished Application
A practical example of a complex [[voicedriven_ai_applications | voice-driven AI application]] is an app that allows users to have a FaceTime call with a vtuber (virtual YouTuber) [00:32:35].
*   **Vtuber Concept**: Vtubers are content creators who use software to embody anime avatars instead of their real faces, popular primarily in Japan [00:32:52].
*   **App Functionality**: This app uses voice APIs (like Pipcats for more developer control) to enable personal calls with AI-driven vtuber characters [00:34:46]. The vtuber models can be acquired from marketplaces like Nzima [00:34:20].
*   **Development**: While not every line of code is written from scratch, the overall app and server architecture are built by an individual developer [00:36:43]. This highlights how modern tools allow small teams or individuals to create sophisticated applications that would have previously required large teams and significant investment [00:36:58].

## Conclusion
The development of [[emerging_trend_of_ai_character_apps_in_tech_industry | AI character apps]] presents a massive opportunity, both for B2B and B2C markets [00:13:06]. With user-friendly tools like Daily and platforms like Vercel, individuals can rapidly [[building_apps_with_ai_tools | build and deploy sophisticated AI voice applications]], transforming creative ideas into functional products [00:01:16].