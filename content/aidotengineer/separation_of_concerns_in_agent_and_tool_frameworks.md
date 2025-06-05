---
title: Separation of concerns in agent and tool frameworks
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

Tool calling is considered more important than just "plumbing" for [[agentic_frameworks_and_tool_integration | AI agents]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While significant effort is often spent on improving agents, less attention has historically been paid to building reusable and robust tools that can be integrated into different frameworks <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, this trend is changing, with more tool platforms and libraries emerging <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The application layer, particularly where tools are built, deserves more attention <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## The Importance of Tools

Tools are essential components of an agent's loop, alongside the large language model (LLM) and memory <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The agent is only as good as its tools <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Problems often arise with tool integration, such as the LLM incorrectly calling or using a tool, or issues within the tool itself <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Therefore, ensuring tools are reusable and robust is crucial for flexibility, allowing them to be brought into any [[agentic_frameworks_and_tool_integration | agentic framework]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Defining Tools

A typical tool definition includes:
*   **Tool Name:** Advised to be kept simple <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Tool Description:** Functions almost like a system prompt for the LLM, often being quite extensive for more complex tools <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Input Parameters:** Necessary for the model to know what is needed to call the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Output Schema:** Increasingly important for type safety, structured outputs, and chaining tool calls <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Evolution of Tool Calling Architectures

### Traditional Tool Calling

In "traditional tool calling," the client application sends a prompt to an AI application (agent). This application then sends the prompt to the LLM, which recommends tool calls. The application itself handles the logic of parsing these recommendations, executing the tools, and managing responses, retries, and errors <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This approach involves a significant amount of back-and-forth between the application logic and the LLM, and between the client app and the agent <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Embedded Tool Calling

More recent frameworks often use "embedded tool calling," where the system acts as a closed circuit. The client app sends a question to the agent, which is a black box. The agent handles all tool calling logic internally, connecting with the LLM and the tools, and then returns the final answer <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. While easier to implement initially as it abstracts away error handling and retries, it offers little control over the tool calling process or decision-making <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The tools are defined within the same agent framework <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

## Achieving Separation of Concerns

A key principle in software development, including [[building_ai_agents_without_frameworks | AI agent engineering]], is the separation of concerns <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This allows for flexibility and easier management of different system parts.

### [[model_context_protocol_and_tool_integration | Model Context Protocol (MCP)]]

The [[model_context_protocol_and_tool_integration | Model Context Protocol (MCP)]], introduced by Anthropic, is a step towards separating client-side and server-side logic in [[agentic_frameworks_and_tool_integration | agentic applications]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Host/Client:** This side connects to servers and doesn't directly see the tools <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Server:** Acts as a backend with access to tools or assets (like data files), handling the logic and tool definitions <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

This clear distinction between the front-end and back-end logic is beneficial for managing [[integration_of_ai_coding_agents_with_thirdparty_tools | AI coding agents with third-party tools]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Standalone Tool Platforms

A standalone tool platform defines and hosts tools separately from the [[agentic_frameworks_and_tool_integration | agentic framework]] <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   **Tool Creation:** Done via code or CLIs <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Tool Execution/Surfacing:** Handled via SDKs that connect to [[agentic_frameworks_and_tool_integration | agentic frameworks]] like LangChain, Crew AI, or Autogen <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

This setup allows the agent to decide which tool to call based on the LLM's recommendation, then pass the execution to the remote tool platform <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
Benefits include:
*   **Centralized Tool Management:** Tools can be created from existing APIs or databases <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Tool Chaining:** Allows for sequencing multiple tool calls within the platform <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   **Authorization and Error Handling:** These concerns can be managed directly by the platform, reducing complexity within the agent <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Flexibility:** Building tools once on a platform allows for easy integration into different [[agentic_frameworks_and_tool_integration | agentic frameworks]], promoting framework independence <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

Examples of such platforms include Compos Tool House, Arcade AI, and WildCard <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

### Dynamic Tools

Instead of creating numerous static tools for every specific function (e.g., separate tools for getting customer count by country, orders, etc.), dynamic tools connect to a schema (like GraphQL or SQL) and allow the LLM to generate the specific query <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   The LLM is provided with the tool definition and the schema (e.g., GraphQL schema) and is instructed to generate valid queries <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
*   Models like Llama, OpenAI models, and Claude are adept at generating GraphQL queries when given a schema, provided the schema isn't overly complex (e.g., deep nesting, custom scalars) <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
*   This approach leverages existing business logic and APIs, reducing the need to define 20 different tools and duplicate logic <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

However, a trade-off is the potential for LLM hallucination, where the model might generate incorrect queries <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. Despite this, [[different_architectures_for_ai_agents | dynamic tools]] represent a promising future for [[multiagent_systems_in_technical_workflows | AI agents]] <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.