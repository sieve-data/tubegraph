---
title: Taskspecific agent loops and reinforcement learning
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

The current [[AI and Reinforcement Learning | state of AI]] development highlights a strong connection between advanced language models and concepts derived from [[AI and Reinforcement Learning | reinforcement learning]], particularly in the creation of AI agents <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>. While there is a push towards more general AI, current agent loops often remain task-specific <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>.

## Understanding Agent Loops

An agent, in the context of large language models (LLMs), is essentially an LLM with access to tools that operates in a continuous loop <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>. These agents are designed to perform tasks by perceiving their environment, thinking, accessing memory, performing actions, and learning from their experiences <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>.

### Current Performance and Challenges
Despite initial hype, like with the "Devin" agent which was advertised to solve programming tasks on platforms like Upwork, many demos have been found to be misleading or "faked" <a class="yt-timestamp" data-t="00:46:15">[00:46:15]</a>. This means the agents do not perform as well as claimed <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>. Benchmarking papers confirm this, showing that while humans can accomplish over 72% of tasks, the best models achieve only 12% success in operating system environments (like OS World) <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a> and 14% success in web-based tasks (like Web Arena) <a class="yt-timestamp" data-t="01:35:24">[01:35:24]</a>. This indicates that [[Challenges and Costs in Reinforcement Learning Implementation | agents are not yet "ready to rumble"]] <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.

A significant [[Challenges and Costs in Reinforcement Learning Implementation | challenge]] is inference speed, especially for competitive, real-time games like first-person shooters, where slow response times hinder performance <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. However, for turn-based or communication games, agents can spend more time on inference, reflection, and information retrieval, which improves their success <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

## Reinforcement Learning Integration

The design of modern AI agents heavily recycles concepts from traditional [[AI and Reinforcement Learning | reinforcement learning]] <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>. These concepts are often formalized using a Partially Observable Markov Decision Process (POMDP), which defines:
*   **State Space (S):** The current configuration of the environment <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>.
*   **Observation Space (O):** What the agent can perceive of the state, which may be partial or fuzzy <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Action Space (A):** The set of possible actions the agent can take <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Transition Function (T):** How taking an action in a given state leads to a new state <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.
*   **Reward Function (R):** A measure of how good an action or state is, typically providing a numerical reward (e.g., 0 or 1 for success/failure) <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.

### LLMs as Reinforcement Learning Components
A key innovation in modern agents is replacing traditional deep neural networks (used for approximating functions like transition and reward in RL) with large language models <a class="yt-timestamp" data-t="01:54:45">[01:54:45]</a>. This allows the state, observation, and action spaces to be expressed as natural language (text), adding a "fuzziness" that better reflects real-world complexities compared to discrete, numerical representations <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.

Common subcomponents of agent loops include:
*   **Perception/Observation:** Taking raw input (e.g., images, text) and turning it into a usable state representation <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. For computer tasks, this can involve using accessibility tools that describe screen elements in text (like an XML format) or using vision language models (VLMs) to caption screenshots <a class="yt-timestamp" data-t="02:00:29">[02:00:29]</a>.
*   **Memory/Retrieval Augmented Generation (RAG):** Accessing a "knowledge bank" (memory) to retrieve relevant information, often text-based, to augment the LLM's context <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This includes retrieving both successful and unsuccessful demonstrations to inform the agent's behavior <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>.
*   **Thinking/Reasoning:** Using multiple auto-regressive steps to generate internal context or "Chain of Thought" in natural language, which helps the LLM arrive at a final answer or action <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Role-Playing:** Giving LLMs specific "identities" or system prompts to influence their behavior, enabling multi-agent collaboration with different roles <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Action:** The output of the agent, which can be raw keyboard and mouse control (like moving a mouse pointer or typing) in a virtual machine environment <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. The action space becomes "infinite" in the sense that it's natural language, offering more flexibility than discrete button clicks <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.
*   **Learning/Self-Improvement:** This often involves training a separate "critic" model (like a reward model or demonstration ranker) that evaluates the usefulness of actions or trajectories <a class="yt-timestamp" data-t="00:47:25">[00:47:25]</a>. This critic helps to improve the "actor" (the model choosing actions) <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>. Techniques like "auto curriculum" automatically generate plausible goals to build demonstration banks <a class="yt-timestamp" data-t="00:53:08">[00:53:08]</a>.

### Task-Specific vs. General Agents
Currently, most effective agent loops are [[TaskSpecific vs General AI Models | task-specific]] <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>. For example, the Wilbur agent is designed specifically for web browsing, while others like "Research Agent" are tailored for scientific literature research <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>. This reflects a similar stage to deep learning several years ago, where models were narrow <a class="yt-timestamp" data-t="01:12:34">[01:12:34]</a>.

The ultimate goal for [[Selfimproving AI through reinforcement learning and reasoning | AGI]] is a generic agent loop that can adapt to any task without being explicitly hardcoded <a class="yt-timestamp" data-t="01:11:49">[01:11:49]</a>.

## Future Outlook
There's a hypothesized shift where fine-tuning language models might diminish in importance due to increasingly longer context windows <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. If context lengths become massive (e.g., 10 million or even a billion tokens), an entire "fine-tuning dataset" could potentially be pasted directly into the model's context for "in-context learning," achieving desired behaviors without gradient updates <a class="yt-timestamp" data-t="01:16:03">[01:16:03]</a>. This could drastically simplify the AI pipeline, but would require overcoming [[Challenges and Costs in Reinforcement Learning Implementation | challenges]] related to inference cost and efficiency of processing long contexts <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a>.

The [[Stateoftheart in Reinforcement Learning | development of Vision Language Models (VLMs)]] that can directly perform reasoning from images without an intermediate captioning step is also seen as a crucial step towards more powerful and general agents <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>.