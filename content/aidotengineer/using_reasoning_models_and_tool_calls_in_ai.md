---
title: Using reasoning models and tool calls in AI
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

ChatGPT quickly became one of the fastest-growing applications in history <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite its popularity, its user experience can be confusing <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The application often feels like its different components were built by separate teams, lacking a cohesive multimodal interface where text and voice interact seamlessly <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## The "Shipping the Org Chart" Problem

This issue is akin to what Scott Hansselman described as "shipping the org chart" <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. He illustrated this by describing the experience of being in an electric vehicle where the map, climate controls, and speedometer all had different fonts, revealing that they were essentially three Android tablets chained together, reflecting the company's internal organizational structure rather than a unified user experience <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. OpenAI exhibits a similar pattern, where rapid technical improvements are shipped without full integration, leading to a "science fair full of potential options" <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.

## Enhancing AI Interaction with Tool Calls and Reasoning Models

To address these limitations, two key improvements for applications like ChatGPT are proposed:
1.  Allowing simultaneous voice and text interaction <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
2.  Smartly choosing the appropriate AI model based on the user's request <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

These enhancements can be achieved using off-the-shelf [[function_calling_in_ai_models | tools and functions]] <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

### The Power of Tool Calls

[[Function calling in AI models | Tool calls]] enable AI models to perform specific actions or access external information. For instance, a real-time audio chat can leverage [[function_calling_in_ai_models | tool calls]] to:
*   Send text messages for longer details, links, or drafts <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   Hand off to a smarter model for more complex queries and then return with an answer <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

An example of a specific [[developing_custom_ai_tools_and_functions | tool]] is the `send chat message` tool, which allows the AI to provide details that are easier to convey via text <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. This can be achieved with simple prompts and descriptive instructions <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

### Leveraging Reasoning Models

For more detailed or complex inquiries, [[Chain of Thought reasoning in AI | reasoning models]] are crucial. These models are designed to:
*   Handle complex questions by breaking them down <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   Write a plan or process to ensure the desired outcome, particularly in tasks like code refactoring <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
*   Provide more detailed responses, even informing the user about the thinking process involved <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

A common pattern involves using heuristics: if a user asks for details, pros, or cons, the request can be handed off to a [[Chain of Thought reasoning in AI | reasoning model]] <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>. Another specific [[developing_custom_ai_tools_and_functions | tool]] for [[Chain of Thought reasoning in AI | reasoning models]] sends the conversation details to the reasoning model whenever a user wants to delve deeper into a topic <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

### Practical Application: An Enhanced AI Experience

An improved AI experience can feature a voice interface with an integrated chat panel. This allows users to speak while simultaneously viewing or typing text, similar to texting a friend during a FaceTime call <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Consider the following interaction:
1.  **User asks via voice**: "Can you send me a link to a park that I should go visit?" <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>
2.  **AI responds via voice and sends text via a [[function_calling_in_ai_models | tool call]]**: "Of course. I'll send you a link to a popular park in California." <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a> (A link appears in the chat panel).
3.  **User asks for more detail via voice**: "I've heard about Yosemite. Can you tell me more about its history? Go deep." <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>
4.  **AI responds via voice and sends detailed text via a [[Chain of Thought reasoning in AI | reasoning model]] tool call**: "Yosemite National Park's history is rich, beginning with its ancient Native American heritage and leading to its establishment as a national park. Check the chat for more details." <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a> (Extensive historical information appears in the chat panel).

This seamless integration of voice and text, facilitated by [[function_calling_in_ai_models | tool calls]] for specific actions and [[Chain of Thought reasoning in AI | reasoning models]] for deeper analysis, creates a far more intuitive and powerful user experience <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. The source code for such an implementation is available on GitHub under "fix gpt" <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.