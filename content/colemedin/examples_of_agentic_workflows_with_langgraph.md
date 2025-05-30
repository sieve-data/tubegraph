---
title: Examples of agentic workflows with LangGraph
videoId: w_HeP0A2MF8
---

From: [[colemedin]] <br/> 

[[building_ai_agent_workflows_with_langgraph | Building production-grade AI agent applications]] can become messy when trying to connect different agents without a clear, concise, and generic structure for their interactions, often leading to unmaintainable "spaghetti code" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. LangGraph offers a powerful solution, making even complex [[agentic_workflows_and_ai_technology | agentic workflows]] clear, concise, and bug-free <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

LangGraph is a library designed for [[developing_ai_agents_with_lang_chain_and_lang_graph | building stateful multi-actor applications with Large Language Models (LLMs)]], specifically used to create agents and multi-agent workflows <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It is a product of LangChain, recognized as a leading library for working with LLMs <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Key concepts in LangGraph include:
*   **Graph**: The highest-level concept defining the workflow structure <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **State**: Variables maintained throughout the execution of the [[agentic_workflows_and_ai_technology | agentic workflow]], such as chat history or tool retry counts <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Nodes**: Represent individual agents within the workflow <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Edges**: Define how agents (nodes) are connected, including conditional connections <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Persistence**: The ability to manage state within the graph across different executions <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **[[agentic_workflows_and_human_in_the_loop_concept | Human in the Loop]]**: Support for user approval at certain points in the workflow <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Streaming Support**: Enables "typewriter-style" output from the AI in a user interface <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

---

## Examples of Agentic Workflows

### 1. Chart Generation Agentic Workflow

This workflow is designed to generate charts based on user input, such as "generate a chart of the average temperature in Alaska over the past decade" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The workflow steps are:
1.  **User Input**: The process begins with a user request <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  **Researcher Agent**: The execution first goes to a "researcher" agent, which gathers information needed to create the chart <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
3.  **Router**: The researcher produces a response that goes to a "router." This router is a core part of the graph, determining if more research is needed or if chart generation can begin <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   If a tool call (e.g., web search) or more research is required, the flow returns to the researcher <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   If research is complete, the flow proceeds to the chart generator <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
4.  **Chart Generator**: This agent invokes tools to execute code and generate the chart <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
5.  **Return to User**: The generated chart is sent back to the user <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

This example demonstrates how LangGraph provides a clear structure for managing complex interactions and conditional routing between multiple AI agents <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Code Execution Agentic Workflow

This workflow handles requests requiring code execution, potentially as a sub-workflow within another larger [[agentic_workflows_and_ai_technology | agentic workflow]], like the chart generation example <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

The workflow steps are:
1.  **User Input**: A question or request comes in, for example, "generate a chart" <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Generate Preamble, Imports, and Code**: An agent generates the necessary code components <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
3.  **Import Code**: The system attempts to import the generated code <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   **Failure**: If the import fails, the process loops back to the code generation step to retry <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   **Success**: If imports are successful, the flow moves to code execution <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
4.  **Execute Code**: The generated code is executed <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Failure**: If execution fails, the process restarts, going back to code generation <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   **Success**: If execution is successful, the final answer is returned to the user <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
5.  **Return to User**: The result is sent back to the user <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

LangGraph simplifies the management of such recursive or nested workflows, which would be challenging to code from scratch <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### 3. Tool Interaction Loop in a Task Management Agent

This is a common [[agentic_workflows_and_ai_technology | agentic workflow]] pattern where an agent interacts with tools in a loop, exemplified by a task management agent interacting with Asana <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

The original implementation of the task management agent used recursion within a `prompt_AI` function to handle tool calls <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. While functional, this approach is not extensible for features like [[agentic_workflows_and_human_in_the_loop_concept | human-in-the-loop]] approval or dynamic LLM selection <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. LangGraph provides a cleaner and more scalable way to define this loop <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The LangGraph implementation of this loop involves:
*   **State**: Keeping track of `messages` (chat history) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Nodes**:
    *   **Agent Node**: Invokes the AI model and adds its response to the `messages` state <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. This node is asynchronous to support streaming output <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
    *   **Tool Node**: Checks the last message for tool calls. If present, it invokes the specified tools and adds their outputs as new messages to the state <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   **Conditional Edge (Router)**: After the Agent Node, a router decides the next step based on the agent's response <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
    *   If no tool calls are needed, the workflow `END`s, and the response is returned to the user <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
    *   If tool calls are needed, the workflow transitions to the Tool Node <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **Loop**: After the Tool Node executes, the flow returns to the Agent Node so the AI can process the tool outputs and decide on the next action (either further tool calls or a final response) <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

This pattern allows the agent to continuously invoke tools and refine its response until a final answer is ready for the user <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Benefits of LangGraph Implementation

By using LangGraph, the task management agent's code becomes significantly cleaner and more scalable <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Key benefits include:
*   **Extensibility**: Easily add new features like [[agentic_workflows_and_human_in_the_loop_concept | human-in-the-loop]] approval or handle different tool calls in varied ways <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **State Persistence**: LangGraph's checkpointing with a SQLite saver allows chat history and state to be automatically saved and retrieved between executions, maintaining conversational context <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Streaming Output**: Continues to support typewriter-style AI responses in the UI <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.

This structured approach prevents the code from devolving into "spaghetti code" when functionality expands <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

---

### Future Enhancements

LangGraph is a foundational tool for further development in [[agentic_workflows_and_ai_technology | AI agent applications]]. Future topics to explore include:
*   **[[agentic_workflows_and_human_in_the_loop_concept | Human-in-the-loop]]**: Integrating human oversight and approval into workflows <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.
*   **LangServe**: Deploying LangGraph runnables as API endpoints in the cloud, allowing them to be used with front-end applications <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.