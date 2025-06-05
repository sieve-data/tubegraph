---
title: Developing and optimizing AI agents
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

The year 2025 is anticipated to be a significant turning point for AI, with agentic workflows transitioning from a buzzword to a practical reality in the field <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. OpenAI has observed the emergence of [[importance_and_progress_of_ai_agents | AI agents]] and their integration into workflows <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This shift signifies a graduation for generative AI from being merely an assistant to becoming a co-worker <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

Through their experience, OpenAI has identified various [[best_practices_and_lessons_learned_in_ai_agent_development | best practices and lessons learned]] for [[building_and_improving_ai_agents | building and improving AI agents]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Defining an AI Agent

An AI agent is conceptualized as an AI application composed of several [[components_of_ai_agents | components of AI agents]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
*   **Model and Instructions** - A core model typically guided by prompts <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Tools** - Access to tools for information retrieval and interaction with external systems <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Execution Loop** - An encapsulated loop where the model controls its termination <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

In each cycle, an agent receives natural language instructions, decides whether to issue tool calls, runs those tools, synthesizes a response from the tool's output, and provides an answer. The agent can also determine if it has met its objective and terminate the execution <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

## Lessons Learned in Developing AI Agents

When building AI agents, particularly concerning [[design_challenges_for_ai_agents | design challenges for AI agents]] and [[evaluating_and_optimizing_ai_agents_and_workflows | evaluating and optimizing AI agents and workflows]], several key insights have emerged <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>:

### 1. Start Simple, Optimize When Needed, Abstract Minimally

When designing an AI agent that orchestrates multiple models, retrieves data, reasons, and generates output, there are two primary approaches <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>:
*   **Starting with Primitives** - Making raw API calls, logging results, outputs, and failures <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Starting with a Framework** - Picking an abstraction and wiring it up to handle details <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

While frameworks are enticing for quick proof-of-concept setups, they often obscure the underlying primitives and system behavior, preventing an understanding of constraints necessary for optimization <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. A better approach is to first build with primitives to understand task decomposition, failure points, and areas for improvement <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Abstraction should only be introduced when there's a clear need to avoid reinventing the wheel (e.g., for embedding strategies or model graders) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The focus should be on understanding data, failure points, and constraints, rather than just choosing a framework <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### 2. Start with a Single Agent, Then Graduate to a Network

Teams often prematurely jump into designing complex multi-agent systems with dynamic coordination and reasoning, which creates many unknowns <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. A more effective strategy is to:
*   **Start with a Single Agent** - Develop a single agent purpose-built for a specific task <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Deploy and Observe** - Put it into production with a limited user set and observe its performance <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Identify Bottlenecks** - This process helps identify real bottlenecks such as hallucinations, low adoption due to latency, or inaccuracy from poor retrieval performance <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Incrementally Improve** - Based on identified underperformance and user needs, incrementally improve the system <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

Complexity should be increased as more intense failure cases and constraints are discovered <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>; the goal is a working system, not necessarily a complicated one <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### 3. Implement Networks of Agents with Handoffs for Complexity

For more complex tasks, a network of agents combined with handoffs can be highly effective <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Network of Agents** - A collaborative system where multiple specialized agents work together to resolve complex requests or perform interrelated tasks, handling subflows within a larger agentic workflow <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   **Handoffs** - The process where one agent transfers control of an active conversation to another <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. Unlike human transfers, handoffs in AI can preserve the entire conversation history, allowing the new agent to seamlessly continue <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

This approach allows for bringing the right tools and models to the right job within a flow. For example, a customer service flow might use a smaller model (like GPT-4o mini) for initial triage, a larger model (GPT-4o) for managing the user conversation, and a reasoning-focused model (O3 mini) for accuracy-sensitive tasks like checking refund eligibility <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Handoffs, by maintaining conversation history while swapping models, prompts, and tool definitions, offer sufficient flexibility for a wide range of scenarios <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### 4. Utilize Guardrails for Safety and Integrity

Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and ensuring system integrity <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Simple Prompts** - Keeping model instructions simple and focused on the target task ensures maximum interoperability and predictable improvement in accuracy and performance <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Parallel Execution** - Guardrails should generally not be part of the main prompts but run in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The proliferation of faster, cheaper models like GPT-4o mini makes this more accessible <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Deferred Actions** - High-stakes tool calls or user responses (e.g., issuing a refund, showing personal account information) can be deferred until all guardrails have returned a clear signal <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This includes running input guardrails (to prevent prompt injection) and output guardrails on the agent's response <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

In summary, the [[best_practices_and_lessons_learned_in_ai_agent_development | lessons for developing and optimizing AI agents]] involve using abstractions minimally, starting with a single agent before graduating to a network, and keeping prompts simple while relying on guardrails for edge cases <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. These practices address common [[challenges_in_developing_ai_agents | challenges in developing AI agents]] and are crucial for [[testing_and_optimization_of_ai_coding_agents | testing and optimization of AI coding agents]].