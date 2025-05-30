---
title: Building Apps with ChatGPT
videoId: oy7uMpPrGMA
---

From: [[everyinc]] <br/> 

The emergence of generative AI, particularly [[using_chatgpt_in_writing | ChatGPT]], is transforming the landscape of software development, making it possible for individuals to create custom applications tailored to their specific needs. This shift is enabling a future of "malleable software," where anyone can "mold their own tools to their needs" <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.

## The Concept of Malleable Software

Jeffrey, a researcher at Ink & Switch, an independent research lab, explores "malleable software." This concept originated from his frustration while working at a startup that constantly had to decline feature requests from teachers using their software <a class="yt-timestamp" data-t="01:31:30">[01:31:30]</a>. He envisioned a world where everyone could "craft software tools that match the workflows they want to have unique to themselves" <a class="yt-timestamp" data-t="02:04:06">[02:04:06]</a>, rather than relying on pre-made, one-size-fits-all tools <a class="yt-timestamp" data-t="02:10:06">[02:10:06]</a>.

Historically, programming has been a significant bottleneck in creating custom software, requiring extensive coding knowledge <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Generative AI offers a "shortcut" by translating "fuzzy ideas into code" <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, making it an exciting time to explore how this technology can empower individuals to make and edit their own software <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

### The "Hotel Room" Analogy

The current software-as-a-service (SaaS) model is likened to staying in a hotel, where "everyone gets the same hotel room" <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Users can customize minor aspects (like putting luggage in), but the core structure is dictated by the company <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. This limits users' agency, as they stop thinking about "what would be a better layout" because they aren't allowed to change it <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

The vision for malleable software is more akin to "everyone owning their own home" <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>, where they have the tools or a "general contractor on staff" (like AI) to make any desired changes <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. The concern with pervasive SaaS tools is that they "subtly affect the way we think" without us realizing it <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. This new paradigm is about providing users with more agency over their digital tools <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

## Generative AI's Impact on Software Development

Generative AI, especially [[using_chatgpt_in_writing | ChatGPT]], plays a pivotal role in enabling malleable software by:

*   **Lowering the Barrier to Entry**: People with little to no coding experience can now "literally build stuff in a way that they couldn't before" <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. A simple push to "just use [[using_chatgpt_in_writing | ChatGPT]]" can lead to a working chatbot in a couple of prompts <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. This immediate success motivates users to learn underlying fundamentals in a practice-connected way, unlike traditional programming education <a class="yt-timestamp" data-t="09:10:00">[09:10:10]</a>.
*   **Facilitating "Make First, Figure Out Second"**: The approach is to "make first and then figure out what I'm doing second" <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. While fundamentals are important for deep progress, they shouldn't be a barrier to getting started <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
*   **Overcoming Frustrations**: [[overcoming_the_limitations_of_chatgpt_for_effective_usage | ChatGPT]] helps mitigate frustrating moments in programming, such as debugging simple errors (e.g., a missing semicolon) <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>. This support creates a feeling of "flow" and momentum, reducing worry about getting stuck <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.
*   **Rapid Iteration**: The "superpower" of [[using_chatgpt_in_writing | ChatGPT]] is that "iterations are fast" <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. It's not about always getting the right answer immediately, but about quickly generating new alternatives <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **A "Muse," Not an "Oracle"**: It's crucial to involve [[using_chatgpt_in_writing | ChatGPT]] early in the brainstorming and development process. It acts as a "muse" that can contribute to ideas and build context, rather than an "oracle" that provides a perfect solution in one go <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   **Assisting with Product Management and Scoping**: [[using_chatgpt_in_writing | ChatGPT]] can help with more than just coding; it can aid in product management, scoping, design, and generating the right ideas to solve problems <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## Building a Podcast Guest App: A Practical Demonstration

The process of building a simple app for a podcast guest demonstrates these principles:

### 1. Defining the Goal <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>

The initial goal was to build an app for a podcast guest to "keep track of time and remember what I want to say" during a show <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### 2. Setting up the Custom GPT <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>

A custom [[using_chatgpt_in_writing | ChatGPT]] instance was configured with specific instructions:
*   Act as a "helpful AI coding assistant" <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   Follow user instructions precisely <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   Use a specific tech stack: React, TypeScript, and Tailwind <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   Generate all code in a single file for easy copy-pasting into an online coding platform like Repl.it <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.
*   Crucially, **ask the user for clarification** on under-specified ideas, fostering a conversational and collaborative development process <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   Generate a plan before writing code to ensure correctness <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

### 3. Initial App Development <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>

The initial prompt to [[using_chatgpt_in_writing | ChatGPT]] was to create an app to help a podcast guest with time tracking and notes <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. [[using_chatgpt_in_writing | ChatGPT]] responded with clarifying questions regarding time tracking (stopwatch/countdown), note management (preload/edit), and styling <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

The user specified:
*   A "digital clock plus progress bar" showing time from 9:00 a.m. to 10:30 a.m. <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   Notes could be preloaded, possibly from a Notion link (though it initially opted for a text area for copy-pasting for simplicity) <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   A "simple dark keynote presenter mode vibe" for styling <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
*   To "start simple" with no other features initially <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

The code was then generated and deployed to Repl.it, an online coding environment that allows quick setup, browser-based editing, and live running of code <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. The result was a functional app with a live clock, progress bar, and a notes section, demonstrating a high degree of complexity achieved in minutes <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

### 4. Adding Features and Overcoming Challenges <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>

*   **Saving Notes**: The first app version did not save notes when reloaded. The user asked [[using_chatgpt_in_writing | ChatGPT]], "is there some way we can save the notes... so they don't get lost when we reload?" <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. [[using_chatgpt_in_writing | ChatGPT]] suggested using local storage, a common client-side browser storage method <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>. This was implemented, and the notes persisted across reloads <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **[[idea_generation_using_chatgpt | GPT-4 Question Generation]]**: To add more utility, a new feature was proposed: a button that takes the podcast notes, sends them to [[idea_generation_using_chatgpt | GPT-4]], and displays generated questions <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
    *   **API Integration Challenges**: Integrating with the OpenAI API introduced common programming hurdles, such as ensuring correct API key handling (especially in a browser environment rather than a server) and handling potential changes in API formats <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
    *   **Iterative Debugging**: When errors occurred (e.g., `openai` not installed, API key issues), the error messages were fed back to [[using_chatgpt_in_writing | ChatGPT]] to identify and suggest fixes, demonstrating the iterative problem-solving approach <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
    *   Despite initial errors, the feature successfully generated relevant questions based on the input notes, showcasing the power of integrating AI into custom tools <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.

## The Future of Software Building

This new approach to building apps highlights several key shifts:

*   **Bespoke Apps for Specific Needs**: It enables the creation of "bespoke apps customized by AI" for "small use cases that are used by single people" <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. These apps are designed with only the "tiny features that I need," avoiding unnecessary bloat <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Faster Than Finding Existing Tools**: For many simple utilities, it's now faster to "just make the thing" with AI than to "go like try to Google which one is the best and learn how to use it" <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.
*   **Modding and Remixing**: The future will involve less starting from scratch and more "modding and remixing" existing applications <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. Users can take existing code, feed it to a custom GPT, and add new features or make tweaks <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
*   **Local-First Architecture**: Research at Ink & Switch is pioneering "local first" software architecture, aiming to make it simple for AI-generated apps to store and sync data privately with minimal code, removing the need for complex server setups <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Integrated AI Environments**: The ultimate vision is for AI-generated UIs to be constructed on the fly directly within [[using_chatgpt_in_writing | ChatGPT]] itself, potentially eliminating the need for copy-pasting into external environments like Repl.it <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. This means the AI would automatically select the best UI (text, custom app, etc.) for a given task <a class="yt-timestamp" data-t="03:07:00">[03:07:07]</a>.

This rapid, iterative, and user-driven approach to app development with [[using_chatgpt_in_writing | ChatGPT]] enables an "effortless flow" in building, making it accessible to more people and in more situations <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

***

*For more on malleable software, read Jeffrey's essay "Malleable Software in the Age of LLMs" on his personal website, jeffreyl.com <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.*