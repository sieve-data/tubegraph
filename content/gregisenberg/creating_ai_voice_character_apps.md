---
title: Creating AI voice character apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The use of AI to create voice character applications is enabling developers to generate significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "characters" are described as the new "apps," representing a significant, under-discussed opportunity <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Even non-technical individuals can leverage these tools to build such applications <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Power of Voice-First AI
Interacting with AI through voice provides a "10x improvement in experience" compared to text-based models like ChatGPT <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The availability of powerful tools makes it incredibly fast and exciting to create impressive voice agents <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The core idea is that if you can dream of a voice app, you can create it <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Core Components and Workflow
Building a voice character app, such as an audio ChatGPT, involves several key technologies and a defined process <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

#### Key Tools
*   **Code Editor:** Cursor, which integrates large language models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Primary Voice Platform:** Daily (specifically Daily Bots), which handles much of the heavy lifting for voice and backend processes <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It simplifies the process by handling LLM calls internally <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Daily also has a developer-focused library called Pip Cat, offering more control over AI interfaces <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **LLM Provider:** Together AI, which provides various AI models, including Llama 3.1 70B, used for the bot's responses <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Development Framework:** Next.js, a framework utilizing React for building websites and server-side logic <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Deployment Platform:** Vercel, a company that created Next.js and provides a platform to host Next.js applications online <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

#### The Voice AI Pipeline
The process for a voice character app involves several stages <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT):** The Daily bot system captures audio from the microphone and converts it into text <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **LLM Processing:** The transcribed text is sent to an LLM (AI model), which processes it and generates a response in text <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS):** Daily takes the LLM's text response and converts it into speech using a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output:** The generated speech is streamed back to the user's browser or device <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire system, including handling performance and errors, is managed by Daily, abstracting away significant [[challenges_and_solutions_in_implementing_voice_ai | complexity]] for the developer <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Building a Weatherman Character App
A fully functional weatherman character app was built during the session <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Getting Started
1.  **Clone the Repository:** Download the Daily Bots demo repository to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Obtain API Key:** Sign up for Daily and retrieve your API key from the dashboard <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Configure API Key:** Paste the API key into the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Run the Server:** Use the command `yarn dev` to start the local server, making the demo accessible via a local host URL <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Customizing Character Personality
The core of defining a character's personality lies in a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Prompts:** You can define a character's role and speaking instructions through prompts, such as "You are an assistant called example poot" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Voice Selection:** The ability to change the character's voice is crucial <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Pre-set Characters:** The demo includes various pre-set character prompts like a "Gen Z middle schooler" or a "skateboard meme guy" <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Creating Custom Characters:** Developers can easily add their own characters by editing this configuration file, linking directly to the character selection screen <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Implementing Function Calling
Function calling allows the AI to perform external actions beyond just outputting text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. While the LLM itself only outputs text, the system around it takes that output and executes predefined functions <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

*   **Defining Tools:** A "weather tool" can be defined in the configuration, including a name and parameters (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   **LLM Instructions:** The AI model is given instructions on how to respond in a specific format (e.g., `<function>...` tags) that Daily recognizes as a function call <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   **Executing Functions:** In the `page.tsx` file, the actual logic for what happens when the AI "calls" a function (like `get_weather`) is defined <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. This often involves calling an API route on the server <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Server-Side Logic:** For the weatherman, a `route.tsx` file within an `API/weather` directory defines what happens when that API route is accessed <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. In the demo, this was set up to return "nonsense" weather conditions like "Whimsical flying pigs" or "singing rainbows" <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. This allows for validation that the function calling is working (by checking logs for API access) and creates viral, shareable content <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### Deployment
Applications can be deployed live using Vercel, which was created by the same company behind Next.js <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.
*   **Vercel CLI:** Vercel provides a command-line interface tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
*   **Simple Deployment:** After logging into your Vercel account, a single command (`vercel`) can deploy your Next.js app live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## The Future of AI Character Apps
The concept of characters as the new apps opens up a huge opportunity <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Retention:** Retention graphs for AI character chat apps indicate they are not a fad and users enjoy interacting with these characters <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Broad Application:** This technology applies to both business-to-business (B2B) and business-to-consumer (B2C) contexts, transforming how users interact with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   **Accessibility:** What once required large teams and significant venture capital is now achievable by individual developers <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.

### Example: AI Vtuber Face-Call App
An example of [[innovation_in_ai_character_applications | innovation in AI character applications]] is an app that allows users to have a FaceTime-like call with a virtual Youtuber (Vtuber) <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
*   **Vtuber Concept:** Vtubers are content creators who stream using a digital avatar, often anime characters, instead of their real face <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>. They are extremely popular, generating millions of followers and revenue <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.
*   **App Functionality:** The app leverages voice APIs and Daily (specifically Pip Cat for more developer control) to enable personal one-on-one calls with an AI-driven Vtuber, providing an interactive experience beyond typical streaming <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>.
*   **Building the Vtuber:** The specific Vtuber model, named Maji, was purchased from a marketplace called Nizima, which offers pre-rigged anime models <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>.

This demonstrates the potential for creating highly engaging and unique consumer experiences using [[voicefirst_technology_and_applications | voice-first technology]] and AI character development. The weatherman app, for example, can be transformed into an [[building_an_ios_app_with_ai | iOS app]] rather than just a web application <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

## Development Approach
It's recommended to build new features by making "small and understandable changes" to existing demos rather than trying to build a complex application from scratch <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. This approach aids learning and understanding of how different components integrate <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.