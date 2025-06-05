---
title: Challenges with current AI implementation
videoId: 2cEGQEllBGc
---

From: [[aidotengineer]] <br/> 

Current trends in AI implementation often focus on integrating chatbots into products, which is seen as an easy but often unhelpful solution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This approach is problematic because it fails to genuinely assist users <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Issues with Reactive AI and Chatbot Interfaces

The prevailing method for AI assistance makes AI reactive, waiting for user input and specific questions <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This leads to:
*   **Generic Interactions**: AI often asks non-specific "how can I help" questions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Lack of Context**: Most AI assistants do not proactively understand the user's immediate needs or work context <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Workflow Disruption**: Chat interfaces introduce contact switching and extra windows, breaking the natural flow of work <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Inefficiency**: Users waste time trying to explain their needs to the AI <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## A Proactive AI Approach: The Tigon Example

Inspired by the concept behind Clippy—a system with the right idea but poor execution and timing—modern technology allows for a proactive AI approach <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The AI issue tracker, Tigon, demonstrates this by having AI anticipate user needs rather than waiting for commands <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Proactive AI Modes

1.  **Suggestion Mode**: The AI tracks user input in real-time, understands the context, and offers specific, contextual questions or suggestions at the opportune moment, without needing a chat window <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   *Example*: When a user reports a bug, the AI immediately asks relevant follow-up questions instead of generic ones <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  **Action Mode**: The AI can recognize complex tasks and suggest better ways to organize work based on previous data and understanding of optimal organization <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This shows the AI's understanding of the domain <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   *Example*: If a user writes an issue that could be split into sub-issues, the AI identifies and suggests this division, considering timelines and resources like a project manager <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  **Question Plus Action Mode**: This combines questioning with proactive action, allowing the AI to ask questions and help manage issues within the natural workflow, seamlessly guiding the user <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### User Control
Users retain control over proactive AI suggestions, with the ability to revert changes with a single click <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## Principles for Proactive AI Design

To foster proactive AI in products, three simple rules can be followed:
1.  **Supplement User Agency**: AI should enhance, not replace, the user's control <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
2.  **Offer Recommendations, Never Force**: AI should provide suggestions without imposing them on the user <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
3.  **Part of Natural Workflow, Not a Stop**: AI should integrate seamlessly into the user's tasks without causing interruptions <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Applications of Proactive AI

This proactive pattern can be applied across various professional tools:
*   **Code Editors**: AI could proactively monitor for common pitfalls and suggest improvements, especially beneficial for developers learning new languages or frameworks <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Design Tools**: Tools could make real-time suggestions for accessible design, eliminating the need for post-design checks <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Communication Tools**: AI could prepare relevant context before meetings or locate documents mentioned during calls, acting as a personal advisor <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Shifting Towards Better AI Interface Design

To implement proactive AI, consider the following:
*   **Identify Friction Points**: Look for areas where users stop to ask for help; these are opportunities for proactive assistance <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Analyze User Behavior Patterns**: Understand where users frequently need help or what questions they consistently ask to identify automation clues <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Focus on Context**: Determine where users get stuck; this is where AI can provide the most valuable help <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The field of AI interface design is still evolving, and simply copying existing chatbot interfaces is not the optimal solution <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Experimentation and challenging the status quo with unexpected UI solutions are encouraged <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.