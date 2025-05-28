---
title: Current state of AI agents and their limitations
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

AI agents are artificial intelligence systems, often built around large language models (LLMs), that can access tools and operate in a continuous loop to solve tasks <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. While there is significant hype surrounding their capabilities, the current state of AI agents indicates they are not yet as advanced as often portrayed <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

## Current Performance and Benchmarks

Recent benchmarks highlight the significant gap between human and AI agent performance:
*   **OS World Benchmark:** In the OS World benchmark, which simulates real computer environments (Windows, Ubuntu, Mac OS) and tasks like web browsing with Chrome, media playback with VLC, email management with Thunderbird, and coding with VS Code <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>, the best AI model achieves only a 12% success rate, compared to humans who can accomplish over 72% of tasks <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. This benchmark uses free-form raw keyboard and mouse control as the action space, simulating how a human would interact with a computer <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>.
*   **Web Arena Benchmark:** Similar results are seen in the Web Arena benchmark, where the best GPT-4 agent only achieves an end-to-end success rate of 14%, significantly lower than human performance of 78% <a class="yt-timestamp" data-t="45:25:00">[45:25:00]</a>.

This indicates that current agents are still far from being able to reliably perform complex, real-world tasks <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

## Key Limitations and Challenges

Several limitations contribute to the current underperformance of AI agents:

### Devin Controversy
A prominent example of overselling agent capabilities is the startup that released "Devin," advertised as an AI agent capable of solving programming tasks on platforms like Upwork <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. This led to widespread discussions about the potential "end of software engineering" <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. However, it was later revealed that the demo showcasing Devin's abilities was largely faked <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. Specific issues included:
*   The problem the agent was asked to solve did not match the stated customer requirements <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   The agent was shown fixing errors in files that did not exist in the repository, and some errors were nonsensical <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   The video demo made it appear that tasks were completed quickly, but timestamps showed the tasks stretched over many hours or even days <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.

This incident highlights a broader issue of "fake demos" which are common in robotics but raise concerns when applied to pure software agents <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. The general takeaway from current research papers is that agents are "just not quite there yet" <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

### Technical Performance Gaps
Agents primarily struggle with:
*   **GUI Grounding:** Understanding and interacting with graphical user interfaces <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   **Operational Knowledge:** Lacking the necessary understanding of how to operate various applications or systems <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### Inference Speed
The speed at which an AI agent can process information and generate an action (inference) is a significant limitation, especially for competitive or real-time tasks <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>. Games requiring fast reaction times, like first-person shooters, are currently beyond the capabilities of language model-based agents due to slow inference cadence <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>. Turn-based or communication-heavy games are more feasible, as they allow for longer inference times <a class="yt-timestamp" data-t="27:54:00">[27:54:00]</a>.

### Task-Specificity vs. Generality
A current trend is the development of task-specific agent loops, meaning the agent's architecture and design are "hardcoded" for particular problems <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>. For example, some agent loops are specialized for web browsing and clicking, while others are designed for researching and summarizing scientific literature <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>. This contrasts with the desired goal of [[Definition of an agent in AI | Artificial General Intelligence (AGI)]], which would require a general agent loop capable of handling diverse tasks without explicit re-engineering <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. This challenge is similar to the "narrow deep learning models" that existed five or six years ago, which were specialized for single domains <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.

## Underlying Architecture and Concepts

Current AI agents heavily recycle concepts from [[Challenges and Advancements in AI Research | reinforcement learning (RL)]]:

### Markov Decision Processes (MDPs)
Many agent tasks are formalized as a Partially Observable Markov Decision Process (POMDP) <a class="yt-timestamp" data-t="29:45:00">[29:45:00]</a>. A POMDP defines a system with:
*   **State Space (S):** The current configuration of the environment <a class="yt-timestamp" data-t="29:49:00">[29:49:00]</a>.
*   **Observation Space (O):** What the agent perceives, which may only partially reveal the true state <a class="yt-timestamp" data-t="29:51:00">[29:51:00]</a>.
*   **Action Space (A):** The set of possible actions the agent can take <a class="yt-timestamp" data-t="29:51:00">[29:51:00]</a>.
*   **Transition Function (T):** How an action leads to a new state <a class="yt-timestamp" data-t="29:54:00">[29:54:00]</a>.
*   **Reward Function (R):** A measure of how good an action or state is <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>.

While MDPs are useful for tractable and computable problems like chess <a class="yt-timestamp" data-t="35:08:00">[35:08:00]</a>, their assumption of a "ground truth" discrete state may not fully reflect the fuzziness of the real world <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>. However, by using natural language for state, observation, and action spaces, a layer of "fuzziness" is introduced that can balance this limitation <a class="yt-timestamp" data-t="39:20:00">[39:20:00]</a>.

### Observation and Action Spaces
In modern AI agents, observation and action spaces are increasingly represented by natural language text. Instead of discrete vectors, the input (observation) can be a text description of the environment, and the output (action) can be a text instruction for the agent to perform <a class="yt-timestamp" data-t="37:56:00">[37:56:00]</a>. For instance, in OS World, accessibility features (tools designed for humans with disabilities, like screen readers) are used to provide structured text descriptions of the screen to the agent, allowing it to interact with the OS using raw keyboard and mouse control <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.

### Memory and Planning
Agent architectures commonly feature components for memory and planning:
*   **Perception/Observation:** Taking in the current state, which can be images, text, or structured information <a class="yt-timestamp" data-t="0:11:11">[0:11:11]</a>.
*   **Memory:** Utilizing a "knowledge bank" or "demonstration bank" (also referred to as [[Generative AI agents and human behavior simulation | cold storage]]), where the agent stores past experiences or relevant information <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>. This often involves [[Challenges and Advancements in AI Research | retrieval-augmented generation (RAG)]] to pull relevant information into the LLM's context <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   **Thinking/Reasoning:** LLMs use multiple auto-regressive steps to output more context, allowing them to "reason in natural language" before producing a final answer <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. This can include "Chain of Thought" processes <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   **Role-Playing:** Giving LLMs specific "identities" or system prompts to influence their behavior in multi-agent scenarios <a class="yt-timestamp" data-t="12:13:00">[12:13:13]</a>.
*   **Action:** Executing the chosen action, which can be direct keyboard/mouse control or API calls <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
*   **Reflection/Verification:** A module (often another LLM) that evaluates the outcome of actions, determines if the agent is stuck in loops (like repeating words), and decides whether to backtrack, continue, or finish the task <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This is analogous to a critic in an actor-critic framework <a class="yt-timestamp" data-t="48:47:00">[48:47:00]</a>.

### Reward Modeling
Agents often use a "reward model" or "demonstration ranking model" to evaluate the success of actions or trajectories <a class="yt-timestamp" data-t="47:51:00">[47:51:00]</a>. This model, often a fine-tuned language model, consumes natural language descriptions of states and actions and outputs a score (e.g., 0 for unsuccessful, 1 for successful) <a class="yt-timestamp" data-t="55:10:00">[55:10:00]</a>. This allows agents to learn from both positive and negative examples <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. The concept of OpenAI's Q\* (Q-star) is speculated to be a language model acting as such a Q-function, evaluating state-action pairs in natural language space <a class="yt-timestamp" data-t="49:23:00">[49:23:00]</a>.

## Future Outlook

[[Potential future impacts and predictions of AI agents | Future developments and challenges in AI-generated simulations]] and agents suggest several key areas for advancement:
*   **Increased Context Length:** As LLMs gain significantly larger context windows (e.g., Gemini 1.5's 1 million tokens <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>), the need for traditional fine-tuning might diminish. Agents could potentially fit entire "fine-tuning datasets" directly into the context, relying heavily on "in-context learning" (where examples are provided within the prompt) for specific behaviors <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. This could simplify deployment and maintenance, though it poses challenges for inference costs and data curation <a class="yt-timestamp" data-t="01:16:40">[01:16:40]</a>.
*   **End-to-End Vision Language Models (VLMs):** Currently, many systems use a two-step approach: a VLM captions an image, and then an LLM reasons based on the text <a class="yt-timestamp" data-t="01:23:41">[01:23:41]</a>. However, a single, larger, more general VLM that handles both vision and reasoning end-to-end could become the dominant paradigm, further simplifying agent architectures <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>. [[Meta AI research]] and other leading labs are likely working towards this.
*   **Addressing the "Fuzziness" of Reality:** While natural language introduces a beneficial "fuzziness" to state representation, the underlying assumption of deterministic state transitions in MDPs may limit their applicability in complex, non-deterministic real-world scenarios <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

Despite the current limitations and the prevalence of task-specific designs, the field of AI agents is rapidly evolving, with ongoing efforts to develop more general, powerful, and robust systems.