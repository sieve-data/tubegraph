---
title: Meta prompting with language models
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

Meta prompting involves [[using_language_models_to_generate_text | using language models (LLMs) to generate text]] to assist in the prompt engineering process itself <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This technique leverages LLMs to create, refine, or improve prompts <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## What is Meta Prompting?

At its core, meta prompting means using an LLM to help in the design and optimization of other prompts <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This can involve tasks such as:
*   Generating initial prompt drafts <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Refining existing prompts for clarity or effectiveness <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>
*   Improving prompt performance <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>

It's considered a valuable approach because it makes sense to use the same technology (LLMs) that users are interacting with to assist in crafting their inputs <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Tools and Frameworks for Meta Prompting

There are numerous frameworks available for meta prompting, some of which may require specialized knowledge, while others are more accessible <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Several user-friendly tools are also available:
*   **Anthropic** offers a notable tool <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **OpenAI Playground** includes functionality for meta prompting <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Prompt Hub** provides its own meta prompting tool <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Prompt Hub's tool offers a unique feature: it allows users to select their specific model provider (e.g., OpenAI or Anthropic). The system then runs a different meta prompt tailored to that provider, recognizing that a prompt effective for an OpenAI model might not perform the same way with an Anthropic model <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This highlights the importance of [[strategies_for_adapting_ai_models_and_prompts | adapting AI models and prompts]].

Additionally, Prompt Hub includes a co-pilot feature that facilitates iterative work, allowing users to run prompts and provide feedback to refine them <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This iterative process is built on concepts similar to frameworks like TechGrad <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.