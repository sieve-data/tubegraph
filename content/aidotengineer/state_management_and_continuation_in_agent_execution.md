---
title: State management and continuation in agent execution
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

When deploying AI agents into production, several considerations arise, including the need for human approval during processing steps and the reliability of agents running for long periods in the presence of failures <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. [[agent_continuations_for_ai_workflows | Agent continuations]] offer a new mechanism to address these challenges <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Introducing Agent Continuations

[[agent_continuations_for_ai_workflows | Agent continuations]], developed by Snaplogic's agent creator research group, allow for capturing the full state of complex agents <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This capability supports both arbitrary human-in-the-loop processing and provides a basis for reliable agent continuation through taking snapshots <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The concept of agent continuations is inspired by the programming language theory concept of continuations <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This long-standing concept allows for stopping program execution at any point, bundling its state, and then resuming or continuing execution from that specific point at a later time <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. It enables taking a snapshot of the program's execution for later resumption <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Challenges in Agent Execution

Several general challenges are faced with agents today:
*   **Human-in-the-Loop** Humans need to be comfortable with agent automation, requiring human oversight for key aspects of agent execution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This is crucial for high-value or high-risk tasks, such as transferring large sums of money or deleting accounts, where a human needs to provide final determination <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **[[managing_longrunning_agents_in_production | Long-running Agents]]** Many agents are designed to be [[managing_longrunning_agents_in_production | long-running]], involving numerous steps in their processing <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The longer a process runs, the higher the chance of failure, necessitating a way to checkpoint agent state to resume without losing all prior work <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Distributed Environments** Agents are increasingly operating in distributed environments, not just on a desktop <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **[[multiagent_systems_in_ai | Multi-Level Agents]]** Sophisticated agents often feature a main orchestrator agent with several [[multiagent_systems_in_ai | sub-agents]], which can further have their own [[multiagent_systems_in_ai | sub-agents]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This hierarchical structure complicates handling human approval and state saving <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Agent Loop Persistence** Traditional frameworks often require the agent loop (the code performing the execution) to run continuously, even when waiting for external input like a human response <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This can be inefficient.

## Understanding Basic Agent Execution

An agent fundamentally operates as a loop, involving calls to a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The LLM specifies potential tools to use, and if it determines a tool is needed, the agent loop calls that tool, collects the results, and sends them back to the LLM in a progressive cycle <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. A tool can even be another agent, creating [[multiagent_systems_in_ai | sub-agent]] structures <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## How Agent Continuations Work

The feasibility of agent continuations stems from how agents interact with LLMs, specifically through the maintenance of a "messages array" <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This array acts as a log of all interactions and is replayed back to the LLM to make its next inference, effectively preserving much of the agent's state <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Usage in a Framework

When using a framework with [[agent_continuations_for_ai_workflows | continuation]] support, a tool can be designated as "needing approval" <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. Instead of a standard agent class, a "continuation agent class" is used <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

If the agent needs to suspend (e.g., for human approval), the response is a "continuation object" instead of a complete agent response <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This object contains metadata explaining the reason for suspension <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. The application layer can inspect this object, provide an update (e.g., human approval or disapproval), and send the updated continuation object back to the agent <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The agent then knows to resume execution from the point of suspension <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

### Implementation Details

When an agent needs to suspend, a continuation object is created <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This object embeds the standard messages array along with additional metadata <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. This metadata provides enough information for the continuation to resume when sent back to the agent <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The key insight is that once the continuation object is created, the agent loops can be completely shut down, as all necessary information has been captured to restart everything <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

The continuation object's structure supports arbitrary layers of nesting, enabling it to handle [[multiagent_systems_in_ai | multi-level agents]] where sub-agents might also suspend <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. For example, a `resume request` within a continuation object can contain its own nested continuation object for a [[multiagent_systems_in_ai | sub-agent]] <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

### Example: Multi-Level HR Agent

Consider a [[multiagent_systems_in_ai | multi-level]] HR agent with an email tool and an account agent tool (a [[multiagent_systems_in_ai | sub-agent]]) <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. The account agent itself has `create account` and `authorize account` tools, with `authorize account` requiring human approval <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

When the HR agent processes a request to create a new account, the [[multiagent_systems_in_ai | sub-agent]] (account agent) might eventually need human approval for the `authorize account` tool <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. At this point, the agent will suspend, create a continuation object, and return it to the application layer for processing <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. The continuation object propagates back through each level, expanding until the full object reaches the application to inspect and act on <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. Once the application updates the object (e.g., with approval), it's sent back to the HR agent, and the framework restores the agent's state (including [[multiagent_systems_in_ai | sub-agent]] state) to resume execution <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

## Prototype and Future Directions

The prototype implementation is built on the OpenAI Python API with no other dependencies <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. The work is being extended beyond human approval to include more general agent suspension points, such as after a certain time, number of turns, or asynchronous requests <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>. The aim is not to create a new agent framework, but to extend existing ones like Strands or Pyantic AI <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

While other frameworks offer forms of state management, this approach is considered novel because it combines a human approval mechanism with the ability to handle arbitrary depths of nesting in complex agents <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. This work emerged from the Agent Creator team at Snaplogic, Snaplogic's visual agent [[building_effective_agents | building]] interface and platform <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>.

In conclusion, [[agent_continuations_for_ai_workflows | agent continuations]] provide a new mechanism for managing agent state and facilitating human-in-the-loop processing <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.