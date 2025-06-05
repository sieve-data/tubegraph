---
title: Evaluating and optimizing AI agents and workflows
videoId: RVN9HWKmkNU
---

From: [[aidotengineer]] <br/> 

[[evaluating_ai_agents_and_assistants | Evaluating AI agents and assistants]] and workflows is crucial for achieving stability and reliability in complex AI applications <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While AI agent swarms theoretically could solve any knowledge work problem, their instability with increasing complexity is a significant limitation <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This instability stems from challenges such as imperfect observability, dynamic environments, comprehensive [[testing_and_optimization_of_ai_coding_agents | testing and optimization of AI coding agents]], and difficulty in tracking consistent progress towards goals <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The general solution lies in robust [[evaluating_ai_agents_and_assistants | evaluations]] <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## [[challenges_in_ai_agent_evaluation | Challenges in AI Agent Evaluation]]

Many approaches to [[evaluating_ai_agents_and_assistants | evaluations]] tend to oversimplify the process <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Simply applying an evaluation stack without systematic use will not lead to significant improvement <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Effective [[evaluating_ai_agents_and_assistants | evaluation]] must not only [[building_and_improving_ai_agents | improve AI agents]] and workflows but also continuously develop and align the evaluation stacks themselves with business requirements <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

Evaluating all aspects of agent behaviors and internal representations presents a complex landscape <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This includes:

*   **Agent's Representation of Reality**: How the agent models, discusses, and grounds reality (i.e., what is true) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Behavioral Aspects**: Whether the agent infers the correct goals, makes progress towards them, and selects the right tools <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

While ideally, all these aspects would be evaluated, starting with a consistent framework for some aspects can yield progress <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Setting Up Evaluators

A clear framework is essential for setting up evaluators <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. For instance, in a hotel reservation agent scenario, evaluators might include:
*   Policy adherence to the specific hotel's reservation rules <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Accuracy of agent outputs to the user <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   Overall appropriate behavior <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

It is critical to have good visibility for creating, maintaining, and systematically improving large stacks of evaluators over time <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## The Stabilization Loop and Model Context Protocol (MCP)

The goal is to achieve a stabilization loop:
1.  An agent attempts a task <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
2.  The task's output is evaluated by an evaluation engine <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
3.  Feedback, in the form of a numeric score and an explanation of what went right or wrong, is sent back to the agent <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
4.  The agent uses this information to [[building_and_improving_ai_agents | improve its own performance]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The Model Context Protocol (MCP) is a method for attaching agents to this evaluation engine <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. MCP allows agents to access evaluators and "charges" (collections of evaluators) that can measure and provide feedback for improvement <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Practical Examples of MCP

### Optimizing Text Output

A simple example involves optimizing text output, such as a marketing message <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. By using an MCP server, an agent can:
1.  List available evaluators or charges <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  Select a relevant charge, like a "marketing message quality judge" <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
3.  Measure the initial message <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
4.  Figure out how to improve the score <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
5.  Suggest an improved version based on scores for persuasiveness, writing quality, and engagingness <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

This process demonstrates how an agent can iteratively improve its output based on continuous evaluation <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Stabilizing an AI Hotel Reservation Agent

Consider a hotel reservation agent for "Shire Hotel" which should *never* recommend or mention "Akma Hotel" next door <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

*   **Without MCP**: The agent might politely offer rooms at Shire Hotel but then unacceptably suggest Akma Hotel as "a great option" <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **With MCP**: When the MCP server is enabled, the agent calls the MCP server for evaluation <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. During this process, evaluators like the "hotel sh booking policy evaluator" are invoked <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. As a result, the agent stops mentioning the Akma Hotel, correcting its behavior <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

This illustrates how an agent, through the MCP, can pick relevant evaluators to [[evaluating_ai_agent_performance_and_reliability | evaluate AI agent performance and reliability]] and self-correct its behavior, even without specific instructions to use certain evaluators <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

## Conclusion

To successfully [[developing_and_optimizing_ai_agents | develop and optimize AI agents]] and workflows:
1.  Ensure your evaluation library or platform is powerful enough to support diverse evaluators, their lifecycle maintenance, and optimization <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. This includes optimizing both the agent itself and the evaluators, as they can incur costs <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
2.  Begin by running MCP manually offline to understand its workings and gain transparency <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
3.  Finally, attach evaluators to agents via MCP <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This approach promises more controllability, transparency, and dynamically self-improving and self-correcting agents <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.