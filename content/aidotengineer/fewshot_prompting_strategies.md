---
title: Fewshot prompting strategies
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

Few-shot prompting is a technique in prompt engineering that involves including examples of desired inputs and outputs within the prompt itself <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This method allows the model to mimic or understand the problem by showing rather than telling <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## How it Works <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>
Instead of explicitly describing the desired tone or style, you provide input and output examples that demonstrate what you want the model to achieve <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

> [!EXAMPLE] Content Generation
> To generate content for a client, you might provide a "brief" (input) and "related content" (output) example. Then, when you provide a new "brief," the model will fill in the corresponding content, having learned from the example how to match the client's tone and style <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Benefits and Effectiveness <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>
*   **Most Gains from Few Examples**: Most performance improvements are seen with just one or two examples <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The graph of performance versus the number of examples typically shows significant gains early on <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Ease of Implementation**: It's a straightforward and accessible way to get better outputs from large language models (LLMs) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Diversity of Examples**: It's beneficial to select diverse examples that cover different inputs the model is expected to handle <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

## Considerations
*   **Performance Degradation**: Sometimes, performance can degrade if too many examples are included <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Interaction with [[reasoning_models_and_their_unique_prompting_requirements|Reasoning Models]]**: With newer [[reasoning_models_and_their_unique_prompting_requirements|reasoning models]], adding examples can sometimes lead to worse performance or overcomplicate things, confusing the model <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Researchers at DeepSeek, for instance, found that few-shot examples degraded performance when building their R1 model <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. If using few-shot with these models, it's advisable to start with only one or two examples <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Few-Shot and [[chain_of_thought_prompting_techniques|Chain of Thought Prompting]]
Few-shot examples can be used within [[chain_of_thought_prompting_techniques|Chain of Thought prompting]] by including examples of the model's desired reasoning steps <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For example, when solving math problems, you can provide an example problem that explicitly shows the step-by-step reasoning process <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. LLMs can also be used to generate these reasoning chains for few-shot examples automatically <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.