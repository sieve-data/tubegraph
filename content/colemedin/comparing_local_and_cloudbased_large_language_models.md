---
title: Comparing local and cloudbased large language models
videoId: 8ommGcs_-VU
---

From: [[colemedin]] <br/> 

The development of Autod Dev, a community-driven project for Bolt.new, aims to enable the use of various large language models (LLMs), including local ones via Ollama <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While Bolt.new originally supported only one LLM, Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, there's a strong demand for [[working_with_local_large_language_models | local LLMs]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Benefits and Drawbacks of Local LLMs

### Cost and Accessibility
One of the primary [[benefits_of_hosting_your_own_large_language_models | benefits of hosting your own large language models]] is the elimination of costs and rate limits associated with cloud-based LLMs <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. [[working_with_local_large_language_models | Local LLMs]] allow for unlimited, free usage on your own machine <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Smaller local models, like Quin 2.5 Coder 7B, can be run on "almost any computer" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, making them highly accessible.

### Performance
Generally, "massive close-source models" such as Claude 3.5 Sonnet and GPT-4o offer the best performance <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. However, [[limitations_of_large_language_models | smaller local LLMs]] can still perform "really, really well" for building full applications <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### Addressing Local LLM Limitations
[[challenges_with_large_language_models | Local LLMs]] may encounter issues with the larger prompts used by AI coding assistants, which isn't typically seen with bigger cloud models <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This is often due to the default context length in Ollama models being too small (2048 tokens) to accommodate the Bolt.new prompt <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

To resolve this, users can create a variation of an Ollama model with an increased context length <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. A context length above 8192 is sufficient, with 32768 tokens generally recommended <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This adjustment significantly improves the model's ability to interact with the web container in Bolt.new <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Recommended Open-Source Model
For a powerful, affordable, and open-source alternative to proprietary models, DeepSeek Coder version 2 (236 billion parameters) is highly recommended <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. It can be accessed via OpenRouter or the DeepSeek API <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

It is significantly cheaper than Claude:
*   **DeepSeek Coder:** $0.14 per million input tokens and $0.28 per million output tokens <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Claude:** $3 per million input tokens and $15 per million output tokens <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
DeepSeek Coder is more than 20 times more affordable than Claude, and similar savings apply compared to GPT <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. It also boasts "incredible" benchmarks and performance <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. While DeepSeek Coder 236B is massive, it can also be run locally <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Development Strategy with Local LLMs
When [[working_with_local_large_language_models | working with local large language models]] in Autod Dev, a key tip is to "start really simple and iteratively get more complicated" to minimize hallucinations and ensure functionality <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This strategy is effective even with more powerful LLMs like Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Providing specific design details, such as colors, padding, and measurements, can significantly help the LLM in designing the application <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

> [!Example] Building a Chat Interface with a Local LLM
> A basic Next.js chat interface can be built using the Autod Dev version of Quin 2.5 Coder 7B, demonstrating its capability for initial app creation <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This simple base can then be iteratively improved with more complex UI/UX requirements <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. The application can be further extended to integrate with an n8n agent API endpoint to interact with an AI agent hooked to a RAG system and PG Vector database <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

The ability to use [[using_local_large_language_models_with_autod_dev | local large language models with Autod Dev]] is a "very good starting point" for creating production-ready applications <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.