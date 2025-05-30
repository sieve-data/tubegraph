---
title: Development and setup of the Archon AI agent
videoId: Ri3iyi3qFlI
---

From: [[colemedin]] <br/> 

The landscape of AI coding assistants, such as Windsurf and Cursor, has significantly boosted developer productivity with features like documentation retrieval and Claude MCP support <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, these general-purpose tools frequently "hallucinate awful code," even with extensive documentation and instructions <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This highlights a need for a significant upgrade to tackle hallucination problems <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The next evolution in AI coding involves a complete paradigm shift: the use of specialized sub-agents <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This concept centers around [[creating_specialized_ai_agent_armies_with_archon | specialized agents]] designed to code with specific tools or frameworks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These sub-agents can be invoked by general AI coders like Windsurf or Cursor when their particular expertise is required <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Introducing [[Introduction to Archon | Archon]]

[[Introduction to Archon | Archon]] is an AI meta-agent, an agent that builds other AI agents using Pydantic AI and LangChain <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>. It began as a Streamlit interface <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> but has evolved to integrate as a sub-agent within AI coding environments <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.

### The Problem with General AI Coders

AI coding assistants are often "Jack of all trades but also the master of none" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Providing them with documentation for a specific framework is often insufficient because they remain too general <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### The Solution: Specialized Sub-Agents via MCP

The Multi-agent Communication Protocol (MCP), developed by Claude, standardizes the use of tools with large language models (LLMs) <a class="yt-timestamp" data-t="01:28:56">[01:28:56]</a>. This protocol allows for the creation of servers that expose API endpoints for various services (e.g., GitHub, Google Drive, Discord) <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. When an MCP server is given to an LLM, the LLM gains dynamic access to these tools <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. Many third-party MCP servers already exist, and [[Archon as an opensource AI agent builder | Archon]] is becoming one of them <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>.

## [[Archon AI agent builder | Archon]] as an MCP Sub-Agent

[[Archon AI agent builder | Archon]] is integrated into AI coders like Windsurf by transforming its capabilities into an MCP tool <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. For example, Claude 3.5 Sonnet running in Windsurf can use [[Archon AI agent builder | Archon]] as a specialized tool for building Pydantic AI and LangChain agents <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

### [[Archons AI agent building process | Archon's Agentic Flow]]

[[Archons AI agent building process | Archon's agent building process]] leverages a LangGraph graph that defines a full workflow for coding agents <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This workflow includes:
*   **Reasoner Model**: Defines the scope for building the agent and high-level reasoning <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Faster Coder Agent**: Produces the actual code <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Human-in-the-Loop Feedback Loop**: Allows for iterative improvements based on user input <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

This entire workflow is packaged as a single tool for AI coders <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Why Not Just Use Built-in Documentation Features?

While AI coders like Windsurf and Cursor have built-in documentation retrieval features (e.g., `@PydanticAI`, `@LangGraph`) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, [[Archon AI agent builder | Archon]] offers distinct advantages:
1.  **Consistent Output**: [[Archons AI agent building process | Archon's agentic flow]], including its Reasoner model and system prompts, ensures a very consistent output structure for generated files and scripts <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. General coders tend to produce varied code every time <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
2.  **Robust Code Quality**: [[Archon AI agent builder | Archon]] is designed to produce better code <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. As it evolves with self-feedback loops and the ability to break problems into smaller steps, it will be significantly more robust than a general coder that "spews out all the code at once" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Managing State within MCP

One challenge with using [[Archon AI agent builder | Archon]] as an MCP sub-agent is that MCP servers are typically stateless <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. However, [[Archon AI agent builder | Archon]], as a sub-agent tool, needs to maintain conversation history to facilitate its iterative human-in-the-loop feedback loop <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This is managed by generating a "thread ID" at the start of an agent-building conversation, which the LLM must remember and pass into future calls to [[Archon AI agent builder | Archon]] <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This ensures that the current Windsurf conversation maps to the correct [[Archons AI agent building process | Archon]] run <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Technical Setup of the [[Archon AI agent builder | Archon]] MCP Server

The [[Archon AI agent builder | Archon]] MCP server is implemented in Python using FastAPI and the MCP Python SDK <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Tool Definitions**:
    *   One tool creates the necessary thread ID for conversation management <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
    *   A second tool invokes [[Archon AI agent builder | Archon]] itself via a FastAPI API endpoint <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. This endpoint interacts with [[Archons AI agent building process | Archon's LangGraph graph]] <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Tool Descriptions**: Docstrings within the function definitions of the MCP server are crucial <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. These strings act as instructions, telling the LLM when and how to use the tools. For example, they instruct Claude to generate a thread ID before running [[Archon AI agent builder | Archon]] for the first time, and to reuse the same thread ID for subsequent iterations <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

[[Archon AI agent builder | Archon]] can still be used directly via its Streamlit interface or as an API endpoint with a custom frontend, offering flexibility <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

### Simplified Setup

A Python script (`setup_mcp.py`) is provided to simplify the setup process <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>. This script sets up the virtual environment and generates the MCP configuration (JSON for Windsurf/Claude desktop, or instructions for Cursor) <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Demonstration: Building a Brave Search Agent with [[Archon AI agent builder | Archon]] and Windsurf

A demonstration showcased [[Archon AI agent builder | Archon]] building an AI agent capable of searching the web using Brave <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
1.  **Initial Prompt**: The user instructed Windsurf to "Build me an AI agent using [[Archon AI agent builder | Archon]] that is able to search the web using Brave" <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
2.  **Thread ID Creation**: Windsurf first called the MCP tool to create a thread ID, which was then passed to [[Archon AI agent builder | Archon]] for all future calls <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
3.  **Agent Generation**: [[Archon AI agent builder | Archon]] (using `03 mini` for the Reasoner and `GPT 40` for the coder) created the agent's initial scope, performed RAG to get Pydantic AI documentation, and generated the necessary files (e.g., `agent.py`, `requirements.txt`, `tools` file, `.env.example`) <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Windsurf then implemented these files <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
4.  **Human-in-the-Loop Feedback**: When the initial `agent.py` had `model = none`, the user requested [[Archon AI agent builder | Archon]] (via Windsurf) to fix it to use `GPT 40` <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. [[Archon AI agent builder | Archon]] was invoked with the same thread ID, directly engaging the coder agent to make the correction <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
5.  **Testing**: After minor manual fixes (related to Brave API specifics, not [[Archon AI agent builder | Archon]]'s core logic or Pydantic AI/LangChain), the generated Brave search agent was successfully run in a Streamlit interface, accurately answering questions like "what is the net worth of Elon Musk" by leveraging its web search tool <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## [[Future Plans for Archon and AI Agent Development | Future Plans for Archon]]

[[Future Plans for Archon and AI Agent Development | Archon]] is still in its early stages <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Planned enhancements include:
*   Adding more nodes to its LangGraph workflow <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   Improving system prompts <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   Implementing self-feedback loops <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   Breaking down agent creation into smaller steps <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
*   Developing a tool library with pre-made tools (e.g., a Brave tool to prevent API hallucinations) <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

The integration of [[Archon AI agent builder | Archon]] into AI IDEs as an MCP server allows for robust agentic flows without needing to manually handle file creation and editing, as the AI coders manage these logistics <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. [[Archon AI agent builder | Archon]] is a community-driven project, welcoming contributions and suggestions <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.