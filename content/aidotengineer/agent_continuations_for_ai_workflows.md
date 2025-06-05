---
title: Agent continuations for AI workflows
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

[[ai_agents_and_agentic_workflows | AI agents]] are increasingly capable of performing complex tasks, but moving them into a production setting introduces several challenges <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These include the need for human approval during processing steps, managing [[longrunning_workflows_in_ai_deployment | long-running agents]] that are susceptible to failure, and enabling [[scaling_ai_agents_in_production | scaling AI agents in production]] within a distributed environment <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Agent continuations are a new mechanism developed by Snaplogic to address these issues, enabling the capture of the full state of complex agents for human-in-the-loop processing and reliable continuation through snapshots <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This work originated from the Agent Creator research group at Snaplogic <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Challenges in AI Agent Deployment

When deploying [[ai_agents_and_agentic_workflows | AI agents]] and [[developing_ai_agents_and_agentic_workflows | agentic workflows]], several challenges arise:

*   **Human in the Loop**: For comfort with [[ai_in_workflow_automation | agent automation]], key aspects of agent execution require human oversight <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Agents may reach a point where a designated high-value or high-risk task (e.g., transferring money, deleting accounts) requires human determination or decision <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Long-Running Agents and Failure**: Many [[ai_agents_and_agentic_workflows | agents]] will be [[longrunning_workflows_in_ai_deployment | long-running]] due to numerous steps in [[developing_ai_agents_and_agentic_workflows | agentic processing]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The longer a process runs, the greater the chance of failure (e.g., network, hardware) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. It is desirable to checkpoint agent state to resume from a point other than the beginning, preventing loss of work <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Distributed Environments**: Increasingly, agents operate in distributed environments rather than just on local desktops, necessitating considerations for [[scaling_ai_agents_in_production | running agents in a scalable distributed environment]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Agent Loop Persistence**: Most current frameworks supporting human-in-the-loop require the agent loop (the code running on a physical machine) to run continuously, even when waiting for human response <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This means the agent loop must persist <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. A key goal for agent continuations was to allow full shutdown and later restart of agent loops <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

Sophisticated, multi-level agents (e.g., orchestrator agents with sub-agents) complicate these challenges <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Understanding Agent Continuations

Agent continuations are inspired by the programming language theory concept of continuations <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Continuations in Programming Languages**: This concept allows pausing program execution at any point, bundling its state, and resuming execution later from that point <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It's like taking a snapshot of program execution <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Agent Continuations**: This mechanism aims to do the same for [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. At any point during agent execution (including multiple tool calls, LLM calls, and sub-agent calls), the agent can be paused, its state saved, and then returned to the application layer for purposes like processing human approval or persisting state for later resumption <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>, <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

A key insight for agent continuations is that [[ai_agents_and_agentic_workflows | agent]] interactions with Large Language Models (LLMs) already do significant bookkeeping by maintaining a 'messages array' <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This array serves as a log of all interactions and is replayed to the LLM for its next inference <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. While the messages array is a good starting point, it's not entirely sufficient on its own <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## How Agent Continuations Work

### Basic Agent Execution (without Continuations)
Standard agent frameworks involve:
1.  Defining tools as Python functions using a decorator <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
2.  Creating an agent by sending the tool list to it <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
3.  Instantiating the agent and making a request with a user prompt <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
4.  The agent performs LLM requests and tool calling, eventually returning a response <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

### Agent Execution with Continuations
The approach with continuation support introduces minimal changes:
1.  A tool can be designated as "needing approval" <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>, <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
2.  Instead of a standard agent class, a `ContinuationAgent` class is used <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>, <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
3.  During execution, the response may be a `ContinuationObject` if the agent needs to suspend <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
4.  The `ContinuationObject` contains metadata explaining the reason for suspension (e.g., human approval) <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>, <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
5.  The application layer inspects the object, provides necessary input (e.g., true/false for approval), and sends the updated `ContinuationObject` back to the agent using the same request method <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>, <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
6.  The agent recognizes the `ContinuationObject` and resumes from the point of suspension <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>, <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

### Implementation Details
*   **Suspension**: When a suspension condition is met (e.g., human approval is needed), a `ContinuationObject` is created <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>, <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **Continuation Object Structure**: It embeds the standard messages array and additional metadata, which provides information on how to resume execution <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. Before being returned, core information is extracted to the top level for easy application layer interaction <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>, <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
    *   A single-level continuation object includes the messages array, a `resume_request` (indicating where to resume), and `processed` (e.g., approval status) <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
    *   For nested agents (e.g., an agent calling a sub-agent), the format is recursive, with a `resume_request` containing its own continuation object, messages, and processed status <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>, <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   **Resumption**: When the updated `ContinuationObject` is sent back, the agent uses its logic to reconstruct its state and continue execution <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>, <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
*   **Key Benefit: Decoupling**: Once the agent is suspended and the `ContinuationObject` created, the agent loops do not need to keep running <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. They can be shut down because all necessary information is captured for restart <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Example: Multi-Level HR Agent

A practical example demonstrates a multi-level HR agent:
*   A top-level HR agent has an email tool and access to an account agent tool <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>, <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   The account agent (a sub-agent) has its own tools: `create_account` and `authorize_account` <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>, <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>, <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   The `authorize_account` tool specifically requires human approval <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>, <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

In a scenario where a user prompts the HR agent to create a new account, the process unfolds as follows:
1.  The HR agent processes the request.
2.  It calls the account agent sub-agent.
3.  The account agent eventually reaches the `authorize_account` tool, which requires human approval <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>, <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
4.  At this point, the agent suspends, creating a `ContinuationObject` <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. This object propagates back through each level of nesting (from sub-agent to main agent) until it reaches the application layer <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
5.  The application layer inspects the `ContinuationObject` (which contains the sub-agent's messages and a top-level approval object for user interaction) and provides the human approval (e.g., setting "processed" to `true`) <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>, <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>, <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.
6.  The updated `ContinuationObject` is sent back to the HR agent <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
7.  The framework restores the state of both the main agent and the sub-agent to where they were when approval was needed <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>, <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
8.  The agent continues processing, resulting in a successful account creation and security level granting <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. The final output shows a normal messages array, with no sign of the continuation <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

## Prototype and Future Work

The prototype for agent continuations is built on top of the OpenAI Python API and has no other dependencies <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>, <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. The implementation is available on GitHub <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

Future directions for agent continuations include:
*   **General Agent Suspension**: Expanding beyond just human approval to arbitrary suspension points, such as after a certain amount of time, a specific number of turns, or asynchronous requests <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>, <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>, <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
*   **Framework Extension**: The goal is not to develop a new, separate agent framework, but rather to extend existing frameworks like Langchain or Pyantic AI <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>, <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.

While some other frameworks offer forms of state management, agent continuations are considered novel because they combine both a human approval element and the sophistication of handling arbitrary depths of nesting into sub-agents <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>, <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>, <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>, <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

The work on agent continuations was developed by the Agent Creator team at Snaplogic <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>. Agent Creator is Snaplogic's visual agent building interface and platform, allowing users to create sophisticated agents visually and visualize agent execution <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>, <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>, <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. Continuations were prototyped both at the Python layer and within the higher-level Snaplogic Agent Creator environment <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>, <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.

In conclusion, agent continuations represent a significant advance in [[best_practices_for_building_resilient_ai_workflows | managing agent state]] and enabling human-in-the-loop processing for [[ai_in_workflow_automation | AI workflows]] <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.