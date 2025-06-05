---
title: ChatGPT design issues
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

Despite being one of the fastest-growing applications in history with hundreds of millions of daily users, ChatGPT presents significant design challenges that lead to a confusing user experience <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Current Design Problems

The primary issue stems from the disjointed integration of its functionalities, particularly between voice and text interactions.

### Disconnected Voice and Text Interfaces
ChatGPT features separate buttons for voice-to-text and voice-to-voice interaction <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While it can respond through voice, collaborating on a written output, like an email, requires ending the call and finding a voice transcript <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This lack of multimodal interaction makes it feel as if "these two apps were built by two different companies" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### "Shipping the Org Chart"
This design flaw is analogous to what Scott Hansselman describes as "shipping the org chart" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. He illustrates this with an electric vehicle where the map, climate controls, and speedometer all use different fonts and appear to be three separate Android tablets chained together, revealing the internal organizational structure rather than a unified product <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. OpenAI is similarly "guilty of this" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, where technical improvements are shipped without marketing consultation, resulting in a "science fair full of potential options" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> rather than a cohesive user experience.

## Proposed Solutions and Improvements

To address these issues, two key changes are proposed:
1.  Allowing simultaneous voice and text interaction <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Smartly choosing the appropriate model based on the user's request <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

These improvements can be achieved using "off-the-shelf tools" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Integrated Multimodal Experience
A redesigned interface could feature a voice button that activates a voice mode, operating similarly to existing voice assistants but with integrated controls for mute, end call, and a new "chat" button <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This "chat" button would pull up an iMessage-like panel, allowing users to text while on a call, with call controls at the top and text responses for detailed information or email drafts <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Smart Model Selection
The system could intelligently hand off tasks to different models based on complexity:
*   **Simple Requests**: For straightforward commands like "undo my last commit," a coding agent could directly run commands <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Complex Questions**: For detailed requests like "refactor this entire codebase to use Flutter instead," the system could detect complexity and engage a "reasoning model" to write a plan, ensuring the code functions correctly <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This pattern is effective when asking for details or pros and cons, allowing the system to take longer to think and provide a more comprehensive response <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Technical Implementation

Implementing these improvements can leverage existing APIs:
*   **Live Audio Chat**: Utilized with "40 Realtime" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Tool Calls**: Can handle various tasks, including sending text for longer details, links, or drafts <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **`send chat message` tool**: This tool is used for sending details that are easier to convey via text <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Its description enables the system to intelligently send appropriate information via text <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **`reasoning model` tool**: Activated when a user wants to delve deeper into a topic, allowing the system to gather details and formulate a detailed response or dump it directly into the client <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The source code for a potential solution is available on GitHub under "fix gpt" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.