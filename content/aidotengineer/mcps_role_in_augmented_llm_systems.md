---
title: mCPs Role in Augmented LLM Systems
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

Model Context Protocol (mCP) is an open protocol designed to enable seamless [[integration_of_mcp_with_ai_applications | integration between AI applications and agents]] with external tools and data sources <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Developed by Anthropic, mCP is rooted in the philosophy that models are only as effective as the context they are provided <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## Motivation and Precursors

Historically, providing context to AI assistants or chatbots involved manual copy-pasting or typing <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Over time, systems evolved to allow models direct hooks into user data and context, making them more powerful and capable of [[personalization_strategies_using_llms | personalized interactions]] <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. mCP was launched to standardize this interaction <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

The development of mCP drew inspiration from preceding protocols:
*   **APIs (Application Programming Interfaces)**: Standardized how web applications interact between front-end and back-end, translating requests and allowing access to servers, databases, and services <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   **LSP (Language Server Protocol)**: Standardizes how Integrated Development Environments (IDEs) interact with language-specific tools <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. An LSP-compatible IDE can interact with features of different coding languages by hooking into a single LSP server <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

Before mCP, the industry faced significant fragmentation in building AI systems, with different teams creating custom implementations for prompt logic, tool integration, and data access <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. mCP aims to standardize AI development, providing a common interface for AI clients to connect with any mCP server <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

## Core Components of mCP

mCP standardizes how AI applications interact with external systems through three primary interfaces <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>:

1.  **Tools**: These are "model-controlled" capabilities <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. mCP servers expose tools, and the Large Language Model (LLM) within the client application chooses when to invoke them <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. This allows LLMs to retrieve data (read tools), send data to applications (write tools), update databases, write files, and perform actions in various systems <a class="yt-timestamp" data-t="11:05:00">[11:05:05]</a>.
2.  **Resources**: These represent "application-controlled" data exposed to the AI application <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. Servers can define and create static or dynamic resources (e.g., images, text files, JSON) <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. The application then decides how to use these resources <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. Resources provide a richer interface for interaction beyond simple text-based chatbots <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
3.  **Prompts**: These are "user-controlled" predefined templates for common interactions with a specific server <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. Users can invoke these prompts, which are then interpolated with context and sent to the LLM <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.

> [!NOTE] Separation of Control
> A key design principle of mCP is the clean separation between what is model-controlled (Tools), application-controlled (Resources), and user-controlled (Prompts) <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. This allows for richer interactions where the application can decide when to use a resource based on predefined rules or LLM calls, rather than relying solely on the model <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

## Value and [[development_and_adoption_of_mcp | Adoption]]

mCP provides value across the ecosystem:
*   **Application Developers**: Can connect mCP-compatible clients to any server with zero additional work <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   **Tool/API Providers**: Can build an mCP server once and see it adopted across various AI applications <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. This addresses the "N times M problem" of many permutations for client-server interaction <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
*   **End Users**: Benefit from more powerful and context-rich AI applications <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a> that can take action in the real world <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.
*   **Enterprises**: Gain a clear way to separate concerns between teams. One team can own and maintain an mCP server for shared infrastructure (e.g., a vector database), allowing other teams to build AI applications faster without needing to rebuild access methods <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

[[development_and_adoption_of_mcp | Adoption]] has been significant, with mCP appearing in almost every Anthropic conversation <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. Examples of mCP clients include Anthropic's first-party applications, Cursor, Windsurf, and agents like Goose by Block <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. Over 1,100 community-built servers have been published open source <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>, alongside servers built by companies and official integrations <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.

## mCP's Role in [[augmented_llm_architectures | Augmented LLM Systems]]

mCP is envisioned as a foundational protocol for agents <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. An [[augmented_llm_architectures | augmented LLM]] is an LLM that can interact with external systems like retrieval systems, tools, and memory <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. These augmentations allow the LLM to query and write data, invoke tools, respond to results, and maintain state <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

> [!INFO] mCP as the Augmentation Layer
> mCP fits in as the "entire bottom layer" of an [[augmented_llm_architectures | augmented LLM]] system <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. It [[integration_of_mcp_with_ai_applications | federates and makes it easier]] for LLMs to communicate with retrieval systems, invoke tools, and access memory in a standardized, open way <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

This standardization means:
*   **Dynamic Capability Expansion**: Agents can expand their capabilities even after initialization, discovering new interactions with the world without being pre-programmed <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Focus for Agent Builders**: Agent builders can concentrate on the core agent loop, context management, and how the LLM uses memory, rather than on building custom integrations with every tool or data source <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Users can also customize the agent by bringing in their own context and data sources <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Key Protocol Capabilities for Agents

1.  **Sampling**: Allows an mCP server to request LLM inference calls (completions) from the client, rather than implementing LLM interaction itself <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This allows the client to own LLM hosting, model choices, privacy controls, and cost parameters, while the server requests intelligence <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This is crucial for servers that need intelligence but don't know anything about the client initially <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
2.  **Composability**: A logical separation where any application, API, or agent can simultaneously be both an mCP client and an mCP server <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. This enables chaining of interactions, where a user talks to a client (e.g., Claude for Desktop), which acts as a server to an agent, which in turn acts as a client to other mCP servers (e.g., file system, web search) <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. This allows for complex, multi-layered [[augmented_llm_architectures | LLM architectures]] where each layer specializes in a particular task <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## Road Map and [[future_of_mcp_in_agentbased_systems | Future of mCP]]

The [[future_of_mcp_in_agentbased_systems | future of mCP]] involves several key developments:

*   **Remote Servers and Authentication**: mCP now supports remotely hosted servers over Server-Sent Events (SSE) <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a> and integrates with OAuth 2.0 for authentication <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. This reduces [[problems_faced_by_mcp_developers | developer friction]], allowing users to connect to servers without needing to understand hosting or building <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>. The server manages the OAuth handshake and holds the token, federating interactions between the user and the end application <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>.
*   **mCP Registry API**: Addressing the [[challenges_in_the_MCP_ecosystem | lack of a centralized way to discover and pull mCP servers]] <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>. This unified, hosted metadata service will make it easier to discover servers, verify their source (e.g., official Shopify server), and manage versioning <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>. The registry will facilitate agents becoming "self-evolving" by dynamically discovering new capabilities and data on the fly <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.
*   **Well-Known mCP JSON**: A complement to the registry, allowing organizations to publish a standard JSON file (e.g., `/.well-known/mcp.json`) describing their mCP endpoint, resources, and tools <a class="yt-timestamp" data-t="16:27:00">[16:27:00]</a>. This provides a verified, top-down approach for agents to discover and interact with specific services <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. It also complements "computer use" models, allowing agents to combine API calls with UI interaction for the long tail of functionalities without dedicated APIs <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.

### Medium-Term Considerations

*   **Stateful vs. Stateless Connections**: Exploring more short-lived connections, allowing clients to disconnect and reconnect while continuing conversations without re-providing data <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
*   **Streaming**: Enhancing the protocol to support first-class streaming of multiple data chunks from server to client over time <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
*   **Namespacing**: Addressing conflicts when multiple servers have tools of the same name, potentially through logical grouping of tools within the protocol <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.
*   **Proactive Server Behavior**: Developing patterns for event-driven servers to initiate actions, such as asking the user for more information or notifying them about updates <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>.