---
title: Future developments and roadmap for mCP
videoId: kQmXtrmQ5Zg
---

From: [[aidotengineer]] <br/> 

The roadmap for [[Model Context Protocol MCP|mCP]] involves several exciting developments aimed at enhancing its capabilities, promoting wider adoption, and simplifying the development and discovery of AI applications and agents <a class="yt-timestamp" data-t="01:11:14">[01:11:14]</a>.

## Remote Servers and Authentication

A significant upcoming feature is the support for remotely hosted [[Model Context Protocol MCP|mCP]] servers, addressing a primary request since the protocol's launch <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a> <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>. This means servers can live on a public URL, removing the need for users to understand or host them locally, making them accessible "like a website exists" <a class="yt-timestamp" data-t="01:15:12">[01:15:12]</a> <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a> <a class="yt-timestamp" data-t="01:15:49">[01:15:49]</a>.

The protocol now supports OAuth 2.0 for authentication <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a> <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>. The server orchestrates the OAuth handshake, guiding the user through the authentication flow (e.g., opening a browser for consent) and then securely holds the OAuth token <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a> <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>. This allows the server to federate interactions with the end application by providing the client with a session token for future use <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>. This design prioritizes the server's control over the interaction with the final application, especially given that clients and servers may not have prior knowledge of each other <a class="yt-timestamp" data-t="01:17:30">[01:17:30]</a> <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>.

## Registry and Discovery

A major focus is addressing the current fragmentation in [[Model Context Protocol MCP|mCP]] server discovery <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a> <a class="yt-timestamp" data-t="01:22:21">[01:22:21]</a>. An official [[Model Context Protocol MCP|mCP]] registry API is under development, designed as a unified and hosted metadata service <a class="yt-timestamp" data-t="01:22:30">[01:22:30]</a> <a class="yt-timestamp" data-t="01:22:38">[01:22:38]</a>. This registry will operate in the open, with its schema and development fully public <a class="yt-timestamp" data-t="01:22:41">[01:22:41]</a>.

The registry aims to solve several problems:
*   **Discovery**: Centralizing how users find [[Model Context Protocol MCP|mCP]] servers <a class="yt-timestamp" data-t="01:23:50">[01:23:50]</a>.
*   **Protocol Details**: Providing information on server protocols (e.g., standard I/O vs. SSE) <a class="yt-timestamp" data-t="01:23:15">[01:23:15]</a>.
*   **Trust and Verification**: Identifying who built a server and if it's officially verified by a company (e.g., Shopify's official [[Model Context Protocol MCP|mCP]] server) <a class="yt-timestamp" data-t="01:23:25">[01:23:25]</a> <a class="yt-timestamp" data-t="01:23:27">[01:23:27]</a>. Users should be judicious about connecting to servers, and the registry will help with trust <a class="yt-timestamp" data-t="01:18:06">[01:18:06]</a> <a class="yt-timestamp" data-t="01:18:28">[01:18:28]</a>.
*   **Versioning**: Supporting versioning for servers, logging changes like new tools or updated descriptions <a class="yt-timestamp" data-t="01:24:04">[01:24:04]</a> <a class="yt-timestamp" data-t="01:24:07">[01:24:07]</a> <a class="yt-timestamp" data-t="01:20:32">[01:20:32]</a>.
*   **Self-Evolving Agents**: Enabling agents to dynamically discover and use new capabilities and data on the fly, without needing to be pre-programmed with all possible tools <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a> <a class="yt-timestamp" data-t="01:37:08">[01:37:08]</a>. An agent could search the registry for a specific server (e.g., Grafana) and then install/invoke it to perform tasks <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>.

Companies will also be able to host their own private registries, similar to Artifactory <a class="yt-timestamp" data-t="01:24:45">[01:24:45]</a> <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>.

## Well-Known [[Model Context Protocol MCP|mCP]] JSON

Complementing the registry, the concept of a `well-known mCP.json` file is being explored <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a> <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>. This standardized file (e.g., `shopify.com/.well-known/mCP.json`) would provide a verified interface for an agent to discover [[Model Context Protocol MCP|mCP]] endpoints, their capabilities, and authentication methods (like OAuth 2.0) for a given domain <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a> <a class="yt-timestamp" data-t="01:39:48">[01:39:48]</a>. This allows for a "top-down" approach to discovery, where an agent can directly look up a domain for its [[Model Context Protocol MCP|mCP]] services <a class="yt-timestamp" data-t="01:40:17">[01:40:17]</a>.

This feature is particularly powerful when combined with "computer use" models (like Anthropic's October 2023 release) that can interact with UIs without APIs <a class="yt-timestamp" data-t="01:40:35">[01:40:35]</a> <a class="yt-timestamp" data-t="01:40:39">[01:40:39]</a>. An agent could use `well-known mCP.json` for predefined API interactions and then fall back to computer use (clicking buttons, logging in) for long-tail scenarios without dedicated APIs <a class="yt-timestamp" data-t="01:40:51">[01:40:51]</a> <a class="yt-timestamp" data-t="01:41:03">[01:41:03]</a>.

## Medium-Term Considerations

Beyond the immediate roadmap, several areas are being considered for future development:
*   **Stateful vs. Stateless Connections**: Exploring a bifurcation where basic client-initiated requests use short-lived connections (like HTTP), while advanced capabilities (e.g., [[Technical structure and features of mCP | sampling]], server-to-client notifications) use long-lived connections (like SSE) <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a> <a class="yt-timestamp" data-t="01:42:06">[01:42:06]</a> <a class="yt-timestamp" data-t="01:42:26">[01:42:26]</a>. This would allow clients to disconnect and reconnect without losing context <a class="yt-timestamp" data-t="01:41:53">[01:41:53]</a>.
*   **Streaming**: Developing first-class support in the protocol for streaming multiple chunks of data from the server to the client over time <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Namespacing**: Addressing tool name conflicts when multiple servers are installed by providing native protocol support for logical grouping of tools <a class="yt-timestamp" data-t="01:42:54">[01:42:54]</a> <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. The registry will also help with this <a class="yt-timestamp" data-t="01:43:11">[01:43:11]</a>.
*   **Proactive Server Behavior/Elicitation**: Improving patterns for servers to initiate actions, such as asking the user for more information or notifying them about changes, possibly driven by events or deterministic systems <a class="yt-timestamp" data-t="01:43:31">[01:43:31]</a> <a class="yt-timestamp" data-t="01:43:38">[01:43:38]</a>. This includes server-initiated notifications when resources change <a class="yt-timestamp" data-t="01:30:06">[01:30:06]</a>.

## Vision for the Future

The combination of sampling (server requesting LLM inference from client) and composability (applications acting as both [[Model Context Protocol MCP|mCP]] clients and servers) is particularly exciting for the future of agents <a class="yt-timestamp" data-t="01:11:43">[01:11:43]</a> <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This enables the creation of hierarchical systems of agents, where different layers specialize in tasks and can federate sampling requests through the system <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a> <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>. This "connectivity layer" allows agents to interact with publicly hosted or custom-built servers while maintaining desired privacy, security, and control <a class="yt-timestamp" data-t="01:12:40">[01:12:40]</a> <a class="yt-timestamp" data-t="01:12:46">[01:12:46]</a>. The vision is for [[Model Context Protocol MCP|mCP]] to be the foundational protocol for agents broadly <a class="yt-timestamp" data-t="02:26:36">[02:26:36]</a>.