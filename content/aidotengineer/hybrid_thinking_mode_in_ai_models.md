---
title: Hybrid thinking mode in AI models
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Hybrid thinking mode is a significant feature introduced in Quen 3, allowing a single model to utilize both "thinking" and "non-thinking" behaviors <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This capability combines two distinct approaches to AI model operation <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Components of Hybrid Thinking Mode

*   **Thinking Mode**
    *   In this mode, before providing a detailed answer, the model engages in a process of reflection, exploring possibilities, and determining its readiness to answer <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Models like 01 and Deep R1 exhibit this "thinking behavior" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Non-thinking Mode**
    *   This is akin to a traditional instruction-tuned model or a chatbot <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   It provides answers without an explicit thinking process, resulting in near-instant responses <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

Quen 3 is noted as potentially the first instance in the open-source community to combine these two modes into a single model <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Users can control the model's behavior using prompts or hyperparameters <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Dynamic Thinking Budget

A key feature enabled by the hybrid thinking mode is the "dynamic thinking budget" <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This budget defines the maximum number of thinking tokens an AI model can use for a given task <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

*   **Impact of Budget**: If a task requires more thinking tokens than the allotted budget, the thinking process will be truncated at the budget limit <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Performance**: Performance generally increases with larger thinking budgets <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For example, in the AM 24 benchmark, a small thinking budget might yield just over 40% performance, while a large budget of 32,000 tokens can achieve over 80% <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Optimization**: Users can tailor the thinking budget to meet specific accuracy requirements, avoiding wasted tokens if a lower budget still achieves the desired outcome (e.g., 8,000 tokens for over 95% accuracy in a task) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Application in [[multimodal_ai_systems | Multimodal AI Systems]]

The concept of thinking capabilities and [[chain_of_thought_reasoning_in_ai | dynamic thinking budget]] has also been explored for [[multimodal_ai_systems | vision language models]] like QVQ <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. Similar to language-only models, a larger thinking budget in [[multimodal_ai_systems | vision language models]] leads to better performance, especially in [[chain_of_thought_reasoning_in_ai | reasoning tasks]] such as mathematics <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

## Agent Capabilities

The ability to combine thinking with environmental interaction is a key aspect of developing productive AI agents <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Models with hybrid thinking mode can use tools, receive feedback from the environment, and continue thinking, which is beneficial for inference-time scaling <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This capability is crucial for models to evolve beyond simple chatbots into highly productive agents in various working life scenarios <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.