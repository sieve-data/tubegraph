---
title: Integrating AI with existing frameworks
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Effectively [[integrating_ai_features_into_mobile_apps | integrating AI features into mobile apps]] or web applications often requires careful planning and a deep understanding of how AI tools interact with existing development frameworks and codebases. This article outlines best practices for leveraging AI assistants like Cursor to build and debug projects, emphasizing the importance of providing context and working within established structures.

## The Importance of Planning

Before diving into coding with AI, it's crucial to adopt a "developer mindset" and plan what you intend to build <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This approach, likened to the "measure twice, cut once strategy," ensures that you provide AI models with as much context as possible <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

*   **Visualize and Sketch**: Start by sketching your ideas, whether on paper, in Paint, or using tools like Figma <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This helps define the visual and structural blueprint of your application. An example provided involved drawing a portfolio page on an iPad and then uploading it to ChatGPT to plan the structure <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Utilize v0 for Mockups**: For visualizing potential app MVPs, [[building_highquality_web_interfaces_with_ai | v0]] is highly recommended <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. It's built using Shadcn UI, allowing for aesthetically pleasing UI designs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can feed your sketches into [[building_highquality_web_interfaces_to_ai | v0]] to generate more refined designs and then take that generated code to Cursor <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   *Starting Point*: Spending significant time in [[building_highquality_web_interfaces_to_ai | v0]] (at least 10-15 prompts) to refine your vision is beneficial before moving to code generation <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

## Setting Up Cursor with Project-Specific Rules

To optimize Cursor's output, it's essential to configure it with the specific technologies and best practices of your project.

*   **`cursor.directory`**: This website offers pre-written prompts that can be copied into your Cursor codebase <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. These prompts serve as initial instructions for Cursor, informing it about the frameworks and libraries you're using (e.g., Next.js, TypeScript, React, Tailwind) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **`.cursor_rules` File**: Create a file named `.cursor_rules` in the root of your project and paste the relevant prompt from `cursor.directory` <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This ensures that every time you prompt Cursor, it understands your codebase's foundation, preventing it from pulling outdated information <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
*   **Custom Prompts**: If your technology stack isn't listed on `cursor.directory`, you can use other AI models like Claude or ChatGPT to generate a similar `.cursor_rules` prompt tailored to your specific technologies (e.g., React and Python) <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## Tagging Documentation for Enhanced Accuracy

Providing AI models with current and accurate information is vital, especially when dealing with rapidly evolving frameworks.

*   **Official Documentation as Source of Truth**: Every technology used in development has official documentation (e.g., Next.js, Supabase) <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>. These "docs" are typically the best source of truth for how a technology works <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **Add Docs to Cursor**: Within Cursor's composer view, you can "tag" documentation by adding URLs to official docs <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This gives Cursor access to the latest information, allowing it to provide up-to-date and best-practice solutions when generating or debugging code <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Learning while Building**: For beginners, this process also serves as a learning opportunity, helping them understand the language and ecosystem of different frameworks <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

## Leveraging Other AI Models for Problem Solving

While Cursor is powerful, it can sometimes get stuck. A [[competitive_approach_to_ai_usage | competitive approach to AI usage]] involves using multiple models.

*   **Consult Other AIs**: If Cursor continuously struggles with an issue, copy the problem (including the bug, attempted solutions, and desired output) and paste it into another AI model like Claude or ChatGPT <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>. Providing this detailed context significantly improves the chances of getting a viable solution <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## AI's Role in Understanding and Extending Existing Code

AI models excel at tasks related to code explanation and adaptation, making them invaluable for working with existing frameworks.

*   **Explaining Code**: AI models can explain existing code to beginners, breaking down its flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>. This allows users to learn about complex concepts (like React components or Next.js directives) as they build <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **Adding Comments**: AI can automatically add comments to existing code, aiding in documentation, which is often a tedious task for developers <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **Duplicating Existing Functionality**: If you have existing functionality on one page that you want to adapt for another, you can copy the relevant code and ask the AI to replicate it with specific modifications. This helps in reusing and extending existing patterns within your framework <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

## Building on Starter Templates

Starting with a pre-existing codebase can significantly accelerate development, especially when working with AI. This aligns with [[building_a_business_with_ai_tools | building a business with AI tools]] by reducing setup time.

*   **Boilerplate Code**: Use starter templates that already include common functionalities like landing pages, payment integrations (e.g., Stripe), database integrations, and authentication (e.g., Google Auth, two-factor authentication) <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Accelerated Development**: By starting with such templates (readily available on platforms like GitHub for Next.js or React), you can direct Cursor to build *on top of* an already functional and complex structure, rather than starting from scratch <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>. This is particularly beneficial for challenging aspects like authentication or database setup <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.

By following these best practices, individuals can maximize the efficiency and accuracy of AI tools like Cursor when [[using_ai_models_for_practical_applications_and_startups | using AI models for practical applications and startups]] and [[using_apis_in_ai_app_development | using APIs in AI App Development]] within existing frameworks. The key is to treat AI as a co-pilot, providing it with structured context and building upon solid foundational planning.