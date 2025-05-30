---
title: Integrating LangGraph with existing AI applications
videoId: w_HeP0A2MF8
---

From: [[colemedin]] <br/> 

[[building_ai_agent_workflows_with_langgraph | LangGraph]] is a powerful tool for [[building_ai_agent_workflows_with_langgraph | building production-grade AI agent applications]] and managing agentic workflows [00:00:03]. It addresses the common issue of messy "spaghetti code" that arises when developers try to tie different AI agents together without a clear and concise structure [00:00:13]. By using [[building_ai_agent_workflows_with_langgraph | LangGraph]], even complex [[examples_of_agentic_workflows_with_langgraph | agentic workflows]] become clear, concise, and bug-free [00:00:37].

## LangGraph Overview
[[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] is a product of [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]], the primary library for working with large language models (LLMs) [00:01:12]. It is specifically designed for "building language agents as graphs" and "building stateful multi-actor applications with LLMs" [00:01:31].

### Key Features
[[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] offers several key features that facilitate the creation and management of complex AI agent applications:
*   **Cycles and Branching** Allows defining intricate graphs where AI agents can work together, making conditional decisions and branching paths [00:01:52].
*   **Persistence** Enables the management of state within the graph, even across different executions [00:01:57].
*   **[[integrating_ai_agents_with_live_platforms | Human in the Loop]]** Provides mechanisms for human approval at certain points in the workflow, ensuring control over AI operations [00:02:03].
*   **Streaming Support** Facilitates typewriter-style output from the AI in user interfaces, enhancing user experience [00:02:10].
*   **Integration with [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]]** Seamlessly integrates with the broader [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] ecosystem [00:02:16].

### Core Concepts
To deeply understand [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]], it's beneficial to grasp its core conceptual components:
*   **Graph** The highest-level concept, representing the overall workflow structure [00:02:32].
*   **State** All variables maintained during the execution of an [[examples_of_agentic_workflows_with_langgraph | agentic workflow]], such as chat history or tool retry counts [00:02:35].
*   **Nodes** Represent individual agents or steps within the workflow [00:02:47].
*   **Edges** Define how agents are connected, including conditional transitions [00:02:49].
*   **Checkpoints and Threads** Mechanisms for managing execution points and individual sessions [00:02:54].

## Examples of Agentic Workflows
[[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] is suitable for various complex [[examples_of_agentic_workflows_with_langgraph | agentic workflows]]:

### Chart Generation Workflow
This workflow involves a user request to generate a chart, like "generate a chart of the average temperature in Alaska over the past decade" [00:03:22].
1.  **Researcher** The execution first goes to a researcher agent to gather information [00:03:30].
2.  **Router** The researcher's response is sent to a router, which determines if more research is needed (e.g., through a tool call like web searching) or if the chart can be generated [00:03:40].
3.  **Chart Generator** If research is complete, the workflow proceeds to a chart generator, which invokes tools to execute code and create the chart, then sends it back to the user [00:04:00].
This example highlights the dynamic routing and decision-making capabilities within [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] [00:04:09].

### Code Execution Workflow
A more advanced example involves an agentic workflow for code execution [00:04:21].
1.  **Code Generation** A user question or request (e.g., "generate a chart") leads to the generation of preamble, imports, and code [00:04:42].
2.  **Code Import/Execution** The system attempts to import the code [00:04:50].
3.  **Conditional Path** If import fails, it cycles back to regenerate the code [00:04:52]. If successful, it proceeds to execute the code [00:04:57].
4.  **Error Handling/Completion** If code execution fails, it restarts the process [00:05:00]. If successful, the final answer is returned to the user [00:05:06].
This demonstrates how a single step in one workflow can itself be an entire [[examples_of_agentic_workflows_with_langgraph | agentic workflow]], which [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] makes manageable [00:05:20].

### Agent-Tool Interaction Loop
This is a simpler, common workflow implemented in the task management agent example [00:05:27].
1.  **Agent Invokes Tool** An agent decides to invoke a tool, such as creating a project in Asana [00:05:41].
2.  **Tool Execution** The tool runs, and its output is returned to the agent [00:05:47].
3.  **Agent Decision** The agent then makes one of two decisions:
    *   **Respond to User** If the task is complete, the agent provides a final response to the user (e.g., "project created") [00:05:51].
    *   **Invoke More Tools** If further actions are needed based on the user's request (e.g., creating tasks within the newly created project), the agent returns to the tool invocation step, continuing the loop [00:06:00].
This loop continues until the agent decides to provide a final response [00:06:21].

## [[building_ai_agent_workflows_with_langgraph | LangGraph]] Implementation in a Task Management Agent
The task management AI agent, part of the AI agents Master Class series, was augmented with [[building_ai_agent_workflows_with_langgraph | LangGraph]] to improve code cleanliness and scalability [00:00:55]. Previously, the `prompt_AI` function used recursion to handle tool calls, making it inextensible for features like [[integrating_ai_agents_with_live_platforms | human in the loop]] or dynamic LLM changes [00:07:27].

### Code Restructuring for [[building_ai_agent_workflows_with_langgraph | LangGraph]]
The task management agent's code was restructured for better compatibility with [[building_ai_agent_workflows_with_langgraph | LangGraph]]:
*   `tools.py`: Contains functions for interacting with Asana (tools) and the mapping to bind them to the AI object [00:08:42].
*   `runnable.py`: Implements the [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] workflow [00:08:54].
*   `main.py`: Handles the Streamlit UI and interacts with the [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] runnable [00:08:57].

### Defining the Graph
The [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] implementation involves defining the state, nodes, and edges:

#### 1. State Definition
The graph's state tracks essential variables. For the task management agent, it simply tracks `messages` [00:10:25]. A special `add_messages` function ensures that new messages are appended to the chat history instead of overwriting it [00:11:05].

#### 2. Node Creation
Two main nodes are created to manage the agent-tool interaction loop:
*   **Call Model Node (`agent`)** [00:11:54]: This asynchronous node invokes the AI agent (chatbot) with the current messages from the graph state. It streams responses for a typewriter-style output in the UI and updates the `messages` state with the AI's response [00:11:57].
*   **Tool Node (`tools`)** [00:13:54]: This node fetches the latest message and checks for tool calls. If tool calls exist, it iterates through them, invokes the relevant tools (e.g., Asana functions), and adds the tool output messages back to the `messages` state [00:14:01].

#### 3. Router (Conditional Edge)
A router function (`should_continue`) acts as a conditional edge, determining the flow of execution [00:14:48].
*   **`End` Condition** If the last message from the AI does not contain any tool calls, it means the agent's response is final. The router returns `END`, signaling the termination of the graph execution and returning the response to the user [00:15:07].
*   **`Tools` Condition** If tool calls are present, the router returns the string `'tools'`, directing the execution to the `tools` node [00:15:26].

#### 4. Workflow Compilation
The workflow is compiled by defining the nodes and their connections:
*   **Entry Point** The workflow starts at the `agent` node when a user provides input [00:15:58].
*   **Conditional Edge** From the `agent` node, a conditional edge using `should_continue` leads either to `tools` or `END` [00:16:09].
*   **Loop Back** If the flow goes to the `tools` node, it then flows back to the `agent` node [00:16:23]. This creates the agent-tool-agent loop, allowing the agent to generate a final response after tool execution [00:16:31].
*   **Persistence** Persistence is easily set up using a `sqlite_saver` as a checkpoint when compiling the workflow. This ensures that the chat history and state are preserved between executions using a `thread_id` [00:16:56].

### Integration with Streamlit UI
The compiled [[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] runnable replaces the old `prompt_AI` function in the Streamlit UI [00:16:49]. The UI:
*   Initializes the runnable instance and a unique `thread_id` for session management [00:17:51].
*   Defines a system message to provide context to the AI agent [00:19:10].
*   Displays chat history and handles user input [00:20:30].
*   Calls the asynchronous `stream_events` function on the runnable to get chunks of AI response [00:19:48].
*   Updates the UI dynamically as chunks are received, creating a "typing" effect [00:21:16].
*   Adds the complete AI response to the chat history [00:21:28].

This new implementation provides a much cleaner and more scalable architecture for the task management agent [00:21:42].

## Future Possibilities
[[developing_ai_agents_with_lang_chain_and_lang_graph | LangGraph]] will be a core tool for future AI agents Master Class series content [00:23:37]. Upcoming topics include:
*   Implementing [[integrating_ai_agents_with_live_platforms | human in the loop]] functionality [00:23:43].
*   [[integrating_ai_agents_with_live_platforms | Deploying LangGraph runnables]] in the cloud using [[integrating_ai_agents_with_live_platforms | LangServe]] to create API endpoints [00:23:48].
*   Integrating with front-end applications using tools like the Vercel AI SDK [00:23:53].