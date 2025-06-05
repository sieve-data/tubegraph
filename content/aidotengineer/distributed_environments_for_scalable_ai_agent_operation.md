---
title: Distributed environments for scalable AI agent operation
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

As [[Building effective AI agents | AI agents]] become more sophisticated and ready for production, key considerations arise regarding their deployment in [[Scaling AI agents in production | production settings]], particularly within distributed environments. The primary concerns revolve around integrating human oversight, ensuring reliability for long-running processes, and managing agent state in a scalable manner <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Challenges in Distributed AI Agent Deployment

Historically, [[Implementing AI agents in daily operations | implementing AI agents]] in a production setting introduces several challenges:
*   **Human Approval** Critical steps in agent processing often require human oversight, especially for high-value or high-risk tasks like transferring money or deleting accounts <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Ensuring that the agent can pause, allow human determination, and then resume is crucial <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Long-Running Agents** Many [[Building effective AI agents | agents]] are designed for complex, multi-step tasks, increasing the likelihood of failure over extended periods <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. Losing work due to failures (e.g., network or hardware) in such scenarios is a significant concern <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Distributed Operation** Agents are increasingly operating in distributed environments rather than just on local desktops <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This requires specific considerations for running them in a scalable manner <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Agent Loop Persistence** Most existing agent frameworks require the agent's processing loop to run continuously, even when waiting for external input like human responses <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This continuous running can be inefficient and problematic in large-scale, distributed deployments where resources might need to be released.

## Agent Continuations: A Solution for Scalability

Snaplogic has developed a new mechanism called "Agent Continuations" to address these challenges, particularly for [[Scaling AI agents in production | scaling AI agents in production]] and managing them in distributed settings <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Core Concept
Agent continuations are inspired by the programming language theory concept of "continuations," which allow a program's execution to be stopped at any point, bundled up, and then resumed later from that exact point <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

Similarly, Agent Continuations enable the capture of the full state of complex agents, allowing for:
*   **Arbitrary Human-in-the-Loop Processing**: Agents can pause execution, send their state to an application layer for human approval, and resume when the human provides a decision <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Reliable Agent Continuation**: By taking snapshots of the agent's state, work is preserved, and agents can resume from a point of failure without starting over <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Addressing Distributed Environments
A key advantage of Agent Continuations for [[Scaling AI agents in production | scaling AI agents in production]] is that once an agent is suspended and its continuation object is created, the agent's execution loops (or multiple agent loops) can be completely shut down <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. All necessary information is captured within the continuation object to restart everything exactly where it left off <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. This contrasts with traditional approaches that require continuous agent loop persistence <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

This capability is particularly powerful for [[Scaling AI agents in production | scaling AI agents in production]] because it allows:
*   **Resource Optimization**: Compute resources are not tied up waiting for human input or external events. They can be freed and reallocated.
*   **Fault Tolerance**: In a distributed environment, if a machine or process fails, the state is preserved, and the agent can be restarted elsewhere using the continuation object.
*   **Flexible Deployment**: Agents can be deployed across various machines or cloud instances, suspending and resuming as needed, without requiring constant connections.

### Implementation Details
The core insight behind Agent Continuations is leveraging the existing "messages array" used by LLMs within agents, which already acts as a log of interactions, preserving a significant portion of the agent's state <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. The continuation object wraps this messages array with additional metadata, enabling the system to understand why the agent suspended and how to resume <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

The mechanism supports [[Multiagent systems in AI | multi-level agents]] and [[Multiagent orchestration in AI copilot systems | multiagent orchestration]], allowing for arbitrary depths of nested agent calls (e.g., a main agent calling a sub-agent, which calls another sub-agent) to suspend and resume effectively <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>, <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>, <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Prototype and Future Directions
A prototype implementation, built on the OpenAI Python API, is available on GitHub <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. Future work aims to integrate this concept into existing frameworks like Strands or Pydantic AI, moving beyond just human approval to include arbitrary suspension points (e.g., after a certain time or number of turns) <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>, <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>. The approach is considered novel for its combination of human approval mechanisms and support for arbitrary nesting of complex agents <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

Snaplogic's Agent Creator, a visual agent-building platform, also incorporates prototyped continuations to allow users to [[Scaffolding AI agents for scalability | create sophisticated agents visually]] and visualize their execution <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>, <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>, <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>.

For further information:
*   [Agent Continuations Prototype on GitHub](https://github.com/your-repo-link) <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>
*   [SnapLogic Agent Creator](https://agentcreator.com) <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>