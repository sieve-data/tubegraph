---
title: Introduction to Archon
videoId: GjR5UsVGE60
---

From: [[colemedin]] <br/> 

[[archon_ai_agent_builder | Archon]] is an [[archon_as_an_opensource_ai_agent_builder | open-source AI agent]] designed to literally build other AI agents <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It serves as both a [[archon_as_a_teaching_tool | teaching tool]] and is being developed to become a powerful AI agent capable of spinning up other agents on demand <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The development is being conducted publicly to allow for community engagement, learning, and contributions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Need for Specialized AI Agents
Coding is identified as the most significant and robust use case for AI currently, a focus shared by companies building large language models (LLMs) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. While many generalist AI coders exist (e.g., Windswept, Cursor, Klein), there is a lack of specialized AI agents that excel at specific frameworks or problem-solving <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Specialized tools like Bolt and Lovable create front ends, but a gap exists for an AI coding assistant that can create, run, and iterate on other AI agents <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This is critical because AI agents are expected to dominate the future software landscape <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. [[archon_ai_agent_builder | Archon]] fills this gap, acting like Bolt but for agents <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## How [[archon_ai_agent_builder | Archon]] Operates
[[archon_ai_agent_builder | Archon]] can be run in two primary ways:
1.  **Standalone Application:** With its own dedicated interface <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Engine within AI IDEs:** It can be used as an engine to build AI agents within AI IDEs such as Windswept, Cursor, and Klein, utilizing the model context protocol (MCP) from Claude <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Within an IDE, [[archon_ai_agent_builder | Archon]] functions as a sub-agent; when the generalist AI IDE requires specialized agent intelligence, it invokes [[archon_ai_agent_builder | Archon]] to generate the necessary code, which is then returned and implemented <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### [[archons_ai_agent_building_process | Agent Building Process]]
[[archons_ai_agent_building_process | Archon]] can generate code for a basic AI agent that uses APIs (e.g., Brave API for web search) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It excels where generalist AI coders often struggle, providing specialized knowledge for frameworks like Pydantic AI and LangGraph through instructions and better RAG retrieval from documentation <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

When [[archon_ai_agent_builder | Archon]] generates an agent:
*   It informs the AI IDE which files to create <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   It produces highly accurate Pydantic AI code <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   It considers necessary environment variables, generating `.env.example` files <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   It generates a `README` file to help users get started with the new agent <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   It can iterate on existing agents, updating code without requiring a rewrite <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Logs of [[archon_ai_agent_builder | Archon]]'s activity within the MCP server are viewable in its UI, showing real-time updates <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

This combination of [[archon_ai_agent_builder | Archon]] with an AI IDE helps reduce hallucinations and generates agents more quickly and correctly <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Underlying Frameworks
[[archon_ai_agent_builder | Archon]] leverages Pydantic AI and LangGraph, chosen for their customizability and control, which other frameworks might lack due to over-abstraction <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## [[development_and_setup_of_the_archon_ai_agent | Development and Setup]]
The [[development_and_setup_of_the_archon_ai_agent | development and setup of the Archon AI agent]] has been structured in iterations to facilitate public contribution and as a [[archon_as_a_teaching_tool | teaching tool]] to demonstrate how to build complex agents <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Iterations include:
*   Starting with a simple agent <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Implementing LangGraph for a more powerful agentic flow <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Adding MCP support in version three <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   Introducing a Streamlit interface for management in the most recent version <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

[[development_and_setup_of_the_archon_ai_agent | Getting Archon up and running]] is made easy through Docker (three commands) or Python installations <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The Streamlit interface guides users through setting up environment variables, database (Superbase), documentation crawling (initially Pydantic AI docs), and MCP services <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## [[future_plans_for_archon_and_ai_agent_development | Future Plans for Archon]]
[[future_plans_for_archon_and_ai_agent_development | The vision for Archon]] is detailed within its interface, outlining extensive [[future_development_plans_for_archon | future development plans]] <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. Key aspirations include:
*   **Multi-agent coding workflows:** Splitting the primary coding agent into specialized sub-agents to handle different parts of code generation (e.g., prompt creation, tool definition, dependency management, agent instance creation) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This leverages different LLMs for different parts of a problem and avoids overwhelming single LLMs with too many instructions <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Tool library and example integrations:** Providing pre-built tools and example agents to improve agent creation, allowing [[archon_ai_agent_builder | Archon]] to pull existing tools (like web search or database querying) from a library instead of building them from scratch, reducing hallucinations <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Similarly, example agents (e.g., a weather agent) will serve as grounding points <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Expanded knowledge base:** Incorporating documentation for more frameworks like LangGraph, CrewAI, and LlamaIndex to allow [[archon_ai_agent_builder | Archon]] to work with diverse frameworks and intelligently choose the best one for a given task <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Self-feedback loops:** Enabling [[archon_ai_agent_builder | Archon]] to autonomously iterate on agents and correct hallucinations without immediate user feedback <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Self-agent execution:** A challenging feature to allow [[archon_ai_agent_builder | Archon]] to not only build but also execute agents in isolated environments with necessary services (databases, web search) using the local AI package, enabling autonomous testing and iteration <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Multi-framework support:** Broadening support beyond Pydantic AI and LangGraph to include frameworks like LangChain, CrewAI, and LlamaIndex, acknowledging diverse user preferences and use cases <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   **Autonomous framework learning:** Allowing [[archon_ai_agent_builder | Archon]] to continuously improve by adding successful agents and tools to its examples and tool library, potentially even adjusting its own system prompt over time <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   **Advanced RAG techniques:** Implementing sophisticated methods for exploring its knowledge base, such as hybrid search, reranking, and better chunking, to enhance its understanding and use of documentation <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
*   **MCP agent marketplace:** Enabling the publishing of agents built with [[archon_ai_agent_builder | Archon]] to an MCP marketplace, allowing others to use them as sub-agents within their AI IDEs or other MCP clients <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Further Integrations:** Planned integrations include LangSmith for tracing and monitoring, [[archon_ai_agent_builder | Archon]]'s availability in MCP marketplaces directly, supporting other vector databases, and integrating with the local AI package <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

[[archon_ai_agent_builder | Archon]] embodies an [[educational_framework_utilizing_archon_for_ai_development | educational framework utilizing Archon for AI development]], aiming to build powerful, practical, and non-easily replaceable AI agents while breaking down complex topics for easy understanding <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.