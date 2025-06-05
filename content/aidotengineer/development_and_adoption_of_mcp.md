---
title: Development and adoption of MCP
videoId: z4zXicOAF28
---

From: [[aidotengineer]] <br/> 

The Model Context Protocol ([[model_context_protocol_mcp | MCP]]) has rapidly gained traction in the AI engineering world, with a dedicated track at the 2025 AI Engineer World's Fair [00:21:49]. Described as the "default protocol for connecting with the outside world" [00:29:09], [[model_context_protocol_mcp | MCP]] is seen as a foundational shift in the internet's economy, where "tool calls are becoming the new clicks" [02:31:08].

## Origin Story and Evolution
The concept of [[model_context_protocol_mcp | MCP]] originated in mid-2023 with Anthropic co-creators David and Justin [02:33:05]. They observed engineers constantly copying and pasting context (like Slack messages or error logs) into an LLM's context window [02:33:20]. Their vision was for LLMs, such as Claude, to "climb out of its box, reach out into the real world and bring that context and those actions to the model" [02:33:52].

The genesis of [[model_context_protocol_mcp | MCP]] was rooted in the idea of "model agency"—giving the model the ability to interact with the outside world [02:34:06]. They concluded that an open-source, [[standardization_and_adoption_of_mcp | standardized protocol]] was essential for this to scale [02:34:20]. This approach aimed to overcome the challenges of closed-source ecosystems, where integrating an LLM would require complex business development and interface alignment [02:34:29].

The protocol was initially developed by a small internal team at Anthropic and launched during their company hack week in November 2023 [02:35:28]. It quickly went viral internally, with engineers building [[model_context_protocol_mcp | MCPs]] to automate workflows [02:35:41]. This success led to [[model_context_protocol_mcp | MCP]] being open-sourced in November 2023 [02:36:08].

Despite the initial enthusiasm, the public launch faced questions about the necessity of a new, open-source protocol given existing model tool-calling capabilities [02:36:40]. However, a significant turning point came with Cursor's adoption of [[model_context_protocol_mcp | MCP]], followed by other coding tools like VS Code and Sourcegraph [02:37:18]. More recently, major AI players including Google, Microsoft, and OpenAI have also adopted [[model_context_protocol_mcp | MCP]], solidifying its status as a standard [02:37:47].

## Key Features and Principles
[[model_context_protocol_mcp_overview | MCP's core focus]] is on enabling model agency, allowing the model's intelligence to choose actions and decide what to do [02:39:18]. The protocol is built on principles that anticipate a future with many more servers than clients [02:40:26], optimizing for server simplicity and better tooling for server builders [02:40:41]. This design choice means that complexity is often pushed to the client side [02:40:50].

Recent advancements in [[model_context_protocol_mcp | MCP]] include:
*   **Streamable HTTP Support:** This enhances bidirectionality, crucial for agents to communicate with each other [02:39:57].
*   **Improved OAuth 2.1:** Initially a significant hurdle, the OAuth implementation was corrected through community feedback and contributions, allowing for enterprise-grade authorization [02:41:23].
*   **Registry API:** This future development will make it easier for models to discover [[model_context_protocol_mcp | MCPs]] not explicitly provided to them, further enhancing model agency [02:43:08].
*   **Elicitation:** Servers can now request more information from end-users, enabling dynamic interactions for tasks like flight booking, where user preferences (e.g., cheapest vs. fastest) can be clarified [02:42:30].
*   **Developer Experience:** Ongoing efforts include updating SDKs and improving the `inspector` debugging tool [02:42:06].

[[model_context_protocol_mcp | MCP]] facilitates "rich stateful interactions" [03:07:07], with features like:
*   **Dynamic Discovery:** Servers can dynamically reveal or hide tools based on context, as demonstrated by a game master agent revealing a "battle" tool only when a monster is present [03:09:43].
*   **Resources:** Allows servers to return references to files or data rather than the full content, which LLMs or users can then act upon [03:10:24]. This enables contextual understanding of environments (e.g., Python settings, installed packages) without constant prompting [03:10:56].
*   **Sampling:** Allows an [[model_context_protocol_mcp | MCP]] server to request LLM completions from the client, useful for summarizing resources or formatting web content into markdown [03:11:54].

## Adoption and [[integration_of_mcp_with_ai_applications | Integration with AI Applications]]
[[standardization_and_adoption_of_mcp | MCP's adoption]] is driven by its ability to simplify common integration problems for AI applications [02:54:13]. Microsoft, a presenting sponsor of the World's Fair, was an early adopter, integrating [[model_context_protocol_mcp | MCP]] with over 1500 tools [00:48:01] and supporting it across its platforms, including GitHub Copilot and Azure AI Foundry [00:49:35]. The Microsoft team highlighted how [[model_context_protocol_mcp | MCP]] and A2A (Agent-to-Agent protocol) are essential for building the "agentic web," where agents interact across different clouds, companies, and devices [03:08:04].

Anthropic itself uses [[model_context_protocol_mcp | MCP]] internally at scale to manage tool calling and integrations [02:50:47]. They developed an "MCP gateway" to provide a single point of entry for engineers, standardizing authentication, rate limiting, and observability [02:58:07]. This "pit of success" model makes the "right thing to do the easiest thing to do," ensuring consistent and secure integration [02:57:51].

Sentry also adopted [[model_context_protocol_mcp | MCP]] for its B2B SaaS business, focusing on integrating its application monitoring capabilities with agent architectures [03:21:06]. David Kramer, Sentry's founder, emphasized that [[model_context_protocol_mcp | MCP]] is not merely an API wrapper; it requires careful design to provide context to agents effectively [03:26:04].

## [[challenges_in_the_mcp_ecosystem | Challenges and Future Outlook]]
Despite rapid [[standardization_and_adoption_of_mcp | adoption]], the [[model_context_protocol_mcp | MCP]] ecosystem faces [[problems_faced_by_mcp_developers | problems]] and [[challenges_in_the_mcp_ecosystem | challenges]].

### [[problems_faced_by_mcp_developers | Problems Faced by Developers]]
*   **"Copy and Paste Hell":** Early AI products suffered from a lack of connectivity, forcing users to manually copy and paste between applications [02:30:00]. [[model_context_protocol_mcp | MCP]] aims to solve this by allowing AI to connect to the rest of the world [02:30:13].
*   **Initial Confusion:** At launch, many developers did not understand the need for a new open protocol when models could already call tools [02:36:40].
*   **"API Wrapper Syndrome":** Many early [[model_context_protocol_mcp | MCP]] implementations simply wrapped existing API endpoints one-to-one [02:45:41], leading to poor results because models struggle to reason about giant, undifferentiated JSON payloads [02:56:01]. A human-readable format like Markdown is often more effective [03:30:12].
*   **Client Support Gaps:** Inconsistent [[model_context_protocol_mcp | MCP]] support across different clients (e.g., IDEs, cloud desktops) [03:26:38]. While VS Code Insiders offers full OAuth and [[model_context_protocol_mcp | MCP]] support, other platforms may lag [03:28:56].
*   **Security Concerns:** The `standard IO` interface for [[model_context_protocol_mcp | MCP]] raises security concerns, including prompt injection risks [03:28:34]. Organizations are advised to trust only verified [[model_context_protocol_mcp | MCP]] tools [03:28:46]. The "lethal trifecta" arises when an AI system with access to private data is exposed to malicious instructions and has exfiltration mechanisms [01:42:36].
*   **Cost Management:** AI tool calls can become expensive if not carefully managed, especially with large token payloads [03:31:52].
*   **Debugging and Logging:** Developers have reported difficulties with debugging and logging [[model_context_protocol_mcp | MCP]] servers [03:13:17], though VS Code now offers a dev mode with console and debugger attachment [03:13:30].
*   **Lack of Streaming Responses for Tools:** A current limitation is the absence of streaming responses for tools, which complicates agent-to-agent communication and forces workarounds like polling [03:33:01].

### Opportunities and Future Direction
Despite the [[problems_faced_by_mcp_developers | problems]], the [[model_context_protocol_mcp | MCP]] ecosystem is still "really early" with massive opportunities [02:45:04].
*   **Higher Quality Servers:** There's a strong need for more, higher-quality [[model_context_protocol_mcp | MCP]] servers [02:45:37]. Building effective servers means designing for three users: the end-user, the client developer, and the model [02:46:01].
*   **Vertical Expansion:** While initial [[model_context_protocol_mcp | MCPs]] were often for developer tools, there's a desire for expansion into other verticals like sales, finance, legal, and education [02:46:31].
*   **Simplifying Server Building:** Given the anticipated proliferation of servers, tools to simplify their creation (hosting, testing, deployment, evaluation) are crucial for both enterprises and indie developers [02:46:52].
*   **Automated [[model_context_protocol_mcp | MCP]] Generation:** A moonshot vision suggests that as model intelligence grows, they will be able to write their own [[model_context_protocol_mcp | MCPs]] on the fly [02:47:44].
*   **AI Security Tooling:** Investment in AI security, observability, and auditing tools is critical as [[model_context_protocol_mcp | MCP]] enables applications to interact with real-world data [02:48:25].
*   **Community Registry:** Efforts are underway to create a community registry for easier discovery of [[model_context_protocol_mcp | MCP]] servers [03:15:32].
*   **Agent-Centric Development:** The overarching advice is to focus on building agents, treating [[model_context_protocol_mcp | MCP]] as a pluggable architecture for these services [03:32:41]. This approach emphasizes designing for context within specific workflows, allowing for greater control over model interactions and results [03:32:50].

The vision for [[model_context_protocol_mcp | MCP]] is to enable a transformative potential for AI applications by ensuring the ecosystem catches up to the capabilities already outlined in the protocol's specification [03:18:11].