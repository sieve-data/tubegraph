---
title: Role of AI agents and agentic frameworks
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

While Large Language Models (LLMs) like InstructGPT marked a significant leap in language understanding and instruction following in 2022, they still struggle with complex instructions, even by 2025 with models like GPT-4.1 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This limitation stems from users attempting to include all context, constraints, and requirements into a single prompt, which often proves insufficient even for seemingly simple tasks like instruction following <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This is where [[ai_agents_and_agentic_workflows | AI agents]] come into play <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

[[ai_agents_and_agentic_workflows | Agents]] do not solely rely on prompting; they incorporate planning <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Defining an AI Agent

From an engineering perspective, the precise definition of an [[ai_agents_and_agentic_workflows | AI agent]] is less critical than its functional effectiveness <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Several concepts are often referred to as [[ai_agents_and_agentic_workflows | agents]] or [[agentic_enterprise_and_ai | agentic]] workflows:

*   **LLM as a Router**: This involves a routing model that directs a query to a specialized LLM <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Function Calling**: LLMs are provided with a list of external tools to interact with APIs, the internet (like Google search), or other systems <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The MCP (Microsoft's framework for multi-agent collaboration and planning) standardizes this concept <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **React (Reason and Act)**: A popular [[ai_agents_and_agentic_workflows | agentic framework]] that works with any language model. It involves a cycle of "thought, then act upon that thought, and observe" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. While effective, React processes steps one at a time, without a look-ahead to the entire plan <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## The Necessity of Planning in Agentic Workflows

[[the_role_and_definition_of_ai | Every AI agent]] ultimately needs to incorporate planning <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Planning is the process of figuring out the steps required to achieve a specific goal <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It becomes essential for complex tasks that are not straightforward and require parallelization and explainability <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This contrasts with React, where the sequence of thoughts is visible, but the overall "why" behind the progression is not clear <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Planning can be implemented using:
*   **Forms-based planners**: Such as TextBL or Magentic One by Microsoft <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Code-based planners**: Examples include [[building_effective_ai_agents | small agents]] from Hugging Face <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Dynamic Planning and Smart Execution

A key aspect of effective planning is **dynamic planning**, which allows for replanning in the middle of a task <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This enables the system to reassess if the current plan is optimal or if a new path should be taken <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

For efficiency, [[ai_agents_and_agentic_workflows | agents]] integrate a "smart execution engine" alongside the planner <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. An execution engine can:
*   Analyze dependencies between steps, enabling parallel execution <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Manage trade-offs between speed and cost, for instance, by using branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## AI21 Maestro: An Agentic Framework Example

AI21 Labs has developed an [[developing_ai_agents_and_agentic_workflows | agentic framework]] called AI21 Maestro, which combines a planner and a smart execution engine <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

In a simplified instruction-following task, Maestro separates the prompt (context and task) from explicit requirements (e.g., length, tone, brand mentions) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This separation makes validation easier <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The process involves an execution tree or graph:
*   At each step, the planner and execution engine select several candidate solutions <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   Only the most promising candidates are pursued, fixed, and improved <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

Techniques used within the execution engine include:
*   **Best of N**: Sampling multiple generations from an LLM (often with high temperature) or using different LLMs <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Candidate Discarding**: Ditching unpromising candidates early and focusing on the best ones based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Validation and Iteration**: Iteratively fixing and refining outputs <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The execution engine can also track expected cost, latency, and success probability, allowing the planner to choose the most appropriate path <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Finally, a "reduce" step combines or selects the best results for a complete answer <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Benefits and Challenges

[[development_and_challenges_of_ai_agents | AI agents]] employing planning and smart execution engines demonstrate significant improvements in instruction following and requirement satisfaction compared to single LLM calls <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. While this approach leads to higher quality, it comes at the cost of increased runtime and financial expenditure <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Conclusion

[[the_impact_and_future_potential_of_ai_and_agents | LLMs alone are not always sufficient]], even for basic tasks like instruction following <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. The approach to [[building_effective_ai_agents | building effective AI agents]] should be incremental:
1.  Start simple with single LLM calls if they suffice <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Incorporate tools or React if the task complexity increases <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
3.  For highly complex tasks, adopting a planning and execution engine framework is necessary to achieve desired quality and performance <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.