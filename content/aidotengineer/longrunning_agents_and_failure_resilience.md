---
title: Longrunning agents and failure resilience
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

When deploying AI agents into production, several key considerations arise, particularly concerning their ability to operate for extended periods and recover from failures <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This involves addressing how agents manage long-running tasks and ensure their progress isn't lost in the event of an interruption <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Challenges of Scaling AI Agents

Current AI agents face several challenges when operating in production environments:

*   **Human in the Loop Requirements**
    *   Many applications require human oversight or approval at various stages of agent execution <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is especially true for high-value or high-risk tasks, such as transferring money or deleting accounts, where a human needs to provide a final decision <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Long-Running Processes and Failure**
    *   AI agents often involve multiple steps and can be [[stateful_ai_agents | longrunning]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The longer a process runs, the higher the chance of encountering failures like network or hardware issues <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. There is a need to [[evaluating_ai_agent_performance_and_reliability | checkpoint]] an agent's state to resume operations without losing all prior work <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   Sophisticated agents performing complex tasks or extensive research across multiple internal or external systems are particularly susceptible to failure <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Mechanisms are needed to tolerate these failures and prevent loss of progress <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Distributed Environments**
    *   Increasingly, agents operate in [[scaling_ai_agents_in_production | distributed environments]] rather than just on a single desktop <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This introduces [[challenges_and_solutions_in_scaling_ai_agents | considerations for running agents in a scalable distributed environment]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   Furthermore, modern agents are becoming more sophisticated, with multi-level configurations involving main orchestrator agents and several sub-agents <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Managing human approval and state saving in such nested scenarios is crucial <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Agent Loop Persistence

A critical challenge for longrunning agents is [[agent_loop_persistence_and_distributed_environments | agent loop persistence]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. The agent's core processing loop, which interacts with users or external channels like Slack, typically needs to run continuously <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This persistent running, even while waiting for human responses, can be inefficient and problematic <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Addressing this, there is a need for a mechanism that allows the agent loop (or multiple loops) to be fully shut down and then restarted later, such as after human approval is received <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Agent Continuations as a Solution

[[zero_ops_resilient_agent_powered_apps | Agent continuations]] offer a new mechanism developed by Snaplogic to address both human-in-the-loop processing and reliable execution for longrunning agents <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

*   **Inspired by Programming Language Theory**
    *   Agent continuations are inspired by the programming language concept of "continuations," which allow capturing the full execution state of a program at any point to pause and then resume it later <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Capturing and Resuming Agent State**
    *   The core idea of agent continuations is to pause an agent's execution—which might involve multiple tool calls, LLM calls, and even sub-agents—and save its complete state <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. This snapshot allows the agent to be resumed from that exact point at a later time <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Leveraging the Messages Array**
    *   A key insight behind agent continuations is that LLM interactions already maintain a "messages array," which acts as a log of all previous interactions <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This array, replayed to the LLM for its next inference, already captures much of the agent's state <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Agent continuations build on this existing bookkeeping <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### [[implementation_and_benefits_of_agent_continuations | Implementation and Benefits]]

The [[implementation_and_benefits_of_agent_continuations | implementation]] of agent continuations involves:

*   **Suspension Conditions**: Agents can be configured to suspend execution based on various conditions, such as requiring human approval for a specific tool call <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a> or other arbitrary suspension points like time limits or turn counts <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
*   **Continuation Object Creation**: When a suspension condition is met, a "continuation object" is created <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This object embeds the standard messages array along with additional metadata to allow for proper resumption <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   **Decoupled Execution**: A powerful aspect of agent continuations is that once the continuation object is created, the agent loops do not need to remain running <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. All necessary information is captured to restart the agent exactly where it left off <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. This addresses [[limitations_of_current_serverless_providers_for_longrunning_workflows | limitations of current serverless providers for longrunning workflows]] that typically require continuous execution.
*   **Recursive Structure**: The continuation object format is recursive, capable of handling arbitrary depths of nested sub-agents, ensuring that state can be captured and restored across complex multi-level agent configurations <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Resumption**: When the continuation object is sent back to the agent (e.g., after human approval), the framework reconstructs the agent's state and resumes execution from the point of suspension <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

### Benefits for Longrunning Agents

Agent continuations directly benefit [[cost_and_latency_optimization_in_agent_operations | longrunning agents]] and their resilience by enabling:

*   **Fault Tolerance**: By allowing agents to snapshot their state, progress is preserved even if the underlying infrastructure fails <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Intermittent Execution**: Agents do not need to run continuously, which is ideal for workflows requiring human intervention or external asynchronous events <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Resource Optimization**: Shutting down agent loops when suspended can lead to more efficient resource usage.

This approach combines a human approval mechanism with arbitrary nesting of complex agents, offering a novel solution for robust agent deployment <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.