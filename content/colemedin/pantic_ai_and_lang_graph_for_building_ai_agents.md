---
title: Pantic AI and Lang graph for Building AI Agents
videoId: BN2ozB7LfvE
---

From: [[colemedin]] <br/> 

Building robust AI agents requires a powerful combination of frameworks, and the synergy between [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] is highlighted as exceptionally effective <a class="yt-timestamp" data-t="01:17:56">[01:17:56]</a>.

## Benefits of the Combination
The combination of [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] is considered the "most powerful combination" for building AI agents <a class="yt-timestamp" data-t="01:22:26">[01:22:26]</a>. This pairing enables the creation of sophisticated agentic workflows, leveraging both regular and reasoning Large Language Models (LLMs) through routing and graph structures <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>.

Key advantages include:
*   **Robustness** <a class="yt-timestamp" data-t="01:30:04">[01:30:04]</a>: [[building_ai_agent_workflows_with_langgraph | LangGraph]] offers enhanced capabilities in areas such as streaming, human-in-the-loop interactions, interrupts, and state management <a class="yt-timestamp" data-t="01:30:06">[01:30:06]</a>.
*   **Concise Instruction** <a class="yt-timestamp" data-t="01:18:13">[01:18:13]</a>: The approach aims to teach complex concepts in a clear and understandable manner.

While other tools like no-code platforms (n8n, Voiceflow) or frameworks (Crew AI, Llama Index, LangChain) have their merits, [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] offer a potent, albeit more complex, solution <a class="yt-timestamp" data-t="01:31:38">[01:31:38]</a>. Both are free and open source <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>.

## Project "Archon"
To demonstrate the capabilities of [[using_pantic_ai_and_lang_graph | Using Pantic AI and LangGraph]] for agent development, an open-source project named "Archon" has been initiated <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>.

### Purpose
Archon is designed as an AI agent that can build other AI agents, powered entirely by [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>. Its primary goal is instructional, serving as a teaching tool for how to build with these two frameworks <a class="yt-timestamp" data-t="01:20:09">[01:20:09]</a>. A unique aspect is its meta-capability: Archon can assist in building the very agents it teaches how to construct <a class="yt-timestamp" data-t="01:20:15">[01:20:15]</a>.

### Iterative Development
Archon is being built in iterations to gradually demonstrate increasing complexity and capability:
*   **V1** <a class="yt-timestamp" data-t="01:21:54">[01:21:54]</a>: A simple [[pantic_ai_framework | Pantic AI]] agent that can build other [[pantic_ai_framework | Pantic AI]] agents by ingesting knowledge from [[pantic_ai_framework | Pantic AI]] documentation <a class="yt-timestamp" data-t="01:21:56">[01:21:56]</a>. This version highlights the limitations of a non-agentic workflow <a class="yt-timestamp" data-t="01:21:18">[01:21:18]</a>.
*   **V2** <a class="yt-timestamp" data-t="01:22:04">[01:22:04]</a>: An agentic workflow using both [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] to build other [[pantic_ai_framework | Pantic AI]] agents more effectively than V1 <a class="yt-timestamp" data-t="01:22:06">[01:22:06]</a>. This serves as an introduction to their combined use <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.
*   **V3** <a class="yt-timestamp" data-t="01:22:11">[01:22:11]</a>: The planned next iteration will involve [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] building other agents that also utilize both [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="01:22:14">[01:22:16]</a>.

### Future Iterations and Features
Future plans for Archon include:
*   **Self-feedback loops** <a class="yt-timestamp" data-t="01:22:41">[01:22:41]</a>.
*   **Tool Library** <a class="yt-timestamp" data-t="01:22:44">[01:22:44]</a>: Allowing pre-packaged tools (e.g., for web search, Google Drive interaction, or [[building_ai_agents_with_pantic_ai_and_mcp | MCP servers]]) to be fetched as context for the LLM, reducing hallucination and improving code generation <a class="yt-timestamp" data-t="01:23:07">[01:23:07]</a>.
*   **Accessibility** <a class="yt-timestamp" data-t="01:28:46">[01:28:46]</a>: The project aims to make complex AI agent development accessible to individuals with limited Python knowledge or those accustomed to no-code tools <a class="yt-timestamp" data-t="01:28:38">[01:28:38]</a>. Archon would act as an assistant to guide users in building more robust agents <a class="yt-timestamp" data-t="01:28:40">[01:28:40]</a>.
*   **Framework Agnostic** <a class="yt-timestamp" data-t="01:32:57">[01:32:57]</a>: The ultimate goal is for Archon to support any open-source agent framework (Python, JS, Go, etc.) by ingesting their documentation, GitHub repositories, and templates <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.
*   **Browser Use Integration** <a class="yt-timestamp" data-t="01:41:02">[01:41:02]</a>: Although currently risky due to security glitches and unrefined technology <a class="yt-timestamp" data-t="01:41:34">[01:41:34]</a>, integrating browser use features is a long-term aspiration <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>.

## Focus on Capabilities, Not Just Tools
The speaker emphasizes the importance of focusing on capabilities and high-level architectural concepts rather than getting overly fixated on specific tools <a class="yt-timestamp" data-t="01:25:45">[01:25:47]</a>. Tools and LLMs are constantly evolving and can be replaced, so understanding the underlying principles of agentic workflows – such as using graph structures, combining reasoning LLMs with faster LLMs, and routing – provides long-term leverage <a class="yt-timestamp" data-t="01:26:09">[01:27:03]</a>.

While [[pantic_ai_framework | Pantic AI]] and [[building_ai_agent_workflows_with_langgraph | LangGraph]] are currently considered leading frameworks for this purpose <a class="yt-timestamp" data-t="01:26:31">[01:26:33]</a>, the learned skills are transferable to other emerging technologies <a class="yt-timestamp" data-t="01:29:57">[01:30:00]</a>.

### Human-in-the-Loop
A crucial capability for AI agents is "human-in-the-loop" functionality <a class="yt-timestamp" data-t="01:34:49">[01:34:50]</a>. This allows an agentic workflow to pause its execution at predefined points to receive feedback or approval from a user <a class="yt-timestamp" data-t="01:34:57">[01:34:59]</a>. For example, an agent researching leads and drafting emails could require human approval before sending the email, preventing potential hallucinations or errors <a class="yt-timestamp" data-t="01:35:04">[01:35:20]</a>. This is vital as current AI models are not yet fully trustworthy for autonomous actions, especially concerning sensitive tasks <a class="yt-timestamp" data-t="01:35:50">[01:36:06]</a>. This feature will be demonstrated in the Archon project <a class="yt-timestamp" data-t="01:35:43">[01:35:46]</a>.