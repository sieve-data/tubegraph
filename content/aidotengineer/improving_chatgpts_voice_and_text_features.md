---
title: Improving ChatGPTs voice and text features
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

ChatGPT is one of the fastest-growing applications in history, but its current voice and text interaction features present significant [[design_flaws_in_chatgpt | design flaws]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These issues can make the app confusing and limit its utility as a comprehensive conversational system <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Current Limitations of ChatGPT

Currently, ChatGPT features two separate buttons for voice interaction: a voice-to-text option and a voice-to-voice option <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While the voice-to-voice feature can provide nicely worded responses, it's limited to voice output only <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This means users cannot collaborate on written content directly within the voice interface <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. To access a voice transcript or any formatting, users must end the call <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

This segregated approach makes the voice and text features feel like they were built by "two different companies," lacking a seamless multimodal experience <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This phenomenon, termed "shipping the org chart" by Scott Hanselman, occurs when an organization's internal structure is inadvertently reflected in the product's disjointed user experience <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Proposed Improvements and Solutions

To address these [[challenges_in_building_ai_voice_agents | challenges in building AI voice agents]], two main changes are proposed for ChatGPT:
1.  **Simultaneous Voice and Text Interaction**: Allowing users to interact using both voice and text at the same time <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  **Intelligent Model Selection**: Smartly choosing the appropriate AI model based on the complexity and nature of the user's request <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

These improvements can be implemented using off-the-shelf tools <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For instance, "40 Realtime" can provide live audio chat, while "tool calls" can manage other functionalities <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Enhanced User Interface for [[Voice and Multimodal AI Agents | Multimodal Interaction]]

A redesigned voice mode interface would enable a more integrated experience:
*   **Persistent Voice Mode**: A voice button transitions the system into a continuous voice mode <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Integrated Chat Panel**: A new "chat" button would pull up an iMessage-like panel <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This allows users to text a "friend" while on a "FaceTime call," with call controls at the top and a text response area for more detailed outputs like email drafts <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Intelligent Model Handoff for Complex Queries

For queries requiring more detail or complex processing, a "reasoning model" can be employed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This pattern is demonstrated by Warp Terminal, a developer tool that uses an AI agent to handle coding tasks <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

*   **Simple Tasks**: A coding agent can execute commands directly (e.g., "undo my last commit") <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Complex Tasks**: For intricate requests (e.g., "refactor this entire codebase to use Flutter"), the system detects complexity and uses a reasoning model to formulate a plan <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Heuristics for Handoff**: If a user asks for "details and pros and cons," the system can hand off to a reasoning model, indicate thinking time, and then return a more detailed response <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Implementation Details

[[Voice AI engineering challenges and solutions | These solutions can be built using off-the-shelf APIs]]:
*   **Send Chat Message Tool**: A "send chat message" tool, powered by tool calls, allows the system to send details that are easier to convey via text <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This tool is effective with a simple description, enabling the model to smartly determine when to send text <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Reasoning Model Tool**: Another tool is designated for "reasoning models." When a user wishes to delve deeper into a topic, this tool sends the details to a more capable model, which then processes the information and sends a detailed response back to the client <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The source code for these improvements is available on GitHub under "fix gpt" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. These patterns demonstrate the effectiveness of [[building_a_reliable_conversation_system_for_voice_agents | building a reliable conversation system for voice agents]] by integrating multimodal interaction and intelligent model routing, moving [[ai_agents_beyond_chat_gpt | AI agents beyond ChatGPT]]'s current limitations.