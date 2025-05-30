---
title: Creating applications with local LLMs in autod Dev
videoId: 8ommGcs_-VU
---

From: [[colemedin]] <br/> 

[[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]] is a community-driven initiative for Bolt.new that aims to implement much-needed features, including the ability to use any large language model (LLM), such as [[using_local_large_language_models_with_autod_dev | local ones]] with [[using_llama_for_llms | Ollama]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Bolt.new natively supports only Claude 3.5 Sonnet, but many users desire to use [[using_local_large_language_models_with_autod_dev | local LLMs]] to avoid costs and rate limits <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Why Use Local LLMs?

[[using_local_large_language_models_with_autod_dev | Local LLMs]] offer significant advantages:
*   **Cost Savings:** You never have to pay <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **No Rate Limits:** Avoid hitting nasty rate limits <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Accessibility:** Smaller models, like Quin 2.5 Coder 7B, can run on almost any computer <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

While massive closed-source models like Claude 3.5 Sonnet and GPT-4o generally offer the best performance, [[using_local_large_language_models_with_autod_dev | local LLMs]] provide unlimited, free usage on your machine <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Getting Started with Autod Dev

To begin [[using_local_language_models_llm_for_code_generation | code generation]] with [[using_local_large_language_models_with_autod_dev | local LLMs]] in [[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]], ensure it is set up and running on your machine <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The Autod Dev README provides comprehensive instructions for setup, including running with or without Docker <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A video tutorial is also available on setting up Docker and [[using_llama_for_llms | Ollama]] to get [[using_local_large_language_models_with_autod_dev | local LLMs]] on your machine <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Key Tip: Ensuring Proper Context for Local LLMs

A common issue with [[using_local_large_language_models_with_autod_dev | local LLMs]] in [[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]] is that the model may not open the web container or create files within it <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This occurs because [[using_llama_for_llms | Ollama]] models have a default context length of 2048 tokens, which is insufficient for the Bolt.new prompt <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. When the context is lost, the model cannot interact with the web container properly <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Solution: Increase Context Length

To fix this, you can create a slight variation of any [[using_llama_for_llms | Ollama]] model with an increased context length <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

1.  **Create a Model File:** Create a file (e.g., `Modelfile`) with the following content:
    ```
    FROM <model_id>
    PARAMETER num_ctx 32768
    ```
    *   Replace `<model_id>` with the [[using_llama_for_llms | Ollama]] model ID you want to use (e.g., `qwen:2.5-coder-7b`) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   Set `num_ctx` to a value above 8192 (the default limit for Bolt.new) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. 32768 is a recommended general value <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  **Run the Command:** Execute the command:
    ```bash
    ollama create -f <path_to_modelfile> <new_model_name>
    ```
    *   Example: `ollama create -f ./Modelfiles/qwen2.5-coder qwen2.5-coder-autodev:7b` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

This process creates a new [[using_llama_for_llms | Ollama]] model with the specified context length, which will now function correctly within Bolt.new <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## General Strategies for Working with LLMs

### Start Simple and Iterate

When building applications with LLMs, especially [[using_local_large_language_models_with_autod_dev | local LLMs]], it's crucial to start simple and iteratively add complexity <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This approach helps avoid hallucinations and ensures the application is not broken from the start <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. This strategy is effective even with more powerful LLMs like Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

### Provide Detailed UI/UX Requirements

To guide the LLM effectively, provide specific UI and UX requirements, such as colors, padding, and measurements for views <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. This level of detail helps the LLM design the application precisely as intended <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Recommended Affordable LLM: DeepSeek Coder v2

While [[challenges_and_costs_of_selfhosting_local_llms | local LLMs]] are powerful, they can run into issues with the large prompts of AI coding assistants <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. For a very good, affordable, and open-source large language model, DeepSeek Coder version 2 (236 billion parameter version) is highly recommended <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

DeepSeek Coder v2 is available via OpenRouter or the DeepSeek API directly <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. It is significantly more affordable than Claude, costing around $0.14 per million input tokens and $0.28 per million output tokens, compared to Claude's $3 and $15 respectively <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Its benchmarks for performance are also excellent <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Building an Application with a Local LLM Example

As a demonstration, a chat interface application can be built using a [[using_local_large_language_models_with_autod_dev | local LLM]] like Quin 2.5 Coder 7B (with increased context) in [[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]] <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

1.  **Initial Simple Application:** Start with a basic Next.js chat interface. This initial version will be functional but may lack sophisticated styling <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
2.  **Iterate for UI/UX Improvements:** Provide detailed prompts to the LLM to refine the UI/UX, defining colors, padding, and other design elements <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. The application will then display a much-improved chat interface with features like a loading indicator <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
3.  **Integrate an AI Agent:** Further iterate by connecting the application to an external AI agent via an API endpoint, such as an n8n agent <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. This involves providing the LLM with the API endpoint, expected payload, authorization details, and the output field for responses <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The application will then be able to communicate directly with the AI agent and display its responses <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This demonstrates [[connecting_llms_to_services_using_mcp | connecting LLMs to services]] and [[strategies_for_scaling_ai_with_local_llms | scaling AI with local LLMs]].

This iterative process allows for the creation of a sophisticated chat widget that can talk to an AI agent, all using a small [[using_local_large_language_models_with_autod_dev | local LLM]] <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

## Community and Future Content

Additional content regarding [[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]] is forthcoming, including tutorials on [[core_contributor_applications_for_autod_dev | how to contribute]] and further guidance on deploying applications and working with Docker <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. The community is excited for the future of [[renaming_of_bolt_new_any_llm_to_autod_dev | Autod Dev]] and its capabilities, especially with [[using_local_large_language_models_with_autod_dev | local LLMs]] <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.