---
title: Agentic frameworks and tool integration
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 
This article discusses the importance of tool calling in [[agentic_frameworks_and_their_applications | AI agents]], emphasizing that it is more than just "plumbing" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The goal is to empower users to build their own tools, separate from [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic frameworks]], to achieve greater flexibility <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

### The Overlooked Importance of Tools
While much attention is given to improving [[agentic frameworks and orchestration layers in AI engineering | agents]], less time has historically been spent on building reusable and robust tools that can be integrated into different frameworks <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. However, this is changing, with more tool platforms and libraries emerging <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. The general sentiment is shifting, recognizing that the "pressure is sort of off the [[agentic frameworks and orchestration layers in AI engineering | agents]]" as people are now trying to improve the tools <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

An agent's effectiveness is directly tied to the quality of its tools <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Frameworks offer significant support for agents but less for tool development itself <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. The application layer, specifically where tools are built, deserves more attention as large language models (LLMs) continue to advance <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

### Understanding Tool Calling
Tool calling allows an [[agentic frameworks and orchestration layers in AI engineering | agent]] to answer complex questions by performing a series of actions, such as calculating the distance of the moon's orbit in terms of trips between two cities <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. While an LLM might sometimes generate an answer directly from its training data <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>, it more commonly uses tool calls to:
*   Search for external information (e.g., distance between Earth and Moon, or cities) via web searches or geographical databases <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
*   Perform calculations using internal functions (e.g., JavaScript, Python) or external APIs (e.g., Wolfram Alpha) <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.

#### Defining Tools
The definition of a tool significantly impacts its utility. Key components include:
*   **Tool Name**: Advised to keep simple <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
*   **Tool Description**: Acts like a system prompt for the LLM, guiding its usage. Larger, more [[agentic frameworks and orchestration layers in ai engineering | agentic tools]] often have detailed descriptions <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   **Input Parameters**: Specifies what the model needs to provide to call the tool <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Output Schema**: An increasingly important feature in [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic frameworks]], allowing for type safety, structured outputs, and chaining of tool calls <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. Without an output schema, the model relies on a string return, making complex sequences difficult to manage <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

### Evolution of Tool Calling within Agent Frameworks
The way tools are called within [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks]] has evolved.

#### Traditional Tool Calling
This approach involves significant back-and-forth communication between the client application, the agent/AI application, and the large language model <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.
*   The client sends a prompt to the agent application <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   The agent application constructs a prompt and sends it to the LLM <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.
*   The LLM recommends a tool call, and the application must explicitly parse and execute these tool call messages based on defined callback functions <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
*   The tool response is sent back to the model, and this process repeats until an answer is formed <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

This method, common in earlier [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic]] implementations, requires manual handling of tool queuing, retries, and errors <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

#### Embedded Tool Calling (Black Box)
This is the prevailing approach in many modern [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | frameworks]] today, where the system acts as a closed circuit <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.
*   The client application simply sends a question to the agent <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.
*   The agent, which is a closed system, handles all interactions with the LLM and the tools internally, performing the tool calls and returning the final answer <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.
*   The tool calling logic is entirely managed by the [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agent framework]], acting as a black box <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

While easier to implement for beginners as it abstracts away error handling and retries <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>, embedded tool calling offers limited control over the tool calling process, how decisions are made, or the output format <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>.

### Separation of Concerns in Agent and Tool Frameworks
A preference for [[separation_of_concerns_in_agent_and_tool_frameworks | separation of concerns]] in software development leads to a desire for more distinct systems for agents and tools <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.

#### [[model_context_protocol_and_tool_integration | Model Context Protocol (MCP)]]
The [[model_context_protocol_and_tool_integration | Model Context Protocol]] (MCP), introduced by Anthropic and adopted by many, is a significant step towards separating client-side and server-side components in [[agentic_enterprise_and_ai_agents | agentic applications]] <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.
*   A "host" (e.g., Cloud Desktop) with a client connects to "servers" <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.
*   These servers act as backends that have access to tools or assets like data files <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
*   The host/client interacts only with the server, not directly with the tools <a class="yt-timestamp" data-t="15:29:00">[15:29:00]</a>.
*   The MCP server handles the logic, tool definition, and tool imports, providing a clear distinction between frontend and backend concerns <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>.

#### Standalone Tool Platforms
A growing trend is the use of standalone tool platforms, which offer greater flexibility by separating tool creation and hosting from the [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic framework]] <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.
*   Tools are defined and hosted on remote servers <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.
*   The [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic framework]] imports these tools via SDKs or API calls <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>.
*   The [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agent]] decides which tool to call using the LLM and then passes the request to the tool platform for execution <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.
*   These platforms often allow for chaining of tools (e.g., getting a user's country then finding customers in that country) <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a> and handle authorization and error management <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   This separation allows developers to build tools once and use them across different [[agentic_frameworks_and_orchestration_layers_in_ai_engineering | agentic frameworks]] (e.g., LangChain, CrewAI, AutoGen) <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>.
*   Examples of such platforms include IBM's WX Flow, Compos Tool House, Arcade AI, and Wild Card <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.

### Dynamic Tools
Instead of creating a separate static tool for every function or query (e.g., a million tools for a CRM with various filters and data types) <a class="yt-timestamp" data-t="21:35:00">[21:35:00]</a>, [[integration_of_ai_coding_agents_with_thirdparty_tools | dynamic tools]] offer a more flexible approach <a class="yt-timestamp" data-t="22:29:00">[22:29:00]</a>.
*   A single dynamic tool can connect to an API schema (like GraphQL) or a database (like SQL) <a class="yt-timestamp" data-t="22:38:00">[22:38:00]</a>.
*   The LLM is then instructed to generate the appropriate query (e.g., GraphQL query) based on the provided schema and user request <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>.
*   Models like Llama, OpenAI, and Claude are adept at generating valid GraphQL queries when provided with the schema, though complex features like custom scalars or deep nesting can cause issues <a class="yt-timestamp" data-t="23:29:00">[23:29:00]</a>.

This approach reduces implementation effort in downstream integration and avoids duplicating business logic <a class="yt-timestamp" data-t="24:18:00">[24:18:00]</a>. However, there are trade-offs, as LLMs can hallucinate, leading to poorly formed queries <a class="yt-timestamp" data-t="24:37:00">[24:37:00]</a>. Despite this, [[integration_of_ai_coding_agents_with_thirdparty_tools | dynamic tools]] represent a significant future direction compared to static tools <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>.

In conclusion, as [[agentic architectures and systems design | AI agents]] become more prevalent, it is crucial to recognize and prioritize the development of robust, reusable tools, ensuring they are as important as the agents themselves <a class="yt-timestamp" data-t="24:58:00">[24:58:00]</a>.