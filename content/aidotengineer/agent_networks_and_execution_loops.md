---
title: Agent networks and execution loops
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

## Introduction to Agents <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
The year 2025 is anticipated to be the "year of Agents," marking a shift from AI functioning merely as an assistant to becoming a co-worker <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. OpenAI has been actively working with customers and internal teams on [[agent_native_companies | agentic products]] like deep research and operator <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This work has led to identifying prevalent patterns and anti-patterns in agent development <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### Defining an AI Agent <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
An AI agent is an application that consists of a model with instructions, typically in the form of a prompt <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. It has access to tools for information retrieval and interaction with external systems <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Crucially, an agent is encapsulated in an [[agent_loop_persistence_and_distributed_environments | execution loop]] where the model itself controls the termination <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### The Agent Execution Cycle <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
Within each [[agent_loop_persistence_and_distributed_environments | execution cycle]], an agent operates as an entity that:
1.  Receives instructions in natural language <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
2.  Determines whether to issue any tool calls <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
3.  Runs those tools <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
4.  Synthesizes a response using the tool's return values <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
5.  Provides an answer to the user <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
The agent may also decide it has met its objective and terminate the [[agent_loop_persistence_and_distributed_environments | execution loop]] <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## Lessons in Building and Scaling Agents <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>

### 1. Start with Primitives, Abstract When Necessary <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>
When designing an AI agent that orchestrates multiple models, retrieves data, reasons over it, and generates output, there are two initial choices:
*   **Starting with Primitives:** Making raw API calls, logging results, and handling failures <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Starting with a Framework:** Picking an abstraction that handles many details <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

While frameworks are enticing for quick proofs of concept <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, they can lead to a lack of understanding of the system's behavior or underlying primitives, deferring critical design decisions <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Without knowing constraints, optimization is difficult <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

A more effective approach is to first build with primitives to understand task decomposition, failure points, and areas for improvement <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. Abstraction should be introduced only when repeating efforts, such as reimplementing an embedding strategy or model graders <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The focus for scalable agent development should be on understanding data, failure points, and constraints, rather than simply choosing the right [[agent_frameworks_and_orchestration_layers_in_ai_engineering | framework]] <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### 2. Start Simple (Single Agent) <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
Often, teams prematurely jump into designing [[multiagent_systems_in_technical_workflows | multi-agent systems]], with agents calling agents or dynamically coordinating tasks <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. This can create unknowns and offer limited insight <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

A better strategy is to begin with a single agent purpose-built for a specific task <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Deploying this single agent in production with a limited user set allows for observing its performance and identifying real bottlenecks, such as hallucinations, high latency, or poor retrieval accuracy <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. Complexity should only be increased incrementally as more intense failure cases and constraints are discovered <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. The goal is to build a system that works, not necessarily a complicated one <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### 3. Graduate to a Network of Agents with Handoffs <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>
For handling more complex tasks, the concept of a [[multiagent_systems_in_technical_workflows | network of agents]] and handoffs becomes crucial <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

*   **[[multiagent_systems_in_technical_workflows | Network of Agents]]:** A collaborative system where multiple agents work in concert to resolve complex requests or perform a series of interrelated tasks <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This allows for specialized agents to handle subflows within a larger [[agent_continuations_for_ai_workflows | agentic workflow]] <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Handoffs:** The process by which one agent transfers control of an active conversation to another agent <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. Similar to a phone call transfer, but with the ability to preserve the entire conversation history, allowing the new agent to seamlessly continue <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

**Example: Customer Service Flow** <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>
In a fully automated customer service flow using a network of agents and handoffs, different models can be applied to specific jobs:
*   GPT-4o Mini can perform triage on incoming requests <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   GPT-4o can manage the conversation with the user on a dispute <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.
*   An O3 Mini reasoning model can handle accuracy-sensitive tasks, like checking refund eligibility <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

Handoffs effectively maintain conversation history and context while allowing for changes in the model, prompt, and tool definitions, providing flexibility for a wide range of scenarios <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### 4. Implement Guardrails <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>
Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and ensuring system integrity <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

*   **Keep Prompts Simple:** Model instructions should be kept simple and focused on the target task to ensure maximum interoperability and predictable accuracy improvements <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Parallel Execution:** Guardrails should not be part of the main prompts, but run in parallel <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. The availability of faster and cheaper models like GPT-4o Mini makes this approach more accessible <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Deferred High-Stakes Actions:** High-stakes actions, such as issuing a refund or displaying personal account information, should be deferred until all guardrails have completed their checks <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

For example, an input guardrail can prevent prompt injection, while output guardrails can be applied to the agent's response <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

## Summary of Agent Development Principles <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>
To build and scale AI agents effectively:
1.  Use abstractions minimally <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
2.  Start with a single agent <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
3.  Graduate to a [[multiagent_systems_in_technical_workflows | network of Agents]] when addressing more intense failure cases <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
4.  Keep prompts simple and focused on the "happy path," using guardrails to manage edge cases <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.