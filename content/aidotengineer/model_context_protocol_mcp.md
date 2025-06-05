---
title: Model Context Protocol MCP
videoId: z4zXicOAF28
---

From: [[aidotengineer]] <br/> 

[[introduction_to_model_context_protocol_mcp | Model Context Protocol (MCP)]] is an open-source, standardized protocol designed to connect AI with the external world, enabling models to interact with tools and access context beyond their immediate environment <a class="yt-timestamp" data-t="02:34:21">[02:34:21]</a>. It addresses the "copy and paste hell" that users and AI products faced when AI was not connected to the rest of the world <a class="yt-timestamp" data-t="02:30:07">[02:30:07]</a>.

## Origin and Motivation

The concept of MCP arose in mid-2024 from David and Justin, the co-creators at Anthropic, who observed the constant need to copy and paste context from external sources like Slack messages or error logs (e.g., Sentry) into a model's context window <a class="yt-timestamp" data-t="02:33:09">[02:33:09]</a>. This led to the fundamental question: How can a model "climb out of its box," reach into the real world, and retrieve necessary context and actions? <a class="yt-timestamp" data-t="02:33:52">[02:33:52]</a>

The core idea was to address model agency – giving models the ability to interact with the outside world <a class="yt-timestamp" data-t="02:34:06">[02:34:06]</a>. For this to scale, it had to be an open-source, standardized protocol <a class="yt-timestamp" data-t="02:34:21">[02:34:21]</a>. This was crucial because proprietary ecosystems require complex business development and alignment on interfaces for integration <a class="yt-timestamp" data-t="02:34:42">[02:34:42]</a>. As reasoning models improved and tool calling became more effective, it was essential to allow wider participation in this ecosystem <a class="yt-timestamp" data-t="02:35:12">[02:35:12]</a>.

A small internal "tiger team" at Anthropic developed MCP, which was launched during the company's hack week in November 2024 <a class="yt-timestamp" data-t="02:35:28">[02:35:28]</a>. This internal launch went viral, with engineers automating workflows using MCPs <a class="yt-timestamp" data-t="02:35:41">[02:35:41]</a>, ultimately leading to its open-source release in November 2024 <a class="yt-timestamp" data-t="02:36:08">[02:36:08]</a>.

## Technical Structure and Features

The [[technical_structure_and_features_of_mcp | MCP specification]] includes:
*   **JSON RPC Specification:** A standard way of sending messages and communicating between context providers and code interacting with models <a class="yt-timestamp" data-t="02:52:38">[02:52:38]</a>.
*   **Global Transport Standard:** Deals with aspects like streamable HTTP, OAuth 2.1, and session management for universal communication <a class="yt-timestamp" data-t="02:53:02">[02:53:02]</a>.
*   **Tools:** Reflect actions and are mostly easy to map to function calling <a class="yt-timestamp" data-t="03:07:17">[03:07:17]</a>. While powerful, too many tools or tools from too many domains can confuse AI <a class="yt-timestamp" data-t="03:07:52">[03:07:52]</a>.
*   **Resources:** Provide a semantic layer to return references to files or data, rather than large direct files, allowing LLMs to follow up on them or users to act upon them <a class="yt-timestamp" data-t="03:10:30">[03:10:30]</a>.
*   **Prompts:** Used in the protocol to guide model behavior <a class="yt-timestamp" data-t="03:05:28">[03:05:28]</a>.
*   **Sampling:** Allows a server to request LLM completions from the client <a class="yt-timestamp" data-t="03:11:55">[03:11:55]</a>. This is a progressive enhancement for tasks like summarizing resources or formatting web content <a class="yt-timestamp" data-t="03:12:26">[03:12:26]</a>.
*   **Elicitation:** Enables servers to ask for more information from end-users, for instance, to clarify "best flight" as "cheapest" or "fastest" <a class="yt-timestamp" data-t="02:42:30">[02:42:30]</a>. This adds more statefulness to tools <a class="yt-timestamp" data-t="03:16:30">[03:16:30]</a>.
*   **Dynamic Discovery:** Allows a server to dynamically offer new tools to the client, depending on context (e.g., a "battle" tool appearing only when a monster is present in a game) <a class="yt-timestamp" data-t="03:09:16">[03:09:16]</a>.
*   **Roots:** Similar to dynamic discovery, new roots can be sent as the client's workspace changes <a class="yt-timestamp" data-t="03:12:49">[03:12:49]</a>.

## Adoption and Impact

Initially, there was confusion about MCP's purpose and its necessity given existing tool-calling capabilities <a class="yt-timestamp" data-t="02:36:38">[02:36:38]</a>. The turning point for widespread adoption occurred when Cursor adopted MCP, followed by other coding tools like VS Code and Sourcegraph <a class="yt-timestamp" data-t="02:37:18">[02:37:18]</a>. More recently, major AI labs including Google, Microsoft, and OpenAI have also adopted MCP, making it increasingly standard <a class="yt-timestamp" data-t="02:37:50">[02:37:50]</a>.

As an [[model_context_protocol_and_tool_integration | industry standard]], MCP simplifies development by providing a single approach for engineers, allowing them to focus on unique problems rather than plumbing integrations <a class="yt-timestamp" data-t="02:54:30">[02:54:30]</a>. Its design preemptively solves common problems, such as integrating different billing models or managing token limits through sampling primitives <a class="yt-timestamp" data-t="02:55:54">[02:55:54]</a>.

For organizations, MCP facilitates building integrations once and using them anywhere, promoting portability of credentials and centralized auditing <a class="yt-timestamp" data-t="02:57:42">[02:57:42]</a>. For example, Anthropic uses an "MCP gateway" as shared infrastructure to provide a single entry point for various services, handling credential management and rate limiting <a class="yt-timestamp" data-t="02:58:07">[02:58:07]</a>.

The rise of MCP signifies a fundamental shift in the internet's economy, where tool calls are becoming the "new clicks" <a class="yt-timestamp" data-t="02:31:05">[02:31:05]</a>.

## Challenges and Considerations

Despite its benefits, [[integrating_ai_with_applications_using_model_context_protocol_mcp | integrating AI with applications using Model Context Protocol MCP]] presents challenges:
*   **OAUTH 2.1 Implementation:** While standard, some developers find it complex, with limited support among providers <a class="yt-timestamp" data-t="03:25:10">[03:25:10]</a>. However, it allows for enterprise-grade authorization <a class="yt-timestamp" data-t="03:14:47">[03:14:47]</a>.
*   **API Wrapper Syndrome:** A common mistake is simply wrapping existing APIs as MCP tools. This leads to poor results because models struggle to reason about giant, undifferentiated JSON payloads <a class="yt-timestamp" data-t="03:25:57">[03:25:57]</a>. MCP tools should be designed with the model and end-user in mind, treating the model as a user and focusing on clear, structured output (e.g., Markdown) <a class="yt-timestamp" data-t="02:46:04">[02:46:04]</a>.
*   **Client Support:** Not all clients fully support the MCP specification, leading to inconsistencies. Continuous updates and feedback from the community are crucial to close this "interoperability gap" <a class="yt-timestamp" data-t="03:17:05">[03:17:05]</a>.
*   **Debugging and Logging:** Early development can be challenging due to difficulties in debugging and logging MCP server interactions <a class="yt-timestamp" data-t="03:13:17">[03:13:17]</a>. Tools like `inspector` and VS Code's dev mode are being developed to improve this <a class="yt-timestamp" data-t="02:42:14">[02:42:14]</a>.
*   **Cost Management:** Since the client often bears the cost, developers need to be mindful of token usage when designing tools <a class="yt-timestamp" data-t="03:31:52">[03:31:52]</a>.
*   **Security:** Deploying random MCP tools in an organization is risky due to prompt injection vulnerabilities and the potential for exfiltrating private data <a class="yt-timestamp" data-t="03:28:40">[03:28:40]</a>. Strong security, observability, and auditing measures are essential <a class="yt-timestamp" data-t="02:48:25">[02:48:25]</a>.

## Future Outlook

The [[future_developments_and_roadmap_for_mcp | future developments and roadmap for mCP]] are focused on enhancing agent experience and simplifying server building:
*   **Agent Experience:** Focus on features like elicitation to allow servers to request more information from users <a class="yt-timestamp" data-t="02:42:24">[02:42:24]</a>.
*   **Registry API:** Will make it easier for models to find MCPs that weren't initially provided, furthering model agency <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>.
*   **Developer Experience:** Continued efforts to provide open-source examples and best practices for building MCPs <a class="yt-timestamp" data-t="02:43:28">[02:43:28]</a>.
*   **Server Building Simplification:** More tools for hosting, testing, and evaluation of MCP servers, for both enterprises and indie developers <a class="yt-timestamp" data-t="02:46:52">[02:46:52]</a>.
*   **Automated MCP Server Generation:** A "moonshot" goal where models might eventually be able to write their own MCPs dynamically <a class="yt-timestamp" data-t="02:47:40">[02:47:40]</a>.
*   **Openness and Governance:** Ensuring MCP remains an open standard forever, with ongoing investment in its governance <a class="yt-timestamp" data-t="02:43:54">[02:43:54]</a>.

The vision for MCP is to enable rich, stateful interactions between agents, leveraging the full specification beyond just simple tool calls <a class="yt-timestamp" data-t="03:07:09">[03:07:09]</a>. This includes using resources for semantic layers, dynamic discovery, and sampling for progressive enhancements <a class="yt-timestamp" data-t="03:10:47">[03:10:47]</a>. The ultimate goal is to enable the development of "action-oriented, context-aware, semantic-aware servers" using the full potential of the protocol <a class="yt-timestamp" data-t="03:17:23">[03:17:23]</a>.