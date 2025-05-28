---
title: Generative agents and simulation of human behavior
videoId: WjLpCgOX7qY
---

From: [[hu-po]] <br/> 

A recent paper from Stanford and Google introduces "Generative Agents," designed to create believable simulations of human behavior for interactive applications <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This work demonstrates generative agents by populating a sandbox environment, reminiscent of The Sims, with 25 agents <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Core Capabilities and Emergent Behavior

These [[AI agents and automation | agents]] are capable of:
*   Sharing news <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
*   Planning their days <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
*   Forming relationships <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   Coordinating group activities <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

The agents exhibit [[emergent_behaviors_and_community_dynamics_in_ai_villages | emergent social dynamics]], forming new relationships <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. For example, if one agent is told about an upcoming party, that agent will spread the word to their virtual friends, leading to a party spontaneously forming within the simulated world <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>, <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. One agent was even observed asking another on a date to the party <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. These social behaviors are emergent rather than pre-programmed <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>, <a class="yt-timestamp" data-t="00:36:08">[00:36:08]</a>.

## Architecture of Generative Agents

The [[architecture_and_components_of_generative_agents | agent architecture]] is novel, making it possible for generative agents to remember, retrieve, reflect, and interact with other agents <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>, <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. It fuses large language models (LLMs), specifically GPT-3.5 Turbo <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>, with computational interactive agents <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The architecture comprises three main components:

1.  **Memory Stream**: A long-term memory that records agents' experiences in natural language <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Observations are stored as text <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>. A retrieval model combines recency, importance, and relevance to fetch pertinent memories <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
    *   **Recency**: An exponential decay function based on sandbox game hours since the memory was last retrieved <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
    *   **Importance**: Subjectively assigned by the agent's internal LLM on a scale of 1-10, distinguishing mundane events from core memories (e.g., a breakup would yield a high score) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
    *   **Relevance**: Calculated as the cosine similarity between the memory's embedding vector and the query's embedding vector <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>, <a class="yt-timestamp" data-t="00:50:29">[00:50:29]</a>. The total score is the sum of these three components <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

2.  **Reflection**: Synthesizes memories into higher-level inferences over time <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Agents reflect roughly two to three times a day <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>, <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>. Reflections can also be recursive, building upon other reflections <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>.

3.  **Planning**: Generates daily plans and recursively detailed sub-plans for actions <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>. Plans are updated based on new observations and interactions, ensuring dynamic and coherent behavior <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.

Reflections and plans are fed back into the memory stream to influence an agent's future behavior <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This system allows agents to develop an internal narrative about themselves, guiding their actions consistently with their persona <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## The Smallville Sandbox Environment

The simulation takes place in "Smallville," a simple sandbox environment with features like houses, a grocery store, a pharmacy, a college, and a park <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>, <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>. The environment is structured as a tree data structure, where the root node describes the entire world, and child nodes describe areas, rooms, and items <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>, <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. This tree is converted into natural language for the LLMs <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>.

Agents are represented by 2D "Sprite" avatars <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. Each agent has a one-paragraph natural language description of their identity, which serves as their initial memory <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>, <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>. They communicate in full natural language <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. Agents also output natural language statements describing their current actions, which are translated into on-screen emojis <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>, <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>.

Users can interact with Smallville:
*   Users can embody an agent and interact with the inhabitants, who treat the user-controlled agent no differently than other agents <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>, <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>, <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.
*   Users can influence agents by providing "whispered thoughts" (inner voice directives) or by changing the status of objects in the environment <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>, <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>, <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.

Agents are not omniscient; their internal environment map may become outdated as they leave an area, reflecting a more human-like perception <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>, <a class="yt-timestamp" data-t="01:02:38">[01:02:38]</a>, <a class="yt-timestamp" data-t="01:02:45">[01:02:45]</a>.

## Evaluation and Observations

Ablation studies were conducted to assess the importance of each architectural component (observation, planning, reflection). While all components contribute to performance, observation appears to be the most critical <a class="yt-timestamp" data-t="01:08:03">[01:08:03]</a>, <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.

Human evaluators rated the believability of agent responses, using a TrueSkill rating system (a generalization of ELO chess rating) <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>, <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. The full architecture consistently bests all other conditions <a class="yt-timestamp" data-t="01:10:26">[01:10:26]</a>.

Common errors observed in agents included:
*   Failing to retrieve relevant memories <a class="yt-timestamp" data-t="01:22:27">[01:22:27]</a>
*   Fabricating embellishments in their memories <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>
*   Inheriting overly formal speech from the language model <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>
*   Forgetting things, which is very human-like <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>, <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>
*   Erratic behaviors caused by mixed classifications of proper behavior (e.g., agents entering closed stores) <a class="yt-timestamp" data-t="01:16:26">[01:16:26]</a>, <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>

During a two-day simulation, the number of agents aware of a mayoral candidacy increased from 4 to 8, and those knowing about a party increased from 1 to 12. Notably, only 5 out of 12 invited agents showed up to the party, mirroring real-world human behavior <a class="yt-timestamp" data-t="01:14:45">[01:14:45]</a>, <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>, <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.

## [[The potential future and challenges of AI agents | Future Potential]] and [[Ethical considerations and societal impacts of AI simulations | Ethical Considerations]]

The development of generative agents opens doors for various interactive applications, from immersive environments to social computing systems <a class="yt-timestamp" data-t="01:22:54">[01:22:54]</a>. They could serve as believable proxies for users, helping to understand user needs and preferences <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.

However, significant challenges remain, including long-term planning and maintaining coherence <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>. The study also highlights the substantial time and resources required to simulate agents (thousands of dollars in token credit for 25 agents over two days) <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>, <a class="yt-timestamp" data-t="01:20:30">[01:20:30]</a>.

[[Ethical considerations and societal impacts of AI simulations | Ethical concerns]] include the potential for generative agents to output biased behavior reflecting stereotypes present in their training data <a class="yt-timestamp" data-t="01:20:53">[01:20:53]</a>, <a class="yt-timestamp" data-t="01:20:57">[01:20:57]</a>. The discussion also touches upon the question of whether computational entities should explicitly disclose their nature <a class="yt-timestamp" data-t="01:21:10">[01:21:10]</a>, <a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>.
