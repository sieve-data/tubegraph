---
title: Function calling and API integration in AI development
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

People are leveraging [[using_ai_to_build_software_applications | AI]] to create voice character applications that are proving to be highly profitable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters" are being touted as the new "apps," representing a significant, often overlooked opportunity for both technical and non-technical individuals <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Voice Chat Applications
Voice chat applications, similar to an audio version of ChatGPT, enable rapid development of engaging tools that can impress both developers and users <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The experience of interacting with a voice-enabled [[using_ai_agents_in_software_development | AI agent]] can be a 10x improvement over text-based interactions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. While some basic coding concepts like GitHub, cloning repositories, and deployment need to be understood, the focus for development can be on configuring the bot's personality and core functionality <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The overarching goal is to inspire users to build their own unique [[using_ai_tools_for_app_functionality_and_innovation | AI-powered applications]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Core Tools and Technologies
Several tools facilitate the creation of these [[integrating_ai_features_in_app_development | AI-powered applications]]:
*   **Cursor** - A code editor that integrates with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily** - A key platform that handles the heavy lifting of voice processing and backend LLM calls <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Daily's "Daily Bots" feature simplifies the process by managing LLM interactions directly <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Pip Cats** - An earlier library by Daily, more developer-focused, for building voice assistants and interfacing with [[tool_and_function_calling_in_ai_development | AI]] <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Next.js** - A React-based framework used for building web applications and defining server-side routes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Vercel** - A platform for deploying Next.js applications online, offering an easy way to host open-source frameworks <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

## Understanding Function Calling
[[tool_and_function_calling_in_ai_development | Function calling]] is a critical concept in enabling [[integrating_ai_tools_in_product_development | AI]] to perform actions beyond generating text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. An LLM's primary output is text, but it can be instructed to output text in a specific format that a surrounding system can interpret as a command to execute a function <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

The process generally involves:
1.  **Speech-to-Text (STT)**: User's audio input is converted into text <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
2.  **LLM Processing**: The text is sent to an LLM (e.g., Llama 3.1 70b via Together AI) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  **Function Call Output**: The LLM, based on its instructions and available tools, outputs a text string indicating a function call (e.g., `<function:get_weather>`) along with parameters (e.g., location) <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
4.  **System Execution**: The Daily bot system detects this specific format and executes the corresponding predefined function on its backend <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
5.  **[[api_usage_in_ai_app_development | API Usage in AI App Development | API Interaction]]**: This function can involve [[api_usage_in_ai_app_development | calling external APIs]] to retrieve data (e.g., weather data) or perform actions <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
6.  **Text-to-Speech (TTS)**: The result from the function call is piped back to the LLM or formatted as text, then converted into audio by a TTS provider, and streamed to the user's browser <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

This entire system abstracts away significant complexity, allowing developers to focus on the assistant's behavior and available tools <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

### Building a Weather Bot Example
A practical demonstration involves creating a "weatherman" character with [[tool_and_function_calling_in_ai_development | function calling]] capabilities to retrieve weather information <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

#### Setup and Configuration
1.  **Clone Repository**: Download the Daily Bots demo repository <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **API Key Integration**: Obtain an API key from the Daily dashboard and paste it into a `.env.local` file to connect the demo to Daily's backend services <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Run Server**: Start the local server using `yarn Dev` and access the application via a local URL <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
4.  **Character Configuration**: Modify the `config` file to define characters, their prompts (personality), and available tools <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   For the weatherman, a `weatherTool` is defined with parameters like `location` <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
    *   The LLM is explicitly informed about these functions and the required response format (e.g., `angle bracket function`) <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
5.  **Function Definition**: In `page.tsx`, the actual code to execute when the [[tool_and_function_calling_in_ai_development | AI]] calls `get_weather` is defined <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. Crucially, the function name (`get_weather`) must align across configurations <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
6.  **API Route**: A Next.js API route (`/api/weather`) is created (`route.tsx`) to simulate fetching weather data. For demonstration, this route returns humorous, "nonsense" weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. This intentional absurdity helps confirm that the [[tool_and_function_calling_in_ai_development | function calling]] is indeed working and not just the AI hallucinating a weather report <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

#### Demonstration
When asked for the weather in New York City, the weatherman bot responds with conditions like "Cloudy Skies, but don't let that fool you, there's a chance of whimsical singing rainbows" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. The server logs confirm that the `/api/weather` route was accessed with the correct location <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.

## Broader Implications and Deployment
The concept of "characters as new apps" presents a massive opportunity for innovation and distribution <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. These can be developed for both B2B and B2C applications, fundamentally changing how users interact with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. Designing characters with unique, shareable responses (e.g., "singing rainbows") can lead to viral "TikTok moments" and free distribution <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.

### Deployment
To make the application publicly accessible, Vercel can be used to deploy the Next.js app <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. After logging into Vercel, a single command (`vercel`) can deploy the application live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

### Advanced Example: Vtuber FaceTime App
An advanced application leveraging these voice [[automation_and_ai_features_in_app_development | AI features]] is a FaceTime-like app that allows users to have personal calls with a "vtuber" (virtual YouTuber) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. Vtubers are content creators who use software to embody virtual avatars, often anime characters, for streaming <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. This app uses Pip Cat, which offers more granular developer control over data flow compared to Daily Bots <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. This demonstrates how, with increasing understanding of [[integration_and_deployment_features_in_ai_coding_tools | AI systems]], developers might choose tools offering greater control <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>.

Historically, building such an application would require a large team and significant capital, but with modern [[using_ai_tools_for_app_functionality_and_innovation | AI tools]], it's possible for individuals to create and launch complex applications <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.