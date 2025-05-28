---
title: Vision language models in AI agents
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

AI agents are a significant area of research in artificial intelligence, involving large language models (LLMs) that can access tools and operate in a continuous loop to perform tasks <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Initially, there was significant hype around startups like "Devin," which advertised the ability of agents to solve programming tasks on platforms such as Upwork, leading to claims of the "end of software engineering" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

However, recent revelations have shown that demonstrations of Devin were "faked" <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Issues included:
*   The problem solved in the demo did not match stated requirements <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Files shown being edited did not exist in the repository <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Tasks presented as quickly completed actually stretched over many hours or even into the next day <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

This situation highlights that current AI agents "are just not quite there yet" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Benchmarks reinforce this, with humans achieving over 72% success on tasks, while the best models manage only 12% (OS World benchmark) or 14% (Web Arena benchmark) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>, <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>. This suggests that agents are currently "getting oversold" <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Agent Architectures and Reinforcement Learning Influence

Many modern agent designs, particularly those based on large language models, borrow heavily from concepts in reinforcement learning (RL) <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>. The core concept is the **Markov Decision Process (MDP)**, or more commonly, a **Partially Observable Markov Decision Process (POMDP)**, which models environments as a set of states, actions, transitions, and rewards <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>, <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.

Key components commonly found in agent architectures include:
*   **Perception or Observation State** – The agent's input from the environment, which can be images, text, or structured information <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Memory (Retrieval Augmented Generation, RAG)** – A mechanism for the agent to access and retrieve relevant information from a "cold storage" memory bank to augment its current context <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, <a class="yt-timestamp" data-t="00:44:31">[00:44:31]</a>. This can include both successful and unsuccessful demonstrations <a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a>.
*   **Thinking** – Using multiple auto-regressive steps to generate more context or "reason" in natural language before producing a final answer <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This mirrors human internal thought processes <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Role-playing** – Assigning different identities or "system prompts" to multiple LLMs to influence their behavior in multi-agent systems <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Action** – The output of the agent, which can be free-form text or direct control signals like mouse and keyboard inputs <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>, <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Learning** – How the agent improves, either by pushing gradients (traditional fine-tuning) or by building up its memory bank for better retrieval <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

A key evolution in agent design is the shift from traditional numerical vector inputs/outputs to natural language for state, observation, and action spaces <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>. This allows for a more "fuzzy" and natural interaction that resembles human cognition <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>.

## Role of [[vision_language_models | Vision Language Models]] (VLMs)

[[vision_language_models | Vision Language Models]] are crucial for agents interacting with visual environments. There are two main approaches:
1.  **Modular "Caption then Reason"**: Using a [[vision_language_models | VLM]] to caption an image (turn it into text), and then feeding that text into a separate LLM for reasoning and action selection <a class="yt-timestamp" data-t="01:24:18">[01:24:18]</a>.
2.  **End-to-End**: Using a single [[vision_language_models | VLM]] to handle both the visual perception and the reasoning directly <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>. This approach is generally seen as more powerful and efficient, as it avoids the complexities and latency of a two-part pipeline <a class="yt-timestamp" data-t="01:29:55">[01:29:55]</a>.

Historically, the language model component of [[vision_language_models | VLMs]] has been smaller than standalone LLMs due to memory constraints and the need to fine-tune the entire model, including the vision encoder <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>. However, newer models like Grok 1.5V suggest a trend towards using larger, more powerful language models within [[vision_language_models | VLMs]], potentially improving their reasoning capabilities <a class="yt-timestamp" data-t="01:33:59">[01:33:59]</a>.

## [[inference_challenges_and_optimizations_in_visionbased_agents | Inference Challenges and Optimizations]]

[[inference_challenges_and_optimizations_in_visionbased_agents | Inference speed]] is a critical challenge, especially for competitive games or real-time tasks where rapid action is required <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. Turn-based games or communication-focused tasks are easier for agents because they allow more time for complex inference, reflection, and RAG processes <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.

A growing area of speculation is the potential obsolescence of traditional fine-tuning for models. As context windows in LLMs and [[vision_language_models | VLMs]] become increasingly large (e.g., Gemini 1.5's 1 million tokens, with projections of 10 million or even a billion tokens in the future) <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>, <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>, it may become feasible to embed an entire fine-tuning dataset directly into the model's context. This "in-context learning" could eliminate the need for separate fine-tuning processes, simplifying the development pipeline and making models more adaptable on the fly <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>, <a class="yt-timestamp" data-t="01:21:57">[01:21:57]</a>. While this would increase the per-query inference cost due to larger context lengths, it could offer long-term benefits in terms of deployment and maintenance compared to retraining numerous fine-tuned models <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a>.

## [[Future directions and implications of AI in vision language models | Future Outlook]]

Currently, most agent loops are task-specific and "hardcoded," relying on specific heuristics and human-designed systems to filter and select information for the LLM's context <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>, <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a>. The long-term goal is to move towards a more "agnostic" or "generic" agent loop that can apply to any task, resembling the generalizability seen in modern foundation models <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>, <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>. This would represent a significant leap towards achieving Artificial General Intelligence (AGI) that can discover and learn new knowledge through experimentation and experience in the world <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>.

The development of larger, more generic [[vision_language_models | VLMs]] that can perform end-to-end reasoning, combined with expanded context windows, points towards a future where a single, powerful [[vision_language_models | VLM]] could adapt to a wide range of tasks simply by receiving relevant examples within its context <a class="yt-timestamp" data-t="01:29:55">[01:29:55]</a>, <a class="yt-timestamp" data-t="01:30:01">[01:30:01]</a>. This approach aims for a more natural and less "materialistic" view of reality, where the "state" of the world is less deterministic and more "fuzzy," akin to human perception <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>, <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.