---
title: Hybrid thinking mode and dynamic thinking budgets
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Quen, developed by the Went team, is a series of large language models (LLMs) and large multimodal models, with the overarching dream of building a generalist model and agent <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.

## Introducing Quen 3

Released shortly before the Spring Festival, Quen 2.5 Max was an instruction-tuned model that served as a strong foundation, achieving competitive performance against state-of-the-art models like Claude 3.5, GPT-4o, and DCB v3 <a class="yt-timestamp" data-t="01:36:13">[01:36:13]</a>. The developers, however, believed in more potential for LLMs beyond simple instruction tuning, especially through reinforcement learning to make them smarter <a class="yt-timestamp" data-t="02:07:33">[02:07:33]</a>. This led to significant performance increases, particularly in [[reasoning_models_and_their_prompting_differences | reasoning tasks]] like math and coding <a class="yt-timestamp" data-t="02:28:44">[02:28:44]</a>.

Recently, the team released Quen 3, their latest large language model, available in multiple sizes of dense and mixture-of-experts (MoE) models <a class="yt-timestamp" data-t="03:18:03">[03:18:03]</a>. The flagship model is an MoE with 235 billion total parameters, activating only 22 billion, making it efficient yet effective <a class="yt-timestamp" data-t="03:33:04">[03:33:04]</a>. A smaller, very fast MoE model with 30 billion total parameters (activating 3 billion) can even outperform Quen 32 billion in some tasks <a class="yt-timestamp" data-t="04:10:48">[04:10:48]</a>. Furthermore, a 4-billion parameter model, developed with distillation techniques, shows [[reasoning_models_and_their_prompting_differences | thinking capabilities]] competitive with the previous flagship, Quen 2.5 72B, and can be deployed on mobile devices <a class="yt-timestamp" data-t="04:37:34">[04:37:34]</a>.

### Hybrid Thinking Mode

A key feature of Quen 3 is its **hybrid thinking mode** <a class="yt-timestamp" data-t="05:24:23">[05:24:23]</a>. This mode allows the model to utilize both thinking and non-thinking behaviors within a single model <a class="yt-timestamp" data-t="05:30:30">[05:30:30]</a>.

*   **Thinking Mode:** In this mode, the model engages in a process of reflection and exploration of possibilities before providing a detailed answer <a class="yt-timestamp" data-t="05:42:32">[05:42:32]</a>. Examples of models with thinking behavior include GPT-4o and Deep R1 <a class="yt-timestamp" data-t="06:05:41">[06:05:41]</a>.
*   **Non-Thinking Mode:** This functions like a traditional instruction-tuned chatbot, providing near-instant answers without an explicit thinking process <a class="yt-timestamp" data-t="06:09:47">[06:09:47]</a>.

Quen 3 is noted as potentially the first in the open-source community to combine these two modes into a single model. Users can control its behavior using prompts or hyperparameters <a class="yt-timestamp" data-t="06:23:17">[06:23:17]</a>.

### Dynamic Thinking Budget

Building on the hybrid thinking mode, Quen 3 introduces the feature of **dynamic thinking budget** <a class="yt-timestamp" data-t="06:40:48">[06:40:48]</a>. The thinking budget defines the maximum number of thinking tokens the model can use for a task <a class="yt-timestamp" data-t="06:46:08">[06:46:08]</a>.

*   **Usage:** If a task requires thinking, and the thinking process finishes within the allocated budget (e.g., 8,000 tokens within a 32,000-token budget), the model provides the answer <a class="yt-timestamp" data-t="06:58:33">[06:58:33]</a>. However, if the thinking process requires more tokens than the budget allows (e.g., 8,000 tokens needed for a 4,000-token budget), the thinking process is truncated at the budget limit <a class="yt-timestamp" data-t="07:16:32">[07:16:32]</a>.
*   **Performance Impact:** Performance significantly increases with larger thinking budgets <a class="yt-timestamp" data-t="07:40:02">[07:40:02]</a>. For instance, in AM 24, a small thinking budget might yield just over 40% performance, while a large budget of 32,000 tokens can achieve over 80% <a class="yt-timestamp" data-t="07:51:39">[07:51:39]</a>.
*   **Efficiency:** This feature allows users to optimize token usage; for example, if a task requires 95% accuracy, one might find that an 8,000-token thinking budget is sufficient, avoiding the waste of more tokens <a class="yt-timestamp" data-t="08:21:04">[08:21:04]</a>.

### Enhanced Agent Capabilities

Quen 3 has significantly increased capabilities in agents and coding, with enhanced support for popular frameworks like MCP <a class="yt-timestamp" data-t="09:40:11">[09:40:11]</a>. The models can effectively use tools during their thinking process, make [[dynamic_vs_static_tool_calling | function calls]], receive feedback from the environment, and continue thinking, which is beneficial for inference time scaling <a class="yt-timestamp" data-t="09:55:05">[09:55:05]</a>.

Examples provided include:
*   Using tools during thinking, receiving feedback, and continuing to think while making function calls <a class="yt-timestamp" data-t="09:55:05">[09:55:05]</a>.
*   Organizing a desktop by accessing the file system, thinking about which tools to use, executing them, getting feedback, and continuing to think until the task is complete <a class="yt-timestamp" data-t="10:29:08">[10:29:08]</a>.

The goal is to evolve models beyond simple chatbots into highly productive agents in real-world working environments <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.

### Future Directions

In the future, the focus will shift from merely training models to training agents <a class="yt-timestamp" data-t="21:10:48">[21:10:48]</a>. This involves:

*   **Enhanced Pre-training:** Utilizing more and cleaner multimodal data, along with synthetic data, potentially incorporating reinforcement learning into pre-training itself, moving beyond next token prediction <a class="yt-timestamp" data-t="21:17:15">[21:17:15]</a>.
*   **Scaling Laws Evolution:** Shifting from scaling model sizes and pre-training data to scaling compute in reinforcement learning <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>.
*   **Long-Horizon Reasoning:** Focusing on models capable of long-horizon reasoning with environment feedback. Models that can interact with their environment, receive feedback, and continue thinking are expected to become increasingly competitive and smarter with inference time scaling <a class="yt-timestamp" data-t="22:28:13">[22:28:13]</a>. This approach leans towards [[proactive_ai_versus_reactive_ai | proactive AI]] agents that can plan and adapt.
*   **Context Scaling:** Aiming to scale context to at least 1 million tokens for most models this year, with an eventual goal of 10 million tokens and even infinite context <a class="yt-timestamp" data-t="22:56:56">[22:56:56]</a>.
*   **Modality Scaling:** Increasing model capabilities and productivity by scaling modalities in both inputs and outputs <a class="yt-timestamp" data-t="23:25:01">[23:25:01]</a>. This includes vision language understanding for tasks like creating GUI agents and unifying understanding and generation (e.g., image understanding and generation simultaneously) <a class="yt-timestamp" data-t="23:37:38">[23:37:38]</a>.

These efforts emphasize the transition from training models to training sophisticated [[dynamic_planning_for_complex_tasks_in_ai | AI agents]] capable of complex interactions and reasoning <a class="yt-timestamp" data-t="24:36:23">[24:36:23]</a>.