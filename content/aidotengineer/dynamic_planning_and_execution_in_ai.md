---
title: Dynamic planning and execution in AI
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

Language models (LLMs) released around 2022, such as OpenAI's InstructGPT, were groundbreaking for their ability to follow instructions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, even by 2025, LLMs like GPT-4.1 still faced challenges in consistently following instructions <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This limitation applies to nearly all language models <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

The initial use cases for LLMs were simple, like explaining the moon landing to a six-year-old <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. However, as developers started using them more extensively, instructions became complex, often involving shoving "all the information, all the context, all the constraints, all the requirements" into a single prompt <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For tasks such as instruction following, LLMs alone are often insufficient <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This is where [[improving_ai_agent_task_execution | AI agents]] come into play, as they require planning in addition to prompting <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## What is an AI Agent?

While there's a philosophical debate about what constitutes an [[improving_ai_agent_task_execution | AI agent]], from an engineering perspective, it's "whatever works" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Various interpretations exist:
*   **LLM as a router**: A routing model directs a query to a specialized LLM <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Function calling**: The LLM is provided with external tools or APIs it can use, such as Google Search, to interact with the world <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **ReAct**: A popular framework that enables any language model to "reason in an action" by thinking, acting upon that thought, and observing the outcome <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. However, ReAct is a step-by-step process without a look-ahead to the entire plan <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## The Role of Planning

Planning in [[improving_ai_agent_task_execution | AI agents]] involves "figuring out the steps that you have to take to reach your goal" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It is particularly useful for complex tasks that are not straightforward and require parallelization and explainability <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Unlike ReAct, which shows thoughts but not the *why* behind them, planning offers greater transparency <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Planners can be form-based (like text-based or agentic from Microsoft) or code-based (like small agents from Hugging Face) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Dynamic Planning
Dynamic planning means the system has the ability to "replan" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Instead of rigidly following a single plan, it can reassess in the middle of execution and decide whether to stick to the current plan or create a new one <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## [[efficiency_and_smart_execution_engines_in_ai_applications | Smart Execution Engines]]

For efficiency, every planner requires an [[efficiency_and_smart_execution_engines_in_ai_applications | execution engine]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. An [[efficiency_and_smart_execution_engines_in_ai_applications | execution engine]] can:
*   Analyze dependencies between steps, enabling parallel execution <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Manage trade-offs between speed and cost <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Utilize techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### AI21 Maestro Example
AI21 Maestro is a system that combines a planner with a [[efficiency_and_smart_execution_engines_in_ai_applications | smart execution engine]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For instruction following, it separates the prompt (context and task) from explicit requirements (e.g., paragraph limit, tone, brand mentions) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This separation simplifies validation <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The system uses an "execution tree" or "execution graph" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. At each step, the planner and [[efficiency_and_smart_execution_engines_in_ai_applications | execution engine]] select several candidate solutions and only continue to refine the most promising ones <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Techniques used include:
*   **Best-of-N**: Sampling multiple generations from an LLM (potentially with high temperature) or using different LLMs <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Candidate Ditching**: Discarding unpromising candidates and pursuing only the best ones based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Validation and Iteration**: Continuous fixing and refining through iterative processes <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

In more complex scenarios, the [[efficiency_and_smart_execution_engines_in_ai_applications | execution engine]] can provide metrics like expected cost, latency, and success probability for different "tracks" or paths <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The planner then chooses the optimal path <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Finally, a "reduce" step combines or selects the best results for a complete answer <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

This approach significantly improves results for tasks like `if_val` and requirement satisfaction, showing high quality even for models like GPT-4, Claude Sonnet 3.5, and 3 Mini <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. While it may incur higher runtime and cost, it leads to substantially higher quality outcomes compared to single LLM calls <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Key Takeaways

*   LLMs alone are often not sufficient, even for seemingly simple tasks like instruction following <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   Always start simple: use basic LLMs if they suffice <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   Progress to more complex solutions as needed:
    *   Add tools to a model <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   Utilize frameworks like ReAct <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   For highly complex tasks, dynamic planning and [[efficiency_and_smart_execution_engines_in_ai_applications | execution engines]] become essential <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.