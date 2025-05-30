---
title: Challenges and strategies for AI startups
videoId: MhKKKBG28a4
---

From: [[everyinc]] <br/> 

The landscape of building software and developing products has dramatically shifted with the advent of AI, presenting both significant [[challenges_and_opportunities_in_ai_startups | challenges and opportunities for AI startups]] <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. The reduced cost of building software means that the "what" of a product—the problem it solves and the experience it creates—has become far more critical than the "how" <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.

## Case Study: Kora and the New Era of Software Development

Kora, an AI-powered email management product, exemplifies many of the unique aspects of building an AI startup today <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

### The Problem with Email
Kora was developed to solve the universal "dread" associated with email inboxes, where users often face thousands of unread messages and constant demands <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. The core solution is to reduce stress by filtering out 90% of emails and providing two daily summarized briefs <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. This allows users to quickly scroll through summaries of newsletters, partnership updates, financial statements, and promotions, and then be "done" without manually archiving <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

### Pivoting and Problem Definition
Kora initially started as an "email assistant" to draft emails, a common approach for many AI products <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. However, the team realized that even the best Large Language Models (LLMs) struggled with context, making it hard to draft truly good emails for about 50% of use cases <a class="yt-timestamp" data-t="07:07:00">[07:07:07]</a>. The real "cognitive load" and stress came from managing and cleaning the inbox, not necessarily responding to emails, which can be the "pleasurable part" as it progresses things forward <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. This led to the pivot to email summarization and filtering.

### The Changing Economics of Software
With AI, building software has become significantly cheaper and faster <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. A rough version of almost anything can be built in a couple of days <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>. This shift makes the journey of defining *what* to build, and iterating on that vision, more valuable than the underlying code itself, as much of the code can now be AI-generated <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.

## Accelerated Development with AI
The speed of development with AI tools is unprecedented. Kora's V1 was functional within a single day <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

### Kieran's Process
The development process for Kora involved:
1.  **Ideation during walks:** Talking out a prompt while walking to achieve a "flow state" and build the prompt in the head <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>, <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
2.  **Voice recording:** Using a memo recorder to speak out a detailed prompt <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>, <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.
3.  **Transcription:** Converting the voice memo to text using tools like Mech Whisper or iOS 18's built-in transcription <a class="yt-timestamp" data-t="23:28:00">[23:28:00]</a>.
4.  **LLM integration:** Taking the transcribed prompt to a chosen LLM (e.g., `o1 Pro`) to convert it into a Product Requirements Document (PRD) <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>, <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.
5.  **Coding and refinement:** Using coding assistants like `cursor composer` to generate and refine the code <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>, <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>.

### Prompt Engineering
Despite claims that prompt engineering is "dead," the ability to provide detailed descriptions and vision for an application, its features, and its aesthetic (e.g., "I want an app that does this," "I want the background to look like this") remains crucial <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>, <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>. This skill in articulating a vision is essential for guiding AI development.

### AI as a Collaborator
AI acts as a "collaborator," enabling faster execution of tedious tasks <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. For Kora, 80-90% of the code was written by AI, but 100% of it was "thought of" by the human developer <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. This shifts the developer's role to be more like a writer who knows how to program, focusing on the story and experience of the software <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

### Tools and Techniques
*   **LLMs:** `o1 Pro` is favored for its "deep thinking" capabilities for planning, strategies, and non-coding collaboration, despite being slower <a class="yt-timestamp" data-t="24:55:00">[24:55:00]</a>. `Claud Sonet` is also mentioned as a good alternative <a class="yt-timestamp" data-t="25:05:00">[25:05:00]</a>. The slowness of `o1 Pro` can even be beneficial, forcing developers to "chill a little bit" amidst the fast pace of AI work <a class="yt-timestamp" data-t="27:07:00">[27:07:00]</a>.
*   **Coding Assistants:** `Cursor Composer` and `Wind Surf` are used for generating code, with agents that can run code, see errors, and fix them automatically, saving significant debugging time <a class="yt-timestamp" data-t="31:11:00">[31:11:00]</a>, <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>.
*   **Context Management:** For consistent AI behavior, especially with coding assistants, developers can use `.cursor_rules` files to define project-specific instructions (e.g., "always use these helpers") <a class="yt-timestamp" data-t="38:46:00">[38:46:00]</a>. Notepads can be used for specific prompts or PRDs to be injected on demand <a class="yt-timestamp" data-t="47:05:00">[47:05:00]</a>.
*   **Agent vs. Normal Mode:** Understanding the difference between agent modes (which can think in steps, run code, and iteratively fix errors) and normal chat modes (which provide one-shot responses) is crucial for effective use <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>.

## Navigating Product-Market Fit and User Feedback
Achieving product-market fit in AI startups involves unique considerations. This connects to [[evaluating_ai_technology_for_startups | evaluating AI technology for startups]].

### The Bias of Internal Use
A key challenge is the inherent bias of founders and early teams who use their own product <a class="yt-timestamp" data-t="53:53:00">[53:53:00]</a>. This can lead to underestimating real user problems because the internal team is accustomed to the product or actively convincing themselves problems don't exist <a class="yt-timestamp" data-t="54:01:00">[54:01:00]</a>.

### Importance of User Onboarding
Manual, "over-the-shoulder" onboarding of early users is a crucial strategy to identify real concerns and apprehensions, especially for high-pressure products like email management <a class="yt-timestamp" data-t="52:51:00">[52:51:00]</a>, <a class="yt-timestamp" data-t="53:42:00">[53:42:00]</a>. This helps in understanding the initial user experience and fixing problems before a wider launch.

### Data and Prioritization
Early data from a few users can be emotionally misleading <a class="yt-timestamp" data-t="56:47:00">[56:47:00]</a>. The solution is to gather more data from a larger pool of users (e.g., 30 instead of 2) to "zoom out" and identify patterns, segment user buckets, and prioritize truly widespread problems <a class="yt-timestamp" data-t="56:20:00">[56:20:00]</a>.

### Focusing on Core Strengths
Instead of trying to achieve feature parity with established competitors (e.g., building a full email client to match Gmail), a startup should focus on making one specific thing 10 times better for a certain type of person <a class="yt-timestamp" data-t="59:18:00">[59:18:00]</a>. This unique value proposition can drive initial adoption despite lacking other features. This is a core aspect of [[strategic_growth_and_monetization_in_ai_startups | strategic growth and monetization in AI startups]].

## The "Mushy" Problems of AI Product Development
Building AI products involves navigating problems that are not binary or easily verifiable. This relates to [[challenges_and_strategies_in_ai_evaluation | challenges and strategies in AI evaluation]].

### Beyond Binary Solutions
Unlike traditional software development where "it works or it doesn't work," many problems AI addresses are "mushy" <a class="yt-timestamp" data-t="01:01:32">[01:01:32]</a>, <a class="yt-timestamp" data-t="01:03:39">[01:03:39]</a>. They cannot be reduced to step-by-step solutions where each step is provable. This requires a different approach to product development, moving away from purely problem-solving engineering <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

### Taste, Vision, and Creativity
The success of AI products increasingly relies on "taste," "vision," "experience," and "creativity" <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>, <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. It's about creating something that makes someone *feel* a certain way <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. The product's "perspective" or "methodology" becomes a core differentiator <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.

### Embracing Messiness
The journey of building a company and product with AI is not about reaching a clear "completion state" <a class="yt-timestamp" data-t="01:04:33">[01:04:33]</a>. It requires embracing the "messiness" and the "suck of difficult decision making" <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>, <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. This often involves sacrificing certain aspects to make progress on what truly matters <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>.

## Conclusion: The Ever-Expanding Frontier of AI
The progression of AI, much like hiking a mountain with "false peaks," constantly reveals new layers of complexity and new frontiers <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>, <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>. While AI can solve clearly defined, verifiable problems, it also highlights the vast number of "squishy" problems that require human intuition, taste, and iterative learning <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>, <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.

AI tools, like Kora, can streamline mundane tasks (e.g., summarizing automated emails) to free up human attention for more meaningful interactions (e.g., focusing on emails from actual people) <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>. This suggests that AI development, particularly for startups, is less about replacing human creativity and more about enabling it and enhancing human connection <a class="yt-timestamp" data-t="01:13:27">[01:13:27]</a>.

> "Maybe Kora is the most human way to email." <a class="yt-timestamp" data-t="01:13:33">[01:13:33]</a>