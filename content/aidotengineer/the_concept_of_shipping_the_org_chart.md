---
title: The concept of shipping the org chart
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

The term "shipping the org chart," coined by Scott Hanselman, describes a phenomenon where a product's user experience directly reflects the internal organizational structure of the company that built it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This often results in a disjointed or confusing user interface, as different features or components, developed by separate teams, lack cohesion <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Manifestation of the Problem

### In Electric Vehicles
A classic example is observed in electric vehicles (EVs), where dashboard displays might appear as a collection of separate interfaces rather than a unified system <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. For instance, the map, climate controls, and speedometer might each have different fonts and layouts, indicating they were developed by distinct internal teams or even resemble "three Android tablets chained together" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This reveals the organizational chart of the large international auto company <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### In AI Applications (e.g., ChatGPT)
OpenAI's ChatGPT is cited as another example, despite being one of the fastest-growing apps in history <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The application's design can be confusing <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

Key issues demonstrating "shipping the org chart" in ChatGPT include:
*   **Confusing Voice Interaction** Two separate buttons for voice interaction exist: one for voice-to-text and another for voice-to-voice <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Lack of Multimodality** When using voice mode, the AI can only respond through voice. To collaborate on a written output, such as an email, the user must end the call and locate a voice transcript with formatting at the end <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This implies two distinct development paths for voice and text functionalities, making them feel like "these two apps were built by two different companies" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Disregard for User Experience** Often, a technical improvement is shipped because it's what consumers crave, but without consultation from marketing, leading to a "science fair full of potential options" rather than a coherent product <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Proposed Solutions and Improvements for AI Applications

To address the issues stemming from "shipping the org chart," two primary changes are suggested for AI applications like ChatGPT:

1.  **Simultaneous Voice and Text Interaction** Allow users to interact using both voice and text at the same time <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   **Implementation** This can be achieved with off-the-shelf tools like 40 Realtime for live audio chat <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   **User Interface Concept** A proposed UI features a voice button to initiate voice mode, with standard controls (mute, end call) and a new "chat" button <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Pressing the "chat" button would open a panel similar to iMessage, allowing users to text while on a call, resembling texting a friend during a FaceTime call <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This allows the AI to send longer details, links, or drafts via text while maintaining the voice conversation <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

2.  **Smart Model Selection** The AI should intelligently choose the appropriate model based on the user's request <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   **Dynamic Hand-off** For simple requests, a basic model could suffice. For complex queries requiring more detail (e.g., pros and cons, in-depth history), a research tool could hand off the request to a "smarter model" or "reasoning model" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   **Example from Warp Terminal** This pattern is explored in Warp Terminal, a developer tool for writing code <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
        *   For simple commands (e.g., "undo my last commit"), it hands off to a coding agent <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
        *   For complex requests (e.g., "refactor this entire codebase to use Flutter"), it detects complexity and writes a plan using a reasoning model to ensure the code works <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   **Implementation with Tool Calls** This intelligent hand-off can be implemented using tool calls, where a "send chat message" tool can be used for details better explained via text <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Similarly, a tool can be used to send queries to a reasoning model when a user wants to "go deeper on a topic" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Simple prompts can achieve significant results with this approach <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

These improvements aim to create a more integrated and intuitive user experience, moving away from a product that reflects the internal organizational divisions and towards one that prioritizes user needs.