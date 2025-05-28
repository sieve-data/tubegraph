---
title: Integration of large language models in interactive agents
videoId: WjLpCgOX7qY
---

From: [[hu-po]] <br/> 

## Introduction
Generative agents are computational entities designed to create believable simulations of human behavior for interactive applications <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This concept involves populating a sandbox environment, similar to *The Sims*, with multiple agents that share news, plan their days, form relationships, and coordinate group activities <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. These agents exhibit emergent individual and social behaviors <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Origin and Scope
The paper "Generative Agents: Interactive Simulacra of Human Behavior" was released in 2023, originating from Stanford and Google <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The research introduces a novel architecture that enables generative agents to remember, retrieve, reflect, and interact with other agents <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Core Components
The success of generative agents requires an approach that can:
*   Retrieve relevant memories and interactions <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   Reflect on those memories and draw higher-level inferences <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Plan reactions and future actions <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

This system moves beyond traditional large language model (LLM) interactions, where an LLM only responds to human prompts, by allowing the LLM to interact in a loop with itself, generating and reflecting on its own prompts, forming an "internal monologue" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Architecture of Generative Agents
The architecture combines [[large_language_models_in_robotics | large language models]] with mechanisms for synthesizing and retrieving relevant information <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. It's built on three main components <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>:

1.  **Memory Stream**: A long-term memory that records all agent experiences in natural language <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This includes observations of behaviors and environmental states <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>.
    *   **Retrieval Model**: Combines recency, importance, and relevance to fetch specific memories <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
        *   **Recency**: Treated as an exponential decay function over the number of sandbox game hours since the memory was last retrieved <a class="yt-timestamp" data-t="00:48:19">[00:48:19]</a>.
        *   **Importance**: Distinguished by assigning a higher score to memories the agent believes to be important (e.g., a breakup vs. eating breakfast) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. The agent rates the "poignancy" of memories on a scale of one to ten <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>.
        *   **Relevance**: Assigned by calculating the cosine similarity between the memory's embedding vector and the query's embedding vector <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. This is analogous to [[large_language_models_and_their_applications | vector databases]] <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>.
        *   The total score is the sum of recency, importance, and relevance scores <a class="yt-timestamp" data-t="00:50:46">[00:50:46]</a>.
2.  **Reflection**: Synthesizes memories into higher-level inferences over time <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. These are abstract thoughts generated periodically, typically two to three times a day <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>. Reflections can also be recursively generated from other reflections <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>.
3.  **Planning**: Allows agents to plan over a longer time horizon to ensure coherent and believable sequences of actions <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. Plans are generated top-down and recursively become more detailed <a class="yt-timestamp" data-t="00:56:39">[00:56:39]</a>. Agents operate in an "action loop" where they perceive the world, store observations, and update their plans <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.

This architecture can be seen as a form of "sense-plan-act" or "observation-planning-reflection" paradigm <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, similar to concepts in [[Impact of Large Language Models on Robotic Capabilities | robotics]] and reinforcement learning <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

## The "Smallville" Sandbox Environment
The study instantiates a small society of 25 agents in a game environment called Smallville, where users can observe and interact with them <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   **Environment Structure**: Smallville features common affordances of a small village, including houses, groceries, a pharmacy, a college, and a bar <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. The world is structured as a tree data structure, representing containment relationships (e.g., a stove in the kitchen) <a class="yt-timestamp" data-t="01:02:06">[01:02:06]</a>.
*   **Agent Representation**: Each agent is represented by a 2D "Sprite" avatar <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a> and has a one-paragraph natural language description defining its identity (e.g., pharmacy shopkeeper) <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>. These descriptions serve as initial memories <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.
*   **Perception**: Agents are not omniscient; their internal "world model" (tree data structure) can get out of date as they leave an area <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>. The sandbox server sends agents and objects within their visual range to their memory <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>.
*   **Action & Movement**: Agents output natural language statements describing their actions, which are translated into concrete movements and displayed as emojis <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. Movement is handled by traditional game pathfinding algorithms; agents simply specify their desired destination <a class="yt-timestamp" data-t="01:04:16">[01:04:16]</a>.

## Agent Interaction and Emergent Behavior
Generative agents communicate in full natural language and are aware of other agents in their local area <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

*   **Human Interaction**: Users can interact with agents by taking on a persona (e.g., a news reporter) <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a> or by adopting the agent's "inner voice" to give direct commands <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. The inhabitants of Smallville treat user-controlled agents no differently than other AI agents, recognizing their presence, initiating interactions, and forming opinions about their behavior <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.
*   **Emergent Social Dynamics**:
    *   Agents form opinions, initiate conversations, and notice each other <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   They can form new relationships <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   If told by a user that she wants to throw a party, an agent will spread the word, and other agents will show up <a class="yt-timestamp" data-t="01:0:15">[01:00:15]</a>. One agent even asked another on a date to the party <a class="yt-timestamp" data-t="00:0:32">[00:00:32]</a>. This behavior is emergent, not pre-programmed <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Agents remember past interactions, such as one agent asking another about her photography project after learning about it earlier <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.
    *   Agents create daily plans that reflect their characteristics and experiences <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, adapting them based on new observations <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.

## Evaluation and Ablation Studies
The believability of agents' behavior was evaluated using a controlled study, where 100 participants judged responses as either human or AI-generated <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>. The study used a "TrueSkill" rating system, a generalization of ELO chess ratings, to measure believability <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>.

Ablation studies were conducted by removing different components of the agent architecture (observation, planning, and reflection) <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>.
*   The full architecture performed best across all interview tasks <a class="yt-timestamp" data-t="01:07:28">[01:07:28]</a>.
*   "No observation" significantly degraded performance, indicating it's the most critical component <a class="yt-timestamp" data-t="01:08:03">[01:08:03]</a>.
*   "No plan" and "no reflection" resulted in only slightly worse performance <a class="yt-timestamp" data-t="01:07:45">[01:07:45]</a>.

## Challenges and Limitations
*   **Computational Cost**: Simulating 25 agents for two days required thousands of dollars in token credit and multiple days to complete, primarily due to the use of GPT-3.5 Turbo for each agent's LLM <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>.
*   **Memory and Coherence**: [[challenges_and_approaches_in_adapting_large_language_models_for_specific_tasks | Challenges with long-term planning and coherence]] remain, necessitating external memory banks because deep learning systems are not inherently good at storing long-term information <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>. The "prompt" context window of LLMs is too small to hold all memories <a class="yt-timestamp" data-t="00:44:14">[00:44:14]</a>.
*   **Hallucination and Errors**: Agents can fabricate embellishments or inherit overly formal speech from the language model <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. They may also fail to retrieve relevant memories or embellish knowledge based on the LLM's world knowledge, leading to incorrect assumptions (e.g., an agent named "Adam Smith" being assumed to be the economist) <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.
*   **Erratic Behaviors**: Occasionally, agents exhibit erratic behaviors, such as entering a closed store, due to "mixed classification of what is considered proper behavior" <a class="yt-timestamp" data-t="01:16:26">[01:16:26]</a>.

## Ethical and Societal Implications
The research raises questions about the nature of consciousness and artificial intelligence:
*   **Simulation Hypothesis**: The creation of believable simulated societies leads to philosophical questions about whether our own reality could be a simulation <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Consciousness**: The emergent behaviors and internal narratives of these agents prompt considerations about whether they possess a form of consciousness or agency <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>, and the ethical implications of "turning off" such a simulated world <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.
*   **Bias**: Generative agents may output behaviors and stereotypes that reflect biases present in their training data <a class="yt-timestamp" data-t="01:20:53">[01:20:53]</a>.
*   **Disclosure**: The paper suggests that generative agents should explicitly disclose their nature as computational entities <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>, though it is acknowledged this may be difficult to enforce in the future <a class="yt-timestamp" data-t="01:21:41">[01:21:41]</a>.

## Future Applications
The integration of [[large_language_models_and_their_applications | large language models and their applications]] into interactive agents has several potential future applications:
*   **[[Large Language Models in Gaming | Gaming]]**: These agents can revolutionize video games by creating dynamic NPCs with believable behaviors, transforming games from linear storylines to open-world MMOs where players can simply "hang out" with AI and friends <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Game engines are likely racing to integrate LLMs deeply <a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a>.
*   **Immersive Environments**: Beyond gaming, these agents can create entire simulated worlds for interactive applications <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Social Prototyping**: Virtual worlds populated by these agents offer accessible test beds for developers and researchers to study social science theories and human behavior <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This allows for controlled experiments on community dynamics, such as observing how information spreads or injecting specific "thoughts" into agents <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.
*   **User Proxies**: Generative agents can serve as proxies for users to develop a deeper understanding of their needs and preferences (e.g., an AI clone watching YouTube videos to recommend content) <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.
*   **Robotics**: Integrating such LLM-powered agents into physical robots like Optimus could lead to the emergence of highly autonomous and interactive systems <a class="yt-timestamp" data-t="01:17:56">[01:17:56]</a>.