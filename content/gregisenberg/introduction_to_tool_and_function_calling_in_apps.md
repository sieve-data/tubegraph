---
title: Introduction to tool and function calling in apps
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Tool and function calling is a technique used in [[AI tools for app development | AI applications]] that allows Large Language Models (LLMs) to interact with external tools or functions to retrieve specific information or perform actions [00:36:43 | 00:36:48]. This method addresses the limitations of LLMs, such as high costs and inefficiency when processing large datasets directly [00:35:09 | 00:35:38].

## What is Tool and Function Calling?

Traditionally, when an LLM needs specific data (e.g., transaction history), an initial LLM might parse a user's message to determine the required data range, then call a function to retrieve that data, and finally pass it to a second LLM for answering [00:36:12 | 00:36:32].

However, tool and function calling streamlines this by allowing a single LLM to directly access and utilize predefined tools [00:36:48]. This means you can "give it tools to use" [00:36:48]. This capability brings [[AI tools for building software | AI apps]] into the realm of [[ai_applications_in_daily_tasks_and_productivity | agents]], where the AI can intelligently decide when and how to use external functions [00:36:51 | 00:37:01]. The tools can be external APIs or even local functions built directly into the application [00:37:07 | 00:37:12].

## Benefits and Purpose

The primary motivation for implementing tool and function calling is efficiency and cost-effectiveness. Instead of feeding an entire dataset (e.g., years of transaction history) to the LLM for every query, the LLM can use a tool to fetch only the relevant data based on the user's question [00:35:09 | 00:35:15]. This prevents wasteful processing of unnecessary information, especially for specific queries like "Where did I eat last week?" versus "Summarize the last year?" [00:35:42 | 00:35:52].

By integrating function calling, an application moves beyond simple chat functionalities, evolving into an agent that can access and utilize specific information or capabilities within the app [00:44:56 | 00:45:00]. This dramatically increases the power and utility of the [[AI tools for app development | AI application]] [00:44:49 | 00:44:51].

## Implementation Process

Implementing tool and function calling involves several steps, as demonstrated with a budgeting app:

### 1. Defining Tools
The LLM is provided with a list of available tools, along with their definitions. For example, a budgeting app might define:
*   `getTransactionsForDateRange`: A tool to retrieve transactions for a specified date range [00:39:20 | 00:39:22].
*   `getCurrentBudget`: A tool to fetch the user's current budget [00:39:26 | 00:39:27].

These definitions include parameters (e.g., `startDate`, `endDate` for `getTransactionsForDateRange`) and specify if parameters are required [00:41:02 | 00:41:06]. Crucially, these tools can be *local functions* within your app, not just external API calls [00:39:32 | 00:39:34].

### 2. LLM Decision Process
When a user asks a question, the LLM follows a logical flow:
*   **Initial Assessment**: Does it have enough context to answer the user's question directly? [00:38:23 | 00:38:27]
*   **Tool Check**: If not, does it have any tools at its disposal that could provide the necessary information? [00:38:29 | 00:38:32]
*   **Tool Execution**: If relevant tools exist, it calls the appropriate tool, passing the required parameters extracted from the user's query [00:38:32 | 00:38:34].
*   **Loop**: This process can loop, meaning the LLM might call multiple tools or refine its approach until it has sufficient context to answer [00:38:34 | 00:38:40]. Developers can set a maximum number of loops to prevent infinite cycles [00:41:48 | 00:41:56].

### 3. Leveraging [[Using tools like Cursor Nextjs and Daily Bots for app development | AI Tools]]
[[Using tools like Cursor Nextjs and Daily Bots for app development | Tools like Cursor]] simplify this process by allowing developers to:
*   **Feed Documentation**: Provide documentation for services like Open Router directly to Cursor. This allows the AI to understand the API calls and required structures for tool integration without manual copying and pasting [00:20:17 | 00:20:47]. This is particularly useful for [[Building iOS apps using AI tools | iOS development]], where LLMs might hallucinate capabilities; feeding Apple documentation reduces such errors [00:20:53 | 00:21:16].
*   **Generate Tool Code**: Prompt Cursor to create the tool functions and modify the LLM's prompt to use these tools. Even with some errors, the process can be remarkably fast, sometimes requiring only a few prompts and subsequent error fixes [00:39:01 | 00:40:28].
*   **Dynamic Model Swapping**: Tools like Open Router enable easy switching between different LLMs (e.g., Claude, Gemini, OpenAI) with a single line of code, facilitating testing and optimization during development [00:18:13 | 00:18:47]. This can also dynamically display model costs and context windows, which is useful for development [00:47:54 | 00:48:18].

### 4. Refining Responses with Prompt Engineering
Even with tool calling, the quality of the LLM's answers depends on the prompt [00:26:46 | 00:26:47]. Developers can use other LLMs like Claude to generate highly effective and concise prompts, often formatted in XML, to ensure the responses are tailored to user expectations (e.g., "like a friend answering it for you" [00:27:24 | 00:28:36]).

### 5. Data Generation for Testing
[[AI tools for app development | AI]] can also generate realistic mock data for testing. Instead of generic data, developers can prompt the AI to create specific, localized data (e.g., "add restaurants and places that look way more realistic for a 28-year-old male in Dallas") to make testing and demonstrations more impactful and relatable for potential users [00:31:37 | 00:32:00]. This enhances the perception of the app and can help gauge user interest [00:32:38 | 00:33:04].

## Conclusion

Tool and function calling significantly enhances the capabilities and efficiency of [[ai_tools_for_app_development | AI-powered applications]]. By enabling LLMs to interact with specific functions and data sources, it allows for more dynamic, context-aware, and cost-effective responses, transforming simple chat interfaces into intelligent agents [00:44:56 | 00:45:00]. This approach is a key component in [[building apps without coding | building advanced applications]] with AI [00:22:20 | 00:22:22].