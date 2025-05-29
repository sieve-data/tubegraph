---
title: Tool and function calling in AI applications
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Tool and function calling is a technique used in artificial intelligence (AI) applications to allow large language models (LLMs) to interact with external tools or functions, expanding their capabilities beyond their training data <a class="yt-timestamp" data-t="00:34:46">[:34:46]</a>. This capability is crucial for [[embedding_ai_to_enhance_app_functionality | embedding AI]] into applications that require dynamic, context-aware interactions <a class="yt-timestamp" data-t="00:24:53">[:24:53]</a>.

## The Concept of Tool and Function Calling

The primary motivation for using tool and function calling is to address the limitations of LLMs regarding real-time data access and specific actions, as well as to optimize costs <a class="yt-timestamp" data-t="00:35:08">[:35:08]</a>.

### Why it's Needed

*   **Context Limitations & Cost**: Directly feeding large amounts of data (e.g., a year's worth of transactions) into an LLM for every query can be very costly and inefficient, especially if the user only asks about a specific period (e.g., last week) <a class="yt-timestamp" data-t="00:35:08">[:35:08]</a>.
*   **Dynamic Data Retrieval**: LLMs, by default, do not have real-time access to user-specific data or the ability to perform actions. Tool calling allows them to "ask for" or "perform" these actions <a class="yt-timestamp" data-t="00:35:29">[:35:29]</a>.

### How it Works

When an LLM is given tools, its process involves a loop:
1.  **Initial Thought**: The LLM first assesses if it has enough context to answer the user's question <a class="yt-timestamp" data-t="00:38:23">[:38:23]</a>.
2.  **Tool Check**: If not, it checks if it has any available tools that could help obtain the necessary context or perform an action <a class="yt-timestamp" data-t="00:38:30">[:38:30]</a>.
3.  **Tool Execution**: If relevant tools exist, the LLM will call one of them, providing specific parameters (e.g., a date range for transactions) <a class="yt-timestamp" data-t="00:38:32">[:38:32]</a>.
4.  **Loop & Answer**: The tool executes its function, providing output back to the LLM. The LLM then re-evaluates if it now has enough context to answer the question. This process repeats until the question can be answered, or a predefined maximum number of loops is reached <a class="yt-timestamp" data-t="00:38:34">[:38:34]</a><a class="yt-timestamp" data-t="00:41:40">[:41:40]</a>.

### Connecting to Agents

This capability directly relates to the concept of AI agents. By providing an LLM with access to various tools, it essentially becomes an agent capable of performing actions and gathering information autonomously to fulfill complex requests <a class="yt-timestamp" data-t="00:36:53">[:36:53]</a>. The agent can leverage local functions within the application itself, not just external APIs <a class="yt-timestamp" data-t="00:37:10">[:37:10]</a>.

## Implementing Tool and Function Calling in iOS Apps

Chris, a developer, demonstrated how he implemented [[function_calling_in_ai_voice_apps | function calling]] in his native iOS budgeting app, Luna, using AI tools <a class="yt-timestamp" data-t="00:11:15">[:11:15]</a>.

### Tools Used

*   **Cursor**: The primary AI coding tool for making file edits and chatting with the AI <a class="yt-timestamp" data-t="00:04:30">[:04:30]</a><a class="yt-timestamp" data-t="00:07:31">[:07:31]</a>.
*   **Xcode**: Used for setting up the project manually, building the app, and making certain manual changes that Cursor cannot handle (e.g., embedding frameworks, enabling network requests) <a class="yt-timestamp" data-t="00:06:29">[:06:29]</a><a class="yt-timestamp" data-t="00:08:41">[:08:41]</a>.
*   **Open Router**: A service that unifies access to over 300 LLMs, allowing developers to switch models with a single line of code, which is invaluable for testing and development <a class="yt-timestamp" data-t="00:18:13">[:18:13]</a>.
*   **Claude (specifically 3.7)**: Used to generate high-quality prompts, especially when formatted in XML, which has shown to yield better results from LLMs <a class="yt-timestamp" data-t="00:27:26">[:27:26]</a>. Claude 3.7 was chosen for its performance in native iOS development <a class="yt-timestamp" data-t="00:05:50">[:05:50]</a>.

### The Prompting Process

1.  **Initial UI Generation**: First, the UI for the chat feature was generated with dummy data, ensuring the AI focused solely on the visual aspect <a class="yt-timestamp" data-t="00:13:19">[:13:19]</a>. The entire codebase was tagged to provide full context <a class="yt-timestamp" data-t="00:13:56">[:13:56]</a>.
2.  **Hooking up to LLM**: A prompt was then given to make the chat functional, using Open Router for model swapping and including a setting to toggle between models <a class="yt-timestamp" data-t="00:19:31">[:19:31]</a>. It was explicitly requested to use the last three months of transactions as context <a class="yt-timestamp" data-t="00:19:53">[:19:53]</a>.
3.  **Feeding Documentation**: A crucial technique is feeding in documentation (e.g., Open Router docs, Apple documentation) by copying and pasting the URL into Cursor. This allows the AI to understand API calls and reduce hallucinations <a class="yt-timestamp" data-t="00:20:17">[:20:17]</a><a class="yt-timestamp" data-t="00:20:50">[:20:50]</a>.
4.  **Improving Prompts**: Claude was used to generate a more refined prompt for the LLM's persona and response style, formatted in XML for better adherence to instructions (e.g., concise, friend-like answers) <a class="yt-timestamp" data-t="00:27:22">[:27:22]</a>.

### Defining Local Tools

To optimize cost and relevance, specific local tools were created:
*   **`getTransactionsForDateRange`**: A tool to fetch transactions within a user-defined date range, avoiding sending all data every time <a class="yt-timestamp" data-t="00:39:20">[:39:20]</a>.
*   **`getUsersCurrentBudget`**: A tool to retrieve the user's current budget information <a class="yt-timestamp" data-t="00:39:26">[:39:26]</a>.
*   **Local Implementation**: Explicitly stated that tools should be local functions within the app, not external API calls, to prevent hallucination <a class="yt-timestamp" data-t="00:39:32">[:39:32]</a>.

### Handling Errors

*   Screenshots of errors were fed directly into Cursor, prompting the AI to debug and fix the code <a class="yt-timestamp" data-t="00:39:58">[:39:58]</a>.

## Demonstrated Functionality

After the implementation, the budgeting app could dynamically use the defined tools:

*   **Dynamic Data Retrieval**: When asked questions like "Where did I eat last year?", the AI agent uses the `getTransactionsForDateRange` tool to pull only the relevant year's data, rather than a hardcoded three months, saving cost and improving accuracy <a class="yt-timestamp" data-t="00:42:52">[:42:52]</a>.
*   **Budget Analysis**: When asked "Am I overbudget anywhere?", the agent utilizes the `getUsersCurrentBudget` tool to access and analyze the user's budget, providing an informed response <a class="yt-timestamp" data-t="00:43:28">[:43:28]</a>.

The entire process, from UI to integrated [[function_calling_in_ai_voice_apps | function calling]] with an agent, took approximately four major prompts (excluding error corrections) <a class="yt-timestamp" data-t="00:44:43">[:44:43]</a>.

## Benefits and Future Potential

The ability to create and provide custom tools to LLMs opens up vast possibilities for app functionality:

*   **Complex Actions**: Agents can be equipped with tools to perform complex actions like generating reports, modifying budgets, or even interacting with financial APIs (e.g., Robin Hood) to manage investments on a user's behalf <a class="yt-timestamp" data-t="00:43:50">[:43:50]</a>.
*   **Enhanced User Experience**: By providing precise, context-aware answers and performing actions, the AI experience becomes more natural and useful <a class="yt-timestamp" data-t="00:43:00">[:43:00]</a>.
*   **Cost Optimization**: Only fetching necessary data via tool calls reduces token usage and associated costs <a class="yt-timestamp" data-t="00:35:38">[:35:38]</a>.
*   **Transparency**: Features like displaying token usage and cost in real-time allow developers to monitor and understand the operational expenses of their AI features <a class="yt-timestamp" data-t="00:47:09">[:47:09]</a>.