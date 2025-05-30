---
title: Agentic workflows and human in the loop concept
videoId: U6LbW2IFUQw
---

From: [[colemedin]] <br/> 

Building powerful [[difference_between_ai_agents_and_llm_workflows | AI agents]] and [[examples_of_ai_agents_and_workflows | AI agent systems]] involves leveraging robust frameworks and tools for [[agentic_workflows_and_ai_technology | agentic workflows]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While many guides offer basic starts, the goal is often to create the "best of the best" [[difference_between_ai_agents_and_llm_workflows | AI agents]] without excessive complexity <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Pydantic AI and LangGraph for Agentic Workflows

[[examples_of_agentic_workflows_with_langgraph | LangGraph]] is described as an incredible [[agentic_workflows_and_ai_technology | agentic workflow]] tool <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The combination of Pydantic AI (an agent framework) with [[examples_of_agentic_workflows_with_langgraph | LangGraph]] is considered a "GameChanger" for building [[examples_of_ai_agents_and_workflows | AI agent systems]] that can perform almost anything <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, including an agent that can build other [[difference_between_ai_agents_and_llm_workflows | AI agents]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Pydantic AI is a Python agent framework that simplifies the creation of [[difference_between_ai_agents_and_llm_workflows | AI agents]] while maintaining customizability and control over aspects like testing, function calling, and chat history <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. [[examples_of_agentic_workflows_with_langgraph | LangGraph]], on the other hand, is not an agent building framework, but an orchestrator <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It allows combining [[difference_between_ai_agents_and_llm_workflows | AI agents]] (built with tools like Pydantic AI) into a workflow, enabling them to collaborate and reason together on shared problems or conversations <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

A key feature of [[examples_of_agentic_workflows_with_langgraph | LangGraph]] is its "low-level abstractions" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, meaning it provides the necessary control and customizability, unlike high-level frameworks (e.g., CrewAI) which might limit intricate developments <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Both [[examples_of_agentic_workflows_with_langgraph | LangGraph]] and Pydantic AI emphasize maintaining user control <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Visualizing Workflows
One of the advantages of [[examples_of_agentic_workflows_with_langgraph | LangGraph]] is its ability to visualize workflows without extra effort, by using the `LangGraph Dev` command to spin up a studio UI <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This visualization helps understand the flow of different nodes (agents) and their connections <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Archon Example: Building AI Agents with LangGraph
Archon is an [[difference_between_ai_agents_and_llm_workflows | AI agent]] built to create other [[difference_between_ai_agents_and_llm_workflows | AI agents]], powered by Pydantic AI and [[examples_of_agentic_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. Version 2 of Archon leverages an [[agentic_workflows_and_ai_technology | agentic workflow]] with both frameworks to build Pydantic AI agents <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

The Archon V2 workflow typically involves:
1.  **Reasoning LLM**: Takes user requirements to build an agent and creates a scope document. It also identifies relevant Pydantic AI documentation pages for context <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
2.  **Coder Agent**: Uses the scope document and relevant documentation (via RAG) to code an [[difference_between_ai_agents_and_llm_workflows | AI agent]] <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
3.  **Iterative Feedback Loop**: The coder agent builds, then receives feedback from the user, and iterates <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>. This loop can continue until the user is satisfied <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.
4.  **Final Agent**: Summarizes the conversation, provides the final agent code, and instructions for running it <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

This structured approach significantly improves results compared to a single-agent model, by providing more information and context to the coder agent <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

### Human-in-the-Loop Concept
A crucial aspect demonstrated in [[agentic_workflows_and_ai_technology | agentic workflows]] is the "human in the loop" concept <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. Since LLMs can "hallucinate all the time" <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>, involving human approval is practical for almost any [[difference_between_ai_agents_and_llm_workflows | AI agent]] <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This allows humans to approve actions or provide feedback at various stages of a workflow <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

In [[examples_of_agentic_workflows_with_langgraph | LangGraph]], this is implemented using an "interrupt" <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. After a node completes its task (e.g., the coder agent generates code), an interrupt can pause the workflow, return control to the user interface, and wait for user input (feedback) <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. This new user input then updates the state, allowing the graph to resume execution, often looping back to the coder agent for revisions <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>.

### Warnings and Considerations
While powerful, there's a warning against "over-engineering" with graph-based [[agentic_workflows_and_ai_technology | agentic workflows]] <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. They are not the right tool for every job and can be overkill for simpler use cases <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. However, for "super robust [[agentic_workflows_and_ai_technology | agentic workflows]] with a lot of [[difference_between_ai_agents_and_llm_workflows | agents]] working together in non-deterministic ways," they are highly effective <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.