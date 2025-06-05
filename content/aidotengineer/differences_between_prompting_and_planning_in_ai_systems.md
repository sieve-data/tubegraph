---
title: Differences between prompting and planning in AI systems
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

In the evolution of AI, particularly with large language models (LLMs), a key challenge has been the ability to consistently [[challenges_with_instruction_following in AI | follow instructions]]. While early models like InstructGPT in 2022 were hailed for their instruction-following capabilities <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, even by 2025, issues persist across many language models <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This highlights a fundamental distinction between simple prompting and more sophisticated planning mechanisms required for complex tasks.

## The Limitations of Direct Prompting

Initially, users were impressed by models' ability to handle straightforward requests, such as "Explain the moon landing to a six-year-old" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. However, as developers began to leverage LLMs for more intricate applications, instructions evolved to include extensive information, context, constraints, and requirements, often all "shoved in one prompt" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

For even seemingly "simple tasks" like instruction following, relying on LLMs alone is often insufficient <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This limitation leads to the necessity of AI agents and planning.

## The Rise of AI Agents and Planning

[[challenges_in_ai_agent_development | AI agents]] go beyond mere prompting by incorporating planning <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. While the philosophical definition of an "agent" can be debated, from an engineering perspective, it refers to whatever mechanism effectively achieves a desired outcome <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Common interpretations or components that contribute to agentic behavior include:
*   **LLMs as Routers**: A routing model directs queries to specialized LLMs <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Function Calling**: LLMs are provided with external tools and APIs (e.g., Google search) to interact with the world <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **React (Reason + Act)**: A popular framework where an LLM thinks, then acts upon that thought, observes the result, and repeats the process <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. While effective, React processes steps one at a time and lacks a look-ahead to the entire plan <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## What is Planning?

Planning in AI involves "figuring out the steps that you have to take to reach your goal" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It is crucial for complex tasks that are not straightforward <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> and require:
*   **Parallelization**: Performing multiple steps simultaneously <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Explainability**: Understanding *why* certain actions were taken, unlike React where you see thoughts but not the underlying rationale for the overall sequence <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Planning can be implemented through form-based planners (e.g., text-based) or code-based planners <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### [[dynamic_planning_and_execution_in_ai | Dynamic Planning and Smart Execution]]

A key aspect of advanced planning is [[dynamic_planning_and_execution_in_ai | dynamic planning]], which allows for replanning mid-process <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Instead of rigidly following a single plan, the system can evaluate if the current plan is optimal or if a new one is needed <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

For efficiency, a planner needs an **execution engine** <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This engine can:
*   Analyze dependencies between steps to enable parallel execution <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Manage trade-offs between speed and cost <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Utilize techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## AI21 Maestro: An Example of Planning and Execution

AI21's Maestro system exemplifies the combination of a planner and a smart execution engine <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For [[challenges_with_instruction_following_in_ai | instruction following]], it separates the core prompt (context and task) from specific requirements (e.g., paragraph limit, tone, brand mentions) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This separation makes requirements easier to validate <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

In each step, the planner and execution engine evaluate several candidate solutions, continuing only with those that appear promising <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. [[strategies_for_effective_ai_implementation | Strategies for effective implementation]] include:
*   **Best of N**: Sampling multiple generations from an LLM (potentially with high temperature) or using different LLMs <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Candidate Discarding**: Discarding unpromising candidates and pursuing only the best ones based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Validation and Iteration**: Iteratively fixing and improving solutions <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The execution engine in such systems can track expected cost, latency, and success probability, allowing the planner to choose the most appropriate path <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. At the end, results are reduced or combined to form a complete answer <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This approach significantly improves quality, even for models like GPT-4, Claude Sonnet, or Mini, albeit with increased runtime and cost <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Conclusion

While direct prompting with LLMs can suffice for simple tasks, more complex scenarios or stringent [[specifying_intent_to_ai_systems | instruction following]] necessitate advanced methods. The key [[strategies_for_adapting_ai_models_and_prompts | takeaway]] is that LLMs alone are not always enough <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

For optimal [[strategies_for_effective_ai_implementation | AI implementation]], consider a progressive approach:
1.  **Start Simple**: If LLMs alone or LLMs with basic tools (like function calling) work, use them <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  **Employ React**: For tasks requiring iterative thought and action, the React framework can be beneficial <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
3.  **Advanced Planning and Execution**: For truly complex tasks, a full planning and execution engine that allows for [[dynamic_planning_and_execution_in_ai | dynamic planning]] and smart execution is the most robust solution <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This represents a significant shift from simple prompting to a multi-step, intelligent problem-solving approach in AI.