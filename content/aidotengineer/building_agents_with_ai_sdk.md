---
title: Building agents with AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

This article explores [[Building and Improving AI Agents | building agents]] using the AI SDK, covering fundamental building blocks and a practical project to create a deep research clone <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The session begins with core concepts of the AI SDK before diving into an agent-building example in Node.js <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

To follow along, clone the repository, install dependencies, and copy environment variables <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The project uses a single `index.ts` file, runnable with `pnpm rundev` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Fundamentals of the AI SDK

### Generating Text

The `generateText` function allows interaction with large language models to produce text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. It takes a specified model (e.g., OpenAI's GPT-4o mini) and a prompt, then logs the resulting text <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

```typescript
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';

async function main() {
  const result = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: 'hello world',
  });
  console.log(result.text);
}

main();
```
<a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

`generateText` can also accept an array of `messages` instead of a `prompt`, where each message has a `role` and `content` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

A core feature of the AI SDK is its [[OpenAIs Agents SDK | unified interface]], enabling easy switching between language models by changing a single line of code <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This is useful for optimizing for cost, speed, or specific use cases <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. For models that lack real-time web access, like GPT-4o Mini, the SDK allows seamless integration with models that have built-in web search capabilities, such as Perplexity <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

```typescript
import { generateText } from 'ai';
import { perplexity } from '@ai-sdk/perplexity';

async function main() {
  const result = await generateText({
    model: perplexity('sonar-pro'),
    prompt: 'when was the AI engineer summit in 2025?',
  });
  console.log(result.text);
  console.log(result.sources); // Accessing sources property
}

main();
```
<a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

The `sources` property provides access to references used by models like Perplexity <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. The AI SDK supports numerous providers, many offering web search, which can be explored in their documentation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. For example, Google's Gemini Flash 1.5 can be used with `searchGrounding` enabled <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### [[Using tools and function calling in AI SDK | Using Tools and Function Calling]]

[[Using tools and function calling in AI SDK | Tools]], or function calling, enable language models to interact with the outside world and perform actions <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The model is given a prompt and a list of available tools, each with a name, description, and required data (parameters) <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

When the model decides to use a tool, it generates a "tool call" (the tool's name and arguments parsed from the conversation context) instead of text <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The developer then parses and runs this tool call <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

The AI SDK simplifies this process:
*   Tools are passed to `generateText` or `streamText` functions via a `tools` object <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   The `tool` utility function provides type safety between defined parameters and arguments in the `execute` function <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   The `execute` function can contain any arbitrary asynchronous JavaScript code <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   The SDK automatically parses tool calls, invokes the `execute` function, and returns the result in a `toolResults` array <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

```typescript
import { generateText, tool } from 'ai';
import { openai } from '@ai-sdk/openai';

async function main() {
  const result = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: 'What\'s 10 + 5?',
    tools: {
      addNumbers: tool({
        description: 'Adds two numbers together',
        parameters: {
          type: 'object',
          properties: {
            num1: { type: 'number' },
            num2: { type: 'number' },
          },
          required: ['num1', 'num2'],
        },
        execute: async ({ num1, num2 }) => num1 + num2,
      }),
    },
  });
  console.log(result.toolResults);
}

main();
```
<a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>

When a model generates a tool call, it typically doesn't return text directly <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. To get the model to incorporate tool results into a generated text answer, the `maxSteps` property is used <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. If `maxSteps` is set, the SDK automatically sends the tool result and previous conversation context back to the model, triggering another generation. This continues until the model generates plain text or the `maxSteps` threshold is reached <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This mechanism allows the model to run autonomously, picking the next step without explicit developer logic <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. This forms the basis of [[Building and Improving AI Agents | multi-step agents]] <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

Example demonstrating `maxSteps` with multiple tools (adding numbers and getting weather):
```typescript
// ... (imports and addNumbers tool as above)
import { perplexity } from '@ai-sdk/perplexity'; // Example for weather tool

async function main() {
  const result = await generateText({
    model: openai('gpt-4o-mini'), // Or perplexity('sonar-pro') for web access
    prompt: 'Get the weather in San Francisco and New York and then add them together.',
    maxSteps: 3, // Allow multiple steps for tools and final text generation
    tools: {
      // ... addNumbers tool
      getWeather: tool({
        description: 'Get the current weather at a location',
        parameters: {
          type: 'object',
          properties: {
            latitude: { type: 'number' },
            longitude: { type: 'number' },
            city: { type: 'string' },
          },
          required: ['city'], // Model infers lat/long from city
        },
        execute: async ({ latitude, longitude, city }) => {
          // Placeholder for actual weather API call
          if (city === 'San Francisco') return { temperature: 12.3 };
          if (city === 'New York') return { temperature: 15.2 };
          return { temperature: null };
        },
      }),
    },
  });
  console.log(result.text);
  console.log(JSON.stringify(result.steps, null, 2)); // Show steps
}
main();
```
<a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>

The `result.steps` array provides a detailed log of each action the agent took, including tool calls and their results <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. The AI SDK also allows tapping into the raw request and response bodies for debugging <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### [[Generating structured data with AI SDK | Generating Structured Data]]

[[Generating structured data with AI SDK | Generating structured data]] (structured outputs) is possible in two ways with the AI SDK:
1.  Using `generateText` with its `experimentalOutput` option <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
2.  Using the dedicated `generateObject` function <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

`generateObject` is particularly powerful for creating type-safe structured outputs <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. It leverages ZOD, a TypeScript validation library, to define schemas <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

Example using `generateText` with `experimentalOutput`:
```typescript
import { generateText, experimental_output } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

async function main() {
  const result = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: 'What\'s 10 + 5?',
    maxSteps: 3,
    tools: { /* ... addNumbers tool ... */ },
    experimental_output: experimental_output(
      z.object({
        sum: z.number(),
      }),
    ),
  });
  console.log(result.experimental_output);
}
main();
```
<a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>

Example using `generateObject` for defining AI agent:
```typescript
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

async function main() {
  const result = await generateObject({
    model: openai('gpt-4o-mini'),
    prompt: 'Please come up with 10 definitions for AI agents.',
    schema: z.object({
      definitions: z.array(z.string()),
    }),
  });
  console.log(result.object);
}
main();
```
<a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>

ZOD's `.describe()` function can be chained to schema definitions to provide more specific instructions to the language model for each value, helping to get more precise outputs <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

```typescript
// ... (inside main function)
schema: z.object({
  definitions: z.array(z.string().describe('Each definition should use as much jargon as possible and be completely incoherent.')),
}),
// ...
```
<a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>

## Building a Deep Research Clone

This section focuses on [[Building and Improving AI Agents | building a multi-step agent]] that mimics a deep research tool <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>. The goal is to take a query, conduct deep research by searching the web, and then write a Markdown report to the file system <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. This project demonstrates structuring a workflow, incorporating autonomous agentic elements, and combining different AI SDK functions <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

### Deep Research Workflow

The general steps for the deep research clone are:
1.  **Input Query**: Take a rough query or prompt <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
2.  **Generate Subqueries**: For the input prompt, generate a set of more specific search queries <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.
3.  **Search the Web**: For each subquery, search the web for relevant results <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
4.  **Analyze Results**: Analyze each search result for key learnings and follow-up questions <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
5.  **Recursion**: If further depth is desired, use the follow-up questions and existing research to generate new queries and repeat the process recursively, accumulating information <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.
6.  **Report Generation**: Synthesize all gathered information into a comprehensive report <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

The process can be controlled by `depth` (levels of recursion) and `breadth` (number of queries at each step) <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

### Step 1: Generate Search Queries

The `generateSearchQueries` function uses `generateObject` to create an array of search queries based on the initial prompt <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.
```typescript
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

const mainModel = openai('gpt-4o-mini'); // Centralized model definition

async function generateSearchQueries(query: string, numberOfQueries: number = 3): Promise<string[]> {
  const { object } = await generateObject({
    model: mainModel,
    prompt: `Generate ${numberOfQueries} search queries for the following query: ${query}`,
    schema: z.object({
      queries: z.array(z.string().min(1).max(5)), // Loose constraints here, but example
    }),
  });
  return object.queries;
}

// ... (main function to test)
```
<a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>

### Step 2: Search the Web with Exa

Exa is used for web search, offering speed and efficiency <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>. The `searchWeb` function takes a query and uses Exa's `search` and `contents` functions <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. Key configurations include `numResults` and `liveCrawl` (to ensure live, up-to-date results) <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

Crucially, the function maps through results to return only relevant information (e.g., `url`, `title`, `text`) to reduce token usage and improve model effectiveness <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.
```typescript
import { Exa } from 'exa';

const exa = new Exa(process.env.EXA_API_KEY);

type SearchResult = {
  url: string;
  title: string;
  text: string;
};

async function searchWeb(query: string): Promise<SearchResult[]> {
  const { results } = await exa.searchAndContents(query, {
    numResults: 1, // Limited for simple demo
    liveCrawl: true,
  });
  return results.map(result => ({
    url: result.url,
    title: result.title,
    text: result.text,
  }));
}
```
<a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>

### Step 3: Search and Process (Agentic Part)

The `searchAndProcess` function is the core agentic component, responsible for finding and validating relevant search results <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>. It uses `generateText` with two tools: `searchWeb` and `evaluate`.

*   **`searchWeb` tool**: Invokes the `searchWeb` function, adds results to a `pendingSearchResults` array, and returns them to the model context <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a>.
*   **`evaluate` tool**: Pulls the latest pending result, uses `generateObject` in enum mode (`relevant` or `irrelevant`) to assess its relevance, and pushes relevant results to `finalSearchResults` <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. If irrelevant, it prompts the model to search again with a more specific query, triggering the `maxSteps` loop <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>.

It also checks `accumulatedSources` to avoid reusing sources that have already been evaluated <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

```typescript
// ... (imports)
import { generateText, tool, generateObject } from 'ai';
import { z } from 'zod';

async function searchAndProcess(
  query: string,
  accumulatedSources: SearchResult[]
): Promise<SearchResult[]> {
  const pendingSearchResults: SearchResult[] = [];
  const finalSearchResults: SearchResult[] = [];

  const { text, toolResults, steps } = await generateText({
    model: mainModel,
    prompt: `Search the web for information about: ${query}`,
    system: `You are a researcher. For each query, search the web and then evaluate if the results are relevant and will help answer the following query. If the page already exists in the existing results, mark it as irrelevant.`,
    maxSteps: 5, // Max attempts to find relevant results
    tools: {
      searchWeb: tool({
        description: 'Searches the web for information about a given query.',
        parameters: z.object({ query: z.string() }),
        execute: async ({ query }) => {
          const results = await searchWeb(query);
          pendingSearchResults.push(...results);
          return { message: `Search results added to pending list.` };
        },
      }),
      evaluate: tool({
        description: 'Evaluates the search results to determine relevance and extract learnings.',
        parameters: z.object({}), // No parameters needed, takes from internal state
        execute: async () => {
          const latestResult = pendingSearchResults.pop();
          if (!latestResult) {
            return { message: 'No pending search results to evaluate.' };
          }

          // Check if source already used
          if (accumulatedSources.some(s => s.url === latestResult.url)) {
            return 'irrelevant'; // Marked as irrelevant if already used
          }

          const evaluation = await generateObject({
            model: mainModel,
            prompt: `Evaluate whether the search results are relevant and will help answer the following query: "${query}"
            
            <searchResult>
            ${JSON.stringify(latestResult)}
            </searchResult>
            `,
            schema: z.enum(['relevant', 'irrelevant']),
          });

          if (evaluation.object === 'relevant') {
            finalSearchResults.push(latestResult);
            return 'relevant';
          } else {
            return 'irrelevant: Please search again with a more specific query.';
          }
        },
      }),
    },
  });

  return finalSearchResults;
}
```
<a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a>

### Step 4: Generate Learnings and Follow-up Questions

After obtaining relevant search results, the `generateLearnings` function extracts key learnings (insights) and generates follow-up questions <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>. This also uses `generateObject` for a structured output:
```typescript
// ... (imports)
type Learning = {
  learning: string;
  followUpQuestions: string[];
};

async function generateLearnings(query: string, searchResult: SearchResult): Promise<Learning> {
  const { object } = await generateObject({
    model: mainModel,
    prompt: `The user is researching: "${query}". The following search results were deemed relevant. Generate a learning and a follow-up question from the following search result.
    
    <searchResult>
    ${JSON.stringify(searchResult)}
    </searchResult>`,
    schema: z.object({
      learning: z.string(),
      followUpQuestions: z.array(z.string()),
    }),
  });
  return object;
}
```
<a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>

### Step 5: Incorporating Recursion and State

To enable deep research, the entire process is wrapped in a `deepResearch` function that calls itself recursively <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. A global `ResearchState` object tracks the accumulated research (original query, active queries, search results, learnings, completed queries) <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>.
```typescript
// ... (imports and types)

type ResearchState = {
  originalQuery: string;
  queries: string[];
  searchResults: SearchResult[];
  learnings: Learning[];
  completedQueries: string[];
};

let accumulatedResearch: ResearchState = {
  originalQuery: '',
  queries: [],
  searchResults: [],
  learnings: [],
  completedQueries: [],
};

async function deepResearch(
  prompt: string,
  query: string | undefined = undefined,
  depth: number = 2, // How many levels deep to go
  breadth: number = 2 // How many subqueries at each level
) {
  if (depth === 0) {
    return accumulatedResearch; // Base case for recursion
  }

  if (query === undefined) {
    query = prompt;
    accumulatedResearch.originalQuery = prompt;
  }

  const queriesToSearch = await generateSearchQueries(query, breadth);
  accumulatedResearch.queries.push(...queriesToSearch);

  for (const q of queriesToSearch) {
    console.log(`Searching the web for: ${q}`);
    const results = await searchAndProcess(q, accumulatedResearch.searchResults);
    accumulatedResearch.searchResults.push(...results);
    accumulatedResearch.completedQueries.push(q);

    for (const result of results) {
      console.log(`Processing search result from: ${result.url}`);
      const learning = await generateLearnings(q, result);
      accumulatedResearch.learnings.push(learning);

      // Recursive call for follow-up questions
      if (learning.followUpQuestions.length > 0 && depth > 1) {
        for (const followUp of learning.followUpQuestions.slice(0, breadth)) {
          console.log(`Going deeper with follow-up: ${followUp}`);
          await deepResearch(prompt, followUp, depth - 1, breadth); // Decrement depth
        }
      }
    }
  }
  return accumulatedResearch;
}
```
<a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>

### Step 6: Generate Report

Finally, the `generateReport` function takes the `accumulatedResearch` and feeds it to a large language model (e.g., GPT-4o mini) to synthesize all the information into a cohesive report <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. A `system` prompt is vital for defining the persona (expert researcher) and specifying formatting (e.g., Markdown) to ensure a structured and high-quality output <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>. The final report is then written to a Markdown file <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>.

```typescript
// ... (imports)
import * as fs from 'fs/promises';

async function generateReport(research: ResearchState): Promise<string> {
  const { text: report } = await generateText({
    model: openai('gpt-4o-mini'), // Or a reasoning model like GPT-4o
    system: `You are an expert researcher. Today's date is ${new Date().toLocaleDateString()}. Follow these instructions exactly:
    - Use Markdown formatting.
    - Structure the report clearly with headings and subheadings.
    - Summarize key findings concisely.
    - Include relevant data and insights.
    - You may use high levels of speculation or prediction, but flag it clearly.`,
    prompt: `Generate a comprehensive report based on the following research data about "${research.originalQuery}":

    <researchData>
    Original Query: ${research.originalQuery}
    Completed Queries: ${JSON.stringify(research.completedQueries, null, 2)}
    Search Results: ${JSON.stringify(research.searchResults.map(r => ({ url: r.url, title: r.title })), null, 2)}
    Learnings: ${JSON.stringify(research.learnings, null, 2)}
    </researchData>
    `,
  });
  return report;
}

async function main() {
  const initialPrompt = 'What do you need to be a D1 shotput athlete?';
  console.log(`Starting deep research for: ${initialPrompt}`);
  const finalResearch = await deepResearch(initialPrompt, undefined, 2, 2); // Depth 2, Breadth 2

  console.log('Generating report...');
  const reportContent = await generateReport(finalResearch);

  await fs.writeFile('research_report.md', reportContent);
  console.log('Report saved to research_report.md');
}

main();
```
<a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>

This detailed workflow demonstrates how to combine [[Components of AI agents | various components of AI agents]] and functions within the AI SDK to build complex, autonomous systems that can perform sophisticated tasks like deep research <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a>.