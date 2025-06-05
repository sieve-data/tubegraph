---
title: Switching between language models with unified interfaces
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

The AI SDK provides a [[unified_interfaces_for_ai_ecosystems | unified interface]] that simplifies the process of interacting with different large language models (LLMs) <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This allows developers to switch between various LLM providers and models by changing as little as a single line of code <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

## Benefits of a Unified Interface

There are several reasons why a developer might want to switch between different [[using_language_models_to_generate_text | language models]] <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>:
*   **Cost-effectiveness**: Some models may be cheaper to operate for certain tasks <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **Performance**: Different models might offer faster response times <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   **Use Case Optimization**: A particular model might be better suited or optimized for a specific use case <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Basic Text Generation with `generateText`

The fundamental primitive for interacting with LLMs in the AI SDK is the `generateText` function <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. This function allows users to call an LLM and generate text <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

### Example: OpenAI's GPT-4o Mini

Initially, `generateText` can be used with a model like OpenAI's GPT-4o mini, providing a simple prompt like "hello world" <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

```typescript
import { generateText, openai } from 'ai'; // Example import

async function main() {
  const result = await generateText({
    model: openai.chat("gpt-4o-mini"), // Specifying the model
    prompt: "hello world",
  });
  console.log(result.text);
}
main();
```
Running this code would yield a response such as "Hello, how can I assist you today?" <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

### Addressing Model Limitations

A common [[challenges_and_solutions_in_using_large_language_models | challenge]] with some models is their knowledge cutoff, meaning they cannot access real-time web information <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. For example, GPT-4o Mini's training data cutoff is around 2024, so it cannot answer questions about future events like the "AI Engineer Summit in 2025" <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

> [03:30:00] I'm sorry, but I don't have information about events scheduled for 2025, including the AI engineer summit.

## Switching Providers for Web Search Capabilities

The [[unified_interfaces_for_ai_ecosystems | unified interface]] of the AI SDK makes it easy to switch to a different model or provider that might have built-in web search capabilities <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

### Using Perplexity

To switch to Perplexity, which has web search built-in, only the model import and instantiation need to be changed <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>:

```typescript
import { generateText, perplexity } from 'ai'; // New import for Perplexity

async function main() {
  const result = await generateText({
    model: perplexity.chat("sonar-pro"), // Switching to Perplexity's Sonar Pro
    prompt: "When was the AI Engineer Summit in 2025?",
  });
  console.log(result.text);
}
main();
```
With Perplexity, the model can provide an accurate answer, such as "The AI Engineer Summit in 2025 took place from February 19th to February 22nd 2025 in New York City" <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

#### Accessing Sources

Perplexity, when using web search, references its sources <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. The AI SDK makes these sources accessible via the `sources` property of the result object <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

```typescript
// ... (previous code)
  console.log(result.text);
  console.log(result.sources); // Logging the sources
// ...
```
This allows developers to see the inline sources used by the model <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### Using Google Gemini

The AI SDK supports many providers, including Google's Gemini <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Switching to Gemini Flash 1.5 with search grounding is similarly straightforward:

```typescript
import { generateText, google } from 'ai'; // New import for Google

async function main() {
  const result = await generateText({
    model: google.chat("gemini-flash-1.5"), // Switching to Gemini Flash 1.5
    prompt: "When was the AI Engineer Summit in 2025?",
    // Specify search grounding if available and desired
    // (Note: The transcript implies this is an option, actual implementation might vary slightly based on SDK version)
  });
  console.log(result.text);
}
main();
```
This demonstrates the power of the [[unified_interfaces_for_ai_ecosystems | unified interface]]: the same prompt and configuration can be sent to different models from different providers, yielding similar accurate answers when using web search capabilities <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. A comprehensive list of supported providers can be found in the AI SDK documentation <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Conclusion

The ability to seamlessly switch between [[using_language_models_to_generate_text | language models]] using a [[unified_interfaces_for_ai_ecosystems | unified interface]] like that provided by the AI SDK is a powerful feature for developers <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. It offers flexibility in terms of cost, speed, and specific model capabilities, allowing for optimization based on the task at hand.