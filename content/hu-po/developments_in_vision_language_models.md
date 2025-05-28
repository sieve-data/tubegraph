---
title: Developments in Vision Language Models
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

[[vision_language_models | Vision Language Models]] (VLMs) are increasingly being used in agent architectures, though current performance indicates significant room for improvement. While some refer to them as "multimodal LLMs" (mLLM), the term VLM is preferred due to its conciseness <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

## VLM Integration in Agent Architectures
A common approach for integrating VLMs into agent systems involves two main strategies:
1.  **Modular Approach (Caption then Reason)**: Utilizing a [[vision_language_models | VLM]] to caption an image (turning it into text), and then feeding this text into a separate Large Language Model (LLM) for reasoning <a class="yt-timestamp" data-t="01:23:37">[01:23:37]</a>. This approach involves two distinct models <a class="yt-timestamp" data-t="01:24:43">[01:24:43]</a>.
2.  **End-to-End Approach**: Directly using a single [[vision_language_models | VLM]] to perform both visual perception and reasoning <a class="yt-timestamp" data-t="01:24:49">[01:24:49]</a>. This method is seen as potentially more powerful, particularly with the use of larger and stronger language models within the VLM architecture <a class="yt-timestamp" data-t="01:24:52">[01:24:52]</a>. The prediction is that this end-to-end approach will become more dominant <a class="yt-timestamp" data-t="01:29:55">[01:29:55]</a>.

### Performance in Benchmarks
Benchmarking shows that current [[vision_language_models | VLM]]-based agents are not yet performing at human levels:
*   On the OS World benchmark, which involves operating system tasks like opening windows and moving files, the best model achieves only 12% success, compared to humans at over 72% <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   On the Web Arena benchmark, focused on web-based tasks, the best GPT-4 agent achieves a 14% end-to-end success rate, significantly lower than human performance of 78% <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.
*   An interesting observation from the Web Arena benchmark indicates that providing a raw screenshot to GPT-4V is more useful than an explicit XML description of the screen elements <a class="yt-timestamp" data-t="01:39:38">[01:39:38]</a>.

### Architectural Considerations
Typically, the language model component within [[vision_language_models | VLMs]] tends to be smaller due to memory and fine-tuning constraints <a class="yt-timestamp" data-t="01:33:02">[01:33:02]</a>. However, companies like Groq are willing to scale up their models, suggesting a trend towards larger language model components within VLMs to achieve higher benchmark scores <a class="yt-timestamp" data-t="01:34:02">[01:34:02]</a>.

## Future Trends and Challenges
### Context Length
The increasing context length of [[vision_language_models | VLMs]] (e.g., Gemini 1.5 with 1 million tokens) <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a> may lead to a future where fine-tuning models becomes less necessary <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. Instead, an entire fine-tuning dataset could potentially be included directly in the context of the model, allowing for in-context learning to achieve desired behaviors <a class="yt-timestamp" data-t="01:16:03">[01:16:03]</a>. This shift could drastically simplify the development pipeline, as it removes the complexities of GPU availability and specialized deep learning knowledge required for fine-tuning <a class="yt-timestamp" data-t="01:15:33">[01:15:33]</a>.

### Agent Loop Generality
Current agent loops are often task-specific, designed with specific assumptions and inductive biases tailored to tasks like web browsing or academic research <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>. A future goal is to develop a "foundation agent" or a general agent loop that is agnostic and effective across all types of tasks, similar to how large language models generalized across sequence-to-sequence tasks <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>.

### Terminology
The field of AI, particularly in agents and [[vision_language_models | VLMs]], suffers from a "word soup" where different terms often describe similar concepts (e.g., "knowledge bank," "memory," "entity-centric knowledge store" all refer to cold memory storage) <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>. Concepts like reward functions, value functions, Q-functions, and evaluation models all describe a mechanism for scoring the utility of states or actions <a class="yt-timestamp" data-t="00:57:44">[00:57:44]</a>.

## Conclusion
Despite current limitations in performance on benchmarks like OS World and Web Arena, [[vision_language_models | VLMs]] and agent research show promise. The field is moving towards more generalized architectures, potentially leveraging ever-increasing context lengths to replace traditional fine-tuning with in-context learning. The core ideas of reinforcement learning, adapted to work with natural language for state and action spaces, are being recycled and refined in this modern context <a class="yt-timestamp" data-t="01:54:47">[01:54:47]</a>.