---
title: Agentic frameworks and their applications
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

## The Evolution of Instruction Following in LLMs

In 2022, OpenAI released InstructGPT, a model praised for its ability to take and follow instructions effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Initially, simple prompts like "Explain the moon landing to a six-year-old" demonstrated its capabilities <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. However, as developers began to use language models for more complex tasks, prompts evolved to include extensive context, constraints, and requirements <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. By 2025, even advanced models like GPT 4.1 still exhibited difficulties with instruction following, indicating that large language models (LLMs) alone are often insufficient for even seemingly simple tasks <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>. This challenge highlights the need for [[agentic frameworks and tool integration | AI agents]] <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

## Defining an AI Agent

From an engineering perspective, the definition of an "agent" is pragmatic: "Whatever works, just make it work" <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Several architectural patterns and [[agentic architectures and systems design | systems design]] are often referred to as [[agentic enterprise and AI agents | AI agents]]:

*   **LLM as a Router**: A routing model directs a query to a specialized LLM <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
*   **Function Calling**: The LLM is provided with a list of external tools to interact with APIs or the internet (e.g., Google search) <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   **ReAct (Reason and Act)**: A widely used [[agent frameworks and orchestration layers in ai engineering | framework]] that allows any language model to think, act upon that thought, and observe the result in an iterative process. This process happens step-by-step without a look-ahead to the entire plan <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

## The Importance of Planning in Agentic Systems

For complex tasks that are not straightforward, planning becomes essential for [[agentic workflows and their levels of autonomy | AI agents]] <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. Planning involves figuring out the sequence of steps needed to achieve a goal <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

Key aspects of planning:
*   **Addressing Complex Tasks**: Planning is crucial when tasks require parallelization and explainability <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. Unlike ReAct, which shows thoughts but not the *why*, planning aims to provide clarity <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.
*   **Dynamic Planning (Replan)**: A plan is not static. A system can re-evaluate its plan midway through execution and adjust it if necessary <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Smart Execution Engine**: Every planner requires an execution engine to analyze dependencies between steps, enabling parallel execution <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. It also manages trade-offs between speed and cost, potentially using techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

Examples of planners include forms-based planners (e.g., text-based, like Microsoft's Magentic) and code-based planners (e.g., from Hugging Face's Small Agents) <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

## AI21 Labs' Maestro: A Practical Application

AI21 Labs developed Maestro, a system that combines a planner and a smart execution engine to improve instruction following <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

**How Maestro Works**:
*   **Separation of Concerns**: Instead of shoving all information (context, task, requirements like paragraph limits, tone, brand mentions) into one prompt, Maestro separates them <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. This makes validation easier <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   **Execution Tree/Graph**: At each step, the planner and execution engine evaluate several candidates, pursuing and improving only those that seem promising <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Techniques for Improvement**:
    *   **Best of N**: Sampling multiple generations from an LLM with high temperature, or using different LLMs <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
    *   **Candidate Pruning**: Ditching non-promising candidates and pursuing only the best ones based on a predefined budget <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
    *   **Validation and Iteration**: Continuous validation and iterative fixing <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Decision Making**: For more complex scenarios, the execution engine tracks expected cost, latency, and success probability, allowing the planner to choose the optimal path <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Reduction**: At the end, results are reduced by selecting the best one or combining them for a complete answer <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.

## Performance and Trade-offs

Using a planner and smart execution engine significantly improves results for instruction following and requirement satisfaction, even with models like GPT-40 or Claude Sonnet 3.5 <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. This comes at a cost of increased runtime and financial expenditure, but yields demonstrably higher quality outputs <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.

## Key Takeaways for Agentic Frameworks

*   LLMs alone are not always sufficient, even for "simple" tasks like instruction following <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.
*   Always start simple: If an LLM alone suffices, use it <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   Progress to [[agentic frameworks and tool integration | tools]]: If needed, integrate tools with your model <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.
*   Consider ReAct: A good next step for structured thought and action <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   Implement planning and execution engines: For highly complex tasks, this approach is necessary to achieve desired results <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.