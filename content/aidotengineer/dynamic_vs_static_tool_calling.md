---
title: Dynamic vs static tool calling
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

Tool calling is considered more important than just "plumbing" for AI agents, as it underpins the capabilities of these agents <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While much attention has been given to improving AI agents, there has historically been less focus on building reusable and robust tools for them <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The application layer, particularly where tools are built, deserves more attention to catch up with advancements in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

An agent's effectiveness is directly tied to the quality of its tools <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Tools must be reusable and robust, enabling them to be integrated into various agent frameworks <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

A typical tool definition includes:
*   A simple tool name <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   A tool description, which acts like a system prompt for the LLM <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Input parameters for the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   An output schema, which is increasingly important for type safety and chaining complex tool calls for structured outputs <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

## Static Tool Calling

Static tool calling refers to methods where tools are either tightly coupled with the agent framework or operate as a "black box" without external query generation by the LLM.

### Traditional Tool Calling

In traditional tool calling, the client application interacts with an agent or AI application, which then prompts the LLM <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The LLM suggests tool calls, but the actual tool execution logic (parsing, filtering, calling tools, handling retries and errors) resides within the server-side application or agent <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>, <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This involves a lot of back-and-forth between the application and the LLM <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

For instance, in LangChain, this involves explicitly looking for tool call messages from the LLM, parsing them, and executing them via a callback function <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Embedded Tool Calling

Embedded tool calling, often a more recent evolution, makes the agent a closed system <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. The client application only asks a question, and the agent, having the tools and connecting with the LLM, handles all tool calling internally as a black box <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

*   **Advantages**: Easy to implement for beginners as it abstracts away error handling, retries, and queuing <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Disadvantages**: Limited control over the tool calling process, execution details, or decision-making <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

## Dynamic Tool Calling

[[developing_and_using_software_automation_tools | Dynamic tool calling]] involves giving the LLM the ability to generate queries for existing APIs or databases directly, rather than defining a separate static tool for every specific operation <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

Instead of needing millions of tools, or even hundreds that could confuse an agent, dynamic tools offer a solution <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. For example, by connecting to a GraphQL schema or SQL database, the LLM can generate the necessary query (e.g., a GraphQL query) based on the user's request <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>, <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.

*   **Process**: The model is given a tool that can connect to a GraphQL or SQL schema. It's prompted to generate valid queries. By providing the schema, the model understands the available types and operations <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **LLM Capabilities**: Models like Llama, OpenAI models, and Claude are adept at generating GraphQL, provided the schema isn't overly complex (e.g., avoiding custom scalars or deep nesting) <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.
*   **Advantages**: Reduces the need to define numerous individual tools, allows direct use of existing business logic, and offers greater flexibility <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>, <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
*   **Trade-offs**: LLMs might hallucinate or mess up syntax, leading to inconsistent query generation <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

## Architectures Supporting Flexibility

Developers often seek [[separation_of_concerns_in_agent_and_tool_frameworks | separation of concerns]] to keep systems more manageable and flexible <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### [[model_context_protocol_and_tool_integration | Model Context Protocol (MCP)]]

The [[model_context_protocol_and_tool_integration | Model Context Protocol (MCP)]], introduced by Anthropic, aims to separate client-side and server-side logic in agentic applications <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. In this model:
*   A "host" (e.g., a desktop client) contains the client <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   "Servers" act as backends that have access to tools or assets like data files <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   The client interacts with the server, which handles tool invocation, providing a clear distinction between front-end and back-end responsibilities <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Standalone Tool Platforms

A standalone tool platform defines and hosts tools separately from the agent framework <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. The agent framework then imports or connects to these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This means [[challenges_and_considerations_in_tool_creation_and_execution | tool creation and execution]] are decoupled <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

These platforms typically offer:
*   A place to create tools (via code or CLIs) <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
*   A place to execute or surface tools (via SDKs that connect to frameworks like LangChain or CrewAI) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   Capabilities like chaining tools (e.g., retrieving a country based on IP, then querying a CRM for customers in that country) <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   Centralized handling of authorization, authentication, and errors for various underlying systems <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

[[using_tools_and_function_calling_in_ai_sdk | Using tools and function calling in AI SDK]]s provided by these platforms allows for significant flexibility <a class="yt-timestamp" data-t="00:19:58">[00:19:58]</a>. Agents can easily switch between different frameworks (e.g., LangChain, LangGraph, CrewAI, Autogen) without rebuilding tools, as the tools are built once and imported <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. The agent decides what tool to call, but the actual execution is handled by the remote tool platform <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>. This approach promotes [[separation_of_concerns_in_agent_and_tool_frameworks | separation of concerns]], with tools in one place and the agent in another <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

Examples of such platforms include Compos, Tool House, Arcade AI, and Wild Card <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. IBM is also building a similar platform called WX Flow <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

Ultimately, the [[importance_of_tool_calling_in_ai | importance of tool calling in AI]] cannot be overstated; tools are as critical as the agents themselves <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.