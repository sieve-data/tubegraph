---
title: Function calling and configuration in AI models
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

AI is enabling the creation of voice character applications that are proving to be highly profitable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "character apps" are emerging as a new form of application, and the process of building them is becoming increasingly accessible, even for those without extensive coding knowledge <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. What might initially appear as a "toy" can evolve into a successful startup <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Core Concepts & Tools

Building these AI-powered voice applications involves understanding key tools and concepts that simplify complex AI processes.

### Key Tools Used
*   **Cursor**: A code editor integrated with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Daily**: This platform is central to handling voice processing and backend operations for AI voice agents <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It simplifies LLM calls, allowing developers to focus on configuring the bot's behavior <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Pip Cat**: An earlier library from Daily, more focused on developers, that made it easier to interface with AI for building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. It offers more control for developers compared to Daily Bots <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.
*   **Next.js**: A framework for building websites using React, also used for setting up a server that runs code <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a> <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.
*   **Vercel**: The company that created Next.js, which also provides a platform for hosting Next.js applications online <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a> <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### The Power of Voice AI
Interacting with AI through voice can be a "10x improvement" in experience compared to text-based chat <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The rapid availability of these tools allows for quick prototyping of impressive applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Building a Voice Character App with Daily Bots

Daily Bots provides a straightforward way to create and customize voice-enabled AI characters.

### Initial Setup
1.  **Obtain API Key**: Sign up for Daily and get an API key from the dashboard <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a> <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This key unlocks Daily's services <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
2.  **Clone the Repository**: Daily provides a demo repository that runs in the browser. Cloning the repo means downloading it to your system <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
3.  **Configure API Key**: Paste the API key into an `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Run the Server**: Use a simple command like `yarn dev` to start the server locally <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a> <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

At this stage, no code has been written; it's primarily about downloading and configuring existing files <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### How Voice Bots Work
The underlying process for a voice bot involves several steps <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT)**: Audio input from the microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a> <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
2.  **LLM Processing**: The text is sent to an LLM (e.g., Llama 3.1 70B via Together AI) for processing <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The LLM generates a text response <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS)**: Daily takes the LLM's text response and converts it into speech using a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
4.  **Audio Output**: The generated speech is streamed back to the user's browser or device <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a> <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

Daily handles the technical complexities of this system, allowing developers to focus on the bot's functionality <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Configuring Character Personality
The personality and behavior of the AI character are defined in a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Prompts**: The initial prompt defines the character's role and instructions, e.g., "You are an assistant called example poot" <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a> <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Instructions on how the AI should speak are included to ensure correct audio output <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Pre-set Characters**: Daily provides default characters like a "gen z middle schooler" or a "skateboard meme guy" <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **[[implementing_ai_in_app_development_processes | Customizing Characters]]**: Users can easily edit the configuration file to create their own characters and define their unique prompts <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This direct mapping between the file and the character selection screen makes customization simple <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

> "If you think of characters as the new apps then there's a huge opportunity and not many people are talking about this around just ideating on characters figuring out what's going to work and launching them" <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
>
> Research suggests that AI character chat apps are not a fad, exhibiting high retention rates and engagement <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a> <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. This trend is expected to influence both B2B and B2C applications, becoming a new form of content interaction <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a> <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## [[operator_ai_capabilities_and_limitations | Function Calling]]

[[operator_ai_capabilities_and_limitations | Function calling]] allows an AI model to interact with external systems and perform actions beyond just generating text.

### How Function Calling Works
An LLM inherently only takes in text and outputs text <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a> <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. To perform actions, a system must be built *around* the LLM <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Instruction Following**: Sufficiently smart LLMs can follow instructions exceptionally well <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a> <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
*   **Output Format**: Function calling involves configuring the LLM to output a specific text format that indicates a function call <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a> <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **System Action**: The system (in this case, Daily's backend) waits for this specific format. When detected, it executes the corresponding function on the backend <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a> <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
*   **LLM is an "Instruction Follower"**: The LLM itself isn't *doing* the action; it's merely outputting text instructions that the surrounding system then carries out <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a> <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. This allows the AI to perform "system stuff" like calling APIs, getting data, or making social media posts <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Implementing a Weather Tool Example
A practical example involves creating a "weatherman" character that can provide weather reports for a specified location <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a> <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

1.  **Define the Tool**: In the configuration, define the tool's name and its parameters (e.g., `location` for a weather tool) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a> <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
2.  **Align Names**: It's crucial that the tool name used in the configuration matches the name defined in the backend code (e.g., `get_weather`) to avoid errors <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a> <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
3.  **Define Backend Action**: In the server-side code (e.g., `page.tsx` and `route.ts` in Next.js), define what actually happens when the AI calls the function <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. For the weatherman, this means calling an API route like `/api/weather` <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
4.  **"Nonsense" Weather**: To make the example more engaging and testable, the weather API can be configured to return humorous or "nonsense" conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a> <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a> <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. This provides clear validation that the function calling is working (by seeing these specific, unusual phrases) <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. These unique responses can also serve as "TikTok moments" for [[building_an_ai_startup_workflow | virality]] <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a> <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.

When building, it's important to make small, understandable changes rather than trying to "one-shot" an entire application with AI, as this aids in learning and debugging <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.

## Deployment

Once an AI character app is built, [[building_and_deploying_apps_with_ai_integration | deploying it live]] to the web is a crucial next step.

### Using Vercel for Deployment
Vercel makes it incredibly easy to host Next.js applications online <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
1.  **Vercel CLI**: Vercel provides a command-line interface (CLI) tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Login**: Connect the CLI to your Vercel account <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
3.  **Deploy Command**: A simple command like `vercel --prod` can deploy your app live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a> <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a> <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>. This makes the application accessible via a public URL on any device <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

## Example of a Finished Product

A sophisticated application built using these principles is a FaceTime-like call with a VTuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.
*   **VTubers**: Content creators who stream using a virtual avatar instead of their real face, often anime characters <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a> <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>. They are very popular, earning millions from subscriptions and merch <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.
*   **App Concept**: The app allows users to have a personal video call with an AI-powered VTuber, something not typically possible with human influencers <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a> <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   **Implementation**: This specific app uses Pip Cat (rather than Daily Bots) for more developer control over data flow <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. The VTuber model itself can be purchased from marketplaces like Booth (Booth.pm) <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a> <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

Such an application, which would have required a large team and venture capital funding years ago, can now be built by an individual due to advancements in AI tools <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.