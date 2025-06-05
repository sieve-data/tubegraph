---
title: Best practices for building AI agents
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

OpenAI anticipates that 2025 will be the "year of Agents," marking a significant shift where generative AI transitions from being merely an assistant to becoming a co-worker <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Through collaborations with customers and internal teams developing agentic products, OpenAI has identified key patterns and anti-patterns in [[challenges_in_creating_effective_ai_agents | agent development]] <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Defining an AI Agent
An AI agent is an application composed of a model that receives instructions (typically via a prompt) and has access to tools for information retrieval and interaction with external systems <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This entire process is encapsulated within an execution loop, whose termination is controlled by the model itself <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

In each execution cycle, the agent:
*   Receives natural language instructions <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   Determines whether to issue tool calls <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Runs those tools <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   Synthesizes a response using the tool's return values <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   Provides an answer to the user <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   May terminate the execution loop if its objective is met <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## [[Best practices for building resilient AI workflows | Best Practices for Building AI Agents]]

OpenAI's experience has yielded four primary lessons for [[building_effective_ai_agents | developing AI agents]]:

### 1. Start with Primitives, Abstract Minimally
When designing an AI agent, you can either start with raw API calls (primitives) or use a pre-built framework <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. While frameworks offer a quick start and easy proof-of-concept <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, they often obscure how the system behaves or what underlying primitives are used, leading to deferred design decisions before understanding constraints <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Without knowing your constraints, optimizing the solution becomes difficult <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

A more effective approach is to:
*   Begin by building with primitives <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   Understand how the task decomposes <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   Identify failure points and areas needing improvement <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   Only introduce abstraction when you find yourself reinventing the wheel (e.g., re-implementing embedding strategies or model graders) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

The focus should be on understanding data, failure points, and constraints, rather than on choosing the "right" framework <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The goal is to start simple, optimize as needed, and abstract only when it enhances the system <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

### 2. Start Simple, Scale Incrementally
Teams often prematurely jump into designing complex multi-agent systems, which can create many unknowns and limit insights <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. A recommended approach is to:
*   Start with a single agent purpose-built for a specific task <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   Deploy it into production with a limited user set <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   Observe its performance to identify real bottlenecks, such as hallucinations, low adoption due to latency, or inaccuracy from poor retrieval <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   Incrementally improve the system based on identified underperformance and user needs <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

Complexity should only increase as more intense failure cases and constraints are discovered <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>; the ultimate goal is a functional system, not a complicated one <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### 3. Leverage Networks of Agents and Handoffs for Complexity
For more complex tasks, a [[developing_ai_agents_for_productivity | network of agents]] combined with handoffs can be highly effective <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Network of Agents**: A collaborative system where multiple specialized agents work in concert to resolve complex requests or perform interrelated tasks <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. These specialized agents handle sub-flows within a larger agentic workflow <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
*   **Handoffs**: The process by which one agent transfers control of an active conversation to another agent <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This is analogous to a phone call transfer but allows the entire conversation history to be preserved, enabling the new agent to seamlessly continue the interaction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

This approach ensures the right tools are brought to the right job <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. For example, in a customer service flow, a cheaper, faster model like GPT-4o Mini can perform initial triage, while a more capable model like GPT-4o manages the main conversation, and a reasoning-optimized model handles accuracy-sensitive tasks like refund eligibility checks <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Handoffs, by maintaining context while swapping models, prompts, and tool definitions, provide sufficient flexibility for a wide range of scenarios <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### 4. Implement Guardrails in Parallel
Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and maintaining system integrity <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

Key recommendations for guardrails:
*   Keep model instructions simple and focused on the target task to ensure maximum interoperability and predictable accuracy/performance improvements <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Do not** make guardrails part of your main prompts <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. Instead, run them in parallel <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. The availability of faster and cheaper models (e.g., GPT-4o Mini) makes this parallel execution more accessible <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   For high-stakes tool calls or user responses (e.g., issuing refunds, displaying personal account information), defer execution until all guardrails have returned their results <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

For instance, an input guardrail can prevent prompt injection, while output guardrails validate the agent's response <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. By keeping prompts focused on the "happy path" and using guardrails for edge cases, systems become more robust <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

These lessons form the foundation for effective and scalable [[building_effective_ai_agents | AI agent development]], addressing many [[challenges_and_solutions_in_building_ai_agents | challenges and solutions in building AI agents]] and providing [[strategies for effective AI implementation | strategies for effective AI implementation]] <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.