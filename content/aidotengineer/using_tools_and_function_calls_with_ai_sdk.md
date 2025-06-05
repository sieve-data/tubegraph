---
title: Using tools and function calls with AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

The [[Tool Usage and Development in AI Frameworks | AI SDK]] provides powerful primitives for building AI applications, including generating text, working with structured data, and integrating external tools. This article explores these core functionalities, focusing on [[function_calling_in_ai | tool calling]] and structured outputs, culminating in a practical example of building a deep research agent.

## AI SDK Fundamentals

The [[Tool Usage and Development in AI Frameworks | AI SDK]] is designed to simplify interactions with large language models (LLMs) and enable the creation of intelligent agents.

### Generating Text with `generateText`

The `generateText` function is a fundamental primitive in the [[Tool Usage and Development in AI Frameworks | AI SDK]] for interacting with LLMs to produce text outputs <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

Key features:
*   **Model Specification**: Users can specify the LLM they want to use, such as OpenAI's GPT-4o mini <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Input**: It accepts either a simple `prompt` string or an array of `messages`, where each message has a `role` and `content` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Unified Interface**: A core feature of the [[Tool Usage and Development in AI Frameworks | AI SDK]] is its unified interface, which allows developers to switch between different language models (e.g., OpenAI, Perplexity, Google Gemini) by changing a single line of code <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. This flexibility is valuable for optimizing costs, speed, or performance for specific use cases <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

Models with built-in web search, like Perplexity's Sonar Pro or Google's Gemini, can directly answer questions requiring up-to-date information, bypassing the need for external tools in some cases <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. Responses from these models often include `sources` that can be accessed via the `sources` property in the [[Tool Usage and Development in AI Frameworks | AI SDK]] result <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

## [[function_calling_in_ai | Tools and Function Calling]]

[[function_calling_in_ai | Tools]], also known as [[function_calling_in_ai | function calling]], allow language models to interact with the outside world and perform actions beyond text generation <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

### Core Idea
The model is given a prompt along with a list of available tools. Each tool includes:
*   **Name**: A unique identifier for the tool <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Description**: What the tool does, which helps the model decide when to use it <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
*   **Parameters**: Any data the tool requires, which the model attempts to parse from the conversation context <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   **Execute Function**: An arbitrary asynchronous JavaScript code block that runs when the model generates a tool call <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

When the model decides to use a tool, it generates a "tool call" (the tool's name and arguments) instead of plain text <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. The developer is then responsible for parsing and executing this tool call <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. The [[Tool Usage and Development in AI Frameworks | AI SDK]] automatically invokes the `execute` function and returns its output in a `toolResults` array <a class="yt-timestamp" data-t="09:23:00">[09:23:23]</a>.

### Enabling Multi-Step Agents with `maxSteps`
By default, if an LLM generates a tool call, the `generateText` function returns the tool result, not a synthesized text response <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. To allow the model to incorporate tool results into a text answer, the `maxSteps` property can be used <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.

The `maxSteps` property enables an "agentic loop":
1.  If the model generates a tool call, the tool result is sent back to the model along with the previous conversation context.
2.  This triggers another generation step.
3.  The process continues until the model generates plain text (no tool call) or the `maxSteps` threshold is reached <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

This feature allows the model to autonomously pick the next step in a process without requiring manual rerouting of output <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. [[importance_of_tool_calling_for_ai_agents | Parallel tool calls]] are also supported, allowing multiple tools to be invoked simultaneously within a single step <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>.

## Generating Structured Data (Structured Outputs)

Beyond text generation, the [[Tool Usage and Development in AI Frameworks | AI SDK]] facilitates generating structured data.

### Methods for Structured Outputs
1.  **`generateText` with `experimentalOutput`**: An experimental option within `generateText` that allows defining an output schema <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.
2.  **`generateObject`**: A dedicated function for generating structured outputs <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>. This function is particularly useful as it ensures type-safe JSON output based on a defined schema <a class="yt-timestamp" data-t="22:22:00">[22:22:00]</a>.

### ZOD Integration
[[AI integration and tool calling | ZOD]], a TypeScript validation library, is heavily used with the [[Tool Usage and Development in AI Frameworks | AI SDK]] to define schemas for structured outputs. This integration provides:
*   **Type Safety**: Ensures the generated output conforms to the expected types <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>.
*   **Schema Description**: The `.describe()` function in ZOD allows adding detailed instructions to the LLM about the desired format or content for specific keys or values within the schema <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>.
*   **Enum Mode**: `generateObject` can operate in an enum mode, restricting outputs to a predefined set of values (e.g., "relevant" or "irrelevant"), simplifying evaluation logic <a class="yt-timestamp" data-t="40:15:00">[40:15:00]</a>.

## Practical Project: Building a Deep Research Clone

To demonstrate these concepts, a "deep research clone" can be built as a Node.js terminal script. This project showcases how to break down complex tasks into a structured workflow, integrate multiple [[AI integration and tool calling | AI SDK]] functions, and create [[building_agents_with_vercel_ai_sdk | autonomous agents]] <a class="yt-timestamp" data-t="24:37:00">[24:37:00]</a>.

### Workflow Overview
The deep research process involves several steps <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>:
1.  **Input Query**: Start with a broad research query <a class="yt-timestamp" data-t="26:53:00">[26:53:00]</a>.
2.  **Generate Subqueries**: Create multiple specific search queries from the main prompt <a class="yt-timestamp" data-t="26:57:00">[26:57:00]</a>.
3.  **Search the Web**: For each subquery, search for relevant results <a class="yt-timestamp" data-t="27:15:00">[27:15:00]</a>.
4.  **Analyze Results**: Extract key learnings and identify follow-up questions from the search results <a class="yt-timestamp" data-t="27:19:00">[27:19:00]</a>.
5.  **Recursive Depth**: If more depth is needed, use follow-up questions to generate new queries, recursively repeating the process while accumulating all research <a class="yt-timestamp" data-t="27:26:00">[27:26:00]</a>.
    *   **Depth**: Controls how many levels deep the research goes <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.
    *   **Breadth**: Controls how many separate lines of inquiry are pursued at each level <a class="yt-timestamp" data-t="28:12:00">[28:12:00]</a>.

### Implementation Details

#### 1. `generateSearchQueries`
This function takes a main `query` and the desired `number` of sub-queries. It uses `generateObject` with a schema to ensure an array of strings is returned, optimized for search engine queries <a class="yt-timestamp" data-t="29:46:00">[29:46:00]</a>.

#### 2. `searchWeb`
This function uses the Exa API to perform web searches and retrieve content <a class="yt-timestamp" data-t="32:52:00">[32:52:00]</a>.
*   **Configuration**: Allows specifying the number of results and using `liveCrawl` for real-time data <a class="yt-timestamp" data-t="33:59:00">[33:59:00]</a>.
*   **Data Trimming**: Crucially, it processes results to return only relevant information (e.g., `url`, `title`, `content`), reducing token count for LLMs and improving model effectiveness <a class="yt-timestamp" data-t="34:49:00">[34:49:00]</a>.

#### 3. `searchAndProcess` (The Agentic Component)
This is the core [[conducting_deep_research_with_ai_sdk | deep research with AI SDK]] agent that manages finding relevant search results <a class="yt-timestamp" data-t="36:14:00">[36:14:00]</a>. It uses `generateText` with two tools:
*   **`searchWeb` tool**: Invokes the `searchWeb` function with a given query <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>.
*   **`evaluate` tool**: Assesses the relevance of a search result. It pulls the latest pending result, uses `generateObject` (in enum mode for "relevant" or "irrelevant") to get the model's judgment, and then either adds the result to `finalSearchResults` or instructs the model to search again with a more specific query if irrelevant <a class="yt-timestamp" data-t="39:41:00">[39:41:00]</a>.

The `maxSteps` property keeps this agentic loop running until a relevant source is found or the step limit is reached <a class="yt-timestamp" data-t="38:27:00">[38:27:00]</a>. It also checks `accumulatedSources` to avoid reusing previously processed links <a class="yt-timestamp" data-t="52:54:00">[52:54:00]</a>.

#### 4. `generateLearnings`
This function takes a `query` and `searchResult` and uses `generateObject` to extract a `learning` (insight) and `followUpQuestions` (an array of strings) from the content, guided by a specific prompt <a class="yt-timestamp" data-t="43:39:00">[43:39:00]</a>.

#### 5. `deepResearch` (Recursion Handler)
This function orchestrates the entire recursive research process <a class="yt-timestamp" data-t="47:07:00">[47:07:00]</a>. It maintains a global `accumulatedResearch` state to track original queries, active queries, search results, learnings, and completed queries <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>.
*   It calls `generateSearchQueries`, `searchAndProcess`, and `generateLearnings` iteratively.
*   It decrements `depth` and `breadth` parameters with each recursive call to control the research scope and prevent infinite loops <a class="yt-timestamp" data-t="50:01:00">[50:01:00]</a>.
*   For follow-up questions, it constructs a new query based on the overall goal, previous queries, and new follow-up questions, then recursively calls `deepResearch` <a class="yt-timestamp" data-t="50:43:00">[50:43:00]</a>.

#### 6. `generateReport`
Finally, after the `deepResearch` process completes, the `generateReport` function takes the `accumulatedResearch` and uses `generateText` with a large reasoning model (e.g., GPT-4o mini) to synthesize all the gathered information into a comprehensive report <a class="yt-timestamp" data-t="54:42:00">[54:42:00]</a>.
*   **System Prompt**: A detailed system prompt is provided to guide the model on persona ("expert researcher"), formatting (Markdown), and content guidelines (e.g., allowing speculation if flagged) <a class="yt-timestamp" data-t="57:22:00">[57:22:00]</a>.
*   The final report is then written to a markdown file <a class="yt-timestamp" data-t="55:49:00">[55:49:00]</a>.

This [[leveraging_ai_tools_for_efficiency_and_scalability | leveraging AI tools for efficiency and scalability]] project demonstrates the power of combining [[Tool Usage and Development in AI Frameworks | AI SDK]]'s primitives to build complex, [[building_agents_with_vercel_ai_sdk | autonomous AI systems]] capable of tasks like deep research <a class="yt-timestamp" data-t="59:06:00">[59:06:00]</a>.