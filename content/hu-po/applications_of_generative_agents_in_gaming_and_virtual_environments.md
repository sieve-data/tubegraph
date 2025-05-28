---
title: Applications of generative agents in gaming and virtual environments
videoId: WjLpCgOX7qY
---

From: [[hu-po]] <br/> 

Generative agents are computational agents designed to simulate believable human behavior in interactive applications <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This technology, explored in a recent paper from Stanford and Google, aims to create interactive simulacra of human behavior <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>.

## Core Concepts and Simulation
The paper demonstrates [[generative_ai_agents_and_human_behavior_simulation | generative agents]] by populating a sandbox environment, reminiscent of *The Sims* or early *Pokémon* games, with 25 agents <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a> <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>. These agents, powered by large language models (LLMs) like GPT-3.5 Turbo <a class="yt-timestamp" data-t="01:43:38">[01:43:38]</a>, are not pre-programmed with specific social behaviors <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>. Instead, they exhibit emergent behaviors such as:
*   Sharing news <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>
*   Planning their days <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>
*   Forming relationships <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>
*   Coordinating group activities <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>
*   Initiating conversations <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>

For example, if one agent is told they are having a party, they will autonomously spread the word to their virtual friends, leading to an emergent party in the simulated world <a class="yt-timestamp" data-t="01:10:15">[01:10:15]</a>.

## Impact on Gaming and Virtual Worlds
This technology holds significant promise for the [[Large Language Models in Gaming | gaming industry]] and the emergence of new virtual worlds <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a> <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Future games could evolve beyond linear storylines with fixed starts and ends, becoming more like Massively Multiplayer Online (MMO) worlds where users primarily "hang out" with AI agents and other players <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. These generative agents are seen as "proto versions" of such interactive environments <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. The speaker anticipates that within the next two years, game engines like Unity, Unreal Engine, Roblox, and Godot will integrate LLMs deeply, enabling NPCs to have LLMs inside their "heads" <a class="yt-timestamp" data-t="01:00:13">[01:00:13]</a>.

## Agent Architecture
The architecture of these generative agents combines LLMs with specific mechanisms to create believable behavior <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a> <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. The core components are:

### Memory Stream
This acts as a long-term memory, recording a comprehensive list of the agent's experiences in natural language <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a> <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Every perception, such as "desk is Idle" or "refrigerator is Idle," is stored with a timestamp <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

### Retrieval Model
This component combines three factors to retrieve relevant memories:
*   **Recency**: Memories that are more recent are given higher weight, using an exponential decay function based on the number of sandbox game hours <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Importance**: The agent itself assigns an importance score (1-10) to memories, distinguishing "mundane" events (like eating breakfast) from "core" memories (like a breakup) <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
*   **Relevance**: This is calculated using cosine similarity between the embedding vectors of memory objects and the current query, allowing the LLM to search within embedding spaces for related information <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. This system allows for [[interactive_pointbased_manipulation_using_GANs | vector databases]] to serve as external memory banks for LLMs <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

### Reflection
Reflections synthesize memories into higher-level inferences over time <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. Agents periodically ruminate on their experiences (e.g., two to three times a day), forming self-narratives and abstract thoughts <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a> <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. This internal monologue, hidden from the user, creates richer interactions <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. Reflections can also be recursive, building upon previous reflections <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

### Planning
Agents create daily plans that reflect their characteristics and experiences <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. These plans start top-down (e.g., "wake up and complete the morning") and recursively generate more detailed actions <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. Plans can also be updated based on new observations, making agents adaptable <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

The entire system operates in a "perceive, plan, act" or "observation, planning, reflection" loop, where the environment provides state information to the memory stream, influencing retrieval, planning, and reflection, which then feed back into the memory <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a> <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. This fusion of LLMs with computational interactive agents is a key aspect of their design <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

## Smallville: A Simulated Society
The generative agents were instantiated in a simple sandbox environment called Smallville <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Environment Structure**: Smallville features common elements of a small village, including houses, a grocery store, a pharmacy, a college, a bar, and a park <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. This environment is structured as a tree data structure, representing containment relationships (e.g., "a stove in the kitchen") <a class="yt-timestamp" data-t="01:02:06">[01:02:06]</a>.
*   **Agent Representation**: Each agent is represented by a 2D "Sprite" avatar and given a one-paragraph natural language description defining their identity and initial relationships <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a> <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Interaction**: Agents communicate in full natural language and are aware of others in their local area <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. Users can interact with the agents by adopting specific personas (e.g., a "news reporter") or by directly issuing commands by taking on the agent's "inner voice" <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Users can also reshape the environment by changing object statuses (e.g., turning a stove from "on" to "burning"), which agents will notice and react to <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Emergent Behaviors in Smallville
The two-day simulation demonstrated complex emergent behaviors:
*   **Information Diffusion**: A party organized by one agent (Isabella) spread through the community via natural language conversations <a class="yt-timestamp" data-t="01:12:40">[01:12:40]</a>.
*   **Relationship Formation**: Agents formed new relationships, with one even asking another on a date to the party <a class="yt-timestamp" data-t="01:13:32">[01:13:32]</a> <a class="yt-timestamp" data-t="01:13:44">[01:13:44]</a>.
*   **Persistent Memory**: Agents remembered past interactions and used them to inform future conversations (e.g., remembering a photography project discussed earlier) <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.
*   **Autonomous Actions**: An agent attending a party arrived early to decorate, an emergent behavior not explicitly programmed <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **Human-like Flaws**: Agents sometimes failed to retrieve relevant memories, fabricated embellishments, or inherited overly formal speech <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. They could also "forget" things or exhibit "erratic behaviors" such as entering closed stores <a class="yt-timestamp" data-t="01:11:26">[01:11:26]</a> <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.

## Ethical and Societal Implications
The project raises profound questions about simulation theory and the nature of consciousness <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a> <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Simulated Consciousness**: The creation of agents with internal monologues, memories, and evolving narratives prompts questions about whether "turning off" such a simulation is ethical, especially if agents develop deep relationships and "beliefs" about themselves <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
*   **User Manipulation**: The ability for users to act as an "omniscient God" or an "inner voice" in the simulated world, injecting ideas or commands, parallels philosophical questions about human existence <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a> <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
*   **Societal Experimentation**: These simulated environments could serve as "test beds" for social science theories, allowing researchers to study community dynamics, information spread, or even the development of pathological behaviors by injecting specific thoughts into agents <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a> <a class="yt-timestamp" data-t="01:15:23">[01:15:23]</a>.
*   **Bias and Stereotypes**: A significant concern is that [[future_developments_and_challenges_in_aigenerated_simulations | generative agents]] may output behaviors and stereotypes that reflect biases present in their training data <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a> <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Transparency**: The ethical debate extends to whether [[generative_ai_agents_and_human_behavior_simulation | generative agents]] should explicitly disclose their nature as computational entities, similar to watermarks on AI-generated images or bot labels on social media <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Future Outlook
Despite challenges like computational cost (simulating 25 agents for two days cost thousands of dollars in token credits <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>) and ensuring long-term planning coherence, the potential of [[generative_ai_agents_and_human_behavior_simulation | generative agents]] is vast <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a> <a class="yt-timestamp" data-t="01:22:52">[01:22:52]</a>. They could play roles in design tools, social computing systems, and immersive environments <a class="yt-timestamp" data-t="01:22:54">[01:22:54]</a>. The concept of creating "virtual clones" of users to understand their needs and preferences (e.g., an LLM watching YouTube to recommend videos for a human user) is an intriguing application <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>. Continued advancements in LLMs, like GPT-5 or GPT-6, are expected to further expand the expressivity and capabilities of these agents <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.