---
title: Building AI agents using pantic AI and Lang graph
videoId: U6LbW2IFUQw
---

From: [[colemedin]] <br/> 

Building AI agents can be complex, with many guides offering only basic introductions <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. To create advanced AI agents without excessive complexity, a powerful combination involves [[pantic_ai_and_lang_graph_for_building_ai_agents | Pantic AI]] and LangGraph <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This approach allows for the creation of sophisticated AI agent systems capable of a wide range of tasks, including building other AI agents <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Understanding the Frameworks

### Pantic AI: The AI Agent Builder
[[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] is a Python agent framework designed for easily building AI agents while maintaining full customizability and control over aspects like testing, function calling, and chat history <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. It allows developers to build virtually any AI agent desired <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

Agents built with [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] generally consist of three key parts <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>:
1.  **Dependencies**: Essential requirements such as API keys or database connections that enable the agent to perform actions <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Agent Definition**: This includes the system prompt and the large language model (LLM) used by the agent <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
3.  **Tool Functions**: The actual functions that allow the agent to perform tasks on behalf of the user, such as querying a database, using Gmail, or getting weather information <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### LangGraph: The Workflow Orchestrator
LangGraph is an "orchestrator" tool, not an AI agent framework itself <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Its purpose is to combine [[Setting up AI Agents with Python and LangChain | AI agents]] built with frameworks like [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] into cohesive workflows, enabling them to work and reason together on shared problems or conversations <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

A key feature of LangGraph is its low-level abstractions <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Unlike high-level frameworks that automate many tasks (reducing code but limiting control), LangGraph provides developers with the necessary control and customizability for intricate [[Developing AI agents with Lang chain and Lang graph | AI agent development]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## [[Benefits of combining pantic AI with Lang graph | Benefits of Combining Pantic AI and LangGraph]]
[[Using Pantic AI and Lang Graph | Combining Pantic AI]] with LangGraph creates a powerful synergy <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] facilitates the easy creation of individual agents, while LangGraph orchestrates these agents into robust, non-deterministic workflows <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This allows for complex interactions and iterative processes between agents, which would be difficult to achieve with a single agent or a less flexible orchestration tool <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

For instance, a research agent workflow built with LangGraph can integrate multiple specialized agents (e.g., researcher, chart generator, router), each potentially built with [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. LangGraph defines the rules and flow between these agents, allowing for dynamic paths based on the task at hand, such as returning to a research step if initial data is insufficient <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## A Fair Warning: Avoid Over-Engineering
While powerful, it's crucial not to "over-engineer" workflows with graph-based setups <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Graph agent workflows are not always the right tool for every job; simple AI agents may suffice for less complex use cases, avoiding unnecessary complexity <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>, <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

## Archon: An Iterative AI Agent Builder

Archon is an open-source [[Developing AI agents with Lang chain and Lang graph | AI agent]] that builds other AI agents, powered by [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] and LangGraph <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. It's developed iteratively to teach [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] and LangGraph concepts, starting simple and progressing to more complex implementations <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>, <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Archon Version 1: Pantic AI Only
Archon V1 is a [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] agent designed to answer questions about code in a GitHub repository and leverage the Pantic AI documentation to build other [[Pantic AI and Lang graph for Building AI Agents | Pantic AI agents]] <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>, <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>, <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

Its knowledge base is set up by fetching [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] documentation pages via sitemap, converting them to Markdown, chunking them, and storing them in Superbase using PG Vector <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>, <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The agent uses tools to perform RAG (Retrieval-Augmented Generation) by matching chunks in the vector database, listing available documentation pages, and getting the contents of specific pages <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

Despite its ability to understand [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] concepts, V1 exhibited shortcomings, often producing code that wasn't immediately runnable, incorrectly defining agents, or missing crucial environment variables <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

### Archon Version 2: [[Using Pantic AI and Lang Graph | Pantic AI and LangGraph Combined]]
Archon V2 significantly improves upon V1 by leveraging an agentic workflow built with both [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] and LangGraph <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>, <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. This allows for a more robust and iterative process for building AI agents <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>.

The workflow of Archon V2 includes several distinct [[Developing AI agents with Lang chain and Lang graph | AI agents]] connected as nodes in a graph <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>:
*   **Reasoner LLM**: Takes user requirements and generates a comprehensive scope document, outlining the agent to be built and identifying relevant [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] documentation pages for the coder agent to reference <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>, <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
*   **Coder Agent**: This is the primary [[Pantic AI and Lang graph for Building AI Agents | Pantic AI agent]] that codes the new AI agent <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>. It uses the scope document from the Reasoner for context and performs RAG on the [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] documentation <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>, <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.
*   **Router Agent**: Determines whether the conversation should loop back to the coder agent for further iteration (based on user feedback) or proceed to the final agent <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>, <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.
*   **Final Agent**: Summarizes the conversation, provides the final AI agent code, and gives instructions for running it <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

Key LangGraph concepts demonstrated in Archon V2:
*   **State Management**: LangGraph manages a global state (e.g., messages, scope) that persists throughout the graph's execution, allowing different nodes to access and update shared information independently for each conversation <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>, <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>.
*   **Human-in-the-Loop**: The workflow incorporates user feedback loops using LangGraph's interrupt feature, allowing for human approval or correction before proceeding to the next stage <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>, <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>.
*   **Conditional Edges**: The Router agent uses conditional edges to direct the workflow based on specific criteria (e.g., user input indicating satisfaction with the generated agent) <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.

Archon V2 shows significant improvements over V1, producing more robust code and providing a structured breakdown of files, better tool definitions, and correct environment variable suggestions <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>, <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### Implementation Details
*   **Local LLMs**: Archon V2 can be configured to use local LLMs like DeepSeek R1 Distil 7B for the Reasoner and Qwen 2.5 Instruct 14B for the coding model <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.
*   **Dynamic System Prompts**: [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] allows dynamic injection of information (like the Reasoner's scope document) into an agent's system prompt, ensuring the agent's behavior is guided by overarching objectives <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.
*   **Streamlit Interface**: A basic Streamlit interface is used to interact with the [[Pantic AI and Lang graph for Building AI Agents | Pantic AI]] and LangGraph agents, providing a user-friendly way to input requests and receive outputs <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>, <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Future Plans for Archon
Archon is envisioned to evolve into a revolutionary open-source agent capable of transforming how agents are built and making coding frameworks accessible to non-coders <a class="yt-timestamp" data-t="00:50:48">[00:50:48]</a>, <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. Future iterations plan to include self-feedback loops, tool library integration, support for other frameworks like LangChain, Llama Index, and Crew AI, and autonomous framework learning <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.