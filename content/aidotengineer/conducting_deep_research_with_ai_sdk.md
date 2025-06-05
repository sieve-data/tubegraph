---
title: Conducting deep research with AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 
The AI SDK enables developers to create sophisticated applications, including those capable of [[role_of_ai_in_research_and_data_analytics | deep research]]. A deep research clone can process an initial query, generate sub-queries, search the web for relevant information, analyze findings, and recursively follow up on new questions to build a comprehensive report <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This process leverages the AI SDK's capabilities for text generation, [[using_tools_and_function_calls_with_ai_sdk | tool use (function calling)]], and structured data output <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a>.

### AI SDK Fundamentals for Building Agents

[[building_agents_with_vercel_ai_sdk | Building agents with the AI SDK]] involves several core primitives that provide flexibility and power:

*   **Generate Text Function**
    The `generateText` function allows calling a large language model to produce text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. It accepts either a simple `prompt` or an array of `messages` with specified `role` and `content` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Unified Interface**
    A key feature of the AI SDK is its unified interface, allowing developers to switch between different language models by changing a single line of code <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This flexibility is useful for optimizing costs, speed, or performance for specific use cases <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. For example, seamlessly transitioning from OpenAI's GPT-4o mini to Perplexity's Sonar Pro or Google's Gemini Flash 1.5, especially when web search capabilities are needed <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. The SDK also provides access to sources used by models like Perplexity <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Using Tools and Function Calling**
    Tools, or function calling, enable language models to interact with the outside world and perform actions <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   **Mechanism**: The model is given a prompt and a list of available tools, each with a name, description, and required parameters <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Instead of generating text, the model might generate a tool call, including the tool's name and arguments parsed from the conversation context <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The developer then executes this tool call <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   **Implementation**: Tools are passed to `generateText` or `streamText` via a `tools` object. The `tool` utility function provides type safety between defined parameters and the arguments passed to the `execute` function <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The AI SDK automatically parses tool calls, invokes the `execute` function, and returns the result in a `toolResults` array <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   **Autonomous Multi-step Agents (`maxSteps`)**: To allow the model to incorporate tool results into a text answer, the `maxSteps` property can be set <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. If a tool call is generated, the tool result and previous context are sent back to the model, triggering another generation. This process continues until plain text is generated or the maximum number of steps is reached, enabling autonomous, multi-step agent behavior <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The model can even perform parallel tool calls <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Generating Structured Data (Structured Outputs)**
    The AI SDK offers two ways to generate structured outputs:
    *   **`generateText` with `experimental_output`**: This option allows defining a schema (e.g., using Zod) for the expected output structure <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. Zod, a TypeScript validation library, pairs well with the AI SDK for defining schemas and making structured outputs easy to work with <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
    *   **`generateObject` Function**: This function is specifically designed for structured outputs <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. It takes a prompt and a schema, returning a type-safe object <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. A useful feature is `.describe()` in Zod, which allows providing detailed context for specific values in the schema, influencing the model's output without altering the main prompt <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. `generateObject` can also operate in enum mode for scenarios with a limited set of discrete values (e.g., "relevant" or "irrelevant") <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>.

### Building a Deep Research Clone

The deep research workflow involves several sequential and recursive steps to gather and synthesize information:

#### Workflow Overview
1.  **Generate Sub-queries**: Convert a broad initial query into specific search queries <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.
2.  **Search the Web**: Find relevant results for each sub-query <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.
3.  **Analyze Results**: Extract learnings and identify follow-up questions <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
4.  **Recursive Follow-up**: Take follow-up questions, generate new queries, and repeat the process while accumulating research <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
5.  **Synthesize Report**: Aggregate all gathered information into a comprehensive report <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.

The process uses `depth` to control how many levels deep the research goes and `breadth` to determine how many different inquiries are pursued at each step <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

#### Step 1: Generating Search Queries
The `generateSearchQueries` function uses `generateObject` to create a list of search-engine-optimized queries from a given prompt <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. The function specifies a schema for an array of strings to ensure the output is structured as expected <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.

#### Step 2: Searching the Web
The `searchWeb` function utilizes the Exa API to search the web for relevant results <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. Key considerations include:
*   **Result Count**: Limiting the number of results to optimize token usage <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.
*   **Live Crawl**: Using `liveCrawl` to ensure results are current, accepting a potential hit on performance <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.
*   **Trimming Information**: Only returning necessary data (e.g., title, URL, content) from search results to reduce token count and improve model effectiveness by removing irrelevant information like favicons <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

#### Step 3: Analyzing Results and Iterating (Agentic Loop)
The `searchAndProcess` function implements an agentic loop using `generateText` with two tools:
*   **`searchWeb`**: Executes the web search for a given query <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>. Search results are pushed to a `pendingSearchResults` array <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.
*   **`evaluate`**: Determines the relevance of the most recent search result <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. It uses `generateObject` in enum mode to classify results as "relevant" or "irrelevant" <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>. If irrelevant, it provides feedback to the model to search again with a more specific query, perpetuating the `maxSteps` loop <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>. This tool also prevents re-using sources that have already been processed <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

#### Step 4: Generating Learnings and Follow-up Questions
The `generateLearnings` function uses `generateObject` to analyze a relevant search result <a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>. It extracts a `learning` (insight) and identifies `followUpQuestions`, both defined by a Zod schema <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>. The search result is passed as stringified XML within the prompt to provide context <a class="yt-timestamp" data-t="00:44:08">[00:44:08]</a>.

#### Step 5: Implementing Recursion and State Management
The `deepResearch` function orchestrates the recursive nature of the research process:
*   It takes an initial prompt, and recursively calls itself with new queries derived from follow-up questions <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>.
*   `depth` and `breadth` parameters control the extent of the recursive search <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>.
*   A global or external `accumulatedResearch` state object stores all gathered information (original query, active queries, search results, learnings, completed queries) across recursive calls <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>.
*   The function decrements `depth` with each recursive call to ensure termination and prevent infinite loops, conserving API credits <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

#### Step 6: Generating the Final Report
Once the recursive research is complete, the `generateReport` function takes the `accumulatedResearch` and uses `generateText` to synthesize all information into a comprehensive report <a class="yt-timestamp" data-t="00:54:39">[00:54:39]</a>.
*   **Model Selection**: A reasoning model like GPT-3.5 Turbo mini can be used for synthesis <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>.
*   **System Prompt**: A detailed system prompt is crucial for guiding the model on the desired report structure and persona (e.g., "expert researcher"), including markdown formatting, today's date, and general research analyst-oriented guidelines <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>. This ensures a high-quality, structured output, minimizing the need for the model to infer formatting or tone <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>.

This comprehensive workflow, built with the AI SDK, demonstrates how complex AI systems can be constructed by combining fundamental building blocks and leveraging agentic behavior to tackle challenging tasks like deep research <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.