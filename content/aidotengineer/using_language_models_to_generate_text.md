---
title: Using language models to generate text
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

The AI SDK is a toolkit designed for building agents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> and developing AI applications <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This article explores its core functionalities, focusing on how [[large_language_model_interpretability | language models]] can be leveraged to generate text, perform actions via tools, and produce structured data.

## Fundamentals

The AI SDK offers fundamental building blocks necessary for interacting with [[large_language_model_interpretability | language models]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The project typically involves a single `index.ts` file, runnable via `pmpp rundev` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### `generateText` Function

The `generateText` function is the primary way to call a [[large_language_model_interpretability | large language model]] to generate text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

It requires specifying a model, such as OpenAI's GPT-4o mini, and a prompt <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For instance, prompting "hello world" to GPT-4o mini might return "Hello, how can I assist you today?" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This function can accept either a direct string prompt or an array of messages, where each message has a role and content <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Unified Interface

A core feature of the AI SDK is its unified interface, allowing developers to switch between different [[large_language_model_interpretability | language models]] by changing a single line of code <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This flexibility is beneficial for reasons such as cost-efficiency, speed, or performance in specific use cases <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Models like GPT-4o Mini have training data cutoffs (e.g., 2024), limiting their knowledge of future events <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. For information requiring real-time data, models with built-in web search capabilities, such as Perplexity's Sonar Pro, can be used <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Perplexity's responses include references or sources, accessible via the `sources` property in the AI SDK <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Google's Gemini Flash 1.5 also supports search grounding for similar functionality <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. The SDK supports a wide range of providers, detailed in its documentation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Tools and Function Calling

Beyond generating text, [[large_language_model_interpretability | language models]] can interact with the outside world and perform actions through "tools" or "function calling" <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### How Tools Work

The fundamental idea behind tools is simple: the model is given a prompt along with a list of available tools <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Each tool includes:
*   A `name` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
*   A `description` of what it does, which the model uses to decide when to invoke it <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>
*   `parameters` (data required to use the tool) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
*   An `execute` function, which is arbitrary asynchronous JavaScript code run when the [[large_language_model_interpretability | language model]] calls the tool <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

When the model decides to use a tool, it generates a "tool call" (the tool's name and arguments parsed from the conversation context) instead of text <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The developer then parses and runs this tool call <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. The AI SDK automatically parses tool calls, invokes the `execute` function, and returns the result in a `toolResults` array <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

The `tool` utility function (e.g., `tool('addNumbers', ...)`) provides type safety between defined parameters and the `execute` function's arguments <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### `maxSteps` for Autonomous Agents

By default, after a tool call, the [[large_language_model_interpretability | language model]] might not generate text <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. To get the model to incorporate tool results into a text answer, the `maxSteps` property can be used <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. When `maxSteps` is set, if the model generates a tool call, the tool result is sent back to the model along with the previous conversation context, triggering another generation <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This continues until the model generates plain text or the `maxSteps` threshold is reached <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This enables the model to run autonomously, picking the next step without explicit developer logic <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

For example, asking "what's 10 + 5?" with an "add numbers" tool will result in a tool call and then a subsequent text generation of "10 + 5 equals 15" if `maxSteps` is configured <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

Models can even make parallel tool calls within a single step <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. For instance, getting weather in two cities ("San Francisco" and "New York") and then adding them together can involve two parallel "get weather" calls followed by an "add numbers" call <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. The [[large_language_model_interpretability | language model]] can infer parameters like latitude and longitude from the city names provided in the prompt, using its training data <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

## Structured Outputs

The AI SDK provides ways to generate structured data, also known as structured outputs <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

### Methods for Structured Output

There are two primary ways to generate structured outputs:
1.  Using `generateText` with its `experimentalOutput` option <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
2.  Using the dedicated `generateObject` function <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. The `streamObject` function is also available for streaming structured output <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

### Zod for Schema Definition

[[large_language_model_interpretability | Language models]] can be guided to output structured data using schema definitions <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>. Zod, a TypeScript validation library, is highly recommended for defining these schemas in the AI SDK <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Zod schemas allow for type-safe objects as output, ensuring data integrity <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.

The `.describe()` function in Zod can be chained onto any key or value within the schema to provide detailed instructions to the [[large_language_model_interpretability | language model]] about the desired output for that specific value <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. This allows for fine-grained control over the generated text within the structured output <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.

`generateObject` can also use an enum mode for schemas with a limited set of discrete values (e.g., "relevant" or "irrelevant"), simplifying the schema definition <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>. This constraint makes it easier for the [[large_language_model_interpretability | language model]] to produce the correct output <a class="yt-timestamp" data-t="00:40:31">[00:40:31]</a>.

## Practical Project: Building a Deep Research Clone

This section demonstrates how to combine the AI SDK's functions to build complex AI systems, specifically a "deep research clone" in Node.js <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. Deep research tools generally take a topic, search the web, aggregate resources, and return a comprehensive report <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

### Workflow Breakdown

The deep research workflow involves several steps <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>:
1.  **Input Query**: Start with a general prompt <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
2.  **Generate Subqueries**: Generate multiple specific search queries from the initial prompt <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.
3.  **Search Web**: For each subquery, search the web for relevant results <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
4.  **Analyze Results**: Analyze search results for "learnings" (insights) and "follow-up questions" <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
5.  **Recursive Research**: Take follow-up questions and existing research to generate new queries, recursively continuing the process while accumulating information <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.

This recursive process explores "webs of thought" by adjusting "depth" (levels of inquiry) and "breadth" (number of queries at each step) <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.

### Implementation Details

#### `generateSearchQueries`
This function uses `generateObject` to create an array of search queries based on an initial prompt and a desired number of queries <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. It defines a Zod schema for an array of strings to ensure structured output <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.

#### `searchWeb` with Exa
The `searchWeb` function uses the Exa service to perform web searches and retrieve content <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. It fetches a specified number of results and can use `liveCrawl` to ensure up-to-date information <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>. Importantly, it maps through the results and only returns relevant information (e.g., URL, title, content) to reduce token count and improve [[large_language_model_interpretability | language model]] effectiveness <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

#### `searchAndProcess` (Agentic Component)
This is the most complex and agentic part of the workflow <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>. It employs `generateText` with two tools:
*   `searchWeb`: Performs a web search <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>. Search results are temporarily stored in `pendingSearchResults` <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>.
*   `evaluate`: Evaluates the relevance of the latest search result using `generateObject` in enum mode (`relevant` or `irrelevant`) <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. If relevant, it moves the result to `finalSearchResults`; otherwise, it discards it <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>.

The `maxSteps` parameter ensures this agentic loop continues until a relevant source is found or the step limit is reached <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>. The model receives feedback ("Search results are irrelevant, please search again with a more specific query") to guide its next action <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>. To prevent redundant searches, the `evaluate` tool also receives a list of `accumulatedSources` and marks already-used URLs as irrelevant <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.

#### `generateLearnings`
This function uses `generateObject` to analyze relevant search results and extract key "learnings" (insights) and "follow-up questions" <a class="yt-timestamp" data-t="00:43:39">[00:43:39]</a>. It defines a Zod schema for a string learning and an array of string follow-up questions <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>.

#### Deep Research Recursion
The overall `deepResearch` function handles the recursion, managing the "accumulated research" state <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This state includes the original query, active queries, search results, learnings, and completed queries <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>. The function decrements `depth` and `breadth` parameters in each recursive call to ensure termination and control the extent of the research <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

#### `generateReport`
Finally, the `generateReport` function takes the `accumulatedResearch` and feeds it into a [[large_language_model_interpretability | large language model]] (e.g., GPT-3.5 mini) to synthesize all the gathered information <a class="yt-timestamp" data-t="00:54:32">[00:54:32]</a>. A detailed system prompt can be provided to guide the model on formatting (e.g., Markdown) and tone (e.g., "expert researcher"), ensuring the output meets specific requirements and is more structured <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>. The final report can then be written to a file system <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>.