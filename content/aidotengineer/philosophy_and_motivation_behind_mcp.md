---
title: Philosophy and motivation behind mCP
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The fundamental philosophy behind the [[model_context_protocol_mcp | Model Context Protocol (mCP)]] is rooted in the belief that models are only as effective as the context provided to them <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This core concept drives the development of [[model_context_protocol_mcp | mCP]] as an open protocol designed to enable seamless integration between AI applications and their tools and data sources <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Historical Precedent and Inspiration
[[model_context_protocol_mcp | mCP]]'s design draws inspiration from prior successful protocols that standardized interactions in other domains <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>:
*   **APIs**: APIs emerged to standardize how web applications interact between the front-end and back-end, acting as a translation layer for requests <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This allowed front-ends to access servers, databases, and services <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **LSP (Language Server Protocol)**: LSP standardized how Integrated Development Environments (IDEs) interact with language-specific tools <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. An LSP-compatible IDE can communicate with a single Go LSP server, granting access to all Go language features when coding <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

[[model_context_protocol_mcp | mCP]] was born from this inspiration, aiming to standardize how AI applications interact with external systems <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Addressing Industry Fragmentation
Before [[model_context_protocol_mcp | mCP]], the AI industry, and even individual companies, experienced significant fragmentation in building AI systems <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Teams would create custom implementations for AI applications to hook into context, often with unique prompt logic, diverse methods for integrating tools and data, and varying approaches to federating access <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This led to an "N times M problem" with numerous permutations for client-server interaction <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### The World With [[model_context_protocol_mcp | mCP]]
[[model_context_protocol_mcp | mCP]] seeks to flatten this complexity by providing a standardized layer between application developers and tool/API developers <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. In a world with [[model_context_protocol_mcp | mCP]], AI development is standardized, allowing any [[model_context_protocol_mcp | mCP]] client (e.g., Perser, Windsurf, Goose) to connect to any [[model_context_protocol_mcp | mCP]] server with zero additional effort <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

An [[model_context_protocol_mcp | mCP]] server acts as a wrapper, federating access to various systems and tools relevant to AI applications, such as databases, CRMs like Salesforce, or local systems like Git <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Value Proposition
The standardization offered by [[model_context_protocol_mcp | mCP]] provides value across the ecosystem:
*   **Application Developers**: Once an application is [[model_context_protocol_mcp | mCP]] compatible, it can connect to any server without additional work <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Tool/API Providers**: Developers can build an [[model_context_protocol_mcp | mCP]] server once and see it adopted across various AI applications <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **End Users**: Experience more powerful and context-rich AI applications that understand them and can take action in the real world <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Enterprises**: Enables a clear separation of concerns between different teams <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. For example, a team managing a vector database can turn it into an [[model_context_protocol_mcp | mCP]] server, allowing other teams to build AI applications faster without needing to re-implement access logic <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This mirrors the benefits seen with microservices <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

## Core Concepts and Interfaces
[[model_context_protocol_mcp | mCP]] standardizes interactions through three primary interfaces: prompts, tools, and resources <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a> <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. A key philosophical distinction lies in their control:

*   **Tools**: Model-controlled, meaning the LLM within the client application decides when to invoke them based on descriptions provided by the server <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Tools allow for reading and writing data, updating databases, or interacting with local file systems <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The choice to use a tool is often best when it's ambiguous if or when it should be invoked <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Resources**: Application-controlled, exposing data (e.g., images, text files, JSON) from the server to the client application <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. The application then decides how to use this data <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Resources offer a rich interface beyond simple text-based chatbot interactions <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a> and can be static or dynamic, interpolated with context from the user or application <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   **Prompts**: User-controlled, serving as predefined templates for common interactions with a specific server <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. This allows users to invoke specific functionalities, akin to "slash commands," which then generate a longer, pre-defined prompt for the LLM <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

This separation of control (model, application, user) is a deliberate design choice to give more control to each part of the system, not just the model <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

## [[agent_evaluation_using_model_conduct_protocol_mcp | mCP]] as a Foundational Protocol for [[agent_evaluation_using_model_conduct_protocol_mcp | Agents]]
A significant motivation and future vision for [[model_context_protocol_mcp | mCP]] is its role as the foundational protocol for [[agent_evaluation_using_model_conduct_protocol_mcp | agents]] <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.

### Augmented LLMs and the Agentic Loop
The concept of an "augmented LLM" involves an LLM enhanced with access to retrieval systems, tools, and memory <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. [[model_context_protocol_mcp | mCP]] functions as the underlying layer that federates and simplifies the LLM's ability to communicate with these systems <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.

This means:
*   **Expandable Agents**: [[model_context_protocol_mcp | Agents]] can expand their capabilities even after initial programming, discovering different interactions with the world <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
*   **Focus on Core Logic**: [[agent_evaluation_using_model_conduct_protocol_mcp | Agent]] builders can focus on the core agent loop, context management, and how the LLM processes data, rather than on the specifics of integrating diverse servers and tools <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.
*   **Open Capabilities**: [[model_context_protocol_mcp | mCP]] provides these capabilities in an open way, allowing users to customize agents with their own context and preferred data interactions <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### Key Protocol Capabilities for [[agent_evaluation_using_model_conduct_protocol_mcp | Agents]]

1.  **Sampling**: Allows an [[model_context_protocol_mcp | mCP]] server to request LLM inference calls (completions) from the client, rather than the server needing to host or interact with an LLM directly <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>. This federates requests and gives the client control over LLM hosting, model choices, privacy, and cost <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>.
2.  **Composability**: An application, API, or [[agent_evaluation_using_model_conduct_protocol_mcp | agent]] can simultaneously be both an [[model_context_protocol_mcp | mCP]] client and an [[model_context_protocol_mcp | mCP]] server <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a>. This enables chaining interactions and building complex, layered architectures where specialized LLM systems can interact <a class="yt-timestamp" data-t="00:57:17">[00:57:17]</a>. Each node in the system can possess autonomy and make decisions on how to pull in richer data <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.

The combination of sampling and composability is particularly exciting for future [[agent_evaluation_using_model_conduct_protocol_mcp | agents]], envisioning hierarchical systems of [[agent_evaluation_using_model_conduct_protocol_mcp | agents]] that can exist on the public web while maintaining privacy, security, and control <a class="yt-timestamp" data-t="01:11:43">[01:11:43]</a>.

## Roadmap and Future Directions
The philosophy of [[model_context_protocol_mcp | mCP]] continues to drive its roadmap, focusing on features that reduce friction, enhance discoverability, and enable more sophisticated AI applications:

*   **Remote Servers and Authentication**: The addition of OAuth 2.0 support allows for remotely hosted servers, removing the need for local setup and friction for users <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a> <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>. This means [[model_context_protocol_mcp | mCP]] servers can exist like websites, discoverable and accessible without complex local configuration <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>.
*   **[[future_developments_and_roadmap_for_mcp | mCP Registry API]]**: A centralized, open, and hosted metadata service is being developed to address discoverability issues for [[model_context_protocol_mcp | mCP]] servers <a class="yt-timestamp" data-t="01:22:27">[01:22:27]</a>. This registry will help users find trusted servers, understand their capabilities, and manage versioning <a class="yt-timestamp" data-t="01:23:34">[01:23:34]</a>. Critically, it aims to make [[agent_evaluation_using_model_conduct_protocol_mcp | agents]] "self-evolving" by allowing them to dynamically discover and utilize new tools and data on the fly, without prior programming <a class="yt-timestamp" data-t="01:35:59">[01:35:59]</a>.
*   **Well-Known [[model_context_protocol_mcp | mCP]]**: This concept provides a top-down approach for organizations to declare their [[model_context_protocol_mcp | mCP]] endpoint (e.g., `well-known/mcp.json`), allowing agents to discover and authenticate with official services <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>. This complements the registry by offering a verified way to access tools, especially when combined with computer use models (for long-tail interactions not covered by APIs) <a class="yt-timestamp" data-t="01:40:52">[01:40:52]</a>.
*   **Medium-Term Considerations**: [[future_developments_and_roadmap_for_mcp | Future developments and roadmap for mCP]] also include exploring stateful vs. stateless connections, streaming data, improved namespacing for tools, and proactive server behavior (where servers can initiate interactions with clients) <a class="yt-timestamp" data-t="01:41:31">[01:41:31]</a>.

The overarching philosophy is to build an open protocol that fosters competition, benefits users and developers, and creates a highly connected and intelligent ecosystem for AI applications and [[agent_evaluation_using_model_conduct_protocol_mcp | agents]] <a class="yt-timestamp" data-t="01:28:39">[01:28:39]</a>.