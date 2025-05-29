---
title: Function calling and tool integration in AI apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

[[Building apps using AI tools | Building AI applications]] often involves more than simple question-and-answer interactions. Advanced AI applications can leverage **function calling** (also known as **tool integration**) to enable AI models to perform specific actions, retrieve dynamic information, and interact with the real world or a system's internal data. This capability transforms a basic chat interface into a powerful agent capable of executing complex tasks <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.

## The Need for Tools

Initially, AI applications might be built by feeding large amounts of context, like several months of transaction history, into the Large Language Model (LLM) for every query <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. While LLM context windows are growing (e.g., Gemini supporting 1 million tokens), this approach is inefficient and costly <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. For instance, if a user asks about spending from the last week, feeding two years' worth of transactions would be wasteful <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.

The challenge is to provide the AI with only the *relevant* information when needed, rather than a constant flood of data. This is where [[tools_and_platforms_for_ai_app_development | tool or function calling]] comes into play <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.

## How Function Calling Works

[[Tools and platforms for AI app development | Function calling]] allows LLMs to be given a set of "tools" they can choose to use <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>. This moves into the realm of [[integration_and_collaboration_features_in_ai_coding_platforms | AI agents]], which can execute more sophisticated workflows <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.

The process generally follows these steps:
1.  **User Query**: The user asks a question or gives a command.
2.  **LLM Evaluation**: The LLM first assesses if it has enough internal context to answer the user's question <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.
3.  **Tool Check**: If not, it checks if it has any available tools that could help answer the question <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
4.  **Tool Execution**: If relevant tools exist, the LLM determines which tool to use, extracts the necessary parameters (e.g., a date range from the user's query), and "calls" that tool <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>.
5.  **Context Augmentation**: The tool executes (e.g., retrieving specific transactions from a database) and returns its output to the LLM <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.
6.  **Looping**: The LLM then re-evaluates the question with the new context provided by the tool's output. This process can loop until the LLM has sufficient information to formulate an answer, with a maximum loop count to prevent infinite loops <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>, <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

## Implementing Tools with Cursor and Open Router

For [[integrating_ai_tools_in_building_saas_startups | integrating AI tools]] in a budgeting app built for iOS, the following steps demonstrate how to implement function calling using Cursor and Open Router:

### 1. Initial UI Setup
The first step is to establish the UI for the chat feature. Using Cursor, the instruction was to "create a new tab for an AI chat" and "make the UI for this" using dummy data and following the app's existing UI style <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. It is crucial to focus on the UI first, as it helps the AI concentrate on a single task <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

*   **Tips for UI generation**:
    *   Explicitly tell the AI to "follow the similar UI as other parts of the app" to maintain consistency <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
    *   Tagging the entire codebase provides the AI with necessary context about the app's structure and existing components <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
    *   Feed screenshots of the desired UI or existing app components to the AI to guide its generation <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>, <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

### 2. Integrating the LLM (Open Router)
Once the UI is set, the next step is to make the chat functional by connecting it to an LLM. Open Router is used because it allows seamless swapping between over 300 different AI models with a single line of code, aiding in testing and optimization <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>, <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

*   **Prompt**: "Can you make this functional and not hardcoded? Can you use open router so I can swap out the chat model quickly? And can you put a setting at the top right so we can toggle between the models?" <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Documentation Feeding**: A critical technique is to feed the LLM the official documentation (e.g., Open Router docs, Apple documentation) by simply copying and pasting the URL into Cursor's `@docs` feature <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>, <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. This reduces hallucinations, especially in platform-specific development like iOS <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>, <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

### 3. Implementing Function Calling (Agents)
To optimize costs and relevance, function calling is introduced. Instead of sending all transactions with every query, the AI will use a tool to fetch only relevant data.

*   **Prompt**: "Can you actually create a new tool function that the LLM is able to call? I want to use function calling from Open Router. Can you create a few tools? So maybe a tool to get the transactions for a specific date range. And then just for fun, I said, 'Okay, let's just also feed in a tool to maybe get the current budget.'" <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Local Tools**: Explicitly instruct the AI that "all the tools to be local" and "we're not calling any external APIs" to prevent the AI from hallucinating external API calls <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.
*   **Error Handling**: Screenshot errors and feed them back into Cursor with a prompt like "Can you fix it?" <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>.
*   **Result**: The AI generates tool definitions and functions like `getTransactionsForDateRange` and `getCurrentBudget` that search the local database for relevant information <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>.

## Benefits and Applications

Integrating tools into AI apps offers significant advantages:

*   **Cost Efficiency**: Reduces token usage by only fetching necessary data <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.
*   **Enhanced Capability**: Allows the AI to perform complex, dynamic tasks within the application's context, such as summarizing specific periods or checking budgets <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a>.
*   **Agentic Behavior**: Transforms the AI from a simple chatbot into an "agent" that can analyze a request, determine the best course of action (e.g., calling a specific function), and then execute it <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>, <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>.
*   **Future Potential**: With access to more tools (e.g., APIs for reports, budget modification, or external services like Robinhood), the agent could become incredibly powerful, handling tasks like rebalancing budgets or even making investments <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>, <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>.

## Important Considerations

*   **Security**: Be cautious about hardcoding sensitive information, like API keys, in the frontend. This is a security risk and should ideally be managed on the backend <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>, <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.
*   **Prompt Engineering**: The quality of the AI's responses heavily depends on the prompt. Using structured formats like XML for prompts can lead to better results <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>. It's also beneficial to specify the desired response style, such as "concise like a friend answering it for you" <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.
*   [[Comparison of AI coding tools | Tool Compatibility]]: Not all LLM models support function calling consistently, so it's important to verify compatibility when selecting models <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>.

Overall, [[integrating_ai_features_in_ios_apps | integrating AI features in iOS apps]] through function calling and tool integration with platforms like Cursor and Open Router demonstrates a powerful workflow for [[combining_different_ai_tools_for_effective_development | effective AI app development]] and [[building_ai_startup_using_ai_tools | building AI startups]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>. This approach allows developers to create more sophisticated, responsive, and cost-effective AI-powered applications.