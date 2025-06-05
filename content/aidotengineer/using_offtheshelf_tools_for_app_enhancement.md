---
title: Using offtheshelf tools for app enhancement
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

While ChatGPT is one of the fastest-growing applications in history, with hundreds of millions of daily users, its user experience can be confusing <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A key issue is the disjointed interaction between its voice and text functionalities, making them feel as if they were developed by separate companies <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This phenomenon, termed "shipping the org chart" by Scott Hanselman, describes how internal organizational structures can inadvertently manifest as fragmented user experiences <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Identifying Key User Experience Issues

The current ChatGPT interface presents two separate buttons for voice interaction: a voice-to-text option and a voice-to-voice option <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While the voice interface can respond to prompts like writing an email <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, it can only respond through voice <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. To collaborate on a written email, users must end the call and find a voice transcript, often with formatting applied at the end <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. An ideal experience would be multimodal, combining text and voice seamlessly <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This lack of cohesive design is similar to a "science fair full of potential options," rather than a unified product <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Proposed Enhancements for AI Applications

Two primary changes can significantly improve the user experience:
1.  **Simultaneous Voice and Text Interaction**: Allowing users to interact using both voice and text at the same time <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  **Intelligent Model Selection**: Automatically choosing the most appropriate AI model based on the user's query <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Leveraging Off-the-Shelf Tools

These enhancements can be achieved using [[use_of_open_source_tools_for_ai_development | off-the-shelf tools]] and APIs <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For instance, "40 Realtime" can facilitate live audio chat, while [[ai_integration_and_tool_calling | tool calls]] can manage the rest <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Sending Text Details**: An application can be designed to send text for longer details such as links and drafts <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Smarter Model Handoff**: A research tool could hand off complex queries to a more capable model to generate a detailed answer <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Enhanced User Interface Concept

Imagine an updated interface where a voice button transitions the app to voice mode, complete with mute, end call, and a new "chat" button <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This chat button would reveal a panel similar to iMessage, allowing users to text while on a call, with call controls at the top, a reminder of past queries, and a text response area for detailed outputs like email drafts <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Handling Complex Queries with Reasoning Models

For queries requiring more detail, a "reasoning model" pattern can be employed. This concept is explored in developer tools like Warp Terminal, which enables writing code in any environment <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Simple Actions**: For simple tasks, such as "undo my last commit," the system hands off to a coding agent that runs commands in the terminal <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Complex Actions**: For complex requests, like "refactor this entire codebase to use Flutter instead," the system detects complexity and uses a reasoning model to formulate a plan, ensuring the code functions correctly <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

This pattern, leveraging heuristics, allows the system to hand off to a reasoning model when details, pros, and cons are requested, indicate thinking time, and then return a comprehensive response <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Practical Implementation with Off-the-Shelf APIs

Building these features with [[using_tools_and_function_calls_with_ai_sdk | off-the-shelf APIs]] is straightforward <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. For instance, when asked for a park link and then its history, the system can provide a link and then elaborate on the history, prompting the user to "check the chat for more details" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

A "send chat message" tool can be used to send details that are more easily explained via text <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This can be achieved with simple descriptions, without extensive system prompts, demonstrating the power of simple prompts in modern AI development <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For reasoning models, another tool can be used to delve deeper into a topic, sending details to the model and allowing it to respond or dump information directly into the client <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The source code for these enhancements is available on GitHub under "fix gpt" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.