---
title: Best practices for using cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[Building an AI app with Cursor | Cursor AI]] offers the potential to transform an idea into code within minutes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its effectiveness and save development time, it's crucial to follow specific best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These strategies provide [[sequential_prompting_with_ai_tools | AI tools]] with the necessary context to produce accurate and working code <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Key Strategies for Optimal Results with Cursor AI

### 1. Planning and Preparation

Effective planning is the foundational step before interacting with [[Building an AI app with Cursor | Cursor AI]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Instead of immediately asking [[Using AI tools like Cursor and Claude for development | Cursor AI]] to build something, adopt a "developer mindset" by outlining what you intend to create and its desired appearance <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   **Visualize Your Project**: Sketch out your ideas using tools like [[planning_and_preparation_before_using_cursor_ai | Figma]], Paint, or even pen and paper <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Having a visual representation provides the [[sequential_prompting_with_ai_tools | AI models]] with crucial context, preventing assumptions <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This approach is likened to the "measure twice, cut once" strategy <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Utilize v0.dev**: For those who prefer not to draw manually, v0.dev is highly recommended as a starting point <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. It helps visualize your app's MVP (Minimum Viable Product) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. You can even upload sketches to v0.dev to generate an initial UI <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Since v0 is built using Shadcn UI, it produces high-quality UI designs <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. After generating a satisfactory design, you can copy its code and bring it into [[Building an AI app with Cursor | Cursor]] for further development <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Iterative Prompting**: Spend a significant amount of time, at least 10-15 prompts, refining your vision in v0 to get it as close as possible to your ideal design before moving to [[Building an AI app with Cursor | Cursor]] <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### 2. Utilizing Cursor.Directory for Initial Context

`cursor.directory` is a valuable resource offering pre-written prompts for various technologies <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Setup a `.cursor.rules` File**: Create a file named `.cursor.rules` in the root folder of your project <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. Copy the relevant prompt from `cursor.directory` based on the technologies you're using (e.g., Next.js, Python) and paste it into this file <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This file acts as an initial prompt that [[Building an AI app with Cursor | Cursor AI]] reads before any other prompts, setting the codebase up for success <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Prevent Outdated Information**: This practice helps prevent the [[sequential_prompting_with_ai_tools | AI model]] from pulling outdated information or non-best practices <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Custom Prompts**: If your specific technology stack isn't listed, you can copy existing prompts from `cursor.directory` and modify them using [[Using AI tools like Cursor and Claude for development | Claude]] or [[Using AI tools like Cursor and Claude for development | ChatGPT]] to fit your needs <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

### 3. Tagging Documentation for Up-to-Date Information

Knowing the technologies you're building with, and providing their official documentation, is crucial <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

*   **Source of Truth**: Official documentation is typically the most reliable and up-to-date source of information for any technology <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
*   **Adding Docs in Cursor**: Within [[Building an AI app with Cursor | Cursor]]'s composer view, you can add documentation links (e.g., Next.js docs, Superbase docs) <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. This gives [[Building an AI app with Cursor | Cursor]] access to the latest information, allowing it to debug issues and provide accurate solutions using the most current data <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   **Learning Opportunity**: Even for non-technical users, browsing documentation can help understand the language and ecosystem of the technologies involved <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. If something is unclear, you can ask [[Using AI tools like Cursor and Claude for development | AI]] to explain it simply <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

### 4. Consulting Other AI Models When Stuck

Sometimes, [[Building an AI app with Cursor | Cursor AI]] might get stuck on a bug or problem <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>.

*   **Cross-Platform Consultation**: If [[Building an AI app with Cursor | Cursor]] is continuously struggling, copy the issue (including the problem, attempted solutions, and expected output) and paste it into another [[sequential_prompting_with_ai_tools | AI model]] like [[Using AI tools like Cursor and Claude for development | Claude]] or even [[Using AI tools like Cursor and Claude for development | ChatGPT]] <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. Providing the context of previous failures helps the new [[sequential_prompting_with_ai_tools | AI]] find a novel solution <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>.

### 5. Leveraging AI for Code Explanation and Teaching

[[Using AI tools like Cursor and Claude for development | AI models]] are excellent for understanding and learning about code <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>.

*   **Explain Existing Code**: Ask [[Using AI tools like Cursor and Claude for development | AI]] to explain what a piece of code does, its flow, and overall logic <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>. This is particularly useful for developers who need to understand existing codebases or for explaining code to others <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.
*   **Generate Documentation**: [[Using AI tools like Cursor and Claude for development | AI]] excels at generating documentation for code, which can be a tedious task for developers <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Learn New Concepts**: When encountering unfamiliar terms or concepts within the explanation, ask the [[sequential_prompting_with_ai_tools | AI]] to clarify them in simpler terms <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. This "learn by doing" approach helps in understanding patterns and expedites the learning process <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

### 6. Duplicating and Adapting Existing Functionality

When similar functionality is needed across different parts of an application, referencing existing, working code can be highly efficient <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

*   **Provide Context**: If a feature works well on one page and you need something similar (but with a twist) on another, copy the existing code and instruct the [[sequential_prompting_with_ai_tools | AI]] to adapt it, explaining the exact modifications desired <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. The more context provided, the better the [[sequential_prompting_with_ai_tools | AI]]'s output <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### 7. Utilizing Starter Templates

For serious projects, starting with a robust boilerplate template can significantly streamline [[implementing_ai_in_app_development_processes | app development processes]] <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

*   **Pre-built Foundations**: Many templates include common functionalities like landing pages, payment integrations (e.g., Stripe), database setup, and authentication (e.g., Google Auth) <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.
*   **Time-Saving**: Building these common features from scratch can be challenging and time-consuming <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>. Starting with a template allows you to focus on the unique aspects of your project <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.
*   **Integration with Cursor**: Download a well-regarded template (e.g., from GitHub) and use it within [[Building an AI app with Cursor | Cursor]] as your starting point <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.

By implementing these best practices, users can significantly enhance their [[implementing_ai_in_app_development_processes | app development processes]] with [[Building an AI app with Cursor | Cursor AI]], leading to more efficient coding and higher quality results <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.