---
title: Using Cursor AI for beginners and nondevelopers
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[building_ai_apps_with_cursor | Cursor AI]] offers the exciting prospect of transforming ideas into code within minutes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its potential, especially for beginners and non-developers, understanding and applying specific best practices is crucial <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This guide outlines strategies to effectively use [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]] and other [[introduction_to_ai_tools_like_cursor_and_daily_for_app_development | AI tools]] for app development.

## [[cursor_ai_best_practices | Cursor AI Best Practices]]

### 1. Planning Before Coding

A fundamental step before interacting with [[building_ai_apps_with_cursor | Cursor AI]] is thorough [[planning_and_preparing_before_coding_with_cursor_ai | planning]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Adopt a "developer mindset" by outlining what you intend to build and how it should look <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

> [!TIP] Measure Twice, Cut Once <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>
> Create sketches of your user interface (UI) using tools like Figma, Paint, or even a pen and paper <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This visualization provides essential context when prompting AI models <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

When using AI, you are the boss, and the AI is your co-pilot; avoid assuming the AI is smart or making it the decision-maker <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. For example, a hand-drawn sketch of a web3 portfolio page was used as a starting point, uploaded to [[efficient_use_ai_tools_like_chatgpt_and_cursor_ai | ChatGPT]] (before [[building_ai_apps_with_cursor | Cursor]] or Claude existed) to ask for planning and structure advice <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This process is akin to "rubber ducking" in programming, where explaining your thoughts leads to realizations <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

#### Utilizing V0 for Visualization
For [[developing_user_interfaces_with_ai_tools | user interface development]], [[comparison_with_cursor_ai_and_v0 | V0]] is highly recommended for visualizing your app's potential MVP <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. You can prompt [[comparison_with_cursor_ai_and_v0 | V0]] to generate UI concepts, such as a "clean looking Marketplace website for bicycle sellers" <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Since [[comparison_with_cursor_ai_and_v0 | V0]] is built with ShadCN UI, it produces aesthetically pleasing UIs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

> [!INFO] Workflow Suggestion <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
> 1.  Draw your idea (Figma, iPad, paper).
> 2.  Take a picture or screenshot.
> 3.  Place it into [[comparison_with_cursor_ai_and_v0 | V0]].
> 4.  Refine with 10-15 prompts in [[comparison_with_cursor_ai_and_v0 | V0]] to get as close as possible to your vision <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
> 5.  Only *then* take the generated code from [[comparison_with_cursor_ai_and_v0 | V0]] over to [[building_ai_apps_with_cursor | Cursor]] or another AI model <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

This approach ensures you have a clear plan before generating code, saving significant time and effort <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### 2. Using Cursor.directory for Initial Prompts

`cursor.directory` is a valuable resource that provides pre-written prompts optimized for various technologies <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. These prompts serve as the initial context [[building_ai_apps_with_cursor | Cursor]] reads before you even start prompting it <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

To use it:
1.  Go to `cursor.directory` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Search for the technologies you are using (e.g., Next.js, Python) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
3.  Copy the relevant prompt, which defines [[building_ai_apps_with_cursor | Cursor]] as an expert in those technologies and outlines best practices <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
4.  Create a new file named `.cursor_rules` in the root of your project <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
5.  Paste the copied prompt into the `.cursor_rules` file and save it <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

This setup ensures that every time you prompt [[building_ai_apps_with_cursor | Cursor]], it understands the foundational technologies of your codebase, leading to more accurate and up-to-date results <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. It helps prevent the model from pulling outdated information <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

> [!NOTE] Customizing Prompts <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>
> If your specific technology stack isn't listed on `cursor.directory`, you can copy a couple of existing prompts, take them to [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Claude]] or [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | ChatGPT]], and ask the AI to generate a similar prompt for your desired technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. You can even specify versions or preferred languages (e.g., JavaScript instead of TypeScript) <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

### 3. Asking Other AI Models When Stuck

There will be instances where [[building_ai_apps_with_cursor | Cursor]] gets stuck on a bug <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. When this happens, it's beneficial to consult other AI models like [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Claude]], [[comparison_with_cursor_ai_and_v0 | V0]], or even [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | ChatGPT]] <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

> [!IMPORTANT] Enhance Your Prompt <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>
> Don't just copy-paste the bug. Provide the new AI model with:
> *   The bug or issue you're facing <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
> *   The solutions [[building_ai_apps_with_cursor | Cursor]] (or the previous AI) attempted but failed <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
> *   The output you're currently getting versus your expected output <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
> This added context (as highlighted in [[enhancing_cursor_ai_prompts_with_context_and_tagging | Enhancing Cursor AI Prompts with Context and Tagging]]) significantly increases the chances of getting a successful resolution <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.

### 4. Leveraging AI to Explain and Teach Code

AI models are excellent for explaining existing code and teaching programming concepts <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>. This is particularly useful for beginners to understand what the code does, its flow logic, and overall functionality <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.

> [!NOTE] Tagging Documentation <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>
> Within [[building_ai_apps_with_cursor | Cursor]]'s composer view, you can "tag docs" by adding URLs of relevant technology documentation (e.g., Next.js, Superbase) <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This gives [[building_ai_apps_with_cursor | Cursor]] access to the latest and most accurate information directly from the source, improving its ability to answer questions and debug issues <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

If something in the AI's explanation doesn't make sense, copy that specific part and ask the AI to explain it in simpler terms <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. This iterative questioning helps you grasp complex concepts and build your understanding of programming patterns <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. While it might take a bit longer in the short term, this learning process fosters self-sufficiency and quicker development in the long run <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

AI is also highly effective at writing documentation for existing code <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.

### 5. Utilizing Existing Code and Templates

When building, especially for serious projects, it's efficient to leverage existing code or templates <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.

*   **Duplicating Functionality**: If you have existing functionality on one page that works well and you need something similar (with a twist) on another page, reference the working code <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>. Provide the AI with the existing code and explain exactly what changes or adaptations you need <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Starter Kits/Boilerplate Code**: Find or create templates that include common boilerplate features like landing pages, authentication (e.g., Google Auth, email, 2FA), database integration, and dashboards <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
    *   Many free templates are available on GitHub (e.g., "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.
    *   By starting with a robust template, you can focus on building unique features rather than setting up complex foundations like authentication or database connections from scratch <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.

This strategy allows [[building_ai_apps_with_cursor | Cursor]] to shine as it builds on top of an existing, well-structured foundation <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Embracing the Developer Mindset

For non-developers using AI to build, it's essential to embrace the "pain" of development <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. There will be moments of getting stuck, breaking things, and needing to debug <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This learning process, where you do, it breaks, you fix, and then you learn, is crucial <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

The overall goal is to give AI models as much context as possible, effectively "onboarding" them like a new employee <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. By [[enhancing_cursor_ai_prompts_with_context_and_tagging | planning]], setting up `.cursor_rules`, tagging documentation, and understanding when to consult other AIs, you significantly improve the quality of the outputs you receive from [[building_ai_apps_with_cursor | Cursor]] <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. Investing time now in learning these practices will prepare you for a future where AI models are even more advanced <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.