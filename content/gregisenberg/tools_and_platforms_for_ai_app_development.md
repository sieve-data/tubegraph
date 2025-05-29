---
title: Tools and platforms for AI app development
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The current landscape of AI tools allows individuals, regardless of their technical background, to quickly develop sophisticated [[building_apps_using_ai_tools | AI-powered applications]], particularly voice character apps <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "character apps" are considered the new form of applications <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Core Development Tools

Developers can leverage a suite of tools and platforms to streamline the creation of AI apps:

### Cursor (Code Editor)
Cursor is a code editor that integrates with large language models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Daily
Daily is a company that provides tools for building voice AI applications <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. It handles much of the heavy lifting for voice and backend processes <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, including the complexities of speech-to-text (STT) and text-to-speech (TTS) conversions, performance, and error handling <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

*   **Daily Bots**: A specific library within Daily that simplifies the process by handling LLM calls directly, allowing developers to focus on configuring bot behavior <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. To use Daily Bots, users sign up, obtain an API key, and integrate it into their project's `.env.local` file <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Pip Cat**: Another library provided by Daily, more focused on developers, offering greater control over interfacing with AI and building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. This is suitable for those who understand how these systems work and desire more customization <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>.

### Together AI
Together AI is a provider of AI models, such as Llama 3.1 70B, which can be specified for use within Daily's backend for AI responses <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Next.js (Web Framework)
Next.js is a framework that utilizes React to build websites and allows for setting up servers to run code through specific routes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

### Vercel (Deployment Platform)
Vercel, the creator of Next.js, provides a platform to host Next.js applications online <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. Deployment is simplified, often requiring only one command (`vercel`) after logging in <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>, <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.

## Key Concepts and Processes

### Voice Chat Apps
These applications enable audio conversations with AI characters, similar to an "audio ChatGPT" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Users can create a variety of voice apps, such as a fully working weatherman character app <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, or even a virtual "FaceTime" call with a Vtuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.

### AI Backend Process
The typical flow for a voice AI character app involves:
1.  **Speech-to-Text (STT)**: Audio input from a microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: The text is fed into an LLM (AI model) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The LLM processes the input and outputs its response as text <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
3.  **Text-to-Speech (TTS)**: Daily takes the LLM's text response and pipes it into a TTS provider to convert it into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is then streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Character Configuration
The personality and behavior of the AI bot are configured through a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This includes defining prompts (e.g., "You are an assistant called Example Poot") and instructions on how to speak <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Pre-set characters are available, but developers can easily create custom characters by editing this file <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>, <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### [[function_calling_and_tool_integration_in_ai_apps | Function Calling and Tool Integration]]
Function calling allows an LLM to interact with external systems and APIs, enabling it to "do stuff" beyond just outputting text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

*   **Mechanism**: The LLM, if smart enough, understands instructions to output text in a specific format indicating a function call <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. The external system (like Daily's backend) then takes this structured text output and executes the corresponding code or API call <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. The AI itself does not *do* anything directly; it only outputs text <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Implementation**: This involves defining the tool for the LLM (e.g., a "weather tool" with a specific name like `get_weather`) and specifying parameters (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>, <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. The system then defines what actions happen when the AI "calls" that function, typically by fetching a route that contains the logic for that function <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

## [[tips_for_developers_using_ai_in_app_development | Tips for Developers Using AI in App Development]]

*   **Focus on the "Cool Stuff"**: With tools handling the underlying AI complexity, developers can concentrate on configuring personality and behavior <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Leverage Documentation and LLMs**: It's crucial to develop the habit of reading documentation <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. If something isn't understood, consult LLMs like ChatGPT or Claude <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Small, Understandable Changes**: When starting out, build off existing demos or repositories and make small, incremental changes. This helps in understanding how different components integrate <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>, <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.
*   **Design for Virality**: When creating characters, consider adding constraints and unique elements (e.g., "whimsical singing rainbows" for weather) that could create "TikTok moments" and generate free distribution <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>, <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.

## Examples of AI Apps

### Weatherman Character App
A fully working weatherman character app was built as a demonstration, capable of providing weather reports, even whimsical ones like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>, <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. This showcases the ease of integrating function calling to fetch external data and have the AI narrate it <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Vtuber FaceTime App (Moji)
An example of a more advanced application is Moji, an app allowing users to have a personal "FaceTime" call with an AI-powered Vtuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. This app utilizes Daily's Pip Cat library for greater developer control <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. Such applications leverage AI to create highly retentive and engaging consumer experiences <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

The development of these applications, once requiring large teams and venture capital, can now be achieved by individuals due to advancements in AI tools <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.