---
title: Integration of mCP in AI tools
videoId: Ri3iyi3qFlI
---

From: [[colemedin]] <br/> 

Modern AI IDEs like Windsurf and Cursor offer significant productivity enhancements, even for non-coders, enabling impressive results with features such as documentation retrieval and [[mcp_integration_with_various_ai_frameworks | Claude mCP support]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, these tools frequently hallucinate code, even when provided with extensive documentation <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. A significant upgrade is needed to address these hallucination problems <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The next evolution for AI coding involves a complete paradigm shift, revolving around specialized sub-agents and Claude's [[mcp_integration_with_various_ai_frameworks | mCP]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## The Problem: Overly General AI Coding Assistants

Current AI coding assistants are too general, acting as "Jack of all trades, master of none" when it comes to coding with diverse frameworks, tools, and libraries <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Providing documentation alone is often insufficient, as they remain too general <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## The Solution: Specialized Sub-Agents via mCP

The proposed solution involves using specialized agents designed specifically to code with a particular tool or framework <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These agents can be called upon by general AI coders like Windsurf or Cursor when needed, offering the best of both general and specialized capabilities <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This approach is feasible because these specialized agents can be defined as sub-agents that function as [[mcp_integration_with_various_ai_frameworks | mCP tools]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. These tools can then be integrated into popular AI coding assistants due to the widespread adoption of Claude's mCP <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### What is mCP?

[[mcp_integration_with_various_ai_frameworks | mCP]] (Multi-Capability Protocol) is a protocol developed by Claude to [[benefits_of_standardizing_ai_tools_with_mcp | standardize the use of tools]] with large language models (LLMs) <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. It allows for the creation of [[implementing_mcp_servers_in_ai_agent_systems | servers]] that expose API endpoints for various services (e.g., GitHub, Google Drive, Discord) to an LLM dynamically <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. This enables LLMs to perform actions on behalf of the user within those services <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. [[mcp_servers_for_ai_coding | mCP servers]] are open-source and can be run locally or referenced via a cloud API endpoint, making tools available to LLMs <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Archon: An mCP Sub-Agent Example

Archon is an [[integrating_mcp_with_ai_agents | AI meta-agent]] that specializes in [[building_ai_agents_with_pantic_ai_and_mcp | building other agents using Pantic AI and LangGraph]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The goal is to evolve Archon into a robust sub-agent usable in AI coders for efficiently building agents with Pantic AI and LangGraph <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

By packaging Archon's entire workflow as a tool, it can be given to LLMs like Claude 3.5 Sonnet running in Windsurf <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. Archon's workflow includes:
*   A Reasoner model to define the agent's scope and high-level reasoning <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   A coder agent that produces the code <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   A human-in-the-loop feedback mechanism for iterative improvements <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

#### Demonstration in Windsurf

When prompted in Windsurf to "build me an AI agent using Archon that is able to search the web using Brave," Windsurf uses its [[mcp_integration_with_various_ai_frameworks | mCP support]] to call Archon <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

1.  **Thread ID Creation:** Archon first calls a tool to create a thread ID, which is necessary for managing conversation history, similar to how Windsurf operates <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
2.  **Archon Invocation:** The primary tool invokes Archon via an API endpoint <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
3.  **Workflow Execution:** Archon's internal workflow (Reasoner using 03 mini, Coder using GPT 4o performing RAG with Pantic AI documentation) executes to generate the agent code <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
4.  **Code Transfer:** Once Archon finishes, control is passed back to Windsurf, which then uses the generated code to create files like `agent.py`, `requirements.txt`, `tools.py`, and `env.example` <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This seamless control transfer between agents is a key benefit <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
5.  **Iterative Refinement:** The human-in-the-loop feature allows for iterative refinement of the agent. For example, a user can ask Archon to fix an issue like `model is none` to use `GPT 4o` <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. Archon will then use the same thread ID to continue the execution within its graph, updating the agent <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

#### Addressing Common Questions

*   **Why not just use built-in documentation features?**
    *   **Consistent Output:** Archon's agentic flow, with its Reasoner model and system prompts, ensures a very consistent output structure for files and scripts <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. General coders like Windsurf often produce varied code structures, leading to more errors <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   **Better Code Quality:** While Archon is still developing, its structured approach (e.g., self-feedback loops, breaking problems into smaller steps) promises more robust and higher-quality code than a general coder spewing out all code at once <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Why generate a thread ID for a stateless mCP server?**
    *   Although [[implementing_mcp_servers_in_ai_agent_systems | mCP servers]] are generally stateless, Archon as a sub-agent tool needs to maintain conversation history for its stateful workflow (Reasoner -> Coder -> Human-in-the-loop) <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. The thread ID acts as an identifier to map the Windsurf conversation to a specific Archon run, allowing for iterative improvements <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The LLM remembers to pass this ID in future calls <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Technical Setup of Archon mCP Server

The Archon mCP server is implemented using a Python script leveraging `fastAPI` and the `mCP python SDK` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. It defines two main tools:
1.  One to create the necessary thread ID <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
2.  Another to invoke Archon itself through a dedicated API endpoint <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

The core LangGraph for Archon remains unchanged; it is simply wrapped within this Fast API endpoint <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
Crucially, the docstrings within the Python function definitions of the mCP server inform the LLM when and how to use these tools <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. These strings are embedded directly into the prompt for the LLM (e.g., Claude 3.5 Sonnet in Windsurf) <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This allows for specific instructions, such as generating a thread ID at the start of building an AI agent and reusing it for subsequent iterations <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.

A setup script automates the creation of the virtual environment and generates the mCP configuration JSON for use in AI coders like Cursor or Windsurf <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

## [[benefits_of_mcp_for_ai_development | Benefits of mCP for AI Development]] and Future Outlook

[[integrating_mcp_with_ai_agents | Integrating MCP with AI agents]] like Archon offers immense potential for [[creating_custom_ai_agent_frameworks_with_mcp | creating custom AI agent frameworks with MCP]] <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. It allows developers to focus on the agentic flow of specialized sub-agents without worrying about the logistics of file creation and editing, as AI coders handle that <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

Future plans for Archon include:
*   Adding self-feedback loops <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.
*   Breaking down agent creation into smaller, manageable steps <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.
*   Developing a comprehensive tool library, which would provide pre-made tools (e.g., a Brave search tool) to prevent hallucinations related to external APIs <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.