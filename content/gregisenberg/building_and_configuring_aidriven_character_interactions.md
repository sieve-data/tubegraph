---
title: Building and configuring AIdriven character interactions
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

AI is being utilized to create voice character applications, with some proving to be highly profitable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters are the new apps," representing a significant, often overlooked, opportunity <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Even non-technical individuals can leverage these tools <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Why AI-Driven Characters?
The experience of interacting with voice AI is a significant improvement over text-based AI like ChatGPT, offering a "10x improvement" in experience <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. These tools allow for rapid development of impressive applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. The core idea is to think of characters as the next generation of applications, presenting a vast opportunity for ideation and launching new products <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This trend extends to both B2B and B2C sectors, fundamentally changing how we interact with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Tools and Setup
The primary tools used in this process include:
*   **Cursor**: A code editor integrated with large language models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **[[creating_ai_voice_character_apps_with_daily_bots | Daily (Daily Bots)]]**: This company provides the core technology for voice and backend processing <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Daily Bots simplifies the process by handling LLM calls, requiring users only to sign up and obtain an API key from their dashboard <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Pip Cats**: An earlier Daily library focused on developers, making it easier to interface with AI and build voice assistants <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. While Daily Bots abstracts much of the complexity, Pip Cats offers more control for developers <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

### Initial Setup Steps:
1.  **Clone the Repository**: Download the Daily Bots demo repository to your system <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Obtain API Key**: Sign up for Daily and get your API key from their dashboard <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Configure API Key**: Place the API key in the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Start the Server**: Run a single command (e.g., `yarn Dev`) to start the server <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
5.  **Access Locally**: Navigate to the local post URL in your browser to see the demo running <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

At this stage, no code has been written; it's purely a setup process of downloading the repository, signing up for the service, pasting a key, and running a command <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Understanding Character Configuration
The core of defining an AI character's personality and behavior lies in a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Daily Bots abstracts away the complex AI mechanics, offering simple configuration tools <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Key Configuration Elements:
*   **Prompts**: The initial instructions given to the LLM define the character's role and speaking style <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. For example, a default prompt might be "You are an assistant called Example Bot. You can ask me anything," with instructions on how to speak for correct audio output <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Voice**: The ability to change the character's voice is crucial for a complete experience <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Character Customization**: Users can easily edit the configuration file to create new characters or modify existing ones <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. The character selection screen directly reflects changes made in this file <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

### AI Model and Process
The demonstration uses `llama 3.1 70b` as the LLM provider <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The entire process for AI-driven character interactions involves:
1.  **Speech-to-Text (STT)**: The system takes audio input from the microphone and converts it into text using an STT provider <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: This text is then fed into the AI model, which processes it and generates a response as text <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: The AI's text response is then converted back into speech using a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is streamed back to the user's browser or device <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily handles the underlying complexity of this system, including performance and error handling, allowing developers to focus on the character's behavior <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## Function Calling for AI Actions
A key capability of AI-driven characters is "function calling," which allows the AI to perform external actions <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. While LLMs primarily output text, they can be instructed to output text in a specific format that a surrounding system can interpret as a command to execute a function <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

### Implementing a Weatherman Character:
1.  **Define the Tool**: Add code in the `config` file to define the "weather tool," specifying its name (e.g., `get_weather`) and parameters (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
2.  **Instruction Alignment**: The AI model is trained to understand functions and their required output format <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. Daily's backend expects a specific message format (e.g., `<function>` tags) to identify when the AI is calling a function <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
3.  **Implement the Function**: In the `page.tsx` file, define what actually happens when the AI "calls" the `get_weather` function <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. Crucially, the function name here must exactly match the name defined for the LLM <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
4.  **API Route**: The function calls an API route (e.g., `/api/weather`) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. This route, typically in a Next.js framework, contains the actual logic for the function <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
5.  **Custom Responses**: For the weatherman, the API was set up to return whimsical weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. This approach not only provides entertaining responses but also helps confirm the function calling is working, as the AI wouldn't normally generate such specific, nonsensical weather reports <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. Such unique responses also have the potential to go viral on social media <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

## Deployment
Once developed, AI character apps can be deployed online. Next.js, an open-source framework for building websites with React, is commonly used <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>. Vercel, the company that created Next.js, provides a platform that makes hosting Next.js apps online very easy <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

### Deployment Steps with Vercel:
1.  **Install Vercel CLI**: Use the Vercel command-line interface tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Log In**: Connect the CLI to your Vercel account <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
3.  **Deploy**: Type a simple command like `vercel` <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This will trigger a deployment, making the app live on the internet <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

This process enables sharing the app via a URL, making it accessible on any device <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

## Example: A Vtuber App
An advanced application of AI-driven character interaction is a FaceTime-like app allowing users to call a [[voicedriven_ai_applications | vtuber]] <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. Vtubers are content creators who stream using a virtual avatar instead of their real face, often anime characters due to the trend's origin in Japan <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. This app utilizes voice APIs and Daily (specifically Pip Cats for greater developer control) to create a personal, interactive experience with an AI-driven vtuber avatar <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. The avatar models can be purchased from marketplaces like Booth (nzima) <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

Just a few years ago, building such an application would require a large team and significant capital. Now, individuals can create sophisticated AI character apps independently <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. For those interested in [[creating_ai_voice_character_apps_with_daily_bots | creating AI voice character apps with Daily Bots]], this demonstrates the potential for powerful and engaging experiences.