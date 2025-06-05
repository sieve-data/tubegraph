---
title: Improving user experience with multimodal interaction
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

The rapid growth of applications like ChatGPT, which has become one of the fastest-growing apps in history with hundreds of millions of daily users, highlights a significant challenge in user experience: complexity and confusion in its interface <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A key area for improvement lies in [[Multimodal interfaces for user interaction | multimodal interaction]], particularly the seamless integration of voice and text.

## Current Challenges in Multimodal AI Systems

Current iterations of AI applications, such as ChatGPT, often present a disjointed user experience when attempting [[Multimodal AI Systems | multimodal interaction]].

### Disconnected Voice and Text Functionality
When interacting with ChatGPT via voice, the system provides two distinct buttons for voice interaction: a voice-to-text option and a voice-to-voice option <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While the system can respond verbally with well-worded content, such as an email draft, it can *only* respond through voice <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This means users cannot collaborate on the written output directly <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The only way to access a written format is to end the voice call and locate a voice transcript with formatting <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

This segregated approach makes it feel as though the voice and text functionalities were developed by two different companies <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### "Shipping the Org Chart"
Scott Hansselman coined the term "shipping the org chart" to describe this phenomenon, where a product's user interface reflects the internal organizational structure rather than a cohesive user experience <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. An example is an electric vehicle (EV) dashboard where different displays (map, climate, speedometer) have varying fonts, revealing they are distinct Android tablets chained together, thus exposing the company's internal divisions <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. OpenAI is similarly "guilty" of this, where technical improvements are shipped without integrated marketing or [[User experience design with AI | user experience design]], resulting in a "science fair full of potential options" rather than a unified product <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Proposed Solutions for Enhanced User Experience

To address these challenges and improve [[User experience design with AI | user experience design with AI]], two key changes are proposed for applications like ChatGPT:
1.  **Allowing simultaneous voice and text interaction** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  **Smartly choosing the right model depending on the user's request** <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

These improvements can be implemented using off-the-shelf tools <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Integrated Multimodal Interaction
A redesigned interface would feature a voice button that transitions from a dormant state to a voice mode, similar to existing functionality <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Crucially, it would include a new "chat" button alongside mute and end call options <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This chat button would pull up an iMessage-like panel, allowing users to text while on a voice call, much like texting a friend during a FaceTime call <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This panel could display call controls, a reminder of previous questions, and a text response for details like email drafts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

This approach embodies the concept of [[Multimodal interfaces for user interaction | multimodal interfaces for user interaction]] by allowing users to fluidly switch between and combine communication modalities.

### Intelligent Model Selection and Information Delivery
The system should intelligently select the appropriate AI model or tool based on the complexity or nature of the user's request.

*   **Handling Detailed Requests**:
    *   For requests requiring longer details, such as links or drafts, the system could utilize "tool calls" to send text directly <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   The "send chat message" tool can be used to send details that are easier to explain via text <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This can be achieved with a simple description, allowing the model to intelligently send the right information as text <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

*   **Complex Reasoning with Specialized Models**:
    *   For more complex questions, a research tool could hand off the query to a "smarter" reasoning model <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   The Warp Terminal, a developer tool for writing code, demonstrates this by having a coding agent handle simple commands like "undo my last commit" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. For complex tasks like "refactor this entire codebase to use Flutter," it detects the complexity and writes a plan using a reasoning model to ensure code functionality <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   This "reasoning model" pattern can be applied using heuristics; for instance, if a user asks for details, pros, and cons, the system could hand off to a reasoning model, indicate it's processing, and then return a more detailed response <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   A dedicated tool for reasoning models can be used when a user wants to "go deeper" on a topic, sending details to the model and then responding back to the user or directly to the client <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Off-the-Shelf Tools
These improvements can be built using existing APIs. For live audio chat, "40 Realtime" can be utilized <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The overall system can then rely on tool calls to manage interactions <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

The source code for these proposed solutions is available on GitHub under "fix gpt" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.