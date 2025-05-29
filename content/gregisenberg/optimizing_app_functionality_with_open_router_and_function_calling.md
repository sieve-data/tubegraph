---
title: Optimizing app functionality with Open Router and function calling
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

This article details how to enhance mobile app functionality by integrating Large Language Models (LLMs) using Open Router and implementing advanced function (tool) calling techniques. Chris Baro, a mobile app developer, shares his exact process for building complex, native iOS applications with AI assistance, specifically using Cursor. <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

## Leveraging AI in Mobile App Development

Chris has built a portfolio of robust mobile apps, including a daily planning app called Ellie with thousands of monthly active users and paid subscribers, and a budgeting app called Luna. <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. He attributes his ability to build such complex applications as a solo developer to the use of AI to supercharge his workflow. <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

Chris primarily uses Cursor for coding, having explored various AI coding tools like GitHub Copilot, Windsurf, and Claude Code over two years. <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. He also uses GPT-4o for asset generation. <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> For LLM models, he prefers Claude 3.7 for its performance, especially for native iOS development. <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Integrating AI Features into Existing Apps

To demonstrate, Chris illustrates how to add an AI chat feature to an existing budgeting app (Luna) that initially had no AI functionality. <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a> The goal was to allow users to chat with the app and ask questions about their spending, similar to how some people export data to ChatGPT. <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>

#### Step 1: Building the UI with Dummy Data

Chris's first step is to focus solely on the user interface (UI), using dummy data to increase the chances of the AI (Cursor) following instructions accurately. <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>

*   **Prompt:** "Create a new tab for an AI chat. Make the UI follow the similar UI as other parts of the app. Hardcode the chat with dummy data." <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>
*   **Context:** Tag the entire codebase (Luna folder) to ensure Cursor has the right context for the app's existing UI patterns. <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>, <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Emphasizing "follow the UI as similarly as the other parts of the app" prevents the AI from generating mismatched components. <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>
*   **Outcome:** Cursor successfully generated a functional chat UI with hardcoded responses and animations (like scrolling down on new messages), remarkably matching the app's existing aesthetic. <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>, <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>, <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Minor adjustments were needed to fix elements like the message area being hidden and scrolling behavior. <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>

> "Cursor knew exactly what to do." <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>

#### Tip: Using Screenshots for UI Adjustments

Chris often feeds screenshots of the app into Cursor to help it visualize and correct UI issues that are hard to describe with text. <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a> This technique helps the AI align with desired visual styles. <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>

#### Step 2: Hooking up to an LLM with Open Router

With the UI ready, the next step is to connect the chat to a live LLM using Open Router. <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>

*   **What is Open Router?** It's a service that centralizes access to over 300 LLM models, allowing developers to switch between models (e.g., Gemini, Claude, OpenAI) with a single line of code. <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>, <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. This is incredibly beneficial for testing different LLMs and monitoring costs during development. <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

*   **Prompt:** "Make this functional and not hardcoded. Use Open Router so I can swap out the chat model quickly. Put a setting at the top right so we can toggle between the models. When asking questions, use the last 3 months of transactions as context." <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>

*   **Key Technique: Feeding Documentation:** Chris highlights the ability to feed entire documentation URLs (e.g., Open Router docs) into Cursor using `@docs`. This allows Cursor to understand the API calls and context needed to integrate services without manual copy-pasting. <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>, <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>. This drastically reduces hallucinations, especially for platform-specific development like iOS or Mac apps where AI might generate non-existent features. <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>, <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

*   **Outcome:** Cursor successfully generated the necessary Swift files (`AI chat view` and `Open Router services`), connected the app to the LLM, and created a model toggle in the UI. <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>, <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>, <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. The AI even correctly structured the new service file based on existing app services. <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>

    *   **Security Note:** Chris points out that AI often places API keys directly in the front end, which is a security risk for production apps and should be moved to the backend. <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>

#### Step 3: Optimizing LLM Prompts for Better Responses

Initially, the LLM's responses were basic because of a simple prompt. Chris aims to create a more sophisticated prompt. <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>, <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.

*   **Technique: Claude for Prompt Generation:** Chris uses Claude (or "Clude" as he calls it) to generate high-quality, concise prompts. <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>, <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
*   **XML Formatting for Prompts:** Formatting prompts in XML (e.g., using tags like `<persona>`, `<response_style>`, `<knowledge_areas>`) significantly increases the likelihood of producing better results from the LLM. <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>, <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
*   **Prompt to Claude:** "I have a budgeting app. I want to add an AI chat to it. Give me a very good prompt in XML format so it can follow the instructions. Make it so the answers are very concise, like a friend answering it for you. Don't show your work unless asked and just answer the question." <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>
*   **Outcome:** The XML-formatted prompt from Claude provided a clear persona and response style, leading to more natural and concise answers in the app. <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>, <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

#### Tip: Generating Realistic Mock Data with AI

To better test the AI feature and make demos more compelling, Chris uses AI to generate realistic mock data. <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>

*   **Prompt:** "Make the mock data less generic. Add restaurants and places that look way more realistic for a 28-year-old male in Dallas." <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>
*   **Benefit:** This saves time by eliminating manual data generation and makes the app more relatable for user demonstrations or testing. <a class="yt-timestamp" data-t="00:31:56">[00:31:56]</a>, <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>. Realistic data helps users visualize themselves using the app. <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>

## Implementing Function Calling (Tool Calling) for Advanced Functionality

A key challenge was the high cost and inefficiency of sending all transaction history (e.g., three months or a year) to the LLM for every query, especially if the query only needed a specific date range. <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>, <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

The solution is **function calling** (also known as tool calling or agents), a feature in LLMs like Open Router and GPT that allows the AI to use specific tools (functions) to gather necessary context before responding. <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>, <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.

### How Tool Calling Works

1.  **User Query:** The user asks a question (e.g., "What did I eat last week?" or "Am I over budget?"). <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>
2.  **LLM Assessment:** The LLM first determines if it has enough context to answer the question. <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>
3.  **Tool Check:** If not, it checks if it has any available tools that can provide the missing context. <a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>
4.  **Tool Execution:** If a relevant tool exists, the LLM executes the tool (e.g., calling a function to retrieve specific data). <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>
5.  **Looping:** This process repeats until the LLM has sufficient information to answer the user's question, with a defined maximum number of loops to prevent infinite cycles. <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>, <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>, <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.

### Implementation of Function Calling

*   **Prompt:** "Create a new tool function that the LLM is able to call. I want to use function calling from Open Router. Create a few tools: a tool to get transactions for a specific date range, and a tool to get the current budget. Ensure all tools are local, not calling any external APIs." <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>
    *   Explicitly stating "local" was crucial to prevent AI from hallucinating external API calls, as function calling examples often involve external services. <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>

*   **Outcome:** Cursor successfully generated Swift code for two local tools: `getTransactionsForDateRange` and `getUserCurrentBudget`. <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>, <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>, <a class="yt-timestamp" data-t="00:40:57">[00:40:57]</a>. These tools search the app's local database to filter and retrieve data. <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>
    *   This enabled the app to answer questions like "Where did I eat last year?" by dynamically calling the `getTransactionsForDateRange` tool to retrieve only the relevant data. <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>
    *   It also allowed queries like "Am I over budget anywhere?" by calling the `getUserCurrentBudget` tool. <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>

> This [[function_calling_in_ai_to_enhance_chatbot_capabilities | function calling]] capability transforms the chat into an agent with access to specific tools, opening possibilities for complex actions like generating reports or modifying budgets directly within the app. <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>

## Monitoring Costs and Model Selection

Chris also implemented a feature to display token usage and estimated costs directly within the chat interface, which is highly beneficial for [[optimizing_and_troubleshooting_ai_app_performance | optimizing and troubleshooting AI app performance]]. <a class="yt-timestamp" data-t="00:45:53">[00:45:53]</a>

*   **Prompt:** "Alter the chat: right below the messages, I want to see the total tokens used and the cost. Make a call to Open Router's generation endpoint to pull runs and get cost/tokens. Pull all Open Router models and display them instead of hardcoding." <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>, <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>, <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.
*   **Outcome:** The app can now display tokens consumed and costs for each query. <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a> While not all models fully support function calling, Chris hardcoded a list of those that do, providing visibility into model context windows and costs. <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>, <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>, <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>. This transparency is invaluable for development and cost management. <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>

## Enhancing App Aesthetics with AI-Generated Assets

Beyond functionality, AI can significantly improve the visual quality of apps. Chris uses GPT-4o for asset generation. <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>

*   **Technique: Iterative Asset Generation:** By providing an initial mascot or character, GPT-4o can generate an "infinite number of secondary assets" for various uses like loading screens or empty states. <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>
*   **Examples:** Taking a ghost mascot, Chris generated variations like one with wire glasses in front of a laptop, or another floating with a coffee cup, maintaining the same artistic style. <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>, <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. He even fed an image of his dog to make an asset resemble his pet. <a class="yt-timestamp" data-t="00:50:17">[00:50:17]</a>
*   **Benefits:** This adds a unique visual dimension and "delight" to apps, helping them stand out from generic, "bare bones" designs. <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>, <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>, <a class="yt-timestamp" data-t="00:52:24">[00:52:24]</a>. AI can even assist in brainstorming initial logos or mascots. <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>

> This approach is part of [[optimizing_aienhancements_in_web_development | Optimizing AI enhancements in web development]] or mobile development, helping developers [[consumer_mobile_app_development_strategies | consumer mobile app development strategies]] and [[using_organic_growth_for_mobile_apps | using organic growth for mobile apps]] by making apps more engaging.

## Conclusion and Recommendations

Chris emphasizes that while AI tools can accelerate development, a foundational understanding of programming remains crucial, especially for advanced tasks and troubleshooting errors. <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>

*   **For Developers:** Embrace AI tools. Those who learn to leverage them will thrive. <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>, <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>.
*   **For Non-Developers:** AI can be a powerful learning tool. Start with more "guarded" platforms like Replit or Lovable, which have more safety checks, before moving to tools like Cursor that offer more freedom but also more risk. <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>, <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>, <a class="yt-timestamp" data-t="00:55:55">[00:55:55]</a>. Always be wary of security issues like hardcoded API keys. <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>, <a class="yt-timestamp" data-t="00:55:41">[00:55:41]</a>.

The techniques discussed, including using Open Router and [[function_calling_in_ai_to_enhance_chatbot_capabilities | function calling]] and detailed in this article, contribute significantly to [[advanced_workflow_techniques_for_mobile_app_development | advanced workflow techniques for mobile app development]] and overall [[ai_app_development_strategies | AI app development strategies]], addressing [[challenges_and_tips_in_aidriven_app_creation | challenges and tips in AI-driven app creation]]. For those interested in [[poly_app_functionality_and_features | Poly app functionality and features]], these principles can be broadly applied across various development environments.