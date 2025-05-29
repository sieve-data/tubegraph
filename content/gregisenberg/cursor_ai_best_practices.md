---
title: Cursor AI best practices
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Exploring [[Building AI Apps with Cursor | Cursor AI]] can be an amazing journey, allowing users to transform ideas into code rapidly <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its effectiveness, it's crucial to understand and implement best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These foundational strategies can save countless hours and ensure that projects are built to work <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Planning is Key
A fundamental best practice is thorough planning <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. It's not advisable to simply open the Cursor AI composer and immediately start building <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. Even when using [[The role of platforms like Cursor AI in AI development | AI]], adopting a developer mindset that prioritizes planning is essential <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

> [!NOTE] Measure Twice, Cut Once Strategy
> This approach emphasizes extensive planning before writing code. You should plan what you're going to build and how it should look <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

**Practical Planning Steps:**
*   **Sketching**: Have some sketches of your ideas, whether handwritten, drawn in Paint, or designed in Figma <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This provides a visual representation to guide the [[Techniques for increasing AI effectiveness | AI]] <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Context for AI**: When prompting [[The potential of Cursor AI for app development | AI models]], provide as much context as possible <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Avoid assuming the [[The potential of Cursor AI for app development | AI]] is inherently smart; instead, position yourself as the "boss" and the [[The potential of Cursor AI for app development | AI]] as the "co-pilot" <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Utilize V0**: V0 is highly recommended for visualizing potential apps or MVPs <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. It allows users to start with a concept, generate a visual, and then refine it through multiple prompts <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. For example, you can describe a "clean looking Marketplace website for bicycle sellers" and V0 will generate a UI <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. You can even upload sketches from your iPad to V0 to generate a more concrete visual <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
    *   V0, built with shaten UI, provides aesthetically pleasing UIs, and its generated code can be directly copied to [[Building AI Apps with Cursor | Cursor AI]] for further development <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
    *   It's beneficial to spend a significant amount of time in V0, aiming for 10-15 prompts, to get the envisioned build as close as possible to reality before moving to Cursor AI <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

## Utilizing `cursor.directory`
A critical step for [[Creating consistent AI coding results | consistent AI coding results]] is using `cursor.directory` <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>. This site provides pre-written prompts that can be copied and pasted into a `.cursorrules` file in the root of your project <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

*   **Purpose**: These rules act as an initial prompt, guiding [[The potential of Cursor AI for app development | Cursor AI]] on best practices for specific technologies (e.g., Next.js, Python, React, TypeScript, Tailwind) <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>. This helps mitigate the risk of [[The potential of Cursor AI for app development | AI models]] pulling outdated information <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.
*   **Implementation**: Create a file named `cursor.rules` in your project's root folder <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. Find prompts on `cursor.directory` relevant to your technology stack, copy them, and paste them into this file <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>. This ensures [[Building AI Apps with Cursor | Cursor AI]] understands your codebase every time you prompt it <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Custom Rules**: If your specific technologies aren't listed, you can take existing prompts from `cursor.directory` and use [[Using tools like Cursor AI Replit and Claude AI | Claude AI]] or ChatGPT to create a similar prompt tailored to your stack <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

## Tagging Documentation
Tagging documentation within [[Building AI Apps with Cursor | Cursor AI]] is vital for ensuring the [[The potential of Cursor AI for app development | AI]] uses the most up-to-date and accurate information <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>.

*   **Process**: In Cursor AI's composer view, you can add documentation URLs (e.g., Next.js, Supabase) <a class="yt-timestamp" data-t="20:37:00">[20:37:00]</a>. This allows [[The potential of Cursor AI for app development | Cursor AI]] to reference the official documentation when generating code or debugging issues <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.
*   **Benefits**:
    *   Provides the [[The potential of Cursor AI for app development | AI]] with the latest information, preventing reliance on potentially outdated scraped internet data <a class="yt-timestamp" data-t="21:05:00">[21:05:00]</a>.
    *   Facilitates debugging by allowing [[The potential of Cursor AI for app development | Cursor AI]] to use official documentation to resolve issues <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>.
    *   Helps beginners learn by allowing them to ask the [[The potential of Cursor AI for app development | AI]] to explain concepts directly from the documentation, fostering a deeper understanding of the ecosystem <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>.

## Consulting Other [[Using tools like Cursor AI Replit and Claude AI | AI Models]]
There will be instances where [[Building AI Apps with Cursor | Cursor AI]] gets stuck on a bug <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>. In such cases, it's beneficial to consult other [[Using tools like Cursor AI Replit and Claude AI | AI models]].

*   **Strategy**: Copy the issue and any solutions [[Building AI Apps with Cursor | Cursor AI]] attempted (that failed) and paste them into another [[The potential of Cursor AI for app development | AI]] like [[Using tools like Cursor AI Replit and Claude AI | Claude AI]] or ChatGPT <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>.
    *   Providing context about failed solutions is crucial <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>. This tells the new [[The potential of Cursor AI for app development | AI]] what *not* to do, leading to more effective results <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.
    *   Giving the expected output alongside the current output also enhances the effectiveness of the query <a class="yt-timestamp" data-t="27:53:00">[27:53:00]</a>.

## Leveraging [[The potential of Cursor AI for app development | AI]] for Learning and Documentation
[[The potential of Cursor AI for app development | AI]] is an excellent tool for explaining and teaching code, particularly for non-developers <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>.

*   **Code Explanation**: Ask [[The potential of Cursor AI for app development | AI]] to explain existing code, focusing on flow, logic, and overall functionality, as if to a beginner <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>. This can help demystify complex concepts like React components, hooks, or client-side rendering <a class="yt-timestamp" data-t="30:58:00">[30:58:00]</a>.
*   **Documentation**: [[The potential of Cursor AI for app development | AI]] excels at generating documentation for existing code, a task often considered tedious by developers <a class="yt-timestamp" data-t="30:30:00">[30:30:00]</a>.
*   **Continuous Learning**: By consistently asking the [[The potential of Cursor AI for app development | AI]] to explain parts of the code or concepts that are unclear, users can gradually build their understanding and recognize programming patterns <a class="yt-timestamp" data-t="32:04:00">[32:04:00]</a>. This "learning by doing" approach, even with initial struggles, leads to significant self-sustaining knowledge <a class="yt-timestamp" data-t="34:10:00">[34:10:00]</a>.

## Duplicating Functionality and Using Templates
When building, it's efficient to leverage existing code and templates.

*   **Adapting Functionality**: If you have a piece of code or functionality that works well on one page, you can copy it and ask [[The potential of Cursor AI for app development | AI]] to adapt it for a similar purpose on another page with specific modifications <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a>. This provides the [[The potential of Cursor AI for app development | AI]] with crucial context, leading to better results <a class="yt-timestamp" data-t="36:05:00">[36:05:00]</a>.
*   **Starter Kits/Templates**: For serious [[The potential of Cursor AI for app development | app development]], starting with a pre-built starter kit or template is highly recommended <a class="yt-timestamp" data-t="36:56:00">[36:56:00]</a>. These templates often include common boilerplate code such as landing pages, payment integrations (e.g., Stripe), database integrations, and authentication (e.g., Google Auth, 2FA) <a class="yt-timestamp" data-t="37:20:00">[37:20:00]</a>.
    *   Using a template means you don't have to build complex components like authentication or database setup from scratch <a class="yt-timestamp" data-t="38:36:00">[38:36:00]</a>.
    *   Many free templates are available on platforms like GitHub; find one that is highly regarded and use it as your foundation in [[Building AI Apps with Cursor | Cursor AI]] <a class="yt-timestamp" data-t="38:13:00">[38:13:00]</a>.

By implementing these best practices, users can significantly enhance their [[The potential of Cursor AI for app development | app development]] process with [[Building AI Apps with Cursor | Cursor AI]], leading to more efficient, reliable, and functional outcomes.