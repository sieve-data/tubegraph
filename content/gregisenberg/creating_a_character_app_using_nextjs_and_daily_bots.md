---
title: Creating a character app using Nextjs and Daily Bots
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

Character apps are emerging as a significant opportunity in the AI landscape, with some individuals already [[using_ai_to_create_voice_character_apps | using AI to create voice character apps]] that are generating substantial revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These applications, which often take the form of voice chat bots, are considered the "new apps" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Even without extensive coding knowledge, it's possible to create a functional character app, such as a fully working weatherman character app, as demonstrated in this episode <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Key Technologies

The core of building these character apps involves leveraging specific AI tools and frameworks:

### Next.js
Next.js is a framework that utilizes React for [[creating_a_functional_fullstack_application | building websites]] <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>. Developed by Vercel, it allows developers to set up a server that runs React applications and specify routes <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Being an open-source framework, Next.js apps can be developed for free and then hosted online through Vercel's platform <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.

### Daily Bots
Daily is a company that provides the main tools for handling voice interaction and backend processes in these applications <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Daily Bots, a specific offering from Daily, simplifies the process by handling the Large Language Model (LLM) calls themselves, removing much of the complexity for the developer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Developers can sign up, access a dashboard, and obtain an API key to unlock Daily's services <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Cursor
[[introduction_to_ai_tools_like_cursor_and_daily_for_app_development | Cursor]] is a code editor that integrates with LLMs to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Understanding Voice Bots

The experience of interacting with a voice bot can be a 10x improvement over text-based interfaces like ChatGPT, offering an "awesome" and "exciting" experience <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### How Voice Bots Work
A voice bot operates through a multi-step process <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech to Text (STT)**: The Daily Bot system takes audio input from a microphone and converts it into text using an STT provider <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **LLM Processing**: This text is then fed into an LLM (AI model), such as Llama 3.1 70B via Together AI, which processes the information and generates a text response <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
3.  **Text to Speech (TTS)**: Daily takes the LLM's text response and converts it into speech using a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The generated speech is then outputted to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire system, including performance and error handling, is managed by Daily, allowing developers to focus on the bot's functionality and personality <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Function Calling
Function calling allows an LLM to interact with external systems and perform actions beyond just generating text <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. The LLM, if smart enough, can understand functions, function calls, and responses, and output text in a format that an external system can then use to perform an action (e.g., calling APIs, getting data, making an Instagram post) <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Daily's system waits for specific message formats to understand when the AI model is trying to call a function <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

## Building a Character App (Weatherman Demo)

The process of [[drafting_app_concepts_with_minimal_coding_knowledge | drafting app concepts with minimal coding knowledge]] and turning them into functional character apps is straightforward.

### Initial Setup
To begin, developers can use a demo repository provided by Daily <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
1.  **Clone the Repository**: Download the demo code to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Obtain API Key**: Sign up for the Daily service and retrieve an API key from the dashboard <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  **Configure API Key**: Paste the API key into the `.env.local` file within the cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Run the Server**: Execute a simple command, such as `yarn dev`, to start the local server and access the demo in your browser <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

At this point, no code has been written; it's purely configuration and setup <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Configuring Character Personality
The core personality of a character app is defined in a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Prompts**: The file contains prompts that instruct the LLM on how to behave, such as "You are an assistant called example bot. You can ask me anything" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Voice**: The voice of the character can also be customized within this configuration <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Custom Characters**: Developers can easily add and edit their own characters by modifying this file, which directly reflects on the character selection screen <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Implementing Function Calling (Weatherman Example)
To enable a character to perform actions, such as fetching weather information, function calling is implemented.
1.  **Define the Tool**: In the configuration, define the tool for the LLM, giving it a name (e.g., `get_weather`) and describing its parameters (e.g., `location`) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
2.  **Align Names**: Ensure the function name used by the AI model (`get_weather`) precisely matches the function name defined in the code <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
3.  **Implement Server-Side Logic**: In the `page.tsx` file, define what happens when the AI "calls" the function <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. For the weatherman, this involves calling a specific API route (e.g., `API/weather`) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
4.  **Create API Route**: Within the Next.js `API` directory, create a route file (e.g., `route.tsx` in `API/weather`) that contains the actual logic for fetching and returning the weather data <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. In the demo, this was intentionally configured to return "nonsense" weather conditions (e.g., "whimsical singing rainbows", "flying pigs") to visually confirm the function calling was working <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

## Deployment with Vercel

Once the app is developed, deploying it to make it live is straightforward.
1.  **Vercel CLI**: Vercel provides a Command Line Interface (CLI) tool that integrates with its platform <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
2.  **Deploy Command**: After logging into your Vercel account via the CLI, a single command, `vercel`, can deploy the Next.js app to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
3.  **Live URL**: Vercel provides a unique URL where the deployed application can be accessed on any device <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>. This allows users to easily share the app with others <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## The Future of Character Apps

The concept of "characters as the new apps" presents a significant opportunity <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This trend applies to both B2B and B2C sectors, suggesting a new way of interacting with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Social Apps and Retention
Notable figures in the tech scene, like Nikita Bier, initially viewed [[building_a_social_app_with_ai | AI character chat apps]] as a fad <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. However, after observing high retention graphs, it became clear that these apps are not going away, and people genuinely enjoy interacting with these characters <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. The future of highly retentive and engaging consumer (and non-consumer) apps will likely involve [[building_successful_ai_apps | creating a character]] that performs specific actions or behaves in a certain way <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### Real-World Example: Vtuber FaceCall App
An example of a complex character app is one that allows users to have a "FaceTime" call with a Vtuber <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. Vtubers are content creators, popular on platforms like Twitch and YouTube, who use software to embody virtual anime avatars instead of their real faces <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. This app allows for a personal interaction that isn't typically possible with traditional influencers <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>. While more advanced, this app uses a similar underlying technology (Daily's Pipkit, which offers more developer control than Daily Bots) to manage voice interactions <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.

## Development Principles
When building character apps or any AI-driven application, it's crucial to:
*   **Focus on Small, Understandable Changes**: Especially when starting out, make incremental changes to ensure comprehension and manage complexity <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   **Build on Existing Demos**: Instead of trying to integrate complex systems from scratch, leverage existing repositories or demos to get started and then add custom features <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.
*   **Utilize AI for Assistance**: If facing difficulties understanding documentation or concepts, use tools like ChatGPT or Claude for explanations <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Consider Virality**: When designing characters and their responses, think about how to create "TikTok moments" – unique or amusing interactions that could go viral and generate free distribution <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

These character apps can be deployed as web applications or even [[building_ios_apps_with_ai | iOS apps]] <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>. The current landscape of AI tools allows individuals to create sophisticated applications that once required large teams and significant investment <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.