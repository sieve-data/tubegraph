---
title: Future of mCP in Agentbased Systems
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The [[Model context protocol MCP|Model Context Protocol (mCP)]] is envisioned as a foundational protocol for agents broadly, due to its specific protocol features and the increasing effectiveness of models in utilizing provided data <a class="yt-timestamp" data-t="02:36:18">[02:36:18]</a>. This evolution allows agents to become more powerful and context-rich <a class="yt-timestamp" data-t="06:28:30">[06:28:30]</a>.

## [[mCPs Role in Augmented LLM Systems|mCP's Role in Augmented LLMs]]

[[mCPs Role in Augmented LLM Systems|mCP]] fits as the bottom layer of an [[mCPs Role in Augmented LLM Systems|augmented LLM]] system <a class="yt-timestamp" data-t="02:49:54">[02:49:54]</a>. An [[mCPs Role in Augmented LLM Systems|augmented LLM]] takes inputs and produces outputs, using its intelligence to decide actions <a class="yt-timestamp" data-t="02:37:31">[02:37:31]</a>. The "augmentation" comes from its ability to interact with retrieval systems, invoke tools, and manage memory <a class="yt-timestamp" data-t="02:40:52">[02:40:52]</a>.

[[Model context protocol MCP|mCP]] standardizes how [[Multiagent systems in AI|AI applications]] interact with external systems <a class="yt-timestamp" data-t="03:10">[03:10]</a> by facilitating communication with:
*   **Tools**: Model-controlled functions for retrieving or sending data, updating databases, or interacting with local file systems <a class="yt-timestamp" data-t="11:02:43">[11:02:43]</a>.
*   **Resources**: Application-controlled data exposed to the application, such as files (static or dynamic) or JSON data <a class="yt-timestamp" data-t="11:23:0">[11:23:0]</a>.
*   **Prompts**: User-controlled, predefined templates for common interactions with a server <a class="yt-timestamp" data-t="12:59:16">[12:59:16]</a>.

This standardization allows agents to expand and discover different capabilities and interactions with the world even after initial programming or initialization <a class="yt-timestamp" data-t="02:41:40">[02:41:40]</a>. Users can also customize how the agent interacts with their data <a class="yt-timestamp" data-t="02:40:52">[02:40:52]</a>.

> "Agent systems at its core aren't that complicated. They are this augmented LLM concept running in a loop where the augmented LLM goes and does a task, it kind of works towards some kind of goal, it invokes a tool, looks at the response and then does that again and again and again until it's done with the task." <a class="yt-timestamp" data-t="02:54:33">[02:54:33]</a>

## Key [[Future of AI agent ecosystems|Protocol Capabilities]] for Agents

### Sampling
[[Future of AI agent ecosystems|Sampling]] is a feature where an [[Model context protocol MCP Overview|mCP]] server can request [[Multiagent systems in AI|LLM]] inference calls from the client <a class="yt-timestamp" data-t="05:52:19">[05:52:19]</a>. This means the server does not need to implement or host its own [[Multiagent systems in AI|LLM]] interaction <a class="yt-timestamp" data-t="05:52:19">[05:52:19]</a>. The client retains full control over privacy, cost, and model preferences <a class="yt-timestamp" data-t="05:42:0">[05:42:0]</a>.

### [[Future of AI agent ecosystems|Composability]]
The logical separation between an [[Model context protocol MCP Overview|mCP]] client and server means that any application, API, or agent can act as both <a class="yt-timestamp" data-t="05:56:26">[05:56:26]</a>. This allows for chaining interactions and creating complex architectures with specialized layers of [[Multiagent systems in AI|LLM systems]] <a class="yt-timestamp" data-t="05:57:28">[05:57:28]</a>. For example, a main client can interact with an orchestrator agent (which is an [[Model context protocol MCP Overview|mCP]] server), and that orchestrator agent can then act as an [[Model context protocol MCP Overview|mCP]] client to invoke other specialized agents (e.g., analysis, coding, research) <a class="yt-timestamp" data-t="06:05:0">[06:05:0]</a>.

## [[MCP agent finetuning|mCP Agent Frameworks]]

Frameworks like Last Mile AI's [[MCP agent finetuning|mCP agent]] allow developers to define sub-agents (e.g., research agent, fact-checker agent, report writer agent) and give them access to various [[Model context protocol MCP Overview|mCP]] servers (e.g., Brave for web search, Fetch for data pulling, file system for local access) <a class="yt-timestamp" data-t="03:14:15">[03:14:15]</a>. This simplifies the development process as the agent builder can focus on the task and how the agent should interact with systems, rather than on the underlying servers or data <a class="yt-timestamp" data-t="03:51:53">[03:51:53]</a>.

## [[Future of AI agent ecosystems|Remote Servers and Authentication]]

Recent developments include support for remotely hosted [[Model context protocol MCP Overview|mCP]] servers and OAuth 2.0 authentication <a class="yt-timestamp" data-t="11:43:56">[11:43:56]</a>. This allows servers to live on a public URL and orchestrate authentication flows directly, with the server holding the OAuth token and giving the client a session token for future interactions <a class="yt-timestamp" data-t="11:49:55">[11:49:55]</a>. This significantly reduces developer friction by making [[Model context protocol MCP Overview|mCP]] servers as accessible as websites <a class="yt-timestamp" data-t="11:50:5">[11:50:5]</a>.

## [[Future of AI agent ecosystems|Registry and Discovery]]

A significant future development is an official [[Model context protocol MCP Overview|mCP]] registry API <a class="yt-timestamp" data-t="12:30:0">[12:30:0]</a>. This unified, hosted metadata service aims to solve discoverability issues for [[Model context protocol MCP Overview|mCP]] servers <a class="yt-timestamp" data-t="12:30:0">[12:30:0]</a>. It will provide a layer above existing package systems (like npm, pipie) to answer questions such as:
*   What is the protocol (standard IO, SSE, local file, URL)? <a class="yt-timestamp" data-t="12:29:0">[12:29:0]</a>
*   Who built it, and is it trusted/verified? <a class="yt-timestamp" data-t="12:29:0">[12:29:0]</a>
*   What changes occurred between versions? <a class="yt-timestamp" data-t="12:40:52">[12:40:52]</a>

This registry will enable agents to be "self-evolving" by dynamically discovering new capabilities and data on the fly, without needing pre-programming <a class="yt-timestamp" data-t="13:59:0">[13:59:0]</a>. For example, a coding agent could search the registry for a verified Grafana server if it needs to check logs <a class="yt-timestamp" data-t="13:59:0">[13:59:0]</a>.

A complementary concept is a ".well-known/mcp.json" file for specific domains <a class="yt-timestamp" data-t="13:52:0">[13:52:0]</a>. This would allow agents to discover [[Model context protocol MCP Overview|mCP]] endpoints directly on a website, providing a verified way to use tools specific to that domain <a class="yt-timestamp" data-t="14:07:0">[14:07:0]</a>. This approach can coexist with computer use models (e.g., [[Multiagent systems in AI|LLMs]] that click around UIs), allowing agents to use direct APIs where available and UI interaction for long-tail cases <a class="yt-timestamp" data-t="14:07:0">[14:07:0]</a>.

## [[Future of AI agent ecosystems|Roadmap and Future Considerations]]

Medium-term considerations for [[Model context protocol MCP Overview|mCP]] include:
*   **Stateful vs. Stateless Connections**: Exploring short-lived HTTP-like connections for basic interactions versus long-lived SSE connections for advanced features like [[Future of AI agent ecosystems|sampling]] and server-to-client notifications <a class="yt-timestamp" data-t="14:11:32">[14:11:32]</a>.
*   **Streaming**: Supporting first-class streaming of data chunks from server to client within the protocol <a class="yt-timestamp" data-t="14:39:41">[14:39:41]</a>.
*   **Namespacing**: Addressing tool name conflicts when multiple servers are installed, potentially through logical grouping of tools within the protocol <a class="yt-timestamp" data-t="14:51:30">[14:51:30]</a>.
*   **Proactive Server Behavior**: Developing patterns for servers to initiate actions, such as event-driven notifications or requesting more information from the user <a class="yt-timestamp" data-t="15:00:23">[15:00:23]</a>.

> [!tip] Integration with existing systems
> The speaker notes that [[Multiagent systems in AI and API-Based Communication|mCP]] complements [[Designing and optimizing agent environments|agent frameworks]] like LangGraph, rather than replacing them. Adapters can be built to connect existing [[Designing and optimizing agent environments|agent systems]] to [[Model context protocol MCP Overview|mCP]] servers, tools, and resources in a standardized way <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>.