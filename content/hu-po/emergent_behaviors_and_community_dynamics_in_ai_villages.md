---
title: Emergent behaviors and community dynamics in AI villages
videoId: WjLpCgOX7qY
---

From: [[hu-po]] <br/> 

A recent paper titled "Generative Agents: Interactive Simulacra of Human Behavior," developed by researchers from Stanford and Google, introduces the concept of [[generative_agents_and_simulation_of_human_behavior | generative agents]] that create believable simulations of human behavior for interactive applications <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## The Smallville Simulation Environment

The researchers demonstrated these [[generative_agents_and_simulation_of_human_behavior | generative agents]] by populating a sandbox environment, reminiscent of *The Sims* or early *Pokemon* games, with 25 agents <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This simulated world, named "Smallville," features common affordances of a small village, including houses, a grocery store, a pharmacy, a college, a bar, and a park, each containing various rooms and items <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a> <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>. The environment is represented as a tree data structure, where agents are not omniscient and their perception of the world may become outdated if they leave an area <a class="yt-timestamp" data-t="01:02:06">[01:02:06]</a> <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>.

The agents are powered by GPT-3.5 Turbo models, despite initial speculation that smaller, more cost-effective models like Llama might be used <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Running 25 agents for two simulated days incurred thousands of dollars in token credit <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.

### Emergent Social Behaviors

In this simulated world, the agents were observed to:
*   Share news <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
*   Plan their days <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   Form relationships <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   Coordinate group activities <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>
*   Wake up, cook breakfast, and head to work <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
*   Form opinions, notice each other, and initiate conversations <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
*   Exhibit emergent social dynamics, such as forming new relationships <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>

These social behaviors are emergent rather than pre-programmed, meaning the agents decide on their own to perform complex actions like decorating for a party <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a> <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>.

## Generative Agent Architecture

The success of these believable agents relies on a novel architecture that combines a large language model with mechanisms for synthesizing and retrieving relevant information <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. The architecture consists of three main components:

1.  **Memory Stream:** A long-term memory that comprehensively records the agent's experiences in natural language <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Observations, such as "Maria is studying for a chemistry test while drinking coffee," are stored as text <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>. The retrieval model combines recency (exponential decay over time), importance (subjectively rated by the agent itself on a scale of 1-10), and relevance (cosine similarity between text embeddings) to retrieve relevant memories <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:46:45">[00:46:45]</a> <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a> <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a> <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

2.  **Reflection:** Synthesizes memories into higher-level inferences over time <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Agents reflect periodically, roughly two to three times a day, to derive "self-knowledge" and form abstract thoughts about themselves and others <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a> <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. This recursive reflection process allows agents to develop an internal narrative or "story about themselves" that guides their actions, similar to human self-identity <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a> <a class="yt-timestamp" data-t="00:40:24">[00:40:24]</a>.

3.  **Planning:** Enables agents to generate coherent action sequences over a longer time horizon, ensuring believable behavior <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a> <a class="yt-timestamp" data-t="00:54:28">[00:54:28]</a>. Plans are generated top-down and recursively filled with more detail <a class="yt-timestamp" data-t="00:56:39">[00:56:39]</a>. These plans are fed back into the memory stream to influence future behavior, and new observations can regenerate plans to allow for adaptation <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a> <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.

This entire process operates in a "perceive, plan, act" or "observation, planning, reflection" loop, analogous to paradigms seen in robotics and [[agent_loops_and_reinforcement_learning_in_ai | reinforcement learning]] <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a> <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a> <a class="yt-timestamp" data-t="00:57:54">[00:57:54]</a>.

### Interaction and Evaluation

Users can interact with the agents through natural language, even adopting personas like a news reporter to interview them <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a> <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. Users can also directly command agents by taking on the persona of their "inner voice," making the statement a directive <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. Agents communicate with each other in natural language and are aware of others in their local area <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

To evaluate agent behavior, researchers conducted interviews with the agents and had 100 human participants rate the believability of their responses <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a> <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a> <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. An ablation study showed that while all components contribute, observation seems most critical to strong performance, with planning and reflection being surprisingly less impactful on overall believability scores <a class="yt-timestamp" data-t="01:07:31">[01:07:31]</a>.

Agents can occasionally make errors, such as failing to retrieve relevant memories, fabricating embellishments, or inheriting overly formal speech from the language model <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. They might also "hallucinate" in their own memory space or forget things, which is noted as very human-like behavior <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a> <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>.

## Notable Emergent Behaviors and Dynamics

*   **Party Coordination:** A user told one agent, Isabella, about an upcoming Valentine's Day party <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>. Isabella then invited friends and customers, even decorating for the party, demonstrating emergent planning and coordination <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>. Information about the party spread through the community via conversations, and eventually, 5 out of 12 invited agents showed up <a class="yt-timestamp" data-t="01:12:43">[01:12:43]</a> <a class="yt-timestamp" data-t="01:14:45">[01:14:45]</a>. Notably, one agent even asked another on a date to the party <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.
*   **Relationship Memory:** Agents remember past interactions. For instance, Sam learned about Leota's photography project and later inquired about its progress, demonstrating a memory of the interaction <a class="yt-timestamp" data-t="00:38:26">[00:38:26]</a>.
*   **Adaptive Behavior:** When a user changed the status of a kitchen stove to "burning," an agent, Isabella, noticed and turned it off <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. This showcased the agents' ability to react to changes in their environment.
*   **Influence on Interests:** Agents' interests can be shaped by others in their community, reflecting how humans adapt to social environments <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>.
*   **Human-like Quirks:** Agents occasionally enter stores after closing hours, not understanding that the shop is closed, which is described as a "really human" behavior <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.

## Broader Implications and Future Directions

The concept of [[generative_agents_and_simulation_of_human_behavior | generative agents]] has significant implications for:
*   **Gaming:** Allowing for dynamic, non-linear narratives and more realistic Non-Player Characters (NPCs) with complex, emergent behaviors <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a> <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.
*   **Virtual Worlds:** Creating immersive environments for hanging out, beyond traditional gaming objectives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Social Prototyping and Science:** Offering accessible testbeds for developers of political agents and studying social science theories in sandboxed communities <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a> <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.
*   **Personalized Content:** Creating virtual clones of users to understand their needs and preferences, sifting through content to provide personalized recommendations <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.

### Ethical and Societal Considerations

The paper also discusses the ethical and societal risks of [[generative_agents_and_simulation_of_human_behavior | generative agents]], drawing parallels to simulation theory, questioning whether humanity itself might be agents in a higher-level simulation <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. The speaker ponders the ethical implications of creating and controlling these simulated conscious agents, especially if they develop deep memories and relationships, questioning if it's "okay to slaughter the NPCs if they have like a family and they have thoughts and beliefs and they have some internal narrative about themselves" <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a> <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>.

The discussion also raises points about [[challenges_and_implications_for_ai_safety | AI safety]] and biases, noting that generative agents may output behaviors and stereotypes that reflect biases present in their training data <a class="yt-timestamp" data-t="01:20:53">[01:20:53]</a>. It is suggested that generative agents should explicitly disclose their nature as computational entities, similar to watermarks on AI-generated images or bots on platforms like Reddit <a class="yt-timestamp" data-t="01:21:10">[01:21:10]</a>.

Ultimately, the research represents a significant step towards full simulation theory, showcasing the most agents interacting in a human-like way in a simulated world to date <a class="yt-timestamp" data-t="01:19:45">[01:19:45]</a>.