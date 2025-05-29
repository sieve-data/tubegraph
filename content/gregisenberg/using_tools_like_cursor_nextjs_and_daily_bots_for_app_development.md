---
title: Using tools like Cursor Nextjs and Daily Bots for app development
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The advent of [[ai_tools_for_app_development | AI tools]] has enabled individuals, regardless of their technical background, to create "voice character apps" that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters are the new apps," a concept not widely discussed but offering immense opportunity <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. One example created during an episode was a fully functional "weatherman" character app <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Core Tools for Development

Building these voice chat apps, conceptualized as an "audio Chat GPT," involves leveraging powerful, readily available tools <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The process is streamlined, allowing rapid development of impressive applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

The main tools used in this process include:

*   **[[using_ai_tools_like_cursor_and_claude_for_development | Cursor]]**: This serves as the code editor, integrated with Large Language Models (LLMs) to assist with coding tasks <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily and Daily Bots**: This company's platform is the central component for handling voice capabilities and backend processes <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Daily Bots simplifies the development process by managing LLM calls directly, requiring developers only to sign up, obtain an API key, and configure the bot's personality <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Next.js**: The underlying framework used for building these applications, allowing for both client-side and server-side code execution <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Pip Cats**: An alternative library focused on developers, offering more direct control over interfacing with AI and building voice assistants, suitable for those desiring more customization than Daily Bots <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.
*   **Together AI**: A provider for AI models, such as Llama 3.1 70b, which serves as the LLM (Large Language Model) for the bots <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Vercel**: A platform that enables hosting and deploying Next.js applications online with minimal effort, often requiring just one command <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>, <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>.

## Building a Voice Character App

The process begins by cloning a demo repository provided by Daily, essentially downloading the code to a local system <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The next step involves connecting the demo to the Daily backend by obtaining an API key and pasting it into a `.env.local` file <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Running the command `yarn dev` starts the server locally <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Understanding the Bot's Architecture

The core of a voice character app involves a sophisticated system:
1.  **Speech-to-Text (STT)**: Audio input from the microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: This text is then fed into an AI model (LLM), which processes it and generates a text response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: The LLM's text response is converted back into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: This speech is then streamed to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire system, including performance and error handling, is largely managed by Daily, removing significant development complexity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Customizing Characters and Functionality

Users can configure the bot's personality and behavior through a configuration file, which includes default prompts for characters <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. The character selection screen directly reflects this file, allowing for easy creation and modification of character names and prompts <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

The concept of "characters as the new apps" presents a significant opportunity for ideation and launching <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

Function calling allows the voice bot to perform actions beyond just responding with text. It involves defining tools and parameters for the LLM to understand and utilize <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. For example, a "weather tool" can be defined with parameters like "location" <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>, <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. The LLM is instructed to respond in a specific format (e.g., `<function>...`) that Daily's backend recognizes to trigger the corresponding function <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>, <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

### The Weather Man Example

In the weather man demonstration, the function `get_weather` is called. However, instead of providing actual weather data, the backend is configured to return humorous, nonsensical weather conditions like "Whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>, <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>, <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. This intentional design serves both as a clear validation that the function calling is working (by observing the AI's response) and as a way to create "TikTok moments" that could lead to viral distribution <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>, <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

![[ai_tools_for_building_software | Using AI tools for building software]] allows for rapid iteration and experimentation <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. It's crucial to make small, understandable changes rather than attempting to "one-shot" an entire application using a single prompt <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. Building upon existing demos or repositories, like the one provided by Daily, is an effective learning strategy <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

### Deployment

Once developed, these web-based applications can be deployed online using platforms like Vercel. Vercel, created by the same company behind Next.js, offers an easy way to host Next.js apps, allowing them to be accessible via a URL on any device <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>, <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>, <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.

## An Advanced Application: The vTuber App

An example of a more complex application built using similar voice-enabled AI technologies is a vTuber (virtual YouTuber) app <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. This app allows users to have a FaceTime-like call with an AI-powered vTuber avatar, purchased from marketplaces like "nzima" <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>. This particular application uses Pip Cat for more granular control over data flow compared to Daily Bots <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.

> "A few years ago... you would need a large team to do that, raise Venture Capital. Here you are, you know, in a room wearing a hoodie, throwing out apps characters." <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>

The development of such sophisticated applications, which were not even possible a few years ago, can now be achieved by individuals, showcasing the power of current [[leveraging_ai_and_automation_in_app_development | AI and automation in app development]] <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.