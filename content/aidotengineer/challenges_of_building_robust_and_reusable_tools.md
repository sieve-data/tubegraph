---
title: Challenges of building robust and reusable tools
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

While much attention is given to improving AI agents, the development of robust and reusable tools for these agents is often overlooked <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This oversight can lead to significant issues, as an agent's effectiveness is often limited by the quality of its tools <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## The Overlooked Importance of Tools

Developers frequently focus on enhancing agents but spend less time on building tools that are reusable, robust, and adaptable across different frameworks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The application layer, specifically where tools are constructed, merits increased focus <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Often, the first component to fail in an agent is its tools <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Issues can include:
*   The Large Language Model (LLM) failing to call a tool correctly <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   The LLM using the incorrect tool <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   Internal failures within the tool itself <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Agents are seen as closed circuits, whereas tools are more dynamic <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Therefore, the agent is only as effective as the tools it employs <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Key Aspects of Tool Definition
The definition of a tool is crucial for its functionality and reusability:
*   **Tool Name**: Should be kept simple <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Tool Description**: Acts almost like a system prompt for the LLM, guiding its usage <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Longer, more detailed descriptions are common in larger, "agentic" tools <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Input Parameters**: Inform the model what is required to call the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Output Schema**: Increasingly vital, it enables type safety, structured outputs, and the chaining of tool calls <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Without it, the model may not know what data is returned <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Tool Calling Paradigms and Their Impact on Reusability

Understanding where a tool is called from is becoming increasingly important <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Tools are often built and defined in the same place as the agents themselves <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Traditional Tool Calling
In a traditional setup, the client application sends a prompt to an agent or AI application, which then passes it to the LLM <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The LLM recommends tool calls, and the application's server-side logic defines and executes these tools based on the LLM's recommendations <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This involves:
*   Explicitly looking for tool call messages from the LLM <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Parsing and executing the messages based on callback functions <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   Handling tool call queuing, retries, and errors <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

This method involves significant back-and-forth between the application logic and the LLM, making it less of a "closed system" <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. While it offers more control over the tool calling process, it places the burden of managing complex logic on the developer <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Embedded Tool Calling
Most modern frameworks utilize embedded tool calling, where the agent acts as a black box <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The client application simply asks a question, and the agent, as a self-contained system, handles all tool connections, LLM interactions, and tool calls internally, returning only the final answer <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   Tool definitions are contained within the agent <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   It is easier to implement for beginners as it abstracts away error handling and retries <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   However, it offers no control over the tool calling process, execution decisions, or data format beyond the initial callback function <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. This lack of control limits reusability, as tools are tightly coupled to the agent framework.

## Strategies for Building Reusable and Robust Tools

To overcome the challenges of tightly coupled tools and enhance reusability, several architectural strategies can be employed.

### Separation of Concerns
Adopting a "separation of concerns" approach, akin to decoupling backend and frontend in web development, is beneficial <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This means keeping different parts of your system distinct, even if they reside in the same repository <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

#### [[reducing_complexity_of_creative_tools_with_mcp | Model Context Protocol (MCP)]]
The [[reducing_complexity_of_creative_tools_with_mcp | Model Context Protocol (MCP)]], introduced by Anthropic, facilitates the separation of client-side (host) and server-side components in agentic applications <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   The host (e.g., desktop client) contains a client that connects to servers <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   Servers act as backends, providing access to tools or data files <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   The host/client interacts with the server, but does not directly see the tools, which are made available through the server <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   Tool logic and definitions are managed on the [[reducing_complexity_of_creative_tools_with_mcp | MCP]] server, allowing for a clear distinction between front-end and back-end logic <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. This approach makes tool calling truly separate from the agentic framework <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

#### [[emergence_of_standalone_tool_platforms_and_dynamic_tools | Standalone Tool Platforms]]
[[emergence_of_standalone_tool_platforms_and_dynamic_tools | Standalone tool platforms]] offer a more distinct separation. Instead of defining tools within a closed agent loop, they are defined separately, often hosted on remote servers <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   The agent imports these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   Tool creation and execution are handled independently <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
*   The agent's role is to take the tool definition, use the LLM to decide which tool to call, and pass this decision to the [[emergence_of_standalone_tool_platforms_and_dynamic_tools | tool platform]] for execution <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   These platforms often allow for chaining tools, handling authorization, and managing errors <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   This separation provides significant flexibility, allowing developers to build tools once and use them across different agent frameworks (e.g., LangChain, CrewAI, AutoGen) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. This means a developer can swap agent frameworks without rebuilding their toolset <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.

#### [[emergence_of_standalone_tool_platforms_and_dynamic_tools | Dynamic Tools]] (e.g., using GraphQL or SQL)
Rather than creating numerous static tools for every specific function (e.g., a separate tool for each customer search filter in a CRM), [[emergence_of_standalone_tool_platforms_and_dynamic_tools | dynamic tools]] leverage query languages like GraphQL or SQL <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
*   A single dynamic tool can connect to a GraphQL schema or a database <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   The LLM generates the specific query (e.g., GraphQL query) based on the user's request and the provided schema <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   The LLM is given the tool and the schema, understanding that it needs to generate a valid query <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
*   This approach reduces the number of tool definitions and avoids duplicating business logic <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.
*   LLMs, particularly models like Llama, OpenAI, and Claude, are capable of generating complex queries such as GraphQL, including concepts like fragments <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
*   **Trade-offs**: LLMs can sometimes hallucinate or mess up syntax, particularly with complex schemas or deep nesting <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

In conclusion, as the focus shifts to building more sophisticated AI agents, it is imperative to equally prioritize the development of robust, reusable tools <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.