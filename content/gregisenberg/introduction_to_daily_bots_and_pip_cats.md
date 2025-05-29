---
title: Introduction to Daily Bots and Pip cats
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

People are utilizing AI to develop voice character applications that are generating significant revenue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "character apps" are seen as the new frontier in applications <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Even without a technical background, it's possible to create a functional voice chat app, like the weatherman character demonstrated in this session <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

> [!info] The New Apps
> Characters are emerging as the new form of applications, presenting a significant opportunity for innovation and ideation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This trend is gaining traction, with insights suggesting that AI character chat apps are highly retentive and engaging, potentially shaping the future of consumer and non-consumer applications <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Daily Bots

Daily Bots is a company offering tools for building voice chat apps, often described as an "audio ChatGBT" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. It simplifies the creation of voice agents and voice AI, providing a 10x improvement in experience compared to text-based AI like ChatGBT <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Key Features and Functionality

Daily Bots performs the heavy lifting for voice and backend processes <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It handles [[understanding_apis_and_integrating_with_ai_models | LLM]] calls internally, meaning users don't need to manage them <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The platform provides easy configuration tools to customize bot behavior and voice <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

The core process of a Daily Bot involves:
1.  **Speech-to-Text (STT):** Takes audio input from a microphone and converts it into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing:** Pipes the text into an [[understanding_apis_and_integrating_with_ai_models | AI model]] (e.g., Llama 3.1 70B from Together AI) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Text-to-Speech (TTS):** Takes the LLM's text response and pipes it into a TTS provider <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output:** Pipes the generated speech back to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Daily Bots manages the complexities of this system, including performance and error handling <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a> <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Setting Up a Daily Bot

To set up a Daily Bot demo, users need to:
1.  Sign up on the Daily dashboard to obtain an [[understanding_apis_and_integrating_with_ai_models | API key]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  Clone (download) the Daily Bots demo repository from GitHub <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a> <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
3.  Paste the [[understanding_apis_and_integrating_with_ai_models | API key]] into the `.env.local` file <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
4.  Run the server using the `yarn Dev` command <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
5.  Access the bot via the local post URL in the browser <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

Users can modify bot personality by editing the configuration file, which directly correlates with the character selection screen in the demo <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a> <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This allows for [[creating_and_customizing_ai_agents_for_specific_use_cases | customizing AI agents]] or creating entirely new ones by defining prompts <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### Function Calling
Daily Bots supports function calling, enabling the bot to perform "system stuff" like [[understanding_apis_and_integrating_with_ai_models | calling APIs]], retrieving data, or making online posts <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a> <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

> [!definition] Function Calling
> Function calling is the process where an [[understanding_apis_and_integrating_with_ai_models | AI model]] (LLM), when sufficiently intelligent, can follow instructions to output text in a specific format that a surrounding system can interpret and use to execute functions. The LLM itself only outputs text; the system built around it performs the actions <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

Implementing function calling involves:
1.  **Defining the tool:** Specifying the tool's name and describing the parameters it accepts (e.g., location for a weather tool) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
2.  **AI Model Instruction:** The [[understanding_apis_and_integrating_with_ai_models | AI model]] is instructed on the functions it has access to and the specific format required for its responses <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
3.  **Action Execution:** The Daily system waits for a specific message format from the AI to understand that a function call is intended (e.g., `<function>`) <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
4.  **Server-side processing:** When the AI "calls" a function, the server executes the corresponding code (e.g., fetching weather data from an [[understanding_apis_and_integrating_with_ai_models | API route]]) <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

It is crucial for tool names to align between the definition and the AI's call to avoid errors <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Deliberately incorporating "nonsense" outputs (like "whimsical singing rainbows" for weather) can validate the function calling is working and create viral moments for the character <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a> <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Deployment
Daily Bots applications, built with Next.js, can be easily deployed online using Vercel <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a> <a class="yt-timestamp" data-t="00:30:18">[00:30:18]</a>. After logging into a Vercel account, a single command (`vercel`) can deploy the app live to the internet <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This allows users to share the character app with others across any device <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.

## Pip Cats
Pip Cats is another library, specifically more focused on developers, that simplifies interfacing with [[benefits_and_challenges_of_using_ai_tools_like_codex | AI tools]] to build voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. While Daily Bots handles LLM calls directly, Pip Cats offers developers more control over how data is passed around <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. This increased control is beneficial as developers gain more understanding of how these [[benefits_and_challenges_of_using_ai_tools_like_codex | AI systems]] operate <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>. An example of a complex app built using Pip Cats is a FaceTime-like call with a VTuber character <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.