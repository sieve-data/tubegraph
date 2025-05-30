---
title: Opensource libraries for agent development
videoId: BFWviieMyGw
---

From: [[colemedin]] <br/> 
AGUI: An Open-Source Protocol for Agent-User Interaction
2025 has been a significant year for [[ai_agents_and_their_development | AI agents]] and agent protocols, such as Anthropic's MCP (connecting tools to agents) and Google's A2A (connecting agents to other agents) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite these advancements, a crucial missing piece for user interaction with [[ai_agents_and_their_development | agents]] has been a standard way to connect agents to a front end to turn them into full applications <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This challenge is addressed by AGUI <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

AGUI (Agent GUI) is a protocol designed to standardize the connection between your [[ai_agents_and_their_development | agents]] and your front end, facilitating user interaction <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is considered a game-changer for taking [[ai_agents_and_their_development | agents]] to the next level by enabling them to become full applications <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Development and Purpose
AGUI was developed by the CopilotKit team <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. CopilotKit itself is an [[open_source_ai_agent_development | open-source]] front-end library specifically for building agentic applications <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

AGUI functions as a middleman, similar to MCP, positioned between an application (e.g., built with React) and [[ai_agents_and_their_development | AI agents]] (e.g., built with [[understanding_ai_agent_frameworks | Langraph]], [[understanding_ai_agent_frameworks | Crew AI]], or [[understanding_ai_agent_frameworks | Pyantic AI]]) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Its primary goal is to make this connection seamless, similar to how MCP connects tools and A2A connects agents <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Addressing Development Challenges
Most [[ai_agents_and_their_development | agents]] require a user interface for interaction, especially for "human in the loop" processes where users need to work alongside agents <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Before AGUI, connecting a front end to an [[ai_agents_and_their_development | agent]] presented several [[ai_agent_development_challenges | challenges]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>:

*   **Real-time Output Streaming:** Users expect real-time output, similar to Claude or GPT, where the agent appears to be "typing" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This requires the API endpoint running the agent to stream tokens in real-time to the front end, which then needs to handle this streaming <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Tool Orchestration and Progress Display:** When agents use tools, the UI often needs to display the progress and results of these tool usages <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Framework Sprawl:** The diversity of backend [[understanding_ai_agent_frameworks | frameworks]] for building agents (e.g., [[understanding_ai_agent_frameworks | Langchain]], [[understanding_ai_agent_frameworks | Crew AI]], Mao) means UIs typically need different adapters and handle various edge cases <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

AGUI addresses these [[ai_agent_development_challenges | challenges]] by providing a single, standard protocol that acts as a middleman between front ends and diverse [[understanding_ai_agent_frameworks | agent frameworks]], simplifying development <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### How AGUI Works
AGUI is completely [[open_source_ai_agent_development | open-source]] and framework-agnostic <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This means developers can build any front end with any [[understanding_ai_agent_frameworks | framework]] and connect it to any [[ai_agents_and_their_development | agent]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

When a user interacts with an application, AGUI facilitates communication with the [[ai_agents_and_their_development | AI agent]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. For every operation performed by the agent (e.g., streaming text, making a tool call), AGUI emits standard events back to the front end <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. There are 16 different event types that provide the front end with all necessary information about the agent's activity <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>:
*   `run started`: Indicates the beginning of an agent execution, including thread ID and execution ID for tracking <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   `message started`: Signals the beginning of a streaming response <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   `text message content`: Contains chunks of text outputted in real-time as the agent "types" <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   `tool call chunk`: Indicates parameters related to a tool call <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   `message end`: Marks the end of a message <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   `run finished`: Signifies the completion of the agent's execution <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   `error events`: Allows the backend to inform the front end about specific issues encountered by the agent, preventing crashes <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

This event-driven communication standardizes how the front end displays agent activity, managing real-time streaming, tool orchestration, and simplifying integration with various [[understanding_ai_agent_frameworks | agent frameworks]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Practical Implementation
To work with AGUI, users need Node.js and npm <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. OpenAI can be used for the LLM <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

For example, a Python backend [[ai_agents_and_their_development | agent]] using Fast API can yield events like `run started`, `text message content` (for streamed text chunks), `text message end`, and `run finished` <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. This allows seamless integration with a JavaScript front end, even when switching the underlying [[ai_agents_and_their_development | agent]] technology <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

AI coding assistants like Windsurf and Cursor can aid in building with AGUI, helping with both backend [[ai_agents_and_their_development | agent]] compatibility and frontend development <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Documentation can be fed to these assistants via built-in features or through MCP servers for RAG knowledge bases <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

> [!info] AGUI's Current State
> AGUI is a new protocol and is still maturing <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. While not yet fully mature for all use cases, it is highly recommended to explore and learn it <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Its initial development and documentation are noted as superior to earlier protocols like MCP <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.