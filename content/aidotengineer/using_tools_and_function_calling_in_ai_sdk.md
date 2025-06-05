---
title: Using tools and function calling in AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

[[function_calling_in_ai_models | Function calling]], or "tools," enables large language models (LLMs) to interact with the outside world and perform actions beyond just generating text <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This capability is a core feature of the [[importance_of_tool_calling_in_ai | AI SDK]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Core Concept of Tools

The fundamental idea behind tools is simple: you provide an LLM with a prompt and a list of available tools as part of the conversation context <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Each tool includes:
*   **Name:** A unique identifier for the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Description:** A clear explanation of what the tool does, which the model uses to decide when to invoke it <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **Parameters:** Any data required by the tool for its operation, which the model attempts to parse from the conversation context <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a> <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

Instead of generating a text response, the model will generate a "tool call" if it decides to use a tool to solve a user's query <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This tool call includes the tool's name and the arguments parsed from the conversation context <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The developer is then responsible for parsing that tool call, running the associated code, and handling the results <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Implementing Tools with AI SDK

### `generateText` with Tools

The `generateText` or `streamText` functions in the AI SDK accept a `tools` object as input <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Within this object, you define each tool using the `tool` utility function <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

The `tool` utility function provides:
*   `description`: Explains the tool's purpose to the model <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   `parameters`: Defines the data schema required by the tool. This can be defined using Zod, a TypeScript validation library, which ensures type safety between the defined parameters and the arguments received by the `execute` function <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a> <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   `execute`: An asynchronous JavaScript function that contains the arbitrary code to be run when the language model generates a tool call <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

The AI SDK automatically parses any tool calls, invokes the `execute` function, and returns the result in a `toolResults` array <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

```typescript
import { generateText, tool } from 'ai';
import { openai } from '@ai-sdk/openai';

async function main() {
  const { toolResults } = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: "What's 10 + 5?",
    tools: {
      addNumbers: tool({
        description: 'Adds two numbers together.',
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

  console.log(toolResults); // Output: [{ toolName: 'addNumbers', args: { num1: 10, num2: 5 }, result: 15 }]
}

main();
```
<a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

### Building [[building_agents_with_ai_sdk | Agents with AI SDK]] using `maxSteps`

When a model generates a tool call, it typically doesn't generate subsequent text <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. To allow the model to incorporate tool results into a generated text answer or perform multiple actions, the `maxSteps` property is used <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

`maxSteps` enables an "agentic loop" <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>:
1.  If the model generates a tool call, the `toolResult` is sent back to the model along with the previous conversation context <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
2.  This triggers another generation, allowing the model to continue autonomously until it either generates plain text or reaches the `maxSteps` threshold <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

This allows the model to pick the next step in a process without requiring complex manual logic or rerouting <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

#### Example: Parallel Tool Calls and Multi-Step Reasoning

A more complex example demonstrates an agent using multiple tools, potentially in parallel, and then synthesizing the results <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. For instance, asking for weather in multiple cities and then adding temperatures together <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The model can infer missing parameters (like latitude/longitude for a city) from the context <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

```typescript
import { generateText, tool } from 'ai';
import { openai } from '@ai-sdk/openai';

async function main() {
  const { text, toolResults } = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: "Get the weather in San Francisco and New York and then add them together.",
    maxSteps: 3, // Allows multiple steps of tool calls and text generation
    tools: {
      getWeather: tool({
        description: 'Get the current weather at a location.',
        parameters: {
          type: 'object',
          properties: {
            latitude: { type: 'number' },
            longitude: { type: 'number' },
            city: { type: 'string' }, // Model can infer lat/long from city
          },
          required: ['city'],
        },
        execute: async ({ city, latitude, longitude }) => {
          // Simulate weather API call
          if (city === 'San Francisco') return { temperature: 12.3 };
          if (city === 'New York') return { temperature: 15.2 };
          return { temperature: 0 };
        },
      }),
      addNumbers: tool({
        description: 'Adds two numbers together.',
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

  console.log(text); // Expected: "The current temperature in San Francisco is 12.3° C. In New York, it's 15.2. When you add these temperatures together, you get 27.5 degrees CC."
  console.log(toolResults); // Will show sequence of tool calls and their results
}

main();
```
<a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a> <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>

## [[generating_structured_data_with_ai_sdk | Generating Structured Data]] (Structured Outputs)

Beyond text, the AI SDK allows models to generate structured data, which is useful for programmatic integration <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

### `generateText` with `experimental_output`

The `generateText` function includes an `experimental_output` option to define the desired structure using a Zod schema <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a> <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

```typescript
import { generateText, tool, experimental_output } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

async function main() {
  const { experimental_output: result } = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: "Get the weather in San Francisco and New York and then add them together.",
    maxSteps: 3,
    tools: { /* ... (same tools as above) ... */ },
    experimental_output: experimental_output(
      z.object({
        sum: z.number().describe('The sum of the temperatures.'),
      })
    ),
  });

  console.log(result.sum); // Direct access to the sum as a number
}

main();
```
<a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a> <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>

### `generateObject` Function

The `generateObject` function is specifically dedicated to structured outputs and is highly favored for this purpose <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. It simplifies defining the output schema.

```typescript
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

async function main() {
  const { object } = await generateObject({
    model: openai('gpt-4o-mini'),
    prompt: 'Please come up with 10 definitions for AI agents.',
    schema: z.object({
      definitions: z.array(z.string().describe('Each definition should be completely incoherent and use as much jargon as possible.')),
    }),
  });

  console.log(object.definitions);
}

main();
```
<a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a> <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a> <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>

The `ZOD.describe` function can be chained to any Zod schema element to provide detailed instructions to the language model about the desired characteristics of that specific value <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

`generateObject` also supports an "enum mode" for when the output needs to be one of a few predefined values (e.g., 'relevant' or 'irrelevant'), making it very ergonomic and easier for the model <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>.

## [[developing_custom_ai_tools_and_functions | Developing Custom AI Tools and Functions]] in Complex Systems

[[integrating_ai_coding_agents_with_thirdparty_tools | Integration of AI coding agents with third-party tools]] is crucial for building complex AI systems. The principles of tool calling and structured outputs are foundational for advanced applications, such as a "deep research clone" <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a> <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.

### Example: Deep Research Clone Workflow

A deep research clone workflow exemplifies [[using_reasoning_models_and_tool_calls_in_ai | using reasoning models and tool calls in AI]] in a structured way <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>:

1.  **Generate Subqueries:** An initial query is broken down into multiple search queries using `generateObject` <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>.
2.  **Search the Web:** A `searchWeb` function (e.g., using Exa API) retrieves relevant results for each subquery <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. It's crucial to filter extraneous information from search results to reduce token count and improve model effectiveness <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>.
3.  **Analyze and Process:** The `searchAndProcess` function acts as an agent, using `generateText` with `maxSteps` and two key tools:
    *   `searchWeb`: Performs the actual web search.
    *   `evaluate`: Determines if the search results are relevant. This tool can also prevent re-using already processed sources <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a> <a class="yt-timestamp" data-t="00:52:22">[00:52:22]</a>. Large search results should be handled as local variables rather than tool parameters to avoid unnecessary token consumption <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>.
4.  **Generate Learnings:** The `generateLearnings` function uses `generateObject` to extract insights ("learnings") and "follow-up questions" from relevant search results <a class="yt-timestamp" data-t="00:43:39">[00:43:39]</a>.
5.  **Recursion and State Management:** The entire process is encapsulated in a recursive `deepResearch` function <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>. Accumulated research (original query, active queries, search results, learnings, completed queries) is stored in a mutable state object, allowing the model to go deeper into sub-topics while retaining context <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.
6.  **Generate Report:** Finally, a `generateReport` function uses a larger reasoning model (e.g., GPT-4o-mini) to synthesize all accumulated research into a comprehensive report <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. Providing a detailed system prompt (e.g., persona, date, markdown formatting, guidelines) significantly improves the quality and structure of the final output <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>.

This workflow demonstrates how different [[implementing_function_calling_and_agents_in_ai | AI SDK functions]] can be combined to build sophisticated, multi-step [[integration_of_ai_into_development_environments_and_editors | AI systems]] that solve complex problems <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a> <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.