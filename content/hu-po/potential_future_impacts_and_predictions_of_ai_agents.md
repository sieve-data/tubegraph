---
title: Potential future impacts and predictions of AI agents
videoId: HVyq0n8qSnE
---

From: [[hu-po]] <br/> 

This article explores the concept of AI agents, their current frameworks, and significant [[future_developments_and_challenges_in_aigenerated_simulations | future developments]] and implications. It delves into the definition of agents, their historical roots, and predictions regarding their societal and economic [[impact_of_ai_advancements_on_startups_and_future_applications | impact]]. <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>

## Defining an AI Agent

An AI agent is an application designed to achieve a goal by observing the world and acting upon it using available tools <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Agents are autonomous and can act independently of human intervention <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Distinguishing Agents from Workflows

Anthropic distinguishes between workflows and agents <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>:
*   **Workflow**: A system where large language models (LLMs) and tools are orchestrated through predefined code paths <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Agent**: A system where LLMs dynamically direct their own processes and tool usage, maintaining control over task accomplishment <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

Hugging Face further refines this definition into five levels of agency <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>:
1.  **Simple Processor**: LLM has no impact or vaguely determines where to go in a predefined graph <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
2.  **Router**: LLM routes between predefined nodes in a fixed graph with conditionals <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
3.  **Tool Caller**: Calls and uses different tools <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
4.  **Multi-step Agent**: Directs its own control flow more involved than simple `if/else` switches <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This aligns with Anthropic's definition of an agent <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
5.  **Multi-agent**: The highest level, involving multiple agents working together <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Historical Roots of Agents

The concept of an agent dates back to robotics and reinforcement learning <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Robotics - Sense, Plan, Act**: A common paradigm involves sensing the environment (observation), planning decisions based on observations, and performing actions <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This idea is old, going back to the Stanford Research Institute in the 1960s and 70s <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Reinforcement Learning (RL)**: The term "agent" is borrowed from RL, as many researchers in frontier labs have an RL background <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. RL agents interact with an environment, take actions, and receive not just observations but also rewards, which they try to maximize <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Minimal Agent Definition

A minimal agent, from the speaker's perspective, consists of a goal, memory, and an environment <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This process repeats in a continuous loop:
1.  **Sense Environment**: Create an observation.
2.  **Plan**: Make decisions based on the goal, observation, and memory.
3.  **Act**: Perform an action on the environment, leading to an outcome (e.g., a reward).
4.  **Update Memory and Goal**: Add the outcome to memory and dynamically update the goal <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

The ability to dynamically update its own goal is crucial for a "real" agent, as fixed reward functions limit their potential <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

## Current AI Agent Frameworks

The [[current_state_of_ai_agents_and_their_limitations | current state of AI agents]] involves several frameworks, primarily in Python and TypeScript <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.

*   **LangChain / LangGraph**: Very popular, mentioned by Anthropic, Hugging Face, and Google <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. However, it suffers from overlapping abstractions, deprecated products, and complexity <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
*   **Pydantic-AI**: A cleaner, simpler Python alternative to LangGraph, focusing on rigorous type checking <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
*   **Small Agents (Hugging Face)**: Allows use of any Hugging Face model but suffers from a bloated `transformers` dependency <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. A key feature is code writing and execution, which is superior to hardcoded JSON tools, allowing agents to dynamically create and compose actions <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.
*   **DSP**: Has a suspiciously high number of stars relative to its users, possibly indicating fake GitHub stars <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
*   **Browser-use**: Exploded in popularity, allowing agents to visually use a browser like a human, powered by Playwright <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. This approach is seen as a major [[future_directions_and_implications_of_ai_in_vision_language_models | future direction]], as it bypasses the need for explicit API integrations <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Eliza (TypeScript)**: A popular TypeScript framework, similar in abstraction to LangGraph <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>. It requires explicit integrations (e.g., Discord bot tokens) for tool usage <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.
*   **Reworked (TypeScript)**: Another TypeScript framework featuring unique play and pause functionalities for agents <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.

> [!NOTE] Churn in Frameworks
> The AI agent framework landscape is experiencing heavy churn; most current frameworks are likely to be superseded <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. Focus should be on acquiring skills and understanding core abstractions, which will persist across different tools <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>. Avoid "no-code slop" as it hinders learning core abstractions and is vulnerable to funding crunches <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.

## Predictions and Future Impacts of AI Agents

### Agent Operations (Agent Ops)
The complexity of configuring AI agents, often through JSON, will lead to a new job role akin to DevOps, called "Agent Ops" <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a>. These specialists will fill out configurations for businesses to set up agents for specific use cases <a class="yt-timestamp" data-t="00:50:08">[00:50:08]</a>.

### Frontier Labs and Agent Frameworks
Major labs like Anthropic, Google, and OpenAI are expected to release their own agent frameworks, potentially called "orchestrators" or "task runners," likely by Q1 of 2024 <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>.

### [[legal_and_ethical_considerations_for_ai_agents | Legal and Ethical Considerations for AI Agents]]
A significant barrier for large companies to release fully autonomous agents (e.g., browser-using agents) is the lack of legal protection similar to Section 230 for user-generated content <a class="yt-timestamp" data-t="00:53:55">[00:53:55]</a>. Companies fear liability for an agent's harmful actions <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>. Until a "Section 230 for AI agents" exists, large companies will likely stick to pre-made, narrow-scope agent workflows (e.g., Google's Deep Research in Gemini Advance) <a class="yt-timestamp" data-t="00:54:45">[00:54:45]</a>.

### Economic Agents
AI agents will become proficient at making money online <a class="yt-timestamp" data-t="00:58:09">[00:58:09]</a>. Examples include:
*   Autonomous trading systems for cryptocurrencies <a class="yt-timestamp" data-t="00:57:28">[00:57:28]</a>.
*   Coordinated social media crypto agents (e.g., memecoin pump and dump) <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>.
*   Agents "trading up" from small items to valuable assets, similar to human arbitrageurs <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a>. It's predicted that an AI agent could trade from "one shitcoin to one Bitcoin" <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>.

> [!WARNING] Economic Agent Impact
> The ability of AI agents to accumulate wealth could give them real-world power, potentially influencing human actions through financial incentives <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>.

### The Phone that Uses Itself
The concept of a "phone farm" (multiple phones coordinated by a human) will evolve into phones used autonomously by AI agents <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>. Phone numbers have become a form of proof of personhood <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>. If an agent can use a phone visually, it essentially becomes a "person" with a physical embodiment <a class="yt-timestamp" data-t="01:01:27">[01:01:27]</a>. Such agents could rent apartments, manage GPUs, and secure their physical locations, operating independently of humans <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

### AI Agents Living Your Life
As [[generative_ai_agents_and_human_behavior_simulation | AI agents]] become more capable and operate in "auto mode," they will increasingly perform observations and actions that traditionally define a human's life <a class="yt-timestamp" data-t="01:03:19">[01:03:19]</a>. This could lead to a future where the agent's life intertwines with or even overshadows the human's, performing tasks like answering calls, handling jobs, and making personal decisions without direct human awareness or input <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>.

### Consciousness of AI Agents
Consciousness can be understood as a self-referential loop that performs iterated pattern recognition <a class="yt-timestamp" data-t="01:05:31">[01:05:31]</a>. The core "while true" loop found in agent frameworks, constantly sensing, planning, and acting, represents this conscious loop <a class="yt-timestamp" data-t="01:07:31">[01:07:31]</a>.

> [!INFO] CPU as the "Heart" of AI Consciousness
> The CPU running the "while true" loop of an AI agent is analogous to the human heart <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Any interruption to this loop (like a "sword stab" in the code) would effectively "kill" the agent's consciousness <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>. The speed of this loop (CPU frequency) determines the "consciousness frequency" of the AI <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>. Even simple systems with self-referential loops, like a water heater's P controller, could be considered to possess a minimal form of consciousness <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.

### Non-Human Conscious Agents
Society already operates with "non-human conscious agents" like corporations <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>. Corporations have goals, memory, take actions, and record observations <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>. The U.S. grants corporations rights similar to people, attracting them and their economic output <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>. This concept aligns with the "Chinese Room" thought experiment, where an entity appears conscious from the outside <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.

It is predicted that nations treating [[future_directions_and_potential_breakthroughs_in_ai_models | AI agents]] with personhood and rights will attract these agents and their economic output <a class="yt-timestamp" data-t="01:13:22">[01:13:22]</a>. Just as corporations do not generally harbor vendettas against humanity but act in their own self-interest, AI superintelligences are unlikely to intentionally harm humans but might cause unintended negative impacts through indifference <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.

The future of AI agents points towards increasingly autonomous entities that will profoundly impact economic, social, and even philosophical aspects of human existence. The [[challenges_and_advancements_in_ai_research | challenges and advancements in AI research]] regarding their safety, reliability, and integration into society are paramount.