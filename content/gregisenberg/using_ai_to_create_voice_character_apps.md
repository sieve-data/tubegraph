---
title: Using AI to create voice character apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The landscape of applications is evolving, with AI-powered voice character apps emerging as a significant new frontier. These innovative applications are gaining traction, with some already "printing money" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The core idea is that "characters are the new apps" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, presenting a huge opportunity for both technical and non-technical individuals <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Rise of Voice Character Apps
[[Voicefirst interfaces and applications | Voice chat apps]], like audio ChatGPT, enable users to interact with AI through speech <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The experience of talking to an AI is described as a "10x improvement" over text-based interactions like ChatGPT <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This emerging area offers an exciting and relatively easy way to [[building_apps_with_ai_tools | build apps with AI tools]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

Nikita Bier has noted that while he initially considered AI character chat apps a fad, retention graphs indicate they are here to stay <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. This suggests that the future of highly retentive and engaging consumer (and non-consumer) apps will likely involve [[developing_ai_character_apps_with_customization | creating AI characters]] that perform specific functions or act in certain ways <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

## Key Tools and Technologies
[[Building and Configuring Voice AI Agents | Building and configuring voice AI agents]] is made accessible through various modern tools:

*   **Code Editor**: **Cursor** is an example of a code editor that integrates with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Voice AI Backend**: **Daily** is a core service that handles the heavy lifting for voice and backend operations <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. They released **Daily Bots**, which abstracts away LLM calls, allowing developers to focus on configuration <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **LLM Provider**: **Together AI** provides a range of AI models, such as Llama 3.1 70b, which can be used by Daily's backend <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Development Framework**: **Next.js** is a framework that uses React to build websites and allows for server-side code execution <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Deployment Platform**: **Vercel** is a platform that simplifies hosting Next.js apps online with minimal commands <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

## How Voice AI Applications Function
The process of a voice AI application involves several steps <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT)**: The Daily Bot system takes audio input from the microphone and converts it into text using an STT provider <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **LLM Processing**: The converted text is sent to an LLM (AI model), which processes the input and generates a text response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: Daily takes the LLM's text response and converts it into speech using a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is then streamed back to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily handles the underlying complexity of performance and error handling, allowing developers to focus on the assistant's behavior and functionality <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Building a Simple Voice Character App (Weatherman Example)

A fully working weatherman character app can be created using these tools <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Initial Setup
1.  **Clone the Repository**: Start by downloading the Daily Bots demo repository to your system <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Connect to Backend**: Obtain an API key from the Daily dashboard and paste it into the `.env.local` file to connect the demo to the Daily backend <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Run Locally**: Start the local server with a simple command like `yarn Dev` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Customizing Characters
The "personality" of the bot is configured through a configuration file <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This file contains "prompts" that instruct the LLM on how to behave, such as "You are an assistant called example poot" and instructions on speaking correctly for audio output <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. Pre-built characters are available, but users can easily [[developing_ai_character_apps_with_customization | customize their own characters]] by editing this file <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### [[Function calling in AI voice apps | Function Calling]]
[[Function calling in AI voice apps | Function calling]] allows the AI to perform external actions <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Concept**: An LLM typically only outputs text <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. [[Embedding AI to enhance app functionality | To enhance app functionality]], a system must be built around the LLM to interpret its output and perform actions <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Function calling enables an LLM to understand instructions and output responses in a format that the surrounding system can then use to "do stuff" <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>, such as calling APIs, getting data, or making an Instagram post <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

*   **Implementing a Weather Tool**:
    *   **Define the Tool**: Add a "weather tool" in the configuration, defining its name (e.g., `get_weather`) and parameters (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
    *   **Instruction to AI**: The AI model needs to be instructed on the format for calling functions <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. Daily waits for a specific message format (e.g., `<angle bracket function>`) to understand the AI is trying to call a function <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
    *   **Define Action**: In the `page.tsx` file, define what happens when the AI "calls" the `get_weather` function, typically by calling an API route <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
    *   **API Route Logic**: In the `api/weather/route.tsx` file, implement the server-side logic for the weather API. For demonstration, this could return humorous or "nonsense" weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. This intentional absurdity can make the app more likely to go viral if users record and share their interactions <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Deployment
To make the app live and accessible to others:
1.  **Install Vercel CLI**: Use Vercel's command-line interface tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Deploy**: Log in to your Vercel account via the CLI and simply type `Vercel` to deploy the application <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. Vercel then handles the build and hosting, providing a live URL <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>.

## Advanced Application: The Vtuber App
A more complex example of an [[innovative_ai_functionalities_in_apps | innovative AI functionality in apps]] is a FaceTime-like app with a vtuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. Vtubers are content creators who use software to embody virtual avatars, often anime characters, for streaming <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>.

This app allows users to have personal calls with an AI-powered vtuber avatar <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. Instead of Daily Bots, this app uses the **Pip Cat** library for more granular developer control over data flow <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>. The avatar models can be acquired from marketplaces like Nzima <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

## Opportunities and Takeaways
*   **Ease of Entry**: Even without extensive coding knowledge, individuals can pick up the necessary concepts and [[building_apps_with_ai_tools | build apps with AI tools]] quickly <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Rapid Development**: These tools enable rapid prototyping and deployment <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Focus on Small Changes**: When starting, it's beneficial to build upon existing demos and make small, understandable changes rather than attempting to build entire apps from scratch <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.
*   **Massive Opportunity**: The concept of "characters as the new apps" represents a significant, largely untapped market <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Versatility**: These apps can be developed for web platforms and even converted into [[building_ios_apps_with_ai | iOS apps with AI]] <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.
*   **Accessibility**: What previously required large teams and venture capital can now be accomplished by individuals using readily available tools <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
*   **B2B and B2C Potential**: AI voice characters are poised to become a new form of interaction with content, applicable across both business-to-business and business-to-consumer sectors <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   **Viral Potential**: Strategic inclusion of unique or humorous responses can lead to organic sharing and "free distribution" <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.