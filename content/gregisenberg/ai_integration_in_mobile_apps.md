---
title: AI integration in mobile apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

## Overview

AI integration in mobile applications represents a significant opportunity for developers and non-technical individuals alike to create robust and highly polished products <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Chris, an experienced app developer, has leveraged AI tools to build a portfolio of native mobile apps, including several robust productivity applications like "Ellie," a daily planning app with thousands of active users <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. His success demonstrates the power of AI to supercharge development workflows, enabling the creation of complex applications that might otherwise require a large team <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Key Tools and Techniques

Chris primarily uses the following tools for [[integrating_ai_services_and_apis_in_app_development | integrating AI services and APIs in app development]] and [[building_ios_apps_with_ai | building iOS apps with AI]]:

*   **Cursor**
    *   Used for native iOS development, which is less common than its use for React and Expo development <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   The workflow involves opening the Xcode project file directly in Cursor, making edits using its chat feature, and then switching back to Xcode to build and debug <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This method is substantially faster than manually pasting code into an LLM and back <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   **Caveat**: Cursor is not recommended for setting up the initial Xcode project or for configuring manual settings like embedding frameworks or enabling outgoing network requests; these must be done manually in Xcode <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **ChatGPT 4o**
    *   Utilized for generating high-quality assets and illustrations for apps <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   Allows for the creation of an infinite number of secondary assets (e.g., for loading screens, empty states) from a single mascot image <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.
    *   Users can feed in existing images and provide prompts to modify them, adding details, changing backgrounds, or even mimicking specific styles <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>. The results are often very polished <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
*   **Claude 3.7**
    *   The preferred LLM model for its effectiveness in native iOS development <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   Chris leverages Claude to generate well-structured prompts, often in XML format, which has shown to yield better results from the LLM <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.

## Integrating AI in an Existing App (Case Study: Luna Budgeting App)

To demonstrate [[integrating_ai_in_existing_app_ideas | integrating AI in existing app ideas]], Chris showcased adding an AI chat feature to his existing budgeting app, Luna <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. The goal was to allow users to ask questions about their spending, similar to how some might export CSVs to ChatGPT <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Step-by-Step Integration

1.  **UI Generation (Prompt 1)**:
    *   Prompted Cursor to create a new tab for an AI chat, requesting it to follow the app's existing UI and use dummy data <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
    *   **Technique**: Focus on UI first with dummy data, then connect backend/data later. This increases the AI's success rate by allowing it to concentrate on one task <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
    *   The entire codebase was tagged to ensure the AI had the correct context for UI patterns <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
    *   The AI successfully generated a functional, hardcoded chat UI that matched the app's aesthetic <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. It even included a scrolling animation for messages <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   **Tip**: Constantly feed screenshots or target UIs to the AI for more accurate design replication <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

2.  **LLM Integration with Open Router (Prompt 2)**:
    *   **Open Router**: A service that unifies access to over 300 LLM models, allowing developers to switch models with a single line of code <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This is game-changing for testing different LLMs and monitoring costs during development <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
    *   Prompted Cursor to make the chat functional, integrate Open Router, add a setting to toggle between models, and use the last three months of transactions as context for responses <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
    *   **Technique**: Feed in documentation by copying and pasting the URL into Cursor (e.g., `@docs` then paste URL). This indexes the documentation, providing the AI with necessary API call context and reducing hallucinations, especially for platform-specific development like Apple <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
    *   Cursor generated two new files: an AI chat view and an Open Router service, structured similarly to existing services in the app <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

3.  **Prompt Engineering for Better Responses**:
    *   Initial AI-generated prompts were too basic and verbose <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.
    *   **Technique**: Use Claude to generate detailed prompts in XML format, specifying persona, response style (e.g., "like a friend"), knowledge areas, and instruction guidelines <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>. This significantly improves the quality and conciseness of the LLM's responses <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.
    *   The improved prompt ensures the AI provides concise, direct answers without unnecessary verbosity <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.

4.  **Implementing Tool/Function Calling (Agents)**:
    *   To optimize costs and relevance, instead of feeding in all transaction data every time, Chris implemented tool calling using Open Router <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.
    *   **Concept**: Tool calling allows the LLM to access and use specific functions (tools) within the application based on the user's query <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This transforms the chat into an agent that can interact with the app's local data <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
    *   **Process**:
        *   Defined tools for "get transactions for a specific date range" and "get current budget" <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.
        *   Explicitly instructed Cursor to keep tools local, avoiding external API calls unless intended <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.
        *   The LLM first determines if it has enough context to answer; if not, it identifies relevant tools, calls them, and then uses the results to answer the question, looping until sufficient context is gathered <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. Max loops can be set to prevent infinite loops <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.
    *   This feature allows the app to dynamically retrieve only necessary transaction data, making the interaction more efficient and cost-effective <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. It also enables complex queries, such as "Am I overbudget anywhere?" <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>.

5.  **Cost Monitoring and Model Switching**:
    *   Added functionality to display the total tokens used and the cost of each LLM interaction directly below the chat messages <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. This provides immediate feedback on usage and expense during development <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a>.
    *   Integrated a feature to dynamically pull and display all available Open Router models, along with their context window sizes and costs, although Chris noted some models don't support function calling <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>.

## Asset Generation for Polish and Humanization

Beyond functionality, [[using_ai_for_app_design_and_functionality | AI is also used for app design and functionality]] to add polish and "delight" to user experience <a class="yt-timestamp" data-t="00:52:24">[00:52:24]</a>:

*   **Mock Data Generation**: AI can generate realistic mock data (e.g., local restaurants, specific demographics) for testing and demos, making the app feel more authentic and relatable to potential users <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.
*   **Visual Assets**: ChatGPT 4o can generate high-quality character assets and illustrations. By feeding in a base image, AI can create variations for different scenarios like loading screens or empty states, ensuring visual consistency and depth <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.
*   **Brainstorming**: AI can assist in brainstorming app mascots or visual concepts, helping developers come up with unique and thematic assets <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## Security Considerations

A significant concern with AI-assisted development is security. Tools like Cursor, in their effort to automate, might place sensitive information (e.g., API keys) directly in the front end of the app <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This is a major vulnerability, as bots can scan open projects for such keys, leading to unauthorized use and accrued costs <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>. Developers must manually ensure API keys and other sensitive data reside on the backend <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

## Advice for Developers and Non-Developers

*   **For Developers**: Embrace AI tools. While it may feel taboo, AI is an inevitable force in development. Those who learn to leverage these tools will thrive in the coming decade, significantly accelerating their productivity <a class="yt-timestamp" data-t="00:53:54">[00:53:54]</a>.
*   **For Non-Developers**: AI tools offer immense potential, but caution is advised. Start with more "guarded" tools like Replit or Lovable, which have more safety rails to prevent accidental damage <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. It's also highly recommended to learn basic programming fundamentals and use AI as a teacher to build a stronger understanding before diving into more complex tools like Cursor <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.

Overall, [[the_potential_of_ai_in_app_development | the potential of AI in app development]] is vast, allowing individuals to build and scale sophisticated mobile applications with unprecedented speed and polish <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.