---
title: Integration of mCP with AI Applications
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The Model Context Protocol (mCP) is an open protocol developed by Anthropic's applied AI team designed to enable seamless integration between AI applications, agents, tools, and data sources <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. It addresses the challenge that models are only as effective as the context provided to them <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## Motivation and Philosophy Behind mCP

A year ago, context was primarily brought into AI chatbots by manual copy-pasting or typing <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Over time, these systems evolved to have hooks into user data and context, making them more powerful and personalized <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. Anthropic observed significant fragmentation in how companies built AI systems, with different teams creating custom implementations for prompt logic, tool integration, and data access <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. This fragmentation led to an "N times M problem," where client applications and servers had myriad ways of interacting <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

mCP aims to standardize [[ai_integration_and_tool_calling | how AI applications interact with external systems]] <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>, providing a layer between application developers and tool/API developers to give LLMs access to data <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Predecessors and Analogies

mCP draws inspiration from previous standardization protocols:
*   **APIs**: Standardized how web applications interact between the front-end and back-end, allowing access to servers, databases, and services <a class="yt-timestamp" data-t="02:12:00">[02:12:12]</a>.
*   **LSP (Language Server Protocol)**: Standardizes how IDEs interact with language-specific tools <a class="yt-timestamp" data-t="02:37:00">[02:37:40]</a>. An LSP-compatible IDE can interact with any Go LSP server, for example, to understand Go language features <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## How mCP Works

mCP standardizes interactions between AI applications and external systems through three primary interfaces <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>:

### 1. Tools
Tools are "model-controlled," meaning the server exposes them to the client application, and the Large Language Model (LLM) within the client decides the optimal time to invoke them <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   Servers provide descriptions of how tools are used <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   Tools can perform various actions, including reading data, writing data, updating databases, and managing local file systems <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.
*   Tools are beneficial when it's ambiguous if and when they should be invoked by the LLM <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.

### 2. Resources
Resources are "application-controlled" data exposed to the application <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
*   Servers can define and create static or dynamic resources (e.g., images, text files, JSON) <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.
*   The client application determines how to use the resource <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   Resources enable richer interactions beyond simple text-based chat <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   In applications like Claude for Desktop, resources appear as attachments, allowing users to select and send them to the model <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>. They can also be automatically attached by the model based on relevance <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.
*   mCP supports resource notifications, where clients can subscribe to a resource and be notified by the server when it's updated with new information or context <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>.

### 3. Prompts
Prompts are "user-controlled" and act as predefined templates for common interactions with a specific server <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
*   They are analogous to slash commands in IDEs like Zed, where a short command can interpolate a longer, predefined prompt to the LLM <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
*   Prompts can standardize formatting rules or data presentation for common tasks like document Q&A across different teams <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
*   Prompts can be dynamic, interpolated with context from the user or application <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.

## Value Proposition of mCP

The adoption of mCP offers several advantages:
*   **For Application Developers**: Once a client is mCP compatible, it can connect to any server without additional work <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   **For Tool and API Providers**: Building an mCP server once allows its adoption across various AI applications <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
*   **For End Users**: Leads to more powerful and context-rich AI applications <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
*   **For Enterprises**: Provides a clear way to separate concerns between teams. For instance, an infrastructure team owning a vector database can turn it into an mCP server, allowing other teams to build AI applications faster without needing direct access or custom integration <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. This concept is similar to microservices, where teams own specific services <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

## Adoption and Real-World Examples

mCP has seen significant traction since its launch <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
*   **Applications and IDEs**: Provides a way for users coding in IDEs to provide context to the IDE, allowing agents within the IDE to interact with external systems like GitHub or documentation sites <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. Examples include Cursor and Windsurf <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Community Servers**: Over 1,100 community-built mCP servers have been published open source <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. Companies like Block have launched mCP clients (e.g., Goose) <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
*   **Official Integrations**: Companies like Cloudflare and Stripe have built official mCP integrations <a class="yt-timestamp" data-t="50:30:00">[50:30:00]</a>.
*   **Demo with Claude for Desktop**:
    *   Claude for Desktop (an mCP client) can be given a GitHub repo URL and tasked with triaging issues <a class="yt-timestamp" data-t="23:13:00">[23:13:00]</a>.
    *   The model (Claude) automatically invokes the "list issues" tool to pull issues into context and summarize them <a class="yt-timestamp" data-t="23:29:00">[23:29:00]</a>.
    *   It intelligently prioritizes issues based on user context <a class="yt-timestamp" data-t="23:43:00">[23:43:00]</a>.
    *   Claude can then triage issues and add them to an Asana project, using tools like "list workspaces" and "search projects" from an Asana mCP server <a class="yt-timestamp" data-t="24:15:00">[24:15:00]</a>.
    *   Many of these servers are community-built and require only a few hundred lines of code <a class="yt-timestamp" data-t="24:52:00">[24:52:00]</a>.
    *   Claude for Desktop acts as a central dashboard for bringing in context from various external systems <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a>.

## [[mCPs Role in Augmented LLM Systems | mCP's Role in Augmented LLM Systems]]

mCP is envisioned as a foundational protocol for agents broadly <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>. It supports the concept of an "augmented LLM," which involves the LLM interacting with retrieval systems, tools, and memory <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>.

### Key Capabilities for Agents

*   **Federation**: mCP can federate and simplify how LLMs interact with retrieval systems, invoke tools, and manage memory in a standardized way <a class="yt-timestamp" data-t="28:10:00">[28:10:00]</a>.
*   **Expandability**: Agents can expand their capabilities even after initial programming by discovering new tools and interactions with the world <a class="yt-timestamp" data-t="28:41:00">[28:41:00]</a>.
*   **Agentic Loop**: At its core, an agent system is an augmented LLM running in a loop, doing tasks, invoking tools, and responding to results until the task is complete <a class="yt-timestamp" data-t="29:03:00">[29:03:00]</a>. mCP provides these capabilities openly, allowing agent builders to focus on the core loop and context management rather than server capabilities or data provision <a class="yt-timestamp" data-t="29:18:00">[29:18:18]</a>.

### mCP Agent Framework Example

The open-source mCP Agent framework, built by Last Mile AI, showcases how agents can interact with mCP <a class="yt-timestamp" data-t="30:21:00">[30:21:00]</a>.
*   A multi-agent system can be defined in a simple Python file <a class="yt-timestamp" data-t="30:41:00">[30:41:00]</a>.
*   Example: A research agent tasked with researching Quantum Computing's impact on cybersecurity, using mCP servers for Brave (web search), Fetch (data retrieval), and File System (file management) <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a>.
*   Other agents, like a fact-checker agent and a research report writer agent, can use similar or different mCP servers to complete their sub-tasks <a class="yt-timestamp" data-t="32:05:00">[32:05:00]</a>.
*   The agent first forms a plan (a series of steps) based on its task and available servers <a class="yt-timestamp" data-t="33:02:00">[33:02:00]</a>.
*   mCP serves as an abstraction layer, allowing the agent builder to focus on the task and agent interactions rather than the underlying server details <a class="yt-timestamp" data-t="33:48:00">[33:48:00]</a>.

### Sampling

Sampling allows an mCP server to request LLM inference calls (completions) from the client, rather than the server implementing its own LLM interaction <a class="yt-timestamp" data-t="53:52:00">[53:52:00]</a>.
*   This is useful when a server needs intelligence (e.g., to ask for more user input or formulate questions) <a class="yt-timestamp" data-t="54:46:00">[54:46:00]</a>.
*   The client retains full control over the LLM interaction, including hosting, model choice, privacy, and cost parameters <a class="yt-timestamp" data-t="54:55:00">[54:55:00]</a>.
*   Servers can specify preferences for model size or version <a class="yt-timestamp" data-t="55:12:00">[55:12:00]</a>.
*   This design principle accounts for scenarios where clients have no prior knowledge of a server <a class="yt-timestamp" data-t="55:52:00">[55:52:00]</a>.

### Composability

Composability means that any application, API, or agent can function as both an mCP client and an mCP server <a class="yt-timestamp" data-t="56:21:00">[56:21:00]</a>.
*   This allows for chaining interactions and building complex, multi-layered architectures of LLM systems, where each layer specializes in a particular task <a class="yt-timestamp" data-t="57:17:00">[57:17:00]</a>.
*   For example, a user interacts with Claude for Desktop (client), which calls a research agent (mCP server and client), which in turn calls other servers like the file system, fetch, or web search servers <a class="yt-timestamp" data-t="56:40:00">[56:40:00]</a>.
*   This enables hierarchical systems of agents where each node can have autonomy and intelligence, making decisions on how to pull in richer data <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>.
*   The combination of sampling and composability allows for hierarchical agent systems where sampling requests are federated through layers back to the application controlling the LLM interaction <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.

## Future and Roadmap

### Remote Servers and Authentication
Support for OAuth 2.0 has been added to the mCP protocol <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
*   This enables remotely hosted servers accessible via a public URL <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>.
*   The server orchestrates the OAuth handshake, handles the callback URL, and stores the OAuth token, providing the client with a session token for future interactions <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.
*   Remote servers can operate over SSSE (Server-Sent Events) as opposed to standard I/O, removing development friction and making servers discoverable like websites <a class="yt-timestamp" data-t="01:14:04">[01:14:04]</a>.
*   This significantly boosts the number of available servers as users don't need to host or build them locally <a class="yt-timestamp" data-t="01:15:37">[01:15:37]</a>.

### Registry and Discoverability
Currently, there's no centralized way to discover and integrate mCP servers <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   An official mCP registry API is under development <a class="yt-timestamp" data-t="01:22:30">[01:22:30]</a>.
*   This will be a unified, hosted metadata service, built in the open, addressing questions like protocol discovery, server trust, and official verification <a class="yt-timestamp" data-t="01:22:52">[01:22:52]</a>.
*   The registry will also include versioning to track changes in APIs, tools, or tool descriptions <a class="yt-timestamp" data-t="01:24:01">[01:24:01]</a>.
*   **Self-Evolving Agents**: An mCP server registry allows agents to become self-evolving by dynamically discovering new capabilities and data on the fly <a class="yt-timestamp" data-t="01:35:59">[01:35:59]</a>. An agent can search the registry for a verified server (e.g., Grafana), install or invoke it remotely, and then perform tasks like querying logs or fixing bugs, even if it wasn't pre-programmed to do so <a class="yt-timestamp" data-t="01:36:32">[01:36:32]</a>. This means agents can find and choose their own tools, making the [[mcps_role_in_augmented_llm_systems | augmented LLM system]] more powerful <a class="yt-timestamp" data-t="01:37:06">[01:37:06]</a>.
*   **Well-Known mCP**: A complementary approach to the registry is a "well-known" mCP JSON file (e.g., `shopify.com/.well-known/mcp.json`) <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>. This provides a verified, top-down approach for agents to discover and interact with specific services using their predefined APIs, complementing UI-based computer use models for long-tail interactions <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

### Medium-Term Considerations
*   **Stateful vs. Stateless Connections**: Exploring short-lived connections for basic capabilities (client asking server) and maintaining long-lived connections for advanced features like sampling or server-initiated notifications <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.
*   **Streaming**: How to support streaming data and multiple chunks of data arriving at the client from the server over time <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Namespacing**: Addressing conflicts when multiple servers have tools with the same name, potentially through logical grouping of tools within the protocol <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>.
*   **Proactive Server Behavior**: Developing patterns for event-driven or deterministic server behavior where the server initiates contact with the user or client to ask for information or provide notifications <a class="yt-timestamp" data-t="01:43:31">[01:43:31]</a>. This includes scenarios where a server initiates sampling from scratch, perhaps triggered by an external API request <a class="yt-timestamp" data-t="01:30:27">[01:30:27]</a>.

Ultimately, Anthropic aims for its products to be the best mCP clients, but not the only ones, fostering competition and an open ecosystem that benefits users and developers <a class="yt-timestamp" data-t="01:28:15">[01:28:15]</a>.