---
title: MultiAgent Communication Systems
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

[[Multiagent systems in technical workflows | Multiagent systems]] involve multiple [[components_of_ai_agents | AI agents]] interacting with each other <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. This contrasts with traditional [[different_architectures_for_ai_agents | AI agent architectures]] where agents might be trapped within a single Python file, unable to run asynchronously or exist independently <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a> <a class="yt-timestamp" data-t="01:01:33">[01:01:33]</a>.

## Limitations of Current Multiagent Frameworks

Many existing multi-agent frameworks, such as Autogen, often lack true independence among agents <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a> <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>. These agents are typically stateless, meaning they do not retain experiences or skills over time, limiting the benefits of a multi-agent setup <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a> <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>. For instance, an expert agent from one multi-agent group cannot be easily extracted and used in another <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.

## Leta's Approach to Multiagent Communication

Leta addresses these limitations by enabling [[multiagentic_systems_in_ai | stateful agents]] that run as services backed by APIs <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a> <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>. This design means that [[multiagent_systems_and_their_applications | multi-agent interaction]] is fundamentally achieved through message passing over APIs <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a> <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>. The ability to import the Leta client directly within a tool allows [[components_of_ai_agents | agents]] to send messages to other [[components_of_ai_agents | agents]], create new ones, and manage their memory <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a> <a class="yt-timestamp" data-t="01:02:57">[01:02:57]</a>.

### Types of Multiagent Communication

Leta supports different patterns for [[multiagent_systems_and_their_applications | multi-agent communication]]:

*   **Asynchronous Messaging** <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>: This mimics human communication, where an agent sends a message and immediately receives a receipt, allowing it to continue its execution without waiting for a reply <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a> <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>.
*   **Synchronous Messaging** <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>: In certain scenarios, it's beneficial for an agent's execution to pause until a reply is received, for example, when an agent needs to consult a supervisor <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a> <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>.
*   **Group Messaging (Supervisor-Worker Concept)** <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>: Agents can be grouped using tags, allowing a supervisor agent to broadcast messages to all agents matching specific tags, facilitating tasks like delegated research or parallelized operations <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a> <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.

### Implementation and Benefits

The `multi-agent messaging tool` is crucial for enabling communication between agents in Leta <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a> <a class="yt-timestamp" data-t="01:07:19">[01:07:19]</a>. This tool, like others in Leta, operates within a sandbox environment, preventing interference between different agents' tools <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a> <a class="yt-timestamp" data-t="01:00:30">[01:00:30]</a>.

The ability for agents to be stateful and communicate via APIs unlocks significant potential for [[multiagent_orchestration_for_ai_copilot_development | multiagent orchestration]], allowing for human-like interaction patterns <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. Agents can be easily managed by adding or removing tools, which can immediately impact their ability to communicate or perform specific actions <a class="yt-timestamp" data-t="01:11:37">[01:11:37]</a> <a class="yt-timestamp" data-t="01:11:40">[01:11:40]</a>.

A prominent use case for [[multiagent_systems_and_their_applications | multi-agent communication systems]] is in enterprise deployments for [[multiagent_systems_in_technical_workflows | stateful workflows]] where agents process transactions and learn about users over time, without necessarily relying on a chatbot interface <a class="yt-timestamp" data-t="01:13:21">[01:13:21]</a> <a class="yt-timestamp" data-t="01:13:33">[01:13:33]</a>.