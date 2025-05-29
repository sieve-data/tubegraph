---
title: Tools for building voice chat apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

People are leveraging AI to create [[creating_ai_voice_character_apps | voice character apps]] that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters" are becoming the new apps <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Building such applications, even a fully working weatherman character app, is achievable for anyone, regardless of technical background <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Core Concepts and Tools

Creating [[voicefirst_technology_and_applications | voice agents and voice AI]] offers an experience that can be 10x more impactful than simply interacting with text-based AI models like ChatGPT <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The process of building these applications has become significantly easier due to the availability of powerful [[using_ai_tools_for_app_functionality_and_innovation | AI tools]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Key tools and technologies used include:
*   **Cursor**: A code editor integrated with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily**: The central platform responsible for the heavy lifting of voice processing and backend operations <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   **Pip Cat**: A library from Daily, focused on developers, that simplifies interfacing with AI to build voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    *   **Daily Bots**: A specific feature by Daily that handles LLM calls, simplifying the process for developers <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Together AI**: A provider of various AI models, including Llama 3.1 70B, used for LLM responses <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Next.js**: A framework that uses React for building websites and allows for server-side code execution via API routes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Vercel**: A platform that enables easy deployment of Next.js applications to the web <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

## Building a Voice Chat App: A Step-by-Step Guide

The process often begins by leveraging existing demo repositories, like Daily's, rather than starting from scratch <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.

### Initial Setup and Configuration
1.  **Clone the Repository**: Download the Daily Bots demo repository to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Connect to Daily Backend**: Obtain an API key from the Daily dashboard and paste it into an `.env.local` file in the project <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This key unlocks Daily's services <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  **Start the Server**: Run the command `yarn Dev` to start the local server <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Understanding the Voice AI Pipeline
The core of the voice chat app involves a sophisticated system:
1.  **Speech-to-Text (STT)**: Daily's system takes audio input from the microphone and converts it into text using an STT provider <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **LLM Processing**: The converted text is sent to an LLM (e.g., Llama 3.1), which processes the input and generates a text response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: Daily then takes the LLM's text response and pipes it to a TTS provider, converting it into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire process, including error handling and performance, is managed by Daily, allowing developers to focus on the character's behavior <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### [[Building and configuring voice agents with Vappy | Configuring Voice Agent Personality and Functionality]]
Daily Bots provides easy [[building_and_configuring_voice_agents_with_vappy | configuration tools]] to change how the bot behaves <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Character Prompts**: The `config` file contains default characters with their prompts, which define their personality and instructions on how to speak <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Developers can easily edit this file to create custom characters <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Function Calling**: This allows the AI bot to interact with external systems or APIs <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
    *   **How it works**: The LLM doesn't execute code directly; it outputs text in a specific format indicating a function call <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. A system built around the LLM then intercepts this output and performs the actual function (e.g., calling an API, making an Instagram post) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
    *   **Implementation**:
        *   Define the tool (function) within the `config` file, specifying its name and parameters (e.g., `location` for a weather tool) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
        *   Ensure the tool's name aligns between the configuration and the code that handles its execution <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
        *   Create an API route (e.g., in Next.js's `pages/api/weather.tsx`) that defines what happens when the function is called <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
        *   For the weatherman example, the API was configured to return whimsical weather conditions like "whimsical singing rainbows" or "flying pigs," which helps validate that the function calling is working when the AI mentions them <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

### Deployment
Once the app is developed, it can be easily deployed using platforms like Vercel:
1.  **Vercel CLI**: Install Vercel's command-line interface tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Deploy Command**: After logging into your Vercel account, simply type `vercel` into the command line, and the app will be deployed live on the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## Applications and Potential

*   **Weatherman App**: A practical demonstration of a voice chat app capable of providing dynamic, albeit humorous, weather reports based on user input <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
*   **Vtuber FaceTime App (Moji)**: A more advanced application allowing users to have a personal FaceTime-style call with an AI-powered virtual character (vtuber) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. This leverages Daily's more developer-focused Pip Cat library for greater control <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. This concept taps into the popularity of vtubers, who are influencers using avatars instead of their real faces <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

These examples highlight the versatility of voice AI in creating engaging and interactive experiences. The "characters as new apps" concept is gaining traction, especially as [[building_social_apps_with_ai | social apps]] evolve <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This represents a significant opportunity for both B2B and B2C applications, fundamentally changing how users [[advanced_voice_notes_and_interactive_media | interact with content]] <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Insights for App Development

*   **Iterative Development**: Focus on making small, understandable changes when building <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. Avoid trying to "one-shot" an entire application, as this limits learning <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.
*   **Leverage Documentation and AI**: Always refer to documentation, and don't hesitate to use AI tools like ChatGPT or Claude to understand complex concepts <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Design for Virality**: When designing characters and their interactions, consider adding unique or whimsical elements (e.g., "raining pigs" or "singing rainbows") that could make the app shareable and gain free distribution <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

The ability to create complex applications, which previously required large teams and significant capital, is now accessible to individuals, making it an exciting time for [[building_and_selling_apps_using_replit_and_chatgpt | building and selling apps]] <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.