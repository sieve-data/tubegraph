---
title: Future of incontext learning vs finetuning
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

The development of Large Language Models (LLMs) and their application in agent systems has sparked discussion regarding the most effective methods for tailoring models to specific tasks. Currently, many agent systems heavily rely on prompt engineering and Retrieval Augmented Generation (RAG) approaches, leading to speculation about the future relevance of [[finetuning_techniques_for_language_models | fine-tuning]] models. <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>

## Current State of Agent Systems and LLMs

Modern LLM-based agents are designed with task-specific "agent loops" <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>. These loops are often hardcoded by humans and are heavily influenced by concepts from reinforcement learning (RL), such as state spaces, action spaces, observation spaces, and reward functions <a class="yt-timestamp" data-t="01:54:07">[01:54:07]</a>. In this new paradigm, traditional neural networks are replaced with language models, allowing state, observation, and action spaces to be represented in natural language <a class="yt-timestamp" data-t="01:54:52">[01:54:52]</a>.

Despite the advancements, current agent performance is still limited. Benchmarks for web navigation and operating system tasks show success rates as low as 12-14% for state-of-the-art models <a class="yt-timestamp" data-t="02:00:25">[02:00:25]</a>. This indicates that while agents are impressive, they are "not quite there yet" <a class="yt-timestamp" data-t="02:00:42">[02:00:42]</a>.

## In-Context Learning (ICL)

In-context learning refers to a model's ability to learn from examples provided directly within its input context, without the need for gradient updates or changes to the model's weights <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>. This approach is prevalent in current agent designs through methods like RAG, where relevant information from a "knowledge bank" (memory) is dynamically added to the LLM's prompt <a class="yt-timestamp" data-t="01:56:30">[01:56:30]</a>.

One benefit of in-context learning is its simplicity. It avoids the complexities of [[finetuning_techniques_for_language_models | fine-tuning]], such as managing GPU memory or curating high-quality, pre-formatted datasets <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>. Agent systems often benefit from providing both successful and unsuccessful demonstrations in context, allowing the model to learn what to do and what to avoid <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>.

## Fine-tuning Language Models

[[finetuning_techniques_for_language_models | Fine-tuning]] involves pushing gradients to update the parameters of a pre-trained language model, adapting it to a specific task or dataset <a class="yt-timestamp" data-t="01:13:49">[01:13:49]</a>. While powerful, [[finetuning_techniques_for_language_models | fine-tuning]] presents challenges:
*   **Computational Cost**: It requires significant GPU resources, making it difficult for many users to perform <a class="yt-timestamp" data-t="01:15:37">[01:15:37]</a>.
*   **Maintenance**: Fine-tuned models may become outdated as base models are updated, necessitating retraining <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.
*   **Complexity**: It requires programming knowledge and expertise in machine learning <a class="yt-timestamp" data-t="01:15:46">[01:15:46]</a>.

## The Potential Decline of Fine-tuning

The speaker hypothesizes that [[finetuning_techniques_for_language_models | fine-tuning]] might eventually "go away" <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a> if context windows for LLMs continue to expand significantly. Models like Gemini 1.5 already offer 1 million tokens of context <a class="yt-timestamp" data-t="01:15:55">[01:15:55]</a>. If context lengths reach 10 million or even a billion tokens, it could become feasible to "copy paste" entire fine-tuning datasets directly into the model's context <a class="yt-timestamp" data-t="01:16:03">[01:16:03]</a>.

This increased context length could lead to in-context learning achieving "parity with [[finetuning_techniques_for_language_models | fine-tuning]]" <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>. The primary method of influencing model behavior would then shift entirely to carefully selecting and structuring the input context – essentially, advanced prompt engineering <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>.

### Arguments for ICL Dominance:
*   **Simplicity**: It drastically simplifies the development pipeline, removing the need for model retraining and maintenance <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>.
*   **Flexibility**: Users could achieve desired behaviors by simply changing the context, without managing multiple fine-tuned models <a class="yt-timestamp" data-t="01:28:07">[01:28:07]</a>.
*   **Scalability**: A single, massive "foundation model" could serve all tasks, configured dynamically via context <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.

### Challenges to ICL Dominance:
*   **Token Consumption and Cost**: Sending extremely long contexts with every inference request could lead to high token consumption and cost <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a>.
*   **Inference Speed**: Large contexts can slow down inference <a class="yt-timestamp" data-t="01:22:54">[01:22:54]</a>.

However, the speaker argues that future improvements in GPU speed, quantization, and techniques like Mixture of Experts (MoE) could mitigate these inference budget concerns, making currently "stupid ideas" like putting an entire browsing history into context feasible <a class="yt-timestamp" data-t="01:50:17">[01:50:17]</a>.

## Implications for Vision-Language Models (VLMs)

The debate extends to Vision-Language Models. Currently, approaches vary: some use a VLM to caption an image (turning it into text) and then use a separate LLM for reasoning, while others attempt end-to-end reasoning with a single VLM <a class="yt-timestamp" data-t="01:24:39">[01:24:39]</a>.

The speaker predicts that the end-to-end VLM approach will become more powerful <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>. As VLMs incorporate larger and stronger language models and vision encoders, it might become unnecessary to have a two-part process. Instead, a single, incredibly general VLM, combined with massive context lengths, could handle any task by simply providing the appropriate in-context examples <a class="yt-timestamp" data-t="01:25:50">[01:25:50]</a>.

## Conclusion

The evolution of LLM-based agents suggests a future where task-specific complexities are increasingly handled through sophisticated prompt engineering and in-context learning. If context window sizes continue to grow exponentially, the fundamental paradigm of how models are adapted and "learn" may shift away from traditional [[finetuning_techniques_for_language_models | fine-tuning]] towards dynamic, context-driven configuration of single, powerful foundation models. This would simplify deployment and maintenance, even if it entails higher per-inference token costs. <a class="yt-timestamp" data-t="01:57:18">[01:57:18]</a>