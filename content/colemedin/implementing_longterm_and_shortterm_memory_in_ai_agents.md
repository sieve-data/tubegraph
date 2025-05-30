---
title: Implementing longterm and shortterm memory in AI agents
videoId: TV8SyEuSMIA
---

From: [[colemedin]] <br/> 

At its core, [[Building AI Agents | building AI agents]] can seem simple when connecting a Large Language Model (LLM) to a few tools, especially with no-code solutions like N8N <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, when tackling more complex problems and [[Building fullscale AI agents | building truly robust AI agents]], the process becomes significantly more challenging <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. A powerful mental model, the "seven node blueprint for [[Understanding AI agents | AI agents]]", helps break down any complex problem involving [[Understanding AI agents | AI agents]] into manageable components <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## [[Understanding AI agents | AI Agents]] as Graphs

The fundamental principle guiding this blueprint is that [[Understanding AI agents | agents]] are essentially graphs under the hood <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This means they involve a cycle where the LLM decides to use a tool, receives feedback, reasons about the outcome, and can then invoke more tools <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This non-deterministic behavior, unlike linear traditional automations, is facilitated by the cyclical nature of graphs <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Thinking of [[Understanding AI agents | agents]] as graphs allows for breaking them down into smaller components, much like Lego bricks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## The Memory Node

The "memory node" is one of the seven categories within this blueprint <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. It is crucial for both [[Setting up and optimizing chat memory for AI agents | long-term memory]] and [[Setting up and optimizing chat memory for AI agents | short-term memory]] retention in [[Understanding AI agents | AI agents]] <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### Short-Term Memory

Short-term memory in [[Understanding AI agents | AI agents]] is typically managed through conversation history <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. In a basic [[Building AI Agents | AI agent]] setup, the core involves an LLM and a tool loop with short-term memory <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This allows the agent to remember recent interactions within a single conversation, enabling it to invoke tools multiple times based on the conversation's progression <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Long-Term Memory

[[Implementing long term memory in AI | Long-term memory]] is typically implemented using vector databases <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. A robust [[Implementing long term memory in AI | long-term memory]] implementation involves:
1.  **Memory Retrieval**: Adding a step at the start of the workflow to retrieve relevant memories from a vector database before the input goes into the LLM. These memories are then fed into the LLM's prompt <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>, <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
2.  **Memory Extraction and Storage**: Including a step at the end of the graph execution to extract relevant memories from the current conversation and store them for future use <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

Libraries like `memzero` are designed for robust [[Implementing long term memory in AI | long-term memory]] management, where the process of adding memories to a vector database is itself structured as a graph <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While typically a vector database is used, a simple example could involve managing [[Implementing long term memory in AI | long-term memories]] in a Google Doc for visual demonstration <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This allows the agent to recall past preferences or information across different conversation sessions <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

### Integrating Memory into Advanced Architectures

In a comprehensive [[Advanced architecture for AI agents | advanced architecture for AI agents]], memory nodes play a vital role alongside other components:
*   **Initial Retrieval**: [[Implementing long term memory in AI | Long-term memory]] is fetched at the very beginning of the process <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.
*   **Primary Agent**: The fetched memory is fed into the primary [[Understanding AI agents | agent]], which also manages its own short-term memory through conversation history <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>, <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.
*   **Memory Saving**: Another [[Implementing long term memory in AI | long-term memory]] node, often using an LLM, extracts key memories or preferences from the conversation to be stored for future interactions <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>, <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.

By understanding how memory nodes fit into the overall "seven node blueprint," developers can systematically determine if an [[Understanding AI agents | agent]] needs [[Implementing long term memory in AI | long-term memory]] and plan its implementation, breaking down a complex [[Building fullscale AI agents | building fullscale AI agents | AI agent]] into simpler, manageable parts <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>, <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This approach makes [[Setting up and optimizing chat memory for AI agents | setting up and optimizing chat memory for AI agents]] a straightforward process within the broader [[Advanced architecture for AI agents | advanced architecture for AI agents]] design.