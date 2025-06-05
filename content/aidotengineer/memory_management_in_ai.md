---
title: Memory Management in AI
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

Memory management is a critical aspect of artificial intelligence, particularly with the widespread adoption of large language models (LLMs). The term "agent memory" or "LMOS" (LLM Operating System) is often used to describe systems that enable AI agents to retain and utilize information over time, much like humans do <a class="yt-timestamp" data-t="01:39:54">[01:39:54]</a>.

## Stateless vs. Stateful Agents

Traditionally, an AI agent could be defined as an LLM taking actions in a loop <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. However, this definition often overlooks a crucial component: the updating of the agent's state within a closed loop <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Modern LLMs, such as transformers, are inherently stateless machines <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This means that after each interaction, a mechanism is required to update their state <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

Prior to the LLM era, the distinction between stateful and non-stateful agents was less emphasized <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. With the current reliance on stateless LLMs for AI, it has become a critical differentiation <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. Memory, or "stapleness," is considered paramount for agents to deliver on their potential <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.

### Limitations of Current AI Implementation

Current methods for handling state in LLM-driven AI often involve simply appending to a list held in process memory <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. While this sufficed for early workflows and experimental use cases, it becomes a significant [[challenges_with_current_ai_implementation | problem]] when agents are used for practical, useful applications <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

A major challenge is that current agents cannot effectively learn from experience, or their learning is extremely limited <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. This becomes particularly evident in applications like chatbots, assistants, companions, and co-pilots <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. For example, an AI might repeatedly ask about an ex-partner if it lacks a robust memory management system to update relationship status <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. Such errors are "devastating" for consumer applications <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

For power users of LLMs, [[prompt_decomposition_in_ai_evaluations | context compilation]] is often a manual process <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>. Conversations that go on for too long can "derail," forcing users to re-describe everything to the LLM, a "painful experience" <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

## The MEGPT Paper and LMOS

The concept of a "Memory Management System for LLMs" or "LMOS" proposes that if LLMs are to continuously improve, the memory management should be handled by another LLM, rather than a human <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. The MEGPT paper (Multi-Agent GPT) explored this idea, suggesting that AI should perform memory management for AI <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

## Stateful AI Agents with Leta

The Leta framework is designed around the concept of [[stateful_ai_agents | stateful AI Agents]] that persist indefinitely, using a server-client process where the server acts as a centralized source of truth <a class="yt-timestamp" data-t="02:08:00">[02:08:08]</a>. Leta aims to automate the compilation of context for LLMs <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.

### Key Concepts in Leta's Memory Management:

*   **Memory Blocks**: The fundamental units of memory in a Leta agent are "memory blocks," which are essentially strings with references <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. These blocks are stored in a database (e.g., Postgres) <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
*   **Three Tiers of Memory**:
    *   **Core Memory**: High-level, frequently accessed information that is always in the context window <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This is analogous to immediately recalling a friend's name and hobbies upon seeing them <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Agents can edit their own core memory, rewriting information based on new experiences <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
    *   **Archival Memory**: A general read/write data store outside the context window, similar to a vector database <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. Agents can "jog their memory" by searching this database <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This is useful for large documents or structured data <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
    *   **Recall Memory**: Specifically designed for prior messages and conversation history, also residing outside the context window <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. It's automatically written to upon events and provides a conversation search function <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Context Window Management**: Leta allows artificial capping of the context window length (e.g., 4K tokens) <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. If the limit is reached, messages are evicted to recall memory, and a configurable summarizer runs to maintain the context within limits <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. This prevents excessive payload sizes, which can lead to slow responses and high costs <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   **Tool Calling**: All LLM invocations in Leta are tool calls, even for simple messages <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. Agents are required to output a tool and a justification (reasoning snippet) <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Leta executes tools on the server side, and tools are sandboxed by default, supporting MicroVMs <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
    *   **Tool Chaining**: Agents can chain tool calls indefinitely, allowing for complex multi-step operations <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. This is managed by "heartbeat requests," where the agent explicitly requests to continue execution <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
    *   **Custom Tools**: Developers can write custom tools in Python, allowing agents to perform arbitrary actions, including creating other agents or managing their memory <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Context Simulator**: A feature in the UI allows developers to visualize the full payload being sent to the LLM, including system instructions, tool descriptions, external summary metadata, and messages <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>. This helps with debugging and understanding [[efficiency_and_smart_execution_in_ai_systems | context compilation]].

## Benefits of Stateful Agents

[[Stateful AI Agents | Stateful agents]] offer several advantages:
*   **Learning from Experience**: They can form new memories and learn over time, addressing a fundamental deficiency of stateless LLMs <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Human-like Interaction**: The behavior of stateful agents becomes more human-like, mimicking fuzzy memory and recall, leading to better user experiences <a class="yt-timestamp" data-t="11:17:00">[01:17:17]</a>.
*   **Improved User Experience**: True statefulness means conversations shouldn't derail; the AI experience should continuously improve as the agent learns more about the user <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
*   **Enterprise Data Handling**: For enterprises with vast amounts of data exceeding typical context window limits, stateful agents allow models to "learn" about the company by incrementally storing information in in-context memory, akin to a post-training phase <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. This helps avoid [[mismanagement_of_ai_resources | common pitfalls in AI strategy]].
*   **Persistent and Shareable Memory**: Memory blocks live in a database and can be shared among multiple agents within an organization, allowing for collaborative knowledge <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

## Multi-Agent Systems with Stateful Agents

Traditional multi-agent frameworks often involve agents trapped within a single file, running synchronously and losing their state upon termination <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>. This contrasts with how humans operate in a multi-agent setting, asynchronously and statefully <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.

With [[stateful_ai_agents | stateful agents]] running on servers and accessible via APIs, multi-agent systems become a matter of message passing <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>. Agents can be "wired" to each other over APIs, similar to how humans communicate using tools like Slack <a class="yt-timestamp" data-t="01:02:38">[01:02:38]</a>. This allows for:
*   **Asynchronous Messaging**: Agents can send messages and immediately return to their own tasks, receiving receipts, analogous to human iMessage interactions <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.
*   **Synchronous Messaging**: For critical interactions (e.g., contacting a supervisor), an agent's execution can be frozen until a reply is received <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.
*   **Group Messaging**: Agents can be grouped by tags, allowing a message to be sent to all agents matching specific criteria, useful for supervisor-worker patterns or parallelized tasks <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
*   **Flexible System Design**: Stateful agents enable [[dynamic_planning_for_complex_tasks_in_ai | dynamic planning for complex tasks]] and allow for the creation of specialized agents that can be integrated into different multi-agent groups <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.

### Practical Implementation

Leta provides a Docker image for easy setup <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. The framework is built on Fast API, Postgres, and Python logic <a class="yt-timestamp" data-t="01:17:32">[01:17:32]</a>. It exposes a robust API for interacting with agents <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>. Developers can use the Python SDK or TypeScript SDK (programmatically generated from the REST API) <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

For local development, Docker is recommended due to frequent schema changes that affect database migrations <a class="yt-timestamp" data-t="01:14:32">[01:14:32]</a>. The system supports external Postgres databases <a class="yt-timestamp" data-t="01:14:38">[01:14:38]</a>. Tools are executed within a sandbox, such as E2B, ensuring secure and isolated environments, especially important for multi-tenant cloud deployments <a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a>. While there is a latency trade-off with cold starts, this approach provides a robust solution <a class="yt-timestamp" data-t="01:19:13">[01:19:13]</a>.

The architecture often leverages [[graph_data_structures_in_ai_and_its_benefits | graph data structures in AI and its benefits]] by allowing agents to operate as fully connected graphs initially, with restrictions (tool rules) applied to enforce specific behaviors <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. This contrasts with frameworks that start with predefined decision trees.

Leta also integrates with external tool providers like Composio <a class="yt-timestamp" data-t="01:00:42">[01:00:42]</a>.

The development environment allows for both programmatic interaction via notebooks and a low-code UI builder, which offers a visual representation of agent behavior and memory management <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This visual tool serves as an "iteration" of the traditional playground, aiming to be the standard experience for stateful agents <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>.