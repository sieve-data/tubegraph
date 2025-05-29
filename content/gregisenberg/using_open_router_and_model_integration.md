---
title: Using Open Router and model integration
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

The process of building mobile applications has been significantly enhanced by leveraging AI models through tools like Cursor and services like Open Router. This integration allows for rapid development, advanced features, and a more polished user experience <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Open Router Overview

Open Router is a service that provides a unified API for interacting with over 300 different AI models <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. It simplifies the process of switching between various Large Language Models (LLMs) like Gemini, Claude, or OpenAI with just a single line of code, often just a string or piece of text <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. This flexibility allows developers to test different LLMs and compare their responses and associated costs efficiently during development <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. While Open Router may have a small fee, its benefits in terms of development speed and model flexibility are considered worthwhile <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

## Integrating Open Router for AI Chat

Chris, a developer building a portfolio of mobile apps, demonstrated how he integrated Open Router into his budgeting app, Luna, to add an AI chat feature <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

The integration process involved several key steps:
1.  **UI First Approach**: Initially, the focus was solely on creating the user interface (UI) for the chat feature using dummy, hardcoded data <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This approach makes it easier for the AI (Cursor) to focus on a single task, increasing the chances of success <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
2.  **Maintaining UI Consistency**: Instructions were given to Cursor to follow the existing UI style of the app, ensuring the new AI chat seamlessly integrated with the app's aesthetic, including its color scheme <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
3.  **Connecting to LLM**: After the UI was established, the next step was to make the chat functional by connecting it to an actual LLM via Open Router <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. This also included adding a setting to toggle between different models at the top right of the chat screen <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
4.  **Contextual Data**: The AI was instructed to use the last three months of transactions as context for answering user questions about spending <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
5.  **Leveraging Documentation**: To ensure Cursor had the necessary information for Open Router integration, the Open Router documentation URL was directly fed into Cursor using the `@docs` feature <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This feature allows Cursor to index entire documentation, providing it with context on necessary API calls <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. This technique is particularly useful for Apple-specific development, where AI models often hallucinate what is possible in iOS or Mac apps <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

### Prompt Engineering for Optimal Responses

The initial prompt provided by Cursor for the AI chat was basic, leading to unhelpful or verbose answers <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. To improve the quality of responses, a more refined prompt was generated using Claude, then provided to Cursor <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.

Key techniques for prompt engineering:
*   **XML Format**: Formatting prompts in XML (with `title` and `description` tags) was found to increase the likelihood of producing good results from the LLM <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **Conciseness and Persona**: Specific instructions were given for the AI to be concise, like a friend, and not to "show its work" unless asked <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>. This empathetic approach to prompting significantly improves the user experience <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

### [[function_calling_and_configuration_in_ai_models | Function Calling]] with Open Router

A significant advancement in the AI chat feature involved implementing tool or [[function_calling_and_configuration_in_ai_models | function calling]], which allows the LLM to access and use specific tools within the application <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This addresses the problem of feeding excessive (and costly) transaction data to the LLM for every query <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

Instead of parsing messages with an initial LLM and then feeding relevant data, tool calling allows a single LLM to:
1.  Assess if it has enough context to answer a user's question <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>.
2.  If not, identify if it has available tools to gather the necessary information <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>.
3.  Utilize those tools (e.g., to retrieve specific date ranges of transactions) and then re-evaluate the context <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>. This process loops until sufficient information is gathered, or a defined max loop limit is reached (e.g., four times) <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

Local tools created for the budgeting app included:
*   `get_transactions_for_date_range`: Retrieves transactions within a specified period <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.
*   `get_users_current_budget`: Accesses the user's current budget information <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>.

These tools are defined locally within the application code, rather than calling external APIs, which is a common misconception about tool calling <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>. This transforms the chat feature into an "agent" capable of performing actions and retrieving specific information based on user queries <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.

### Monitoring Costs and Models

During development, it's beneficial to monitor the cost and token usage of LLM interactions <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>. Open Router provides an API endpoint to retrieve call costs and token usage, which was integrated to display this information directly below chat messages <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. Additionally, the app was modified to dynamically pull and display all available Open Router models, their context windows, and costs, rather than hardcoding them <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>. This allows for real-time cost analysis and model selection based on performance and budget.

### AI for Asset Generation

Beyond code generation and model integration, AI, specifically GPT-4o, is also used for generating high-quality visual assets for apps <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. By providing an initial mascot or character, GPT-4o can generate an "infinite number of secondary assets" suitable for various app states like loading screens or empty states <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>. This allows for consistent style and the creation of unique, delightful visual elements that enhance the user experience <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>.

### Security Considerations

When [[building and deploying_apps_with_ai_integration | building and deploying apps with AI integration]], especially with tools that directly interact with APIs like Open Router, security is paramount <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. Hardcoding API keys directly into the frontend of an application, while convenient for demos, is highly dangerous. These keys should ideally reside in the backend to prevent unauthorized access and potential financial abuse by bots that scan public repositories or exposed services <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

### General Advice on AI Tooling

For developers, embracing AI tooling is seen as inevitable and beneficial for career acceleration <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>. For non-developers, AI tools should be used as learning aids to understand programming fundamentals <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. It is recommended to start with tools that have more "guardrails" or checks, such as Replit or Lovable, rather than Cursor, which offers greater flexibility but also poses more risks for unintentional errors or security vulnerabilities <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.