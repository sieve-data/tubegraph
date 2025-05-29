---
title: Designing characters as the new apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

Character-based applications, particularly [[creating_ai_voice_character_apps | AI voice character apps]], are emerging as a significant new frontier in app development. These "characters are the new apps" and are observed to be "printing money" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The shift towards character apps presents a substantial opportunity for both technical and non-technical individuals <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Why Characters are the New Apps

The development of voice chat apps, conceptualized as "audio ChatGPT" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, offers a significantly enhanced [[user_experience_design_for_apps | user experience]] compared to text-based AI interactions, described as a "10x Improvement" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This sector is gaining traction, with observations from the tech scene suggesting that AI character chat apps are not a fad due to high user retention <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a> <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. It is posited that the future of engaging consumer and non-consumer apps will involve creating characters that act in specific ways <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a> <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. This applies to both B2B and B2C contexts, representing a new form of content interaction <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a> <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.

## Tools for [[creating_ai_voice_character_apps | AI Voice Character Apps]]

The process of building these applications leverages several modern [[ai_app_development | AI app development]] tools:

*   **Cursor**: A code editor integrated with large language models (LLMs) for coding assistance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Daily.co**: A company that provides the core backend for voice interactions and handles LLM calls, simplifying the process for developers <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Pip Cat**: A library, focused on developers, that facilitates easier interfacing with AI for building voice assistants <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>. Daily Bots built on Pip Cat simplifies the process further by handling LLM calls directly <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Next.js**: A framework that uses React for building websites and allows for server-side code execution through "routes" <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a> <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   **Vercel**: A platform that enables easy hosting and deployment of Next.js applications online <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a> <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>.
*   **Together AI**: A provider of various AI models, including Llama 3.1 70B, used for LLM responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a> <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## Building a Voice Character App: A Tutorial Overview

Creating a voice character app, such as a fully working weatherman character app <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, involves several key steps:

### Initial Setup
The foundational step involves downloading a demo repository, such as Daily's demo which runs in the browser <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a> <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This process typically involves:
*   **Cloning the repository**: Downloading the demo code to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Obtaining an API Key**: Signing up for a service like Daily and acquiring an API key to access its services <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This key is placed in an `.env.local` file <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Running the Server**: Starting the local server with a command like `yarn dev` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, which makes the app accessible via a local host URL <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Configuring Personality and Voice
A core aspect of character [[user_experience_design_for_apps | user experience design]] is defining its personality and voice:
*   **Configuration File**: The bot's behavior is managed through a configuration file that makes it easy to change how the bot behaves <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Prompts**: Character personalities are defined using prompts, which are instructions given to the LLM. For example, a default prompt might be "You are an assistant called example poot. You can ask me anything" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a> <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Custom characters can be created by simply editing this file <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Voice**: The choice of voice is crucial for the bot's character <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. The system internally converts speech to text (STT) for the LLM, and then converts the LLM's text response back to speech (TTS) for the user <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a> <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

### Adding Interactivity with Function Calling
To enable characters to "do stuff" beyond just talking, [[ai_app_development | AI app development]] incorporates function calling:
*   **Concept**: Function calling allows an LLM to understand what a function is and how to call it, enabling the system around the LLM to perform actions based on the text output <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a> <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. The LLM itself only outputs text; the external system acts upon it <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a> <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Implementation**: A "tool" (function) is defined for the LLM, specifying its name and any necessary parameters, such as a `location` for a weather tool <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a> <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The AI is trained to respond in a specific format (e.g., `<angle bracket function>`) that Daily's backend recognizes as a function call <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a> <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   **API Integration**: When the AI "calls" a function, it triggers an action on the server. For the weatherman example, this involves calling a specific API route (e.g., `/api/weather`) <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a> <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. The server then executes code to fetch data, like weather conditions, and returns it to the AI for verbalization <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

### Deployment
Once an app is built, it can be deployed to the web:
*   **Vercel**: Next.js apps can be hosted online using Vercel, which provides a straightforward command-line interface (CLI) tool for deployment <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a> <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
*   **Simple Deployment**: After logging into a Vercel account, a single command (`vercel`) can deploy the app live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a> <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>. This allows users to access the character app on any device via a URL <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

## Key Insights for [[user_experience_design_for_apps | User Experience Design]] and Virality
When designing characters, consider strategies to maximize engagement and virality:
*   **Small, Understandable Changes**: When starting out, it's beneficial to make small, incremental changes to existing demo code rather than attempting to build an entire application from scratch <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a> <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.
*   **Viral Moments**: Incorporate unexpected or humorous elements into character responses. For example, programming a weatherman to report "whimsical singing rainbows" or "flying pigs" can create "TikTok moments" that encourage users to screen-capture and share the experience, leading to free distribution <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a> <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a> <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.
*   **Beyond Web**: While web-based apps are demonstrated, character apps can also be developed as [[aidriven_ios_app_prototyping | iOS apps]] <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.

## Advanced Examples

A more advanced example of a character app is one that enables a FaceTime-like call with a VTuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a> <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>. VTubers are content creators who stream using digital avatars, often anime characters <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a> <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>. This app allows for personal interaction with an AI-powered VTuber, using tools like Pip Cat for greater developer control <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a> <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

Historically, developing such an application would require a large team and significant capital <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. However, with the current tools and advancements in [[ai_app_development | AI app development]], individuals can create complex and engaging character-based applications independently <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.