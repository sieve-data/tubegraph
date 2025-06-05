---
title: Stateful Agents and AI Memory Management
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article explores the concept of [[state_management_and_continuation_in_agent_execution | stateful agents]] and their crucial role in [[memory_management_and_delegation_in_ai | AI memory management]], contrasting them with traditional stateless Large Language Models (LLMs) and discussing practical implementations using the Leta framework.

## Introduction to Stateful Agents
The term "agent" has become widely used, but its definition remains challenging. A more precise term is "[[state_management_and_continuation_in_agent_execution | stateful agent]]" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. While a common definition for an agent in the LLM era is "an LLM taking actions in a loop" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, this definition often overlooks the critical aspect of state updates within that closed loop <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Current AI computational units, like transformers, are inherently stateless machines <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This means a mechanism is required to update their state when the loop closes <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This distinction between stateful and stateless agents has become highly important because LLMs are stateless <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Solving "stapleness" or memory is considered the most important factor for agents to deliver on their hype <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### The Problem of Statelessness
For LLM-driven AI, "stapleness" is synonymous with memory, as LLMs effectively have no memory beyond their weights and context window <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Unlike humans who form new memories and learn over time <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, LLMs do not <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Any learning must be managed externally by the user or framework <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Traditionally, state has been handled by simply appending to a list in process memory <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. While this was acceptable for early workflows, it becomes a significant problem when trying to use agents for useful applications, especially with long-running interactions <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Why Stateful Agents are Necessary
The main problem with current LLM-driven agents is their inability to learn from experience, or their learning is extremely limited <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This is particularly evident when [[developing_ai_agents_for_productivity | building AI agents]] for assistants, companions, or co-pilots <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Consider an example of an AI chatbot:
> Imagine an AI asking a user about their Valentine's Day plans with "James," only to be corrected that James is now an ex-boyfriend <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Without a permanent, rewritable memory store, the AI could make this devastating error repeatedly <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Humans, by contrast, would aggressively write such information to their "core memory" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

[[implementing_ai_agents_in_daily_operations | Implementing AI agents in daily operations]] for enterprise environments also highlights the need for statefulness. Enterprises possess far more data than can fit into an LLM's context window <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. [[state_management_and_continuation_in_agent_execution | Stateful agents]] allow the model to "learn" about the company without retraining weights, instead updating its in-context memory <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

The promise of [[state_management_and_continuation_in_agent_execution | stateful agents]] includes:
*   Preventing conversations from derailing <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   Improving the user experience over time as the AI learns <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Creating human-like memory constructs, leading to more human-like agent behavior with fuzzy memory, forgetfulness, and recall <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## MEGPT: A Memory Management System for LLMs
The concept of [[memory_management_and_delegation_in_ai | memory management and delegation in AI]] is central to the MEGPT paper <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. If LLMs require memory management beyond simple list appending, this management should ideally be performed by another LLM, essentially enabling AI to manage AI memory <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This system is referred to as an "LMOS" (LLM Operating System) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

A key difference from stateless approaches is that a [[state_management_and_continuation_in_agent_execution | stateful agent]] relies on a machine assembling the context window, optimizing the arrangement of information <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This context is drawn from a potentially very large state that cannot fit entirely within the context window <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Leta Framework's Memory Architecture
Leta, an open-source stack built on Fast API, Postgres, and Python, implements a [[memory_management_and_delegation_in_ai | context management system]] for LLMs <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. The core idea is to make the LLM aware of the context problem, allowing it to manage memory using specific tools <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This is centered around tool calling, as LLMs are increasingly proficient at it <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

The [[components_of_ai_agents_router_skills_and_memory | main components of AI agents]]' memory in Leta include:
*   **Memory Blocks**: Strings that hold references, allowing the agent to edit its own memory <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. For example, an agent can update a user's name from "Bob the Builder" to "Charles" and remember past relationships <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. These blocks are stored in a database (Postgres) and have identifiers, enabling sharing among multiple agents in a [[multiagent_systems_in_ai | multiagent system]] <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Core Memory**: High-level information always kept in the context window, akin to immediate human recall (e.g., a friend's name, hobbies) <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
*   **Archival Memory**: Data sources existing *outside* the context window, acting as a general read-write data store (like a vector database of strings) <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. Agents can "jog their memory" by searching this database using tools <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
*   **Recall Memory**: Specifically designed for conversation history, write-protected, and automatically updated with events <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. It mimics a conversation search function.

Leta also provides metadata statistics about what's outside the LLM's context window, addressing the "you can't know what you don't know" problem <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

## [[building_effective_ai_agents | Building effective AI agents]] with Leta
The Leta framework uses a server-client process where agents are intended to be stateful and persist indefinitely <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. The server acts as a centralized source of truth, and users interact with agents via a REST API <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

### Agent Execution Flow
In Leta, every LLM invocation is a tool call <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>. Agents follow a "React-style" pattern with explicit reasoning <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. An agent is expected to output a tool and a justification (reasoning snippet) for its use <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>. Agents can chain tool calls indefinitely, with optional limits set via the API <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. Unlike some frameworks where agents must declare "I'm done," Leta agents must explicitly say "I want to keep going" (via heartbeat requests), making derailment less likely <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.

### Context Window Management
Leta aggressively manages the message buffer <a class="yt-timestamp" data-t="00:42:38">[00:42:38]</a>. Developers can artificially cap the context window length (e.g., to 10k tokens) <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>. If the context exceeds the limit, messages are evicted to recall memory (making them searchable) and a configurable summarizer runs (e.g., truncation or recursive summary) <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

### Tooling and Customization
*   **Default Tools**: MEGPT agents have built-in memory management tools for appending, replacing, and searching core memory, as well as inserting into external databases <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.
*   **Custom Tools**: Python tools can be written and attached to agents <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. Agents can even import the Leta client within a tool, allowing an agent to create or manage other agents and their memory <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>.
*   **Sandboxing**: Tools run within a sandbox (e.g., E2B) by default to prevent interference between agents, especially in multi-tenant environments <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
*   **Tool Limits**: Generally, performance can degrade with more than 12-15 tools, as agents may get confused <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. A potential solution is a "split-thread agent" where memory tools are managed by a separate, subconscious agent <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **Tool Testing**: The Leta UI allows testing tools independently of the agent, rather than relying on the agent to invoke them <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>.

## [[multiagent_systems_in_ai | Multiagent systems in AI]] with Stateful Agents
Unlike traditional [[multiagent_systems_in_ai | multiagent frameworks]] where agents are often trapped in a single Python file and run synchronously, [[state_management_and_continuation_in_agent_execution | stateful agents]] in Leta exist independently as services backed by APIs <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>.

This paradigm enables:
*   **Asynchronous Communication**: Agents can communicate over API channels, much like humans using messaging apps; sending a message doesn't freeze their execution <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.
*   **Synchronous Communication**: For scenarios requiring immediate response (e.g., supervisor-worker interactions), agents can pause execution until a reply is received <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.
*   **Shared State**: Because memory blocks live in a database, information can be shared and updated across multiple agents instantaneously <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.
*   **Dynamic Groups**: Agents can be grouped by tags, allowing messages to be sent to all agents matching a tag (e.g., for map-reduce patterns) <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
*   **Modular Agents**: [[state_management_and_continuation_in_agent_execution | Stateful agents]] can be "taken out" of one [[multiagent_systems_in_ai | multiagent group]] and "attached" to another, retaining their learned experience and skills <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.

The ability to easily connect agents via APIs allows for complex, human-like, or machine-optimized communication patterns <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>.

## Practical Considerations for [[best_practices_for_building_ai_agents | Building AI agents]]
*   **UI/DX**: The Leta UI provides a visual environment for creating and interacting with agents, including a "context simulator" to visualize the full payload sent to the LLM <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>. This is crucial for debugging and understanding agent behavior, especially when working with [[state_management_and_continuation_in_agent_execution | stateful agents]] <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.
*   **Prompt Engineering**: In-context memory tuning (e.g., system prompts, personas) is the primary way to change agent behavior <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.
*   **Learning Curve**: While the workshop environment is set up with Docker for ease of use, manual setup can be prone to package management issues <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>.

## Use Cases and Future Outlook
[[scaling_ai_agents_in_production | Scaling AI agents in production]] benefits greatly from statefulness. Current applications include:
*   **Verticalized Agents**: Specialized agents for specific domains that require retaining information <a class="yt-timestamp" data-t="01:12:55">[01:12:55]</a>.
*   **Enterprise Deployments**: Advanced [[multiagent_systems_in_ai | multiagent systems]] processing large volumes of transactions and learning about users, often without direct chatbot interaction <a class="yt-timestamp" data-t="01:13:17">[01:13:17]</a>.

Unsolved problems in [[memory_management_and_delegation_in_ai | memory management and delegation in AI]] include:
*   **Forgetting**: While archival memory is timestamped for consolidation, an automatic forgetting mechanism is still an area of research <a class="yt-timestamp" data-t="01:14:57">[01:14:57]</a>.
*   **Ingesting Large Data**: Compressing vast amounts of temporal data into a single memory block requires the agent to chain function calls and recursively regenerate the memory block over time <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>.
*   **Active Document Editing**: Agents are generally better at writing entire documents from scratch rather than performing line-by-line diffs, making collaborative human-agent document editing a complex challenge <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.
*   **Coding Agents vs. Tool Calls**: The trade-off between the perceived higher performance of coding agents (which execute code directly) and the complexity of secure execution environments for every tool remains a consideration <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>.Okay, here's the article based on the transcript, formatted for Obsidian and adhering to all rules.

# Stateful Agents and AI Memory Management

This article explores the concept of [[state_management_and_continuation_in_agent_execution | stateful agents]] and their crucial role in [[memory_management_and_delegation_in_ai | AI memory management]], contrasting them with traditional stateless Large Language Models (LLMs) and discussing practical implementations.

## Defining Stateful Agents
The term "agent" has become widely used, but its definition remains challenging <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. A more precise term is "[[state_management_and_continuation_in_agent_execution | stateful agent]]" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. While a common definition for an agent in the LLM era is "an LLM that's taking actions in a loop" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, this definition often overlooks the critical aspect of state updates within that closed loop <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Current AI computational units, like transformers, are inherently stateless machines <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This means a mechanism is required for updating their state when the loop closes <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This distinction between stateful and stateless agents has become highly important because LLMs are stateless and widely used in AI <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Solving "stapleness" or memory is considered the most important factor for agents to deliver on their hype <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### The Challenge of Statelessness
For LLM-driven AI, "stapleness" is synonymous with memory, as LLMs effectively have no memory beyond their weights and context window <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Unlike humans, who form new memories and learn over time <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, LLMs do not <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Any learning must be managed externally by the user or framework <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Traditionally, state has been handled by simply appending to a list in process memory <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. While this was acceptable for early workflows, it becomes a significant problem when trying to use agents for useful applications, especially with long-running interactions <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Why Stateful Agents are Crucial
The main problem with current LLM-driven agents is their inability to learn from experience, or their learning is extremely limited <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This is particularly evident when [[developing_ai_agents_for_productivity | building AI agents]] for assistants, companions, or co-pilots <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Consider an example of an AI chatbot:
> Imagine an AI asking a user about their Valentine's Day plans with "James," only to be corrected that James is now an ex-boyfriend <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Without a permanent, rewritable memory store, the AI could make this devastating error repeatedly, such as asking about "boyfriend James" after a breakup <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This is an error a human would never make, as such information would be aggressively written to "core memory" <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

[[implementing_ai_agents_in_daily_operations | Implementing AI agents in daily operations]] for enterprise environments also highlights the need for statefulness <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Enterprises possess far more data than can fit into an LLM's context window (e.g., 10 million tokens) <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. [[state_management_and_continuation_in_agent_execution | Stateful agents]] allow the model to "learn" about the company without retraining weights, instead updating its in-context memory <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

The promise of [[state_management_and_continuation_in_agent_execution | stateful agents]] includes:
*   Preventing conversations from derailing <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   Improving the user experience over time as the AI learns <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Creating human-like memory constructs, leading to more human-like agent behavior with fuzzy memory, forgetfulness, and recall <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## MEGPT: A Memory Management System for LLMs
The concept of [[memory_management_and_delegation_in_ai | memory management and delegation in AI]] is central to the MEGPT paper <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. If LLMs require memory management beyond simple list appending, this management should ideally be performed by another LLM, essentially enabling AI to manage AI memory <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This system is referred to as an "LMOS" (LLM Operating System) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

A key difference from stateless approaches is that a [[state_management_and_continuation_in_agent_execution | stateful agent]] relies on a machine assembling the context window, optimizing the arrangement of information <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This context is drawn from a potentially very large state that cannot fit entirely within the context window <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Implementing Stateful Agents with Leta
The Leta framework, an open-source stack built on Fast API, Postgres, and Python, implements a [[memory_management_and_delegation_in_ai | context management system]] for LLMs <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a> <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. The core idea is to make the LLM aware of the context problem, allowing it to manage memory using specific tools <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This is centered around tool calling, as LLMs are increasingly proficient at it <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

Leta utilizes a server-client process where agents are intended to be stateful and persist indefinitely <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. The server acts as a centralized source of truth, and users interact with agents via a REST API <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The framework can be run locally using Docker <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

### Leta's Memory Architecture
The [[components_of_ai_agents_router_skills_and_memory | main components of AI agents]]' memory in Leta include:
*   **Memory Blocks**: Strings that hold references, allowing the agent to edit its own memory <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. For example, an agent can update a user's name from "Bob the Builder" to "Charles" <a class="yt-timestamp" data-t="00:43:30">[00:43:30]</a>. These blocks are stored in a database (Postgres) and have identifiers, enabling sharing among multiple agents in a [[multiagent_systems_in_ai | multiagent system]] <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Core Memory**: High-level information always kept in the context window, akin to immediate human recall (e.g., a friend's name, hobbies) <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
*   **Archival Memory**: Data sources existing *outside* the context window, acting as a general read-write data store (like a vector database of strings) <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a> <a class="yt-timestamp" data-t="00:45:54">[00:45:54]</a>. Agents can "jog their memory" by searching this database using tools <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
*   **Recall Memory**: Specifically designed for conversation history, write-protected, and automatically updated with events <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. It mimics a conversation search function.

Leta also provides metadata statistics about what's outside the LLM's context window, addressing the "you can't know what you don't know" problem <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

### Agent Execution and Tooling
In Leta, every LLM invocation is a tool call <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>. Agents follow a "React-style" pattern with explicit reasoning <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. An agent is expected to output a tool and a justification (reasoning snippet) for its use <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>. Agents can chain tool calls indefinitely, with optional limits set via the API <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. Unlike some frameworks where agents must declare "I'm done," Leta agents must explicitly say "I want to keep going" (via heartbeat requests), making derailment less likely <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.

Leta aggressively manages the message buffer <a class="yt-timestamp" data-t="00:42:38">[00:42:38]</a>. Developers can artificially cap the context window length (e.g., to 10k tokens) <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>. If the context exceeds the limit, messages are evicted to recall memory (making them searchable) and a configurable summarizer runs (e.g., truncation or recursive summary) <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

For [[best_practices_for_building_ai_agents | building AI agents]], Leta provides:
*   **Default Tools**: MEGPT agents have built-in memory management tools for appending, replacing, and searching core memory, as well as inserting into external databases <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.
*   **Custom Tools**: Python tools can be written and attached to agents <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. Agents can even import the Leta client within a tool, allowing an agent to create or manage other agents and their memory <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>.
*   **Sandboxing**: Tools run within a sandbox (e.g., E2B) by default to prevent interference between agents, especially in multi-tenant environments <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
*   **Tool Limits**: Generally, performance can degrade with more than 12-15 tools, as agents may get confused <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. A potential solution is a "split-thread agent" where memory tools are managed by a separate, subconscious agent <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **Tool Testing**: The Leta UI allows testing tools independently of the agent, rather than relying on the agent to invoke them <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>.

## [[multiagent_systems_in_ai | Multiagent systems in AI]] with Stateful Agents
Unlike traditional [[multiagent_systems_in_ai | multiagent frameworks]] where agents are often trapped in a single Python file and run synchronously (e.g., Autogen) <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>, [[state_management_and_continuation_in_agent_execution | stateful agents]] in Leta exist independently as services backed by APIs <a class="yt-timestamp" data-t="01:01:12">[01:01:12]</a> <a class="yt-timestamp" data-t="01:01:28">[01:01:28]</a>.

This paradigm enables:
*   **Asynchronous Communication**: Agents can communicate over API channels, much like humans using messaging apps; sending a message doesn't freeze their execution <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.
*   **Synchronous Communication**: For scenarios requiring immediate response (e.g., supervisor-worker interactions), agents can pause execution until a reply is received <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.
*   **Shared State**: Because memory blocks live in a database, information can be shared and updated across multiple agents instantaneously <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.
*   **Dynamic Groups**: Agents can be grouped by tags, allowing messages to be sent to all agents matching a tag (e.g., for map-reduce patterns) <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
*   **Modular Agents**: [[state_management_and_continuation_in_agent_execution | Stateful agents]] can be "taken out" of one [[multiagent_systems_in_ai | multiagent group]] and "attached" to another, retaining their learned experience and skills <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.

The ability to easily connect agents via APIs allows for complex, human-like, or machine-optimized communication patterns <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>.

## Practical Considerations for [[building_effective_ai_agents | Building Effective AI Agents]]
*   **UI/DX**: The Leta UI provides a visual environment for creating and interacting with agents, including a "context simulator" to visualize the full payload sent to the LLM <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>. This is crucial for debugging and understanding agent behavior, especially when working with [[state_management_and_continuation_in_agent_execution | stateful agents]] <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.
*   **Prompt Engineering**: In-context memory tuning (e.g., system prompts, personas) is the primary way to change agent behavior <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

## Use Cases and Future Outlook
[[scaling_ai_agents_in_production | Scaling AI agents in production]] benefits greatly from statefulness. Current applications include:
*   **Verticalized Agents**: Specialized agents for specific domains that require retaining information <a class="yt-timestamp" data-t="01:12:55">[01:12:55]</a>.
*   **Enterprise Deployments**: Advanced [[multiagent_systems_in_ai | multiagent systems]] processing large volumes of transactions and learning about users, often without direct chatbot interaction <a class="yt-timestamp" data-t="01:13:17">[01:13:17]</a>.

Unsolved problems in [[memory_management_and_delegation_in_ai | memory management and delegation in AI]] include:
*   **Forgetting**: While archival memory is timestamped for consolidation, an automatic forgetting mechanism is still an area of research <a class="yt-timestamp" data-t="01:14:57">[01:14:57]</a>.
*   **Ingesting Large Data**: Compressing vast amounts of temporal data into a single memory block requires the agent to chain function calls and recursively regenerate the memory block over time <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>.
*   **Active Document Editing**: Agents are generally better at writing entire documents from scratch rather than performing line-by-line diffs, making collaborative human-agent document editing a complex challenge <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.
*   **Coding Agents vs. Tool Calls**: The trade-off between the perceived higher performance of coding agents (which execute code directly) and the complexity of secure execution environments for every tool remains a consideration <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>.