---
title: Design tips for nondesigners using AI tools
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

Vercel's V0 is an [[building_apps_using_ai_tools | AI assistant]] specifically designed for web development, aiming to simplify the process of creating high-quality web products using technologies like JavaScript, HTML, CSS, and modern frameworks <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. For nondesigners, V0 and similar [[tips_for_developers_using_ai_in_app_development | AI tools]] can act as a knowledgeable "super senior engineer" or designer, guiding them through the design and development process <a class="yt-timestamp" data-t="02:27:54">[02:27:54]</a>.

## General Approach to Design with AI

When approaching design with [[utilizing_ai_for_nondesigners_in_creative_projects | AI tools]], consider these two creative modes:

*   **Having an opinion**: If you have a clear vision or specific aesthetic in mind, start by providing detailed input, such as screenshots of desired designs <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Letting the AI paint**: If you're unsure what you want, provide a general idea of the functionality, and let the [[utilizing_ai_for_nondesigners_in_creative_projects | AI]] generate initial concepts <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. You can then iterate from there.

The process is often iterative, requiring multiple rounds of feedback and refinement to achieve the desired outcome <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

## Specific Design Tips for Nondesigners

### 1. Start with Screenshots for Inspiration

Using screenshots as a starting point is highly effective <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Instead of trying to describe a complex layout, provide an image of something similar to what you envision <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. This allows the AI to capture the "bones" and layout, even if you don't intend to copy the design exactly <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

*   **Inspiration Sources**: Websites like [Godly.website](https://godly.website) and Patterns.dev offer a wealth of design inspiration, from entire website layouts to specific UI patterns like pricing pages <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>, <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Leverage Existing Components**: V0, for example, is built on Shad CN UI, which provides pre-built UI patterns for common elements like mail apps, dashboards, cards, and music players <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. You can prompt the AI to use these or modify them to fit your brand <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

### 2. Leverage AI for Learning

If you're a novice in design, [[utilizing_ai_for_nondesigners_in_creative_projects | AI assistants]] can help you learn design principles and the right questions to ask <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

*   **Ask for Design Advice**: Directly ask the AI, "I am a novice at web design; I don't know what I'm doing. What can I try to make things look a little better? Any common practices or patterns?" <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Understand Terminology**: If the AI uses terms you don't know (e.g., "sans-serif font"), ask for clarification <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. The AI can explain concepts like consistent color schemes, whitespace, readable fonts, and responsive design <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.
*   **Study Good Design**: Observe how your favorite apps implement common features, like settings pages, and use those as mental models or screenshots for your prompts <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

### 3. Effective [[prompting_techniques_for_effective_use_of_ai_models | Prompting Techniques]]

The way you communicate with the AI significantly impacts the output.

*   **Use Natural Language**: Often, talking to the AI as you would to a human designer is effective ("make it have warmer grays," "the time playing bar should be longer") <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>, <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **Incorporate Technical Terms (if known)**: If you have some knowledge of web design or CSS, use specific terms like Tailwind CSS classes (e.g., "make it size four") or CSS properties (e.g., "use tabular nums") to precisely steer the AI <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>, <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.
*   **Provide Visuals**: You can upload images or paste them into the chat for the AI to use in its designs, which greatly enhances the visual output <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. High-quality images are crucial for a professional look <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Refine Incrementally**: Don't expect perfection on the first try. Iterate by asking for specific changes ("less vertical spacing," "add more realistic fake data," "make it mobile responsive") <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>, <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Describe Intent**: Instead of just saying "fix it," explain *why* something isn't working (e.g., "I can't see the table of songs because the image is so large") <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.

### 4. Beyond UI: Backend and Logic

Some [[utilizing_ai_for_nondesigners_in_creative_projects | AI tools]] like V0 can go beyond just UI, assisting with backend logic and architecture <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.

*   **Implement Functionality**: Ask the AI to add interactivity or logic to the generated UI <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. For example, implementing forms, managing subscriptions, or updating user info <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   **Database Schema and API Integration**: The AI can help design database schemas (e.g., for users and emails), suggest ORMs (like Drizzle or Prisma), and even advise on performance optimizations like using indexes for faster queries <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>, <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>, <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>. It can also fetch data from external APIs <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

## Mindset for Nondesigners

While pre-existing knowledge can accelerate the process, it's not a requirement <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.

*   **Go Slow to Go Fast**: Sometimes, taking the time to ask questions and learn about design principles from the AI will ultimately speed up your development process <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.
*   **Develop Taste**: By observing good design (e.g., on inspiration sites) and experimenting with AI, you can develop an opinion and taste for what a good product looks like <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>, <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.
*   **Embrace Augmentation, Not Replacement**: [[Impact of AI on design and web apps | AI tools]] are not replacing human work but augmenting it, providing capabilities similar to having a super senior engineer available to answer questions and offer best practices <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

Ultimately, [[building_apps_using_ai_tools | AI tools]] empower individuals to build whatever they can conceive, making it an unprecedented time for product creation <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. It's recommended to try these new [[utilizing_ai_for_nondesigners_in_creative_projects | AI tools]] and see how they can transform your approach to building applications <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.