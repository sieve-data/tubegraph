---
title: Tool Usage and Development in AI Frameworks
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article explores the role and development of tools within AI frameworks, focusing on their integration with Large Language Models (LLMs) and the emerging paradigm of stateful agents.

## Workshop Setup: Leta Framework <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

The Leta framework workshop includes an interactive component that requires users to install Docker and pull a specific Docker image to run the server component <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. A Jupyter notebook serves as the client, interacting with the Docker-hosted server <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The Leta server is an open-source stack built with FastAPI, PostgreSQL, and Python logic <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. Its API allows interaction with agents <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>, similar to the chat completions API, but session-based, eliminating the need to provide full conversation history with each interaction <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

### Core Concepts in Leta <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>

Leta distinguishes itself from other frameworks by being a server-client process, allowing agents to be stateful and persist indefinitely <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. This centralized server acts as a single source of truth for agent states <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.

Key components of memory in a Leta agent include:
*   **Memory Blocks**: These are strings with references that the agent can edit. For example, an agent can rewrite its own "persona" or update information about a user <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   **System Prompt**: While read-only for the agent, users can configure the system prompt to guide agent behavior and interaction style <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.
*   **Tools**: Agents are equipped with tools to manage their memory and perform actions <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>.

## Stateful Agents and Memory Management <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>

The workshop redefines the concept of an "agent" as a [[stateful_agents | stateful agent]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. While a common definition of an agent is an LM taking actions in a loop <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, this definition often misses the crucial aspect of the agent being updated within a closed loop <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. LLMs, built on stateless transformers <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, necessitate a mechanism for state updates when the loop is closed <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. The distinction between stateless and stateful agents is vital because LLMs inherently lack memory beyond their weights and current context window <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

For agents to deliver on their promise, solving the problem of "stapleness" or memory is paramount <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Unlike humans who form new memories and learn over time <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, learning in LLMs must be managed by the user or the framework <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Traditionally, state is handled by simply appending to a list <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, which becomes problematic when building useful, long-running agents <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

The concept of a "Memory Management System for LLMs" (LMOS) is introduced <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The core idea is that if LLMs are to improve, the memory management should ideally be performed by another LLM <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This contrasts with the typical approach where context windows are loosely defined and held in process memory <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. A memory management system implies an optimal way to arrange the context window, drawing from a potentially very large state outside the immediate context <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This automated context compilation aims to prevent issues like chat derailment, a common problem when using tools like ChatGPT or Claude for extended periods <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

The primary reason for desiring stateful agents is the inability of current agents to truly learn from experience <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. While less noticeable in workflow-based applications, this limitation becomes evident when building assistants or companions <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Stateful agents are crucial for learning from vast amounts of data, especially in enterprise settings where data often exceeds context window limits <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. This introduces a "post-training" phase where the model learns about a specific company or user in-context memory, not by updating its weights <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Memory Tiers <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>

Leta employs two tiers of memory to mimic human memory:
1.  **Core Memory**: This is top-level information directly within the context window, akin to immediate recall about a person <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.
2.  **Archival and Recall Memory**: These are data sources that exist outside the context window. The agent can "jog its memory" to retrieve information from these sources, similar to a human searching through photos for a past event <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>. This is analogous to [[agentic_rag | agentic RAG]] <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.

The key distinction between archival and recall memory:
*   **Recall Memory** (conversation history): Automatically written upon event, but cannot be manually written to <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. It's designed to mimic a conversation search function <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.
*   **Archival Memory**: A general read/write data store of infinite size, like a vector database of strings <a class="yt-timestamp" data-t="00:33:25">[00:33:25]</a>. It's for actively storing large documents or data outside the context window <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

Memory blocks are backed by an API, allowing direct modification and sharing among multiple agents in a multi-agent system <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

## Tools and Function Calls <a class="yt-timestamp" data-t="01:12:13">[01:12:13]</a>

Tool calling is central to Leta's design for managing context <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>. LLMs are continually improving at [[using_tools_and_function_calls_with_ai_sdk | tool calling]] <a class="yt-timestamp" data-t="01:12:16">[01:12:16]</a>.

### Agent Interactions and Tool Execution <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>

In Leta, every LLM invocation is treated as a tool call <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>. Even simple responses require calling a "send message" tool <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. This means tools are always "on" <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>, allowing agents to run in the background without constantly speaking to the user <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>.

When a message is sent, a payload is created including the system prompt, memories, messages, and tool schemas <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. The agent is required to output a tool call and a reasoning snippet (justification) <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>. Leta supports native reasoning from models like DeepSeek's R1 API or injects "think tokens" for models without native reasoning <a class="yt-timestamp" data-t="00:52:17">[00:52:17]</a>.

Agents can chain tool calls indefinitely, with limits settable via API <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. This chaining is enabled by "heartbeat requests," where the agent explicitly signals its desire to continue execution <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. This is an inversion of the traditional React pattern, where agents typically loop until they explicitly state they are "done" <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.

### Types of Tools <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>

Leta agents come with built-in memory management tools:
*   **Core Memory Tools**:
    *   `append`: Add information to memory blocks (e.g., "the user also has a boyfriend called James") <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
    *   `replace`: Update existing information (e.g., "the user's name is actually Charles") <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
    *   `search`: Perform specific conversation searches or generic RAG queries on external data sources <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.
*   **Archival Memory Tool**: `insert`: Store data into the external database <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>. This is typically a vector database <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>.

### Custom Tool Development <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>

Custom tools can be written in Python and deployed on the Leta backend <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>. A key feature is the ability to import the Leta client directly within a tool <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>, allowing agents to manage other agents' memory or even create new agents <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a>. Tools run inside a sandbox by default, supporting E2B keys for secure execution in private clouds or multi-tenant services <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.

All Composio tools are also baked into Leta by default, allowing integration with popular services like BigQuery or Google Calendar if a Composio API key is provided <a class="yt-timestamp" data-t="01:00:42">[01:00:42]</a>.

### [[challenges_in_ai_development | Challenges in AI Development]] with Tools <a class="yt-timestamp" data-t="01:12:13">[01:12:13]</a>

*   **Tool Confusion**: Agents can become confused if too many tools are added, leading to performance degradation <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. A potential solution is a dedicated "shadow agent" or "subconscious" that handles memory management tools, separate from the main agent's general API actions <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **"You Can't Know What You Don't Know"**: If information exists outside the LLM's context window, the agent won't know it has access to it. This can be mitigated by providing metadata statistics (e.g., number of previous messages or total archival memories) within the context <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.
*   **Context Window Limits**: Leta allows artificial capping of context window length (e.g., 10k tokens) to manage costs and latency <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>. If the limit is approached or exceeded, Leta automatically evicts messages into recall memory via a summarizer (configurable as truncation or recursive summary), ensuring the context never overflows <a class="yt-timestamp" data-t="00:54:36">[00:54:36]</a>.
*   **Debugging**: Visualizing the full payload sent to the LLM can be challenging in many frameworks <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>. Leta's "context simulator" provides clear visibility into what's in the context window at any given point <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.
*   **Testing Tools**: It can be difficult to test if a tool is working well without getting the agent to run it. Leta allows running tools separately from the agent for easier testing <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>.

## Multi-Agent Systems with Tools <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>

The concept of multi-agent systems is explored, contrasting with traditional frameworks like Autogen where agents are often trapped within a Python file and lack true independence <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>. Leta's approach emphasizes independent, stateful agents running on servers and accessible via APIs <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>. This allows for asynchronous message passing between agents, similar to human communication over channels like Slack <a class="yt-timestamp" data-t="01:02:40">[01:02:40]</a>.

Leta provides multi-agent tools to facilitate communication patterns:
*   **Asynchronous Message Passing**: Agents can send messages to each other and immediately get a receipt without pausing their own execution <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. This mimics human interaction where one doesn't freeze while waiting for a reply <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>.
*   **Synchronous Message Passing**: Agents can send a message and wait for a reply, which is useful when a supervisor agent needs to freeze its execution until it receives a response (e.g., asking for help) <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.
*   **Group Messaging**: Agents can send messages to all agents matching specific tags, enabling supervisor-worker concepts or parallelized tasks <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.

Because agents are API-accessible services, they can be dynamically managed (e.g., removing a tool to prevent an agent from replying) <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>.

## User Interface and Experience <a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>

The Leta framework also offers a UI builder (AD) for faster iteration in a low-code environment <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>. This interface visualizes agent interactions, memory blocks, and tool usage, offering an alternative to purely programmatic SDK interactions <a class="yt-timestamp" data-t="00:57:18">[00:57:18]</a>. The AD environment can be used to set up basic agent attributes, adjust context window sizes, and explore the `context simulator` for payload transparency <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>. This represents a potential [[developing_ai_agents_for_productivity | new iteration of the playground]] experience, moving beyond the current ubiquitous stateless chat interfaces <a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>.

## Conclusion <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>

The focus on stateful agents and robust tool integration, particularly with an "agents as services" paradigm, addresses current deficiencies in LLM agents' ability to learn and retain memory, moving towards more human-like AI behavior <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>. This approach is highly relevant for building verticalized agents and complex enterprise workflows where continuous learning and persistent state are critical <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.