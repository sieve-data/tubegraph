---
title: Creating AI voice character apps
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The development of [[ai_app_development | AI apps]] has advanced to a point where people are leveraging AI to create voice character apps that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This field offers a massive opportunity, particularly for those looking to build innovative solutions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Characters as the New Apps

A core idea in this space is that [[designing_characters_as_the_new_apps | characters are the new apps]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This concept suggests a shift in how applications are perceived and built, with a focus on interactive, personality-driven AI agents <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This trend is gaining traction, with retention graphs showing strong engagement for AI character chat apps <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. The future of highly retentive and engaging consumer (and non-consumer) apps will likely involve creating characters that perform specific actions and interact in certain ways <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

## Why Build Voice AI Apps?

The tools available today allow for incredibly rapid development of engaging voice AI applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Interacting with a voice-enabled AI can be a "10x improvement in experience" compared to text-based interfaces like ChatGPT <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It's also more accessible than many might think, even for those without extensive coding knowledge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Essential Tools and Technologies

[[building_apps_with_ai | Building apps with AI]], especially voice-enabled ones, relies on several key components:

*   **Code Editor:** Cursor, hooked up with Large Language Models (LLMs) to assist with coding <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Voice AI Platform:** Daily is a crucial platform that handles the heavy lifting of voice and backend operations <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   **Pip Cats:** An earlier Daily library, more developer-focused, for easier interface with AI and building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    *   **Daily Bots:** A later offering from Daily that removes the need to handle LLM calls, simplifying development <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **LLMs:** Large Language Models, such as Llama 3.1 70B provided by Together AI, are the brain of the AI, taking in text and outputting responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Speech-to-Text (STT) Provider:** Converts spoken audio from the microphone into text for the LLM <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Text-to-Speech (TTS) Provider:** Converts the LLM's text response into spoken audio for the user <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Framework for Development:** Next.js, a framework that uses React, allows developers to set up a server and build web pages <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Deployment Platform:** Vercel provides a platform to host Next.js apps online, making deployment incredibly easy <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

## Step-by-Step Tutorial: Building a Weather Man App

A practical demonstration of [[building_a_weatherman_voice_app_with_ai | building a weatherman voice app with AI]] illustrates the process:

1.  **Start with a Demo Repository:** Begin by cloning the demo repository provided by Daily Bots, which runs in the browser <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This repository can be downloaded to your system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
2.  **Obtain API Key:** Sign up for Daily's service and retrieve your API key from their dashboard. This key unlocks access to Daily's services <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Configure API Key:** Paste the obtained API key into the `.env.local` file within your cloned repository <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  **Start the Server:** Run the command `yarn dev` to start the local development server <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
5.  **Configure Character Personality:** The core of defining the character lies in the configuration file. This file contains prompts that instruct the LLM on how to behave <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   **Prompt Engineering:** Understanding the prompt (the instructions given to the LLM) is crucial for defining the AI's persona and behavior <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   **Voice Selection:** The configuration also allows for changing the AI's voice, which is vital for the character's appeal <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   **Custom Characters:** You can easily edit the configuration file to create your own unique characters beyond the default presets <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
6.  **Implement Function Calling:** [[building_flexible_voice_ai_agents_with_vappy | Function calling]] enables the AI to perform "system stuff" or "computer stuff," such as calling APIs, getting data, or making posts <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   **Defining the Tool:** Add a tool definition (e.g., `weatherTool`) to the configuration, describing what the tool does and what parameters it accepts (e.g., `location`) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   **LLM Understanding:** The AI model is trained to understand functions and their required output format. Daily expects a specific message format (e.g., starting and ending with angle brackets around "function") to trigger actions <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
    *   **Handling the Function Call:** In your application code (e.g., `page.TSX`), define what happens when the AI "calls" a function (i.e., outputs the specific function call format). This involves aligning the function name with the tool defined earlier <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
    *   **Backend Logic:** The actual action (e.g., fetching weather) is handled by a backend route (e.g., `API/weather` in Next.js). This route contains the code to perform the desired operation <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. For the weatherman demo, the backend generated whimsical weather reports like "whimsical singing rainbows" <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
7.  **Deployment:** Once your app is functional locally, you can deploy it live online.
    *   **Vercel CLI:** Install the Vercel command-line interface tool <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
    *   **Log In:** Log in to your Vercel account via the CLI <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Deploy:** Simply type `vercel` into your terminal, and the app will be deployed and hosted on Vercel <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This makes the app accessible via a URL that can be shared <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

### Key Learnings from Development

*   **Small, Understandable Changes:** When building, especially with new technologies, it's beneficial to make small, iterative changes rather than trying to build a complex system all at once <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   **Leverage Existing Demos:** Starting with an existing demo repository and adding to it can significantly accelerate the learning and building process <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>.
*   **Read Documentation:** Developing a habit of reading and understanding documentation is crucial for problem-solving <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Use AI for Assistance:** If documentation is unclear, leverage LLMs like ChatGPT or Claude to ask questions and gain understanding <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **AI Output vs. Action:** Remember that LLMs primarily output text. The "magic" of function calling comes from the *system built around* the LLM that interprets this text output and performs real-world actions based on it <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Designing for Virality:** When [[innovative_app_ideas_using_ai | designing characters]], consider incorporating elements that can go viral, such as unexpected or whimsical responses that encourage social sharing (e.g., "raining pigs" or "singing rainbows") <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

## Practical Applications and Future Directions

[[practical_applications_of_voice_ai_in_startups | Practical applications of voice AI in startups]] are wide-ranging and include both B2B and B2C solutions <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. One example of an [[innovative_app_ideas_using_ai | innovative app idea using AI]] is a social app that allows users to have a FaceTime-like call with a VTuber (virtual YouTuber) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. These virtual characters embody avatars and have garnered millions of followers and significant income through subscriptions and merchandise <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.

This type of app, while more complex, utilizes voice AI platforms (like Pip Cat for greater developer control) to create a personalized, interactive experience that isn't possible with traditional content consumption <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>.

The ability to [[advanced_ios_development_techniques_using_ai | turn a web-based app into an iOS app]] is also entirely possible, expanding the reach and accessibility of these AI character creations <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>. What previously required large teams and significant venture capital can now be built by individuals, empowering a new wave of creators to launch unique AI character apps <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.