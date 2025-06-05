---
title: Challenges in instruction following by language models
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

Despite early advancements, [[large_language_models_in_ai_agents | language models]] (LLMs) continue to face difficulties in consistently following instructions, even for what appear to be simple tasks <a class="yt-timestamp" data-t="00:00:24">00:00:24</a>.

## The Evolution of the Problem

In 2022, OpenAI released InstructGPT, which was a significant step forward as the first model capable of taking and following instructions effectively <a class="yt-timestamp" data-t="00:00:00">00:00:00</a>. Early demonstrations, such as explaining the moon landing to a six-year-old, impressed many <a class="yt-timestamp" data-t="00:00:37">00:00:37</a>.

However, as developers began to integrate LLMs into more complex applications, the nature of instructions evolved <a class="yt-timestamp" data-t="00:00:51">00:00:51</a>. Prompts grew to encompass extensive information, context, constraints, and requirements, all typically crammed into a single input <a class="yt-timestamp" data-t="00:01:02">00:01:02</a>. This increased complexity highlighted the limitations of standalone LLMs for instruction following <a class="yt-timestamp" data-t="00:01:14">00:01:14</a>.

## The Role of AI Agents

The need to overcome these challenges has led to the development and increased importance of [[large_language_models_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:01:21">00:01:21</a>. Unlike simple prompting, agents require more sophisticated approaches, particularly planning <a class="yt-timestamp" data-t="00:01:24">00:01:24</a>.

Various interpretations and implementations of [[large_language_models_in_ai_agents | AI agents]] exist:
*   **LLM as a Router** Some systems route queries to specialized LLMs based on an initial routing model <a class="yt-timestamp" data-t="00:01:53">00:01:53</a>.
*   **Function Calling** This involves providing an LLM with a list of external tools it can use to interact with APIs, the internet (e.g., Google search), or other systems <a class="yt-timestamp" data-t="00:02:08">00:02:08</a>.
*   **React Framework** A popular framework that allows any [[large_language_models_in_ai_agents | language model]] to "reason in an action" by thinking, acting upon that thought, and observing the results iteratively <a class="yt-timestamp" data-t="00:02:39">00:02:39</a>. However, React processes steps one at a time without an overall look-ahead plan <a class="yt-timestamp" data-t="00:02:58">00:02:58</a>.

### The Necessity of Planning

For complex tasks that are not straightforward, [[large_language_models_in_ai_agents | AI agents]] need **planning** <a class="yt-timestamp" data-t="00:03:15">00:03:15</a>. Planning involves figuring out all the necessary steps to reach a goal, enabling parallelization and improving explainability, which is often lacking in reactive systems like React <a class="yt-timestamp" data-t="00:03:20">00:03:20</a>.

Planning can take various forms:
*   **Text-based planners** such as Text BL-based systems like Microsoft's Magentic One <a class="yt-timestamp" data-t="00:03:43">00:03:43</a>.
*   **Code-based planners** utilized by agents like Small Agents from Hugging Face <a class="yt-timestamp" data-t="00:03:50">00:03:50</a>.

### Dynamic Planning and Smart Execution

A key aspect of advanced planning is **dynamic planning**, which allows for replanning mid-process if the initial plan is no longer optimal <a class="yt-timestamp" data-t="00:03:57">00:03:57</a>.

For efficiency, every planner requires an **execution engine** <a class="yt-timestamp" data-t="00:04:14">00:04:14>. An execution engine is crucial because it can:
*   Analyze dependencies between steps, facilitating parallel execution <a class="yt-timestamp" data-t="00:04:22">00:04:22</a>.
*   Manage trade-offs between speed and cost, potentially using techniques like branch prediction for faster systems <a class="yt-timestamp" data-t="00:04:29">00:04:29</a>.

## AI21 Mastro: A Case Study

AI21 Mastro is an example of a system that integrates both a planner and a smart execution engine to tackle instruction following <a class="yt-timestamp" data-t="00:04:40">00:04:40</a>.

In this system:
*   The prompt, context, task, and requirements are separated, making validation easier <a class="yt-timestamp" data-t="00:04:53">00:05:53</a>.
*   At each step, the planner and execution engine evaluate several candidate solutions, pursuing only the most promising ones for refinement <a class="yt-timestamp" data-t="00:05:15">00:05:15</a>.
*   Techniques used include:
    *   **Best-of-N:** Sampling multiple generations from an LLM with high temperature or using different LLMs <a class="yt-timestamp" data-t="00:05:32">00:05:32</a>.
    *   **Candidate Discarding:** Eliminating unpromising candidates early to focus resources on the best options within a predefined budget <a class="yt-timestamp" data-t="00:05:49">00:05:49</a>.
    *   **Validation and Iteration:** Continuously validating results and iteratively fixing them <a class="yt-timestamp" data-t="00:05:59">00:05:59</a>.

The execution engine can forecast expected cost, latency, and success probability for different paths, allowing the planner to choose the optimal route <a class="yt-timestamp" data-t="00:06:15">00:06:15</a>. Finally, a "reduce" step combines or selects the best results for a complete answer <a class="yt-timestamp" data-t="00:06:30">00:06:30</a>.

Results from AI21's internal customer data show that integrating a planner and smart execution engine significantly improves performance (e.g., for GPTO 40, Cloud Sonet 3.5, or 3 Mini) and requirement satisfaction compared to single LLM calls <a class="yt-timestamp" data-t="00:06:42">00:06:42</a>. While this approach may incur higher runtime and cost, it delivers substantially higher quality <a class="yt-timestamp" data-t="00:07:10">00:07:10</a>.

## Conclusion

LLMs alone are often insufficient for instruction following, especially with complex tasks <a class="yt-timestamp" data-t="00:07:21">00:07:21</a>. For simpler scenarios, direct LLM calls, tool integration, or the React framework may suffice <a class="yt-timestamp" data-t="00:07:30">00:07:30</a>. However, for highly complex tasks, adopting a planning and execution engine framework becomes essential to achieve reliable and high-quality instruction adherence <a class="yt-timestamp" data-t="00:07:43">00:07:43</a>.