---
title: Role of AI agents in planning and executing tasks
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

Even with the advancements of large language models (LLMs) like InstructGPT in 2022, which could follow instructions effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, general language models continue to struggle with complex instructions and multiple requirements <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This difficulty arises when developers combine all information, context, constraints, and requirements into a single prompt <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. For even seemingly simple tasks like instruction following, LLMs alone are often insufficient <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This is where [[importance_and_progress_of_ai_agents | AI agents]] become crucial <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## What is an AI Agent?

The precise definition of an [[importance_and_progress_of_ai_agents | AI agent]] can be debated <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, from an engineering perspective, what matters is functionality <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Various approaches are sometimes referred to as agents, including:
*   **LLM as a Router** A routing model directs queries to specialized LLMs <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **[[implementing_function_calling_and_agents_in_ai | Function Calling]]** LLMs are provided with external tools and APIs, allowing them to interact with the world, such as through Google search <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **React (Reason and Act)** This framework, usable with any language model, follows a "thought then act upon that thought and observe" loop. It processes tasks step-by-step without an overall look-ahead plan <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

While these methods offer various capabilities, effective [[components_of_ai_agents | AI agents]] for complex tasks go beyond mere prompting and require [[task_planning_and_decisionmaking_in_ai_agents | planning]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## The Necessity of Planning in AI Agents

[[task_planning_and_decisionmaking_in_ai_agents | Planning]] in the context of [[components_of_ai_agents | AI agents]] involves figuring out the sequence of steps needed to achieve a goal <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It becomes essential for:
*   **[[dynamic_planning_for_complex_tasks_in_ai | Complex tasks]]**: When problems are not straightforward <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Parallelization**: Enabling concurrent execution of steps <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Explainability**: Unlike React, where the flow of thought is visible but the overall reasoning unclear, planning allows for a better understanding of *why* certain steps were taken <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

[[task_planning_and_decisionmaking_in_ai_agents | Planners]] can be categorized as forms-based (e.g., text-based, like Microsoft's Magentic) or code-based (e.g., Hugging Face's Small Agents) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Dynamic Planning and Smart Execution

[[dynamic_planning_for_complex_tasks_in_ai | Dynamic planning]] involves the ability to replan during execution <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Instead of adhering to a single, rigid plan, an agent can reassess and adjust its strategy mid-way <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

For efficiency, every [[task_planning_and_decisionmaking_in_ai_agents | planner]] needs an **execution engine** <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. An execution engine's capabilities include:
*   **Dependency Analysis**: Analyzing dependencies between steps <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Parallel Execution**: Enabling concurrent processing of tasks <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Trade-off Management**: Balancing speed and cost, potentially using techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## AI21 Maestro: A System for Planning and Execution

AI21 Maestro exemplifies a system that combines a [[task_planning_and_decisionmaking_in_ai_agents | planner]] and a smart execution engine <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Simplified Instruction Following
In a simplified scenario for instruction following, a prompt contains context, task details, and requirements (e.g., paragraph limits, tone, brand mentions). These requirements are separated from the main prompt for easier validation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

The system uses an execution tree or graph <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>:
1.  The [[task_planning_and_decisionmaking_in_ai_agents | planner]] and execution engine select several candidate solutions at each step <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
2.  Only promising candidates are pursued for further refinement <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

Techniques used include:
*   **Best of N**: Sampling multiple generations from an LLM (potentially with high temperature or from different LLMs) instead of just one <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Candidate Discarding**: Discarding unpromising candidates and focusing on the best ones based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Validation and Iteration**: Continuous validation and iterative fixing <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Complex Task Execution
For more [[dynamic_planning_for_complex_tasks_in_ai | complex tasks]], the system's input leads to various "tracks" <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The execution engine estimates the expected cost, latency, and success probability for each track <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The [[task_planning_and_decisionmaking_in_ai_agents | planner]] then chooses the optimal path <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Ultimately, results are reduced or combined to form a complete answer to the original query <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

Using a [[task_planning_and_decisionmaking_in_ai_agents | planner]] and smart execution engine significantly improves results for instruction following and requirement satisfaction, even for models like GPT-40 or Claude Sonnet 3.5 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. While this approach may incur higher runtime and cost, it delivers significantly higher quality outcomes <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Key Takeaways

*   **LLMs Alone Are Insufficient**: Even for "simple" instruction following, LLMs by themselves are often not enough <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Start Simple**: Begin with the simplest solution that works. Use raw LLMs if they suffice <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Leverage Tools**: Integrate tools or use frameworks like React when basic LLMs aren't enough <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Adopt Planning for Complexity**: For truly [[dynamic_planning_for_complex_tasks_in_ai | complex tasks]], [[task_planning_and_decisionmaking_in_ai_agents | planning]] combined with an execution engine is necessary <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.