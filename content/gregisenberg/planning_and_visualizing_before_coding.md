---
title: Planning and visualizing before coding
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

When using AI coding tools like Cursor AI, it's crucial to adopt best practices to achieve optimal results and avoid wasting time <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The core principle for getting the best outcomes is thorough planning and visualization before writing any code <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## The "Measure Twice, Cut Once" Strategy

Before jumping into Cursor's composer to build something, it's essential to have a developer mindset and plan what you're going to build <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This strategy, likened to "measure twice, cut once," involves visualizing the desired outcome <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Key aspects of this planning phase include:
*   **Sketching and Wireframing** <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>: Create sketches of what the product should look like using tools like [[developing_a_product_roadmap_and_user_interface_design | Figma]], Paint, or even by hand on paper <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The goal is to have a clear picture in mind <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Providing Context to AI** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>: AI models perform better when given as much context as possible <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Avoid assuming the AI is smart; instead, treat it as a co-pilot where you are the boss <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **"Rubber Ducking" with AI** <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>: Use the AI as a sounding board to explain your thoughts and ideas. This process can lead to new realizations and help refine your approach, similar to explaining a problem to a fictional rubber duck in traditional programming <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

For instance, an initial product idea was sketched on an iPad for client work, which then informed discussions with ChatGPT about the project structure <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Visualizing with Vercel v0

A recommended tool for visualizing an app's Minimum Viable Product (MVP) is Vercel v0 <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

*   **Generating UI from Sketches** <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>: You can drag and drop your sketches into v0 and prompt it to build the desired UI <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This allows for an interactive refinement of the design, such as moving elements or adding sections <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Iterative Design** <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>: It's advisable to spend a significant amount of time, perhaps 10 to 15 prompts, in v0 to get the design as close as possible to your vision before moving to Cursor <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Quality UI Output** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>: Since v0 is built using Shadcn UI, it can generate high-quality [[incorporating_visual_interest_and_effects_in_ui_design | UIs]] with features like gradients or rounded edges, providing a strong starting point for Cursor <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

Starting with v0 means avoiding Cursor initially, as the first step to being good at Cursor is not to go on Cursor right away <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Setting Up Cursor for Success: `cursor.directory` and Tagging Docs

To further enhance Cursor's performance, properly configuring its environment is key.

### Using `cursor.directory` for Initial Prompts
`cursor.directory` is a website that provides pre-written prompts optimized for specific technologies (e.g., Next.js, Python) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Customizing Cursor's Understanding** <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>: By copying a relevant prompt and pasting it into a `.cursor_rules` file in the root of your project, you set up an initial prompt that Cursor reads before any other queries <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This helps Cursor understand your codebase and follow best practices for the chosen technologies, preventing it from pulling outdated information <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Creating Custom Rules** <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>: If your specific technology stack isn't listed, you can take a few existing prompts from `cursor.directory` and ask another AI model like Claude or ChatGPT to write a similar prompt tailored to your technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### Tagging Documentation
It's vital to provide Cursor with the latest and most accurate information by tagging documentation for the technologies you are using <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

*   **Adding Docs to Cursor** <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>: Within Cursor's composer, you can add documentation URLs (e.g., Next.js, Superbase) to provide the AI with up-to-date reference material <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>.
*   **Debugging and Learning** <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>: When issues arise, Cursor can leverage these tagged docs to debug problems with the most current information <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. This process also serves as a learning opportunity, as the AI's solutions help you understand how things work <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

These steps collectively provide the AI models with the necessary context, akin to an "onboarding phase" for a new employee <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

## Strategies for Overcoming Challenges and Learning

### Consulting Other AI Models
If Cursor gets stuck on a bug or issue, it can be beneficial to consult other AI models like Claude or ChatGPT <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

*   **Providing Comprehensive Context** <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>: When moving to another AI, don't just provide the bug. Include the solutions Cursor attempted that failed, the output you're currently getting, and what you're expecting <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>. This additional context increases the likelihood of a successful resolution <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.

### Using AI as a Learning and Explanatory Tool
AI models are excellent at explaining and teaching code and concepts <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

*   **Code Explanation** <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>: You can ask an AI to explain existing code, such as a project component, in simple terms for a beginner <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. This helps non-developers understand the flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
*   **Concept Clarification** <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>: If a term or concept (e.g., "use client directive") is unclear, you can ask the AI to explain it in simpler terms <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.
*   **Accelerated Learning** <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>: This iterative process of asking questions and clarifying information allows users to quickly understand patterns and concepts, expediting the learning process significantly <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. While it might take longer in the short term, it fosters self-sufficiency and a deeper understanding of the development landscape <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

### Duplicating and Leveraging Existing Functionality
When building new features, especially if they are similar to existing ones, it's efficient to duplicate and adapt <a class="yt-timestamp" data-t="00:35:23">[00:35:23]</a>.

*   **Adapting Code with a Twist** <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>: If a specific functionality works well on one page, you can copy that code or concept and ask the AI to replicate it for another page with specific modifications <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Again, providing explicit instructions on the desired changes (the "twist") is key <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. This approach reiterates the importance of giving AI models maximum context <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### [[creating_and_utilizing_templates_in_software_development | Creating and Utilizing Templates]]
For recurring projects or functionalities, using a starter kit or template can significantly speed up development <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>.

*   **Boilerplate Code** <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>: Templates can come pre-built with common features like landing pages, authentication (Google, email, two-factor), payment integrations (e.g., Stripe), database setups, and dashboards <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>.
*   **Starting Point for Serious Projects** <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>: Instead of building these complex components from scratch, you can find existing templates (e.g., on GitHub by searching "Next.js starter template") and build on top of them using Cursor <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>. This is considered the smartest way to approach serious software development <a class="yt-timestamp" data-t="00:39:59">[00:39:59]</a>.

By combining meticulous planning, leveraging AI for visualization and learning, and utilizing existing templates, users can significantly enhance their productivity and the quality of their AI-assisted coding projects.