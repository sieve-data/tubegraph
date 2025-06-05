---
title: Letta Framework and MemGPT
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article provides an overview of the Letta Framework and the concepts behind MemGPT, focusing on the development of stateful agents.

## Introduction to Stateful Agents and Memory

The core idea of stateful agents addresses a significant challenge in modern AI: the inherent statelessness of large language models (LLMs). While traditional agents (from the era before LLMs) were generally understood to be stateful, the current wave of AI relies on transformers, which are fundamentally stateless machines <a class="yt-timestamp" data-t="02:50:06">[02:50:06]</a>. This means that when an LLM operates in a closed loop (like an agent taking actions), there must be an external mechanism to update its state <a class="yt-timestamp" data-t="02:56:11">[02:56:11]</a>.

The speaker suggests "stateful agents" as a more precise term for what agents truly meant before the LLM era <a class="yt-timestamp" data-t="02:17:09">[02:17:09]</a>. A common, though incomplete, definition of an agent today is an LLM taking actions in a loop <a class="yt-timestamp" data-t="02:26:08">[02:26:08]</a>. However, this definition often overlooks the crucial aspect of the agent being updated within that closed loop <a class="yt-timestamp" data-t="02:38:09">[02:38:09]</a>.

### Why Stateful Agents Matter

The primary reason for pursuing stateful agents is to enable learning from experience, a capability that current LLM-driven agents lack or have in a very limited way <a class="yt-timestamp" data-t="07:31:09">[07:31:09]</a>. This is especially critical for applications like assistants, companions, and co-pilots <a class="yt-timestamp" data-t="07:44:07">[07:44:07]</a>. Without state, agents can make obvious mistakes, such as forgetting crucial information like a user's relationship status, which a human would never do <a class="yt-timestamp" data-t="08:18:04">[08:18:04]</a>. Such errors are devastating for consumer applications <a class="yt-timestamp" data-t="08:48:07">[08:48:07]</a>.

Statefulness, or [[memory_management_in_ai | memory]], is considered perhaps the most important problem to solve for agents to deliver on their hype <a class="yt-timestamp" data-t="03:22:04">[03:22:04]</a>. It is synonymous with [[memory_management_in_ai | memory]] in the context of LLMs, as LLMs only have memory in their weights and context window <a class="yt-timestamp" data-t="03:39:27">[03:39:27]</a>. Humans are stateful, forming new memories and learning over time, while LLMs do not <a class="yt-timestamp" data-t="03:57:07">[03:57:07]</a>. Any learning with LLMs must be done by the user or the framework <a class="yt-timestamp" data-t="04:02:16">[04:02:16]</a>. Traditionally, this meant simply appending to a list, which is problematic for complex, useful agent applications <a class="yt-timestamp" data-t="04:10:04">[04:10:04]</a>.

For enterprise settings, stateful agents are vital because companies possess far more data than can fit into an LLM's context window (e.g., 10 million tokens) <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. Stateful agents enable a "training phase" where the model learns about the company *after* deployment, not by changing its weights, but by leveraging in-context memory <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.

A common user experience, particularly with [[design_flaws_in_chatgpt | ChatGPT]], involves conversations derailing when they become too long, requiring the user to "mentally context compile" and re-describe everything <a class="yt-timestamp" data-t="10:24:02">[10:24:02]</a>. The promise of stateful agents is to eliminate this derailment, making the AI experience consistently improve over time as the AI learns more about the user <a class="yt-timestamp" data-t="10:50:09">[10:50:09]</a>. By creating human-like memory constructs, agents can exhibit more human-like behavior, including fuzzy memory and recall <a class="yt-timestamp" data-t="11:14:04">[11:14:04]</a>.

## MemGPT: A Memory Management System for LLMs

The concept of MemGPT originated from a paper focused on a [[memory_management_in_ai | memory management]] system for LLMs <a class="yt-timestamp" data-t="05:13:04">[05:13:04]</a>. The core idea is that if LLMs are stateless and require memory management, and if LLMs are continuously improving, then an AI should manage memory for the AI itself <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

### Context Management in MemGPT

MemGPT proposes an "LMOS" (LLM Operating System) approach, which contrasts with typical LLM usage:
*   **Traditional (Stateless)**: A loosely defined context window, not tied to a database, held in process memory, with new information appended over time <a class="yt-timestamp" data-t="05:55:07">[05:55:07]</a>. This often necessitates tracing software and observability to understand the "black box of tokens" shoved into the LLM <a class="yt-timestamp" data-t="06:21:05">[06:21:05]</a>.
*   **MemGPT (Stateful)**: Recognizes that there's an optimal way to arrange an LLM's context window, with context coming from a potentially very large state (much larger than the context window itself) <a class="yt-timestamp" data-t="06:29:08">[06:29:08]</a>. This system aims to automate the "context compilation" that power users of [[design_flaws_in_chatgpt | ChatGPT]] or Claude currently perform manually <a class="yt-timestamp" data-t="06:51:01">[06:51:01]</a>.

## The Letta Framework

Letta is an open-source framework designed to implement stateful agents and memory management, building on the ideas of MemGPT <a class="yt-timestamp" data-t="05:00:05">[05:00:05]</a> <a class="yt-timestamp" data-t="13:48:02">[13:48:02]</a>. It utilizes a client-server architecture (FastAPI, Postgres, and Python logic) to ensure agents persist indefinitely <a class="yt-timestamp" data-t="17:30:08">[17:30:08]</a> <a class="yt-timestamp" data-t="22:06:05">[22:06:05]</a>.

### Core Components and Architecture

*   **Client-Server Model**: Agents are created on the server and are persistent. The client interacts with the agent via a REST API, sending individual messages rather than the entire conversation history <a class="yt-timestamp" data-t="22:06:05">[22:06:05]</a> <a class="yt-timestamp" data-t="23:09:05">[23:09:05]</a>.
*   **Memory Blocks**: The main components of memory in a Letta agent are memory blocks, which are essentially strings with references <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. These blocks are stored in a database (Postgres) and can be edited by the agent itself <a class="yt-timestamp" data-t="23:44:05">[23:44:05]</a> <a class="yt-timestamp" data-t="32:02:00">[32:02:00]</a>.
    *   **Core Memory**: High-level, top-level information that is always in the agent's context window, mimicking immediate human recall (e.g., a friend's name, hobbies) <a class="yt-timestamp" data-t="29:55:07">[29:55:07]</a>. Core memory can be updated (append/replace) <a class="yt-timestamp" data-t="31:32:08">[31:32:08]</a>. It has configurable limits, and if a limit is hit, the agent might receive an error suggesting eviction to archival memory <a class="yt-timestamp" data-t="48:18:04">[48:18:04]</a>.
    *   **Archival Memory**: A general read/write data store that exists outside the context window, effectively a vector database of strings <a class="yt-timestamp" data-t="33:10:09">[33:10:09]</a>. The agent can "jog its memory" by searching this database using a tool <a class="yt-timestamp" data-t="30:37:07">[30:37:07]</a>. This is analogous to "agentic RAG" (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="30:52:09">[30:52:09]</a>. It is not automatically written to; data must be actively inserted <a class="yt-timestamp" data-t="34:01:03">[34:01:03]</a>.
    *   **Recall Memory**: Specifically designed for conversation history, write-protected, and automatically updated every time an event happens <a class="yt-timestamp" data-t="33:47:04">[33:47:04]</a>. It mimics a conversation search function <a class="yt-timestamp" data-t="34:15:08">[34:15:08]</a>.
    *   **Shared Memory Blocks**: Memory blocks can be shared among multiple agents, allowing them to share information and automatically update when one agent writes to a shared block <a class="yt-timestamp" data-t="32:12:00">[32:12:00]</a>.
*   **System Prompt and Tools**: The agent's behavior is influenced by its system prompt and the tools it has access to <a class="yt-timestamp" data-t="29:49:03">[29:49:03]</a>. Letta agents are forced to follow a React-style pattern (Reasoning, Action, Observation) <a class="yt-timestamp" data-t="27:27:03">[27:27:03]</a>.
    *   **Tool Calling**: Every LLM invocation in Letta is a tool call <a class="yt-timestamp" data-t="51:29:00">[51:29:00]</a>. Agents must explicitly call tools, even to send messages <a class="yt-timestamp" data-t="51:39:00">[51:39:00]</a>. This enables agents to run frequently in the background without always needing to output a message to the user <a class="yt-timestamp" data-t="51:44:00">[51:44:00]</a>.
    *   **Tool Execution**: Tools are executed on the server side and are sandboxed by default, supporting environments like E2B <a class="yt-timestamp" data-t="29:17:00">[29:17:00]</a> <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
    *   **Tool Chaining**: Agents can chain multiple tool calls together, and they continue looping until they explicitly decide to stop ("I want to keep going" vs. "I'm done") <a class="yt-timestamp" data-t="43:45:00">[43:45:00]</a> <a class="yt-timestamp" data-t="44:39:00">[44:39:00]</a>.
    *   **Custom Tools**: Developers can write custom Python tools that can even import the Letta client, enabling agents to create or manage other agents and their memory <a class="yt-timestamp" data-t="49:25:00">[49:25:00]</a>.
*   **Context Window Management**: Letta automatically manages the context window by capping its length <a class="yt-timestamp" data-t="25:11:00">[25:11:00]</a>. If the context exceeds the limit, messages are evicted into recall memory and a summarizer runs (configurable as truncation or recursive summary) <a class="yt-timestamp" data-t="54:40:00">[54:40:00]</a>. This ensures agents never send payloads over a set limit, saving cost and time <a class="yt-timestamp" data-t="58:00:00">[58:00:00]</a>.
*   **Metadata Statistics**: To address the "you can't know what you don't know" problem, Letta can provide agents with metadata statistics about information outside their context window (e.g., number of previous messages, total archival memories) <a class="yt-timestamp" data-t="41:54:00">[41:54:00]</a>.

### Multi-Agent Systems in Letta

Letta's approach to multi-agent systems differs from frameworks like Autogen by emphasizing stateful, independently existing agents <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **Asynchronous and Persistent Agents**: Unlike agents trapped in a Python file, Letta agents run asynchronously and persist indefinitely on servers <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>. This allows agents to be "taken out" of one group and attached to another, carrying their experience and memories <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.
*   **API-driven Message Passing**: Multi-agent communication is facilitated through message passing via APIs, similar to humans communicating over Slack <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>.
*   **Multi-Agent Tools**: Letta provides built-in tools for multi-agent communication, including:
    *   **Asynchronous Messaging**: An agent sends a message and immediately receives a receipt, without pausing its own execution, akin to iMessage <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>.
    *   **Synchronous Messaging**: An agent sends a message and waits for a reply, beneficial when a supervisor or critical response is needed <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>.
    *   **Group Messaging**: Agents can send messages to all agents matching specific tags, enabling supervisor-worker or map-reduce patterns <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>.
*   **Dynamic Tool Management**: Agents can have their communication tools dynamically added or removed, effectively controlling their ability to interact with other agents <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>.

## Practical Implementation and Workflow

Letta provides a workshop experience to demonstrate its capabilities:
*   **Setup**: Requires Docker for the server, which is an open-source stack (FastAPI, Postgres, Python) exposing a robust API <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a> <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. The client interacts via Python SDK or REST API <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.
*   **Jupyter Notebooks**: Used to lay out basic ideas behind the context management system, focusing on an LLM being aware of its context window and managing memory with tools <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.
*   **Web UI (AD)**: An interactive application (app.leta.com) that serves as a "new iteration of the playground" for stateful agents <a class="yt-timestamp" data-t="01:12:45">[01:12:45]</a>. It allows for faster iteration in a low-code environment compared to SDKs <a class="yt-timestamp" data-t="56:07:00">[56:07:00]</a>.
    *   **Context Simulator**: A feature within the UI that allows developers to visualize the full payload being sent to the LLM, including system instructions, tool descriptions, external summary metadata, and messages <a class="yt-timestamp" data-t="58:48:00">[58:48:00]</a>. This helps in understanding and debugging what the agent "sees" in its context window <a class="yt-timestamp" data-t="59:08:00">[59:08:00]</a>.
    *   **Tool Testing**: The UI enables testing tools separate from the agent, which is challenging in a notebook environment <a class="yt-timestamp" data-t="59:45:00">[59:45:00]</a>.
*   **Prompt Engineering**: Tuning in-context memory is the primary way to change agent behavior <a class="yt-timestamp" data-t="43:04:00">[43:04:00]</a>.
*   **[[finetuning_language_models_with_mcp | Finetuning Language Models with MCP]]**: While not explicitly detailed as "MCP," the framework aims for agents to "learn" about companies by processing data into their in-context memory, suggesting a form of continual learning post-training <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.

## Challenges and Considerations

*   **Tool Overload**: Agents can become confused if too many tools are added (e.g., more than 12-15 tools can degrade performance) <a class="yt-timestamp" data-t="35:04:00">[35:04:00]</a> <a class="yt-timestamp" data-t="53:02:00">[53:02:00]</a>. A solution involves having a dedicated "shadow agent" or "subconscious" that handles memory tools, keeping the main agent's toolset lean <a class="yt-timestamp" data-t="35:09:00">[35:09:00]</a>.
*   **"Doesn't Know What It Doesn't Know"**: If information is only in archival memory, the agent might not know to search for it without explicit prompting or pre-defined tool rules <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a> <a class="yt-timestamp" data-t="46:40:00">[46:40:00]</a>.
*   **External Database Integration**: Currently, Letta primarily supports Postgres due to schema changes and migration scripts, though SQL light is technically supported for local use <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.
*   **Forgetting**: While archival memory is tagged with timestamps, there's no inherent "forgetting" mechanism; consolidation needs to be actively managed by the agent <a class="yt-timestamp" data-t="01:14:57">[01:14:57]</a>.
*   **Secure Execution Environment**: Running tools in a [[microvms_in_ai_sandboxes | sandbox]] (like E2B) is crucial for security, especially in multi-tenant environments, but can introduce latency <a class="yt-timestamp" data-t="01:18:56">[01:18:56]</a>.
*   **Active Document Editing**: LLMs are often better at rewriting entire documents than making precise line-by-line diffs, posing a challenge for collaborative or iterative document agents <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.

## Use Cases

Letta is designed for deploying stateful, LLM-based services <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>.
*   **Verticalized Agents**: Companies building specialized agents for specific domains require memory and state <a class="yt-timestamp" data-t="01:12:55">[01:12:55]</a>.
*   **Enterprise Deployments**: Advanced multi-agent systems can run stable workflows, processing transactions and learning about users without direct messages (i.e., not chatbots) <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>.