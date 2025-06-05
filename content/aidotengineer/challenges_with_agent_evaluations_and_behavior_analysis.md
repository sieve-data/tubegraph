---
title: Challenges with agent evaluations and behavior analysis
videoId: RVN9HWKmkNU
---

From: [[aidotengineer]] <br/> 

Developing stable AI agent swarms capable of solving complex knowledge work problems is a significant aspiration in AI development. However, these swarms often lack stability when tackling increasingly intricate challenges <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This instability stems from several [[Challenges in AI agent evaluation | challenges]], including:
*   Inability to perfectly observe agent behavior <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   The dynamic nature of environments in which agents operate <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   Difficulties in comprehensively testing agents beforehand <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Lack of clarity regarding whether agents are consistently making progress towards a goal when they don't achieve it in a single attempt <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## The Role of Evaluations

Robustly addressing these [[Challenges in Developing AI Agents | challenges]] requires effective evaluations, or "evals" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Many people tend to oversimplify the concept of evaluations <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Simply adopting an eval stack without systematic usage will likely not yield significant results <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. For evaluations to be effective, they must be used systematically to not only improve agents and workflows but also to continuously develop and align the evaluation stacks themselves with actual business requirements <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Complexity of Agent Evaluation

A fundamental difficulty in agent evaluation is the need to assess all aspects of agent behaviors and internal representations, which presents a complex landscape <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This involves both [[Semantic and behavioral evaluation of agents | semantic and behavioral evaluation of agents]]:

*   **Semantic Evaluation:** Focuses on how the agent represents reality, models it, discusses it with the user, and how well it is grounded in terms of truth <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Behavioral Evaluation:** Concerns whether the agent infers the correct goals, makes progress towards those goals, and selects the appropriate tools to achieve them <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

Ideally, all these aspects would be evaluated, but even consistently evaluating a subset can be a valuable starting point <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Framework for Setting Up Evaluators

To begin, a clear framework for setting up evaluators is essential <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For instance, evaluating a hotel reservation agent might involve evaluators for:
*   Policy adherence to the specific hotel's reservation policy <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Accuracy of the agent's outputs to the user <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   Overall appropriate behavior <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

It is crucial to have good visibility into creating large stacks of evaluators and to maintain and improve them systematically over time, especially when running dozens simultaneously <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Stabilization Loop with Model Conduct Protocol (MCP)

The goal is to achieve a stabilization loop where an agent attempts a task, its output is evaluated by an evaluation engine, and then feedback (numeric scores and explanations of what went right or wrong) is provided back to the agent <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This feedback enables the agent to improve its own performance <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The Model Conduct Protocol (MCP) is a method for attaching agents to this evaluation engine to facilitate this feedback <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Practical Example

In a demonstration, an agent's output text (e.g., a marketing message) can be evaluated by a "marketing message quality judge" from an MCP server <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. The MCP interface allows scoring the message and then attempting to improve that score, providing feedback on aspects like persuasiveness, writing quality, and engagingness <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>, <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This process can be manually triggered for transparency or automatically integrated into an agent's operation <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

A more direct example involved a hotel reservation agent that, without MCP, recommended a competing hotel — a undesirable behavior <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. With the MCP server enabled and evaluating the agent's output, the agent stopped recommending the competitor and invoked a specific "hotel booking policy evaluator" to ensure policy adherence, even without being explicitly asked to <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This shows how an agent, attached to an evaluation engine via MCP, can receive feedback and improve its own behavior <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Approach to Robust Evaluation

To approach robust agent evaluation:
1.  **Powerful Evaluation Infrastructure:** Ensure your evaluation library or platform is sufficiently powerful to support diverse evaluators and their lifecycle maintenance and optimization <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. This includes optimizing both the agent and the evaluators themselves, as many will be run, incurring costs <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
2.  **Manual Offline MCP Use:** Start by running the MCP manually offline, as demonstrated with the marketing message example <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This provides initial understanding and transparency into how evaluations work <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
3.  **Attach to Agents via MCP:** Finally, attach evaluators to agents through the MCP <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This promises to make agent behavior more controllable, transparent, dynamically self-improving, and self-correcting <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

Root Signals offers a free MCP server for this purpose, and other solutions are expected to emerge, enabling various evaluation platforms and frameworks to be integrated into agent stacks <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. These [[Challenges in building reliable AI agents | challenges in building reliable AI agents]] can be mitigated through systematic evaluation.