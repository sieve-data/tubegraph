---
title: Building iOS apps using AI tools
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Building native iOS mobile applications is a significant opportunity, with the potential for individuals to generate substantial revenue <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. Chris, a developer who has built a large portfolio of polished and interesting mobile apps, demonstrates his exact process for [[prototyping_ios_apps_with_ai_tools | creating them using AI and Cursor]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. His approach allows a single individual to create robust applications that users might typically associate with a larger team <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

## Chris's Approach to AI-Powered App Development

Chris emphasizes a unique, advanced Cursor workflow for [[implementing_ai_in_app_development_processes | native iOS development]] <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. His method highlights how individuals can build complex applications over time by using AI to supercharge their workflow <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Key Tools Used

*   **Cursor:** The primary tool for coding and interacting with AI for code generation <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. Chris has used various tools like GitHub Copilot, Windsurf, and Claude Code, but finds Cursor most effective currently <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. It's surprising to many that Cursor can be used for native iOS development, as it's more commonly associated with React or Expo <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **ChatGPT 4o:** Used specifically for asset generation <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a> and brainstorming asset ideas <a class="yt-timestamp" data-t="52:54:00">[52:54:00]</a>.
*   **Claude 3.7:** Chris uses Claude 3.7 as his preferred language model, finding it the best for native iOS development, despite its tendency to "go off the rails" sometimes. He uses it to generate high-quality prompts <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Open Router:** A service that allows developers to easily switch between over 300 different AI models with a single line of code, making it invaluable for testing and development <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.

### Core Workflow for iOS Development

Chris's workflow involves opening the Xcode project directly in Cursor and using Cursor's chat feature to make file edits <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. After edits, he switches back to Xcode to build and verify the changes <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. While this involves switching between applications, it's significantly faster than manually pasting code into an LLM and back <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

> [!CAUTION] Setting Up Xcode Projects
> Do not use Cursor to set up the initial Xcode project <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. Many settings and framework embeddings must be done manually within Xcode, as Cursor cannot handle these tasks <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. For example, enabling outgoing network requests needs to be done manually in Xcode <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.

### Iterative Development Process with AI

Chris demonstrates his process by adding an AI chat feature to an existing budgeting app.

1.  **UI First Approach:** Chris's primary technique is to first focus on generating only the user interface (UI) with dummy data, then hooking up the backend or data afterwards <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>. This makes it easier for the AI to follow instructions by focusing on one task <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>. When prompting for UI, it's crucial to instruct the AI to follow the existing UI style of the app to ensure consistency <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
    *   **Result:** For the budgeting app, Cursor successfully created a new tab with a chat UI, matching the app's purple color scheme and even hardcoding animated responses <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
    *   **Troubleshooting:** Minor UI issues, like a hidden message area, were resolved with a few prompts <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.

2.  **Feeding Documentation:** A powerful technique is to feed documentation directly into Cursor. By copying and pasting a URL into Cursor (e.g., `@docs` command), it indexes the entire documentation of a service, providing context for API calls <a class="yt-timestamp" data-t="20:17:00">[20:17:19]</a>. This significantly reduces hallucinations, especially when working with platform-specific development like iOS or Mac apps <a class="yt-timestamp" data-t="20:53:00">[20:53:00]</a>.

3.  **Connecting to LLM (Open Router):** After the UI is complete, the next step is to make it functional by connecting it to an LLM <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.
    *   Chris used Open Router to allow quick model swapping, requesting a toggle in the UI for this purpose <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.
    *   He explicitly instructed the AI to use the last three months of transactions as context for questions <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.
    *   **Result:** Cursor generated two new files: `AI Chat View` for the UI and `Open Router Services` for handling API calls. The `Open Router Services` file was structured similarly to other existing services, demonstrating Cursor's understanding of the codebase's architecture <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>.

4.  **Prompt Optimization:** The quality of the prompt is paramount for AI app development <a class="yt-timestamp" data-t="26:46:00">[26:46:00]</a>. Chris uses Claude to generate effective prompts, often requesting them in XML format, which has shown a higher chance of producing good LLM results <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>. He specifies desired response styles, such as "concise" and "like a friend answering" <a class="yt-timestamp" data-t="28:26:00">[28:26:00]</a>.

5.  **Generating Realistic Mock Data:** To effectively test the AI feature and improve app demos, Chris uses AI to generate less generic mock data <a class="yt-timestamp" data-t="31:37:00">[31:37:00]</a>. He can request data specific to a demographic (e.g., "restaurants and places that look way more realistic for a 28-year-old male in Dallas") <a class="yt-timestamp" data-t="31:43:00">[31:43:00]</a>. This makes the app feel more real and helps users envision themselves using it <a class="yt-timestamp" data-t="32:57:00">[32:57:00]</a>.

### Advanced AI Integration: Tool/Function Calling (Agents)

To optimize costs and relevance, Chris implements tool or function calling, allowing the LLM to dynamically retrieve only necessary data <a class="yt-timestamp" data-t="35:58:00">[35:58:00]</a>. Instead of feeding all transaction history, the LLM can call specific local functions.

*   **Concept:** The LLM is given "tools" (functions) it can use. When a user asks a question, the LLM first assesses if it has enough context. If not, it checks if it has a tool to get the necessary information, calls the tool, and then uses the new context to answer <a class="yt-timestamp" data-t="38:19:00">[38:19:00]</a>.
*   **Implementation:** Chris prompted Cursor to create local tool functions for "get transactions for a specific date range" and "get the current budget" <a class="yt-timestamp" data-t="39:18:00">[39:19:00]</a>. He explicitly stated that these tools should be local and not call external APIs <a class="yt-timestamp" data-t="39:32:00">[39:32:00]</a>.
*   **Result:** The AI successfully generated functions that search the local database for relevant transactions based on date ranges <a class="yt-timestamp" data-t="41:26:00">[41:26:00]</a>. This transforms the chat from a simple query system into an agent with access to specific app functionalities <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>.

### Cost Monitoring

Chris integrated a feature to display the total tokens used and the cost of each AI call directly within the chat UI <a class="yt-timestamp" data-t="45:52:00">[45:52:00]</a>. This was achieved by making a simple call to Open Router's generation endpoint, which provides cost and token data <a class="yt-timestamp" data-t="46:06:00">[46:06:00]</a>. He also pulled all available Open Router models and their context window sizes and costs into the app for development insight <a class="yt-timestamp" data-t="47:27:00">[47:27:00]</a>.

### AI-Powered Asset Generation

Chris uses GPT40 for [[creating_ai_voice_character_apps | asset generation]], surprising many who ask about his high-quality app assets <a class="yt-timestamp" data-t="48:58:00">[48:58:00]</a>. The technique involves taking an initial mascot or character and then prompting GPT40 to generate infinite variations for use in loading screens, empty states, or other UI elements <a class="yt-timestamp" data-t="49:28:00">[49:29:00]</a>. Users can feed in existing images and request specific modifications (e.g., adding glasses, changing backgrounds, altering poses) <a class="yt-timestamp" data-t="49:37:00">[49:37:00]</a>. This allows for consistent styling across various assets <a class="yt-timestamp" data-t="49:57:00">[49:57:00]</a>.

### Security Concerns

A significant concern with [[using_ai_for_app_development | AI tools in app development]] is security <a class="yt-timestamp" data-t="24:07:00">[24:07:00]</a>. AI might inadvertently place sensitive information, like API keys, in the front-end of an app, which is dangerous <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>. Chris notes that bots are actively scanning publicly exposed code for such keys, leading to potential financial loss <a class="yt-timestamp" data-t="55:36:00">[55:36:00]</a>. Developers must manually correct such issues or use tools with stronger guardrails <a class="yt-timestamp" data-t="55:55:00">[55:55:00]</a>.

## Advice for Developers and Non-Technical Individuals

*   **For Developers:** Chris believes experienced developers will benefit most from [[ai_tools_for_app_development | AI tooling]] <a class="yt-timestamp" data-t="53:56:00">[53:56:00]</a>. He advises developers to embrace AI, as it's an inevitable technology, and those who learn to use it will thrive in the coming decade <a class="yt-timestamp" data-t="54:23:00">[54:23:00]</a>.
*   **For Non-Developers:** Non-developers should also consider [[using_ai_tools_to_build_saas_products | using AI tools]], but with caution. Chris recommends using tools like Replit or Lovable, which have more guardrails and are less likely to break things or expose sensitive data <a class="yt-timestamp" data-t="54:50:00">[54:50:00]</a>. He suggests learning programming basics and using AI as a teacher to build fundamental skills before diving into more complex tools like Cursor <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>.