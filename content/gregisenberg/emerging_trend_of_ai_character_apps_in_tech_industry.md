---
title: Emerging trend of AI character apps in tech industry
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

The tech industry is currently experiencing a significant shift towards the creation of voice-based AI character applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These applications are generating substantial revenue, and the concept of "characters" is being hailed as "the new apps" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This trend is accessible to both technical and non-technical individuals, with tools available that simplify the development process <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The best [[successful_ai_applications_and_startups | startups]] often start as seemingly simple "toys" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Building AI Voice Chat Apps

The process of [[creating_ai_voice_character_apps_with_daily_bots | building apps with AI tools]] often involves developing voice chat applications that function like an "audio ChatGPT" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This offers a significantly enhanced user experience compared to traditional text-based AI interactions <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Tools available today enable rapid development and deployment of these applications, even for those without extensive coding backgrounds <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. While some coding concepts (like GitHub, cloning a repo, and deployment) might need to be learned, the focus for developers is on configuring the bot's personality and core functionality <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Key Tools and Technologies

Several tools are central to [[building_apps_with_ai_tools | building apps with AI tools]]:
*   **Cursor**: A code editor integrated with Large Language Models (LLMs) for coding assistance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Daily (and Daily Bots)**: This company provides the core backend for voice processing and LLM calls, simplifying the development of voice agents and AI <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. [[creating_ai_voice_character_apps_with_daily_bots | Daily Bots]] removes the need for developers to handle LLM calls directly <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Previously, Daily offered a library called **Pip Cat**, which provided more developer control for interfacing with AI and building voice assistants <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Next.js**: A framework used for setting up servers that run React, allowing for the specification of routes and pages that execute code <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Vercel**: A platform that enables free hosting of Next.js applications online, offering simple deployment via a command-line interface (CLI) tool <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

### How Voice AI Characters Work

The underlying system of a voice AI character involves several steps <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
1.  **Speech-to-Text (STT)**: Audio input from a microphone is converted into text <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  **LLM Processing**: The text is sent to an AI model (like Llama 3.1 70B via Together AI) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. The LLM's behavior is configured via a simple file, defining its personality and how it should respond <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
3.  **Text-to-Speech (TTS)**: The LLM's text response is converted back into speech <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
4.  **Audio Output**: The speech is then streamed to the user's browser <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This entire complex process, including performance and error handling, is managed by platforms like Daily, allowing developers to focus on the character's function and personality <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Building a Weatherman Character App

As an [[examples_of_ai_integration_into_mobile_apps | example of AI integration into mobile apps]], a fully functional weatherman character app can be created <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This demonstration utilizes [[creating_ai_voice_character_apps_with_daily_bots | Daily Bots]] and involves several steps to configure its "personality" and add interactive capabilities:

### Configuring Personality

*   **Character Prompts**: The AI's default behavior is set via a "prompt" — a text instruction that tells the LLM how to act (e.g., "You are an assistant called Example Poot. You can ask me anything.") <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Voice Selection**: The voice of the AI is a crucial customizable element <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Custom Characters**: Developers can easily create their own characters by editing a configuration file, defining unique prompts and behaviors <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This allows for diverse character concepts, such as a "Gen Z middle schooler" or a "skateboard meme guy" <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Implementing Function Calling

Function calling (also known as tool calling) allows the AI to perform actions beyond just outputting text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **How it Works**: An LLM, when sufficiently intelligent, can follow instructions to output text in a specific format that indicates a function call <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. A system built around the LLM then intercepts this output and executes the corresponding code or API call <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Weather Tool Example**: To create a weatherman, a `get_weather` tool is defined for the LLM, specifying parameters like `location` <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   **API Integration**: When the AI "calls" `get_weather`, the system accesses a defined API route (e.g., `/api/weather`) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. In the demonstration, this API route was configured to return humorous, non-sensical weather conditions like "whimsical singing rainbows" or "flying pigs" <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. This not only validates the function call but also creates potential "TikTok moments" for viral content <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Deployment

Once developed, these applications can be easily deployed <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>. Using Vercel, a Next.js app can be made live on the internet with a single command (`vercel`) after logging in <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. The deployed app can be accessed on any device via a URL <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>. These web applications can also be converted into [[building_ios_apps_using_ai | iOS apps]] <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.

## Market Opportunity and Impact

The idea of "characters as the new apps" presents a massive opportunity <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Notable figures in the tech scene, such as Nikita Bier, initially viewed AI character chat apps as a fad but later acknowledged their significant retention graphs, indicating their staying power <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. The future of highly engaging consumer (and non-consumer) applications will likely involve [[creating_ai_employees_for_startups | creating AI employees for startups]] or characters that perform specific functions or act in certain ways <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This trend impacts both Business-to-Business (B2B) and Business-to-Consumer (B2C) sectors, transforming how people interact with content <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

## Real-World Application: The Vtuber Call App

A more advanced [[examples_of_ai_integration_into_mobile_apps | example of AI integration into mobile apps]] is an app that allows users to have a "FaceTime" call with a Vtuber <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. Vtubers are content creators who use software to embody virtual avatars, predominantly anime characters, for streaming on platforms like Twitch and YouTube <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. They have gained immense popularity, with millions of followers and significant earnings from subscriptions and merchandise <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.

The Vtuber app concept leverages voice AI to enable personal, one-on-one calls with these virtual characters, a level of interaction typically unavailable with human influencers <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. The developer of this app used the Pip Cat library for greater control over data flow, demonstrating how developers might transition to more granular tools as their understanding of AI systems deepens <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

## Conclusion

The ability to create sophisticated [[using_ai_in_mobile_apps | AI in mobile apps]] and character-based applications has been revolutionized by recent advancements in AI tools <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>. What previously required large teams and significant capital can now be accomplished by individuals, leading to a surge in innovative app development within the [[yc_startups_and_ai_niche_opportunities | AI niche opportunities]] <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. This emerging trend signifies a new era for content interaction and application design, with a low barrier to entry for creators to launch unique and engaging experiences.