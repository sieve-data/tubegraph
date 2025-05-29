---
title: Using AI to create voice character apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

AI is being utilized to create voice character applications that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "voice chat apps" or "audio ChatGPT" experiences offer a "10x improvement" over text-based AI <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Even without extensive coding knowledge, individuals can [[building_successful_ai_apps | build successful AI apps]] in this space <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## The Rise of AI Characters as Applications

The concept that "characters are the new apps" is emerging, suggesting a significant opportunity that is not yet widely discussed <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This trend is evident in the retention rates of AI character chat apps, indicating they are not merely a fad but a lasting form of engagement <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>, <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Such apps can be applicable in both B2B and B2C contexts, serving as a new form of interactive content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Building a Voice Character App

The process of [[building_apps_with_ai_tools | building apps with AI tools]] focuses on getting the bot operational and configuring its personality <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. A demonstrable example includes the creation of a fully working "weatherman" character app <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Key Tools and Technologies

*   **Cursor:** A code editor that integrates with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily:** A core platform for handling the voice backend and heavy lifting of AI <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Daily Bots, a service by Daily, simplifies the process by handling LLM calls directly <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Pip Cat:** An alternative library, more focused on developers, that offers greater control when interfacing with AI for [[building_and_optimizing_voice_ai_agents | building and optimizing voice AI agents]] <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.
*   **Next.js:** A framework used for setting up servers and building React applications, providing structure for [[building_ios_apps_with_ai | building iOS apps with AI]] as well as web-based ones <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>, <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>.
*   **Vercel:** A platform for hosting Next.js applications online, enabling easy deployment with a single command <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>, <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
*   **Together AI:** A provider of various AI models, including Llama 3.1 70B, which is used for the bot's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Development Workflow

1.  **Setup:** Obtain an API key from Daily <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Clone a demo repository provided by Daily, which comes with a pre-configured demo screen <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The API key is then added to a `.env.local` file <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
2.  **Running the Server:** Start the development server using a command like `yarn dev` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
3.  **Core AI Process:** The system operates by taking audio input from the microphone, converting it to text via a Speech-to-Text (STT) provider. This text is sent to an LLM (e.g., Llama 3.1 70B), which processes the input and outputs a text response. This text is then converted back into speech by a Text-to-Speech (TTS) provider and streamed to the user's browser <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
4.  **Character Configuration:** The bot's behavior and voice are controlled through a configuration file <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Users can edit existing character prompts or add new ones by modifying this file, directly impacting the character selection screen <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>, <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This allows for diverse character creation, from a Gen Z middle schooler to a skateboard meme guy <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
5.  **Function Calling:** Advanced functionality allows the AI to perform "system stuff," such as calling APIs, fetching data, or making social media posts <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This involves defining tools and parameters for the LLM to understand and utilize <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. The LLM outputs text in a specific format that the Daily system interprets as a function call, which then triggers the corresponding code on the server <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>, <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
6.  **Deployment:** Once developed, the application can be deployed online using platforms like Vercel with a simple command, making it accessible via a URL on any device <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>, <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

### Design and Virality

When [[using_ai_for_app_design_and_functionality | using AI for app design and functionality]], it's important to think about what will make the character engaging and potentially viral <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Adding unique or humorous elements, like a weather bot reporting "whimsical singing rainbows" or "flying pigs," can lead to shareable moments and free distribution <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>, <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>, <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

## [[the_potential_of_ai_in_app_development | The Potential of AI in App Development]]

The simplicity and accessibility of these tools mean that individuals can rapidly develop complex [[advanced_ai_voice_note_applications | advanced AI voice note applications]] and other AI-powered experiences that previously required large teams and significant capital <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>, <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>. An example of a more advanced application is a "FaceTime call with a vtuber," which uses AI voice APIs and custom models to create a personalized interactive experience with an animated avatar <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>, <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>, <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. This highlights the growing capabilities and creative possibilities in [[using_ai_to_create_video_games | using AI to create video games]] and other interactive media.