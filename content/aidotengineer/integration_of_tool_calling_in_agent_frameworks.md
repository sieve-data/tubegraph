---
title: Integration of tool calling in agent frameworks
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

[[ai_integration_and_tool_calling | Tool calling]] is more than just "plumbing" for [[ai_agents_and_agentic_workflows | AI agents]]; it is a crucial component that deserves more attention and can significantly enhance the flexibility and robustness of [[ai_agents_and_agentic_workflows | agentic frameworks]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While much focus has been placed on improving the [[ai_agents_and_agentic_workflows | agents]] themselves, there's a growing need to build reusable, robust tools that can be integrated into various [[ai_agents_and_agentic_workflows | agentic frameworks]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

The application layer, particularly where tools are built, requires more focus as it offers significant opportunities for improvement on top of advancing large language models (LLMs) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Understanding Tool Calling

In a typical [[ai_agents_and_agentic_workflows | agent]] loop, a user asks a question or sends a prompt to the [[ai_agents_and_agentic_workflows | agent]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This [[ai_agents_and_agentic_workflows | agent]] utilizes LLMs and memory, and critically, tools <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

For instance, if an [[ai_agents_and_agentic_workflows | agent]] is asked "how far does the moon orbit expressed as the number of trips between Amsterdam and San Francisco?", it might use a series of tool calls <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>:
1.  Search for the distance between the Earth and the Moon <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
2.  Search for the distance between Amsterdam and San Francisco <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
3.  Perform calculations, possibly using another tool or the LLM itself <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

These tool calls often involve external APIs (e.g., web search, databases) or internal functions (e.g., JavaScript, Python for calculations) <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Defining Tools
The definition of a tool is crucial and includes:
*   **Tool Name**: Advised to keep simple <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Tool Description**: Acts almost like a system prompt for the LLM, guiding its usage of the tool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Longer descriptions are common for more complex, "agentic" tools <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Input Parameters**: Specifies what is needed to call the tool <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Output Schema**: Becoming increasingly important for type safety and structured outputs, especially when chaining tool calls or building complex [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. This allows models to understand the data returned and chain calls effectively <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Evolution of Tool Calling Integration

Historically, [[ai_agents_and_agentic_workflows | agent]] development often meant embedding tool logic directly within the [[ai_agents_and_agentic_workflows | agent framework]].

### Traditional Tool Calling
In what is now considered "traditional" tool calling, the tool logic is intertwined with the [[ai_agents_and_agentic_workflows | agent]]'s application logic <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   A client application sends a prompt to the [[ai_agents_and_agentic_workflows | agent]] or [[ai_agents_and_agentic_workflows | AI application]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   The [[ai_agents_and_agentic_workflows | agent]] sends the prompt to the LLM <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   The LLM recommends a tool call <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   The application explicitly defines and handles the tool call logic, including parsing the LLM's recommendation, executing the tool via a callback function, and managing queuing, retries, and errors <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   This creates a significant back-and-forth between the application logic and the LLM, making it less of a closed system <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. An example in LangChain would involve explicitly filtering tool call messages and executing them <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Embedded Tool Calling
Most modern [[ai_agents_and_agentic_workflows | agent frameworks]] today utilize what is called "embedded" tool calling, where the system acts as a closed black box <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   The client app sends a question to the [[ai_agents_and_agentic_workflows | agent]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   The [[ai_agents_and_agentic_workflows | agent]] is a self-contained system, connecting with the LLM and the tools, handling all tool calling internally <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   The tool definitions and logic are defined within the same [[ai_agents_and_agentic_workflows | agent framework]] <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   The application sends a prompt and tools, and an answer is returned, with no control over the internal tool calling process <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   While easier to implement for beginners as it handles errors and retries, it offers no control over the tool calling process or decision-making <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Promoting Separation of Concerns

As a developer, a preference for separation of concerns is ideal, preventing tightly coupled systems <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This applies to [[ai_agents_and_agentic_workflows | agentic workflows]] as well.

### Model Context Protocol (MCP)
The Model Context Protocol (MCP), introduced by Anthropic and adopted by others, is a significant step towards separating client-side and server-side logic in [[ai_agents_and_agentic_workflows | agentic applications]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   MCP defines a "host" (e.g., a desktop client) that contains a "client" <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   This client connects to "servers," which are backend systems with access to tools or assets like data files <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   The host/client only sees the server, not the tools directly, as the tools are made available through the server <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   The MCP server handles the logic, defining and importing tools, while the MCP host and client understand how to call these servers <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   This provides a clear distinction between the "front side" (host/client) and "back side" (server with tools) of the system <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Standalone Tool Platforms
A more advanced approach is to use standalone tool platforms, which are gaining market attention <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   Instead of defining tools within a closed [[ai_agents_and_agentic_workflows | agent loop]], tools are defined separately on remote servers <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   The [[ai_agents_and_agentic_workflows | agentic framework]] imports these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   The tool creation, hosting, and execution are entirely separate from the [[ai_agents_and_agentic_workflows | agent]] <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
*   The [[ai_agents_and_agentic_workflows | agent]]'s role is to take the tool definition, use the LLM to decide which tool to call, and pass this to the tool platform for execution <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   These platforms often allow for chaining tools, handling authorization, and managing errors <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   This separation provides significant flexibility, allowing developers to build tools once and use them across different [[ai_agents_and_agentic_workflows | agentic frameworks]] like LangChain, LangGraph, CrewAI, or Autogen <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   Examples of tool platforms include Compos, Toolhouse, Arcade AI, and Wild Card <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

## Dynamic Tools

Rather than creating a multitude of static tools for every possible operation (e.g., a separate tool for each type of customer query), dynamic tools leverage LLMs to generate queries for existing APIs or databases <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.
*   A dynamic tool can connect to a GraphQL schema or SQL database <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.
*   Instead of passing fixed arguments, the LLM is instructed to generate a valid GraphQL query or SQL command based on the provided schema and available operations <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.
*   LLMs, especially models like Llama, OpenAI models, and Claude, show strong capabilities in generating GraphQL when provided with a clear schema <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>. Simplifications like avoiding custom scalars or deep nesting can improve performance <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.
*   This approach significantly reduces the need to define numerous individual tools and allows for direct integration of existing business logic <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
*   However, a trade-off exists: LLMs can sometimes hallucinate or generate incorrect syntax, leading to errors <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Despite this, there's a strong future for dynamic tools over static ones <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

## Conclusion
Ultimately, an [[ai_agents_and_agentic_workflows | agent]] is only as good as its tools <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Ensuring that tools are reusable, robust, and easily integrated into different [[ai_agents_and_agentic_workflows | agentic frameworks]] is paramount for [[building_effective_agents | building effective agents]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The shift towards separation of concerns, utilizing protocols like MCP, and adopting standalone tool platforms or dynamic tool generation will drive greater flexibility and capability in [[ai_agents_and_agentic_workflows | AI agent]] development <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.