---
title: Emergence of standalone tool platforms and dynamic tools
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

The common perception that [[AI integration and tool calling | tool calling]] is merely "plumbing for AI agents" understates its significance <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While much attention has been given to improving AI agents, less focus has historically been placed on building robust, reusable tools for these agents <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, this trend is changing, with more tool platforms and libraries emerging <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The application layer, where tools are constructed, is increasingly recognized as critical for enhancing AI capabilities <a class="yt-timestamp" data-t="00:02:25">[02:25]</a>.

## The Importance of Tools in Agent Frameworks

An agent is only as effective as the tools it utilizes <a class="yt-timestamp" data-t="00:02:56">[02:56]</a>. Often, the first component to fail when building an agent is its tools, whether due to a large language model (LLM) miscalling a tool, using the incorrect one, or internal tool breakdowns <a class="yt-timestamp" data-t="00:02:35">[02:35]</a>. This highlights the need for tools that are reusable, robust, and transferable across different [[integration_of_tool_calling_in_agent_frameworks | agent frameworks]] <a class="yt-timestamp" data-t="00:03:13">[03:13]</a>.

### Understanding Tool Calling

Tool calling enables an agent to extend its capabilities beyond its internal knowledge <a class="yt-timestamp" data-t="00:04:06">[04:06]</a>. For example, to answer a complex query like "How far does the moon orbit expressed as the number of trips between Amsterdam and San Francisco?", an LLM might perform a series of tool calls <a class="yt-timestamp" data-t="00:04:10">[04:10]</a>:
1.  Search for the distance between the Earth and the Moon <a class="yt-timestamp" data-t="00:04:51">[04:51]</a>.
2.  Search for the distance between Amsterdam and San Francisco airports <a class="yt-timestamp" data-t="00:04:56">[04:56]</a>.
3.  Perform calculations, possibly [[using_offtheshelf_tools_for_app_enhancement | using a calculation tool]] or an external API like Wolfram Alpha <a class="yt-timestamp" data-t="00:04:59">[04:59]</a>.

The definition of a tool is crucial <a class="yt-timestamp" data-t="00:05:54">[05:54]</a>. A typical tool definition includes:
*   **Tool Name:** Kept simple <a class="yt-timestamp" data-t="00:06:06">[06:06]</a>.
*   **Tool Description:** Functions almost like a system prompt for the LLM, guiding its usage <a class="yt-timestamp" data-t="00:06:09">[06:09]</a>.
*   **Input Parameters:** Specifies what data the tool needs to be called <a class="yt-timestamp" data-t="00:06:40">[06:40]</a>.
*   **Output Schema:** Increasingly important for structured outputs and chaining tool calls, ensuring type safety <a class="yt-timestamp" data-t="00:06:46">[06:46]</a>.

## Evolution of Tool Calling Architectures

### Traditional Tool Calling

In traditional tool calling, the application or agent explicitly defines and manages the tool calling logic <a class="yt-timestamp" data-t="00:09:02">[09:02]</a>.
*   A client application sends a prompt to the agent/AI application <a class="yt-timestamp" data-t="00:09:23">[09:23]</a>.
*   The agent sends the prompt to the LLM <a class="yt-timestamp" data-t="00:09:31">[09:31]</a>.
*   The LLM recommends a tool call, and the application must then filter, parse, and execute the tool call based on defined callback functions <a class="yt-timestamp" data-t="00:09:42">[09:42]</a>.
*   This involves significant back-and-forth between the application and the LLM, and requires handling queues, retries, and errors within the application logic <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Embedded (Meta) Tool Calling

More modern frameworks often use an embedded or "meta" tool calling approach, where the agent framework handles all tool calling internally <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   The agent is a closed system; tools are passed in as a black box <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   The client app sends a question to the agent, which connects with the LLM and its defined tools, performs calls, and returns the answer <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   This simplifies initial implementation by abstracting away error handling and retries <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   However, it offers less control over the tool calling process, how decisions are made, or the output format <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

### Separation of Concerns with MCP

Inspired by architectural principles like separation of concerns in web development (e.g., separating backend from frontend) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>, the Model Context Protocol (MCP) emerged <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. Introduced by Anthropic, MCP aims to separate the client-side (host) from the server-side in agentic applications <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   The **host** (e.g., a desktop client) has a client that connects to servers <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Servers** act as backends, having access to tools or assets like data files <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   The host and client interact only with the server, not directly with the tools <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   This approach clearly distinguishes between the front-end and back-end logic, with the MCP server handling tool definition and logic <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Standalone Tool Platforms

A significant advancement in [[challenges_of_building_robust_and_reusable_tools | building robust and reusable tools]] is the rise of standalone tool platforms <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   **Definition:** Tools are defined and hosted separately from the agentic framework <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   **Integration:** Agents import these tools via an SDK or API call <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Execution:** The agent uses the LLM to decide which tool to call, then passes the request to the remote tool platform for execution <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Benefits:**
    *   **Separation of Concerns:** Clear distinction between tool creation/hosting/execution and agent logic <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
    *   **Ease of Creation:** Platforms facilitate building tools from existing APIs or databases <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   **Tool Chaining:** Platforms can manage sequential or complex tool calls <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
    *   **Centralized Handling:** Authorization, authentication, and error management can be handled by the platform, simplifying the agent's responsibilities <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
    *   **Flexibility:** Tools built on a standalone platform can be easily integrated into different [[integration_of_tool_calling_in_agent_frameworks | agent frameworks]] (e.g., LangChain, CrewAI, AutoGen), allowing for framework switching without rebuilding tools <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

Examples of standalone tool platforms include Composable, Toolhouse, Arcate AI, WildCard, and IBM's WX Flow <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Dynamic Tools

Instead of creating numerous static tools for every specific function within a complex system (e.g., a CRM) <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>, **dynamic tools** offer a solution <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   A single dynamic tool can connect to a schema (e.g., GraphQL or SQL) <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.
*   The LLM itself generates the necessary query (e.g., a GraphQL query) based on the schema and user's request <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   The model is provided with the tool, instructed to generate valid queries, and given the schema (type definitions, available operations) <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
*   **Benefits:** Allows for the [[integration_of_thirdparty_tools_with_ai_web_agents | integration of existing APIs and databases]] into agent frameworks with less implementation overhead, avoiding duplication of business logic <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   **Considerations:** There are [[differences_between_regular_and_meta_tool_calling | trade-offs]], such as the potential for LLM hallucination in generating queries or issues with complex schema features (e.g., custom scalars, deep nesting) <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Despite these, dynamic tools are seen as a promising future direction for tool building <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

Ultimately, as AI agents continue to advance, ensuring the quality and flexibility of the tools they use is equally important <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. The shift towards standalone platforms and dynamic tools reflects a growing understanding of this critical relationship.