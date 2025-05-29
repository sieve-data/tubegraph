---
title: Integrating AI features into mobile apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Integrating [[ai_and_emerging_technologies_in_mobile_apps | AI]] into mobile applications can significantly enhance their functionality and user experience. Chris Barok, a developer who has built a large portfolio of native [[building_ios_apps_with_ai | mobile apps]] using [[ai_and_emerging_technologies_in_mobile_apps | AI]] and Cursor, shares his exact process and techniques <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. He emphasizes the opportunity for [[building_ios_apps_with_ai | iOS apps]], noting that people will "print millions of dollars doing it" <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Chris's success stems from using [[ai_and_emerging_technologies_in_mobile_apps | AI]] to supercharge his workflow, enabling him to build complex, robust applications like his daily planning app, Ellie, which boasts thousands of monthly active users <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Core Tools and Models

Chris primarily uses:
*   **Cursor:** His main tool, even for native [[building_ios_apps_with_ai | iOS development]] <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **ChatGPT-4o:** Utilized for [[aibased_feature_enhancements_in_software_development | asset generation]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Claude 3.7:** His preferred model for coding, especially for [[building_ios_apps_with_ai | iOS development]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **OpenRouter:** A service that allows easy swapping between over 300 different LLMs with just one line of code <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. It's particularly useful during development to test various models and their costs <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

## Building AI Features in a Native iOS App

Chris demonstrates the process by adding an [[ai_and_emerging_technologies_in_mobile_apps | AI]] chat feature to his budgeting app, Luna, allowing users to ask questions about their spending <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### Workflow for iOS Development
Chris's "jankst setup" for [[building_ios_apps_with_ai | iOS development]] involves:
1.  Opening the Xcode project in Cursor <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
2.  Using Cursor's chat feature to make file edits <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
3.  Switching back to Xcode to build and see the changes <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This process, while requiring switching, is substantially faster than pasting code into an LLM and then back into the IDE <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Manual Setup and Nuances
Cursor cannot set up the Xcode project. Developers must manually configure Xcode settings, such as embedding frameworks or enabling outgoing network requests <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This manual setup is crucial before using Cursor for code generation.

### Step-by-Step Feature Integration: AI Chat
1.  **Build the UI First:** Chris's key technique is to focus on creating the user interface (UI) with dummy data first, before hooking up the backend or live data <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This approach makes it easier for the [[ai_and_emerging_technologies_in_mobile_apps | AI]] to follow instructions by concentrating on a single task <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
    *   **Prompting:** Instruct Cursor to create a new tab for an [[ai_and_emerging_technologies_in_mobile_apps | AI]] chat, asking it to follow the existing UI style <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. Tagging the entire codebase provides the necessary context for the [[ai_and_emerging_technologies_in_mobile_apps | AI]] to understand the app's structure <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
    *   **UI Polish:** The [[ai_and_emerging_technologies_in_mobile_apps | AI]] can intuitively handle UX standards for chat apps, like message display and auto-scrolling <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
    *   **Visual Context:** Feeding screenshots into Cursor helps the [[ai_and_emerging_technologies_in_mobile_apps | AI]] better understand and replicate desired UI elements or fix issues <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

2.  **Hook up to an LLM:**
    *   **OpenRouter Integration:** Use OpenRouter to make the chat functional and allow swapping of chat models <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. This allows for dynamic model selection within the app <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
    *   **Documentation Feeding:** A powerful technique is to feed documentation (e.g., OpenRouter's API docs or Apple's documentation) directly into Cursor. This helps the [[ai_and_emerging_technologies_in_mobile_apps | AI]] understand necessary API calls and reduces hallucinations, especially for platform-specific development like [[building_ios_apps_with_ai | iOS]] <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

3.  **Improve Prompting for Better Responses:**
    *   **XML Format:** Formatting prompts in XML can lead to higher quality results from LLMs <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
    *   **Empathetic Prompting:** Ask the [[ai_and_emerging_technologies_in_mobile_apps | AI]] to adopt a persona (e.g., "concise like a friend") and specific response styles to improve the user experience <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

4.  **Realistic Mock Data Generation:**
    *   Using [[ai_and_emerging_technologies_in_mobile_apps | AI]] to generate less generic, more realistic mock data (e.g., restaurants in a specific city) greatly enhances testing and demoing the [[ai_and_emerging_technologies_in_mobile_apps | AI]] feature <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. This also helps with [[embedding_ai_for_app_virality_and_user_engagement | user engagement]] and potential virality <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.

5.  **[[embedding_ai_for_app_virality_and_user_engagement | Tool/Function Calling]] (Agents):**
    *   Instead of feeding massive amounts of data for every query, LLMs can be given "tools" or "functions" to call locally within the app <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.
    *   This allows the [[ai_and_emerging_technologies_in_mobile_apps | AI]] to decide when to fetch specific data (e.g., transactions for a particular date range) and reduces costs <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>.
    *   The LLM first assesses if it has enough context to answer a question. If not, it uses available tools to gather the necessary information, looping until it can provide a relevant answer <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. This transforms the chat into an "agent" with access to in-app capabilities <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>.

## Enhancements and Considerations

### Cost Monitoring
[[integrating_ai_with_existing_frameworks | Integrating AI]] into apps incurs costs. By calling OpenRouter's generation endpoint, developers can display the tokens used and the cost for each [[using_apis_in_ai_app_development | API]] call directly in the app <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. This is helpful for development and understanding potential production costs <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>.

### [[aibased_feature_enhancements_in_software_development | AI for Asset Generation]]
GPT-4o can be used to generate high-quality, consistent assets for apps. By providing a base asset, the [[ai_and_emerging_technologies_in_mobile_apps | AI]] can generate variations for loading screens, empty states, and other UI elements <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>. This adds a level of polish and delight to the app, making it more appealing to users <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

### Security Concerns
A significant challenge when [[integrating_ai_with_existing_frameworks | integrating AI]] is the security of [[using_apis_in_ai_app_development | API]] keys. Cursor might hardcode keys into the front end, which is dangerous as bots can find and misuse them, leading to unexpected costs <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>. Keys should ideally reside in the backend <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

## Advice for Developers and Non-Developers

### For Developers
*   Embrace [[ai_and_emerging_technologies_in_mobile_apps | AI]] tooling. Developers who learn to use these tools will "thrive for the next decade" <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. While some perceive it as "killing the art," its adoption is inevitable <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>.

### For Non-Developers
*   Use [[ai_and_emerging_technologies_in_mobile_apps | AI]] as a learning tool <a class="yt-timestamp" data-t="00:54:45">[00:54:45]</a>.
*   Start with tools like Replit or Lovable, which have more guardrails, as Cursor can be "dangerous" and lead to accidental critical errors like exposed [[using_apis_in_ai_app_development | API]] keys <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.
*   Learn programming fundamentals alongside [[ai_and_emerging_technologies_in_mobile_apps | AI]] to better understand and leverage the tools <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.

Chris's journey demonstrates that with the right tools and techniques, even individual developers can build a substantial portfolio of high-quality, [[ai_and_emerging_technologies_in_mobile_apps | AI-powered mobile apps]] <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.