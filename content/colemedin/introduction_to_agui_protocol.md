---
title: Introduction to AGUI protocol
videoId: BFWviieMyGw
---

From: [[colemedin]] <br/> 

2025 has seen the rise of AI agents and agent protocols like Anthropic's [[Agent protocols like MCP and A2A | MCP]] for connecting tools to agents, and Google's [[Googles A2A protocol for AI agents | A2A]] for connecting agents to other agents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite their power, a significant gap remained: a standard way to connect agents to front ends, allowing users to interact with them as full applications <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This changed with the introduction of AGUI <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

AGUI is a protocol designed to standardize the connection between AI agents and user interfaces (front ends) <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It is considered a crucial "missing piece" for transforming agents into complete applications <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## What is AGUI?

AGUI was developed by the CopilotKit team <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. CopilotKit is an open-source front-end library specifically for [[Building AIdriven applications with AGUI | building agentic applications]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. AGUI serves as a middleman protocol, situated between an application built with frameworks like React and AI agents built with frameworks such as Langraph, Crew AI, or Pyantic AI <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Its primary goal is to facilitate seamless communication between these components, much like [[Agent protocols like MCP and A2A | MCP]] and [[Googles A2A protocol for AI agents | A2A]] do for tools and agents, respectively <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

AGUI is particularly valuable for conversational agents where users need to work alongside the AI, especially for "human in the loop" scenarios <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. It is less useful for entirely autonomous agents that operate solely in the background <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Challenges Before AGUI

Before AGUI, building front ends to connect with AI agents presented several challenges <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>:
*   **Real-time Streaming:** It was difficult to set up real-time output streaming, where the agent's response appears to be typed out in real-time, similar to Claude or GPT <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This required custom handling for API endpoints to stream tokens and for the front end to process them <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Tool Orchestration:** Displaying the progress and results of an agent's tool usage in the UI was complex, as a single agent execution could involve many components <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Framework Sprawl:** The multitude of backend frameworks for building agents (e.g., Langchain, Crew AI, Mao) meant that connecting a UI to each required different approaches, often necessitating the reinvention of adapters and handling numerous edge cases <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. AGUI provides a single standard to simplify this connection <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## How AGUI Works

AGUI is an open-source standard that does not rely on a specific framework <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Similar to [[Agent protocols like MCP and A2A | MCP]], which allows using different LLMs besides Claude, AGUI allows developers to build any front end with any framework and connect it to any agent <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

The process involves:
1.  A user interacts with an application (e.g., built with React) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  AGUI acts as a middleman, connecting the application to the AI agents <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
3.  When an agent performs an operation (e.g., streams text, makes a tool call), AGUI emits standardized events back to the front end <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
4.  The front end uses these standard events to display everything the agent is doing <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This solves problems related to real-time streaming, tool orchestration, and framework sprawl <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### AGUI Events

The core of AGUI lies in its standardized events that the backend emits to the front end <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. These events provide crucial metadata and information about the agent's actions:
*   **Run Started Event:** Signals the beginning of an agent's execution, including a thread ID for conversation tracking and an execution ID for the current run <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This metadata is important for tasks like fetching conversation history <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Message Start/End Events:** Indicates the beginning and end of streaming a response, with chunks of content in between <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Text Message Content Event:** Emitted for each chunk of text received from the LLM, allowing the front end to build up the response in real time <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Tool Call Chunk Event:** Used when the LLM outputs a tool call, signaling the front end that the parameters relate to a tool call <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Run Finished Event:** A final event indicating the completion of the agent's execution, informing the front end it can proceed with post-processing actions <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Error Events:** Allows the backend to send specific error information to the front end, preventing application crashes and enabling appropriate error handling <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

There are 16 total event types that can be sent, providing comprehensive information about the AI agent's operations to the front end <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. This standardized approach allows developers to use any LLM or framework as long as they emit these standard AGUI events <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Practical Implementation

The official AGUI documentation provides guides for [[Creating User Interfaces for AI Agents | building AI agents]] in the backend and frontend applications that work with the protocol <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Frontend Integration
When using a library like CopilotKit, the frontend (e.g., a React page) sets up an instance of CopilotKit pointing to an API endpoint where the AGUI-compatible agent is running <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. CopilotKit simplifies the integration of agent components within React <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. However, it's possible to build a custom frontend from scratch that leverages these AGUI events directly, watching for text messages to stream them out and tool calls to display them as desired <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

### Backend Implementation
AGUI allows for flexibility in backend language and framework. For example, an agent can be built using Python with Fast API, yielding AGUI events like "run started," "text message content" chunks, and "run finished" <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. This enables seamless switching between backend implementations (e.g., JavaScript agent to Python agent, or frameworks like Langchain to Crew AI) without requiring changes to the frontend, as long as the AGUI protocol is followed <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

### Aid with AI Coding Assistants
To assist developers, AGUI documentation provides an "llm's-fold.ext" file that can be used as documentation for AI coding assistants like Windsurf and Cursor <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. This knowledge base helps in [[Building AIdriven applications with AGUI | building compatible agents]] and frontends, making AGUI more accessible <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## Current State of AGUI

AGUI is a new protocol and is still maturing <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. While worth exploring and learning, it may not yet be suitable for all applications due to ongoing development <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. Similar to [[Agent protocols like MCP and A2A | MCP]] and [[Googles A2A protocol for AI agents | A2A]], which took time for widespread adoption (e.g., [[Agent protocols like MCP and A2A | MCP]] took about 4-5 months after its November release) <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>, AGUI is expected to follow a similar trajectory. However, the initial documentation and structure of AGUI are well-designed and easy to work with <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.