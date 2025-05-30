---
title: Evolution of AI IDEs
videoId: Ri3iyi3qFlI
---

From: [[colemedin]] <br/> 

Modern [[ai_ides_and_platforms | AI IDEs]] such as Wind Surf and Cursor are widely used, even by non-coders, to achieve significant productivity gains due to features like documentation retrieval and Claude mCP support <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite these strengths, current [[ai_development_tools | AI development tools]] have notable flaws, particularly their tendency to hallucinate inaccurate code, even with extensive documentation and instructions <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This highlights a critical need for a major [[improvements_to_ai_coding_assistants | upgrade for AI coding assistants]] to address these hallucination problems <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Next Evolution: Specialized Sub-Agents

The future of [[future_of_ai_in_coding_and_development | AI in coding and development]] is moving beyond incremental [[improvements_to_ai_coding_assistants | improvements]] towards a complete paradigm shift, involving specialized sub-agents and Claude mCP (Multi-tool Cooperation Protocol) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Current [[ai_development_tools | AI coding assistants]] are often too general, acting as "jack of all trades but master of none" when it comes to coding with different [[frameworks_and_tools_for_ai_agent_development | frameworks, tools, and libraries]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Providing documentation alone is insufficient to overcome this generality, leading to [[external_knowledge_issues_in_ai_coding_tools | external knowledge issues in AI coding tools]] and less effective code generation <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

The solution involves creating specialized agents designed to code with specific tools or frameworks <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These specialized agents can be invoked by general [[ai_ides_and_platforms | AI coders]] like Wind Surf or Cursor when needed, offering the best of both general and specialized capabilities <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This approach is achievable now by defining these specialized agents as sub-agents that function as mCP tools. Their descriptions guide the general [[ai_ides_and_platforms | AI coders]] on when to use them, for instance, specifying that Archon should be used to build Pydantic AI and LangGraph agents <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Archon as an mCP Sub-Agent

Archon, an [[opensource_ai_coding_assistant_development | open-source AI meta-agent]] developed to build other [[frameworks_and_tools_for_ai_agent_development | AI agents]] using Pydantic AI and LangGraph, serves as a practical example of this concept <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It has been transformed into an mCP sub-agent and integrated into Wind Surf <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Demonstration

When prompted to build an [[frameworks_and_tools_for_ai_agent_development | AI agent]] (e.g., a web-searching agent using Brave), Wind Surf initiates a request to Archon <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

The process involves:
1.  Calling a tool to create a thread ID, which Archon uses to manage conversation history <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
2.  Invoking Archon's API endpoint <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
3.  Archon's workflow:
    *   A Reasoner model (e.g., Claude 3 Opus Mini) defines the agent's scope <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   A coder agent (e.g., GPT-4o) performs RAG (Retrieval Augmented Generation) to retrieve Pydantic AI documentation and generate the initial agent code <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
4.  Control is passed back to Wind Surf, which then creates the necessary files (e.g., `agent.py`, `requirements.txt`, `tools` file, `.env.example`) based on Archon's output <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

This seamless handoff demonstrates the effectiveness of a general [[ai_ides_and_platforms | AI coder]] relying on a specialized sub-agent for specific tasks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. The generated code for the Brave search agent, including API key setup, appears robust and well-structured <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Advantages over Built-in Documentation

Using specialized sub-agents like Archon offers distinct advantages over merely leveraging the built-in documentation features of [[ai_ides_and_platforms | AI coders]] (e.g., `@PydanticAI` in Wind Surf) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:
*   **Consistent Output:** Archon's agentic flow, including its Reasoner model and system prompts, ensures a consistent output structure for generated files and scripts, which general [[ai_ides_and_platforms | AI coders]] struggle to maintain <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Superior Code Quality:** As Archon develops with features like self-feedback loops and the ability to break problems into smaller steps, its generated code will be significantly more robust and accurate than code produced by general coders <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Iterative Refinement:** Archon's design supports a human-in-the-loop feedback mechanism, allowing users to request iterative improvements to the generated agent code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Multi-tool Cooperation Protocol (mCP)

mCP, developed by Claude, is a protocol that standardizes the use of tools with Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. It allows for the creation of servers that expose API endpoints for various services (e.g., GitHub, Google Drive, Brave Search, AWS S3), dynamically providing these tools to an LLM <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. The [[opensource_ai_coding_assistant_development | open-source community]] actively creates and shares these mCP servers <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

Archon leverages mCP by packaging its entire agent-coding workflow as a tool for [[ai_ides_and_platforms | AI coders]] <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The implementation uses FastAPI with the mCP Python SDK, defining tools to create a thread ID (for stateful conversation) and to invoke Archon's API endpoint <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. Docstrings in the tool definitions are crucial as they are included in the LLM's prompt, guiding it on when and how to use the tools <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

## [[Effective_use_of_AI_coding_assistants | Effective Use of AI Coding Assistants]] and Future Outlook

Even in its early stages, the integration of Archon as an mCP sub-agent demonstrates a powerful method for building [[frameworks_and_tools_for_ai_agent_development | AI agents]] <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. The ability to iterate on generated code through human feedback, while still relying on the sub-agent's specialized knowledge, creates a more robust development process <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. Minor adjustments, such as correcting API parameters, can quickly lead to a fully functional agent <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.

The vision for Archon includes significant expansion with more nodes, improved system prompts, and a tool library to provide pre-made components, addressing issues like API hallucinations <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. This approach allows developers to focus on the agentic flow without worrying about the logistics of file creation and editing, as the [[ai_ides_and_platforms | AI coders]] handle those aspects <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. Future plans for this [[opensource_ai_coding_assistant_development | open-source, community-driven project]] include self-feedback loops and further breaking down agent creation into smaller, manageable steps <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.