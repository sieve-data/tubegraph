---
title: Building a weatherman voice app with AI
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

This article outlines how to create an AI-powered weatherman voice application using readily available tools, demonstrating the potential for [[creating_ai_voice_character_apps | AI voice character apps]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The process allows both technical and non-technical individuals to rapidly develop functional and engaging voice applications <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The core idea is that AI "characters" are the new "apps," offering a significant opportunity in the current technological landscape <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

## Key Insights and Benefits

*   **Rapid Development** The tools available enable quick setup of something that can "wow" both the developer and friends <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   **Enhanced User Experience** Interacting with AI through voice provides a "10x improvement in experience" compared to text-based interfaces like ChatGPT <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
*   **Focus on Character Design** The underlying AI system handles the complexity, allowing creators to focus on defining the character's personality and behavior <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.
*   **Viral Potential** Incorporating unique or "wacky" responses (like "singing rainbows" or "flying pigs" for weather) can lead to viral content and free distribution for the character <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>, <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>.
*   **Accessibility** Despite technical jargon, the process is made easy with current tools, lowering the barrier to entry for app creation <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>, <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Future of Apps** [[building_a_social_app_using_ai | AI character chat apps]] are demonstrating high retention, suggesting they are a significant part of the future for engaging consumer and non-consumer applications <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>, <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.

## Tools and Technologies Used

*   **Cursor:** A code editor integrated with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.
*   **Daily:** The primary service for handling the voice backend and heavy lifting, providing voice AI capabilities <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
    *   **Daily Bots:** A specific Daily offering that simplifies LLM calls and back-end complexities <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>, <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
*   **Together AI:** An LLM provider used for the AI models <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   **Llama 3.1 70B:** The specific AI model used for the bot's responses <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.
*   **Next.js:** A React framework for building web applications, used for setting up the server and pages <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>, <a class="yt-timestamp" data-t="20:26:00">[20:26:00]</a>.
*   **Vercel:** A platform for deploying Next.js applications online, making them live on the web <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>, <a class="yt-timestamp" data-t="29:30:00">[29:30:00]</a>.
*   **Pip Cat:** An alternative library by Daily (mentioned, but Daily Bots was chosen for simplicity in this tutorial as it handles LLM calls directly) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="34:49:00">[34:49:00]</a>.

## Building the Weatherman Voice App

The process involves minimal coding and largely relies on configuring existing frameworks and services.

### Core Mechanics of Voice AI

The system operates through a series of transformations:
1.  **Speech-to-Text (STT):** Audio input from the microphone is converted into text by a Speech-to-Text provider <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.
2.  **LLM Processing:** This text is sent to the LLM (AI model), which processes it and generates a text response <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
3.  **Text-to-Speech (TTS):** The LLM's text response is then converted back into speech by a Text-to-Speech provider <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
4.  **Audio Output:** The generated speech is streamed back to the user's browser <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>.

Daily handles the complexities of this entire system, including performance and error handling <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>, allowing developers to focus on the assistant's behavior and personality <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.

### Step-by-Step Implementation

1.  **Obtain Daily API Key:** Sign up for Daily and acquire an API key from their dashboard <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>, <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
2.  **Clone the Daily Bots Demo Repository:** Download the pre-existing demo code to your system <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>, <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
3.  **Configure API Key:** Place the Daily API key into the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>, <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.
4.  **Run the Development Server:** Execute the `yarn dev` command in your terminal to start the application server <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>, <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
5.  **Access the Demo:** Navigate to the provided local host URL in your browser to interact with the default bot <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>, <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### Customizing the Character and Functionality

The default demo includes a configuration file that allows easy modification of the bot's behavior and voice <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>, <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

#### Character Definition
*   **Prompt Engineering:** The core of defining a character is the prompt. For example, the default assistant is configured with: "You are an assistant called example poot. You can ask me anything," along with speaking instructions for correct audio output <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **Custom Characters:** New characters can be added simply by editing the configuration file <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. The character selection screen directly reflects changes made in this file <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.

#### Implementing Function Calling (Tools)
Function calling allows the AI to interact with external systems and perform actions, going beyond just text output <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>, <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   **Concept:** An LLM itself only outputs text. Function calling involves building a system around the LLM that interprets its text output (specifically formatted calls) and then performs the desired actions (e.g., calling an API) <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>, <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.
*   **Defining the Tool:**
    *   In the `config.ts` file, a `weatherTool` is defined, including its `name` (e.g., `get_weather`) and `parameters` (e.g., `location`) <a class="yt-timestamp" data-t="17:43:00">[17:43:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.
    *   The structure of this definition follows Daily's documentation, ensuring the AI model understands how to respond with the correct format (e.g., starting with `<function>` and ending with `</function>`) <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>, <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.
*   **Executing the Tool:**
    *   In `page.tsx`, the `get_weather` function is mapped to an actual code execution <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>, <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>.
    *   This code calls an API route, specifically `/api/weather` in the Next.js application <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>.
*   **API Route Logic:**
    *   The `API/weather/route.ts` file contains the logic for the weather data. For demonstration, it returns humorous, non-real weather conditions like "peculiar whimsical flying pigs" or "whimsical singing rainbows" <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>, <a class="yt-timestamp" data-t="22:25:00">[22:25:00]</a>.
    *   This allows validation that the function calling is working (by observing the AI mention these nonsense phenomena) <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a> and creates potential for viral content <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>.

### Deployment

Once the app is configured, it can be deployed live online:
1.  **Install Vercel CLI:** Install the Vercel command-line interface tool <a class="yt-timestamp" data-t="30:04:00">[30:04:00]</a>, <a class="yt-timestamp" data-t="30:08:00">[30:08:00]</a>.
2.  **Log In:** Log in to your Vercel account via the CLI <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
3.  **Deploy:** Simply type `vercel` in the terminal to deploy the application. Vercel automatically deploys Next.js apps <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>, <a class="yt-timestamp" data-t="30:58:00">[30:58:00]</a>.
4.  **Access Live App:** Vercel provides a URL where the app is hosted and accessible on any device <a class="yt-timestamp" data-t="31:24:00">[31:24:00]</a>, <a class="yt-timestamp" data-t="31:58:00">[31:58:00]</a>.

## Beyond the Weatherman: Real-World Applications

The demonstrated weatherman app is a basic example. [[innovative_app_ideas_using_ai | AI voice character apps]] can be extended to more complex applications, such as [[building_flexible_voice_ai_agents_with_vappy | building flexible voice AI agents]] or even [[practical_applications_of_voice_ai_in_startups | social applications]] <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

An example of a more complex [[building_apps_with_ai | AI-powered app]] is one that facilitates a FaceTime-like call with a VTuber (virtual YouTuber) <a class="yt-timestamp" data-t="32:35:00">[32:35:00]</a>. This app allows users to have personal conversations with an AI-driven anime character, leveraging voice APIs like Daily or Pip Cat (for more developer control) to embody an avatar <a class="yt-timestamp" data-t="33:44:00">[33:44:00]</a>, <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>. Such applications highlight the potential for single developers to create sophisticated systems that previously would have required large teams and significant investment <a class="yt-timestamp" data-t="36:58:00">[36:58:00]</a>.