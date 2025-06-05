---
title: Importance of tool calling for AI agents
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

[[ai_integration_and_tool_calling | Tool calling]] is not merely "plumbing" for [[building_effective_ai_agents | AI agents]]; it is more important than some people realize and can be effectively used with agentic frameworks <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While much attention is often given to improving the agents themselves, building reusable and robust tools for agents has been less emphasized <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. However, this trend is changing, with more tool platforms and libraries emerging to facilitate tool development <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The belief is that an agent is only as effective as its tools, and therefore, focus should be on creating tools that are reusable and robust across different agent frameworks <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## The Role of Tools in Agent Frameworks

In a typical agent loop, a user sends a prompt, and the agent, utilizing large language models and memory, relies on tools to find answers <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. When an agent breaks, it's often due to issues with the tools, such as the large language model failing to call the correct tool or problems within the tool itself <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The application layer, specifically where tools are built, deserves more attention as it offers significant opportunities for improvement on top of models <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

For example, to answer a question like "How far does the moon orbit expressed as the number of trips between Amsterdam and San Francisco?", an agent might perform a series of [[function_calling_in_ai | tool calls]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This could involve searching for distances via external APIs (e.g., web search, geographical databases) and performing calculations using a JavaScript function or an external API like Wolfram Alpha <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Defining Tools for AI Agents

The way tools are defined significantly impacts their utility <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. A typical tool definition includes:
*   **Tool Name:** Advised to be simple <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Tool Description:** Acts almost like a system prompt for the large language model, guiding its use of the tool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Long and detailed descriptions, sometimes resembling system prompts, are common in larger, more agentic tools <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Input Parameters:** Specifies the variables required for the tool to be called <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Output Schema:** Increasingly important, this helps make tools type-safe, enables structured outputs, and allows for chaining tool calls <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. It informs the model about the expected data return type, even if the primary output is a string <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Types of Tool Calling Implementations

Historically, the location and method of tool calling within agent frameworks have evolved:

### Traditional Tool Calling
In this model, the client application sends a prompt to an agent or AI application, which then sends it to the large language model along with tool definitions <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The model recommends tool calls, and the application explicitly parses and executes these calls using defined callback functions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This involves significant back-and-forth communication between the application logic and the large language model, requiring explicit handling of queuing, retries, and errors <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This approach offers more control over the tool calling process <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Embedded Tool Calling
This approach treats the agent as a closed system <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. The client app simply asks a question, and the agent, which contains the tools and connects with the large language model, handles all tool calling logic internally <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. The tools are defined within the same agent, and the application receives only the final answer <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. While easy to implement for beginners as it abstracts away error handling and retries <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>, it offers no control over the tool calling process or decision-making inside the black box <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

## Separating Concerns: [[integration_of_tool_calling_in_agent_frameworks | Tool Calling and Agent Frameworks]]

A key principle for [[best_practices_for_building_ai_agents | building effective AI agents]] is the separation of concerns <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

### Model Context Protocol (MCP)
Introduced by Anthropic, MCP is a protocol designed to separate the client and server sides of agentic applications <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. In MCP, a host (client) connects to servers that have access to tools or assets <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. The host and client do not directly see the tools; rather, the server makes them available <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This clear distinction between front-end and back-end logic, where the MCP server handles tool definition, import, and execution, is a good step towards separating tool calling from the agentic framework <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Standalone Tool Platforms
A standalone tool platform means that tools are defined and hosted separately from the agentic framework <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. Agents can then import these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This approach centralizes tool creation and execution remotely <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. The agent decides which tool to call and passes the request to the tool platform for execution <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

These platforms often consist of:
*   **Tool Creation:** Done via code or CLIs <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Tool Execution/Surfacing:** Done via SDKs that connect to agent frameworks like LangChain or CrewAI <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

Benefits of standalone tool platforms include:
*   **Chaining Tools:** Allows for sequential execution of tools, handling repetitive patterns <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   **Authorization and Error Handling:** Centralized management of credentials, authorization, and error handling for various connected systems (CRMs, databases) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Flexibility:** Enables building tools once and bringing them into different agentic frameworks like LangChain, LangGraph, CrewAI, or Autogen, simplifying framework switching <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>. This also supports [[integration_of_thirdparty_tools_with_ai_web_agents | integration of third-party tools with AI web agents]].

## Dynamic Tools

Instead of creating a multitude of static tools for every specific function (e.g., a different tool for each component of a CRM), dynamic tools offer a more flexible approach <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

For example, a dynamic tool can connect to a GraphQL schema or SQL database <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. The large language model is given access to the schema and tasked with generating a valid query (e.g., GraphQL query) to interact with the database or API <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. Models like Llama, OpenAI, and Claude have shown proficiency in generating GraphQL queries given a clear schema <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.

This approach reduces the need to define numerous individual tools and avoids duplicating business logic <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. However, there are trade-offs, as LLMs might hallucinate or struggle with complex schemas, leading to incorrect syntax <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Despite these challenges, the future of dynamic tools appears promising <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

## Conclusion

As [[developing_ai_agents_for_productivity | AI agents]] become more prevalent, it is crucial not to overlook the importance of the tools they utilize <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. By focusing on robust tool definitions, adopting architectures that promote separation of concerns, and exploring dynamic tool capabilities, developers can significantly enhance the effectiveness, reusability, and maintainability of their AI applications <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.