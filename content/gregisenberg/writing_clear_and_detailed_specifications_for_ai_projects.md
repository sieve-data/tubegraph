---
title: Writing clear and detailed specifications for AI projects
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing AI applications, particularly those based on large language models (LLMs), often presents challenges due to the unpredictable nature of AI coding results <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. While tutorials might suggest AI can build an entire application from a simple prompt, the reality is that LLMs can "hallucinate," leading to numerous errors and inconsistent outcomes <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To achieve more predictable and consistent results in [[practical_examples_of_ai_project_development | AI project development]], a structured workflow centered around clear and detailed specifications is crucial <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Importance of Detailed Specifications

The most important step in streamlining AI coding is to invest significant upfront time in writing very clear and detailed specifications <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This approach aims to reduce uncertainty and lead to more consistent outcomes <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The goal is to simulate how a product team normally operates: a product manager defines the core functionality, and an engineering manager then details the architecture and individual tasks, leaving less ambiguity for implementation <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This preparation helps uncover potential issues early in the planning phase <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Workflow for Creating AI Project Specifications

A comprehensive specification for an AI coding project should include:

### 1. Project Overview and Core Functionality
Begin with a simple project overview that outlines the goal and the must-have features <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This initial outline should clearly communicate the project's objective and its essential functionalities without needing to be excessively detailed at this stage <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### 2. Proof of Concept and Documentation
Crucially, include documentation on how to implement key features, often by building small proofs of concept early on <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This involves:
*   **Researching Packages and APIs**: Use tools like ChatGPT to identify appropriate packages (e.g., `snoowrap` for Reddit data) and then consult their documentation or examples (e.g., npm documentation) to understand their usage and authentication methods <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Building Core Functionality Proofs**: Create simple scripts for critical functionalities (e.g., fetching Reddit posts or categorizing content with OpenAI's structured output) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Debugging Early**: Testing these proofs of concept early allows you to encounter and debug errors, ensuring the core functionality works before integrating it into the larger project <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. When debugging with AI, it's helpful to provide error messages and ask the AI to "think step by step" to encourage a more systematic problem-solving approach <a class="yt-timestamp" data-t="00:29:25">[00:29:25]</a>.
*   **Structuring Outputs**: When using AI for tasks like categorization, specify the desired output format to ensure consistency <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. It's also beneficial to make prompts more generic to allow for easier future modifications, such as adding new categories <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.

### 3. Current File Structure
Include the current file structure of the project <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Tools like `tree` can generate this easily <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>. This helps the AI understand the project's organization, preventing it from creating files in incorrect locations or mismanaging dependencies <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### 4. Additional Requirements and Common Prompts
Add specific requirements that AI models often miss or get wrong, such as `use client` directives in web apps, proper environment variable usage, or error handling <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. These can be categorized by project type (e.g., web app, iOS app) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

### Leveraging Stronger Models for Refinement

Once a draft specification is complete, it can be refined using a stronger AI model, like 01, to act as an "engineer manager" <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. Provide the entire draft spec and ask the model to structure the project files and identify dependencies <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>. This process generates a more detailed and architecturally sound plan, similar to what an experienced engineer would produce, defining functionalities and file structures in granular detail <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. This detailed Product Requirements Document (PRD) provides engineers with exactly what they need to build a robust product <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

## Role of Different AI Tools and Step-by-Step Building

When [[building_successful_ai_apps | building AI applications]], it's beneficial to use different AI tools for their strengths:
*   **Cursor for Functionality**: Focus Cursor on developing the core functionalities of the application <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. By providing the detailed, refined specification, you can prompt Cursor to implement tasks incrementally, feature by feature <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>. This "crawl, walk, run" approach reduces errors and makes the process more manageable than attempting to build everything at once <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.
*   **v0 for UI Refinement**: Once the functionality is largely built and stable, use v0 (or similar tools) to improve the user interface (UI) <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Since the functional code is already present, v0 can focus on styling and aesthetics without disrupting underlying logic <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. Providing specific style preferences (e.g., "black and white, dark mode, similar to Vercel") yields better UI results <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.

## Reusable Modular Prompts

The concept of reusable modular prompts is powerful for accelerating AI coding <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Standard features like user authentication or payment processing are consistent across many projects <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Developing a collection of well-tested prompts for these common functionalities allows developers to quickly integrate them into new applications, significantly speeding up the [[developing_a_minimally_viable_product_with_ai_assistance | development process]] <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.

By adopting this structured approach—starting with detailed specifications, building functionality first, refining UI later, and leveraging reusable prompts—developers can achieve a higher success rate and a more controlled AI coding experience <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. This strategy makes AI coding a more predictable and efficient process, akin to using an electric-assisted bicycle that provides a boost while still requiring effort and direction <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a>.