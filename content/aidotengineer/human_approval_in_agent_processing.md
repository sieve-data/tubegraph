---
title: Human approval in agent processing
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

When [[AI agents and agentic workflows | AI agents]] are deployed in production settings, a significant concern is how to integrate [[human_oversight_and_interaction_in_aidriven_analysis | human oversight]] and approval into their operations <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. For people to become comfortable with [[implementing_ai_agents_in_daily_operations | agent automation]], it's crucial that key aspects of agent execution allow for a degree of human approval <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Challenges with Human-in-the-Loop Agents
Traditional approaches to "human-in-the-loop" processing for [[AI agents and agentic workflows | agents]] face several challenges:
*   **High-Value or High-Risk Tasks** Agents may encounter designated tools or tasks that involve high value or risk, such as transferring large sums of money or deleting accounts <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In these scenarios, there needs to be a mechanism for the agent to pause and allow a human to provide a final determination or decision <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Long-Running Processes** Many [[AI agents and agentic workflows | agents]] are designed to be long-running, involving numerous steps <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The longer a process runs, the higher the chance of failure <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Without a way to checkpoint or resume, all work done up to the point of failure could be lost <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Agent Loop Persistence** Most current [[developing_ai_agents_and_agentic_workflows | agent frameworks]] that support human-in-the-loop functionality require the underlying agent loop to run continuously <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This means the physical machine or cloud instance executing the agent must remain active, even if it's merely waiting for a human response from a communication channel like Slack <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This continuous running can be inefficient and costly.

## Agent Continuations: A Solution
To address these challenges, Snaplogic has [[developing_ai_agents_and_agentic_workflows | developed a new mechanism]] called "agent continuations" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Inspired by the programming language theory concept of continuations <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, agent continuations allow for capturing the full state of complex [[AI agents and agentic workflows | agents]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This state capture can be used for both arbitrary [[human_oversight_and_interaction_in_aidriven_analysis | human-in-the-loop]] processing and for creating reliable checkpoints to resume agent execution through snapshots <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The core idea is to pause agent execution, save its complete state, and then resume or continue the execution from that exact point at a later time <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### How Agent Continuations Facilitate Human Approval
The process of integrating human approval with agent continuations involves the following steps:
1.  **Tool Designation** Developers can designate specific tools within an [[AI agents and agentic workflows | agent's]] capabilities as needing approval <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
2.  **Suspension** When the [[AI agents and agentic workflows | agent]] reaches a point where an approved tool needs to be called, or any other suspension condition is met, it will automatically suspend <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
3.  **Continuation Object Creation** Upon suspension, a "continuation object" is created <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This object embeds the standard messages array (which maintains the history of interactions with the LLM) along with additional metadata required to resume execution <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
4.  **Application Layer Interaction** The continuation object is then sent back to the application layer. This layer extracts core information to make it easy for the application to understand why the agent suspended and to present the necessary information to the user for approval <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
5.  **Human Review and Update** A human [[human_reviews_of_ai_outputs | reviews the situation]] and provides their approval or disapproval <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. The application layer then updates the continuation object with this human decision <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
6.  **Resumption** The updated continuation object is sent back to the [[AI agents and agentic workflows | agent]] <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. The agent framework recognizes it as a continuation and uses the embedded logic and state to reconstruct the agent and resume its execution from the exact point of suspension <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

### Key Advantage: Decoupled Operations
A powerful aspect of agent continuations is that once the agent has suspended and a continuation object has been created, the underlying agent loops do *not* need to remain running <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. They can be shut down because all necessary information has been captured to restart everything exactly where it left off <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This addresses the challenge of continuous agent loop persistence.

### Support for Multi-Level Agents
[[AI agents and agentic workflows | Agents]] are becoming increasingly sophisticated, often involving a main orchestrator [[AI agents and agentic workflows | agent]] that delegates tasks to several sub-agents, which can, in turn, have their own sub-agents <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Agent continuations are designed to handle this complexity. The format for the continuation object is recursive, capable of supporting arbitrary layers of nesting, ensuring that even when a sub-agent requires human approval, the state of the entire multi-level agent can be saved and restored <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

>[!EXAMPLE] Multi-Level HR Agent
>An example shows an HR agent that uses an "Account Agent" as a sub-agent <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. The Account Agent has an "authorize account" tool that requires human approval <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. If the HR agent initiates an account creation process that eventually leads to the sub-agent needing authorization, the entire process suspends, a nested continuation object is propagated back to the application layer, and once approved, the process resumes from that exact point within the sub-agent <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

## Implementation Details
The prototype implementation is built on top of the OpenAI Python API <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. While other frameworks consider state management, this approach is novel in combining both a [[human_oversight_and_interaction_in_aidriven_analysis | human approval mechanism]] and the ability to handle arbitrary nesting of complex [[AI agents and agentic workflows | agents]] <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.

The work originated from the Agent Creator research group at Snaplogic, which also provides a visual [[developing_ai_agents_for_productivity | agent building interface]] and platform <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>. The continuation concept has been prototyped both at the Python layer and within Snaplogic's higher-level platform <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.