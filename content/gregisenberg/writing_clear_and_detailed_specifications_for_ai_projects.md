---
title: Writing clear and detailed specifications for AI projects
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing with large language models (LLMs) often appears straightforward in tutorials, suggesting one can simply prompt an AI to build an entire application <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. However, in reality, results can be unpredictable, with frequent errors and "hallucinations" <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. To achieve more consistent and predictable outcomes in AI coding, it's crucial to adopt a structured workflow that emphasizes upfront planning and detailed specifications <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## The Importance of Detailed Specifications

The primary goal of a structured AI coding workflow is to reduce uncertainty and improve the consistency of AI-generated code <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. While many emphasize [[planning_before_using_ai_tools | planning upfront]], the specifics of *how* to write a detailed specification for AI communication are often overlooked <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This disciplined approach is essential for developers transitioning from casual AI coding to becoming an "AI coder" <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

By spending significant time upfront on detailed specs, much of the uncertainty in the development process is uncovered early on <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. This process aims to simulate a traditional product team's workflow, where a Product Manager (PM) writes core functionality specs, which are then detailed by an Engineering Manager into individual tickets or architecture plans, leaving minimal ambiguity for engineers <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This approach makes engineers "light up" because they receive exactly what they need to build a "super tight" and valuable end product <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

## Key Components of a Detailed Specification

A robust specification for an AI project should include several core elements:

### 1. Project Overview
Start with a simple, clear overview that defines the project's goal <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. For example, building a Reddit analytics platform where users can view subreddit analytics, top content, and category breakdown <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.

### 2. Core Functionality
Break down the "must-have" features, similar to how a Product Manager would outline them <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. It's okay to keep this part open-ended initially, focusing on clear communication of the project's goals <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>. For the Reddit analytics platform, core functionalities would include:
*   Displaying a list of available subreddits and allowing new ones to be added <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   Building a subreddit page with "top posts" and "analysis" tabs <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
*   Fetching Reddit post data and categorizing it into different themes <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.

### 3. Including Documentation and Proof of Concept
Instead of just linking to external documentation, it's beneficial to build small proof-of-concept scripts for core functionalities and include them directly in the spec <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This ensures that the AI understands the exact implementation details.
*   **Researching Packages:** Use tools like ChatGPT to identify appropriate packages (e.g., `snoowrap` for Reddit data in Next.js) <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Testing Core Logic:** Create simple scripts to test key features, such as fetching Reddit posts <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a> or using OpenAI's structured output for categorization <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>.
*   **Debugging Early:** These proof-of-concept steps are crucial for catching errors early <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>. Debugging is a natural part of the process, and one effective prompting technique for AI is to instruct it to "let's think step by step" to break down complex problems into smaller, manageable pieces, leading to better results <a class="yt-timestamp" data-t="29:25:00">[29:25:00]</a>.
*   **Documenting Expected Output:** For AI categorization tasks, clearly define the desired JSON output format <a class="yt-timestamp" data-t="21:40:00">[21:40:00]</a>, but make the prompt generic enough not to be tied to specific categories for future flexibility <a class="yt-timestamp" data-t="25:52:00">[25:52:00]</a>.

### 4. Current File Structure
Provide the AI with the project's current file structure, especially important for tools like Cursor, which can struggle to correctly place files and manage dependencies <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. Tools like `tree` can help generate this structure <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>.

### 5. Additional Requirements and Common Pitfalls
Include specific instructions tailored to the project type (e.g., web app, iOS app). These often address common mistakes or best practices the AI might miss:
*   Using `use client` directives in web apps <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
*   Correct file placement and dependency management <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
*   Utilizing environment variables for credentials <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.
*   Ensuring proper API call syntax and error handling <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.

## Leveraging AI for Spec Generation

Once a draft spec is created, a more powerful model like the 01 model can be used to act as an "engineer manager" to fill in the remaining details <a class="yt-timestamp" data-t="35:40:00">[35:40:00]</a>.
*   **Generate File Structure:** Prompt the model to propose a final project structure and identify dependencies <a class="yt-timestamp" data-t="36:14:00">[36:14:00]</a>.
*   **Refine PRD:** Then, instruct it to add all the details of the original Product Requirements Document (PRD), including variables, file structures, and additional requirements, without generating actual code <a class="yt-timestamp" data-t="37:29:00">[37:29:00]</a>. This results in a highly detailed documentation that leaves much less ambiguity for later stages <a class="yt-timestamp" data-t="38:31:00">[03:31:00]</a>.

## Building Functionality First, UI Later

A recommended workflow is to prioritize building core functionality using tools like Cursor first, and only then moving to UI refinement with tools like Vercel's v0 <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. Many developers do the opposite, starting with wireframes in v0, but this can lead to more difficulties in integrating functionality later <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>. By building functionality first, the project's core is stable, making UI adjustments more predictable and easier <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>, <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.

To guide the AI in UI design, provide specific style preferences or examples, such as "similar to Vercel" or "black and white, dark mode" <a class="yt-timestamp" data-t="46:41:00">[46:41:00]</a>. This prevents the AI from interpreting "look better" in unexpected ways <a class="yt-timestamp" data-t="47:00:00">[47:00:00]</a>. Improving prompting for AI interface design can also involve studying design principles from books to provide the AI with a more sophisticated vocabulary for design <a class="yt-timestamp" data-t="47:21:00">[47:21:00]</a>.

## Reusable Modular Prompts

For common functionalities like user authentication or payment systems, creating [[designing_and_optimizing_ai_tasks_and_agents | reusable, modular prompts]] can significantly speed up development <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. These prompts act as self-contained documentation that the AI can use to implement standard features consistently across projects <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. While Cursor offers directories for "rules," the most impactful reusable components are often found in well-crafted prompts that define standard functionalities <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. This concept could potentially lead to community-shared aggregators of such prompts, enabling developers to quickly integrate complex features <a class="yt-timestamp" data-t="55:12:00">[55:12:00]</a>.

## Conclusion

This structured workflow — emphasizing detailed upfront specification, building functionality before UI, and leveraging reusable prompts — transforms AI coding from an unpredictable guessing game into a more reliable and efficient development process <a class="yt-timestamp" data-t="55:57:00">[55:57:00]</a>. It manages expectations, making AI coding feel less "hard" compared to traditional development, and enables non-coders to become "AI coders" by effectively lowering the barrier to creation <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>. This approach turns AI into an "electric-assisted bicycle" for development, providing a boost while still requiring the user to "pedal the wheels" of structured thought and planning <a class="yt-timestamp" data-t="57:41:00">[57:41:00]</a>.