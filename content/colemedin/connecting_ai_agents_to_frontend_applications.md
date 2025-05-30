---
title: Connecting AI agents to frontend applications
videoId: BFWviieMyGw
---

From: [[colemedin]] <br/> 

Connecting [[understanding_ai_agents | AI agents]] to frontend applications is crucial for enabling user interaction and transforming agents into full applications <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, especially as 2025 has been a significant year for [[understanding_ai_agents | AI agents]] and agent protocols <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While protocols like Anthropic's MCP facilitate connecting tools and Google's A2A enable seamless agent-to-agent connections, a critical missing piece has been a standard way to [[integrating_ai_with_front_ends | connect agents to any frontend]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Introducing AGUI: The Agent-to-GUI Protocol

This challenge has been addressed with the introduction of AGUI (Agent-to-GUI), a protocol specifically designed for [[integrating_ai_with_front_ends | connecting AI agents to frontend applications]] and users in a standardized manner <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. AGUI is poised to be a game-changer, akin to MCP and A2A <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

Developed by the CopilotKit team—known for their open-source frontend library for [[building_ai_agents | building agentic applications]]—AGUI acts as a middleman <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It sits between the user's application (e.g., built with React) and the [[understanding_ai_agents | AI agents]] (e.g., built with Langraph, Crew AI, Pyantic AI) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This standardized connection is essential for allowing users to work alongside their agents <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, particularly for "human in the loop" processes where user oversight is desired <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Challenges Solved by AGUI

Before AGUI, [[creating_custom_frontends_for_ai_agents | building custom frontends for AI agents]] presented several difficulties:

*   **Real-time Output:** Achieving real-time output that simulates typing (like in Claude or GPT) is complex. It requires the agent's API endpoint to stream tokens in real-time, and the frontend to handle these streams <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Tool Orchestration:** Displaying the progress and results of an agent's tool usage in the UI is not trivial, as a single agent execution can involve many components to display <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Framework Sprawl:** The diversity of backend frameworks (e.g., Langchain, Crew AI, Mao) for [[building_ai_agents | building AI agents]] meant that connecting a UI often required reinventing adapters and handling different edge cases for each framework <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

AGUI addresses these issues by providing a single, open-source standard that simplifies development by abstracting away framework-specific complexities <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. It allows developers to use any frontend framework and connect it to any agent <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## How AGUI Works

AGUI operates by emitting a series of standard events from the backend agent to the frontend <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. When an [[understanding_ai_agents | agent]] performs an operation (e.g., streams text, makes a tool call), these standardized events are sent through AGUI to the frontend <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This allows the frontend to have a consistent way to display everything the agent is doing <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

Key event types include:
*   `run started`: Initiates the agent execution <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   `message started`: Indicates the beginning of a streaming response <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   `content`: Contains chunks of text content as they are generated <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   `tool call chunk event`: Relays parameters related to a tool call (e.g., changing background color) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   `message end`: Signifies the conclusion of a message <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   `run finished`: Marks the completion of the agent's execution <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   `error events`: Communicates specific issues encountered by the agent in the backend to the frontend for appropriate handling <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

These 16 different event types provide the frontend with all necessary information about the [[integrating_ai_agents_with_live_platforms | AI agent's]] actions <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. This means developers can use any LLM or framework, as long as these standard events are emitted <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Practical Implementation

[[transforming_ai_agents_into_api_endpoints | Transforming AI agents into API endpoints]] and then consuming them with AGUI is straightforward. The CopilotKit library simplifies this process for React applications by providing a `CopilotKit` instance that points to the agent's runtime URL <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

For example, a JavaScript agent using GPT-4.1 Mini can stream text and tool calls (like changing background color) via AGUI events <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. These `text message chunk` and `tool call chunk` events allow the frontend to build up the response and display tool interactions in real-time <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

AGUI's flexibility also allows for different backend languages. An [[understanding_ai_agents | AI agent]] built with a Python backend (e.g., using Fast API) can emit the same AGUI events as a JavaScript backend <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This enables seamless switching of the backend agent without requiring changes to the frontend <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

![[integrating_ai_with_front_ends#AGUI Architecture]]

## Current State and Future Outlook

AGUI is a new protocol, still in its early stages <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. While not yet fully mature for all production scenarios, it offers a robust foundation and is worth exploring for [[building_and_deploying_custom_ai_front_ends | building and deploying custom AI front ends]] <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. The developer experience is promising, showing significant improvements over other protocols in their initial releases <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

AI coding assistants like Windsurf and Cursor can further facilitate [[creating_custom_frontends_for_ai_agents | creating custom frontends for AI agents]] by providing documentation and code generation capabilities tailored to AGUI <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

The integration of agent protocols, such as MCP with services like Lutra, also highlights the growing ecosystem for [[integrating_ai_agents_with_services_like_slack_and_google_drive | integrating AI agents with services like Slack and Google Drive]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, enhancing their utility beyond simple conversational interfaces.