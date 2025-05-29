---
title: Integrating AI features in iOS apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris, a developer who has built a portfolio of mobile apps, uses AI tools like Cursor to create native iOS applications and put them on the App Store <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. He demonstrates how to add significant features with just a few prompts <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Chris emphasizes that while many tutorials cover weekend projects, his methods allow for the creation of complex, robust applications over time <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

> "People are always curious, can you build something like way more advanced? Um, what happens if you do this over a long period of time and you have AI? And I think this is exactly what happens. is like you can build some pretty serious complex things." <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>

## Key Tools Used for [[ai_app_development_strategies | AI App Development]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

Chris primarily uses:
*   **Cursor:** His main tool for coding, even for native iOS development, which he notes is not common <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. He has used various other tools like GitHub Copilot, Windsurf, and Claude Code but finds Cursor to be the most effective for his current workflow <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **ChatGPT 4o:** Used for asset generation, providing a high level of polish to his apps <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Its recent improvements in image generation have been particularly beneficial <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Claude 3.7:** The preferred LLM model for coding, especially for native iOS development <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. While Claude 3.7 can sometimes "go off the rails," Chris, as an experienced developer, can guide it effectively <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Open Router:** A service that allows developers to easily switch between over 300 LLM models with a single line of code, enabling rapid testing and comparison of different models <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Workflow for Native iOS Development with Cursor <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>

Chris's workflow for [[building_an_ios_app_using_ai | building an iOS app using AI]] with Cursor is unique:
*   **Xcode Integration:** He opens his Xcode project files directly in Cursor for editing <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. He uses Cursor's chat feature to make file edits, then switches back to Xcode to build and test the app <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. This method, though involving switching, is substantially faster than his previous approach of copy-pasting code into Claude <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Manual Project Setup:** A crucial caveat is that Cursor should *not* be used to set up the Xcode project initially <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Many settings and framework embeddings in Xcode must be done manually, as Cursor is not capable of handling these configurations via the terminal like it might for React Native <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Leveraging Screenshots and Documentation:** Chris frequently feeds screenshots of the app to Cursor to help it understand UI issues and desired layouts <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. He also consistently feeds Apple and API documentation (e.g., Open Router docs) into Cursor, which significantly reduces hallucinations and improves code accuracy, especially for iOS and Mac development <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

## Case Study: Building an AI Chat Feature in a Budgeting App

Chris demonstrates [[building_apps_using_ai_tools | building apps using AI tools]] by adding an AI chat feature to his existing budgeting app, Luna <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. The goal is to allow users to ask questions about their spending, similar to how some people manually export data to ChatGPT <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Initial UI Development <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>
Chris's strategy is to focus on the UI first, using dummy data <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Prompt:** He asked Cursor to create a new tab for an AI chat, requesting it to follow the app's existing UI style and hardcode dummy chat data <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. He also tagged the entire codebase to provide full context <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Results:** In one shot, Cursor generated a chat UI that matched the app's purple color scheme and even included an animation for responses <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. Chris manually added a chat icon <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The AI successfully implemented standard chat UX patterns, such as message placement and scrolling behavior <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### Integrating an LLM with Open Router <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>
After the UI was stable, Chris moved to integrating a live LLM using Open Router.
*   **Prompt:** He requested Cursor to make the chat functional (not hardcoded), use Open Router for model swapping, include a setting to toggle between models (e.g., GPT and Claude), and use the last 3 months of transactions as context for questions <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. He fed Open Router's documentation into Cursor to ensure proper API calls <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   **Code Structure:** Cursor generated two new files: `AI chat view` (for the UI) and `Open Router services` <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. It intelligently placed the Open Router service within the app's existing `services` folder, demonstrating its understanding of the codebase structure <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
*   **Security Note:** Chris highlights that for demo purposes, API keys were placed in the front end, but in a production app, these should reside in the back end for security <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. Exposed keys can lead to significant cost accumulation <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a>.

### Improving LLM Responses with Prompt Engineering <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>
The initial LLM prompt provided by Cursor was basic and produced unhelpful responses <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>. Chris used Claude to generate a more effective prompt.
*   **Prompt Generation with Claude:** He asked Claude to create a concise, friendly prompt in XML format, specifying guidelines like "Don't show your work unless asked" <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. XML formatting (e.g., `<budgeting_assist_instructions>`) is a technique that can yield better LLM results <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **Integrating the New Prompt:** He then told Cursor to inject this refined prompt into the app's LLM call <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. The improved prompt led to much better and more concise answers from the AI <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>.

> "If you can create a great prompt, the UX ultimately becomes way better. And if the UX comes better, you know, all your metrics are going to go up." <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>

### Generating Realistic Mock Data for Testing <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>
To better test the AI feature, Chris used AI to generate more realistic dummy data.
*   **Prompt:** He asked Cursor to make the mock data less generic, adding specific details like "restaurants and places that look way more realistic for a 28-year-old male in Dallas" <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.
*   **Benefit:** This realistic data makes demos more impactful and helps users envision themselves using the app, which is crucial for gauging interest in new startup ideas <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.

## Advanced AI Integration: [[function_calling_and_tool_integration_in_ai_apps | Function Calling and Tool Integration in AI Apps]] <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>

A common [[challenges_and_opportunities_for_ai_integration | challenge with AI integration]] is the cost of feeding large contexts (like a year's worth of transactions) to an LLM for every query <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>. Chris implemented **tool or function calling** (a core concept for AI agents) to address this <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.

*   **How Tool Calling Works:** LLMs can be given "tools" (functions) they can call <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>. When a user asks a question, the LLM first assesses if it has enough context to answer <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>. If not, it checks if any available tools can provide the necessary information <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. This process loops until it has sufficient context or reaches a defined maximum number of loops <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>.
*   **Implementing Local Tools:** Chris instructed Cursor to create local tool functions, avoiding external API calls unless necessary <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.
    *   **"Get Transactions for Date Range" Tool:** This tool filters and retrieves transactions from the local database based on a date range extracted by the LLM from the user's query <a class="yt-timestamp" data-t="00:40:52">[00:40:52]</a>.
    *   **"Get Current Budget" Tool:** This tool allows the AI to access the user's budget information <a class="yt-timestamp" data-t="00:40:57">[00:40:57]</a>.
*   **Benefits:** This approach significantly reduces costs by only feeding relevant data to the LLM when needed <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. It transforms the chat into an "agent" that can intelligently interact with the app's internal data and capabilities <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>.

## Monitoring Costs and Models <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>
To manage costs and understand model performance, Chris added features to display token usage and estimated cost for each AI interaction directly within the app's chat interface <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. He also enabled the app to pull and display a list of all available Open Router models, along with their context window sizes and costs <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>.

## AI for Asset Generation with GPT-4o <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>

Chris uses GPT-4o for generating high-quality visual assets for his apps, which can significantly enhance the user experience <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.
*   **Generating Variations:** He can take an existing mascot or image and prompt GPT-4o to generate infinite variations for use in loading screens, empty states, or other UI elements <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>. Examples include changing accessories (glasses, coffee cups), backgrounds, or even mimicking specific styles <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.
*   **Brainstorming:** AI can also be used to brainstorm initial app mascots or logos <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## Advice for Developers and Non-Technical People <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>

*   **For Developers:** Chris strongly encourages developers to embrace AI tooling, as those who know how to program stand to benefit the most by accelerating their workflows <a class="yt-timestamp" data-t="00:53:46">[00:53:46]</a>. He believes it's better to learn and adapt to these inevitable tools <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>.
*   **For Non-Technical People:** While AI tools are powerful, Chris advises non-developers to use them as learning tools rather than solely for building complex applications <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>. Tools like Replit or Lovable might be safer choices due to their "guardrails" compared to Cursor, which can "destroy things" if not used carefully <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>. He emphasizes the importance of learning basic programming fundamentals and using AI as a teacher for these basics before diving into more advanced AI coding platforms <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.
*   **Security Warning:** Be extremely cautious with API keys and other sensitive information; never hardcode them into the front end of an app, as bots can quickly find and exploit them, leading to significant unexpected costs <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>. This is a critical consideration for [[tips_for_developers_using_ai_in_app_development | developers using AI in app development]] and in [[the_role_of_ai_and_new_technologies_in_app_development | the role of AI and new technologies in app development]].