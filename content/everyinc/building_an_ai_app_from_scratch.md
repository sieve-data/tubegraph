---
title: Building an AI app from scratch
videoId: MhKKKBG28a4
---

From: [[everyinc]] <br/> 

## The Rapid Development of Kora: A Case Study
Kora, an AI-powered email management product, serves as a prime example of the rapid pace at which AI applications can be built today. The initial functioning version (V1) of Kora was developed in a single day <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>, a feat considered unimaginable just a year or two prior <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. The full product, which drastically reduces email stress by taking away 90% of non-essential emails and briefing them twice a day <a class="yt-timestamp" data-t="03:46:27">[03:46:27]</a>, was built end-to-end in approximately three months <a class="yt-timestamp" data-t="06:05:13">[06:05:13]</a>.

Kora's development initially explored an "email assistant" model, generating email drafts <a class="yt-timestamp" data-t="06:43:08">[06:43:08]</a>. However, it was realized that even a highly skilled LLM couldn't mimic a user's voice or provide necessary context for about 50% of emails requiring responses <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. The team pivoted to address the core cognitive load: the stress of managing an inbox, not necessarily responding to emails <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

## The New Reality of Software Development
The landscape of software development has dramatically shifted. Building software is now significantly cheaper <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. This change makes the "what" you're building far more important than the "how," as a rough version of almost anything can be built in a couple of days <a class="yt-timestamp" data-t="08:35:10">[08:35:10]</a>. Much of the underlying code can be written by AI <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>, leading to a new paradigm where the ability to define and refine the problem, and iterate rapidly, is more valuable than just writing code <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.

## Kieran's Rapid Development Process
Kieran, the GM of Kora, outlines his process for rapidly [[Developing apps and prototypes using AI | developing apps and prototypes using AI]]:

### Ideation and Prompt Generation
The process often starts with an idea, which then "buzzes" in his head <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. He takes a walk to get into a flow state, using voice memos to talk out a large, detailed prompt, envisioning the app and its elements <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>. This includes describing the app's appearance, functionality, and even abstract concepts like "fancy" or "Apple design" <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. He continues adding details until his brain is "empty" <a class="yt-timestamp" data-t="21:47:00">[21:47:00]</a>.

### Tools and Workflow
1.  **Voice Memos & Transcription:** The initial voice recording is transcribed using tools like Mech Whisper or iOS 18's native transcription <a class="yt-timestamp" data-t="23:32:00">[23:32:00]</a>.
2.  **LLM Integration:** The transcribed prompt is then fed into his chosen LLM (currently 01 Pro due to its deeper thinking capabilities) to convert it into a Product Requirements Document (PRD) <a class="yt-timestamp" data-t="24:52:00">[24:52:00]</a>. He also uses Claude Sonnet for this <a class="yt-timestamp" data-t="25:03:00">[25:03:00]</a>.
3.  **Coding with Cursor:** For coding, Kieran primarily uses [[Building an app with OpenAI and Cursor | Cursor composer]] <a class="yt-timestamp" data-t="31:44:00">[31:44:00]</a>. While AI writes 80-90% of the code, 100% of the thinking behind it is human <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. The AI acts as a collaborator, accelerating tedious tasks <a class="yt-timestamp" data-t="11:55:00">[11:55:59]</a>.

This rapid iterative process allows for significant progress in a short time. An example was a music app with a complex compositional system that Kieran tested with a new model to see its limits <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.

### The Enduring Role of Prompt Engineering
Despite discussions that prompt engineering is "dead," the ability to articulate a vision in detail (e.g., "I want an app that does this, the background to look like this, and the button style like this") remains crucial <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>. This detailed vision, even if rambling initially, forms the core of effective prompt engineering <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.

## AI as a Collaborator: Writing Code and Beyond
Kieran's process highlights AI not just as a code generator but as a thought partner.

### Cursor Rules and Notepads for Context
To ensure the AI remembers past decisions and follows specific guidelines, Kieran uses `.cursorrules` files within a project <a class="yt-timestamp" data-t="38:46:00">[38:46:00]</a>. These rules, often derived from past errors, provide instructions on how the AI should structure code or apply conventions (e.g., helpers in controllers) <a class="yt-timestamp" data-t="39:31:00">[39:31:00]</a>. Additionally, "notepads" (saved prompts or PRDs) can be injected into specific composer sessions for context, unlike cursor rules which are always followed <a class="yt-timestamp" data-t="47:05:00">[47:05:00]</a>.

### Balancing Human Oversight and AI Delegation
When building an app with AI, especially for larger products like Kora that use familiar technologies like Ruby on Rails and HTML <a class="yt-timestamp" data-t="35:42:00">[35:42:00]</a>, a developer's existing knowledge allows for informed opinion and feedback on the AI-generated code <a class="yt-timestamp" data-t="36:06:00">[36:06:00]</a>. Errors in AI-written code often indicate a lack of clarity in the initial idea or problem definition <a class="yt-timestamp" data-t="36:25:00">[36:25:00]</a>. The human's role shifts to being very clear on direction and structure to prevent the AI from "going rogue" <a class="yt-timestamp" data-t="37:16:00">[37:16:00]</a>.

For one-off applications, a more "copy-paste monkey" approach of pasting errors back into the AI to fix them is viable <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>. The limiting factor is no longer knowledge but "patience and your own determination" <a class="yt-timestamp" data-t="33:27:00">[33:27:00]</a>. The agent mode in tools like Cursor is powerful because it can run code, detect errors, and automatically fix them, saving significant debugging time <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>.

## The Philosophy of [[Building applications with AI | Building AI Applications]]: More Than Just Problem Solving
Software development, especially with AI, is evolving beyond merely solving well-defined problems.

### Focus on User Experience and "Feeling"
Kieran, with a background in music composition, views software development similarly to telling a story or creating an experience that makes a user "feel a certain way" <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>. This means thinking big to small, prioritizing the user's excitement and feeling over just functional perfection <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>. This shift makes software more like content: easier to write, able to go viral, and focused on creating a desired feeling <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

In this new paradigm, where anyone can [[Developing AI tools for entrepreneurship | build an email summarizing tool]], the product that makes users *feel* great will win <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. This necessitates a strong perspective, taste, and vision, which can be applied through AI to force a certain methodology on users (e.g., Kora's approach to email) <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

### Navigating the "Startup Roller Coaster" and Prioritization
A key challenge in [[Building AI applications for large scale use | building AI applications for large scale use]] is navigating the "startup roller coaster" <a class="yt-timestamp" data-t="56:47:00">[56:47:00]</a>. Early user feedback, often from manual onboarding, is crucial for identifying real concerns, especially for high-pressure products like email management <a class="yt-timestamp" data-t="53:30:00">[53:30:00]</a>. However, developers must balance internal biases (loving their own product) with external feedback, recognizing that early data can lead to emotional highs or lows <a class="yt-timestamp" data-t="56:51:00">[56:51:00]</a>. The solution is often to gather more data from a larger user base to identify patterns and prioritize problems <a class="yt-timestamp" data-t="56:20:00">[56:20:00]</a>.

Startups should focus on being "so good at one thing" for a specific type of person that it's 10 times better than competitors, even if it lacks feature parity <a class="yt-timestamp" data-t="59:18:00">[59:18:00]</a>. This "mushy" problem-solving requires a clear perspective and continuous iteration <a class="yt-timestamp" data-t="01:01:32">[01:01:32]</a>.

## The Evolving Landscape of AI Development
The progress in AI, while astounding, is compared to a "false peak" in hiking <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>. Each breakthrough reveals more complexity and a "new frontier" <a class="yt-timestamp" data-t="01:08:33">[01:08:33]</a>. While AI labs focus on solving verifiable, step-by-step problems like coding or math, many real-world problems are "squishy" and not easily reducible to such solutions <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.

This highlights the continued importance of human taste, intuition, and pattern matching, which LLMs are good at, but for which optimization requires a feedback loop of "do something, get data, come up with new ideas, try again" <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>. The human role in [[Applying agency in AI development | applying agency in AI development]] will be to enjoy the iterative journey, embrace the messiness, and collaborate to ask difficult questions <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>. AI will expand the circle of human knowledge, opening new doors for creativity rather than limiting it <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>. Kora exemplifies this by making email more human, filtering out automated noise to allow users to focus on direct human interactions <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>.