---
title: Reasoning in AI models
videoId: Wo95ob_s_NI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The development of sophisticated reasoning capabilities in Artificial Intelligence (AI) models is a key area of research and discussion. This article outlines the current understanding, challenges, and future directions in enhancing AI reasoning, based on insights from John Schulman, co-founder of OpenAI.

## Current State of Reasoning

Current AI models, particularly Large Language Models (LLMs), demonstrate impressive abilities on a "per token basis," potentially matching the smartest humans in generating immediate, contextually relevant text <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Pre-training endows these models with a broad base of knowledge and the ability to generate diverse content by predicting subsequent tokens <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a> <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

However, significant limitations exist, particularly in:
*   **Long-term Coherence:** While smart on a per-token level, models struggle to maintain coherence over extended interactions or complex tasks, such as writing a multi-file coding project aligned with broader goals [[the_future_of_programming_and_ai_tools_like_github_copilot]] <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a> <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Deep Thinking and Attention:** Models can "struggle to really think hard about things or pay attention to what you ask them" <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a> <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
*   **Error Recovery and Edge Cases:** Current models may get "stuck and get lost" when encountering errors or edge cases, though future models are expected to improve in recovering from errors [[challenges_in_ai_alignment_and_potential_risks]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Miscellaneous Deficits:** Even with improvements in long-horizon tasks, other "miscellaneous deficits" may persist, causing models to get stuck or make worse decisions than humans in certain situations <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Improving Reasoning Capabilities

Several avenues are being explored to enhance the reasoning abilities of AI models.

### Training on More Complex and Longer Tasks
A fundamental approach involves training models specifically to handle more involved and longer-duration tasks <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This could involve tasks like carrying out an entire coding project, requiring the model to write multiple files, test code, and iterate based on output <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This training can be done through methods like Reinforcement Learning (RL), supervising the final output, or supervising each step [[reinforcement_learning_from_human_feedback_rlhf]] <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a> <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Long-Horizon Reinforcement Learning (RL)
Training models for long-horizon tasks using RL is seen as a key step <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. The ability to act coherently for longer periods is a primary unlock expected from this training regime <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. However, it's not anticipated that this alone will solve all capability deficits <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a> <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Internal Monologue and Chain-of-Thought
Improving reasoning through an "internal monologue" or step-by-step thinking is being explored via two main approaches:
1.  **Training-Time Learning:** The model learns from its own outputs over several potential "trains of thought," and is then trained on the path that leads to the correct answer before deployment <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a> <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.
2.  **Inference-Time Computation:** The model uses significant compute resources during deployment to "talk to itself" and explore different reasoning paths [[ai_alignment_and_safety_research]] <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a> <a class="yt-timestamp" data-t="00:31:56">[00:31:56]</a>.

Schulman suggests that the best results will likely come from combining these two strategies—gaining from practice at training time and performing computation at test time <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a> <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. Reasoning, in this context, can be defined as tasks requiring some form of computation or deduction at test time <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a> <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.

### Introspection, Active Learning, and Mid-Term Memory
Current systems largely learn through massive pre-training or transient in-context learning <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a> <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>. A "middle ground" is considered missing:
*   **Deliberate, Active Learning:** This involves models not just possessing memory, but also specializing in certain tasks, putting effort into particular projects, and reasoning to develop knowledge <a class="yt-timestamp" data-t="00:35:28">[00:35:28]</a> <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.
*   **Introspection and Self-Knowledge:** Models could use introspection or self-knowledge to identify gaps in their understanding and actively seek out new information to fill those holes [[role_of_memory_in_learning_and_understanding]] <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a> <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. This capability might emerge from models' existing calibration regarding their own knowledge and limitations <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a> <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>.
This could manifest as a form of "medium-term memory" – too large for current context windows but smaller in scale than pre-training data <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>. Such capabilities are expected to become more crucial for long-horizon tasks <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a> <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>.

### Learned Algorithms for Exploration and Search
For learning within a specific task (test-time learning), especially for complex projects, policy gradient RL algorithms might not be the most sample-efficient <a class="yt-timestamp" data-t="00:39:52">[00:39:52]</a>. Instead, future systems might rely more on:
*   **In-context learned algorithms:** Models that have learned how to explore, try possibilities exhaustively, and avoid repeating mistakes <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a> <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>.
*   **Learned search algorithms:** These would be employed for specific tasks, allowing for more efficient problem-solving [[alphazero_and_efficient_search_techniques]] <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>.

## Reasoning and Generalization

A key question is the extent to which reasoning skills generalize across domains or from specific training data.
*   **Cross-Lingual Generalization:** Fine-tuning on English data can lead to improved behavior in other languages, suggesting the model latches onto a "helpful persona" that transcends language <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a> <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   **Multimodal Generalization:** Text-only fine-tuning can sometimes lead to reasonable behavior with images <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **Understanding Limitations:** A small amount of data (e.g., ~30 examples) teaching a model about its limitations (like not being able to send emails) generalized well to other capabilities it wasn't explicitly trained on <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a> <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a> <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Code to Language Reasoning:** The hypothesis that training on code improves reasoning in natural language is an area of interest, but public results from ablation studies at scale (e.g., GPT-4 size) are not yet available to confirm this <a class="yt-timestamp" data-t="00:54:34">[00:54:34]</a> <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>. Schulman notes that transfer might be more evident in larger models which can learn better shared representations, compared to smaller models that might rely more on memorization <a class="yt-timestamp" data-t="00:57:20">[00:57:20]</a> <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.

## Impact on Future Capabilities

Improvements in reasoning are expected to unlock more sophisticated applications:
*   **Complex Coding Projects:** Models could autonomously manage entire coding projects [[impact_of_ai_on_software_development_and_productivity]] <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Scientific Research:** AI could accelerate science by understanding vast amounts of literature and sifting through data [[ai_for_science_and_societal_challenges]] <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a> <a class="yt-timestamp" data-t="01:03:31">[01:03:31]</a>.
*   **Taste and Ambiguity:** Human experts bring qualities like "taste" or better dealing with ambiguity, which are important for tasks like research. Future models will need to develop or simulate these <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

While long-horizon RL and improved coherence are significant, they are not expected to be a silver bullet. Other "mundane limitations" or "miscellaneous deficits" <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a> <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a> might still pose challenges on the path to more generally capable AI.