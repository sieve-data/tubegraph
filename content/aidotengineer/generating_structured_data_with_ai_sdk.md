---
title: Generating structured data with AI SDK
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

The AI SDK offers two primary methods for generating structured outputs from large language models <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>:
1.  Using the `experimentalOutput` option with the `generateText` function <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
2.  Utilizing the dedicated `generateObject` function <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

The `generateObject` function is particularly highlighted as a powerful "workhorse" for handling structured data generation <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

## Using `experimentalOutput` with `generateText`

This method allows developers to specify a desired output schema when calling `generateText` <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This is useful for combining text generation with structured data extraction.

### Example: Extracting a Sum from a Conversation
Consider a scenario where the model calculates a sum through [[using_tools_and_function_calling_in_ai_sdk | tool calls]], and the desired output is just that numerical sum <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

```typescript
import { generateText, experimental_output, tool } from 'ai/experimental';
import { z } from 'zod'; // ZOD for schema definition
import { openai } from '@ai-sdk/openai';

// Define a tool to add numbers
const addNumbersTool = tool({
  description: 'Adds two numbers together.',
  parameters: z.object({
    num1: z.number().describe('The first number to add.'),
    num2: z.number().describe('The second number to add.'),
  }),
  execute: async ({ num1, num2 }) => {
    return num1 + num2;
  },
});

async function main() {
  const result = await generateText({
    model: openai('gpt-4o-mini'),
    prompt: "What's 10 + 5?",
    tools: {
      addNumbers: addNumbersTool,
    },
    maxSteps: 3, // Allows the model to perform tool calls and then generate text
    experimental_output: experimental_output.object(() => ({
      // Define the schema for the expected output
      schema: z.object({
        sum: z.number(),
      }),
      // Function to extract the sum from the model's text generation
      extractor: (text) => {
        const match = text.match(/(\d+\.?\d*)/); // Simple regex to find a number
        return { sum: match ? parseFloat(match[1]) : 0 };
      },
    })),
  });

  // Log the structured output
  console.log(result.experimental_output);
}

main();
```
In this example, the `experimentalOutput` option uses ZOD to define that the expected output object should contain a `sum` key with a number value <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. The `extractor` function then parses the raw text output to conform to this schema <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

## The `generateObject` Function

The `generateObject` function is specifically designed for generating structured data <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. It simplifies the process by directly expecting a schema definition for the desired output object.

### Defining Schemas with ZOD
ZOD is a TypeScript validation library that integrates seamlessly with the AI SDK for defining schemas <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. It provides type safety and makes working with structured outputs "an absolute breeze" <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

#### Example: Generating Definitions for an AI Agent
To demonstrate `generateObject`, one could ask an AI model to generate 10 definitions for an "AI agent" and expect these definitions in a structured array <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

```typescript
import { generateObject } from 'ai/experimental';
import { z } from 'zod';
import { openai } from '@ai-sdk/openai';

async function main() {
  const result = await generateObject({
    model: openai('gpt-4o-mini'),
    prompt: "Please come up with 10 definitions for AI agents.",
    schema: z.object({
      definitions: z.array(z.string()),
    }),
  });

  console.log(result.object);
}

main();
```
This will return a type-safe object with a `definitions` key, which is an array of strings <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

#### Adding Context with `.describe()`
ZOD's `.describe()` function can be chained to schema definitions to provide more specific instructions to the language model about the expected content of a particular field <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

```typescript
import { generateObject } from 'ai/experimental';
import { z } from 'zod';
import { openai } from '@ai-sdk/openai';

async function main() {
  const result = await generateObject({
    model: openai('gpt-4o-mini'),
    prompt: "Please come up with 10 definitions for AI agents.",
    schema: z.object({
      definitions: z.array(
        z.string().describe("Use as much jargon as possible. It should be completely incoherent.")
      ),
    }),
  });

  console.log(result.object);
}

main();
```
By adding `.describe()` to the string schema, the model is guided to generate definitions that are highly technical and intentionally "incoherent" <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.

### Enum Mode for Restricted Values
For situations where the output needs to be one of a few predefined values, `generateObject` can be used in "enum mode" <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>. This is more ergonomic than using ZOD for simple binary choices and can be easier for the language model to adhere to <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>.

#### Example: Evaluating Search Result Relevance
When [[developing_custom_ai_tools_and_functions | developing custom AI tools]] for web searches, a model might need to classify a search result as either "relevant" or "irrelevant" <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>.

```typescript
import { generateObject } from 'ai/experimental';
import { openai } from '@ai-sdk/openai';

async function evaluateRelevance(searchResult: string) {
  const evaluation = await generateObject({
    model: openai('gpt-4o-mini'),
    prompt: `Evaluate whether the search results are relevant and will help answer the following query.
      <searchResult>${searchResult}</searchResult>`,
    mode: 'enum', // Use enum mode
    values: ['relevant', 'irrelevant'], // Define the allowed values
  });

  return evaluation.object; // Will be either 'relevant' or 'irrelevant'
}

// Example usage
// const result = await evaluateRelevance("Content of a search result...");
// console.log(result); // 'relevant' or 'irrelevant'
```
This restricts the model's output to only the specified enum values, ensuring a predictable and easily parsable response <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>. This is particularly useful in multi-step agents or recursive workflows where the model needs to decide its next action based on a clear, constrained output <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>.

Overall, generating structured data with the AI SDK provides developers with robust tools for controlling model outputs, enhancing type safety, and building more reliable and efficient [[building_scalable_ai_systems | AI systems]] <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.