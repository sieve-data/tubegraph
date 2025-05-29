---
title: Function calling in AI voice apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

AI voice applications can extend their capabilities beyond simple conversational responses by utilizing "function calling" or "tool calling" <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This advanced feature allows an AI agent to interact with external systems, perform actions, and retrieve specific data <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Understanding Function Calling
At its core, a large language model (LLM) primarily takes in text and outputs text <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. It cannot directly perform actions outside of its text-based domain <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Function calling bridges this gap by enabling the system *around* the AI to interpret the LLM's text output as a command to execute a predefined function <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

The process involves:
1.  **AI Understanding Instructions**: The LLM is designed to understand what a function is, how to call it, and what parameters it requires <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
2.  **Structured Output**: The AI outputs a specific text format that indicates it wants to call a function, including the function's name and any necessary arguments <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
3.  **System Execution**: The application's backend system monitors for these structured outputs. When detected, it executes the corresponding real-world function, such as calling an external API to get data <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.
4.  **Result Integration**: The result from the function call is then fed back to the LLM, which uses this information to formulate a natural language response to the user <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

## Implementing Function Calling with Daily Bots
A practical example of [[tool_and_function_calling_in_ai_applications | embedding AI to enhance app functionality]] involves using Daily Bots, a platform that simplifies the creation of AI-powered voice applications <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Daily Bots handles the complex backend operations, including speech-to-text (STT) conversion, LLM calls, and text-to-speech (TTS) synthesis <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

### Setup and Configuration
To get started with [[building_and_configuring_voice_ai_agents | building and configuring voice AI agents]]:
*   **Daily API Key**: Users sign up for Daily and obtain an API key, which authenticates access to Daily's services <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Repo Cloning**: A demo repository provided by Daily can be cloned (downloaded) locally. This repository contains the basic structure for a voice character app <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Environment Variables**: The Daily API key is placed into a `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Running the Server**: A simple command, `yarn dev`, starts the local server, making the app accessible in a web browser <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Defining a Weather Function
The example of a "weatherman" character demonstrates function calling <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>:
1.  **Tool Definition**: Within the `config` file, a "weather tool" is defined. This definition includes:
    *   A unique `name` for the tool (e.g., `get_weather`) <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
    *   A `description` of what the tool does <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   `parameters` that the tool requires, such as `location` for a weather lookup <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
2.  **AI Instruction**: The AI model (e.g., Llama 3.1 70B via Together AI) is instructed on how to respond when it needs to call this function <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. Daily's system expects a specific format (e.g., starting with `<function>` tags) <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
3.  **Function Execution**: In the `page.tsx` file, the actual logic for handling the function call is defined <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. When the AI outputs the `get_weather` command, the system calls an API route (e.g., `/api/weather`) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
4.  **Backend Route**: Using Next.js, an API route (`/api/weather/route.tsx`) is set up to receive the function call <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. For demonstration purposes, this route might return humorous, non-real weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. This also serves as a clear validation that the function call was successful <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### Deployment
Once developed, a voice character app can be deployed to the web. Platforms like Vercel, which created Next.js, make this process straightforward <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. A simple command like `vercel` can deploy the application live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This allows users to share their [[voicefirst_interfaces_and_applications | voice-first applications]] and "characters" with others <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## Impact and Future of AI Characters
The ability to incorporate function calling transforms AI characters from simple chatbots into interactive agents that can perform real-world tasks <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This capability opens up significant opportunities for [[developing_ai_character_apps_with_customization | innovative AI functionalities in apps]], leading to what some consider "characters as the new apps" <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

Instead of needing large teams and significant capital, individuals can now develop and launch sophisticated AI character apps, leveraging existing tools and frameworks <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>. This trend is observed in various sectors, from consumer-facing social apps to business-to-business (B2B) applications <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. The focus shifts to ideating compelling characters and their unique functionalities <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. For example, a developer can create an app allowing users to have a personal video call with a [[using_ai_to_create_voice_character_apps | virtual character]] that can answer questions and interact dynamically <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.