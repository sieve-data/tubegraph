---
title: Setting up and deploying apps using Nextjs
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 
This article details the process of setting up and [[development_of_startup_ideas_into_apps | developing startup ideas into apps]], specifically focusing on [[using_ai_to_create_and_deploy_web_applications | using AI to create and deploy web applications]] that involve voice characters. It highlights the use of Next.js as the core framework for building these applications.

## Building AI Voice Character Apps

The current landscape sees individuals creating voice character apps that are "printing money" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. These "characters are the new apps," and they offer a 10x improvement in user experience compared to text-based AI like ChatGPT when interacted with vocally <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. Even non-technical individuals can leverage available tools to create such applications quickly <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Key Tools and Technologies

Building these AI voice character apps primarily involves:

*   **Cursor**: A code editor integrated with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.
*   **Daily**: A company providing the core voice AI backend, handling heavy lifting like voice processing and LLM calls <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. They offer "Daily Bots" which simplify the integration of LLMs <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Pipcat**: An earlier library from Daily focused on developers, making it easier to interface with AI and [[building_a_saas_app_using_ai | build voice assistants]] <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Together AI**: A provider of various AI models, including Llama 3.1 70B, used for the LLM response <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   **Next.js**: A framework that enables developers to build both the frontend (using React) and the backend server for web applications <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>.
*   **Vercel**: The company behind Next.js, which also provides a platform for hosting Next.js applications online <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.

### Setting Up a Voice Character App

The process begins by leveraging existing demos and platforms:

1.  **Clone the Repository**: Start by cloning the Daily Bots demo repository. This involves downloading the code to your system <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
2.  **Connect to Daily Backend**: Obtain an API key from the Daily dashboard. This key is placed in an `.env.local` file to unlock Daily's services <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. At this stage, no code has been written; it's purely setup <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
3.  **Run the Application**: Use the command `yarn Dev` to start the server and access the application via a local host URL <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

#### Configuring Character Personality

The core of an AI voice character is its personality and behavior, defined in a configuration file <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

*   **Prompts**: The default prompt might be "You are an assistant called example bot. You can ask me anything," along with instructions on how to speak for correct audio output <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.
*   **Voice**: The ability to change the character's voice is crucial <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   **Speech-to-Text (STT) and Text-to-Speech (TTS)**: The Daily bot system converts microphone audio into text using an STT provider, pipes it to the LLM, receives a text response, and then converts that text back into speech using a TTS provider before sending it to the browser <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. Daily handles the underlying complexity of this system <a class="yt-timestamp" data-t="11:36:00">[11:36:00]</a>.
*   **Custom Characters**: Users can easily add or edit characters by modifying the configuration file <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. This flexibility allows for ideation on what sort of voice apps can be created <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

#### The "Characters as New Apps" Paradigm

The concept of "characters as the new apps" presents a huge opportunity for [[startup_strategies_for_consumer_apps | consumer apps]] and B2B applications alike <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>. Social apps, especially after iOS 18's contact sync restrictions, may give way to AI character chat apps, which show high retention rates <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>. This new form of content interaction is seen as the future <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.

### Implementing Function Calling

Function calling allows AI characters to perform actions beyond just outputting text, such as calling APIs or getting data <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

*   **How it Works**: An LLM, being sufficiently smart, can follow instructions to output text in a specific format that a surrounding system can interpret and act upon. The LLM itself only outputs text; the system built around it performs the actual actions <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.
*   **Weather Man Example**:
    *   A "weather tool" is defined in the configuration, specifying its name (e.g., `get_weather`) and parameters (e.g., `location`) <a class="yt-timestamp" data-t="17:43:00">[17:43:00]</a>.
    *   The AI model is instructed to respond with a specific format (e.g., `<function>get_weather</function>`) that Daily's backend recognizes <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.
    *   In Next.js, an API route (e.g., `/api/weather`) is defined. When the AI "calls" the function (outputs the specific text), the server fetches this route and executes the associated code <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>.
    *   For demonstration purposes, a "nonsense weather" function can be created to produce humorous, viral-worthy outputs like "whimsical singing rainbows" or "flying pigs," which also serve as clear indicators that the function calling is working <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>.

#### Building Practices

When building applications, especially with new AI tools, it's crucial to make small, understandable changes and build off existing structures <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>. Instead of trying to integrate everything from scratch, it's more effective to modify and expand upon a demo or existing repository <a class="yt-timestamp" data-t="28:03:00">[28:03:00]</a>.

### [[deploying_ai_apps_using_github_and_vercel | Deploying Apps with Vercel]]

Once the Next.js application is ready, [[deploying_ai_apps_using_github_and_vercel | Vercel]] provides a seamless platform for going live.

*   **Vercel's Role**: Vercel allows you to host your free and open-source Next.js application online <a class="yt-timestamp" data-t="29:28:00">[29:28:00]</a>.
*   **Deployment Command**: After logging into your Vercel account, a simple command like `vercel` typed in the command line interface (CLI) is all it takes to deploy the app to the internet <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.
*   **Accessibility**: Once deployed, the application is accessible via a URL on any device <a class="yt-timestamp" data-t="31:58:00">[31:58:00]</a>.

### Example of a Final Application

A real-world example of what can be created is an app allowing users to have a "FaceTime call" with a VTuber (virtual YouTuber) <a class="yt-timestamp" data-t="32:42:00">[32:42:00]</a>. VTubers are content creators who use software to embody anime avatars, and they are incredibly popular <a class="yt-timestamp" data-t="32:52:00">[32:52:00]</a>. This app uses Pipcat for more developer control and involves integrating bought VTuber models from marketplaces like Booth (nzima) <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>. Such an app, previously requiring a large team and venture capital, can now be built by an individual <a class="yt-timestamp" data-t="36:58:00">[36:58:00]</a>.