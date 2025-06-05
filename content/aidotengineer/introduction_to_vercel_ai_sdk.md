---
title: Introduction to Vercel AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

The Vercel AI SDK is a versatile toolkit designed to simplify the process of building Artificial Intelligence (AI) applications and integrating large language models (LLMs) into projects [00:00:02]. It provides a unified interface, enabling developers to switch between various language models with minimal code changes [00:02:37].

This introduction covers the fundamental building blocks of the AI SDK and demonstrates how to construct a complex AI system, such as a deep research clone, using its features [00:00:15].

## Core Concepts of the AI SDK

The AI SDK provides several core primitives for interacting with language models and building AI applications.

### Generating Text

The `generateText` function is the most fundamental primitive, allowing developers to call a large language model and receive a text response [00:01:06].

*   **Usage**: It takes a model (e.g., `OpenAI`'s GPT-4o mini) and a prompt as input [00:01:39]. Alternatively, it can accept an array of messages, each with a role and content [00:02:16].
*   **Unified Interface**: A key feature of the AI SDK is its unified interface, allowing easy switching between different language models (e.g., `OpenAI`'s GPT-4o mini, Perplexity, Google Gemini) by changing a single line of code [00:02:41]. This flexibility is beneficial for cost, speed, or use-case specific performance [00:02:50].
*   **Accessing Sources**: When using models like Perplexity or Google Gemini that integrate web search, the AI SDK provides access to the sources used in the model's response via the `sources` property [00:04:40]. This allows developers to see the references directly [00:04:51]. For example, a query about the "AI engineer summit in 2025" can be answered by a web-enabled model like Perplexity's Sonar Pro [00:03:10]. Similarly, Google's Gemini Flash 1.5 can provide search grounding for accurate results [00:05:33].

### [[using_tools_and_function_calling_in_ai_sdk | Using Tools and Function Calling]]

[[developing_custom_ai_tools_and_functions | Tools]], also known as function calling, extend the capabilities of language models beyond text generation, allowing them to interact with the outside world and perform actions [00:06:15].

*   **Concept**: The model is provided with a prompt and a list of available tools [00:06:31]. Each tool has a `name`, a `description` (which the model uses to decide when to invoke it), and `parameters` (data needed to use the tool) [00:06:38]. Instead of generating text, the model can generate a "tool call," specifying the tool to use and any parsed arguments [00:07:01]. The developer is then responsible for executing that tool's code [00:07:16].
*   **Defining Tools**: The AI SDK simplifies tool definition using a `tool` utility function [00:08:06]. This function provides type safety between the defined `parameters` and the arguments received by the `execute` function [00:08:54]. The `execute` function can contain any arbitrary asynchronous JavaScript code [00:08:34].
*   **Automatic Invocation (`maxSteps`)**: The AI SDK automatically parses tool calls and invokes their `execute` function, returning the result in a `toolResults` array [00:09:24]. To enable the model to incorporate tool results into its final text response, the `maxSteps` property can be set [00:11:35]. When a tool call is generated, the `maxSteps` feature sends the tool result back to the model along with the previous conversation context, triggering another generation [00:11:50]. This allows the model to autonomously continue a process until it generates plain text or reaches the `maxSteps` threshold [00:12:03].
*   **Example**: Demonstrating tool usage, a simple `addNumbers` tool can be defined to sum two numbers [00:07:31]. The model, instead of calculating, calls the tool, and the result is returned [00:09:59]. More complex scenarios can involve multiple tools, such as `getWeather` and `addNumbers`, working in tandem, even supporting parallel tool calls [00:14:10]. The model can infer necessary parameters (like latitude and longitude for weather) from the conversation context [00:15:05].

### [[generating_structured_data_with_ai_sdk | Generating Structured Data]]

The AI SDK offers two primary methods for generating structured outputs, which are particularly useful for making model responses easier to consume programmatically [00:18:43].

*   **`generateText` with `experimentalOutput`**: This option allows `generateText` to produce structured data based on a defined schema [00:18:46]. It integrates seamlessly with Zod, a TypeScript validation library, to define schemas and ensure type safety [00:19:47].
*   **`generateObject` function**: This is a dedicated function for structured outputs and is highly favored for its power and ease of use [00:18:55].
    *   **Zod Integration**: Like `experimentalOutput`, `generateObject` leverages Zod for schema definition, making it straightforward to define the desired structure of the output (e.g., an array of strings for definitions) [00:22:09].
    *   **`.describe()` method**: Zod's `.describe()` function can be chained onto schema definitions to provide additional context and instructions to the language model for specific values, influencing the generated content within the structured output [00:23:14].
    *   **Enum Mode**: For simple cases where only a few predefined values are expected (e.g., "relevant" or "irrelevant"), `generateObject` can be used in "enum mode," directly specifying the allowed string values instead of a full Zod schema [00:40:15]. This is ergonomic and helps constrain the model's output [00:40:27].

## [[building_agents_with_ai_sdk | Building a Deep Research Clone]]

The AI SDK's primitives can be combined to build complex AI systems, such as a deep research clone that autonomously gathers and synthesizes information from the web [00:24:39]. This project demonstrates an agentic workflow, combining various AI SDK functions for interesting use cases [00:25:22].

The deep research workflow involves several structured steps:

1.  **Generate Subqueries**: Based on an initial prompt, the system generates multiple specific search queries [00:26:58]. This is achieved using the `generateObject` function, which takes the main query and the desired number of subqueries, returning them as a structured array of strings [00:30:08].
2.  **Search the Web**: For each generated subquery, the system searches the web for relevant results [00:27:15]. This implementation uses the Exa search API, ensuring live crawls and efficient data retrieval [00:32:56]. Crucially, only relevant information (e.g., title, URL, content) is extracted from search results to reduce token count and improve model effectiveness [00:34:49].
3.  **Analyze Results (`searchAndProcess` Agent)**: This is the most complex and agentic part of the workflow [00:36:10].
    *   It uses `generateText` with two custom [[developing_custom_ai_tools_and_functions | tools]]: `searchWeb` and `evaluate` [00:38:18].
    *   The `searchWeb` tool calls the Exa API and pushes results to a `pendingSearchResults` array [00:39:24].
    *   The `evaluate` tool pulls the latest pending result, runs it through `generateObject` (in enum mode for "relevant" or "irrelevant"), and provides feedback to the model [00:39:41]. If a result is irrelevant, the tool returns a message prompting the model to search again with a more specific query, effectively driving the agentic loop [00:41:01].
    *   To prevent redundant searches, the `evaluate` tool also checks against a list of `accumulatedSources` (URLs) to ensure previously used pages are marked irrelevant [00:52:50].
    *   Local variables are used to store search results for evaluation rather than passing them as tool parameters. This avoids unnecessary token usage and processing by the model [00:41:28].
4.  **Generate Learnings and Follow-up Questions**: Once relevant search results are obtained, the system analyzes them to extract key learnings and propose follow-up questions [00:27:20]. The `generateLearnings` function uses `generateObject` to create a structured output containing the learning (a string) and an array of `followUpQuestions` [00:43:55].
5.  **Recursive Research**: To achieve "deep" research, the process is made recursive [00:27:31]. The `deepResearch` function manages the overall workflow, taking `depth` (levels of inquiry) and `breadth` (number of parallel inquiries at each level) parameters [00:49:09]. Follow-up questions from one level become the new queries for the next, accumulating research in a shared state until the defined depth is reached [00:46:18].
6.  **Generate Report**: Finally, all the `accumulatedResearch` (original query, queries performed, search results, learnings, completed queries) is passed to a larger reasoning model (e.g., GPT-3.5 Turbo) [00:47:52]. The `generateReport` function synthesizes this information into a comprehensive markdown report, which can then be written to the file system [00:54:47]. Crucially, a detailed system prompt guides the model on formatting (e.g., Markdown) and tone to ensure a high-quality, structured output [00:57:11].

This multi-step, agentic approach demonstrates how the AI SDK enables the creation of sophisticated AI applications by combining its core functions and allowing models to autonomously navigate complex tasks [00:59:08].

## Resources

*   AI SDK Documentation: <a class="yt-timestamp" data-t="00:59:35">[00:59:35]</a>