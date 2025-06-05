---
title: Challenges of agent execution and human approval
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

When deploying AI agents into a production setting, several significant [[challenges_in_developing_ai_agents | challenges]] arise, particularly concerning human interaction and the reliability of long-running processes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A new mechanism called agent continuations has been developed by Snaplogic to address these issues <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a> <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Challenges in Agent Execution

### Human in the Loop
A primary concern in agent processing is determining the human's role <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For users to be comfortable with agent automation, human oversight is required for key aspects of agent execution <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This often involves the agent reaching a point where a designated tool or task (e.g., transferring a large sum of money or deleting an account) is high-value or high-risk <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. At such junctures, a mechanism is needed to ensure the human can provide the final determination or decision <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Long-Running Agents and Failure Tolerance
Many agents are designed to be long-running, involving numerous steps in their processing <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The longer a process runs, the greater the chance of a failure, such as a network or hardware issue <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. To prevent the loss of significant work, a method is needed to checkpoint the agent's state, enabling resumption from a point other than the beginning <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Dynamic LLM APIs and Rate Limiting
The landscape of Large Language Models (LLMs) and their APIs is rapidly changing, leading to dynamic usage patterns <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. New models are frequently released and heavily used, which can lead to issues like rate limiting <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Mechanisms are required to handle these situations <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Multi-Level and Nested Agents
Agents are becoming increasingly sophisticated, often involving a main orchestrator agent with several sub-agents, which can themselves have sub-agents (nested configurations) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Addressing human approval and state saving in such complex, multi-level agent architectures presents additional [[challenges_in_applevel_infrastructure_with_ai_agents | challenges]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Agent Loop Persistence
The code driving an agent's loop must run on a physical machine, whether in the cloud or on a desktop <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Most current agent frameworks require this agent loop to run continuously, even when waiting for external responses like human input from Slack <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This continuous persistence is a challenge, as it ties up resources <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Agent Continuations: A Solution
Agent continuations are a new mechanism inspired by the programming language theory concept of continuations <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. In programming, a continuation allows stopping program execution at any point, bundling its state, and resuming it later <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This is akin to taking a snapshot of the program's execution <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

Agent continuations apply this concept to AI agents, allowing the pausing and saving of an agent's state at any point during its execution, including across multiple tool calls, LLM calls, and even calls to sub-agents <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This saved state can then be returned to the application layer for purposes such as processing human approval or persisting the agent's state for later resumption <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### How Agent Continuations Work
The feasibility of agent continuations builds on how LLMs in agents already work: by maintaining a "messages array" <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This array acts as a log of all interactions and is replayed to the LLM for its next inference, effectively saving much of the agent's state <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

When an agent needs to suspend (e.g., for human approval or another predefined condition), a "continuation object" is created <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a> <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This object embeds the standard messages array along with additional metadata <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. This metadata provides enough information to resume the agent's execution <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The continuation object is then sent back to the top-level application layer, which can inspect its metadata to understand the reason for suspension and provide updates, such as human approval <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

Once the application layer updates the continuation object, it can be sent back to the agent <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. The agent framework recognizes it as a continuation and contains the logic to reconstruct the agent's state, allowing it to continue execution from the suspension point <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

### Key Advantage: Decoupled Execution
A crucial aspect of agent continuations is that after the agent is suspended and the continuation object is created, there is no need to keep any of the agent loops running in the system <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. The loops can be shut down because all necessary information has been captured to restart everything exactly where it left off <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This capability addresses the challenge of agent loop persistence and resource consumption.

### Support for Nested Agents
The continuation object format is recursive and can handle arbitrary layers of agent nesting <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a> <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. This means complex, multi-level agent structures can be suspended and resumed, with sub-agent states correctly captured within the overarching continuation <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a> <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

Agent continuations are considered novel because they combine both a human approval mechanism and the ability to handle arbitrary nesting depths for complex agents <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>. They represent a significant step in [[evaluating_ai_agent_performance_and_reliability | improving the reliability]] and [[evaluating_ai_agents_and_assistants | manageability]] of agents in production environments <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.