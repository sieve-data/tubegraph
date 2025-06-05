---
title: Introduction to Model Context Protocol mCP
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The Model Context Protocol ([[model_context_protocol_mcp | mCP]]) is an open protocol designed to enable seamless integration between AI applications, agents, and external tools and data sources <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. It aims to standardize how AI applications interact with these external systems <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

## Philosophy and Motivation Behind mCP
The core motivation behind [[model_context_protocol_mcp | mCP]] is the understanding that models are only as effective as the context provided to them <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. Historically, context was manually provided to chatbots through copy-pasting or typing <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Over time, systems evolved to allow models to directly access user data and context, making them more powerful and personalized <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

[[model_context_protocol_mcp | mCP]] draws inspiration from established protocols:
*   **APIs:** Standardized how web applications interact between front-end and back-end, allowing access to servers, databases, and services <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **LSP (Language Server Protocol):** Standardizes how Integrated Development Environments (IDEs) interact with language-specific tools, enabling an LSP-compatible IDE to work with different coding languages efficiently <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

Before [[model_context_protocol_mcp | mCP]], the AI industry faced significant fragmentation in building AI systems <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Teams often created custom implementations for integrating context, prompting logic, and tool/data access <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. This led to an N times M problem, with numerous permutations for client applications to interact with servers <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

The world with [[model_context_protocol_mcp | mCP]] promotes standardized AI development <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. An [[model_context_protocol_mcp | mCP]] client (e.g., Anthropic's first-party applications, Cursor, Windsurf, Goose) can connect to any [[model_context_protocol_mcp | mCP]] server with zero additional work <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. An [[model_context_protocol_mcp | mCP]] server acts as a wrapper, federating access to various relevant systems and tools, such as databases, CRMs like Salesforce, or local systems like Git <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Value Proposition of mCP
[[model_context_protocol_mcp | mCP]] offers significant benefits to various stakeholders in the AI ecosystem:
*   **Application Developers:** Once an application client is [[model_context_protocol_mcp | mCP]] compatible, it can connect to any [[model_context_protocol_mcp | mCP]] server without additional work <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   **Tool/API Providers:** Developers can build their [[model_context_protocol_mcp | mCP]] server once and see it adopted across many AI applications <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
*   **End Users:** Gain access to more powerful and context-rich AI applications <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
*   **Enterprises:** Provides a clear way to separate concerns among different teams. For example, one team can own and maintain an [[model_context_protocol_mcp | mCP]] server interface for a vector database, allowing other teams to build AI applications faster without constantly needing direct access or custom implementations <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. This mirrors the benefits of microservices architectures <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

## Technical Structure and Features of mCP
[[model_context_protocol_mcp | mCP]] standardizes interactions through three primary interfaces <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>:

### Tools
Tools are "model-controlled" <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. The server exposes tools to the client application, and the Language Model (LLM) within the client decides when to invoke them <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. Descriptions of tool usage are part of the server definition <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>. Tool possibilities are vast, including:
*   Read tools to retrieve data <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.
*   Write tools to send data or take actions in various systems <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.
*   Tools to update databases or write files to a local file system <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.
*   Tools can be used when it's ambiguous if they should be invoked, allowing the LLM to decide based on context <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.

### Resources
Resources are "application-controlled" and represent data exposed to the application <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. Servers can define and create various data types like images, text files, or JSON objects <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. The application then determines how to use these resources <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
Resources provide a richer interface for application-server interaction beyond just text <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>. Use cases include:
*   Surfacing static or dynamic files <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
*   Client applications sending information (user data, file system context) to the server, which interpolates it into complex data structures and sends it back <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
*   In Cloud for Desktop, resources appear as attachments that users can select and send to the chat, or models can automatically attach them if relevant to the task <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.
*   Resources in [[model_context_protocol_mcp | mCP]] can be dynamic, interpolated with context from the user or application <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.
*   Resource notifications allow clients to subscribe to a resource and be notified by the server when it's updated with new information <a class="yt-timestamp" data-t="21:17:00">[21:17:17]</a>.

### Prompts
Prompts are "user-controlled" and are considered tools that the user invokes directly, as opposed to the model <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. They are predefined templates for common interactions with a specific server <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
*   An example is Slash commands in an IDE like Zed, where a user types a command (e.g., `/GPR` for a PR summary) and the server interpolates a longer, predefined prompt to the LLM <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
*   Prompts can standardize common interactions, such as document Q&A or specific data formatting rules <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
*   Similar to resources, prompts can also be dynamic and customized based on the task at hand <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.

[[model_context_protocol_mcp | mCP]] provides more control to different parts of the system—model, application, and user—rather than just the model <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.

## Adoption and Real-World Examples
[[model_context_protocol_mcp | mCP]] has seen significant adoption, becoming a frequent topic in discussions with Anthropic's customers <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
*   **Applications and IDEs:** Provides a way for users coding in an IDE to give context to the AI, allowing agents to interact with external systems like GitHub or documentation sites <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   **Server-Side Development:** Over 1,100 community-built [[model_context_protocol_mcp | mCP]] servers have been open-sourced <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. Companies like Cloudflare and Stripe have also published official integrations <a class="yt-timestamp" data-t="50:30:00">[50:30:00]</a>.
*   **Open Source Contributions:** There's active contribution to the core protocol and its infrastructure layer <a class="yt-timestamp" data-t="09:07:00">[09:07:07]</a>.

### Demonstration: Cloud for Desktop
In a demonstration, Cloud for Desktop (an [[model_context_protocol_mcp | mCP]] client) interacts with GitHub and Asana through [[model_context_protocol_mcp | mCP]] servers <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. The user provides a GitHub repo URL and asks Claude to pull issues and triage them <a class="yt-timestamp" data-t="23:13:00">[23:13:00]</a>. Claude automatically invokes a `list issues` tool, summarizes the issues, and intelligently prioritizes them based on previous interactions <a class="yt-timestamp" data-t="23:32:00">[23:32:00]</a>. When asked to add issues to an Asana project, Claude uses installed Asana server tools (`list workspaces`, `search projects`) to find the project and add tasks <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.

Key takeaways from this example:
*   The Asana and GitHub servers were community-built with just a few hundred lines of code, primarily for surfacing tools <a class="yt-timestamp" data-t="24:52:00">[24:52:00]</a>.
*   Multiple distinct tools and systems seamlessly interplay within the Cloud for Desktop interface, which acts as a central dashboard for daily tasks <a class="yt-timestamp" data-t="25:07:00">[25:07:00]</a>.
*   Other applications like Windsurf and Goose also use [[model_context_protocol_mcp | mCP]], sometimes calling tools "extensions," demonstrating the protocol's adaptability to different application layers and UIs <a class="yt-timestamp" data-t="25:52:00">[25:52:00]</a>.

### Demonstration: mCP Agent Framework
The [[model_context_protocol_mcp | mCP]] agent framework, an open-source tool by Last Mile AI, illustrates how [[model_context_protocol_mcp | mCP]] integrates with agent systems <a class="yt-timestamp" data-t="30:21:00">[30:21:00]</a>. This framework allows defining different sub-agents for a larger task <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a>.
*   A "research agent" is defined as an expert web researcher, given access to Brave for web searching, a fetch tool for data retrieval, and the file system <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>.
*   A "fact checker agent" uses the same tools to verify information <a class="yt-timestamp" data-t="32:06:00">[32:06:00]</a>.
*   A "research report writer agent" synthesizes data and produces a report, with access only to the file system and fetch tools <a class="yt-timestamp" data-t="32:21:00">[32:21:00]</a>.

The [[model_context_protocol_mcp | mCP]] agent framework lets the overall orchestrator agent (which plans and tracks steps) leverage these specialized sub-agents <a class="yt-timestamp" data-t="32:55:00">[32:55:00]</a>. [[model_context_protocol_mcp | mCP]] acts as an abstraction layer, allowing agent builders to focus on the task and agent interactions rather than managing individual servers or tools <a class="yt-timestamp" data-t="33:48:00">[33:48:00]</a>. It enables agents to interface with community-built, authoritative servers in a standardized, declarative way <a class="yt-timestamp" data-t="34:58:00">[34:55:00]</a>.

## mCP as a Foundational Protocol for Agents
[[model_context_protocol_mcp | mCP]] is positioned to become a foundational protocol for agents <a class="yt-timestamp" data-t="26:38:00">[26:38:00]</a> due to its protocol features and the increasing effectiveness of agent systems and models <a class="yt-timestamp" data-t="26:54:00">[26:54:00]</a>.

### Augmented LLMs and the Agent Loop
The concept of an "augmented LLM" involves an LLM that takes inputs, produces outputs, and uses its intelligence to decide on actions, but is augmented with access to retrieval systems, tools, and memory <a class="yt-timestamp" data-t="27:29:00">[27:29:00]</a>. This allows the LLM to query and write data, invoke tools, respond to results, and maintain state across interactions <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>.

[[model_context_protocol_mcp | mCP]] fits in as the entire bottom layer, federating access and making it easier for LLMs to interact with these systems in a standardized way <a class="yt-timestamp" data-t="28:10:00">[28:10:00]</a>. This means agents can expand their capabilities even after initialization, discovering different interactions with the world without being pre-programmed <a class="yt-timestamp" data-t="28:34:00">[28:34:00]</a>.

Agent systems fundamentally involve an augmented LLM running in a loop, performing tasks, working towards goals, invoking tools, and responding to results until the task is complete <a class="yt-timestamp" data-t="28:57:00">[28:57:00]</a>. [[model_context_protocol_mcp | mCP]] provides these capabilities to the augmented LLM in an open way, allowing agent builders to focus on the core loop, context management, and model usage, while users can customize agent interactions with their own data <a class="yt-timestamp" data-t="29:18:00">[29:18:00]</a>.

### Sampling
Sampling is a powerful, though underutilized, [[model_context_protocol_mcp | mCP]] capability that allows an [[model_context_protocol_mcp | mCP]] server to request LLM inference calls (completions) from the client <a class="yt-timestamp" data-t="53:49:00">[53:49:00]</a>. This means the server doesn't need to implement its own LLM interaction or host an LLM <a class="yt-timestamp" data-t="54:02:00">[54:02:00]</a>.
*   The client controls all LLM interactions, including hosting, model choice, privacy, and cost parameters <a class="yt-timestamp" data-t="54:55:00">[54:55:00]</a>.
*   The server can request inference with various parameters (model preferences, system/task prompts, temperature, max tokens), though the client retains discretion to fulfill the request <a class="yt-timestamp" data-t="55:12:00">[55:12:00]</a>.
*   This is crucial because clients and servers often interact without prior knowledge of each other, yet servers may still need to request intelligence <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>.

### Composability
Composability means that the distinction between a client and a server is logical, not physical; any application, API, or agent can act as both an [[model_context_protocol_mcp | mCP]] client and an [[model_context_protocol_mcp | mCP]] server <a class="yt-timestamp" data-t="56:21:00">[56:21:00]</a>. This enables chaining interactions, where, for example, a user talks to a client, which then calls an agent (acting as both client and server), which in turn invokes other servers (file system, web search) <a class="yt-timestamp" data-t="56:40:00">[56:40:00]</a>. Data then flows back through the chain to the user <a class="yt-timestamp" data-t="57:13:00">[57:13:00]</a>.

This allows for building complex, multi-layered architectures where each layer specializes in a particular task <a class="yt-timestamp" data-t="57:28:00">[57:28:00]</a>. The combination of sampling and composability is particularly exciting for agent systems, allowing for hierarchical agents where sampling requests are federated through layers back to the main application that controls the LLM interaction <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.

## Future Developments and Roadmap for mCP
The [[future_developments_and_roadmap_for_mcp | roadmap for mCP]] focuses on enhancing its capabilities and ease of use.

### Remote Servers and Authentication
A significant development is the support for remote servers and OAuth 2.0 authentication <a class="yt-timestamp" data-t="01:13:22">[01:13:22]</a>.
*   This allows [[model_context_protocol_mcp | mCP]] servers to live on public URLs and be discoverable <a class="yt-timestamp" data-t="01:15:12">[01:15:12]</a>.
*   The server orchestrates the OAuth handshake, with the client opening the authentication flow in a browser, and the server holding the OAuth token. Subsequent interactions use a session token provided to the client <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.
*   This removes developer friction, as users don't need to understand [[model_context_protocol_mcp | mCP]] hosting or building; servers simply exist like websites <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a>.
*   It enables agents and LLMs to run on completely different systems from where the server is hosted, while maintaining privacy, security, and control <a class="yt-timestamp" data-t="01:15:28">[01:15:28]</a>.

### mCP Registry
To address the current fragmentation and lack of a centralized way to discover and pull in [[model_context_protocol_mcp | mCP]] servers, an official [[model_context_protocol_mcp | mCP]] registry API is under development <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   This will be a unified and hosted metadata service, built in the open, with its schema and development fully transparent <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>.
*   It will sit above existing package systems (npm, pip, Java, Rust, Go) where [[model_context_protocol_mcp | mCP]] servers are deployed <a class="yt-timestamp" data-t="01:22:52">[01:22:52]</a>.
*   The registry will solve problems like discovering server protocols (standard IO vs. SSSE), whether a server is local or URL-based, and verifying who built it (e.g., official verification by companies like Shopify) <a class="yt-timestamp" data-t="01:23:10">[01:23:10]</a>.
*   It will also support versioning, allowing tracking of changes to tools or tool descriptions <a class="yt-timestamp" data-t="01:24:01">[01:24:01]</a>. Companies can host their own registries similar to Artifactory <a class="yt-timestamp" data-t="01:24:45">[01:24:45]</a>.

For agents, an [[model_context_protocol_mcp | mCP]] server registry allows for "self-evolving" agents <a class="yt-timestamp" data-t="01:35:59">[01:35:59]</a>. Agents can dynamically discover new capabilities and data on the fly, without needing prior programming <a class="yt-timestamp" data-t="01:36:04">[01:36:04]</a>. For example, a coding agent could search the registry for a verified Grafana server if it needs to check logs, install or invoke it (even remotely), and proceed with the task <a class="yt-timestamp" data-t="01:36:16">[01:36:16]</a>. This empowers agents to find and choose their own tools, making the augmented LLM system even more powerful <a class="yt-timestamp" data-t="01:37:04">[01:37:04]</a>.

### Well-Known mCP
A complement to the registry is the concept of a `.well-known/mcp.json` endpoint <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>. A service like Shopify could host this file at `shopify.com/.well-known/mcp.json`, providing a verified interface detailing its [[model_context_protocol_mcp | mCP]] endpoint, resource capabilities, and OAuth 2.0 authentication <a class="yt-timestamp" data-t="01:39:30">[01:39:30]</a>. This allows agents to directly discover and use [[model_context_protocol_mcp | mCP]] capabilities for known services <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

This approach complements computer vision-based "computer use" models (e.g., Anthropic's model released in October) <a class="yt-timestamp" data-t="01:40:36">[01:40:36]</a>. For systems with well-defined APIs, [[model_context_protocol_mcp | mCP]] provides a predefined way to call them. For the "longtail" of systems without APIs, computer use models can click around and interact with UIs <a class="yt-timestamp" data-t="01:41:03">[01:41:03]</a>. The future vision is one where both coexist within a single agent <a class="yt-timestamp" data-t="01:41:11">[01:41:11]</a>.

### Medium-Term Considerations
*   **Stateful vs. Stateless Connections:** Exploring more short-lived connections where clients can disconnect and reconnect without losing context, potentially bifurcating basic client-initiated requests from advanced server-initiated behaviors (like sampling or notifications that require long-lived connections) <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.
*   **Streaming:** Developing first-class support in the protocol for streaming multiple chunks of data from the server to the client over time <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Namespacing:** Addressing conflicts when multiple servers expose tools with the same name, potentially through registry support, allowing logical grouping of tools, or introducing protocol-level namespacing <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>.
*   **Proactive Server Behavior:** Refining patterns for server-initiated actions, where the server decides to ask the user for more information or notify them based on events or deterministic systems <a class="yt-timestamp" data-t="01:43:31">[01:43:31]</a>.