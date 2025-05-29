---
title: Using AI and cursor to build mobile apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroque has built a significant portfolio of mobile applications using [[building_apps_using_ai_tools | AI]] and [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to create them, including native [[building_an_ios_app_using_ai | iOS apps]] that can be launched in the App Store <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. His process involves [[the_role_of_ai_and_new_technologies_in_app_development | using AI]] agents within apps, leveraging Open Router, and integrating [[aipowered_mobile_apps | ChatGPT-4o]] for image generation <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Chris, a self-described "regular guy" who didn't attend Stanford or work at Google, demonstrates how a single individual can create robust apps with AI assistance <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Key [[tools_and_platforms_for_ai_app_development | Tools and Platforms]]

Chris's workflow is significantly [[the_role_of_ai_and_new_technologies_in_app_development | supercharged by AI]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. He primarily uses:

*   **[[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]]**: This is his main coding tool <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. He has used various AI coding tools over two years, including GitHub Copilot, Windsurf, and Claude Code, but finds [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to be the most effective for native [[building_an_ios_app_using_ai | iOS development]] <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **ChatGPT-4o**: Utilized for asset generation to add a high level of polish to apps <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Claude 3.7**: Chris prefers this model for its performance, especially in native [[building_an_ios_app_using_ai | iOS development]], despite its occasional tendency to "go off the rails" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. He leverages his development skills to guide it effectively <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Open Router**: A service that provides a unified API for over 300 different LLM models, allowing easy switching between models with a single line of code <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This is invaluable for testing and development <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

## Workflow for Native [[building_an_ios_app_using_ai | iOS App Development]] with [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]]

Chris's approach to [[building_an_ios_app_using_ai | native iOS development]] with [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] is unique:
*   **Xcode Integration**: He opens the Xcode project directly in [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to make edits using the chat feature <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. He then switches back to Xcode to build and test the app <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This process is significantly faster than his previous method of copying and pasting code into Claude <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Manual Project Setup**: A crucial [[best_practices_for_using_cursor_ai | tip]] is *not* to use [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to set up the Xcode project initially <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Manual setup within Xcode is necessary for tasks like configuring frameworks and enabling network requests, as [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] currently cannot handle these specific Xcode settings <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## [[building_an_ai_app_with_cursor_and_firebase | Building an AI Feature]] into an Existing App

Chris demonstrated how to integrate an [[aipowered_mobile_apps | AI]] chat feature into his existing budgeting app, Luna <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. The goal was to allow users to ask questions about their spending history <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Step 1: UI Creation with Dummy Data
*   **Prompt**: Chris asked [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to create a new tab for an [[aipowered_mobile_apps | AI]] chat, asking it to follow the app's existing UI and use hardcoded dummy data <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Strategy**: This phased approach (UI first, then data) helps the [[the_role_of_ai_and_new_technologies_in_app_development | AI]] focus on one task, increasing the chances of success <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. He also tagged the entire codebase to provide full context <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Result**: In one shot, [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] generated a highly polished chat UI, matching the app's purple color scheme and even including an animation for responses <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. Chris only had to manually add a chat icon <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. [[the_role_of_ai_and_new_technologies_in_app_development | AI]] models are well-trained on common UX patterns for chat interfaces <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

### Step 2: Integrating with an LLM (Open Router)
*   **Prompt**: Chris instructed [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to make the chat functional (not hardcoded) using Open Router, allowing for quick model swapping <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>. He also requested a setting to toggle between models and for the [[aipowered_mobile_apps | AI]] to use the last 3 months of transactions as context <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
*   **Strategy: Feeding in Documentation**: A key [[best_practices_for_using_cursor_ai | technique]] is to feed in relevant documentation (e.g., Open Router docs, Apple documentation) by simply pasting the URL <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This helps the [[the_role_of_ai_and_new_technologies_in_app_development | AI]] understand specific API calls and reduces "hallucinations," especially in Apple development environments <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   **Result**: [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] successfully integrated Open Router, created necessary files (e.g., `OpenRouterServices`), and set up the model toggle, all in one major prompt <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. It understood the existing app's structure for services <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

### Step 3: Improving the Prompt with Claude
*   **Initial Problem**: The [[the_role_of_ai_and_new_technologies_in_app_development | AI]]'s initial prompt was too simplistic, leading to poor answers <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.
*   **Strategy**: Chris used Claude to generate a better prompt <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. He found that formatting prompts in XML (e.g., `<budgeting_assist_instructions>`) increases the chance of producing good results from the LLM <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>. He asked Claude to create a prompt for a "budgeting assistant" persona that answers concisely, like a friend, without showing its work unless asked <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>. This empathetic approach to prompting is crucial for better user experience <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
*   **Integration**: He then provided this Claude-generated XML prompt to [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to improve the app's [[aipowered_mobile_apps | AI]] responses <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

### Step 4: Implementing Agent/Tool Calling
*   **Problem**: Initially, the [[aipowered_mobile_apps | AI]] chat was hardcoded to feed 3 months of transaction history, which could be costly and inefficient for varying user queries <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
*   **Solution**: Chris implemented LLM tool or function calling <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This allows the LLM to access specific local functions (tools) within the app to retrieve relevant data based on the user's query <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
*   **Prompt**: He asked [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] to create new tool functions, such as `get_transactions_for_date_range` and `get_current_budget`, explicitly stating they should be *local* functions and not call external APIs <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>. He also fed the Open Router tool calling documentation <a class="yt-timestamp" data-t="00:39:08">[00:39:08]</a>.
*   **Process**: The LLM first assesses if it has enough context. If not, it checks available tools, uses the appropriate tool, and then tries to answer <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. A loop limit (e.g., 4 times) is set to prevent infinite loops <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.
*   **Result**: In just a few prompts, [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] generated the tool definitions and the local functions to retrieve filtered transactions and budget information, allowing the [[aipowered_mobile_apps | AI]] to provide accurate, context-specific answers without wasteful data transfer <a class="yt-timestamp" data-t="00:40:28">[00:40:28]</a>.

### Step 5: Cost Monitoring and Dynamic Models
*   **Feature**: Chris added functionality to display the total tokens used and the cost of each [[aipowered_mobile_apps | AI]] call directly below the chat messages <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>.
*   **Dynamic Model List**: He also attempted to dynamically pull and display all available Open Router models, along with their context windows and costs, making it easier to test different models <a class="yt-timestamp" data-t="00:46:34">[00:46:34]</a>.

## Asset Generation with [[aipowered_mobile_apps | AI]]

Chris uses [[aipowered_mobile_apps | GPT-4o]] for generating high-quality app assets and illustrations <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   **Infinite Variations**: By providing an initial mascot or character, he can generate an infinite number of secondary assets for loading screens, empty states, and illustrations by prompting for specific modifications (e.g., "give it wired glasses and put it in front of a laptop") <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.
*   **Refinement**: He refines images through iterative prompting, even feeding in personal photos for the [[aipowered_mobile_apps | AI]] to mimic <a class="yt-timestamp" data-t="00:50:17">[00:50:17]</a>. While not always perfect (around 60-70% success rate), the efficiency gained is worth it <a class="yt-timestamp" data-t="00:51:12">[00:51:12]</a>.
*   **Brainstorming**: [[the_role_of_ai_and_new_technologies_in_app_development | AI]] can also help brainstorm initial app logos or mascots <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## [[tips_for_developers_using_ai_in_app_development | Tips for Developers Using AI]]

*   **Embrace [[the_role_of_ai_and_new_technologies_in_app_development | AI]]**: Developers should learn to use [[the_role_of_ai_and_new_technologies_in_app_development | AI]] tools, as it's an inevitable shift that will benefit highly skilled developers most <a class="yt-timestamp" data-t="00:53:46">[00:53:46]</a>. Those who adapt will thrive in the coming decade <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>.
*   **Realistic Mock Data**: Use [[the_role_of_ai_and_new_technologies_in_app_development | AI]] to generate realistic mock data (e.g., Dallas restaurants for a Dallas user) to improve testing and make app demos more compelling for potential users <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.
*   **Screenshot Errors**: When encountering errors, screenshot them and feed them back into [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]], instructing it to fix them <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.
*   **Security of API Keys**: Be aware that [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] may place API keys directly in the front end, which is a security risk <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. Such keys should ideally reside in the backend <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. Chris shared an anecdote about bots scanning publicly exposed applications for embedded API keys, leading to significant unexpected costs <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>.

## [[tips_for_developers_using_ai_in_app_development | Advice for Non-Technical Users]]

While [[the_role_of_ai_and_new_technologies_in_app_development | AI]] is powerful for non-developers, Chris recommends starting with [[tools_and_platforms_for_ai_app_development | tools]] like Replit or Lovable, which have more "guardrails" and are less likely to "destroy things" compared to [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. He advises learning programming basics and using [[the_role_of_ai_and_new_technologies_in_app_development | AI]] as a teacher to strengthen fundamental knowledge <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.

The ability to [[building_apps_using_ai_tools | build complex applications]] with just a few prompts using [[the_role_of_ai_and_new_technologies_in_app_development | AI]] tools like [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | Cursor]] represents a significant opportunity for developers and entrepreneurs alike <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.