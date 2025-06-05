---
title: Current and Future Trends in Large Language Models
videoId: JIsgyk0Paic
---

From: [[aidotengineer]] <br/> 

Will Brown, a machine learning researcher at Morgan Stanley, presented insights on the future of [[large_language_models_in_ai_agents | agents]] and the increasing role of [[reinforcement_learning_in_large_language_models | reinforcement learning]] (RL) in their development at the AI Engineer Conference <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. His talk focused on speculative future directions rather than current production systems or best practices <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The goal is to prepare for a future where [[reinforcement_learning_in_large_language_models | reinforcement learning]] becomes integral to the [[large_language_models_in_ai_agents | agent]] engineering loop <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Current State of Large Language Models

Most [[large_language_models | LLMs]] are currently understood as chatbots <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Using OpenAI's five levels framework, progress has been strong in chatbots and reasoners <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These models, such as GPT-4, GPT-3, Gemini, and Grok-3, excel at question answering and interactive problem-solving, particularly for longer reasoning tasks <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

The current challenge is to advance to Level 3: [[large_language_models_in_ai_agents | agents]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. These are systems designed to take actions and perform longer, more complex tasks <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Present approaches involve chaining multiple calls to underlying chatbot or reasoner [[large_language_models | LLMs]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Techniques like prompt engineering, tool calling, and human-in-the-loop evaluations are common <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. While results are "pretty good," true autonomous [[large_language_models_in_ai_agents | agents]] with AGI-level capabilities are not yet realized <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Agents vs. Pipelines

It's useful to distinguish between [[large_language_models_in_ai_agents | agents]] and pipelines (or workflows) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Pipelines are systems with relatively low autonomy, requiring significant engineering to define decision trees and refine prompts <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

Winning applications in the "[[large_language_models_in_ai_agents | agent]] space" often feature tight feedback loops where users interact with an interface, get quick responses, and perform short tasks <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Examples include IDEs like Cursor, Warp, and Replit, and search tools for complex question-answering <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Few current [[large_language_models_in_ai_agents | agents]] can operate autonomously for more than 10 minutes <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Exceptions like Devin, Operator, and OpenAI's Deep Research are seen as moving towards more autonomous [[large_language_models_in_ai_agents | agents]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## The Role of Reinforcement Learning

The traditional definition of [[large_language_models_in_ai_agents | agents]] in [[reinforcement_learning_in_large_language_models | reinforcement learning]] involves a system interacting with an environment to achieve a goal, learning to improve over time through repeated interaction <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This iterative improvement is often missing in current LLM applications <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. If an LLM-powered system performs at 70% accuracy after prompt tuning, getting to 90% often lacks a clear path forward without better models or tools for continuous learning <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Model Trends and Unlocks

Current model trends suggest:
*   **Pre-training**: Showing diminishing returns on capital, indicating a need for new techniques <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **RLHF (Reinforcement Learning from Human Feedback)**: Excellent for creating friendly chatbots but doesn't consistently push the frontier for increasingly smarter models <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Synthetic Data**: Good for distilling larger models into smaller, performant ones, but not a standalone unlock for massive capabilities unless combined with verification or rejection sampling <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **[[reinforcement_learning_in_large_language_models | Reinforcement Learning]]**: Appears to be the key trick for enabling test-time scaling in models like GPT-4 and DeepSeek-R1 <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. It's not bottlenecked by manually curated human data and has shown practical effectiveness <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### DeepSeek-R1 and OpenAI's Deep Research

The DeepSeek-R1 model and paper were significant because they explained how a model like GPT-4 is built, revealing that [[reinforcement_learning_in_large_language_models | reinforcement learning]] is at its core <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The process involves giving the model questions, measuring answer correctness, and iteratively giving feedback to reinforce successful strategies <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. The long chain-of-thought reasoning in these models emerges as a byproduct of this RL process, rather than being explicitly programmed <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. [[reinforcement_learning_in_large_language_models | Reinforcement learning]] excels at identifying effective strategies for problem-solving <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

OpenAI's Deep Research, an example of an end-to-end [[reinforcement_learning_in_large_language_models | reinforcement learning]] system, can perform up to a hundred tool calls for browsing and querying the internet to synthesize answers <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. While impressive, it's not AGI and struggles with out-of-distribution tasks or highly manual calculations <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This suggests that [[reinforcement_learning_in_large_language_models | reinforcement learning]] unlocks new skills and autonomy but doesn't grant universal problem-solving capabilities <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. It offers a path to teaching models skills and improving them in conjunction with environments, tools, and verification <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## How Reinforcement Learning Works for LLMs

The core idea of [[reinforcement_learning_in_large_language_models | reinforcement learning]] is **explore and exploit**: try things, see what works, and do more of the successful actions <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. For example, in [[large_language_models_in_code_generation | code generation]], a model writes code to pass test cases, receiving numerical rewards for formatting, language use, and passing tests <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This means the model learns from synthetic data rollouts and their scores, rather than pre-curated datasets <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The GRPO algorithm, used by DeepSeek, illustrates this simply: for a given prompt, sample multiple completions, score them, and train the model to be more like the higher-scoring ones <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. This is typically applied in single-turn reasoner models, not yet fully in the [[large_language_models_in_ai_agents | agentic]] world <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Rubric Engineering

[[Experiments with Large Language Models and AI Assisted Work | Experiments with Large Language Models and AI Assisted Work]] have shown that even simple [[reinforcement_learning_in_large_language_models | reinforcement learning]] setups can catch the imagination of the community <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. A single Python file demonstration using the GRPO algorithm to train a small Llama model for math reasoning revealed how accuracy improved and reasoning chains extended with RL <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

This led to the concept of **rubric engineering**, akin to prompt engineering <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. When a model undergoes [[reinforcement_learning_in_large_language_models | reinforcement learning]], it receives a reward, but the design of this reward is crucial <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Beyond simple right/wrong answers, models can be rewarded for:
*   Following specific XML structures <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   Adhering to output formats (e.g., producing an integer answer even if incorrect) <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

This offers significant room for creativity in designing rules that allow the model to understand its own performance and use that feedback for further training <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Future opportunities include using [[large_language_models | LLMs]] to design or autotune these rubrics, incorporating LLM judges for scoring, and preventing reward hacking, where models find ways to maximize reward without truly performing the task <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

## Future of AI Engineering in the RL Era

A new framework is being developed for doing [[reinforcement_learning_in_large_language_models | reinforcement learning]] inside multi-step environments <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. The idea is to leverage existing [[large_language_models_in_ai_agents | agent]] frameworks by creating an "environment" that the model plugs into, allowing interaction protocols to be defined without worrying about weights or tokens <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This allows models to continuously improve over time with defined rewards <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

Key considerations for the future of AI engineering in the RL era include:
*   **Off-the-shelf API models**: It's uncertain if they will be sufficient for all tasks <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Skill vs. Knowledge**: It's hard to instill a "skill" through prompting alone; models, like humans, often require trial and error to truly master a skill <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. RL has been the most promising unlock for higher autonomy [[large_language_models_in_ai_agents | agents]] <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Fine-tuning**: Despite being written off by some, fine-tuning remains important, especially as the gap between open and closed-source models closes <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. True RL for models like DeepSeek-R1 and Deep Research requires fine-tuning <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

Many challenges and research questions remain <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. However, skills learned in current AI engineering, such as building environments and rubrics, are directly transferable to building evaluations and prompts <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. The need for good monitoring tools and a supportive ecosystem of companies and products will persist <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. Looking ahead, [[reinforcement_learning_in_large_language_models | reinforcement learning]] may be essential to unlock truly autonomous [[large_language_models_in_ai_agents | agents]], innovators, or organizations powered by [[large_language_models | language models]] <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.