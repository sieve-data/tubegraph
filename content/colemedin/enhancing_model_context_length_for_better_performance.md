---
title: Enhancing model context length for better performance
videoId: 8ommGcs_-VU
---

From: [[colemedin]] <br/> 

When working with local large language models (LLMs) in development environments like `autodDev` for [[enhancing_bolt_new_with_multiple_large_language_models | Bolt.new]], an insufficient context length can severely hinder performance and functionality <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. This limitation, often seen with default [[working_with_local_large_language_models | Ollama]] models, prevents the LLM from fully interacting with the development environment <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

## The Problem: Insufficient Default Context <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>

`Bolt.new` typically only supports one LLM, Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. However, many users prefer [[benefits_of_hosting_your_own_large_language_models | local LLMs]] to avoid costs and [[limitations_of_ai_coding_assistants_and_overcoming_them_with_context_7 | rate limits]] <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. The default context length for any [[working_with_local_large_language_models | Ollama]] model is typically 2048 tokens <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. This is often insufficient to fit the `Bolt.new` prompt, causing the model to lose context and fail to interact properly with the web container (e.g., creating files or showing previews) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This results in an experience akin to just chatting with Ollama in the terminal, without the automated code generation and preview features of `Bolt.new` <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## The Solution: Increasing Context Length with Ollama Modelfiles <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>

Ollama provides an easy way to create a variation of any model with an increased context length <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.

1.  **Create a Modelfile**:
    *   Create a file (e.g., `Modelfile` or any other name) <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
    *   Add two lines:
        ```
        FROM <model_ID>
        PARAMETER num_ctx <new_context_limit>
        ```
        *   `<model_ID>` is the ID of the Ollama model you want to use (e.g., `quen:2.5-coder-7b`) <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
        *   `<new_context_limit>` should be above 8196, as this is the default limit for `Bolt.new` <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. A recommended value is 32768 <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

    *Example Modelfile (e.g., `quen_2.5_coder`):*
    ```
    FROM quen:2.5-coder-7b
    PARAMETER num_ctx 32768
    ```
    <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>

2.  **Create the New Model**:
    *   Run the command: `ollama create -f <modelfile_name> <new_model_ID>` <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
        *   `<modelfile_name>` is the name of your Modelfile (e.g., `quen_2.5_coder`) <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
        *   `<new_model_ID>` is the name you give to the new model (e.g., `quen-2.5-coder-autodev-7b`) <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.

    *Example Command:*
    `ollama create -f quen_2.5_coder quen-2.5-coder-autodev-7b`
    <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>

After this, the new model with increased context length will be available in your `Bolt.new` instance, functioning seamlessly by opening the code window, creating files, and providing previews just like larger models <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

## General Tips for LLM Performance in AI Coding <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>

Even with enhanced context length, other strategies can maximize LLM performance in AI coding assistants like `autodDev`:

*   **Start Simple and Iterate**: Begin with a very simple prompt to create a basic application. Once the core functionality is established, iteratively add more complexity and details <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. This helps avoid hallucinations and broken applications from the start <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. This strategy is effective even with more powerful LLMs like Claude 3.5 Sonnet <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.
*   **Provide Detailed UI/UX Requirements**: When iterating, describe specific UI/UX details, including colors, padding, and measurements for views <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. This guides the LLM effectively, even with powerful models <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.

## Alternative: DeepSeek Coder Version 2 <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>

While local LLMs are beneficial, some challenges with smaller models arise due to their inability to handle the larger prompts of AI coding assistants <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>. For a very affordable, open-source, and high-performing alternative, DeepSeek Coder version 2 (236 billion parameter version) is highly recommended <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

*   **Cost-Effectiveness**: It is cheaper than GPT-4o Mini and significantly more affordable (over 20 times) than Claude, with prices around $0.14 per million input tokens and $0.28 per million output tokens compared to Claude's $3 and $15 respectively <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
*   **Performance**: It boasts incredible benchmarks, offering robust performance for building complex web applications, similar to what Claude can achieve <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
*   **Accessibility**: It can be accessed via OpenRouter or the DeepSeek API directly <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. While a 236 billion parameter model is massive for local [[hardware_requirements_for_running_large_language_models_locally | hardware]], it offers a strong cloud-based option that mitigates rate limits <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

## Practical Demonstration: Building a Chat Interface <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>

Using `autodDev` with a locally enhanced `Quen 2.5 Coder 7B` model (a 7 billion parameter LLM), a functional chat interface can be built <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. This involves:

1.  **Initial Prompt**: Creating a basic Next.js chat interface <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. Even if initially basic or "ugly," it provides a functional starting point <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
2.  **UI/UX Iteration**: Refining the interface with detailed UI/UX requirements like specific colors, padding, and measurements <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
3.  **Integrating an AI Agent**: Connecting the chat interface to an `n8n` agent API endpoint to allow interaction with an external AI agent, which could be hooked up with Retrieval-Augmented Generation (RAG) and a PG Vector database <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. This involves providing the LLM with the API endpoint, expected payload, authorization details, and the output field for the response <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.

This process demonstrates how even a smaller, local LLM, when properly configured for context, can effectively build a functional application, highlighting the power of [[reasoning_large_language_models_and_their_impact | local LLMs]] and the capabilities of `autodDev` <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.