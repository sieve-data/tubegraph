---
title: Building native iOS apps with AI and cursor
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroque has built a substantial portfolio of clean and interesting mobile applications, many of which he believes can achieve significant Monthly Recurring Revenue (MRR) <a class="yt-timestamp" data-t="01:16:18">[01:16:18]</a>. He achieves this by leveraging Artificial Intelligence (AI) to supercharge his development workflow <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Chris focuses on [[building_ios_apps_with_ai | native iOS development]], which he notes is not commonly seen with AI tools like Cursor <a class="yt-timestamp" data-t="02:14:10">[02:14:10]</a> <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

## Chris's Portfolio and AI Use

Chris's portfolio includes several robust productivity apps, such as "Ellie," a daily planning app with thousands of monthly active users and around 2,000 paid users <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. Other apps include a budgeting app and a personal CRM <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. He emphasizes that the complexity and polish of these apps are only possible due to his use of AI, demonstrating that AI can facilitate the creation of serious, complex projects over time, not just weekend prototypes <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

## Tools and Models Used

Chris's primary tool for development is [[using_tools_like_cursor_ai_for_functionality_and_vz_for_ui | Cursor AI]] <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. He has explored many other AI coding tools over two years, including GitHub Copilot, Windsurf, and Claude Code <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

For asset generation, he utilizes ChatGPT 4o, specifically for image generation, which has significantly improved the visual polish of his applications <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a> <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.

Regarding Language Model (LLM) choices, Chris primarily uses Claude 3.7, finding it to be the [[best_practices_for_using_cursor_ai | best model for native iOS development]], despite its occasional tendency to "go off the rails" <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a> <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. He has also experimented with Gemini and other models <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

## Cursor Workflow for iOS Development

Chris employs a unique, "janky" setup for [[building_ios_apps_with_ai | building native iOS apps]] with Cursor <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>:
*   He opens the Xcode project file directly in Cursor <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
*   He uses Cursor's chat feature to make file edits <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   He then switches back to Xcode to build and run the application, repeating this process <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. This method, while involving switching between tools, is significantly faster than his previous method of copying and pasting code into Claude and back <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

### Important Caveats for Xcode Projects
A critical tip for using Cursor with Xcode is **not to use Cursor to set up the initial Xcode project** <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. Manual setup is required for many Xcode-specific configurations, such as:
*   Project settings <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   Selecting and embedding frameworks <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   Enabling specific capabilities like outgoing network requests (which Apple requires manual enabling for) <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
Cursor, unlike with React Native, cannot perform these actions via the terminal for Xcode projects <a class="yt-timestamp" data-t="09:24:00">[09:24:24]</a>. Developers should manually set up the project and then open it in Cursor <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

## Building an AI Feature (Budgeting App Example)

Chris demonstrated the process of [[embedding_ai_to_enhance_app_functionality | embedding AI to enhance app functionality]] by adding an AI chat feature to his existing budgeting app, Luna <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. The goal was to allow users to ask questions about their spending history directly within the app <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.

### Phase 1: UI Generation
*   **Prompt**: Chris first instructed Cursor to create a new tab for an AI chat, focusing solely on the UI with dummy data, and to follow the existing UI style of the app <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
*   **Technique**: He emphasizes building the UI first with dummy data before hooking up the backend or live data, as this makes it easier for the AI to focus and follow instructions <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>.
*   **Context**: He tagged the entire codebase for Cursor to have the necessary context of the app's structure and existing UI <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>.
*   **Result**: In one shot, Cursor generated a fully functional chat UI with hardcoded data and even animations for sending messages, closely matching the app's purple color scheme and UX patterns (e.g., sender/receiver bubbles, scrolling) <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a> <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.
*   **Troubleshooting**: Minor issues, like the message area being hidden, were fixed with subsequent prompts, often aided by feeding screenshots of the UI problem into Cursor <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a> <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.

### Phase 2: Integrating with LLM (OpenRouter)
*   **OpenRouter**: Chris explained OpenRouter as a service that integrates with over 300 LLMs, allowing developers to swap models with a single line of code, which is invaluable for testing during development <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.
*   **Prompt**: The next major prompt asked Cursor to make the chat functional by connecting it to OpenRouter, allowing model swapping, and providing the last 3 months of transactions as context <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.
*   **Key Technique (Documentation Feeding)**: Chris consistently feeds external documentation (e.g., OpenRouter docs, Apple documentation) into Cursor. This allows Cursor to index the service's API calls and significantly reduces hallucinations, especially for platform-specific development like iOS <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a> <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.
*   **Result**: Cursor successfully connected the chat to the LLM via OpenRouter and integrated a model toggle. It generated two main files: an `AI chat view` for the UI and an `Open Router services` file, demonstrating its understanding of the app's service structure based on the codebase <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.
*   **Security Concern**: API keys were placed in the frontend for demo purposes, but Chris noted they should ideally reside in the backend due to security risks <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>.

### Phase 3: Prompt Optimization and Data Management
*   **Prompt Improvement**: The initial prompt generated by Cursor for the LLM was too simplistic <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>. Chris used Claude ("Clude") to generate a more effective prompt <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>.
*   **Technique (XML Formatting)**: He asked Claude to provide the prompt in XML format, which he found increases the chances of producing better results from the LLM <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>. The prompt included persona, response style (concise, like a friend), knowledge areas, and instruction guidelines <a class="yt-timestamp" data-t="28:42:00">[28:42:00]</a>.
*   **Realistic Mock Data**: To test the AI feature effectively, Chris used AI to make his mock data less generic <a class="yt-timestamp" data-t="31:37:00">[31:37:00]</a>. He prompted Cursor to create realistic restaurant and location names for a 28-year-old male in Dallas, which significantly improved the demo's relatability <a class="yt-timestamp" data-t="31:41:00">[31:41:00]</a>. This technique saves time and helps visualize the app with real data, making product demos more impactful <a class="yt-timestamp" data-t="32:24:00">[32:24:00]</a>.

### Phase 4: Implementing Tool/Function Calling (Agents)
*   **Problem**: Constantly feeding large amounts of transaction history (e.g., 3 months or a year) to the LLM is costly and inefficient, especially if the user only asks about recent spending <a class="yt-timestamp" data-t="35:07:00">[35:07:00]</a>.
*   **Solution**: Chris implemented tool or function calling, a feature in LLMs like OpenRouter and GPT that allows the LLM to access and use defined "tools" (functions) <a class="yt-timestamp" data-t="36:43:00">[36:43:00]</a>. This moves into the realm of [[developing_ai_character_apps_with_customization | AI agents]] <a class="yt-timestamp" data-t="36:53:00">[36:53:00]</a>.
*   **How it Works**: The LLM first assesses if it has enough context to answer a user's question. If not, it identifies if it has tools at its disposal that can provide the necessary information. It then calls the relevant tool (a local function in this case) to fetch the data, and then answers the question, looping until it has sufficient context <a class="yt-timestamp" data-t="37:20:00">[37:20:00]</a> <a class="yt-timestamp" data-t="41:39:00">[41:39:00]</a>.
*   **Prompt**: Chris instructed Cursor to create tools for getting transactions within a specific date range and getting the user's current budget <a class="yt-timestamp" data-t="39:18:00">[39:18:00]</a>. He explicitly told Cursor to make these tools local functions, not external API calls, to prevent hallucination <a class="yt-timestamp" data-t="39:32:00">[39:32:00]</a>.
*   **Result**: After a few prompts and error corrections, Cursor successfully generated the tool definitions and the local functions to retrieve relevant data from the app's database <a class="yt-timestamp" data-t="40:16:00">[40:16:00]</a>. This transformation meant the app was no longer just a chat interface but an agent with access to specific tools <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>. For example, asking "am I overbudget anywhere?" triggers the budget tool, providing a direct answer based on the user's budget <a class="yt-timestamp" data-t="43:23:00">[43:23:00]</a>. This opens possibilities for [[innovative_ai_functionalities_in_apps | advanced AI functionalities]] like generating reports or rebalancing budgets <a class="yt-timestamp" data-t="43:50:00">[43:50:00]</a>.

### Phase 5: Cost Tracking and Model Display
*   **Cost Display**: Chris implemented a feature to display the total tokens used and the cost for each chat interaction, by having Cursor make calls to OpenRouter's generation endpoint <a class="yt-timestamp" data-t="45:52:00">[45:52:00]</a>.
*   **Model Display**: He also had Cursor pull and display all available OpenRouter models directly in the app, showing their context window sizes and costs, which is useful for development <a class="yt-timestamp" data-t="47:26:00">[47:26:00]</a>. (Note: Some models were hardcoded to support function calling consistently) <a class="yt-timestamp" data-t="47:39:00">[47:39:00]</a>.

## Asset Generation with ChatGPT 4o

Chris extensively uses GPT-4o for generating high-quality character assets and illustrations for his apps, which adds a significant layer of polish <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a> <a class="yt-timestamp" data-t="49:00:00">[49:00:00]</a>.

*   **Workflow**: He starts with a base asset (either AI-generated or existing) and then prompts GPT-4o to generate variations <a class="yt-timestamp" data-t="49:26:00">[49:26:00]</a>. This allows for creating an "infinite number of secondary assets" for various uses like loading screens or empty states <a class="yt-timestamp" data-t="49:28:00">[49:28:00]</a>.
*   **Examples**: He demonstrated modifying a ghost mascot with wired glasses and a laptop, or changing background colors and adding elements like coffee cups <a class="yt-timestamp" data-t="49:37:00">[49:37:00]</a>. He even fed an image of his own dog and asked GPT-4o to make the mascot look more like it <a class="yt-timestamp" data-t="50:17:00">[50:17:00]</a>.
*   **Specificity**: While powerful, it requires specific prompting and gets it right 60-70% of the time, which is still worthwhile <a class="yt-timestamp" data-t="51:07:00">[51:07:00]</a>.
*   **Impact**: Integrating these [[developing_a_user_interface_using_ai_tools | AI-generated illustrations]] into the app, like the dog mascot at the top of the chat, adds a unique dimension and makes the app more visually appealing <a class="yt-timestamp" data-t="51:34:00">[51:34:00]</a>. This contrasts with common "bare bones" apps and allows for "humanizing" the product with small delightful details <a class="yt-timestamp" data-t="51:55:00">[51:55:00]</a>.

## General Advice for Building Apps with AI

*   **For Developers**: Chris encourages developers to embrace AI tooling, as those who learn to use it effectively will "thrive for the next decade" <a class="yt-timestamp" data-t="53:43:00">[53:43:00]</a>. He acknowledges some perceive it as "killing the art" but emphasizes its inevitability <a class="yt-timestamp" data-t="54:19:00">[54:19:00]</a>.
*   **For Non-Developers**: Non-developers should use AI as a learning tool to grasp programming fundamentals <a class="yt-timestamp" data-t="54:45:00">[54:45:00]</a>. He suggests using tools like Replit or Lovable, which have more "guardrails" compared to Cursor, which can be "dangerous" and prone to misconfigurations (e.g., embedding API keys in the frontend, leading to cost issues) <a class="yt-timestamp" data-t="54:51:00">[54:51:00]</a> <a class="yt-timestamp" data-t="55:55:00">[55:55:00]</a>. Learning basics alongside AI use is key <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>.

The ability to [[building_apps_with_ai_tools | build apps with AI tools]] and rapidly iterate on features, coupled with smart prompt engineering and asset generation, offers a powerful path to creating polished and functional mobile applications.