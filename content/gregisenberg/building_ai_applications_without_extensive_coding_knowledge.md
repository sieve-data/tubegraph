---
title: Building AI applications without extensive coding knowledge
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

People are leveraging AI to create voice character applications that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters" are described as the new applications, and the process of [[building_apps_using_ai_tools | building apps using AI tools]] is accessible to both technical and non-technical individuals <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. What might appear as a simple "toy" can evolve into a successful startup, as many impactful startups begin with a toy-like appearance <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

This guide explores how to build these voice chat applications, often referred to as "audio ChatGPT," with a focus on ease of setup and configuration rather than deep coding <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## What You'll Learn <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

This tutorial demonstrates:
*   The power and speed with which these AI tools can be utilized <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The 10x improvement in user experience when interacting with a voice-enabled AI compared to a text-based one <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   How to configure a bot's personality and integrate functions <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   The fundamental concept that "characters are the new apps" <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

While some basic concepts like GitHub, cloning repositories, and deployment are useful to understand, the core focus is on the exciting aspects of getting a bot running and customizing it <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Tools and Platforms Used <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>

*   **Cursor**: A code editor integrated with large language models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily**: A company providing the backend for voice and AI integration, handling heavy lifting like LLM calls <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   **Daily Bots**: A specific product by Daily that simplifies the process by handling LLM calls directly <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   **Pipcat**: Another library by Daily, more focused on developers, offering greater control for building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.
*   **Together AI**: A provider of AI models; specifically, Llama 3.1 70B was used for the LLM in the demonstration <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Next.js**: A framework for building websites that allows for setting up a server running React and defining routes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Vercel**: The company that created Next.js, also provides a platform to host Next.js applications online easily <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

## Building a Voice Character App – A Walkthrough

The process begins with using the Daily platform and its demo repository <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Initial Setup <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

1.  **Clone the Repository**: Download the demo code to your system <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This means no code needs to be written at this stage <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Sign Up for Daily and Get an API Key**: Obtain an API key from the Daily dashboard <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Connect the Demo**: Paste the API key into the `.env.local` file in the cloned repository to unlock Daily's services <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
4.  **Run the Server**: Execute `yarn Dev` to start the server <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
5.  **Access Locally**: Navigate to the local host URL to see the demo running in your browser <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### How the Voice AI System Works <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>

The Daily bot system handles the complex pipeline for voice interaction <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT)**: Audio input from the microphone is converted into text by an STT provider <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: This text is fed into the LLM (AI model), which processes it and generates a response as text <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: The LLM's text response is then converted into speech by a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is streamed back to your browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily abstracts away the complexity of managing performance, errors, and the entire system, allowing developers to focus on the bot's functionality and personality <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Configuring Character Personality <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>

The bot's behavior is controlled via a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Prompts**: The file contains default prompts like "You are an assistant called example poot," along with instructions on how the bot should speak for correct audio output <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Customization**: Users can easily edit this file to change existing characters or add new ones <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This direct control over the configuration file allows for rapid iteration and personalization of the AI character <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

### [[function_calling_and_tool_integration_in_ai_apps | Function Calling and Tool Integration]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>

[[function_calling_and_tool_integration_in_ai_apps | Function calling]] enables an AI model to interact with external systems and perform actions beyond just outputting text <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **How it Works**: An LLM, if sufficiently intelligent, can understand instructions to call a function. The AI itself only outputs text (e.g., specifying a function to call and its parameters), but the system built around it takes this output and executes the actual code (e.g., calling an API, getting data, making a post) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a> <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Implementing a Weather Tool**:
    1.  **Define the Tool**: In the `config` file, define the tool's name (e.g., `get_weather`) and describe the parameters it accepts (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. This teaches the AI how to use the tool <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
    2.  **Handle the Call**: In `page.tsx`, specify what happens when the AI "calls" the function, which in this case involves making an API call to a defined route <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. Crucially, the function name here must align with the one defined in the config <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
    3.  **Implement the API Route**: In Next.js, an API route (e.g., `api/weather`) is created (`route.tsx`) to contain the actual logic that fetches or generates weather data <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
    *   **Demonstration**: A "weatherman" character was created that, when asked for the weather, would call this function. For humorous demonstration, the API was configured to return "nonsense" weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a> <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. This also served as a clear validation that the [[function_calling_and_tool_integration_in_ai_apps | function calling]] was working as intended <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

## Deployment <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>

[[tools_and_platforms_for_ai_app_development | Tools and platforms for AI app development]] like Vercel make it extremely easy to deploy Next.js applications <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.
*   **Vercel CLI**: After logging into your Vercel account, a single command (`vercel`) can deploy your application live to the internet <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
*   **Accessibility**: Once deployed, the app is accessible via a URL on any device <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.

## Example of a Finished Product: Vtuber App <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>

An example of a more advanced [[building_apps_using_ai_tools | AI application built using AI tools]] is an app that enables FaceTime calls with a "vtuber" <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.
*   **Vtubers**: Content creators who stream using a digital avatar instead of their real face, often anime characters, extremely popular in Japan and globally <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.
*   **App Concept**: The app leverages voice APIs to create a personal, interactive FaceTime experience with a vtuber, which is typically not possible with traditional influencer interactions <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.
*   **Technology**: This app uses Pipcat instead of Daily Bots, as it provides more control for developers to manage data flow <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. The vtuber model itself was purchased from a marketplace called "Nzima" <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.
*   **Significance**: This demonstrates that complex voice-enabled AI applications, which would have required a large team and significant capital years ago, can now be developed by an individual with accessible tools <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>. This highlights the potential for individuals to be [[building_ai_startup_using_ai_tools | building AI startups using AI tools]] or [[building_businesses_with_ai_tools | building businesses with AI tools]] independently <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

## [[tips_for_developers_using_ai_in_app_development | Tips for Developers Using AI in App Development]] <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>

*   **Small, Understandable Changes**: When starting out, make small, incremental changes to your code. This helps in understanding how different components interact and avoids getting lost in complex AI-generated code <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   **Build Off Existing Demos**: Instead of starting from scratch, leverage existing demo repositories. This provides a solid foundation and allows you to focus on adding custom features <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.
*   **Characters as New Apps**: Recognize the huge opportunity in ideating and launching AI characters. This is an emerging trend with significant potential for engagement and retention in both B2C and B2B contexts <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a> <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Documentation and AI Assistance**: Develop the habit of reading documentation. For anything you don't understand, ask AI models like ChatGPT or Claude <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Think Viral**: When designing characters, consider adding constraints or unique elements that could lead to "TikTok moments" – content that encourages users to screen record and share, leading to free distribution <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.