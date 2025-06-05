---
title: Challenges with instruction following in AI
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

Despite advancements, Language Models (LLMs) continue to face [[challenges_in_ai_development | difficulties with instruction following]], even years after models like InstructGPT were introduced specifically for this purpose <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This is not unique to one model; "every language model has some problems with following instructions" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Evolution of Instruction Complexity
In 2022, InstructGPT was lauded for its ability to follow instructions, exemplified by simple queries like "Explain the moon landing to a six-year-old" <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. However, as more developers began using language models, instructions evolved into complex prompts packed with context, constraints, and requirements, often hoping for the best outcome from a single, lengthy prompt <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

This shift revealed that for even seemingly "simple tasks such as instruction following," LLMs alone are "no longer enough" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## AI Agents: A Solution to Instruction Following Challenges
To overcome these [[challenges_in_ai_agent_development | limitations]], AI agents have emerged as a crucial component <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Agents go beyond simple prompting; they require "planning" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

While the definition of an "AI agent" can be a philosophical debate, for engineers, it refers to "whatever works" to achieve a goal <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This can include various approaches:
*   **LLM as a Router**: A routing model directs queries to specialized LLMs <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Function Calling**: Providing an LLM with external tools and APIs (like Google search) to interact with the world <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **ReAct (Reason and Act)**: A popular framework where any language model can follow a "thought, then act upon that thought, and observe" loop, step-by-step <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. A key [[challenges_in_creating_effective_ai_agents | challenge]] with ReAct is that it doesn't "look ahead to the entire plan" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## The Critical Role of Planning
Planning is defined as "figuring out the steps that you have to take to reach your goal" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It becomes essential for:
*   "Complex tasks" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
*   Non-straightforward problems <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>
*   Tasks requiring parallelization <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>
*   Ensuring explainability, unlike ReAct which shows thoughts but not the "why" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>

Planners can be forms-based (e.g., text-bl based like Microsoft's Magentic One) or code-based (e.g., Small Agents from Hugging Face) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Dynamic Planning and Smart Execution
**Dynamic planning** allows for "replan" mid-process, meaning the system can re-evaluate and change its course if the current plan isn't optimal <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

For efficiency, every planner needs an **execution engine** <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. An execution engine can:
*   Analyze dependencies between steps, enabling "parallel execution" <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Manage trade-offs between speed and cost <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### AI21 Maestro: An Example of Planning and Execution
AI21's Maestro system combines a planner with a smart execution engine to address complex instruction following <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. It separates context, task, and requirements, making validation easier <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

In each step of the process, the planner and execution engine:
1.  Choose several "candidates" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  Continue to refine and improve only the most "promising" ones <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  Utilize techniques like "best of n" (sampling multiple generations from LLMs or different LLMs) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
4.  Discard unpromising candidates and pursue the best ones based on a predefined budget <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
5.  Incorporate validation steps with iterations for fixing <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The execution engine also tracks expected cost, latency, and success probability, allowing the planner to choose the optimal path <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Finally, a "reduce" step combines or selects the best results for a complete answer <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Results
This approach significantly improves instruction following and requirement satisfaction, as demonstrated by high results for models like GPTO 40 and Claude Sonnet 3.5. While it may incur "more runtime and more money," it yields "higher quality" <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Key Takeaways
*   LLMs alone are often insufficient for even "simple tasks such as just instruction following" <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   It's advisable to "start simple" with LLMs or tool-augmented models, like those using React <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   For "complex" tasks, planning and execution engines are necessary for robust AI agents <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.