---
title: Managing longrunning agents in production
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

When [[building_effective_agents | agents]] are ready for a production setting, several considerations arise, particularly concerning human involvement and system resilience <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Key challenges include:
*   The need for human approval during agent processing steps <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   Ensuring agents can run for [[longrunning_workflows_in_ai_deployment | long periods of time]] in the presence of failures <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   Addressing issues with [[scaling_ai_agents_in_production | scaling AI agents in production]] and distributed environments <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## Challenges with [[implementing_ai_agents_in_daily_operations | Agents in Production]]

### Human in the Loop
A significant concern for [[implementing_ai_agents_in_daily_operations | agent automation]] is where human oversight fits into agent processing <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For users to be comfortable with agents, key aspects of their execution require human approval <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This is particularly relevant for high-value or high-risk tasks, such as transferring money or deleting an account <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. When an agent reaches such a point, it needs a mechanism to involve a human for final determination <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### [[longrunning_workflows_in_ai_deployment | Longrunning Agents]] and Failure Tolerance
Many agents are designed to be [[longrunning_workflows_in_ai_deployment | longrunning workflows in AI deployment]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The more steps involved in agentic processing, the longer a process runs, and the greater the chance of failure <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. To prevent the loss of significant work, there's a need to checkpoint agent state, allowing for resumption from a specific point rather than restarting from the beginning <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This is crucial for sophisticated agents performing complex tasks or extensive research across multiple systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Distributed Environments
Increasingly, agents will operate in distributed environments rather than just on a single desktop <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This introduces [[scaling_ai_agents_in_production | scaling AI agents in production]] considerations for reliable agent execution <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### [[state_management_and_continuation_in_agent_execution | Agent Loop Persistence]]
Standard agent execution often involves an LLM-tool loop <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This loop code must run continuously on a physical machine, whether in the cloud or on a desktop, to interact with the user or third-party channels like Slack <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Most existing frameworks require this agent loop to persist, even when waiting for human input <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This continuous running adds overhead and limits flexibility.

## Introducing Agent Continuations

To address these challenges, Snaplogic has developed a new mechanism called [[agent_continuations_for_ai_workflows | agent continuations]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Definition and Inspiration
[[agent_continuations_for_ai_workflows | Agent continuations]] allow for capturing the full state of complex agents <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This state can be used for:
*   Arbitrary human-in-the-loop processing <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   Providing a basis for reliable agent continuation through snapshots <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The concept is inspired by "continuations" from programming language theory, which allow stopping program execution, bundling up its state, and resuming from that point later <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Core Concepts and [[stateful_agents_and_ai_memory_management | State Management]]
A key insight for [[agent_continuations_for_ai_workflows | agent continuations]] is that LLM interactions already maintain a "messages array," which acts as a log of all interactions and is replayed to the LLM for its next inference <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This messages array already saves a significant portion of the agent's state <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

## Using Agent Continuations

### Standard Agent Execution
In a typical agent framework, tools are defined (e.g., using a decorator for Python functions), and an agent is instantiated with a list of these tools <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. A user prompt is sent to the agent, which then performs LLM requests and tool calls to generate a response <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

### Continuation-Enabled Execution
With [[agent_continuations_for_ai_workflows | continuation]] support, a tool can be designated as "needing approval" <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. Instead of a standard agent, a `continuation agent class` is used <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

When the agent needs to suspend (e.g., for human approval or another condition), the response becomes a *continuation object* <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This object contains metadata indicating the reason for suspension <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. The application layer can then inspect this object, provide input (e.g., human approval), and send the updated continuation object back to the agent <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The agent, recognizing it's a continuation object, will resume execution from the suspended point <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

Crucially, once the agent is suspended and the continuation object is created, the agent loops do *not* need to keep running; they can be shut down <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. The captured information in the continuation object is sufficient to restart everything where it left off <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

### Structure of the Continuation Object
A continuation object typically wraps the standard messages array and includes additional metadata:
*   **Resume Request:** Indicates the exact tool call or point to resume from <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
*   **Processed:** Populated with the outcome of the suspension, such as approval or disapproval <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

For complex, multi-level agents with sub-agents, the continuation object format is recursive, allowing for arbitrary layers of nesting <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This means a nested `resume request` can contain its own `continuations object` with its own messages and resume details, preserving the full state of the sub-agent <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Example: Multi-level HR Agent
Consider an HR agent that uses an email tool and an account agent sub-tool responsible for creating accounts and setting privileges <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. The account agent, in turn, has `create account` and `authorize account` tools, with `authorize account` requiring approval <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

When a user prompts the HR agent to create a new account, the process flows until the sub-agent's `authorize account` tool is invoked <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. At this point, human approval is needed, causing the agent to suspend and create a nested continuation object <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. This object propagates back to the application layer, expanding at each level until the full state is available for inspection and action <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. Once the application layer provides the approval, the continuation object is sent back to the HR agent, and the framework restores the agent's and sub-agent's states to continue processing <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

## Implementation and Future Directions
The prototype implementation is built on the OpenAI Python API with no other dependencies <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. It is available on GitHub <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

Future work aims to implement more general agent suspension beyond just human approval, allowing for arbitrary suspension points based on time, turns, or asynchronous requests <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>. The goal is not to develop a new, separate agent framework, but to extend existing ones like Strands or PyDantic AI with [[agent_continuations_for_ai_workflows | continuation]] capabilities <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

While other frameworks offer forms of [[state_management_and_continuation_in_agent_execution | state management]], they often lack the explicit human approval element or the sophistication to handle arbitrary depths of nested sub-agents <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. The [[agent_continuations_for_ai_workflows | agent continuations]] approach is novel in combining both a human approval mechanism and arbitrary nesting for complex agents <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

This work originated from the Agent Creator research group at Snaplogic, which provides a visual agent building interface and platform <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>. The continuations were prototyped both at the Python layer and within the higher-level Snaplogic Agent Creator environment <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

## Conclusion
[[agent_continuations_for_ai_workflows | Agent continuations]] offer a new mechanism for [[state_management_and_continuation_in_agent_execution | managing agent state]] and human-in-the-loop processing for [[longrunning_workflows_in_ai_deployment | longrunning workflows]] in [[scaling_ai_agents_in_production | AI deployment]] <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.