---
title: Challenges and Solutions in Building AI Agents
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

The field of AI agents has seen rapid development, particularly with the advent of Large Language Models (LLMs). However, despite widespread discussion, a concrete definition of an AI agent remains elusive, and significant [[Challenges in AI agent development | challenges]] persist in their effective implementation <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

## The Core Challenge: Statelessness of LLMs
A fundamental issue in [[building_effective_ai_agents | building effective AI agents]] with modern LLMs stems from the stateless nature of the transformer architecture, which is the "fundamental unit of compute" for current AI <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. Unlike recurrent neural networks, transformers do not inherently retain information across interactions <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

This statelessness leads to several problems:
*   **Lack of Learning from Experience** The most significant deficiency is that current LLM-driven agents cannot truly learn from experience, or their learning is extremely limited <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. Any learning must be managed externally by the user or framework <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Limited Memory:** LLMs only possess memory stored in their weights and what is present in their immediate context window <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
*   **Simple State Management:** Traditionally, state has been handled by merely appending to a list, which becomes highly problematic when trying to build agents for useful, persistent tasks <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
*   **Derailment of Conversations:** Without persistent memory, long conversations with agents like ChatGPT often "derail," forcing the user to manually re-describe context <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
*   **Devastating Errors in Consumer Apps:** The inability to permanently store critical information, such as a user's relationship status, can lead to "devastating errors" in consumer applications <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.
*   **Handling Large Datasets:** Enterprises possess vastly more data than can fit into an LLM's context window (e.g., 10 million tokens), posing a challenge for models to learn from this data <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.
*   **"You Don't Know What You Don't Know":** If information exists outside the LLM's current context window, the agent has no inherent way of knowing it has access to that information <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>.
*   **Tool Overload:** Providing too many tools to an agent can lead to confusion and degraded performance, typically when exceeding 12-15 tools <a class="yt-timestamp" data-t="35:04:00">[35:04:00]</a>.
*   **Reasoning Forgetting:** Some reasoning APIs (like R1) do not persist an agent's extended reasoning chain, meaning the agent "immediately forgets in the next turn" even complex, multi-step thought processes <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>.
*   **Cost and Latency:** Large context windows (e.g., 200k tokens) are expensive and slow, with even 10k tokens causing noticeable delays <a class="yt-timestamp" data-t="58:02:00">[58:02:00]</a>.
*   **Difficulty Testing Tools:** It can be challenging to test if a tool is working correctly without forcing the agent to invoke it <a class="yt-timestamp" data-t="59:36:00">[59:36:00]</a>.
*   **Limitations of Multi-Agent Frameworks:** Existing multi-agent frameworks often lack independent, persistently stateful agents, meaning agents are "trapped inside of a Python file" and cannot be easily moved or reused in other groups <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a>.
*   **Document Editing:** LLMs are generally better at regenerating an entire document from scratch rather than performing line-by-line edits <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.

## Solutions and Approaches

The primary solution revolves around developing "stateful agents" – a concept that existed before the LLM era but has become critically important due to LLMs' stateless nature <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Memory Management Systems
The **MEGPT paper** introduced the idea of a memory management system for LLMs, proposing that AI should manage memory for AI <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This means moving beyond simply appending to a list and towards a more structured approach.

### The Leta Framework Approach
The Leta framework addresses these challenges by implementing a server-client architecture, allowing agents to be stateful and persist indefinitely <a class="yt-timestamp" data-t="22:06:00">[22:06:00]</a>.

Key features and solutions:
*   **API-Backed Agents:** Agents are created and interacted with via an API, similar to chat completions but session-based, removing the need to send entire conversation history with each interaction <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>.
*   **Memory Blocks:** Leta agents use "memory blocks," which are strings with references, allowing the agent to read from and write to its own memory programmatically <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>.
    *   This enables agents to update information dynamically, such as changing a user's relationship status from "boyfriend James" to "ex-boyfriend James" <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
    *   Memory blocks can be shared among multiple agents in a multi-agent system, ensuring consistent information and automatic updates when one agent writes to a shared block <a class="yt-timestamp" data-t="32:12:00">[32:12:00]</a>.
*   **Tiered Memory System:**
    *   **Core Memory:** High-level, top-level information, akin to immediate human recall (e.g., a friend's name, hobbies) <a class="yt-timestamp" data-t="29:56:00">[29:56:00]</a>. Agents can directly append to or replace content in these blocks <a class="yt-timestamp" data-t="31:34:00">[31:34:00]</a>.
    *   **Archival/Recall Memory:** Data sources existing outside the immediate context window (e.g., vector databases), which the agent can "jog its memory" by searching <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.
        *   Recall memory is designed for conversation history, automatically written by default <a class="yt-timestamp" data-t="33:47:00">[33:47:00]</a>.
        *   Archival memory is a general read/write data store of infinite size for arbitrary data, requiring active insertion by the agent <a class="yt-timestamp" data-t="33:59:00">[33:59:00]</a>.
*   **Context Management:** Leta aggressively manages the message buffer and context window, using more intelligent recursive summarization mechanisms <a class="yt-timestamp" data-t="42:40:00">[42:40:00]</a>. It can artificially cap the context window (e.g., to 4K tokens) and evict messages to recall memory, summarizing them to prevent overflow without perceived memory loss <a class="yt-timestamp" data-t="54:40:00">[54:40:00]</a>.
*   **Metadata Statistics:** To address the "you don't know what you don't know" problem, agents are provided with metadata statistics (e.g., number of previous messages, total archival memories) to inform them about available information outside their immediate context <a class="yt-timestamp" data-t="42:08:00">[42:08:00]</a>.
*   **Tool Calling:** Every LLM invocation in Leta is treated as a tool call, even simple responses. This constant tool use allows for greater control and chaining of actions <a class="yt-timestamp" data-t="51:29:00">[51:29:00]</a>.
    *   Agents are required to output a tool and a reasoning snippet (justification) for its use <a class="yt-timestamp" data-t="52:08:00">[52:08:00]</a>.
    *   Agents decide if they "want to keep going" by setting a `request_heartbeat` keyword argument to `true`, preventing indefinite loops unless explicitly desired <a class="yt-timestamp" data-t="52:44:00">[52:44:00]</a>.
*   **Configurability and Observability:**
    *   System prompts are completely configurable <a class="yt-timestamp" data-t="57:50:00">[57:50:00]</a>.
    *   The platform provides a "context simulator" to visualize the full payload being sent to the LLM, offering transparency into the context window's contents, similar to tracing software <a class="yt-timestamp" data-t="58:48:00">[58:48:00]</a>.
*   **Custom Tools and Sandboxing:** Users can write custom Python tools that can even import the Leta client, allowing agents to create and manage other agents or their memories <a class="yt-timestamp" data-t="49:40:00">[49:40:00]</a>. These tools run in sandboxed environments (e.g., E2B) to ensure security <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
*   **Multi-Agent Communication:** Leta supports asynchronous message passing between persistently stateful agents via API calls, enabling more human-like, independent interactions unlike traditional round-robin multi-agent systems <a class="yt-timestamp" data-t="01:03:34">[01:03:34]</a>.
    *   Synchronous options exist for scenarios requiring an immediate reply (e.g., supervisor-worker communication) <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
    *   Agents can be grouped using tags, allowing for broadcast messages to multiple agents <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
    *   Tools can be dynamically added or removed from agents, effectively "detaching" them from communication channels <a class="yt-timestamp" data-t="01:11:37">[01:11:37]</a>.

By addressing the inherent statelessness of LLMs with robust memory management, flexible tool integration, and a server-client architecture, frameworks like Leta aim to overcome key [[technical_challenges_in_ai_agent_development | technical challenges in AI agent development]] and deliver on the promise of human-like, continuously learning AI agents <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.