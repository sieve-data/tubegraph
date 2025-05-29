---
title: Using Daily Bots and Nextjs for voice applications
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

Voice AI applications, where "characters are the new apps," are emerging as a significant opportunity in the tech landscape <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. These applications, often looking like "toys" initially, can grow into successful [[practical_applications_of_voice_ai_in_startups | startups]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This article outlines how to build such applications using Daily Bots and Next.js, making the process accessible even to those without extensive coding knowledge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Core Technologies

The primary tools for [[building_apps_with_ai | building apps with AI]] focused on voice chat are:
*   **Daily Bots**: This company provides the core voice AI backend, handling speech-to-text (STT), text-to-speech (TTS), and Large Language Model (LLM) calls <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Daily Bots simplifies the process by abstracting away the complex AI infrastructure <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Next.js**: A React framework that allows for setting up both front-end web pages and back-end server routes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

Additional tools and concepts include:
*   **Cursor**: A code editor integrated with LLMs for coding assistance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **GitHub**: Used for cloning (downloading) code repositories <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a> <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Vercel**: A platform that enables easy deployment and hosting of Next.js applications online <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

## Setting up Your First Voice Application

Building a voice AI application is surprisingly quick <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. The process begins with setting up the Daily Bots demo:

1.  **Clone the Daily Bots Repo**: Download the demo repository to your system <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Sign up for Daily**: Obtain an API key from the Daily dashboard <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Connect the Demo**: Paste the API key into the `.env.local` file within your cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Run the Server**: Use the `yarn dev` command to start the local server, which will typically run on a local URL like `localhost` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

At this point, no code has been written; you've merely downloaded and configured an existing demo <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Understanding Voice AI Interaction

The core interaction of a voice AI bot involves several steps:
1.  **Speech to Text (STT)**: Audio input from the microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: The text is sent to an LLM (e.g., Llama 3.1 70B via Together AI) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. The LLM processes the input and generates a text response <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
3.  **Text to Speech (TTS)**: Daily takes the LLM's text response and converts it into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is piped back to the user's browser or device <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily handles the complexities of this entire system, including performance and error handling <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## Configuring Character Personalities

The personality and behavior of your voice bot are controlled via a configuration file <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Prompts**: The file contains default prompts like "You are an assistant called example bot" <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Customization**: You can easily edit this file to define new characters, prompts, and even adjust the bot's voice <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This flexibility makes [[creating_ai_voice_character_apps | AI voice character apps]] a significant opportunity <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Implementing Function Calling (Tools)

Function calling allows the voice bot to "do stuff" beyond just outputting text <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. While the LLM itself only outputs text, a system built around it can interpret specific text formats as calls to external functions or APIs <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### Building a Weatherman Voice App

As an example, a [[building_a_weatherman_voice_app_with_ai | weatherman voice app]] can be built using function calling:

1.  **Define the Tool**: In the `config` file, define a "weather tool" with a specific name (e.g., `get_weather`) and describe the parameters it accepts, like "location" <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a> <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
2.  **Instruction for LLM**: The LLM is instructed to respond in a specific format (e.g., starting with `<angle bracket function>`) when it intends to call this tool <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
3.  **Implement the Function Call**: In `page.tsx`, define what actually happens when the LLM "calls" the `get_weather` function <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. This involves calling an API route (e.g., `API/weather`) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
4.  **API Route Logic**: In the `API/weather` route (defined in `route.tsx` within the Next.js API directory), implement the logic for retrieving weather information <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. For demonstration, this example uses "nonsense" weather conditions like "whimsical singing rainbows" <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a> <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. This deliberate "wacky" output can serve as a "TikTok moment," making the product more shareable and potentially viral <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
5.  **Testing**: By interacting with the weatherman bot, you can confirm that the function calling is working if the bot provides a response that includes the defined "nonsense" weather conditions and if the server logs show the API route being accessed <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a> <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.

## Deployment with Vercel

Once your application is ready, Vercel makes it easy to deploy your Next.js app to the web:

1.  **Vercel CLI**: Use the Vercel command-line interface (CLI) tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Login**: Log in to your Vercel account through the CLI <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
3.  **Deploy**: Simply type `vercel` in your terminal, and the app will be deployed live online <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a> <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.

## Advanced Voice AI Applications

While Daily Bots simplifies initial development, for more complex applications, developers might use libraries like Pipette, which offers more control over data flow <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a> <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

An example of a more advanced application is "Vappy," an app that allows users to have a FaceTime-like call with a VTuber (virtual YouTuber) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. This app combines voice AI with avatar embodiment technology, demonstrating the potential for [[voicefirst_interfaces_and_content_discovery | voice-first interfaces]] <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a> <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. Vappy showcases how to [[building_flexible_voice_ai_agents_with_vappy | build flexible voice AI agents]] that can act in specific ways, similar to how influencers interact with their audience <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

## Conclusion

The ability to create sophisticated voice AI applications with minimal code and single-person teams highlights a new era of app development <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. The concept of characters as the "new apps" presents vast opportunities for both B2B and B2C markets, transforming how users interact with content and services <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a> <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.