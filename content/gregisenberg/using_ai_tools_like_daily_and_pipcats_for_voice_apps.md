---
title: Using AI tools like Daily and Pipcats for voice apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

## Overview
The rapid advancement of AI tools has made it possible for individuals, regardless of their coding experience, to create sophisticated [[voicedriven_ai_applications | voice apps]] and [[creating_ai_voice_character_apps_with_daily_bots | AI voice character apps]] that can generate significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These applications, often referred to as "characters," are seen as a new frontier in app development <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article explores how platforms like Daily and Pipcats facilitate the creation, configuration, and deployment of such [[voicedriven_ai_applications | voice-driven AI applications]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Power of Voice AI
Interacting with [[voicedriven_ai_applications | voice AI]] offers a significantly enhanced user experience compared to text-based AI models like [[using_ai_design_tools_like_midjourney_and_chatgpt | ChatGPT]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The ability to speak to an AI, rather than just type, provides a 10x improvement in engagement <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This immersive quality is driving a trend where AI characters become highly retentive and engaging consumer (and B2B) apps <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

## Key AI Tools for Voice Apps

### Daily
Daily is a core platform that handles the heavy lifting for voice and backend processes in [[voicedriven_ai_applications | voice chat apps]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Its feature, [[creating_ai_voice_character_apps_with_daily_bots | Daily Bots]], simplifies the process by managing Large Language Model (LLM) calls, allowing developers to focus on configuring bot behavior <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

**Setup and Functionality:**
1.  **Dashboard and API Key:** Users sign up for Daily and obtain an API key from their dashboard <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Repo Cloning:** A demo repository is provided, which can be cloned (downloaded) to the user's system <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
3.  **API Key Integration:** The Daily API key is pasted into a local environment file (`.env.local`) within the cloned project <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Server Startup:** The application server is started with a single command (`yarn dev`) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

**Voice Processing Pipeline:**
Daily Bots orchestrates a complex sequence to enable real-time voice interaction <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT):** Audio input from the user's microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing:** This text is sent to an LLM (e.g., Llama 3.1 70B via Together AI) for generating a response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS):** The LLM's text response is then converted back into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output:** The generated speech is streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily handles the underlying complexity of performance and error management, allowing creators to focus on the character's persona and functionality <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Pipcats
Pipcats is an earlier library from Daily that is more focused on developers, providing greater control over the AI interface <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. While Daily Bots abstracts away some complexity, Pipcats offers more granular control for developers who need to manage data flow and system interactions in detail <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.

## Building Voice Characters

### Ideation and Configuration
The core idea is that [[creating_ai_voice_character_apps_with_daily_bots | characters are the new apps]], offering a huge opportunity for creators to ideate and launch unique personalities <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Personality Prompts:** Character behavior is configured through simple prompts, such as "You are an assistant called Example Bot, you can ask me anything" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Voice Customization:** Users can easily change the voice of their AI character <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Character Creation:** New characters can be added simply by editing a configuration file, instantly making them available in the application <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Function Calling (Tools)
[[incorporating_ai_features_in_applications | Incorporating AI features in applications]] via function calling allows voice bots to interact with external systems and perform actions <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Concept:** An LLM outputs text, and a surrounding system interprets that text to trigger specific functions, like calling APIs to fetch data or make posts <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. The LLM itself only outputs text; the external system acts on it <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Implementation:**
    1.  **Define the Tool:** A tool (e.g., `get_weather`) is defined with a unique name and parameters (e.g., `location`) in a configuration file <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. This instructs the AI on available functions and their expected inputs <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    2.  **System Action:** A `page.tsx` file (in a [[implementing_and_deploying_ai_voice_applications_with_nextjs | Next.js]] environment) defines what happens when the AI calls the tool, such as making an API request to a specific route (`/api/weather`) <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
    3.  **API Route Logic:** A corresponding API route (e.g., `api/weather/route.tsx`) contains the actual code to perform the function, such as generating a weather report <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
*   **Viral Elements:** When [[building_apps_with_ai_tools | building apps with AI tools]], incorporating unexpected or "wacky" responses (like "whimsical singing rainbows" or "flying pigs") into function calls can create shareable "TikTok moments" and provide free distribution for the character <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

## Deployment with Vercel
[[implementing_and_deploying_ai_voice_applications_with_nextjs | Implementing and deploying AI voice applications with Next.js]] for web access is streamlined using Vercel. Vercel, the company behind Next.js, provides a platform to host [[implementing_and_deploying_ai_voice_applications_with_nextjs | Next.js]] applications online <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. After logging into Vercel via its command-line interface (CLI), an app can be deployed live to the internet with a single `vercel` command <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This ease of deployment allows creators to quickly share their [[voicedriven_ai_applications | voice apps]] with friends and users <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## Real-World Examples
*   **Weatherman App:** A fully functional weatherman character app was created using these tools, capable of providing whimsical weather forecasts <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **VTuber FaceTime App:** An application was developed to allow users to have a personal FaceTime call with a VTuber (a virtual avatar streamer), leveraging [[voicedriven_ai_applications | voice AI]] and bought anime models <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. This app used Pipcats for greater developer control <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. This demonstrates the potential for [[using_ai_in_mobile_apps | mobile apps]] and advanced, engaging experiences.

## Development Philosophy
When [[building_apps_with_ai_tools | building apps with AI tools]], especially for beginners, it's crucial to make small, understandable changes and build iteratively upon existing demos or repositories <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. While AI can generate large amounts of code quickly, understanding the underlying file structure and how components route together is vital for effective learning and development <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. The age of AI enables individuals to build complex systems that previously required large teams and significant capital <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.