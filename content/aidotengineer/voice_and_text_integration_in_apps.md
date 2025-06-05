---
title: Voice and text integration in apps
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

## The Problem: Lack of Multimodality in Chatbots

ChatGPT is recognized as one of the fastest-growing applications in history, used by hundreds of millions daily <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite its popularity, the current design of its voice interaction can be confusing <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The application presents two distinct buttons for voice interaction: a voice-to-text option and a voice-to-voice option <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

When using the voice-to-voice option, the system responds with a well-worded email, but it can only communicate through voice <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. To collaborate on the written email, users must end the call and find a voice transcript with formatting <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This highlights a critical lack of multimodal interaction where text and voice work together seamlessly <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### "Shipping the Org Chart"

This disjointed user experience is likened to "shipping the org chart," a concept explained by Scott Hanselman <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Hanselman described sitting in an electric vehicle where the map, climate controls, and speedometer all displayed different fonts, revealing them to be three Android tablets chained together <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This indicated the organizational structure of the large international auto company <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

Similarly, OpenAI is seen as guilty of this, where a technical improvement shipped by a "whiz kid" is exactly what consumers want, but marketing is never consulted <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This results in a "science fair full of potential options" rather than a cohesive product <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Proposed Solutions for Improved Integration

To fix these issues in [[conversational_ai_applications_in_business | conversational AI applications]], two key changes are proposed for ChatGPT:
1.  Allowing voice and text interaction simultaneously <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  Smartly choosing the right model based on the user's request <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

These improvements can be achieved using off-the-shelf tools <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **40 Realtime** can provide live audio chat <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, facilitating [[voicefirst_ai_overlays | voicefirst AI overlays]].
*   **Tool calls** can handle the rest, enabling the system to send texts for longer details like links and drafts <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   A **research tool** could hand off to a smarter model and return with a detailed answer <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Enhanced User Interface Concept

An improved interface would feature a voice button that transitions the app to a voice mode <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This mode would include mute and end call controls, along with a new "chat" button <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Activating the chat button would pull up an iMessage-like panel, allowing users to text while on a call, similar to a FaceTime call <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This panel would show call controls at the top, a reminder of what was asked, and a text response for details like email drafts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Smart Model Selection

The system could also adapt to complex queries. For instance, in a developer tool like Warp Terminal for writing code, a simple request like "undo my last commit" can be handled by a coding agent running commands <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For more complex questions, such as "refactor this entire codebase to use Flutter instead," the system detects the complexity and writes a plan using a "reasoning model" to ensure the code works <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

This pattern can be applied using heuristics: if a user asks for details or pros and cons, the system could hand off to a reasoning model, indicate its thinking time, and then return a more detailed response <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This represents a significant step towards the [[future_directions_for_voicefirst_ai | future directions for Voicefirst AI]].

## Demonstration of Enhanced Integration

A practical demonstration illustrates this enhanced [[integrating_openai_api_with_voice_agents | integrating OpenAI API with voice agents]]:
*   A user asks, "Can you send me a link to a park that I should go visit?" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   The system responds verbally, "I'll send you a link to a popular park in California," and simultaneously sends the link via text in the chat panel <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   When asked, "Can you tell me more about its history? Go deep," the system verbally provides an overview and then directs the user to "Check the chat for more details" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This shows an improved [[evaluation_of_voice_applications_including_audio and text | evaluation of voice applications including audio and text]].

### Technical Implementation

This multimodal interaction is achieved using tool calls for handling text input <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. A "send chat message" tool sends details that are easier to explain via text <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This is implemented without a specific system prompt, simply by adding a description that allows the system to intelligently send relevant information as text <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

For "reasoning models," another tool is used <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. When a user wishes to delve deeper into a topic, this tool sends details to the reasoning model, which then responds back to the main model or directly to the client <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This approach leverages the power of simple prompts to achieve complex behaviors <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The source code for this "fix gpt" project is available on GitHub <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.