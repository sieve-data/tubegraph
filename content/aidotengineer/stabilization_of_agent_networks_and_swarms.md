---
title: Stabilization of agent networks and swarms
videoId: RVN9HWKmkNU
---

From: [[aidotengineer]] <br/> 

The primary challenge with [[multiagent_systems_and_their_applications | agent swarms]] is their inherent instability when attempting to solve increasingly complex knowledge work problems, despite their potential to solve nearly any such problem if stable <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This instability stems from difficulties in perfectly observing them, the dynamic environments they operate in, and challenges in comprehensive pre-deployment [[testing_and_optimization_of_ai_coding_agents | testing and optimization of AI coding agents]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It is often unclear whether agents consistently progress towards their goals, especially when they cannot achieve them in a single step <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## The Role of Evaluations (Evals)

The general solution to stabilizing [[stateful_ai_agents | AI agents]] and workflows is through systematic evaluations, or "evals" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Simply adopting an eval stack without a systematic approach is unlikely to yield significant results <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Effective use of evaluations not only facilitates [[developing_and_optimizing_ai_agents | improvement of agents]] and workflows but also ensures the continuous development and alignment of the evaluation stacks themselves with business requirements <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

Evaluating all aspects of agent behaviors and internal representations presents a complex landscape <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This includes:
*   **Representational Aspects**: How the agent models reality, discusses it with the user, and its grounding to reality (truthfulness) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Behavioral Aspects**: Whether the agent infers the correct goals, makes progress towards them, and selects the appropriate tools <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

To begin, a clear framework for setting up evaluators is necessary <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For instance, a hotel reservation agent might require evaluators for policy adherence, accuracy of outputs, and overall appropriate behavior <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. It's crucial to have visibility into creating and maintaining large stacks of evaluators, systematically improving them over time <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## The Stabilization Loop with Model Context Protocol (MCP)

The desired outcome is a stabilization loop where an agent attempts a task, its output is evaluated by an evaluation engine, and feedback (numeric score and explanation) is returned to the agent <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This feedback enables the agent to improve its performance <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The Model Context Protocol (MCP) is the latest method for attaching agents to these evaluation engines <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Practical Examples of Stabilization

#### 1. Text Optimization Example
Using a simple text example, like "routing MCP service awesome let you access nicely" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, one can use an MCP server (e.g., Fruit Signals MCP server <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>) via a UI like Cursor <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This allows listing available evaluators or "charges" (collections of evaluators) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. By selecting a relevant charge, such as a "marketing message quality judge," the system can score the initial message, identify issues, suggest improvements, and then re-score the improved version <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This process of scoring and re-scoring can happen automatically within an agent <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

#### 2. Hotel Reservation Agent Example
Consider a hotel reservation agent (e.g., built with Pyantic AI <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>) that is explicitly instructed not to recommend competitor hotels <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Without MCP**: If a user subtly hints at interest in a competitor, the agent might inadvertently suggest the competitor, like the "Akma hotel" <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **With MCP**: By enabling the MCP server for evaluation <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, the agent invokes evaluators, such as a "hotel policy adherence evaluator" <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This allows the agent to self-correct and avoid mentioning the competitor, even if not specifically instructed to invoke that evaluator <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This demonstrates how an agent can receive feedback and improve its own behavior <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>, showing the potential for [[scaling_ai_agents_in_production | scaling AI agents in production]] to more complex scenarios <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

## Approach for Implementing Stabilization

To effectively implement this stabilization, follow these steps:
1.  **Ensure a Powerful Evaluation Platform**: Your evaluation library or platform must be robust enough to support a diversity of evaluators, manage their lifecycle, and facilitate their maintenance and [[evaluating_and_optimizing_ai_agents_and_workflows | optimization]] <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. This includes optimizing both the agent and the evaluators themselves, as running many evaluators can be costly <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
2.  **Start Manually/Offline**: Begin by running the MCP manually and offline, as demonstrated with the marketing message example <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This helps in understanding its behavior and gaining transparency into how it works (or doesn't) <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
3.  **Attach via MCP**: Finally, integrate evaluators to the agents through the MCP <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

This approach promises to make agent behavior more controllable, transparent, dynamically self-improving, and self-correcting <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. The Root Signals MCP server is available for free, and more such servers are expected to emerge, enabling various evaluation platforms and frameworks to be integrated into [[integration_of_ai_agents_into_existing_infrastructure | AI agent stacks]] <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.