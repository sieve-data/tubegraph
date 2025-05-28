---
title: Reinforcement learning concepts in AI
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

The field of AI agents is rapidly evolving, often drawing upon established concepts from [[reinforcement_learning_techniques | reinforcement learning]] (RL). These agents, primarily [[deep_learning_concepts_and_models | large language models]] (LLMs) with access to tools, operate in a continuous loop to perform tasks <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Current State of Agents

Recent demonstrations of AI agents, such as "Devin," have faced controversy due to suggestions of being faked or highly curated. Issues highlighted include problems not matching stated requirements, non-existent files being edited, and tasks taking significantly longer than depicted <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. This contrasts sharply with advertised capabilities, as current benchmarks show agents struggling:
*   In the OS World benchmark, the best model achieves only a 12% success rate, compared to humans at over 72%, primarily struggling with GUI grounding and operational knowledge <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   The Web Arena benchmark reports an end-to-end success rate of 14% for the best GPT-4 agent, far below human performance of 78% <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.
These figures indicate that agents are "not quite there yet" and are being oversold by startups with vested interests <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>, <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

Despite these limitations, the underlying principles of AI agents are rooted in [[reinforcement_learning_techniques | reinforcement learning]] concepts, particularly the Markov Decision Process (MDP) paradigm <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>, <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

## [[reinforcement_learning_techniques | Reinforcement Learning]] Fundamentals

At its core, [[reinforcement_learning_techniques | reinforcement learning]] is modeled as a Markov Decision Process (MDP) <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. An MDP consists of:
*   **State Space (S)**: The set of all possible configurations of the environment <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>, <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. In chess, this would be the current layout of the board <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.
*   **Observation Space (O)**: In a Partially Observable Markov Decision Process (POMDP), the agent doesn't know the true state (S) but receives an observation (O) that partially informs it about the state <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>, <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Action Space (A)**: The set of all possible actions an agent can take <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Transition Function (T)**: Defines how taking an action in a given state leads to a new state <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>. In a deterministic environment like a computer, this function is deterministic <a class="yt-timestamp" data-t="01:36:10">[01:36:10]</a>.
*   **Reward Function (R)**: Provides feedback to the agent, indicating the desirability of a state-action pair <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>. Rewards are often binary (e.g., 0 for unsuccessful, 1 for successful) <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.

In traditional [[reinforcement_learning_techniques | deep reinforcement learning]], these functions are approximated by deep neural networks, with states and actions often represented as vectors (e.g., joint angles for a robot or one-hot vectors for game buttons) <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.

### Recycling RL for [[deep_learning_concepts_and_models | Large Language Models]]

A key advancement in modern agents is the adaptation of [[reinforcement_learning_techniques | reinforcement learning]] principles for LLMs <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>. The interesting shift is that the state space, observation space, and action space are now often **text-based** <a class="yt-timestamp" data-t="00:37:56">[00:37:56]</a>. This means:
*   Observations from the environment (e.g., a website screenshot) can be turned into a textual description <a class="yt-timestamp" data-t="01:37:43">[01:37:43]</a>.
*   Actions are generated as natural language instructions <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>, providing an "infinite action space" compared to discrete buttons <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.
*   LLMs, acting as function approximators, process text inputs and produce text outputs <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. This allows for a more "fuzzy" representation of states, aligning potentially better with real-world complexities compared to strictly discrete states <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.

This approach gives new life to [[reinforcement_learning_techniques | RL ideas]] that might have seemed "stale" <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

## Key Components and Concepts in LLM Agents

LLM-based agents often incorporate several functional modules, many of which are direct analogues of [[reinforcement_learning_techniques | reinforcement learning]] concepts:

*   **Perception/Observation**: Capturing the current state of the environment, whether through images, raw text, or structured information <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Tools like accessibility features (e.g., XML formats for screen descriptions) can provide rich textual observations to agents <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>, <a class="yt-timestamp" data-t="01:37:46">[01:37:46]</a>.
*   **Memory/Knowledge Bank**: This acts as "cold storage" for past experiences or relevant information. It's used for [[reinforcement_learning_techniques | retrieval augmented generation]] (RAG), where specific pieces of text are pulled from memory to augment the LLM's context for a given task <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:44:40">[00:44:40]</a>.
*   **Thinking/Reasoning**: This involves using multiple auto-regressive steps to generate internal thoughts or context before producing a final answer, similar to human reasoning <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This often involves "Chain of Thought" prompting <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.
*   **Role Playing**: Assigning specific "identities" or system prompts to different LLMs within a multi-agent system, allowing them to embody different roles and behaviors <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Action**: The final output or action taken by the agent, which is then input into the environment <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. In benchmarks like OS World, this involves raw keyboard and mouse control <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Learning/Evaluation**: How the agent improves over time. This includes:
    *   **Reward Models / Q-functions**: A model (often another LLM) that predicts the utility or "goodness" (reward) of a given state or action <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>, <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>. This is analogous to the "critic" in an [[reinforcement_learning_and_selfplay_in_artificial_intelligence | actor-critic framework]], which estimates the value function (Q-value) <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>.
    *   [[qar_and_reinforcement_learning | QAR]]: This concept, often discussed by OpenAI, is interpreted as a [[reinforcement_learning_techniques | Q-function]] based on a language model that evaluates natural language states and actions, potentially using A* search for optimal path planning <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>, <a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>.
    *   **Demonstration Banks**: Databases storing sequences of successful (and sometimes unsuccessful) state-action pairs or trajectories. These can be generated through expert human demonstrations or "auto-curriculum" generation (creating random goals and attempting to achieve them) <a class="yt-timestamp" data-t="00:53:08">[00:53:08]</a>, <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
    *   **In-context Learning**: Improving behavior by providing examples directly in the LLM's input prompt, rather than through traditional gradient-based fine-tuning <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>. This is closely related to RAG.
    *   **Loop Detection/Backtracking**: A mechanism to prevent agents from getting stuck in repetitive error modes by detecting loops in their actions and potentially backtracking <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

## Outlook for [[reinforcement_learning_techniques | Reinforcement Learning]] in AI

While many current agent systems feature "task-specific agent loops" — loops hardcoded for particular tasks like web browsing or research <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a> — the long-term goal is to develop "general agents" or "foundation agents" with agnostic loops that can handle diverse tasks <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. This mirrors the shift seen in [[deep_learning_concepts_and_models | deep learning]] from narrow, task-specific models to broad, general-purpose LLMs <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.

The future of agents might involve:
*   **Increased Context Lengths**: As context windows for LLMs continue to expand (e.g., Gemini 1.5 with 1 million tokens), the need for traditional fine-tuning might diminish. Instead, entire "fine-tuning datasets" could be directly included in the prompt for in-context learning <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. This could simplify development and maintenance, despite potential inference costs <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a>.
*   **End-to-End [[deep_learning_concepts_and_models | Vision-Language Models]] (VLMs)**: Instead of separate models for image captioning and reasoning, a single, more powerful VLM could handle both perception and reasoning end-to-end. This would streamline the pipeline, especially if VLMs also benefit from larger context windows and model sizes <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>.

The pervasive use of [[reinforcement_learning_techniques | reinforcement learning]] concepts, particularly the "reward model" or "Q-function" <a class="yt-timestamp" data-t="01:58:14">[01:58:14]</a>, within these agent loops highlights how fundamental RL remains to advancing AI's capabilities, even as its practical implementation evolves with [[deep_learning_concepts_and_models | large language models]].