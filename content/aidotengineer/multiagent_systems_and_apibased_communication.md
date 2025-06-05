---
title: MultiAgent Systems and APIBased Communication
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article explores the concept of [[ai_agents_and_agentic_workflows | AI agents]], focusing on the critical need for "stateful agents" and how API-based communication enables effective [[multiagent_systems_in_ai | multiagent systems in AI]]. The content is derived from a workshop that introduced foundational ideas for [[building_effective_agents | building effective agents]], particularly those with robust memory capabilities.

## The Challenge of Stateless LLMs in AI Agents

While a common definition for an [[ai_agents_and_agentic_workflows | AI agent]] is "an LM that's taking actions in a loop" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, this definition misses a crucial component: the agent must be updated within that closed loop <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The fundamental unit of compute in the current wave of AI, the transformer, is inherently stateless <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This means a mechanism is required for updating the agent's state when the loop closes <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This distinction between stateless and stateful agents has become particularly important because Large Language Models (LLMs) are stateless <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Why Stateful Agents?

Stapleness, or statefulness, is synonymous with memory in the context of LLMs <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. LLMs effectively have no memory beyond their weights and context window <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Unlike humans who form new memories and learn over time <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, LLMs do not. Any learning must be handled by the user or the agent framework <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Traditionally, state handling in [[ai_agents_and_agentic_workflows | AI agents]] has been limited to appending to a list <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This approach is insufficient for [[ai_agents_beyond_chatbots | AI agents beyond chatbots]] that perform useful, complex tasks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The inability to learn from experience is a major limitation of current agents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. For example, an agent that fails to update its memory after being informed of a user's breakup can lead to "devastating error[s]" in consumer applications <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

Stateful agents promise:
*   **Learning from experience:** Essential for assistants, companions, and copilots <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Handling large enterprise data:** Enterprises often have more data than can fit into an LLM's context window <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Stateful agents enable learning from this data, effectively like a post-training phase that updates in-context memory <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Enhanced user experience:** Eliminating conversational derailment where users have to repeatedly re-describe context to the LLM <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. The experience should get progressively better as the AI learns more about the user <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Human-like behavior:** [[building_effective_agents | Building effective agents]] with human-like memory constructs (fuzzy memory, forgetfulness, recall) leads to more natural agent behavior <a class="yt-timestamp" data-t="01:11:17">[01:11:17]</a>.

## LMOS: A Memory Management System for LLMs

To address the statelessness of LLMs, a "memory management system for LLMs" (LMOS) is proposed, based on the MEGPD paper <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The core idea is that if LLMs need memory management, and they are becoming increasingly capable, then this management should be performed by another LLM – the AI managing the memory for the AI <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

In this system, an LLM is made aware of its context problem and is given tools to manage memory <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This approach is centered around [[integration_of_tool_calling_in_agent_frameworks | tool calling]], as LLMs are continually improving at this task <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>.

### Memory Tiers in Stateful Agents

The Leta framework implements a multi-tiered memory system:
1.  **Core Memory:** Top-level, in-context memory, akin to immediate human recall (e.g., a friend's name, hobbies) <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. These are strings with references, editable by the agent itself <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
2.  **Archival/Recall Memory:** Data sources that exist outside the context window, similar to long-term memory that requires conscious effort to retrieve (e.g., searching old photos) <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
    *   **Recall Memory** is effectively conversation history that is write-protected but automatically updated with events <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.
    *   **Archival Memory** is a general read/write data store, akin to an infinite-sized vector database of strings, where agents can actively store and retrieve arbitrary data, such as large documents <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

Agents can "jog their memory" by using tools to search these external data sources <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>, a concept similar to [[ai_agents_and_agentic_workflows | agentic workflows]] based on Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>.

### Context Window Management

The system actively manages the context window, allowing developers to artificially cap its length (e.g., to 4K tokens) <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>. If the context exceeds this limit, messages are evicted into recall memory and a summarizer runs to keep the in-context payload within bounds <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>. This prevents payloads from growing excessively large, which can lead to high costs and slow response times <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

### Tooling and Agent Behavior

[[integration_of_tool_calling_in_agent_frameworks | Integration of tool calling in agent frameworks]] is central. Agents are given tools to manage their memory, including:
*   Appending to memory blocks <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
*   Replacing content in memory blocks <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.
*   Searching memory (specific conversations or general RAG queries) <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.
*   Inserting into external databases <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.

The framework supports [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]] by allowing tool execution on the server side <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. Tools can be sandboxed, and agents can be extremely "meta," importing the client itself to create or manage other agents and their memory <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>.

Agents in this paradigm generally follow a "React-style" pattern of reasoning, action, and observation <a class="yt-timestamp" data-t="00:44:11">[00:44:11]</a>. Unlike traditional React agents that loop until they explicitly state they are done, Leta agents must explicitly state they "want to keep going" (via "heartbeat requests"), which is considered more practical for preventing derailment <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>.

## API-Based Communication for Multi-Agent Systems

A key benefit of stateful agents running on servers and being accessible via APIs is the simplicity of [[multitagent_collaborations_and_communication | multi-agent collaborations and communication]] <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>. Unlike many existing [[multiagent_systems_in_ai | multiagent systems in AI]] (e.g., Autogen) where agents are often trapped within a single Python file and don't exist independently <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>, API-backed stateful agents can communicate via simple message passing <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>.

This mirrors human interaction in a remote company, where individuals communicate asynchronously but maintain their own state and experience <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>. The lack of stapleness in traditional multi-agent frameworks means losing the benefit of taking an "expert" agent from one group and placing it into another <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a>.

Multi-agent communication patterns include:
*   **Asynchronous Messaging:** An agent sends a message and receives a receipt without pausing its own execution, similar to a human sending an instant message <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>.
*   **Synchronous Messaging:** An agent sends a message and waits for a reply, beneficial when the agent needs to freeze execution (e.g., waiting for supervisor input) <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
*   **Group Communication:** Agents can be grouped by tags, allowing messages to be sent to all agents matching specific criteria, supporting "supervisor-worker" concepts and parallelized tasks <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.

These [[multitagent_collaborations_and_communication | multitagent collaborations and communication]] tools are implemented by having agents import the client and send messages to other agents via API calls <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>. The ability to remove or add tools dynamically also allows for runtime control over agent communication permissions <a class="yt-timestamp" data-t="01:11:37">[01:11:37]</a>.

## Conclusion and Future Outlook

The [[future_of_mcp_in_agentbased_systems | future of mCP in Agentbased Systems]] (Memory, Compute, and Persistence) strongly points towards stateful agents and API-based communication. This enables the development of human-like [[ai_agents_and_agentic_workflows | AI agents]] capable of learning from experience and adapting to diverse enterprise and consumer use cases <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This general platform supports deploying any stateful, LLM-based service <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>.

While challenges remain (e.g., optimizing tool performance, human-agent collaboration on active documents, automated memory forgetting), the foundational shift towards stateful agents and robust API-driven [[multiagent_orchestration_in_ai_copilot_systems | multiagent orchestration in AI copilot systems]] provides a powerful paradigm for the next generation of AI applications.