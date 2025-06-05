---
title: Efficiency and smart execution engines in AI applications
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

In 2022, OpenAI released InstructGPT, which was lauded as the first model capable of taking and following instructions effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, even by 2025 with GPT 4.1, language models (LLMs) continue to struggle with complex instruction following <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This challenge isn't exclusive to OpenAI; every language model faces issues with consistently following instructions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Initially, simple prompts like "Explain the moon landing to a six-year-old" demonstrated impressive capabilities <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. But as developers began to leverage LLMs for more intricate tasks, prompts evolved to include extensive information, context, constraints, and requirements, all "shoved into one prompt" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For even seemingly simple tasks like instruction following, LLMs alone are often insufficient <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## The Rise of AI Agents

This limitation highlights the need for [[developing_ai_agents_for_productivity | AI agents]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Unlike basic prompting, agents require planning <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The definition of an "agent" can be fluid, with some even referring to an LLM acting as a router that directs queries to specialized LLMs as an agent <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Other forms of agents include:
*   **Function Calling**: Providing an LLM with a list of external [[tool_usage_and_development_in_ai_frameworks | tools]] it can use to interact with APIs or perform actions like Google searches <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **React (Reason and Act)**: A popular framework where an LLM thinks, then acts upon that thought, and observes the result, iterating step by step towards a solution <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. However, React typically lacks a look-ahead to the entire plan <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## The Importance of Planning

Planning is crucial for [[developing_ai_agents_for_productivity | AI agents]], involving the process of figuring out the necessary steps to achieve a goal <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It is particularly valuable for complex tasks that are not straightforward <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Planning offers advantages such as:
*   **Parallelization**: Enabling multiple steps to be executed concurrently <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Explainability**: Providing a clear understanding of *why* certain steps were taken, which is often missing in reactive frameworks <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Planners can be forms-based, like Microsoft's Magentic, or code-based, such as Small Agents from Hugging Face <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Dynamic Planning and Smart Execution

A key aspect of advanced planning is [[dynamic_planning_and_execution_in_ai | dynamic planning]], which includes the option to replan <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This means a system can reassess its current plan mid-execution and decide if a different path is more optimal <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

To achieve true [[techniques_for_improving_ai_model_efficiency | efficiency]], every planner needs an execution engine <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. A smart execution engine can:
*   Analyze dependencies between steps, enabling parallel execution <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Manage trade-offs between speed and cost <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For example, using branch prediction can lead to faster systems <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### AI21 Mastro: An Example System

AI21's Mastro system exemplifies the integration of a planner and a smart execution engine <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. In a simplified instruction-following scenario, Mastro separates the prompt (context and task) from explicit requirements (e.g., paragraph limits, tone, brand mentions) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This separation makes validation easier <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The system uses an execution tree or graph where, at each step, the planner and execution engine:
1.  Choose several candidate solutions <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
2.  Continue to fix and improve only the most promising candidates <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

Key [[techniques_for_improving_ai_model_efficiency | techniques for improving efficiency]] and quality include:
*   **Best of N**: Instead of a single generation, multiple generations are sampled from an LLM with high temperature, or different LLMs are used <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Candidate Ditching**: Unpromising candidates are discarded, and only the best ones are pursued based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Validation and Iteration**: Continuous validation allows for iterative fixing and improvement <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

In more complex scenarios, the execution engine tracks expected cost, latency, and success probability, allowing the planner to choose the most appropriate path <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Finally, a "reduce" phase consolidates multiple results into the best or a combined answer <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Performance and Trade-offs

Systems employing planning and smart execution engines demonstrate significantly improved results compared to single LLM calls, even for advanced models like GPT-40 or Claude Sonnet 3.5 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For instance, in requirement satisfaction tasks, these methods show considerable improvement <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

While there is a trade-off in terms of increased runtime and cost, the resulting higher quality often justifies the investment <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Key Takeaways

*   **LLMs alone are not always enough**: Even for seemingly "simple" tasks like instruction following, advanced LLMs can fall short <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Start Simple**: Begin with basic LLMs if they suffice <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Incrementally Add Complexity**: If needed, incorporate [[tool_usage_and_development_in_ai_frameworks | tools]] or frameworks like React <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Embrace Planning and Execution for Complex Tasks**: For highly complex tasks, a full planning and execution engine is necessary to achieve desired outcomes <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This approach represents a powerful [[strategies_for_effective_ai_implementation | strategy for effective AI implementation]] and [[enhancing_existing_systems_with_ai_capabilities | enhancing existing systems with AI capabilities]].