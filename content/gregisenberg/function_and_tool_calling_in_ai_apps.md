---
title: Function and tool calling in AI apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Building robust AI applications involves more than just integrating a basic chat interface. A key strategy for creating powerful and cost-effective AI apps is the implementation of function and tool calling, which allows the AI to interact with its environment and perform specific actions based on user queries <a class="yt-timestamp" data-t="03:46:48">[03:46:48]</a>. This approach enables AI agents to dynamically retrieve relevant information and execute functions, leading to more accurate, efficient, and sophisticated responses <a class="yt-timestamp" data-t="03:57:56">[03:57:56]</a>.

## Why Use Function and Tool Calling?
Initially, AI apps might feed in large amounts of context (e.g., three months of transaction history) with every query, which can be inefficient and costly <a class="yt-timestamp" data-t="03:07:34">[03:07:34]</a>. For instance, asking "where did I eat last week?" with a full year's data is wasteful if only a week's data is needed <a class="yt-timestamp" data-t="03:50:09">[03:50:09]</a>.

Function and tool calling addresses this by allowing the AI to:
*   **Dynamically retrieve context**: Instead of feeding in all possible data, the AI can call specific tools to get only the necessary information (e.g., transactions for a specific date range) <a class="yt-timestamp" data-t="03:59:58">[03:59:58]</a>. This saves on latency and cost <a class="yt-timestamp" data-t="02:20:41">[02:20:41]</a>.
*   **Perform actions**: Beyond just answering questions, tools enable the AI to execute functions, such as retrieving a user's current budget or even modifying it <a class="yt-timestamp" data-t="04:37:34">[04:37:34]</a>. This transforms a simple chat into an [[ai_applications_for_automating_tasks | agent-based system]] <a class="yt-timestamp" data-t="04:57:56">[04:57:56]</a>.
*   **Reduce hallucinations**: By giving the LLM specific tools and documentation, it becomes less prone to "hallucinating" capabilities or actions that don't exist <a class="yt-timestamp" data-t="02:11:05">[02:11:05]</a>.

## Implementing Tool Calling with Cursor and Open Router
The process of [[building_apps_with_ai_tools | building apps with AI tools]] that leverage function calling, such as the budgeting app example (Luna), can be streamlined with platforms like Cursor and Open Router <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

### Core Tools Used
*   **Cursor**: An AI-powered code editor primarily used for native iOS development, though it also supports React and Expo <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>. It's used for making file edits and chatting with the AI model <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
*   **Open Router**: A service that integrates with over 300 LLMs, allowing developers to switch models with a single line of code <a class="yt-timestamp" data-t="01:28:30">[01:28:30]</a>. This is game-changing for testing different LLMs' responses and costs during development <a class="yt-timestamp" data-t="01:29:53">[01:29:53]</a>.
*   **Claude 3.7**: The preferred LLM model for native iOS development due to its performance, despite sometimes "going off the rails" for less experienced developers <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>.
*   **ChatGPT 4o**: Utilized for high-quality asset generation, allowing for the creation of unique, consistent, and polished illustrations for apps <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.

### Workflow for [[integrating_ai_in_existing_app_ideas | Integrating AI in Existing App Ideas]]
The general workflow for adding an AI feature to an existing app, like a budgeting app, follows these steps:

1.  **UI First (Dummy Data)**: Start by asking Cursor to create the UI for the new feature (e.g., an AI chat tab) using dummy data. Explicitly instruct the AI to match the existing app's UI <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>. This helps the AI focus on one task and increases the chances of success <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
2.  **Hook Up to LLM (Open Router)**: Once the UI is satisfactory, instruct Cursor to make it functional by connecting it to an LLM via Open Router <a class="yt-timestamp" data-t="01:57:50">[01:57:50]</a>. Request a setting to toggle between models and specify the initial context (e.g., last three months of transactions) <a class="yt-timestamp" data-t="01:57:50">[01:57:50]</a>.
3.  **Feed in Documentation**: Crucially, feed the LLM relevant documentation (e.g., Open Router docs, Apple documentation) by simply copying and pasting URLs <a class="yt-timestamp" data-t="02:17:17">[02:17:17]</a>. This indexes the documentation, giving the AI context for API calls and reducing hallucinations, especially in platform-specific development like iOS <a class="yt-timestamp" data-t="02:11:05">[02:11:05]</a>.
4.  **Refine Prompt Engineering**: The quality of the AI's responses is highly dependent on the prompt <a class="yt-timestamp" data-t="02:46:47">[02:46:47]</a>.
    *   Use a separate LLM (like Claude) to generate and optimize the base prompt, focusing on persona, response style, knowledge areas, and instruction guidelines <a class="yt-timestamp" data-t="02:26:50">[02:26:50]</a>.
    *   Format prompts in XML for higher chances of producing good results <a class="yt-timestamp" data-t="02:57:55">[02:57:55]</a>.
    *   Emphatically define desired response characteristics (e.g., "concise, like a friend answering") <a class="yt-timestamp" data-t="02:28:26">[02:28:26]</a>. This is a crucial step in [[building_successful_ai_apps | building successful AI apps]] by improving the user experience <a class="yt-timestamp" data-t="02:48:49">[02:48:49]</a>.
5.  **Implement Tool/Function Calling**: Define specific tools that the LLM can use, such as `getTransactionsForDateRange` or `getCurrentBudget` <a class="yt-timestamp" data-t="03:59:01">[03:59:01]</a>.
    *   The LLM will decide whether to answer directly or call a tool based on the query and available context <a class="yt-timestamp" data-t="03:57:56">[03:57:56]</a>.
    *   Specify that tools should be local functions, not external API calls, to prevent hallucination <a class="yt-timestamp" data-t="03:34:06">[03:34:06]</a>.
    *   Configure the maximum number of loops for tool calling to prevent infinite loops <a class="yt-timestamp" data-t="03:52:02">[03:52:02]</a>.
    *   This transforms the app into an agent that can intelligently retrieve and act on data <a class="yt-timestamp" data-t="04:57:56">[04:57:56]</a>.

> [!WARNING] Security Note:
> For speed and demo purposes, API keys might be placed in the front end <a class="yt-timestamp" data-t="02:39:56">[02:39:56]</a>. However, in production, these sensitive keys *must* reside in the back end to prevent security vulnerabilities and accidental racking up of costs by malicious bots <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. This highlights a critical aspect of [[levels_of_control_and_technical_requirements_of_ai_tools | levels of control and technical requirements of AI tools]].

## Enhancing the App and Workflow

### Generating Realistic Mock Data
For testing AI features, especially those that analyze user data, generating realistic mock data is crucial <a class="yt-timestamp" data-t="03:19:19">[03:19:19]</a>. AI can be used to create mock data that is less generic and more representative of actual user behavior (e.g., "add restaurants and places that look way more realistic for a 28-year-old male in Dallas") <a class="yt-timestamp" data-t="03:19:19">[03:19:19]</a>. This significantly improves the quality of AI testing and makes product demos more relatable and compelling <a class="yt-timestamp" data-t="03:56:08">[03:56:08]</a>.

### Cost Tracking and Model Insights
With Open Router, it's possible to query API calls to track tokens consumed and the associated costs <a class="yt-timestamp" data-t="04:42:06">[04:42:06]</a>. This allows developers to monitor expenses during development and gain insights into model performance and context windows <a class="yt-timestamp" data-t="04:57:04">[04:57:04]</a>.

### [[creative_workflows_and_tools_in_ai_design | Creative Workflows and Tools in AI Design]]
[[developing_user_interfaces_with_ai_tools | Developing user interfaces with AI tools]] and app assets can also be greatly enhanced:
*   **Asset Generation**: GPT-4o can be used to generate high-quality character assets and modify existing ones, creating variations for loading screens or empty states <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. This allows for consistent style and an infinite number of secondary assets <a class="yt-timestamp" data-t="04:58:28">[04:58:28]</a>.
*   **Brainstorming**: AI tools can help brainstorm initial app logos, mascots, or even "delight" features to humanize the app experience <a class="yt-timestamp" data-t="05:28:31">[05:28:31]</a>.

> [!TIP] Humanizing AI Apps:
> Beyond core functionality, focus on adding "delight" to the app through polished UI/UX, personalized content, and engaging visuals <a class="yt-timestamp" data-t="05:14:02">[05:14:02]</a>. AI can assist in brainstorming these elements, making the app more appealing to users <a class="yt-timestamp" data-t="05:28:31">[05:28:31]</a>.

## Conclusion
[[strategies_for_maximizing_the_potential_of_ai_tools | Strategies for maximizing the potential of AI tools]] in app development, such as function and tool calling, enable the creation of powerful, dynamic, and cost-effective AI applications <a class="yt-timestamp" data-t="04:57:04">[04:57:04]</a>. While there are [[levels_of_control_and_technical_requirements_of_ai_tools | technical requirements]] and potential pitfalls (like security risks), adopting these AI-powered workflows is seen as essential for developers and non-technical individuals alike to thrive in the evolving landscape of [[building_successful_ai_apps | building successful AI apps]] <a class="yt-timestamp" data-t="05:39:39">[05:39:39]</a>. Developers who embrace these tools are poised to accelerate their work, while non-developers can leverage them as learning instruments to grasp programming fundamentals <a class="yt-timestamp" data-t="05:40:40">[05:40:40]</a>.