---
title: Differences between regular and meta tool calling
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

[[importance_of_tool_calling_for_ai_agents | Tool calling]] is not merely "plumbing" for [[ai_integration_and_tool_calling | AI agents]]; it is more significant than some people realize <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While much attention is often given to improving agents, less focus has historically been placed on building reusable and robust tools for them <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, this is changing, with more tool platforms and libraries emerging <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The agent's effectiveness is often directly tied to the quality of its tools <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Understanding Tool Calling

At its core, [[function_calling_in_ai | tool calling]] allows an agent to interact with external functionalities or data sources <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. For example, when an agent is asked a complex question like "How far does the moon orbit Express as the number of trips between Amsterdam and San Francisco?" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, it might perform a series of [[function_calling_in_ai | tool calls]]. This could involve searching for distances, using a calculator, or querying a database <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. These tools often connect to external APIs, web searches, or geographical databases <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

A typical tool definition includes:
*   **Tool Name:** Kept simple for clarity <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Tool Description:** Functions almost like a system prompt for the Large Language Model (LLM), guiding it on how to use the tool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Input Parameters:** Specifies what the model needs to provide to call the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Output Schema:** Increasingly important for type safety, structured outputs, and chaining tool calls <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Traditional Tool Calling

Traditional tool calling, as seen two to three years ago, involves explicit management of the tool calling logic by the application where the agent resides <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Process
In this model, the client application sends a prompt to the agent/AI application <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The application then puts this into a prompt and sends it to the model <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The model suggests a tool call, and the application explicitly looks for tool call messages, parses them, and executes them based on a callback function <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This requires handling things like queuing tool calls, retries, and errors within the application logic <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. There is a lot of back and forth between the application and the LLM, as well as between the client app and the agent <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Characteristics
*   **Explicit Control:** Developers have direct control over the tool calling process, including how tools are executed and how errors are handled <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Complex Implementation:** Requires developers to write specific logic for filtering tool call messages, parsing data, and managing execution flow <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Separation of Concerns (Partial):** While logic for tool calls is defined in the server app, it's still tightly coupled with the agent's implementation <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Embedded/Meta Tool Calling

[[integration_of_tool_calling_in_agent_frameworks | Embedded tool calling]], also referred to as meta tool calling, is a more recent approach where the tool calling logic is encapsulated within a closed system, often the agent framework itself <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

### Process
In this model, the client application simply asks a question <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. The agent, acting as a black box, handles connecting with the LLM, calling the tools, and performing all necessary logic internally <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. The tools are defined within the same agent framework, and the final answer is returned directly to the client <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. For example, in LangChain, this is achieved using functions like `create_react_agent` which take tools, a model, and a prompt, and handle the execution <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

### Characteristics
*   **Ease of Implementation:** Simpler for developers, as they don't need to worry about errors, retries, or explicit tool calling logic <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Lack of Control:** Developers have no control over the internal tool calling process, how decisions are made, or the format of outputs beyond the initial tool definition <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
*   **Black Box System:** The agent acts as a self-contained unit, abstracting away the complexities of tool interaction <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Evolution and Future Directions

While embedded tool calling offers simplicity, there's a strong argument for greater separation of concerns in building [[ai_integration_and_tool_calling | AI applications]] <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### Model Context Protocol (MCP)
Introduced by Anthropic, the Model Context Protocol (MCP) aims to separate the client-side (host) from the server-side in agentic applications <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. The server, which has access to tools and assets, is the only component the host and client directly interact with <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. This provides a clearer distinction between the front-end and back-end logic <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

### [[emergence_of_standalone_tool_platforms_and_dynamic_tools | Standalone Tool Platforms]]
A growing trend is the [[emergence_of_standalone_tool_platforms_and_dynamic_tools | development of standalone tool platforms]] <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. These platforms allow tools to be defined and hosted separately from the agent framework <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. The agent framework then imports these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. The tool creation and execution are handled remotely, offering greater flexibility and clear separation of concerns <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. Examples include Compos Tool House, Arcade AI, and Wild Card <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

Advantages of standalone tool platforms:
*   **Modularity:** Tools can be created once and used across different agentic frameworks like LangChain, CrewAI, or Autogen <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Centralized Management:** Platforms can handle complex logic like chaining tools, authorization, and error handling <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Flexibility:** Allows for easy switching between agent frameworks without rebuilding tools <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

### [[emergence_of_standalone_tool_platforms_and_dynamic_tools | Dynamic Tools]]
Instead of creating a multitude of static tools for every specific function (e.g., separate tools for "get customers," "get customers by country," "get orders"), [[emergence_of_standalone_tool_platforms_and_dynamic_tools | dynamic tools]] offer a more generalized approach <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. For example, a single tool can be created that connects to a GraphQL or SQL schema <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>. The LLM then generates the appropriate query (e.g., GraphQL query) based on the schema and the user's request <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

### Considerations
While [[emergence_of_standalone_tool_platforms_and_dynamic_tools | dynamic tools]] reduce the number of explicit tool definitions and allow existing business logic to be leveraged <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>, they come with trade-offs. LLMs can sometimes hallucinate or generate incorrect syntax for queries, requiring careful handling <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. However, there's a strong potential for building a future around [[emergence_of_standalone_tool_platforms_and_dynamic_tools | dynamic tools]] rather than static ones <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.