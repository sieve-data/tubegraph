---
title: Planning strategies for AIdriven development
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Effective planning is crucial when using AI tools like Cursor AI to build applications, saving hours of development time and establishing a solid foundation for your projects <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. By adopting a "developer mindset" even if you're not a traditional developer, you can achieve optimal results <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The core principle is to give AI models as much context as possible, treating the AI as a co-pilot rather than the boss <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This approach follows a "measure twice, cut once" strategy <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Initial Planning and Visualization

The very first step to getting the best results from Cursor AI is extensive planning, ideally *before* you even open the Cursor composer <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### 1. Sketching and Wireframing
Begin by planning what you intend to build, including what it should look like <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This can involve:
*   **Sketches:** Use tools like Figma, Paint, or even simple pen and paper <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Utilizing AI for structure:** You can take a screenshot of your handwritten sketch and upload it to an AI like ChatGPT to ask for advice on planning its structure <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This process is akin to "rubber ducking," where explaining your thoughts to an AI can lead to realizations and better approaches <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 2. Visualizing with V0
After initial sketching, a highly recommended tool for visualizing your application or Minimum Viable Product (MVP) is V0 (v0.dev) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Generate UI:** V0 allows you to generate user interfaces based on your prompts, and you can even upload your sketches to refine them <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **Iterate:** Spend a significant amount of time (e.g., 10-15 prompts) in V0 to get the visualization as close as possible to your vision <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Export Code:** Once you have a satisfactory design, you can copy the generated code from V0 (which uses libraries like ShadCN UI) and bring it into Cursor AI, giving Cursor a strong foundation to build upon <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Preparing Cursor AI for Development

Once you have a clear plan and initial UI, you need to configure Cursor AI for optimal performance by providing it with essential context about your project.

### 3. Using `cursor.directory`
The `cursor.directory` website provides pre-written prompts, or "cursor rules," that you can copy and paste into a `.cursor-rules` file in the root of your project <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Set up best practices:** These rules act as initial prompts for Cursor, guiding it on best practices for specific technologies (e.g., Next.js, Python, React, TypeScript) <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This helps prevent the model from pulling outdated information <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Customization:** If your specific technology stack isn't listed, you can copy existing rules and use another AI model (like Claude or ChatGPT) to rewrite them for your particular technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. This process takes minimal effort but can lead to "Night and Day Results" <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### 4. Tagging Documentation
Inside Cursor, you can "tag" documentation for the technologies you are using <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   **Source of Truth:** Documentation is often the most accurate and up-to-date source of information for any given technology <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **Enhanced Debugging:** By tagging documentation (e.g., Next.js, Supabase), Cursor can reference the latest information when generating code or debugging issues, making problem-solving much easier <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   **Accelerated Learning:** For beginners, reviewing these documents helps you understand the ecosystem and "speak the language" of development faster <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

> [!INFO] Context is King
> All these preparation steps boil down to providing the AI model with as much context as possible. Think of it like onboarding a new employee – the more information you give them upfront, the more aligned and effective they will be <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

## Advanced Strategies and AI Leverage

Beyond initial setup, AI can be continuously leveraged throughout the development process for problem-solving, learning, and code efficiency.

### 5. Consulting Other AI Models
There will be instances where Cursor AI gets stuck or provides unhelpful solutions <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   **Switching AI:** If Cursor is continuously stuck, copy the issue (the bug, the problematic code, and even the solutions Cursor attempted but failed) and paste it into another AI model like Claude or even ChatGPT <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
*   **Provide full context:** Critically, include the failed solutions and expected output to help the new AI model understand what *not* to do, leading to much better results <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

### 6. Using AI for Code Explanation and Learning
AI models are exceptional at explaining and teaching code, which is invaluable for learning and maintaining a codebase <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.
*   **Explain existing code:** Ask the AI to explain existing code like a beginner, detailing its flow, logic, and overall function <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.
*   **Clarify concepts:** If a term or concept isn't clear, ask the AI to explain it in simpler terms <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **Add comments:** AI can automatically add comments to your code, which is typically a tedious but essential task for developers <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
*   **Learn by doing:** This iterative process of building, encountering issues, and using AI to understand and solve them accelerates learning <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.

> [!NOTE] Developer's Outlook
> While there's a lot of "pain" in building, especially with AI, planning saves significant headaches. For serious projects, a developer mindset that embraces planning and structured building is key <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. However, for side projects, feel free to "have fun, go one-shotting, break stuff" as it's also a valuable learning process <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

### 7. Duplicating and Referencing Existing Functionality
When you have a piece of code or functionality that works well on one page and you need something similar (but with a twist) on another, leverage existing code.
*   **Reference working code:** Copy the working code or describe its functionality and explain to the AI how you want to adapt it for the new context <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Providing this existing reference point gives the AI more context, leading to better answers <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### 8. Using Pre-Built Starter Kits/Templates
Starting with a boilerplate template can significantly streamline development, especially for common functionalities.
*   **Pre-built features:** Templates often include essential features like landing pages, payment integrations (e.g., Stripe), database setups, and authentication (e.g., Google Auth, 2-factor authentication) <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Foundation for AI:** Building on a template means you don't have to start from scratch with difficult components like authentication or database setup <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.
*   **Find resources:** You can find free starter templates on platforms like GitHub (e.g., "Next.js starter template," "React starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.

By implementing these strategies, developers and non-developers alike can significantly enhance their [[aidriven_improvements_in_codebases|AI-driven development]] process, leading to more robust and efficient applications. This disciplined approach sets you up for success as AI models continue to advance exponentially <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.