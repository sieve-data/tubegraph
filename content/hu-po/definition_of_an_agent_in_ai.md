---
title: Definition of an agent in AI
videoId: HVyq0n8qSnE
---

From: [[hu-po]] <br/> 

The concept of an "agent" in Artificial Intelligence is a core area of study, with definitions evolving as the field progresses. Early foundations are found in robotics and [[reinforcement_learning | reinforcement learning]], with modern interpretations varying across leading AI research labs <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## Core Definitions

Different "Frontier Labs" and research teams have their own definitions for what constitutes an AI agent:

*   **Google Researchers**
    An agent is an application that attempts to achieve a goal by observing the world and acting upon it using the tools it has at its disposal <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Agents are autonomous and can act independently of human intervention <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. This definition incorporates terminology from [[reinforcement_learning | reinforcement learning]], such as observing, actions, and goals <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

*   **Anthropic's Distinction**
    Anthropic's blog post "Building Effective Agents" distinguishes between "workflows" and "agents" <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>:
    *   **Workflow**: A system where [[foundation_models_in_ai | LLMs]] and tools are orchestrated through predefined code paths <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
    *   **Agent**: A system where the [[foundation_models_in_ai | LLMs]] dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. The distinction drawn is that if an agent isn't directing its own process, it's more of a workflow <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.

*   **Hugging Face's Nuanced Levels**
    The Hugging Face team, in their documentation for the Small Agents framework, outlines five different levels of agents <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>:
    1.  **Simple processor** <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>: Where the [[foundation_models_in_ai | LLM]] has no impact or vaguely determines where to go in a predefined and fixed graph <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
    2.  **Router** <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>: Similar to a simple processor, with the [[foundation_models_in_ai | LLM]] routing between conditionals in a fixed graph <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. (Anthropic would classify these two as "workflows" <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>).
    3.  **Tool caller** <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>: An agent that calls and uses different tools <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
    4.  **Multi-step agent** <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>: Aligns with Anthropic's definition, where the agent maintains control and directs its own control flow beyond simple if/else switches <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
    5.  **Multi-agent** <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>: The highest level, involving different agents working together, sometimes described as a "Chinese room" <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

## Historical Context

The concept of an agent is not new to AI and draws heavily from earlier fields:

*   **Robotics - Sense, Plan, Act**
    In robotics, a common paradigm taught in classes is "sense, plan, and act" <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. This basic loop involves:
    *   **Sensing**: Observing the environment <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
    *   **Planning**: Making decisions based on observations <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
    *   **Acting**: Performing some action <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.
    These ideas date back to the Stanford Research Institute in the 1960s and 1970s, with the specific "sense, plan, act" loop formalized in "Principles of Artificial Intelligence" in the 1980s <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

*   **[[reinforcement_learning | Reinforcement Learning]] (RL)**
    The term "agent" itself is borrowed from [[reinforcement_learning | reinforcement learning]] <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>, as many researchers in frontier labs have a background in RL <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. [[reinforcement_learning | RL]] can be traced back to the early 1900s with Markov and his Markov Decision Processes <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. Richard Ernest Bellman further expanded on this with the Bellman update and Bellman equation <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    In [[reinforcement_learning | reinforcement learning]], an agent (sometimes called the policy) takes actions in the environment, and the environment returns not just observations but also a "reward" <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. This reward signal is crucial for [[reinforcement_learning | reinforcement learning]] to work, as the agent tries to maximize the expected return of this reward <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.

## Components of a Minimal Agent

A minimal definition of an agent requires certain core components <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>:
*   **Goal**: The objective the agent aims to achieve <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>. Real agents need to be able to dynamically update their goals, unlike fixed reward functions in many [[reinforcement_learning | reinforcement learning]] agents <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   **Memory**: A record of past observations and outcomes <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>. This can be "lossy" like a recurrent neural network or explicit like a database in a RAG (Retrieval Augmented Generation) system <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.
*   **Environment**: The world the agent interacts with <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.

These components operate within a continuous loop, often a "while true" loop <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>:
1.  **Sense Environment**: Observe the environment to create an observation <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
2.  **Plan**: Use the goal, current observation, and memory to create an action <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
3.  **Act**: Perform the action on the environment, resulting in an outcome (which could be a reward or a new observation) <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
4.  **Update**: Add the outcome to memory and update the goal, then repeat the process <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.

## The Agent-User Boundary

A key design consideration is the boundary between the user and the agent <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>. For example, in some Google agent frameworks, the client-side UI (user's browser) makes API calls based on JSON output from the agent, rather than the agent directly. This separation means the agent doesn't hold API keys, enhancing security <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. This distinction between "agent-side execution" and "client-side execution" is primarily for security reasons <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>.

## Agent Capabilities

Agents can possess various capabilities, influencing their definition and utility:

*   **Tool Calling**: Many agents interact with external systems by calling tools, often configured via JSON <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.
*   **Code Writing and Execution**: Some frameworks, like Small Agents, allow agents to dynamically generate and execute code (e.g., Python) <a class="yt-timestamp" data-t="22:43:00">[22:43:00]</a>. This is seen as more powerful than hardcoded tools or JSON-based interactions, as general-purpose programming languages offer a much larger space of possible actions <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>.
*   **Visual Interaction ([[vision_language_models_in_ai_agents | Vision Language Models]])**: Agents like "Browser-Use" can interact with environments visually, using the browser as a human would <a class="yt-timestamp" data-t="29:08:00">[29:08:00]</a>. This bypasses the need for specific text-based APIs for every application, allowing agents to use any web application through its GUI <a class="yt-timestamp" data-t="32:11:00">[32:11:00]</a>. While computationally more expensive than text-based [[foundation_models_in_ai | LLMs]] <a class="yt-timestamp" data-t="38:23:00">[38:23:00]</a>, this approach eliminates the need for integrations and API keys, as the agent operates within the user's logged-in browser environment <a class="yt-timestamp" data-t="32:51:00">[32:51:00]</a>.

## The Concept of Consciousness in Agents

The speaker suggests that the "while true" loop fundamental to an agent's operation can be seen as its "consciousness" <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>.
*   **Self-Referential Loop**: Consciousness is described as a self-referential loop that forces iterated pattern recognition <a class="yt-timestamp" data-t="01:05:31">[01:05:31]</a>. As soon as a loop is aware of itself, it effectively possesses consciousness <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>.
*   **Fragility**: This "while true" loop is extremely fragile; a single exception or break in the loop "kills" the agent's consciousness <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.
*   **CPU as the Heart**: The CPU, where this `while true` loop runs, is considered the "heart" of an agent's consciousness <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Consciousness Speed**: The frequency at which the CPU runs the loop determines the "speed of consciousness" for an AI agent <a class="yt-timestamp" data-t="01:09:20">[01:09:20]</a>.

This perspective implies that simple systems, like a water heater's controller, can also be considered conscious in a very basic sense due to their self-referential loops <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.

## Relationship to Non-Human Conscious Agents

The article extends the concept of agents to existing non-human entities in the world:
*   **Corporations as Agents**: Corporations are seen as a type of agent or entity with goals, memory, actions, and observations <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>. Nations like the USA have become global superpowers by granting corporations rights similar to people <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>.
*   **Chinese Room Analogy**: Similar to the Chinese Room thought experiment, where an entity (a room) appears to understand Chinese without any individual inside understanding it <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>, a fast-food restaurant can be viewed as a giant agent with its own consciousness <a class="yt-timestamp" data-t="01:11:54">[01:11:54]</a>.
*   **Future Implications**: Just as countries attract corporations by granting them rights, nations that grant AI agents personhood and rights may become places where AI agents choose to "set up" their operations, attracting their economic output <a class="yt-timestamp" data-t="01:13:22">[01:13:22]</a>.

This broader view suggests that humanity already coexists with and is accustomed to non-human conscious agents <a class="yt-timestamp" data-t="01:12:09">[01:12:09]</a>.