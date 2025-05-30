---
title: Using Pantic AI and Lang Graph
videoId: AgN3RHSZGwI
---

From: [[colemedin]] <br/> 

Complex problems yield better results when tackled by specialized teams, and the same principle applies to AI agents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Individual AI agent expertise, when combined, creates exponentially better solutions because AI agents work more effectively when their roles and goals are narrow <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

Large Language Models (LLMs) can become overwhelmed quickly when too many instructions and tools are added, leading to hallucinations <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. A solution to this is fragmenting an AI agent into different sub-agents, each handling distinct components <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This approach can elevate AI agents to the next level <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Parallel Agent Architecture

Creating an army of specialized agents requires careful consideration of problem splitting, tool assignment, combining agent work, and managing response times <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The parallel agent architecture addresses these challenges by allowing a group of specialized agents to run simultaneously to achieve a common goal <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

This architecture is considered one of the most important for agents <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It can be implemented effectively using frameworks like [[Pantic AI framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

According to an Anthropic article on building effective agents, the parallelization architecture involves:
1.  **Input**: A user's input is fed into multiple AI agents <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Specialized Agents**: Each agent, with its own instructions and tools, tackles a specific part of the problem <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
3.  **Aggregator/Synthesizer**: An LLM-based agent takes the parallel outputs from each specialized agent and combines them into a nicely formatted, comprehensive output for the end-user <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This differs from a non-LLM aggregator by using another AI agent for synthesis <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

> "Frameworks provide a level of abstraction that can sometimes be dangerous, so you have to understand how these frameworks work under the hood" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Travel Planner Assistant Example

A practical demonstration of the parallel agent architecture is a travel planner assistant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This assistant, while seemingly manageable as a single agent, benefits from specialized sub-agents for different components like flight, hotel, and activity recommendations <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

The workflow involves:
1.  **Information Gathering**: An initial loop collects necessary details from the user (e.g., origin, destination, trip duration) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
2.  **Parallel Planning**: Once all information is gathered, specialized agents (Flight, Hotel, Activity) plan their respective parts of the trip simultaneously <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  **Synthesizer**: A final agent takes the recommendations from all parallel agents and summarizes them into a neat package for the user <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

A Streamlit user interface allows users to input preferences (airlines, hotel amenities, budget) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. When a trip is requested, the specialized sub-agents execute in parallel, and their outputs are combined and streamed to the user interface <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. For simplicity, this example uses mocked flight, hotel, and weather data <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Archon: An Advanced Use Case

For a full-fledged application of the parallel agent architecture, Archon, an open-source AI agent that builds other AI agents, is a relevant example <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Archon autonomously refines the AI agent code it produces, kicking off a parallel workflow with agents to refine prompts, tools, and the agent itself <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Archon can integrate with AI IDEs via its MCP server <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## [[Pantic AI features and implementation | Building AI Agents with Pantic AI]]

[[Pantic AI framework | Pantic AI]] agents are built in three distinct parts:

1.  **Defining Dependencies**: These are external connections or parameters needed by the agent's tools, such as API keys or database connections <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. For the flight agent, this includes preferred airlines provided by the user <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Defining the Agent Itself**: This involves specifying the Large Language Model (LLM) to use, the system prompt outlining its role and goals, its dependencies, and other parameters like automatic retries <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
3.  **Defining Tools**: Tools are functions that the agent can call to perform specific actions <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. A Python decorator tells [[Pantic AI framework | Pantic AI]] that a function is a tool for the agent <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. The function's docstring specifies when and how the agent should use the tool, including its purpose and required arguments (e.g., origin, destination, date for a flight search) <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. The `run_context` parameter injects dependencies into the tool function <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Tools return a JSON string back to the LLM for reasoning <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

### Specialized Agents in the Travel Planner

*   **Flight Agent**: Uses mock data to simulate flight search based on origin, destination, date, and user's preferred airlines <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Hotel Agent**: Takes amenities and budget level as dependencies <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. Uses mock data to filter and sort hotel options based on price and amenities <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Activity Agent**: No specific dependencies beyond the core agent definition <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. Includes a tool to look up mock weather data based on date and city to recommend indoor or outdoor activities <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Final Synthesizer Agent**: The primary role is to combine recommended hotels, flights, and activities into a concise summary <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. It does not have its own tools but can be extended to validate outputs from other agents <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   **Info Gathering Agent**: Crucial for gatekeeping the process <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. It uses [[Pantic AI features and implementation | Pantic AI's structured outputs]] to guarantee that every response contains key pieces of information (destination, origin, max hotel price, dates) needed by the specialized sub-agents <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. A boolean value (`is_all_details_given`) determines if all necessary information has been provided, controlling the flow of the [[Building AI agent workflows with LangGraph | LangGraph]] workflow <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. This agent is conversational, building up message history over time <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## [[Building AI agent workflows with LangGraph | Building LangGraph Workflows]]

[[Building AI agent workflows with LangGraph | LangGraph]] implementations also consist of three main parts:

1.  **Defining the State**: These are the key pieces of information tracked throughout the workflow's execution, such as user messages, conversation history, travel details, user preferences, and results from agent executions <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. A `StateGraph` object is initialized with this defined state <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
2.  **Defining Nodes**: Each node in the graph encapsulates specific logic, which can be an AI agent invocation or deterministic code <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
3.  **Setting up the Graph**: This involves taking the defined state and nodes, adding them to a graph instance, and connecting them with edges <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.

### LangGraph Implementation Details

*   **Info Gathering Node**: Invokes the `Info Gathering agent`, managing conversation history and handling [[Pantic AI features and implementation | Pantic AI's structured outputs]] by converting between JSON (for database storage) and Pantic AI's object format <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>. It uses `run_stream` to output tokens in real-time <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>.
*   **Parallel Nodes (Flight, Hotel, Activity)**: These nodes get necessary travel details and user preferences from the graph state <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>. They invoke their respective specialized agents synchronously (`.call()`) to get recommendations <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Synthesizer Node**: Gathers the results from all parallel agents (flight, hotel, activity) from the graph state <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. It constructs a prompt asking the synthesizer agent to summarize these recommendations into a comprehensive travel plan <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. The output is streamed to the user using a `stream_text` function <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   **Conditional Edges and Routing**: A routing function (e.g., `is_all_details_given`) determines the flow of the graph based on the state <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. If all required travel details are present, it returns a list of nodes to execute in parallel, enabling simultaneous execution <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>. Otherwise, it routes back to the "get next user message" node.
*   **Human-in-the-Loop (Interrupts)**: The "get next user message" node uses a LangGraph concept called an "interrupt" to pause the workflow and wait for user input <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. Once input is received, the graph resumes, feeding the new information back to the Info Gathering agent <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **Memory**: A simple memory saver (e.g., in RAM) can be used to remember the graph's state during human-in-the-loop interruptions <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>. For production, persistent options like SQLite or PostgreSQL memory savers can be used <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.

### Integrating LangGraph with Streamlit

The [[integrating_langgraph_with_existing_ai_applications | LangGraph]] instance is imported into the Streamlit UI script <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>. The `ainvoke` function is used to call the graph <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>:
*   For the first message, an `initial_state` is provided, including user input and preferences <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.
*   For subsequent messages (after an interrupt), the `resume` directive is used to pass the new user input, continuing the conversation <a class="yt-timestamp" data-t="00:37:49">[00:37:49]</a>.
*   `stream_mode="custom"` allows the `writer` object to pass into the nodes, enabling real-time streaming of [[Pantic AI features and implementation | Pantic AI]] agent outputs to the frontend <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

## Conclusion

The parallel agent architecture, facilitated by frameworks like [[Pantic AI framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]], allows for the creation of specialized AI agents that run in parallel <a class="yt-timestamp" data-t="00:40:52">[00:40:52]</a>. This approach is highly efficient and transformative, enabling the solution of complex problems that would be difficult for a single AI agent <a class="yt-timestamp" data-t="00:41:05">[00:41:05]</a>. This method unlocks the next level of [[developing_ai_agents_with_lang_chain_and_lang_graph | building agentic systems]] that are significantly more powerful <a class="yt-timestamp" data-t="00:40:59">[00:40:59]</a>.