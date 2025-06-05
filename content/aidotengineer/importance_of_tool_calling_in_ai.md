---
title: Importance of tool calling in AI
videoId: zuMw0pkPXpU
---

From: [[aidotengineer]] <br/> 

[[function_calling_in_ai_models | Tool calling]] is considered more significant than some people realize and is crucial for [[implementing_function_calling_and_agents_in_ai | agentic frameworks]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It is not merely "plumbing" for AI agents <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Why Tool Calling Matters

While much attention is given to improving AI agents, the focus on building reusable and robust tools for these agents has been less prominent <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. However, this trend is changing, with more tool platforms and libraries emerging to facilitate tool building <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. A common issue is that tools are often the first component to break when building an agent, whether due to incorrect calls by the Large Language Model (LLM) or internal tool failures <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

> "The agent is only as good as their tools." <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>

As LLMs have advanced significantly, the application layer—especially where tools are built—deserves more attention <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Wrappers around models or chat interfaces offer substantial opportunities for improvement by enabling smart software solutions on top of the core models <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Understanding Tool Calls

When an agent receives a complex query, such as "How far does the moon orbit expressed as the number of trips between Amsterdam and San Francisco?", it often performs a series of tool calls <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This could involve searching for the distance between the Earth and the Moon, the distance between the two cities, and then performing calculations, potentially using external APIs like Wolfram Alpha <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Defining Tools

The way a tool is defined significantly impacts its utility <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Key components of a tool definition include:
*   **Tool Name**: Should be kept simple <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Tool Description**: Acts almost like a system prompt for the LLM, guiding its usage. Larger tools often have lengthy, detailed descriptions <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Input Parameters**: Specifies what the model needs to provide to call the tool <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Output Schema**: Increasingly important for type-safe tools, enabling structured outputs and the chaining of tool calls <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Evolution of Tool Calling Paradigms

Historically, tools were often built and defined within the same agent framework <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. However, there's a shift towards more separated and flexible approaches.

### Traditional Tool Calling

In traditional tool calling, the client application interacts with an agent or AI application, which then sends prompts to the LLM <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The application explicitly defines the logic to filter tool call messages from the LLM's response, parse them, and execute them via callback functions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This approach involves a significant amount of back-and-forth between the application and the LLM and requires handling queuing, retries, and errors <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

[!example]
```python
# Simplified LangChain example for traditional tool calling
tools = [
    Tool(
        name="get_customer_count",
        func=get_customer_count_callback,
        description="..."
    )
]
# Model and agent setup...
# Explicitly look for tool call messages and execute them
```
This method was common in early [[evolution_of_ai_engineering_and_tools | agentic]] setups <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Embedded Tool Calling

Modern frameworks often feature "embedded tool calling," where the system acts as a closed black box <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. The client application sends a question to the agent, which handles all tool calling logic internally, connecting with the LLM and tools, and then returns the final answer <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

[!example]
```python
# Simplified LangChain example for embedded tool calling
from langchain.agents import AgentExecutor, create_react_agent
# Define tools, model, prompt...
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
# All tool calling logic is hidden within create_react_agent and AgentExecutor
```

While easier to implement for beginners as it abstracts away error handling and retries, embedded tool calling offers less control over the tool calling process and decision-making <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

## Strategies for Separation of Concerns

As a developer, separating concerns is often preferred to increase flexibility and maintainability <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### Model Context Protocol (MCP)

Introduced by Anthropic, the Model Context Protocol (MCP) is a protocol for separating the client-side and server-side logic in [[implementing_function_calling_and_agents_in_ai | agentic applications]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Host/Client**: The host, such as Cloud Desktop, contains a client capable of connecting to servers <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Servers**: Act as backends with access to tools or assets like data files <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

The client interacts only with the server, which handles the tool logic and definitions, providing a clear distinction between front-end and back-end responsibilities <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

### Standalone Tool Platforms

A growing trend is the use of standalone tool platforms, which allow tools to be defined and hosted separately from the [[implementing_function_calling_and_agents_in_ai | agentic framework]] <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   Tools are created and executed on remote servers <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
*   The agent imports these tools via an SDK or API calls <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   The agent's role is to use the LLM to decide which tool to call and then pass the request to the tool platform for execution <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

These platforms typically offer:
*   **Tool Creation**: Via code or CLIs <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Tool Execution/Surfacing**: Via SDKs that integrate with frameworks like LangChain or CrewAI <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Tool Chaining**: The ability to sequence multiple tool calls within the platform, handling complex workflows (e.g., getting user country, then customer count) <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   **Authorization and Error Handling**: Centralized management of credentials and errors for various connected systems <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

This separation offers flexibility, allowing developers to build tools once and use them across different [[implementing_function_calling_and_agents_in_ai | agentic frameworks]] <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Dynamic Tools

Rather than creating a multitude of static tools for every possible operation (e.g., separate tools for "get customers by country," "get customers by search filter"), dynamic tools allow the LLM to generate queries for existing APIs or databases <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

For example, a single dynamic tool can connect to a GraphQL schema <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. The LLM is given the GraphQL schema and instructed to generate valid GraphQL queries <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. This allows the LLM to understand type definitions and available operations (like `getCustomers` or `getOrders`) <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

[!info]
Models such as Llama, OpenAI models, and Claude are particularly good at generating GraphQL queries, especially when schemas are simple and nesting is not too deep <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.

Dynamic tools reduce the need to define many individual tools and prevent duplication of business logic, leading to more flexible integrations with existing APIs and databases <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. However, there are trade-offs, as LLMs can sometimes hallucinate or generate syntactically incorrect queries <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Despite these challenges, the future of dynamic tools appears promising <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.