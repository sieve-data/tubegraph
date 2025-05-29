---
title: Developing AI character apps with customization
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The landscape of applications is evolving, with **AI character apps** emerging as a significant new frontier. These applications, often leveraging voice [[using_ai_to_create_voice_character_apps | AI]] technologies, are seen by some as the "new apps" with substantial opportunities for creators, regardless of their technical background <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Rise of Voice Chat Apps

These applications are essentially voice chat apps, akin to an "audio ChatGPT," enabling dynamic audio interactions <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The experience of talking to a ChatGPT-like entity provides a "10x improvement in experience" compared to text-based interactions <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Despite seeming like a "toy" at first, many successful startups begin with simple, playful concepts <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Core Tools and Concepts

Developing these apps involves a combination of specialized tools and an understanding of how [[embedding_ai_to_enhance_app_functionality | AI]] processes information.

### Key Technologies

*   **Cursor:** A code editor integrated with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily:** A central platform that handles the heavy lifting for voice and backend processes in AI character applications <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Daily offers `Daily Bots`, which abstract away the complexity of LLM calls, allowing developers to focus on configuration <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Pip Cat:** A library focused on developers, making it easier to interface with [[innovative_ai_functionalities_in_apps | AI]] and [[creating_and_customizing_ai_agents_for_specific_use_cases | build voice assistants]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. While Daily Bots simplify LLM calls, Pip Cat offers more control for developers <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.
*   **Next.js:** A framework used for setting up a server that runs React, enabling the creation of web pages that run code <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

### The AI Interaction Pipeline

The core of a voice AI character app involves a sophisticated pipeline:
1.  **Speech-to-Text (STT):** The Daily bot system converts audio input from the microphone into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing:** This text is sent to an LLM (e.g., Llama 3.1 70B via Together AI) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. The LLM processes the text based on its configured personality and prompts <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
3.  **Text-to-Speech (TTS):** The LLM's text response is then converted back into speech by a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output:** The generated speech is streamed back to the user's browser or device <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily handles the underlying complexity of this system, including performance and error handling, allowing developers to focus on the character's behavior and features <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Understanding Function Calling

Function calling is a crucial capability for AI characters to interact with external systems.
*   **LLMs only output text:** An LLM itself cannot perform actions beyond generating text <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **System around the LLM:** A system is built around the LLM to interpret its text output and trigger real-world actions <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Following instructions:** Smart LLMs can be instructed to output text in a specific format that indicates a function call, including parameters <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This formatted output is then picked up by the surrounding system to execute the desired function (e.g., calling APIs, getting data, making an Instagram post) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Building a Basic AI Character: The Weatherman Demo

A practical example of building an AI character app involves creating a weatherman.

### Initial Setup

1.  **Clone the Repository:** Start by downloading the daily bot demo repository to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Daily API Key:** Sign up for Daily and obtain an API key, which is essential to unlock their services <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  **Configuration:** Paste the API key into the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Run the Server:** Execute the `yarn dev` command to start the local server, making the demo accessible in your browser <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Customizing Character Personality

The `config.ts` file is where the AI character's personality and behavior are defined.
*   **Prompts:** The `prompt` field contains instructions for the LLM, such as "You are an assistant called example poot. You can ask me anything," along with speaking instructions for correct audio output <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Editing Characters:** You can easily add or edit characters by modifying this file. For instance, changing the default character's name to "Eric" directly updates the character selection screen <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

### Implementing Function Calling (The Weatherman)

To make the weatherman character functional, function calling is implemented:

1.  **Define the Tool:** In the `config.ts` file, a "weather tool" is defined for the LLM <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
    *   **Name:** The tool's name (e.g., `get_weather`) is crucial and must be aligned across definitions <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
    *   **Parameters:** Parameters like `location` are specified so the AI knows what information to expect for the function <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
    *   **Response Format:** The AI model is instructed to respond in a specific format (e.g., starting with `<function>` and ending with `</function>`) so Daily can interpret it as a function call <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

2.  **Implement the Function:** In `page.tsx`, the `get_weather` function is defined to handle what actually happens when the AI calls it <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This function calls a specific route (e.g., `/api/weather`) on the server <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

3.  **Server-Side Logic:** The `/api/weather/route.ts` file contains the server logic. For the demo, instead of real weather data, a randomized "nonsense weather" response is used (e.g., "whimsical singing rainbows" or "flying pigs") <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
    > [!TIP] The inclusion of humorous or unexpected responses like "flying pigs" serves a dual purpose: it helps confirm that the function calling is working (as the AI is retrieving specific, predefined nonsense) and it creates viral "TikTok moments" that can generate free distribution for the app <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### Testing and Validation

After setup, the app is tested. When asked for the weather in New York City, the weatherman responds with a random "nonsense" condition like "whimsical singing rainbows," confirming the function calling pipeline is operational <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. Server logs also confirm the API route was accessed with the correct location <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.

## Deployment

Once developed, an app can be deployed online for public access.
*   **Vercel:** As Next.js was developed by Vercel, their platform provides an easy way to host Next.js apps <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.
*   **Simple Deployment:** After logging into Vercel, a single `vercel` command can deploy the app live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. The deployed app can then be accessed via a URL on any device <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

## Advanced Application: The VTuber App

Beyond simple character apps, these technologies enable more complex and [[building_a_social_app_with_ai | innovative AI functionalities in apps]]. An example is an app that allows users to have a personal "FaceTime call" with a VTuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.

*   **VTubers:** These are content creators, popular on platforms like Twitch and YouTube, who embody avatars (often anime characters) rather than showing their real faces <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. They have millions of followers and generate significant income <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.
*   **Concept:** The app leverages voice APIs (like Daily or Pip Cat) to create a personalized interactive experience with an AI-powered VTuber, which is not typically possible with live influencers <a class="yt-timestamp" data-t="00:33:44">[00:33:44]</a>.
*   **Development:** The VTuber model itself can be purchased from marketplaces like "nzima," and the app is built to integrate this model with voice AI for interactive calls <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>. This particular app uses Pip Cat for more developer control <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.

## Challenges and Opportunities in AI App Development

> [!NOTE] Building anything, especially when starting out, benefits from making small, understandable changes rather than attempting a large "one-shot" project <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>. Leveraging existing demo repositories and gradually adding features helps in understanding how components fit together <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

*   **Characters as the New Apps:** There's a "huge opportunity" in ideating and launching AI characters, a concept not widely discussed <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Retention:** While some initially considered [[building_ios_apps_with_ai | AI character chat apps]] a fad, their high retention rates suggest they are here to stay <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This is particularly relevant as traditional [[building_a_social_app_with_ai | social apps]] face challenges, such as contact sync restrictions after iOS 18 <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Broad Applications:** AI character apps are applicable in both B2B and B2C contexts, serving as a new form of content interaction <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Accessibility:** Modern [[building_apps_with_ai_tools | AI tools]] and frameworks greatly simplify development, allowing individuals to [[development_of_a_healthfocused_ai_app | build sophisticated applications]] that previously would have required large teams and significant capital <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.
