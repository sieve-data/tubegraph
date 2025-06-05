---
title: Dynamic planning for complex tasks in AI
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

The landscape of AI models has evolved significantly since OpenAI's release of InstructGPT in 2022, a model lauded for its ability to follow instructions effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, even with advanced models like GPT 4.1 in 2025, challenges persist in reliably following complex instructions <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This limitation extends to nearly every language model <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Initially, simple instructions like "Explain the moon landing to a six-year-old" demonstrated the power of early LLMs <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. However, as developers began integrating language models into more sophisticated applications, prompts grew in complexity, often attempting to cram all context, constraints, and requirements into a single input <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For even seemingly simple instruction following, LLMs alone are no longer sufficient <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[role_of_ai_agents_in_planning_and_executing_tasks | Role of AI Agents in Planning and Executing Tasks]]

This is where [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]] become crucial <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Agents go beyond mere prompting and necessitate planning <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

While the philosophical definition of an "agent" in AI is debated <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, from an engineering perspective, it refers to any system that works to achieve a goal <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Various interpretations of agents exist:
*   **LLM as a Router** A routing model that directs queries to specialized LLMs <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Function Calling** Providing an LLM with external tools and APIs (e.g., Google Search) it can use to interact with the world <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This approach has been standardized by MCEP <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **ReAct (Reason and Act)** A popular framework where a language model thinks, acts upon that thought, and observes the result in a step-by-step manner <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. However, ReAct does not involve a "look ahead" to the entire plan, focusing on the next immediate step <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## [[task_planning_and_decisionmaking_in_ai_agents | Task Planning and Decision-Making in AI Agents]]

[[task_planning_and_decisionmaking_in_ai_agents | Planning]] in AI agents involves figuring out the necessary steps to reach a specific goal <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It is particularly useful for complex tasks that are not straightforward <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, especially those requiring parallelization and explainability <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Unlike ReAct, where the thought process is visible but the *why* of the overall progression isn't clear, planning aims for greater transparency <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Planners can be forms-based (like TextBL-based planners such as Magentic by Microsoft) or code-based (like Small Agents from Hugging Face) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Dynamic Planning

Dynamic planning refers to the ability to re-plan in the middle of a task <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Instead of rigidly adhering to one initial plan, a dynamic planner can evaluate its progress and decide to re-plan if a better path emerges <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Execution Engines and [[efficiency_and_smart_execution_in_ai_systems | Smart Execution]]

For efficiency, every planner requires an execution engine <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. An execution engine plays a vital role by:
*   Analyzing dependencies between steps, enabling parallel execution <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Managing trade-offs between speed and cost <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, potentially using techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## AI21 Maestro: An Example of Planning and Smart Execution

AI21's Maestro system exemplifies the integration of a planner and a [[efficiency_and_smart_execution_in_ai_systems | smart execution engine]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For instruction following, Maestro separates the prompt's context, task, and requirements (e.g., paragraph limits, tone, brand mentions) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This separation simplifies validation <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The system operates using an execution tree or graph <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>:
*   At each step, the planner and execution engine select several candidate solutions <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   Only promising candidates are pursued, fixed, and improved <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   Techniques like "best of N" are used, where multiple generations from an LLM (potentially different LLMs) are sampled with high temperature <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   Unpromising candidates are discarded, and only the best ones are pursued based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   Validation and iterative refinement (fixing) are integral parts of the process <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

For more complex scenarios, the execution engine can estimate expected cost, latency, and success probability for different execution tracks, allowing the planner to choose the optimal path <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Finally, a "reduce" step combines or selects the best results for a complete answer <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Results and Trade-offs

Using this planning and [[efficiency_and_smart_execution_in_ai_systems | smart execution]] approach, systems like Maestro demonstrate significantly higher results for various LLMs (e.g., GPT-40, Claude Sonnet 3.5, 3 Mini) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For requirement satisfaction, using an internal customer-data-based dataset, this method shows clear improvement over single LLM calls <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This comes with a trade-off: increased runtime and cost for higher quality <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Conclusion

The key takeaways for [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] are:
*   LLMs alone are often insufficient, even for tasks like instruction following <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   Start simple: if LLMs suffice, use them. If tools are needed, use function calling. If more structured reasoning is required, consider ReAct <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   For complex tasks that demand advanced capabilities, a planning and execution engine is essential to achieve high quality and reliability <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.