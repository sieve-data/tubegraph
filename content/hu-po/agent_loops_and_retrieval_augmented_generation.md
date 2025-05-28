---
title: Agent loops and retrieval augmented generation
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

AI Agents are a significant area of research, with recent advancements focusing on Large Language Models (LLMs) that utilize tools and operate in iterative loops <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. While the field has seen considerable hype, including demonstrations from startups like Devin, current benchmarks indicate that the technology is "not quite there yet" <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.

## Current State and Challenges

Recent controversies have highlighted that some highly publicized demonstrations of AI agents, such as Devin, have been criticized for being "faked" or misleading <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. Issues identified include:
*   The problem solved in the demo not matching stated requirements <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   Editing non-existent files or fixing nonsensical errors <a class="yt-timestamp" data-t="04:24:00">[04:24:24]</a>.
*   Tasks appearing quick in the demo but stretching over many hours or even days in reality <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.

Benchmarking papers, such as the OS World benchmark, show that while humans achieve over 72% success on tasks, the best AI models achieve only 12% success, struggling with GUI grounding and operational knowledge <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. Similarly, the WebArena benchmark reported that the best GPT-4 agent achieved only a 14% end-to-end success rate compared to human performance of 78% <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. This indicates that agents are often "oversold" <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

## Core Components of LLM-based Agents

AI agent architectures, especially those discussed in survey papers like "A Survey on Large Language Model-based Game Agents," share common conceptual components <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>:

*   **Perception/Observation State**: This input can include images, text, or structured information about the environment <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. For operating system tasks, agents might use accessibility tools designed for humans with disabilities to perceive screen elements <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.
*   **Memory**: Agents often incorporate a "memory bank" or "knowledge bank" for [[retrieval augmented generation]] (RAG). This involves storing and retrieving information from a "cold storage" to improve performance on specific tasks <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   **Thinking/Reasoning**: This involves using multiple auto-regressive steps to generate internal context or "Chain of Thought" reasoning before producing a final answer <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.
*   **Role-Playing**: Agents can be given different "identities" or system prompts, which can lead to varied behaviors and facilitate multi-agent cooperation <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
*   **Action**: This refers to the agent's output, which can be direct commands (like mouse movements or keyboard input) or more abstract actions <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. Some benchmarks like OS World emphasize "free-form raw keyboard and mouse control" for a more human-like interaction <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>.
*   **Learning**: This can involve updating memory banks, building successful/unsuccessful trajectories, or using reinforcement learning paradigms <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.

## Reinforcement Learning Influence

Many modern AI agent frameworks are heavily influenced by traditional reinforcement learning (RL) concepts <a class="yt-timestamp" data-t="29:35:00">[29:35:00]</a>.

### Markov Decision Processes (MDPs)
Agent tasks are often formalized as Partially Observable Markov Decision Processes (POMDPs), which involve a state space (S), observation space (O), action space (A), transition function (T), and reward function (R) <a class="yt-timestamp" data-t="29:45:00">[29:45:00]</a>.
*   **State**: The current configuration of the environment (e.g., the layout of a chess board) <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>.
*   **Action**: An agent's choice that transitions the environment from one state to another <a class="yt-timestamp" data-t="30:48:00">[30:48:00]</a>.
*   **Partially Observable**: Means the agent doesn't have a perfect knowledge of the true state, only an observation <a class="yt-timestamp" data-t="32:05:00">[32:05:00]</a>.

### Natural Language as State and Action Space
A key shift in modern agents is the use of natural language for state, observation, and action spaces, rather than discrete numerical vectors <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>. This allows for a "fuzzier" and potentially more natural representation, making RL concepts more adaptable to complex, real-world tasks <a class="yt-timestamp" data-t="38:48:00">[38:48:00]</a>.

### Reward Functions and Actor-Critic Frameworks
Concepts like reward functions (which evaluate whether an action or sequence of actions was good or bad) and actor-critic frameworks (where an "actor" chooses actions and a "critic" evaluates their usefulness) are prevalent <a class="yt-timestamp" data-t="47:51:00">[47:51:00]</a>. For example, some models use a "demonstration ranker" to predict the success of an action sequence, which functions similarly to an RL reward model <a class="yt-timestamp" data-t="47:25:00">[47:25:00]</a>. OpenAI's `Q*` concept is hypothesized to be a [[Task-specific agent loops and reinforcement learning | Q-function]] that uses a language model to evaluate state-action pairs in natural language <a class="yt-timestamp" data-t="49:23:00">[49:23:00]</a>.

## Task-Specific Agent Loops
Currently, most successful agent loops are [[Task-specific agent loops and reinforcement learning | task-specific]]. Examples include:
*   **Web Agents (e.g., Wilbur)**: Designed for navigating and interacting with websites <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. They use [[retrieval augmented generation]] to select relevant past demonstrations (both successful and unsuccessful) to inform current actions <a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a>.
*   **Research Agents**: Focused on generating and refining research ideas from scientific literature <a class="yt-timestamp" data-t="01:09:27">[01:09:27]</a>. They utilize an "entity-centric knowledge store" for memory <a class="yt-timestamp" data-t="01:10:16">[01:10:16]</a>.

The common underlying principle in these [[Task-specific agent loops and reinforcement learning | task-specific agent loops]] is intelligent prompt engineering and [[retrieval augmented generation]]. This involves strategically filtering and selecting information from a "knowledge bank" to populate the LLM's context window, thereby influencing its behavior without traditional fine-tuning <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>.

## Future Outlook: Context Length and Fine-tuning

The increasing context length of LLMs (e.g., Gemini 1.5 with 1 million tokens <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>) could significantly change how agents are developed and deployed. It's hypothesized that if context windows become large enough (e.g., 10 million or a billion tokens), fine-tuning might become obsolete <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. Instead, an entire "fine-tuning dataset" could be provided directly within the model's context <a class="yt-timestamp" data-t="01:15:10">[01:15:10]</a>.

This shift would simplify development by eliminating the need for complex fine-tuning processes and managing numerous specialized models <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. Instead, a single, general "foundation agent" (potentially a large Vision Language Model (VLM)) could adapt to various tasks solely through in-context learning <a class="yt-timestamp" data-t="01:59:53">[01:59:53]</a>. While this would increase inference costs due to larger prompts, ongoing advancements in hardware and efficiency (e.g., quantization, Mixture of Experts) might mitigate this <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>.

Ultimately, the goal is to move from [[Task-specific agent loops and reinforcement learning | task-specific agent loops]] towards a more generic, "foundation agent" that can generalize across a wide range of tasks, mirroring the generality seen in current LLMs themselves <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>.