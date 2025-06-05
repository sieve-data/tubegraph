---
title: Challenges and considerations in tool creation and execution
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

Tool calling is more significant than simply "plumbing" for AI agents, playing a crucial role in their effectiveness and flexibility [00:00:04]. While much attention is often given to improving AI agents themselves, less focus has historically been placed on building reusable, robust tools that can function across different frameworks [00:00:53]. This trend is changing, with more tool platforms and libraries emerging to support tool development [00:01:06].

## The Agent's Reliance on Tools

An AI agent's capability is directly tied to the quality of its tools [00:02:56]. Failures often originate within the tools, such as the Large Language Model (LLM) incorrectly calling a tool, using the wrong tool, or encountering internal tool failures [00:02:37]. The application layer, where tools are built, demands more attention as LLMs continue to advance [00:03:20]. Enhancing the "wrappers" around models and chat interfaces, through smart software solutions, offers significant opportunities for improvement [00:03:44].

When an agent needs to answer a complex query, such as calculating the moon's orbit in terms of trips between two cities, it often relies on a sequence of tool calls rather than solely on its training data [00:04:50]. This can involve web searches, querying databases for geographical data, or utilizing external APIs like Wolfram Alpha for calculations [00:05:37].

## Defining AI Tools

The way a tool is defined significantly impacts its usability and effectiveness [00:05:56]. Key components of a tool definition include:
*   **Tool Name**: Should be kept simple [00:06:06].
*   **Tool Description**: Acts as a system prompt for the LLM, guiding its usage [00:06:09]. More complex tools often have longer, detailed descriptions [00:06:21].
*   **Input Parameters**: Specifies what the model needs to provide to call the tool [00:06:40].
*   **Output Schema**: An increasingly important element that helps make tools type-safe and facilitates structured outputs or chaining tool calls by defining the expected data return [00:06:46].

For instance, a tool to count customers might require a filter like a country as an argument [00:07:39].

## Evolution of Tool Calling Approaches

Historically, and presently, there are different architectural patterns for integrating tools with AI agents:

### Traditional Tool Calling

In a traditional tool calling setup, the client application sends a prompt to an agent or AI application [00:09:02]. This application then prompts the LLM [00:09:29]. The LLM suggests tool calls, but the actual execution logic resides explicitly within the server application or agent framework [00:09:42]. This involves:
*   Filtering tool call messages from the LLM's response [00:10:47].
*   Parsing and executing the recommended tools based on defined callback functions [00:10:54].
*   Manually handling various complexities like queuing tool calls, retries, and errors [00:11:01].

This approach involves significant back-and-forth communication between the application logic and the LLM, making it less of a closed system [00:10:08].

### Embedded Tool Calling

More modern frameworks often adopt an embedded tool calling approach, where the system operates as a closed unit [00:11:19]. The client application simply sends a question to the agent, which is responsible for everything internally [00:11:36]. The agent framework handles connecting with the LLM, defining and connecting with tools, and executing tool calls within its own logic [00:11:42]. The output is a direct answer from the agent [00:11:50].

This "black box" approach simplifies implementation, as developers don't need to worry about managing errors or retries [00:13:10]. However, it offers less control over the tool calling process, how decisions are made, or the output format, other than through the tool's description and provided callback functions [00:13:19].

## Separating Concerns in AI Systems

A key consideration for developers is the separation of concerns, preventing systems from becoming monolithic and inflexible [00:13:41]. This principle, common in software development, promotes modularity even within a single repository [00:14:41].

### [[Model Context Protocol and tool integration | Model Context Protocol (MCP)]]

The [[Model Context Protocol and tool integration | Model Context Protocol (MCP)]], introduced by Anthropic, is a significant step towards separating client-side and server-side logic in agentic applications [00:14:48]. In an MCP setup:
*   A "host" (e.g., a desktop application) contains a client that connects to "servers" [00:15:10].
*   These "servers" act as backends, providing access to tools or assets like data files [00:15:20].
*   The host and client do not directly see the tools; instead, they interact with the server which exposes the tools' functionality [00:15:31].

This provides a clear distinction between the front-end (host/client) and back-end (server), where tool logic is managed and imported [00:15:41].

### Standalone Tool Platforms

An advanced approach involves utilizing standalone tool platforms [00:16:25]. Instead of defining tools within the agentic framework, they are defined and hosted separately on remote servers [00:16:39]. The agent framework then imports these tools via an SDK or API calls [00:16:48].

Benefits of this separation include:
*   **Decoupled Creation and Execution**: Tool creation, hosting, and execution are distinct from the agent's logic [00:16:54].
*   **Flexibility**: Tools can be built once and easily integrated into various agentic frameworks (e.g., LangChain, CrewAI, Autogen), allowing for framework switching without rebuilding tools [00:19:00].
*   **Tool Chaining and Abstraction**: Platforms can manage complex operations like chaining multiple tool calls (e.g., getting a user's country and then retrieving customer count from a CRM) [00:17:59].
*   **Centralized Authorization and Error Handling**: These platforms can handle authorization and authentication for different backend systems (like CRMs or databases), streamlining credential management and error handling outside the agent framework [00:18:25].

Examples of such platforms include Compos Tool House, Arcade AI, and WildCard [00:19:36].

## [[Dynamic vs static tool calling | Dynamic vs Static Tool Calling]]

Traditional tools are often "static," meaning they are predefined functions with fixed arguments [00:24:50]. However, a significant development is the emergence of [[Dynamic vs static tool calling | dynamic tools]] [00:21:24].

Instead of creating numerous static tools for every variation (e.g., separate tools for customer count by country, by order, etc.), a [[Dynamic vs static tool calling | dynamic tool]] can connect to a broader data schema, such as a GraphQL or SQL schema [00:21:37]. The LLM is then provided with this schema and tasked with generating a valid query (e.g., GraphQL query) to interact with the underlying data [00:22:55].

This approach offers:
*   **Reduced Tool Count**: A single [[Dynamic vs static tool calling | dynamic tool]] can replace many static ones, preventing agent confusion when dealing with hundreds of tools [00:21:40].
*   **Leveraging Existing Logic**: Direct integration with existing business logic and APIs [00:24:29].
*   **LLM Capabilities**: Models like Llama, OpenAI models, and Claude are adept at generating GraphQL queries when provided with a clear schema [00:23:29].

However, [[Dynamic vs static tool calling | dynamic tools]] come with trade-offs:
*   **Hallucination Risk**: LLMs might hallucinate or produce syntactically incorrect queries, especially with complex schemas, custom scalars, or deeply nested data [00:23:37].
*   **Design Constraints**: Simpler schemas and less nesting are preferred for optimal LLM performance [00:23:47].

Despite these challenges, there is a strong future for [[Dynamic vs static tool calling | dynamic tools]] over static ones, enabling more flexible and efficient integration with diverse data sources [00:24:48].

In conclusion, as AI agents become more prevalent, it is crucial to recognize that the tools they utilize are as important as the agents themselves for achieving robust and flexible AI solutions [00:24:58].