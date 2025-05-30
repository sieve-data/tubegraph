---
title: Building AI agent workflows with LangGraph
videoId: w_HeP0A2MF8
---

From: [[colemedin]] <br/> 

LangGraph is a powerful tool designed for [[developing_ai_agents_with_lang_chain_and_lang_graph | building production-grade AI agent applications]] and [[examples_of_agentic_workflows_with_langgraph | agentic workflows]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It addresses the common problem of messy "spaghetti code" that arises when developers try to tie different agents together without a clear, concise, and generic structure for defining agent interactions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. LangGraph makes even complex workflows clear, concise, and bug-free <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## What is LangGraph?

LangGraph is a product of [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]], which is a leading library for working with large language models (LLMs) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It is specifically built for [[examples_of_agentic_workflows_with_langgraph | building stateful multi-actor applications with LLMs]], used to create agents and multi-agent workflows <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Key Features

LangGraph offers several key features essential for robust [[examples_of_agentic_workflows_with_langgraph | AI agent development]]:
*   **Cycles and Branching** Allows defining complex graphs where [[examples_of_agentic_workflows_with_langgraph | AI agents]] can work together <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Persistence** Enables managing state within the graph, even between different executions <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Human in the Loop** Supports human approval for certain actions, ensuring control over [[examples_of_agentic_workflows_with_langgraph | AI agent]] operations <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Streaming Support** Provides typewriter-style output from the AI in a user interface <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Integration with [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]]** Seamlessly integrates with the [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] ecosystem <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Core Concepts

To understand how LangGraph works, it's important to grasp its core concepts <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>:
*   **Graph** The highest-level concept, defining the overall workflow <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **State** All variables maintained during the execution of the [[examples_of_agentic_workflows_with_langgraph | agentic workflow]], such as chat history or tool retry counts <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Nodes** Represent individual agents or steps within the workflow <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Edges** Define how agents are connected, including conditional connections <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Checkpoints and Threads** Used for managing persistent state across multiple executions and sessions <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Examples of Agentic Workflows

LangGraph excels at defining [[examples_of_agentic_workflows_with_langgraph | agentic workflows]] that would otherwise be difficult to code without clear structure <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Chart Generation Workflow

An [[examples_of_agentic_workflows_with_langgraph | agentic workflow]] for generating charts involves multiple steps and conditional routing <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>:
1.  **User Input** The user requests a chart (e.g., "generate a chart of the average temperature in Alaska over the past decade") <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
2.  **Researcher Agent** Gathers information to create the chart <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Router** Determines the next step based on the researcher's response <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   If more research or tool calls (e.g., web search) are needed, it loops back to the Researcher <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   If research is complete, it proceeds to the Chart Generator <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
4.  **Chart Generator Agent** Invokes tools to execute code and generate the chart, then sends it back to the user <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Code Execution Workflow

LangGraph can manage complex code execution workflows, even embedding one workflow as a step within another <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>:
1.  **User Question/Request** (e.g., "generate a chart") <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Generate Code** The system generates preamble, imports, and code <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
3.  **Import Code** Attempts to import the generated code <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   If import fails, it loops back to regenerate code <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   If import succeeds, it proceeds to execute the code <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
4.  **Execute Code** Runs the code <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   If execution fails, it restarts the whole process to try again <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   If execution succeeds, the final answer is returned to the user <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Agent-Tool Loop Workflow

A common pattern is an agent-tool interaction loop <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>:
1.  **Agent Decision** An agent decides to invoke a tool (e.g., creating a project in Asana) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  **Tool Execution** The tool runs, and its output is returned to the agent <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
3.  **Agent Re-evaluation** The agent then makes one of two choices <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>:
    *   **Return to User** Gives the final response to the user <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   **Invoke More Tools** Decides to invoke more tools based on the user's request, looping back to the tool execution step (e.g., after creating a project, creating tasks within it) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

This loop can repeat several times until the agent determines all necessary actions are complete <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. LangGraph makes implementing such loops very beneficial <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Practical Implementation: Task Management Agent

LangGraph can significantly improve the cleanliness and scalability of [[setting_up_ai_agents_with_python_and_langchain | AI agent code]], replacing recursive function calls with a structured graph <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Refactoring a Task Management Agent

Previously, a task management [[setting_up_ai_agents_with_python_and_langchain | AI agent]] might use a recursive `prompt_AI` function for tool invocation and response generation <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. While concise, this approach is not extensible for features like human-in-the-loop, diverse tool call handling, or dynamic LLM switching <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. LangGraph transforms this into a scalable architecture.

The structure of the LangGraph implementation for a task management agent involves:
*   **Tools Module** Contains functions for interacting with tools like Asana and tool mappings <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Runnable Module** Where the LangGraph logic is implemented from scratch <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Main Script** Handles the [[setting_up_ai_agents_with_langchain_and_streamlit | Streamlit UI]] and interaction with the LangGraph runnable <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### LangGraph Implementation Steps

1.  **Imports and Model Setup**
    *   Import necessary libraries from LangGraph and [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   Load environment variables and set up the LLM (e.g., ChatOpenAI or ChatAnthropic) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   Bind tools to the AI object so the LLM can use them <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

2.  **Defining the Graph State**
    *   Create a `GraphState` that tracks variables, primarily a list of `messages` (chat history) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    *   Utilize `add_messages` functionality to append new messages without overwriting the history <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

3.  **Creating Nodes**
    *   **Call Model Node** (`call_model`) Asynchronously invokes the [[examples_of_agentic_workflows_with_langgraph | AI agent]] to stream responses <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
        *   Automatically receives `graph_state` and `configuration` (e.g., `thread_id`, `max_nodes`) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
        *   Fetches `messages` from the state, invokes the model, and updates the `messages` state with the response <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    *   **Tool Node** (`tool_node`) Handles tool invocations <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
        *   Fetches the `messages` from the state to get the latest AI message <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
        *   If the last message contains tool calls, it loops through them, invokes each tool, and adds the tool output messages to the chat history <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
        *   Updates the `messages` state with the tool response outputs <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

4.  **Defining the Router (Conditional Edge)**
    *   **Should Continue Function** (`should_continue`) Acts as a conditional edge to decide the next step <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
        *   Checks if the last message from the AI has tool calls <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
        *   If no tool calls, it returns `END` (a LangGraph literal), ending the graph execution and sending the response to the user <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
        *   If tool calls exist, it returns the string `"tools"`, directing execution to the `tool_node` <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

5.  **Building and Compiling the Workflow**
    *   Define the `workflow` based on the `GraphState` <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
    *   Add the `call_model` node (named `agents`) and `tool_node` (named `tools`) <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
    *   Set the `entry_point` to `agents` <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
    *   Add the conditional edge using `should_continue` from the `agent` node, directing to `tools` or `END` <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
    *   Add a regular edge from `tools` back to `agents` to complete the loop, allowing the agent to re-evaluate after tool execution <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
    *   Compile the workflow into a runnable `app` <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
    *   Set up persistence (e.g., in-memory SQLite saver) as a `checkpoint` to manage state across executions using a `thread_id` <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

### Integration with [[setting_up_ai_agents_with_langchain_and_streamlit | Streamlit UI]]

The compiled LangGraph runnable (`app`) is then used in the [[setting_up_ai_agents_with_langchain_and_streamlit | Streamlit UI]] instead of direct chatbot invocation <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   The runnable is initialized once using `st.resource` <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   A `thread_id` is used to maintain a single session and state persistence between executions <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
*   The `prompt_AI` function now asynchronously streams events from the LangGraph runnable using `stream_events`, yielding chunks for a typewriter-style display in the UI <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   The UI displays chat history, takes user input, adds it to the message state, and calls `prompt_AI` to get and display the streamed AI response <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

This [[integrating_langgraph_with_existing_ai_applications | integration]] results in a much simpler, yet highly extensible and scalable [[examples_of_agentic_workflows_with_langgraph | AI agent]] implementation <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## Future Possibilities

LangGraph opens up possibilities for advanced [[examples_of_agentic_workflows_with_langgraph | AI agent]] features and deployment:
*   **Human-in-the-loop**: Incorporating human intervention and approval workflows <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.
*   **LangServe**: Deploying LangGraph runnables as API endpoints for remote execution in the cloud and [[integrating_langgraph_with_existing_ai_applications | integration]] with frontends (e.g., Vercel AI SDK) <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.