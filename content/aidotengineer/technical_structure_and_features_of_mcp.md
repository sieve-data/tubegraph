---
title: Technical structure and features of mCP
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The [[model_context_protocol_mcp | Model Context Protocol (mCP)]] is an open protocol designed to enable seamless integration between AI applications/agents and external tools and data sources <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. It standardizes how AI applications interact with external systems <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

The motivation behind [[model_context_protocol_mcp | mCP]] is the core concept that models are only as good as the context provided to them <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This contrasts with earlier AI applications where context was often manually copied and pasted <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Over time, models have evolved to have hooks into user data and context, making them more powerful and personalized <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

[[model_context_protocol_mcp | mCP]] can be understood by comparing it to preceding protocols:
*   **APIs** standardized how web applications interact between the front-end and back-end, allowing front-ends access to servers and databases <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **LSP (Language Server Protocol)** standardized how IDEs interact with language-specific tools, allowing an LSP-compatible IDE to communicate with different features of coding languages <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
    *   For example, building a Go LSP server once allows any LSP-compatible IDE to hook into Go-specific functionalities during coding <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

The aim of [[model_context_protocol_mcp | mCP]] is to flatten the `N` times `M` problem of fragmentation in AI system development, where different client applications had numerous permutations for interacting with various servers <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. [[model_context_protocol_mcp | mCP]] serves as a layer between application developers and tool/API developers to standardize access for LLMs <a class="yt-timestamp" data-t="06:17:00">[06:17:17]</a>.

## Core Components and Interfaces

[[model_context_protocol_mcp | mCP]] standardizes interactions through three primary interfaces <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>:

### Tools
Tools are model-controlled functionalities <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. An [[model_context_protocol_mcp | mCP]] server exposes tools to the client application, and the Language Model (LLM) within the client application can choose when to invoke these tools <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
*   Tool descriptions are provided as part of the server definition, allowing the model to decide optimal invocation times <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
*   Tools can be used for various actions, including:
    *   Retrieving (read) data <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.
    *   Sending (write) data to applications <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.
    *   Updating databases or writing files to a local file system <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.
*   Tools are beneficial when it's ambiguous if and when an LLM should invoke them, for example, deciding whether to call a vector database based on current context <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.
*   Thousands of tools can theoretically be exposed by an LLM if search mechanisms like "tool to search tools" are implemented, using Rag (Retrieval Augmented Generation) or fuzzy/keyword search over tool libraries <a class="yt-timestamp" data-t="46:51:00">[46:51:00]</a>. Hierarchical systems of tools can also progressively expose groups of tools based on the current task <a class="yt-timestamp" data-t="47:18:00">[47:18:00]</a>.

### Resources
Resources are data exposed to the application, and they are application-controlled <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
*   A server can define or create resources like images, text files, or JSON data <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.
*   Resources offer a rich interface for applications and servers to interact beyond simple text-based chat <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   They can be static (e.g., a static file) or dynamic, where the client application sends user or file system information, and the server interpolates it into a complex data structure sent back to the client <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
*   In applications like Claude for Desktop, resources manifest as attachments, allowing users to select and attach them to a chat for the model to use <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.
*   Resources can also be automatically attached by the model if deemed relevant to a task <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.
*   [[model_context_protocol_mcp | mCP]] supports resource notifications, where the client can subscribe to a resource and be notified by the server when it's updated with new information <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>.

### Prompts
Prompts are user-controlled, predefined templates for common interactions with a specific server <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
*   They are invoked by the user, unlike tools which are invoked by the model <a class="yt-timestamp" data-t="13:01:00">[13:01:01]</a>.
*   An example is slash commands in an IDE like Zed, where `/GPR` can interpolate a longer, predefined prompt from an [[model_context_protocol_mcp | mCP]] server to summarize a pull request <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
*   Prompts can be dynamic, interpolated with context from the user or application, allowing the server to return a customized prompt based on the task <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.
*   They allow different teams to standardize interactions, such as document Q&A with specific formatting rules <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.

The distinction between tools, resources, and prompts emphasizes [[model_context_protocol_mcp | mCP]]'s goal to define richer interactions between applications and servers, providing more control to the model, application, and user, respectively <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.

## Key Technical Features

### Sampling
Sampling allows an [[model_context_protocol_mcp | mCP]] server to request LLM inference calls (completions) from the client, rather than the server needing to implement or host its own LLM interactions <a class="yt-timestamp" data-t="53:52:00">[53:52:00]</a>.
*   This feature allows servers to access intelligence, even if they've never interacted with a client before <a class="yt-timestamp" data-t="56:06:00">[56:06:00]</a>.
*   The client retains full control over privacy, cost parameters, and model preferences (e.g., specific Claude versions, model size), potentially ignoring malicious or undesired requests <a class="yt-timestamp" data-t="55:34:00">[55:34:00]</a>.
*   This design federates LLM requests, letting the client own LLM hosting and model choice, while the server can request inference with various parameters like system/task prompts, temperature, and max tokens <a class="yt-timestamp" data-t="54:55:00">[54:55:00]</a>.

### Composability
Composability in [[model_context_protocol_mcp | mCP]] refers to the logical, not physical, separation between a client and a server <a class="yt-timestamp" data-t="56:21:00">[56:21:00]</a>. Any application, API, or agent can simultaneously function as both an [[model_context_protocol_mcp | mCP]] client and an [[model_context_protocol_mcp | mCP]] server <a class="yt-timestamp" data-t="56:34:00">[56:34:00]</a>.
*   This enables chaining interactions, where calls can hop from a user to a client-server combination, and then to the next client-server combination, and so on <a class="yt-timestamp" data-t="57:17:00">[57:17:00]</a>.
*   This allows for the creation of complex, multi-layered architectures of LLM systems, where each layer can specialize in a particular task <a class="yt-timestamp" data-t="57:28:00">[57:28:00]</a>.
*   The combination of sampling and composability allows for hierarchical systems of agents, where each agent/server can federate sampling requests through layers back to the application controlling the primary LLM interaction <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.

### Remote Servers and Authentication
[[model_context_protocol_mcp | mCP]] supports remotely hosted servers and OAuth 2.0 for authentication <a class="yt-timestamp" data-t="01:13:28">[01:13:28]</a>.
*   Remote servers can operate over `ssse` (Server-Sent Events), which is the preferred method for remote communication, as opposed to standard IO for local or in-memory communication <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="01:32:19">[01:32:19]</a>.
*   The server orchestrates the authentication handoff (e.g., with Slack), handling the OAuth 2.0 handshake, getting a callback URL, and letting the client open it for user authorization <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.
*   The server then holds the OAuth token and federates future interactions using a session token <a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a>.
*   This removes the friction of local hosting, allowing agents and LLMs to live on different systems from where the server is running <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.

## [[integrating_ai_with_applications_using_model_context_protocol_mcp | Integration with Agents]]
[[model_context_protocol_mcp | mCP]] is seen as a foundational protocol for agents <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   It supports the concept of an "augmented LLM," which is an LLM enhanced with retrieval systems, tools, and memory <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   [[model_context_protocol_mcp | mCP]] serves as the layer that federates and simplifies how LLMs interact with these systems, allowing agents to expand their capabilities even after initial programming <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   Agent builders can focus on the core agent loop (context management, memory usage, model choice) while relying on [[model_context_protocol_mcp | mCP]] to standardize the way agents hook into external servers, tools, and data <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   Frameworks like "mCP Agent" (built by Last Mile AI) demonstrate how to define sub-agents (e.g., research agent, fact-checker agent, report writer agent) and give them access to various [[model_context_protocol_mcp | mCP]] servers (e.g., Brave for web search, file system access) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   This declarative approach means the agent builder specifies the task and available servers/tools, and the framework handles the underlying interactions <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## [[future_developments_and_roadmap_for_mcp | Future developments and roadmap for mCP]]
Key areas on the roadmap include:
*   **Registry API**: A unified and hosted metadata service to centralize the discovery and publishing of [[model_context_protocol_mcp | mCP]] servers <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. This will address fragmentation and enable dynamic discovery of new capabilities for agents, making them self-evolving <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>. It will also help with trust and verification (e.g., official servers) and versioning <a class="yt-timestamp" data-t="01:23:25">[01:23:25]</a>, <a class="yt-timestamp" data-t="01:24:01">[01:24:01]</a>.
*   **.well-known**: A complement to the registry, allowing services (like `shopify.com`) to host a `.well-known/mcp.json` file to declare their [[model_context_protocol_mcp | mCP]] endpoint, resources, and tools <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>. This provides a top-down, verified way for agents to find and use tools on a specific domain <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.
*   **Stateful vs. Stateless Connections**: Exploring short-lived HTTP-like connections for basic requests and long-lived SSE connections for advanced features like sampling or server-to-client notifications <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.
*   **Streaming**: Supporting first-class streaming of multiple chunks of data from server to client within the protocol <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Namespacing**: Addressing tool name conflicts when multiple servers expose tools with the same name, potentially through logical grouping of tools or first-class protocol support <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>.
*   **Proactive Server Behavior**: Developing patterns for servers to initiate actions (e.g., event-driven, deterministic systems) by asking for user input or notifying the user about something <a class="yt-timestamp" data-t="01:43:31">[01:43:31]</a>.

## Considerations and Best Practices
*   **Error Handling and Debugging**: While [[model_context_protocol_mcp | mCP]] itself doesn't enforce observability, the server builder is incentivized to expose useful data and debugging information via metadata to the client for a good user experience <a class="yt-timestamp" data-t="01:05:25">[01:05:25]</a>. Tools like "Inspector" (from Anthropic) allow users to examine logs and server connections <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>.
*   **Version Control**: [[model_context_protocol_mcp | mCP]] servers, often released as packages (npm, pip), follow standard package versioning, implying clear upgrade paths <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>. The upcoming registry will also support versioning for metadata <a class="yt-timestamp" data-t="01:24:01">[01:24:01]</a>.
*   **Trust and Security**: Users should be judicious about which servers they connect to <a class="yt-timestamp" data-t="01:18:06">[01:18:06]</a>. The server builder is responsible for controlling the flow of information and authentication, and future registry features will aid in verifying trusted sources <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>, <a class="yt-timestamp" data-t="01:38:19">[01:38:19]</a>.
*   **LLM Generation of Servers**: For simpler servers that primarily wrap existing APIs, LLMs can automatically generate [[model_context_protocol_mcp | mCP]] servers <a class="yt-timestamp" data-t="01:49:24">[01:49:24]</a>. However, more complex logic, logging, and data transformations may require manual implementation <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Transport Agnostic**: [[model_context_protocol_mcp | mCP]] is transport agnostic, meaning the underlying communication method (e.g., standard IO, SSE) does not alter the protocol's fundamental behavior, allowing for custom transports <a class="yt-timestamp" data-t="01:32:05">[01:32:05]</a>.