---
title: Agent orchestration and parallel processing
videoId: fcPUqxfrE6Y
---

From: [[aidotengineer]] <br/> 

## Building AI Agents with Primitives

Building [[ai_agents_and_agentic_workflows | AI agents]] that are production-ready and scalable often involves using AI primitives rather than frameworks <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Frameworks can be bloated, slow-moving, and filled with unnecessary abstractions <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Primitives, on the other hand, have a native ability to work well in production and scale massively, similar to Amazon S3 as an object storage primitive <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

[[ai_agents_and_agentic_workflows | AI agents]] are considered a new way of writing code, changing how projects and SaaS are built <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Instead of large frameworks, the focus should be on small, composable building blocks that are useful across the stack <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Langbase aims to provide the fastest way to build production-ready [[ai_agents_and_agentic_workflows | AI agents]] by leveraging predefined, highly scalable, and composable AI primitives <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

Key AI primitives include:
*   **Memory:** An autonomous "drag engine" that can scale to store terabytes of data, often with a vector store for similarity search <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Workflow Engine:** Purpose-built for [[agent_continuations_for_ai_workflows | multi-step agent workflows]] <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Threads:** For storing and managing context and conversation history for agents <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Parser:** To extract context from various file types, like converting PDF to text <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Chunker:** To split extracted text into smaller pieces of context for efficient processing <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Tools Infrastructure:** For agents to automatically call external APIs or services <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

By using these primitives, developers can build serverless [[ai_agents_and_agentic_workflows | AI agents]] that handle heavy lifting automatically <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Agent Orchestration

[[Multiagent orchestration in AI copilot systems | Agent orchestration]] involves a primary agent managing and coordinating the tasks of multiple other agents. This is crucial for complex problems that require a division of labor.

### Agent Router Architecture
An "Agent Router" or "LLM Router" is an architectural pattern where an agent or LLM decides which other specialized agent needs to be called next <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This allows for dynamic routing of tasks to agents best suited for the job.

**Example Implementation:**
An example involves three specialized agents:
1.  **Summary Agent:** Uses Gemini for summarizing text <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
2.  **Reasoning Agent:** Uses DeepSeek Llama 70B for analysis and explanations <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
3.  **Coding Agent:** Uses Claude Sonnet for writing code <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

A "routing agent" is instructed on its job, has access to all these specialized agents, and responds with valid JSON, picking the appropriate agent for a given task <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. For instance, given the task "Why days are shorter in winter," the router correctly decides to run the reasoning agent <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

### Agent Orchestrator Worker Architecture
This is a more sophisticated form of [[multiagent_orchestration_in_ai_copilot_systems | orchestration]] where a single orchestrator agent plans and creates subtasks for multiple worker agents <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. The results from these worker agents are then synthesized by another agent to form a final output <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>. This architecture is similar to a "deep research agent" <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

**Example Implementation:**
To write a blog post on "benefits of remote work" covering productivity, work-life balance, and environmental impact:
1.  The orchestrator agent generates a list of subtasks: writing the introduction, sections on productivity, work-life balance, environmental impact, and a conclusion <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
2.  These subtasks are distributed among individual worker agents, each completing one part <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.
3.  Finally, a synthesizing agent combines all the completed subtasks into the full blog post <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

This pattern can be implemented in about 90 lines of code without a complex framework <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.

## Parallel Processing of Agents

Running [[ai_agents_and_agentic_workflows | AI agents]] in parallel is another common architecture that leverages primitives for simplicity.

**Implementation:**
In JavaScript, a set of agents (e.g., a sentiment agent, a summary agent, a decision-maker agent) can be run concurrently using `Promise.all` <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This allows multiple agents to process different aspects of an input simultaneously, significantly speeding up the overall workflow.

## Benefits of Primitives for Advanced Architectures

Using AI primitives for [[multiagent_orchestration_in_ai_copilot_systems | agent orchestration]] and parallel processing offers significant advantages:
*   **Flexibility:** It avoids being stuck with abstractions from bloated frameworks, which is crucial in a fast-moving space with new LLM paradigms emerging constantly <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
*   **Scalability:** Primitives like `langbase.memories` are designed to scale automatically, handling large amounts of data without manual intervention <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Control:** Developers retain full control over their code, as there's no "magic" or new concepts to learn beyond standard programming practices <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   **Debugging:** Building on primitives makes debugging much easier compared to navigating obscure abstractions found in frameworks <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

By building with primitives, developers can quickly build, deploy, and use production-ready agents that scale, rather than creating "silly demos" that may not <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.