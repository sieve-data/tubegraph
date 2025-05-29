---
title: Best practices for using Cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[using_cursor_ai_and_replit_for_app_development | Cursor AI]] has emerged as a powerful tool for transforming ideas into code rapidly <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its effectiveness and save development time, it's crucial to adopt specific best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These practices focus on providing ample context to the AI, setting up the development environment correctly, and leveraging AI for learning and debugging <a class="yt-timestamp" data-t="02:49:51">[02:49:51]</a>.

## 1. Plan Thoroughly Before Coding

One of the most critical steps to getting the best results from [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] is thorough planning <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. This approach is likened to the "measure twice, cut once" strategy <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

> "You don't want to assume it's smart and you don't want to make the AI the boss. You're the boss, the AI is the co-pilot." <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>

*   **Adopt a Developer Mindset**: Even if you're not a seasoned developer, approach your project with a planning mindset <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   **Visualize Your Idea**: Sketch out what you intend to build. Tools like Figma or even simple programs like Paint, or a handwritten drawing, can be incredibly effective <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Having a visual reference provides essential context when prompting AI models <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Utilize [[tools_for_ai_code_development_cursor_and_v0 | V0]] for Prototyping**: Before jumping into [[using_cursor_ai_and_replit_for_app_development | Cursor AI]], use [[tools_for_ai_code_development_cursor_and_v0 | V0]] to visualize your potential app or MVP <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. [[tools_for_ai_code_development_cursor_and_v0 | V0]] allows you to iterate on design and functionality, getting as close as possible to your vision through 10-15 prompts <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>. It's built using Shadcn UI, allowing for nice-looking UIs <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. You can even drag and drop a sketch into [[tools_for_ai_code_development_cursor_and_v0 | V0]] to kickstart the visual process <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
*   **"Rubber Ducking" with AI**: Use the AI as a sounding board, similar to "rubber ducking" in programming, where you explain your thoughts to clarify your own ideas and gain new realizations <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

## 2. Leverage Cursor.Directory for Contextual Prompts

To set up your [[using_cursor_ai_agent_for_app_development | Cursor AI]] codebase for success, utilize `cursor.directory` <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

*   **Initial Prompting**: This site provides pre-defined prompts that act as an initial context for [[using_cursor_ai_and_replit_for_app_development | Cursor AI]], helping it understand your project's technology stack (e.g., Next.js, Python) <a class="yt-timestamp" data-t="11:33:00">[11:33:33]</a>.
*   **Combat Outdated Information**: AI models can sometimes provide outdated information <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>. Using `cursor.directory` ensures [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] follows best practices for your chosen technologies <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
*   **Create `.cursor_rules` File**: Copy the relevant prompt from `cursor.directory` and paste it into a file named `.cursor_rules` in the root of your project <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. This tells [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] what your codebase is based on every time you prompt it <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Customize Prompts**: If your specific technology stack isn't listed, you can copy existing prompts and ask another AI model like [[using_ai_models_like_claude_and_v0_with_cursor_ai | Claude]] or ChatGPT to modify them to fit your technologies <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

## 3. Tag Documentation for Up-to-Date Context

Knowing the technologies you're building with and providing their documentation to [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] is crucial for accuracy and debugging <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.

*   **Docs as Source of Truth**: The official documentation for any technology is typically the most reliable source of information <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>.
*   **Add Docs to [[using_cursor_ai_and_replit_for_app_development | Cursor AI]]**: In [[using_cursor_ai_and_replit_for_app_development | Cursor AI]]'s composer, you can add external documentation URLs (e.g., Next.js, Superbase) <a class="yt-timestamp" data-t="20:31:00">[20:31:00]</a>. This gives [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] access to the latest and greatest information for setting up and debugging <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>.
*   **Learn While Building**: Use the documentation as a learning moment. If something is unclear, ask [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] to explain it <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>. This iterative process helps beginners understand the ecosystem and "speak the language" of development <a class="yt-timestamp" data-t="23:57:00">[23:57:00]</a>.

## 4. Consult Other AI Models When Stuck

Sometimes, [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] might get stuck on a bug <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>. In such cases, consulting other AI models can yield better results.

*   **Provide Full Context**: When moving to another AI model (e.g., [[using_ai_models_like_claude_and_v0_with_cursor_ai | Claude]], ChatGPT), don't just copy the bug <a class="yt-timestamp" data-t="27:11:00">[27:11:00]</a>. Include:
    *   The bug itself <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>.
    *   The solutions [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] tried that failed <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>.
    *   The output you're getting and what you're expecting <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a>.
*   **Different Models, Different Results**: Even if an AI uses the same underlying model, copy-pasting the issue to a different platform like [[using_ai_models_like_claude_and_v0_with_cursor_ai | Claude]] can sometimes resolve the problem <a class="yt-timestamp" data-t="26:47:00">[26:47:00]</a>.

## 5. Leverage AI for Code Explanation and Learning

AI models, especially [[using_cursor_ai_and_replit_for_app_development | Cursor AI]] and [[using_ai_models_like_claude_and_v0_with_cursor_ai | Claude]], excel at explaining and teaching code concepts <a class="yt-timestamp" data-t="32:47:00">[32:47:00]</a>.

*   **Explain Existing Code**: Ask the AI to explain existing code, making it easier to open-source or explain to others <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>. This is particularly useful for writing documentation, a task often disliked by developers <a class="yt-timestamp" data-t="30:30:00">[30:30:00]</a>.
*   **Interactive Learning**: If a part of the explanation doesn't make sense, copy that specific part and ask the AI for a more detailed explanation <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>. This interactive approach helps in understanding patterns and concepts over time <a class="yt-timestamp" data-t="32:04:00">[32:04:00]</a>.
*   **Long-Term Gains**: While it might take a bit longer initially, this learning process leads to greater self-sufficiency and quicker building in the long run <a class="yt-timestamp" data-t="33:10:00">[33:10:00]</a>. Investing time now prepares you for future, more advanced AI models <a class="yt-timestamp" data-t="33:54:00">[33:54:00]</a>.

## 6. Utilize Templates and Duplicate Functionality

Efficiency in development can be significantly improved by leveraging existing structures and patterns.

*   **Add Comments to Code**: Use AI to automatically add comments to your code, improving readability and maintainability <a class="yt-timestamp" data-t="35:11:00">[35:11:00]</a>.
*   **Duplicate and Adapt Functionality**: If you have existing functionality on one page that needs to be adapted for another, copy that code and instruct the AI to modify it with the desired changes <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a>. The more context you provide about the existing code and the desired changes, the better the output <a class="yt-timestamp" data-t="36:05:00">[36:05:00]</a>.
*   **Start with Boilerplate Templates**: For serious projects, begin with a starter template that includes common boilerplate code such as a landing page, authentication (Google Auth, email, 2FA), payment integration (Stripe), database integration, and a dashboard <a class="yt-timestamp" data-t="36:42:00">[36:42:00]</a>. Many free templates are available on platforms like GitHub (e.g., search "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="38:13:00">[38:13:00]</a>. This significantly speeds up development, especially for complex features like authentication <a class="yt-timestamp" data-t="38:36:00">[38:36:00]</a>.