---
title: Building agents with Vercel AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

This session explores [[building_effective_agents | building agents]] using the Vercel AI SDK, covering fundamental building blocks and a practical project to create a deep research clone <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The examples are demonstrated in Node.js <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

To follow along, clone the repository, install dependencies, and set up environment variables <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The project typically involves a single `index.ts` file, runnable via `pnpm rundev` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Fundamental Building Blocks

### `generateText` Function
The `generateText` function is a core primitive for calling a large language model and generating text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

> [!EXAMPLE] Basic Usage
> ```typescript
> import { generateText, openai } from 'ai';
>
> async function main() {
>   const result = await generateText({
>     model: openai('gpt-4o-mini'),
>     prompt: 'Hello world.',
>   });
>   console.log(result.text);
> }
> main();
> ```
> This example prompts GPT-4o Mini to respond to "Hello world," logging "Hello, how can I assist you today?" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The `generateText` function (along with `streamText`, `generateObject`, and `streamObject`) can accept either a `prompt` string or an array of `messages` as input, where each message has a `role` and `content` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Unified Interface and Model Switching
A core feature of the AI SDK is its unified interface, allowing developers to switch between different language models by changing a single line of code <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a> <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This is useful for optimizing for cost, speed, or specific use cases <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Models like GPT-4o Mini might struggle with recent information as their training data has a cutoff <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. To address this, one can either add a tool for web access or select a model with built-in web search capabilities <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

> [!EXAMPLE] Switching to Perplexity with Web Search
> To switch to Perplexity's `sonar-pro` model, which includes web search, simply change the model import and invocation <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>:
> ```typescript
> import { generateText, perplexity } from 'ai'; // Changed import
>
> async function main() {
>   const result = await generateText({
>     model: perplexity('sonar-pro'), // Changed model invocation
>     prompt: 'When was the AI engineer summit in 2025?',
>   });
>   console.log(result.text);
> }
> main();
> ```
> Perplexity's response will correctly state the summit dates, often including sources via the `sources` property <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This flexibility extends to many providers, including Google's Gemini with search grounding <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### [[using_tools_and_function_calls_with_ai_sdk | Tools (Function Calling)]]
[[using_tools_and_function_calls_with_ai_sdk | Tools]] allow language models to interact with the outside world and perform actions <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The core idea is to provide the model with a prompt and a list of available [[using_tools_and_function_calls_with_ai_sdk | tools]], each with a name, description, and required parameters <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Instead of generating text, the model might generate a tool call, which the developer then parses and executes <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

> [!EXAMPLE] Adding Two Numbers with a Tool
> ```typescript
> import { generateText, openai, tool } from 'ai';
> import { z } from 'zod';
>
> async function main() {
>   const result = await generateText({
>     model: openai('gpt-4o-mini'),
>     prompt: "What's 10 + 5?",
>     tools: {
>       addNumbers: tool({
>         description: 'Adds two numbers together.',
>         parameters: z.object({
>           num1: z.number(),
>           num2: z.number(),
>         }),
>         execute: async ({ num1, num2 }) => num1 + num2,
>       }),
>     },
>   });
>   console.log(result.toolResults); // Logs the tool execution result
> }
> main();
> ```
> The `tool` utility function provides type safety between defined parameters and the `execute` function arguments <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The AI SDK automatically parses tool calls, invokes the `execute` function, and returns the result in a `toolResults` array <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### `maxSteps` Property for Multi-step Agents
When a tool call is generated, the language model does not immediately provide a text response <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. The `maxSteps` property enables the model to continue autonomously <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. If a tool call occurs, the `toolResult` is sent back to the model with the previous conversation context, triggering another generation <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. This loop continues until plain text is generated or the maximum step threshold is reached <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

> [!EXAMPLE] Multi-step Agent with `maxSteps`
> ```typescript
> import { generateText, openai, tool } from 'ai';
> import { z } from 'zod';
>
> async function main() {
>   const { text, toolResults, steps } = await generateText({
>     model: openai('gpt-4o-mini'),
>     maxSteps: 3, // Set max steps to allow follow-up generations
>     prompt: 'Get the weather in San Francisco and New York and then add them together.',
>     tools: {
>       addNumbers: tool({ /* ... */ }),
>       getWeather: tool({
>         description: 'Get the current weather at a location.',
>         parameters: z.object({
>           latitude: z.number(),
>           longitude: z.number(),
>           city: z.string(),
>         }),
>         execute: async ({ latitude, longitude, city }) => {
>           // Simulate weather API call
>           if (city === 'San Francisco') return { temperature: 12.3, unit: 'C' };
>           if (city === 'New York') return { temperature: 15.2, unit: 'C' };
>           return { temperature: 0, unit: 'C' };
>         },
>       }),
>     },
>   });
>   console.log('Resulting text:', text);
>   console.log('Steps:', JSON.stringify(steps, null, 2));
> }
> main();
> ```
> In this example, the model might first call `getWeather` for both cities (potentially in parallel tool calls), then `addNumbers` with the extracted temperatures, and finally generate a text summary <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a> <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. The `maxSteps` allows this sequence of actions and textual synthesis <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Developers can tap into the raw request and response bodies for debugging <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Structured Data and `generateObject`
The AI SDK provides two ways to generate structured outputs:
1.  Using `generateText` with its `experimental_output` option <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
2.  Using the dedicated `generateObject` function, often considered a powerful "workhorse" <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

**Using `generateText` with `experimental_output`:**
This option allows defining a ZOD schema for the desired output structure <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. ZOD is a TypeScript-first schema declaration and validation library, ideal for structured outputs <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

> [!EXAMPLE] Structured Output with `generateText`
> ```typescript
> import { generateText, openai, tool } from 'ai';
> import { z } from 'zod';
>
> async function main() {
>   const { experimental_output } = await generateText({
>     model: openai('gpt-4o-mini'),
>     maxSteps: 3,
>     prompt: 'Get the weather in San Francisco and New York and then add them together.',
>     tools: { /* ... getWeather and addNumbers tools ... */ },
>     experimental_output: z.object({
>       sum: z.number(), // Define the desired output schema
>     }),
>   });
>   console.log(experimental_output?.sum); // Access type-safe output
> }
> main();
> ```
> This results in a simple, type-safe object rather than verbose text <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

**Using `generateObject` Function:**
`generateObject` is specifically designed for structured outputs <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.

> [!EXAMPLE] `generateObject` for AI Agent Definitions
> ```typescript
> import { generateObject, openai } from 'ai';
> import { z } from 'zod';
>
> async function main() {
>   const { object } = await generateObject({
>     model: openai('gpt-4o-mini'),
>     prompt: 'Please come up with 10 definitions for AI agents.',
>     schema: z.object({
>       definitions: z.array(z.string().describe('Each definition should use as much jargon as possible and be completely incoherent.')),
>     }),
>   });
>   console.log(object.definitions);
> }
> main();
> ```
> This example generates an array of 10 AI agent definitions <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. The `.describe()` function in ZOD allows adding specific instructions for each part of the schema, guiding the model's generation without cluttering the main prompt <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

## Practical Project: [[conducting_deep_research_with_ai_sdk | Deep Research Clone]]

The practical project involves [[conducting_deep_research_with_ai_sdk | building a deep research clone]] in Node.js <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>. This demonstrates how to break down complex tasks into a structured workflow, combine different AI SDK functions, and create autonomous agentic elements <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

The concept of deep research involves giving a model a topic, letting it search the web, aggregate resources, go down "webs of thought," and finally produce a report <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

### Workflow Breakdown
The typical workflow for a deep research agent is:
1.  **Input Query:** Start with a rough query/prompt <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.
2.  **Generate Subqueries:** For the input prompt, generate multiple search queries (e.g., "What is an electric car?", "Biggest electric car producers?") <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.
3.  **Search Web:** For each subquery, search the web for relevant results <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
4.  **Analyze Results:** Analyze the search results for key learnings and follow-up questions <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
5.  **Recursive Inquiry:** If more depth is desired, take the follow-up questions and existing research, generate new queries, and repeat the process recursively, accumulating information <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. This allows for exploring "webs of thought" <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.

The depth and breadth settings control the level and scope of information gathered <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

### `generateSearchQueries` Function
This function takes the main query and the desired number of subqueries to generate <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>. It uses `generateObject` with a specific schema to ensure the output is an array of strings suitable for search engines <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

> [!EXAMPLE] `generateSearchQueries`
> ```typescript
> // Uses generateObject to produce a list of search queries
> async function generateSearchQueries(query: string, numQueries: number) { /* ... */ }
>
> async function main() {
>   const prompt = 'What do you need to be a D1 shot put athlete?';
>   const queries = await generateSearchQueries(prompt, 3);
>   console.log(queries);
> }
> main();
> ```
> For the prompt "What do you need to be a D1 shot put athlete?", it might generate queries like "requirements to become a D1 shotput athlete," "training regiment for D1 shotput athlete," etc. <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>.

### `searchWeb` Function
This function uses the Exa API for web search <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>. It takes a query and returns relevant results. Important configurations include `numResults` and `liveCrawl` (to ensure live, non-cached results) <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

> [!NOTE] Token Efficiency
> It's crucial to map through search results and only return the information relevant to the language model (e.g., URL, title, content) <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>. This reduces token count, making calls cheaper and improving model effectiveness by removing irrelevant information <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>.

### `searchAndProcess` Function (Agentic Evaluation)
This is the most complex and "agentic" part of the workflow <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>. It uses `generateText` with two tools: `searchWeb` and `evaluate` <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>. The model continually searches the web and then evaluates the relevance of the results <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

*   **`searchWeb` tool:** Calls the `searchWeb` function and adds the results to a `pendingSearchResults` array <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>.
*   **`evaluate` tool:** Pulls the latest pending result, uses `generateObject` (in enum mode for "relevant" or "irrelevant" output) to determine its usefulness for the query <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. If relevant, it's added to `finalSearchResults`; otherwise, it's discarded <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>. If irrelevant, the tool returns a message prompting the model to "search again with a more specific query," leveraging `maxSteps` to continue the loop with feedback <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>.

> [!NOTE] Optimizing Tool Execution
> Instead of making the language model parse potentially large search results as tool parameters (which can be costly and error-prone), use local variables or a shared state within the tool's `execute` function <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. This keeps token usage down and improves accuracy <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>.

### `generateLearnings` Function
This function takes the original query and the relevant search results to generate a learning (insight) and follow-up questions <a class="yt-timestamp" data-t="00:43:39">[00:43:39]</a>. It uses `generateObject` with a schema expecting a `learning` string and an array of `followUpQuestions` strings <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>.

> [!EXAMPLE] `generateLearnings` Output
> For a query about D1 shotput, a learning might be: "To become a D1 shop at athlete, high school athletes typically need to have four years of varsity experience, achieve highstate finishes or be state champions, and participate in national events like USATF National Junior Olympic Outdoor Track and Field Championships." <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a> Follow-up questions could be: "What are the specific training regimens for shot put athletes?" or "How do division one recruiting standards differ from division two and three?" <a class="yt-timestamp" data-t="00:45:58">[00:45:58]</a>

### Recursion and State Management
To achieve "deep research," the process must be recursive <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>. This requires a dedicated recursive function (e.g., `deepResearch`) and a global or shared state variable (e.g., `accumulatedResearch`) to track all gathered information across recursive calls <a class="yt-timestamp" data-t="00:46:36">[00:46:36]</a>.

The `deepResearch` function takes parameters like `depth` (how many levels deep to go) and `breadth` (how many new queries to generate at each step) <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>. It updates the `accumulatedResearch` object with new search queries, search results, learnings, and completed queries <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a>. The recursion decrements `depth` and `breadth` to ensure termination <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

To prevent redundant searches, the `searchAndProcess` function is updated to pass in previously used sources (URLs) to the `evaluate` tool <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>. If a search result's URL already exists, it's marked as irrelevant, prompting the agent to find new information <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.

### `generateReport` Function
Finally, all the `accumulatedResearch` is passed to a reasoning model (e.g., GPT-4o Mini) using `generateText` to synthesize the information into a comprehensive report <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>.

> [!NOTE] Improving Report Quality
> To get the best response from the model, provide clear guidance on the desired output format and structure. A `systemPrompt` can define the model's persona (e.g., "You are an expert researcher"), today's date, formatting requirements (e.g., "Use markdown formatting"), and specific guidelines (e.g., allowing speculation but requiring flags) <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>.

The resulting markdown report will be structured and detailed, demonstrating the agent's ability to conduct in-depth research and synthesize findings into a coherent document <a class="yt-timestamp" data-t="00:58:12">[00:58:12]</a>. The entire deep research agent, including all components, can be built in relatively few lines of code (e.g., 218 lines) using the AI SDK <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.