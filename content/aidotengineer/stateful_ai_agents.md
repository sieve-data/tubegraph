---
title: Stateful AI Agents
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

[[Stateful AI Agents | Stateful agents]] are a conceptualization of AI agents that retain and update their internal state and memory over time, addressing the inherent statelessness of large language models (LLMs) like transformers <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. While a common definition of an agent is an LLM taking actions in a loop, this definition often overlooks the critical need for the agent to be updated within that closed loop <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Since LLMs are fundamentally stateless, a mechanism for updating their state is essential for them to "learn" and "remember" across interactions <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## The Problem with Stateless LLMs

LLMs primarily rely on their pre-trained weights and the current context window for "memory" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Without an explicit state management system, any "learning" or memory retention must be handled externally by the user or a framework <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Traditionally, this often means simply appending information to a list within a Python or Node.js process, which becomes highly problematic when trying to build reliable and useful [[Developing and optimizing AI agents | AI agents]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

Current LLM-driven agents face a significant limitation: they struggle to learn from experience, or their learning is extremely limited <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This is less noticeable in simple workflows but becomes evident when building assistants, companions, or co-pilots <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

For instance, an AI chatbot might mistakenly ask a user about an ex-partner if its memory isn't updated. A human would never make such a mistake, as this information would be aggressively written to their core memory <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The inability to learn from experience leads to painful interactions, where users must repeatedly re-describe context to the LLM <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## The Promise of Stateful Agents

The core idea behind [[Stateful AI Agents | stateful agents]] is to automate the context compilation process that power users of LLMs currently perform manually <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. True statefulness promises a product experience where interaction gets progressively better as the AI learns more about the user over time, eliminating derailments and haywire responses <a class="yt-timestamp" data-t="0:10:57">[0:10:57]</a>. By creating human-like memory constructs, the behavior of agents becomes more human-like, encompassing both recall and forgetfulness <a class="yt-timestamp" data-t="01:11:17">[01:11:17]</a>.

Beyond consumer applications, statefulness is crucial for enterprise use cases where companies possess vast amounts of data that cannot fit into a single context window <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. Stateful agents enable a "post-training" phase where the model can learn about a specific company or domain through in-context memory, rather than merely updating its weights <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This helps [[Building and Improving AI Agents | building and improving AI agents]] that are more human-like and capable <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Memory Management in Stateful Agents

The concept of "LMOS" (LLM Operating System) was introduced in the MeGPT paper, referring to a memory management system for LLMs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. If LLMs are to improve, memory management should ideally be handled by another LLM, allowing AI to manage AI memory <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Key aspects of memory management for stateful agents:

*   **Context Compilation** The process of optimally arranging the LLM's context window, drawing from a potentially very large state that cannot fit entirely within the window <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **Memory Blocks**: These are fundamental [[Components of AI agents | components of AI agents]] in frameworks like Leta, essentially strings with references that agents can edit <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. An agent can rewrite its own memory, for example, updating its persona or user information <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.
*   **Memory Tiers**: Mimicking human memory, stateful agents can utilize tiered memory:
    *   **Core Memory**: High-level, top-of-mind information that's always in the context window, similar to immediately remembering a friend's name and hobbies upon seeing them <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
    *   **Archival/Recall Memory**: Data sources existing outside the direct context window. This is akin to an agent "jogging its memory" by searching a database <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This functions similarly to "agentic RAG" (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.
        *   **Recall Memory** is typically conversation history, automatically written with events and read-protected from manual edits <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.
        *   **Archival Memory** is a general read/write data store of potentially infinite size, useful for storing large documents or arbitrary data outside the context window <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.
*   **Tools for Memory Management**: Agents are equipped with tools to manage their own memory <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.
    *   **Core Memory Tools**: Append to blocks (e.g., adding user details), replace blocks (e.g., correcting a user's name), and search memory (specific conversation search or generic RAG query) <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
    *   **Archival Memory Tools**: Insert data into the external database <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.
*   **Context Window Management**: Frameworks can artificially cap the context window length (e.g., 10k tokens or 4k tokens) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. If the context exceeds the limit, messages are evicted to recall memory and a summarizer runs to prevent overflow <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>.
*   **Metadata Statistics**: To address the "don't know what you don't know" problem, agents can be provided with metadata statistics about information outside their direct context (e.g., number of previous messages, total archival memories) <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

## Building and Operating Stateful Agents

Frameworks like Leta are designed around the concept of agents as persistent, stateful services, rather than ephemeral Python processes <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

*   **Server-Client Architecture**: Agents are created on a server, and the client interacts with them via an API, sending individual messages without needing to track the full conversation history <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. This allows agents to persist indefinitely <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Tool Calling Centric**: Every LLM invocation is treated as a tool call. Even when an agent just says "hello," it calls a `send_message` tool <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>. This enables frequent background execution and ensures tools are always "on" <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>.
*   **React-style Reasoning**: Agents often follow a "reasoning-action-observation" (ReAct) loop. In some frameworks, agents must explicitly state "I want to keep going" (heartbeat requests) to continue chaining actions, which is more practical than an "I'm done" explicit termination <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>.
*   **Configurability**: System prompts, personas, and memory limits are fully configurable <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.
*   **Tool Development**: Custom tools can be written (e.g., in Python for a Python backend) and attached to agents <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. These tools can even import the client, allowing agents to create or manage other agents and their memories <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>.
*   **Sandboxing**: Tools often run inside sandboxed environments (e.g., E2B) for security and to prevent interference between different agents or users <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
*   **Observability**: Developers can visualize the full payload sent to the LLM at any given point, making it easier to understand and debug agent behavior <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.

## Multi-Agent Systems with Stateful Agents

The persistence and API accessibility of [[Stateful AI Agents | stateful agents]] fundamentally change how multi-agent systems can be built <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. Unlike frameworks where agents are trapped in a single Python file, stateful agents exist independently and can communicate asynchronously through message passing <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>.

*   **Independent Existence**: Agents can be taken out of one multi-agent group and integrated into another, retaining their experience and memories <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.
*   **Flexible Communication**:
    *   **Asynchronous Messaging**: Agents can send messages and immediately continue their execution, similar to humans sending an iMessage without pausing their entire mental process <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>.
    *   **Synchronous Messaging**: For critical interactions (e.g., reaching out to a supervisor), an agent's execution can be paused until a reply is received <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.
    *   **Broadcast Messaging**: Agents can send messages to all other agents matching specific tags, enabling supervisor-worker patterns or parallelized tasks <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
*   **Shared Memory Blocks**: Memory blocks can be shared among multiple agents, ensuring consistent information across an organization of agents without duplication <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>. When one agent writes to a shared block, it is immediately broadcasted to all other agents linked to that block <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>.

## Challenges in Building Stateful Agents

*   **Tool Limit Degradation**: LLMs can become confused if given too many tools (e.g., typically above 12-15 tools can lead to performance degradation) <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. Solutions include dedicated "shadow agents" to handle memory tools, keeping the main agent's toolset focused on general API actions <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **"Don't Know What You Don't Know"**: If information is outside the context window and not explicitly prompted, the agent won't know it exists <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>. This can be mitigated by forcing agents to search archival memory at the start of a conversation via tool rules <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.
*   **Memory Eviction and Summarization**: When core memory blocks hit their limits, agents may receive errors, prompting them to summarize and push information to archival memory, similar to an OS flush <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>. This behavior can be controlled through prompt engineering.
*   **Document Editing**: LLMs are often better at rewriting entire documents than performing line-by-line diffs, making collaborative document editing with humans a complex, largely unsolved problem <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.

Despite these [[Challenges in Developing AI Agents | challenges]], the focus on statefulness and robust memory management is considered essential for moving beyond basic workflows towards more intelligent, human-like, and financially valuable AI applications <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.