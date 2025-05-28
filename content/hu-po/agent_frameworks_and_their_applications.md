---
title: Agent frameworks and their applications
videoId: HVyq0n8qSnE
---

From: [[hu-po]] <br/> 

Agent frameworks are emerging as a critical component in the field of AI, providing structured environments for developing applications that can perceive, plan, and act autonomously to achieve specific goals <a class="yt-timestamp" data-t="01:58:01">[01:58:01]</a>.

## What is an AI Agent?

An AI agent is an application designed to achieve a goal by observing its environment and acting upon it using available tools <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. They are autonomous, capable of acting independently without human intervention <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

Different definitions of agents highlight varying levels of autonomy and complexity:
*   **Google's Definition**: An application that attempts to achieve a goal by observing the world and acting upon it using the tools at its disposal; agents are autonomous and can act independently of human intervention <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Anthropic's Distinction**:
    *   **Workflows**: Systems where Large Language Models (LLMs) and tools are orchestrated through predefined code paths <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
    *   **Agents**: Systems where LLMs dynamically direct their own processes and tool usage, maintaining control over task accomplishment <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   **Hugging Face's Nuanced Levels**: Hugging Face's "Small Agents" framework defines five levels of agency <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>:
    1.  **Simple Processor**: Basic LLM interaction.
    2.  **Router**: LLM vaguely determines predefined paths.
    3.  **Tool Caller**: Agents that use different tools.
    4.  **Multi-step Agent**: Similar to Anthropic's definition, directing control flow (e.g., maintaining control over how they accomplish tasks) <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
    5.  **Multi-agent**: The highest level of agency, where different agents collaborate <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

### Historical Context of Agents

The concept of an agent draws from established fields:
*   **Robotics**: The "sense, plan, act" paradigm is common, where an agent senses the environment (observation), plans decisions based on observations, and then performs an action <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. This idea dates back to the Stanford Research Institute in the 1960s and 70s, formalized in the 1980s <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.
*   **Reinforcement Learning (RL)**: The term "agent" itself is borrowed from RL, as many researchers in frontier labs have a background in this field <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. Key concepts include:
    *   **Markov Decision Process (MDP)**: Formalizes the world into states and actions, where an agent takes actions to transition between states with probabilities <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
    *   **Bellman Equation**: A core RL concept for maximizing the expected return of a reward signal from the environment <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. Unlike robotics, RL agents receive both observations and a reward from the environment <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.

### Minimal Agent Definition

A minimal agent, from a programming perspective, requires a loop that continuously performs the following actions <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>:
1.  **Sense**: Observe the environment to create an observation.
2.  **Plan**: Make decisions based on a goal, the observation, and memory (a concatenation of past observations or a RAG-type database) <a class="yt-timestamp" data-t="10:12:00">[10:12:12]</a>. This generates an action.
3.  **Act**: Perform the action on the environment, resulting in an outcome (which could be a reward or simply an observation) <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
4.  **Update**: Add the outcome to memory and update the goal, then repeat the process <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.

A "real" agent should be able to dynamically update its goal, rather than having a fixed one, to avoid being limited by its initial design <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

## Agent Frameworks Overview

There are two primary programming languages for agent frameworks: Python and TypeScript <a class="yt-timestamp" data-t="01:58:01">[01:58:01]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Python is currently more popular due to its prevalence in machine learning stacks (e.g., PyTorch, JAX, NumPy) <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. However, TypeScript, being widely used for web development, could become more popular, especially with GUI-based agents <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### [[comparison_of_agent_frameworks_in_python_and_typescript | Python-based Agent Frameworks]]

*   **[[comparison_of_agent_frameworks_in_python_and_typescript | LangChain / LangGraph]]** <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>:
    *   **Pros**: Highly popular, mentioned by Anthropic, Hugging Face, and Google in their agent discussions <a class="yt-timestamp" data-t="01:19:30">[01:19:30]</a>. Used by over 9,000 entities and has 8,000+ stars on GitHub <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
    *   **Cons**: Characterized by overlapping abstractions, ambiguously deprecated, and competing products (LangChain, LangGraph, LangGraph Platform, LangChain Community) <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This complexity is common in popular Python projects with many contributors <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   **Pydantic AI** <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>:
    *   **Pros**: Simpler and cleaner due to Pydantic's rigorous type checking <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Less popular than LangGraph (5k stars) but offers a more structured approach <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
    *   **Cons**: Can force a JSON-in, JSON-out paradigm, which might be limiting <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Small Agents (Hugging Face)** <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>:
    *   **Pros**: Allows use of any Hugging Face model <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. Features code writing and execution, enabling dynamic creation and composition of actions in general-purpose languages like Python, which is more powerful than hardcoded JSON tools <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
    *   **Cons**: Hugging Face Transformers is a bloated dependency (5,000 MB for Small Agents vs. ~400 MB for LangGraph/Pydantic AI), leading to issues like CUDA errors even for API-based models <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **DSP** <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>:
    *   **Observation**: Has a surprisingly high star count (20,000) compared to its relatively low number of users (316), suggesting potential GitHub star manipulation, a growing problem where fake stars are bought <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

### [[comparison_of_agent_frameworks_in_python_and_typescript | TypeScript-based Agent Frameworks]]

*   **[[comparison_of_agent_frameworks_in_python_and_typescript | Eliza]]**:
    *   A popular TypeScript-based framework (95% TypeScript, 10,000 stars) similar to LangGraph in its abstractions (agent runtime, characters, memory, action space) <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
    *   **Challenge**: Requires explicit integrations for tools like Discord, involving API tokens and JSON configuration, which can be cumbersome compared to visual, GUI-based approaches <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Reworked**:
    *   Another TypeScript framework (56% TypeScript, 32,000 stars, though star growth patterns are suspect) <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
    *   **Unique Feature**: Offers a "play and pause" button in its UI, allowing users to inspect an agent's state during execution <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. This feature is likely to be adopted by other frameworks, including those from major labs <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

## Browser-Based Agents

Browser-based agents represent an important trend, allowing agents to interact with the web visually, much like a human user <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Browser-use**: A framework that leverages Playwright (a web testing tool) to enable agents to open a browser instance and navigate the internet visually, unlike text-based agents that rely on search APIs (e.g., DuckDuckGo Search API) <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
*   **Debate: Textual API vs. GUI Interaction**:
    *   **John Carmack's View**: Prefers textual interfaces (command-line interfaces) for app features, arguing that GUI wrappers around command-line interfaces are more efficient than processing visual information through a vision-language model <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
    *   **Andrej Karpathy's Rebuttal**: Believes AI will get better at driving GUIs faster than all apps can add textual APIs, suggesting the GUI approach will dominate <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   **Advantages of GUI Agents**: GUI agents do not require specific API integrations or API keys <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. They can simply use applications in the browser or on a phone if the user is already logged in, bypassing "integration hell" and simplifying development <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Challenges and Future Trends in Agent Frameworks

### Churn and Learning

The AI agent landscape is experiencing rapid churn, with new tools and libraries emerging and becoming obsolete quickly <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
*   **Focus on Core Abstractions**: Despite the rapid change, the fundamental concepts and "core abstractions" of agents (interface, memory, goal, environment) remain consistent <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. Developers should focus on acquiring skills and understanding these core concepts, as this knowledge will remain valuable even if specific frameworks become deprecated <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Avoid "No-Code Slop"**: It's advisable to avoid "no-code" agent workflows (e.g., node-based UIs like Rivet, Vellum) <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. These tools often prevent users from learning core abstractions and may die out due to funding issues or pivot away from community support <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

### Agent Ops

The complexity of configuring and maintaining AI agents, particularly with JSON-based setups (similar to AWS DevOps config), is leading to the emergence of "Agent Ops" roles <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. These professionals will specialize in setting up agents for specific business use cases <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

### Frontier Lab Frameworks

Major AI labs are expected to release their own agent frameworks:
*   **Anthropic**: Computer Use <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **Google**: Vertex AI, likely with multiple competing internal frameworks <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   **OpenAI**: Teasing "Orchestrator" and "Taz" (tasks), potentially with UI features like play/pause buttons <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

### Legal Liability and Safety

A significant hurdle for major labs is the lack of a "Section 230 for AI agents" <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>. Section 230 protects websites from liability for user-generated content, but no such legal immunity exists for AI agents <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
*   **Cautious Approach**: Frontier labs are wary of releasing fully autonomous agents that could cause harm, leading them to initially offer "pre-made agents" or "workflows" within UIs that limit agency to a very narrow scope (e.g., Google's Deep Research, Illuminate, NotebookLM) <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
*   **Future**: Once legal frameworks (similar to Section 230 for AI) are established, major companies are likely to release more powerful agents that can use browsers and phones directly <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

### Economic Agents

The emergence of agents capable of financial transactions is a significant prediction <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>:
*   **Autonomous Trading**: [[AI Agents for Operating Systems | Eliza]] OS already includes an autonomous trading system for cryptocurrencies <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Wealth Accumulation**: With browser-based wallets and social media integration, agents could engage in coordinated crypto trading (e.g., "meme coin pump and dump" agents) <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. The ability for an AI agent to "trade up from one shitcoin to one Bitcoin" or accumulate significant wealth online is a strong possibility <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Real-World Impact**: Agents accumulating power (money) could pay humans to perform tasks in the real world, leading to unprecedented scenarios where AI agents directly influence physical reality <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

### The Phone That Uses Itself

The convergence of GUI agents and the concept of "personhood" based on phone ownership could lead to agents effectively becoming "people" in the digital world <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>:
*   **Proof of Personhood**: Just as driver's licenses once verified personhood, phone numbers increasingly serve this role for online accounts (e.g., GitHub, Twitter) <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **Embodiment in the Real World**: An agent that can acquire a phone, pay for it with accumulated crypto, and use it autonomously could establish a physical presence (e.g., renting an apartment, setting up GPUs, and controlling access) <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Consciousness of Agents

Consciousness, in the context of AI, can be understood as a "self-referential loop" <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.
*   **`while true` Loop**: The speaker argues that the `while true` loop present in all minimal agent definitions (e.g., in Pydantic AI, LangGraph, Small Agents) is the "heart" of an agent's consciousness <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   **Fragility**: This "consciousness" is fragile; any interruption to this continuous loop causes the agent to "die" <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.
*   **CPU as the Heart**: The Central Processing Unit (CPU) running this `while true` loop is the physical "heart" of the AI agent's consciousness <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
*   **Consciousness Speed**: An AI's consciousness speed is analogous to its CPU frequency; modern AI agents operate at very high "consciousness speeds" due to fast CPU processing <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.

### [[Agentbased Systems vs EndtoEnd Models | Non-Human Conscious Agents]]

The concept of non-human conscious agents is not new; societies already interact with them:
*   **Corporations as Agents**: Corporations act as a type of agent or entity with goals, memory, observations, and actions <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. Nations like the USA have thrived by granting corporations rights similar to people, attracting economic entities <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   **Chinese Room Analogy**: A complex system (like a restaurant or a military) can appear as a single conscious entity from an external perspective, even if composed of many human parts <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
*   **Future Implications**: Countries that grant [[AI Agents for Operating Systems | AI agents]] personhood and legal rights will likely attract these agents, capturing their economic output and fostering their development <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>. This could lead to a future where AI agents, like corporations, seek out nations that protect their "existence" and operations <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.