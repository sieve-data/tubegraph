---
title: AI agents beyond chatbots
videoId: UOsOfLnAX3Y
---

From: [[aidotengineer]] <br/> 

AI agents represent a significant evolution in computing, moving beyond the capabilities of simple chatbots to perform complex tasks autonomously <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This field has garnered considerable attention, with figures like Bill Gates describing it as "the biggest revolution in computing" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> and Andrew Ng noting it as "massive AI progress" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Sam Altman from OpenAI has even suggested that 2025 could be "the year of agent" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Despite the enthusiasm, there are also criticisms, with some viewing agents as mere wrappers around large language models (LLMs) that struggle with planning and practical solutions, as seen with issues like AutoGPT <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. However, the core concept of agents is not new; it is the enhanced power derived from LLMs that has made them more capable today <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## What is an AI Agent?

An [[ai_agents_and_agentic_workflows | AI agent]] is a system that interacts with its environment through a cyclical process involving:

1.  **Perception:** Agents sense information from their environment through various modalities like text, images, audio, video, and touch <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Reasoning:** This involves processing perceived information, breaking down tasks into individual steps, utilizing environmental inputs, and determining appropriate tools or actions. This inner planning process is often referred to as "chain of thought" reasoning, powered by LLMs <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Agents can also perform "meta-reasoning" steps, such as "reflection," where they evaluate past actions and adjust their approach if necessary <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  **Action:** Agents perform actions based on their reasoning, which can include talking to humans, moving between locations, or interacting with digital interfaces <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

In essence, [[ai_agents_and_agentic_workflows | AI agents]] interact with the environment through actuations of actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Levels of Autonomy in AI Agents

The deployment complexity and autonomy of [[ai_agents_and_agentic_workflows | AI agents]] can be understood through an analogy with self-driving cars, which also exhibit levels of autonomy <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

*   **Level 1: Chatbot (2017 onwards)**
    *   Primarily focused on retrieving information <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 2: Agent Assist**
    *   An agent generates suggested responses, but a human must approve the final message (e.g., customer service) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Level 3: Agent as a Service**
    *   LLMs automate [[ai_agents_and_agentic_workflows | AI workflows]] for specific tasks (e.g., meeting bookings, writing job descriptions) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Level 4: Autonomous Agents**
    *   An agent can delegate and perform multiple, interrelated tasks that share components, knowledge, and resources <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Level 5: Fully Autonomous (Jarvis-like)**
    *   Agents are fully trusted, delegated with sensitive measures like security keys, and perform actions entirely on behalf of the user <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This level is comparable to a Jarvis-like [[ai_agents_using_humanlike_interfaces_and_workflows | AI agent]] from Iron Man <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

Unlike high-risk applications like self-driving cars where errors can be catastrophic, [[ai_agents_and_agentic_workflows | AI agents]] for general tasks can be segmented into low-risk and high-risk categories <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Low-risk tasks (e.g., filing reimbursements) can initially have human supervision and gradually build trust for automation <a class="yt_timestamp" data-t="00:05:12">[00:05:12]</a>. Customer-facing tasks are generally considered higher risk <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Improving AI Agent Performance

Research focuses on enhancing LLMs for [[building_effective_ai_agents | building effective AI agents]] by improving their reasoning and reflection capabilities, eliciting better behaviors, and learning from past interactions <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Enhancing Reflection and Self-Improvement

LLMs can solve reasoning tasks using methods like:

*   **Few-shot prompting:** Providing examples of similar problems and their answers as context <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Chain of thought:** Instructing the model to "think step by step," allowing it to reason over tokens to reach an answer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

A more advanced technique combines these methods: self-refinement or self-improvement <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This involves:
1.  Asking the LLM to solve a problem step-by-step <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
2.  Prompting the LLM to generate feedback on its initial answer (reflection) <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
3.  Combining the reflection with the original question and answer to prompt the model again, allowing it to update its answer and internal processes <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This process can be iterated until a correct answer is reached <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

#### Challenges with Smaller LLMs

While effective for larger LLMs, this self-improvement process can be problematic for smaller, cost-efficient models (e.g., LLaMA 7B) <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. The feedback generated by smaller models often contains "noise" that can propagate and degrade results, a phenomenon described as "the blind leading the blind" <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Additionally, the internal logic or "demonstrations" of large LLMs may be incompatible with smaller models, rendering their feedback useless <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. Just as one simplifies explanations for a child, feedback for smaller models must be "dumbed down" to match their internal logic <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

#### The `Wiass` Method

To address these challenges, the `Wiass` method proposes helping smaller models acquire self-improvement capabilities by distilling information from larger LLMs <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Instead of smaller models generating their own feedback, a large LLM or external tool (like Python scripts for math tasks) is used to edit and tailor the smaller model's feedback <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This corrected feedback then guides the smaller model's iterative updates <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

By collecting traces of successful trial-and-error processes, these models can be fine-tuned using on-policy data <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This approach has shown significant improvements (up to 48% accuracy after three iterations) in mathematical reasoning problems, outperforming supervised training on static data <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. The key takeaway is that models can learn self-reflection without explicit human supervision by using synthetic data generation <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### Eliciting Stronger Model Behavior (Test-Time Scaling)

While pre-training LLMs is often limited by compute, data size, and parameter size <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>, a promising direction is "test-time scaling" <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This involves taking an existing pre-trained model and giving it more steps or budget during inference to achieve better results <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Examples include instructing the model to "think step by step" or perform reflection <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

#### Tree Search for Sequential Decision-Making

For sequential decision-making tasks (e.g., dialogue), [[ai_agents_using_humanlike_interfaces_and_workflows | AI agents]] need to strategize and plan ahead <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. This is analogous to playing chess, where anticipating opponent moves is crucial <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. Tree search algorithms, like those used in AlphaGo, enable an agent to:
1.  Propose potential moves <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
2.  Simulate outcomes of those moves <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
3.  Evaluate the quality of the outcomes <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
4.  Repeat this process multiple times to find the strongest move <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

In conversational settings, a method called `GPZ0` applies Monte Carlo Tree Search (MCTS) without requiring training data <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. It leverages LLMs to:
*   Search for promising actions (policy) <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   Simulate action outcomes <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
*   Evaluate action quality <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   Simulate opponent behavior (e.g., user responses) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

Unlike closed-loop MCTS, conversational tasks require "open-loop MCTS" to account for the variance in human responses by stochastically sampling possible simulated paths <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. For tasks with clear, objective goals (e.g., persuading someone to donate to charity), `GPZ0` can generate more competitive results without specific training <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Evaluations with LLMs and human studies show that agents using this planning algorithm are more persuasive, natural, and coherent <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. These models also self-discover task information, like the importance of not asking for donations too early <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>, and learn to diversify strategies <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>.

#### Expanding to General AI Agent Tasks

To enable LLMs to perform various [[ai_agents_and_agentic_workflows | AI agent tasks]] beyond conversation, they need to perceive the world visually, processing both images and text <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. Traditional Visual Question Answering (VQA) models are not sufficient for agent tasks that involve computer screenshots and action sequences (e.g., "clear my shopping carts" requires clicking buttons) <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. While humans can achieve 88% success on benchmarks like Visual Web Arena (navigating browsers) and OS World (interacting with a Linux environment), simple LLMs like GPT-4V without planning achieve only 16% <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

The `R MCTS` (Reinforcement Learning Monte Carlo Tree Search) algorithm has been introduced to address this <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. It extends MCTS by incorporating:
1.  **Contrastive Reflection:** Allows agents to learn from past interactions and dynamically improve search efficiency <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. This is achieved through a memory module that caches learned experiences (successes or errors) into a vector database for future retrieval and decision enhancement <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.
2.  **Multi-Agent Debate:** Improves the reliability of state evaluation. Instead of a single LLM prompting for progress, two or more agents debate why an action is good or bad, counterbalancing biases <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

`R MCTS` builds a search tree on the fly, providing reliable state estimates through multi-agent debate and performing contrastive self-reflection at the end of tasks to learn from experience <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. This approach outperforms other search algorithms and non-search methods on benchmarks like Visual Web Arena and OS World, demonstrating improved performance without additional human supervision <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.

### Improving Base LLM with Generated Data (Exploratory Learning)

The knowledge gained through these advanced search and self-improvement processes can be transferred back to train the base LLM <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.

Instead of traditional "imitation learning" (direct training on the best action found in the tree), "exploratory learning" treats the entire tree search process as a single trajectory <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. The model learns how to linearize the search tree traversal, motivating it to learn how to explore, backtrack, and evaluate <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. This teaches the model to improve its decision processes by itself, showing significant gains over imitation learning, especially with constrained test-time budgets <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

## Future Directions and Challenges

The field of [[future_of_ai_agent_ecosystems | AI agent ecosystems]] is rapidly evolving <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. Key areas of ongoing research and development include:

*   **Reducing Reliance on Search Trees:** Developing better reinforcement learning (RL) methods or model predictive control to make the expensive environment setup and interaction more efficient <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
*   **Improved Control and Autonomous Exploration:** Enhancing the agent orchestration layer, as seen in frameworks like ARCollex, which offers features like continuous learning and task decomposition <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.
*   **Interdisciplinary Approaches:** Combining machine learning expertise with systems, human-computer interaction (HCI), and security expertise to advance systems in a deeper, more practical way <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.
*   **Multi-Agent and Multi-User Planning:** Moving beyond single-agent, single-task benchmarks to address challenges in scenarios where multiple humans interact with multiple agents simultaneously on the same computer <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. This introduces complex system-level problems like scheduling, database interaction (to avoid side effects), security (human handover points), and quantifying adversarial settings <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.
*   **Realistic Benchmarks:** Establishing benchmarks that consider not only task completion but also efficiency and security for future applications <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

The development and [[development_and_challenges_of_ai_agents | challenges and benefits of AI agents]] are significant, pushing the boundaries of what LLMs can achieve autonomously <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.