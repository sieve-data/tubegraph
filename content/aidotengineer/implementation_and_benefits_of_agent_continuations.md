---
title: Implementation and benefits of agent continuations
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

Agent continuations are a novel mechanism developed at Snaplogic to address critical challenges in deploying AI agents to production, specifically human approval workflows and failure resilience for long-running agents <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This concept allows the full state of complex agents to be captured, enabling both arbitrary human-in-the-loop processing and reliable [[longrunning_agents_and_failure_resilience | agent continuation]] through snapshots <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Challenges in Agent Execution

Before agent continuations, several key challenges existed when moving agents from development to production <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>:

*   **Human Approval and Oversight**
    *   A significant concern is integrating human oversight into agent processing to ensure comfort with agent automation <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   High-value or high-risk tasks, such as transferring money or deleting an account, require a mechanism for human intervention to provide final determination or decision <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a> <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Long-Running Agents and Failure Resilience**
    *   Many agents are designed to be long-running, involving numerous steps <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a> <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
    *   The longer a process runs, the higher the chance of failure (e.g., network or hardware issues) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a> <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   There is a need to avoid losing all work an agent has done and to be able to checkpoint agent state for resumption from a point other than the beginning <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Distributed Environments**
    *   Agents are increasingly operating in distributed environments, not just on a single desktop <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Considerations for running agents scalably in such environments are crucial <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Multi-level Agents**
    *   Agents are becoming more sophisticated, often involving a main orchestrator agent with several nested [[multiagent_systems_and_their_applications | sub-agents]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   Addressing human approval and state saving becomes more complex with these multi-level configurations <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Agent Loop Persistence**
    *   Most current agent frameworks require the agent loop (the code driving the agent) to run continuously, even when waiting for human input <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   This poses challenges for scalability and resource management <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## What are Agent Continuations?

Agent continuations are inspired by the programming language theory concept of "continuations" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. In programming, a continuation allows stopping program execution at any point, bundling its state, and resuming it later from that exact point <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a> <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This is akin to taking a snapshot of the program's execution <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

[[agent_continuations_for_ai_workflows | Agent continuations]] apply this idea to AI agents <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>:
At any point during agent execution—which may involve multiple tool calls, LLM interactions, and even calls to sub-agents—the agent can be paused, its state saved, and then returned to the application layer for processing, such as awaiting human approval or for persistence <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a> <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

## Implementation Details

The implementation of agent continuations leverages the existing way LLMs interact with agents <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Messages Array as a Basis
The core insight is that agent interactions with LLMs already maintain a "messages array," which acts as a log of all past interactions <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This history is replayed back to the LLM for its next inference, effectively saving much of the agent's state <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### The Continuation Object
When an agent needs to suspend (e.g., for human approval), a "continuation object" is created <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a> <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. This object embeds:
*   The standard messages array <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   Additional metadata, such as a "resume request" indicating the exact tool call or point for resumption, and a "processed" field for updates like human approval <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a> <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

For multi-level agents, the continuation object format is recursive, handling arbitrary layers of nesting, allowing sub-agents to also capture their states <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a> <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Workflow with Continuations
1.  **Designation**: Tools that require human approval are explicitly designated <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
2.  **Suspension**: If an agent reaches a designated suspension point (e.g., needing human approval or another condition), it suspends execution <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a> <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
3.  **Continuation Object Creation**: A continuation object is created, encapsulating the agent's current state. This object propagates back to the top-level agent, extracting core information for the application layer <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a> <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a> <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
4.  **Application Layer Interaction**: The application layer receives the continuation object, inspects its metadata (e.g., reason for suspension), and presents it to the user for input or approval <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a> <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.
5.  **Resumption**: Once the application layer updates the continuation object (e.g., with human approval), it sends the object back to the agent <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a> <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. The agent framework then uses the logic within the continuation object to reconstruct the agent's state and resume execution from the point of suspension <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a> <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

## Benefits of Agent Continuations

*   **Decoupled Agent Loops**: A key benefit is that once a continuation object is created, the agent loops do not need to keep running <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. They can be fully shut down, as the continuation object captures enough information to restart everything back to where it was <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This addresses the challenge of [[stateful_ai_agents | agent loop persistence]] and resource management <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Seamless Human-in-the-Loop**: Enables effective and natural integration of human approval steps for high-stakes actions within complex agent workflows <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Enhanced Failure Resilience**: Allows for checkpointing of agent state, meaning that if an agent encounters a failure, it can be resumed from the last saved state rather than restarting from the beginning, preventing loss of work <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Support for Complex Agent Architectures**: The recursive nature of the continuation object natively supports multi-level agents and nested sub-agents, making it applicable to sophisticated [[multiagent_systems_and_their_applications | multiagent systems]] <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   **General Agent Suspension**: Beyond human approval, the mechanism can be extended to support arbitrary suspension points, such as after a certain amount of time, a specific number of turns, or for asynchronous requests <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

## Prototype and Future Directions

A prototype implementation has been built on top of the OpenAI Python API, with no other dependencies <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. The aim is not to develop a new, separate agent framework but to extend existing frameworks like LangChain or PyDantic AI to incorporate this functionality <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

While other frameworks offer forms of state management, agent continuations are considered novel because they combine both a human approval mechanism and arbitrary nesting of complex agent states <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a> <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>. This work emerged from Snaplogic's Agent Creator research group, where continuations were prototyped in both Python and the visual agent building interface <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a> <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>.