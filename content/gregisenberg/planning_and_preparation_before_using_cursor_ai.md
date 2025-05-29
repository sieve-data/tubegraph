---
title: Planning and preparation before using cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Successfully transforming an idea into code using [[best_practices_for_using_cursor_ai | Cursor AI]] requires thoughtful planning and preparation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. By adopting best practices, users can save hours of time and establish a solid foundation for their projects <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This approach ensures that the output is more accurate and aligned with the user's vision <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## The "Measure Twice, Cut Once" Strategy

The initial and most crucial step before engaging with [[using_ai_tools_like_cursor_and_claude_for_development | Cursor AI]] is thorough planning <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It's essential to approach development with a "developer mindset," even when utilizing AI <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   **Visualize Your Project**: Before prompting [[using_ai_tools_like_cursor_and_claude_for_development | Cursor]], visualize what you intend to build <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This includes having a clear picture of its appearance.
*   **Sketching and Wireframing**: Create sketches or wireframes using tools like Figma, Paint, or even handwritten notes <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. These visuals provide crucial context to the AI model <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   One example involved drawing a web3 portfolio page on an iPad and uploading it to an AI model to ask for planning and structure advice <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **AI as a "Rubber Duck"**: Utilize AI as a "co-pilot" or a form of "rubber ducking" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Explain your thoughts and ideas to the AI; this process can lead to new realizations about the best approach <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Using v0 for Visualization**: If direct planning with design tools is challenging, start with v0. It helps visualize the potential look of your application or Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   v0 can take a simple text prompt, or even a sketch, and generate a visual representation <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a> <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
    *   It's recommended to spend significant time with v0, iterating through 10 to 15 prompts to get the design as close as possible to your vision <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    *   The generated code from v0 (often built with ShadCN UI) can then be copied and used as a starting point for [[using_ai_tools_like_cursor_and_claude_for_development | Cursor]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Delay Direct Coding**: "Step one of being good at [[building_an_ai_app_with_cursor | Cursor]] — don't go on [[building_an_ai_app_with_cursor | Cursor]]" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. The coding phase should begin only after the planning and design are clear <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This prevents extensive debugging and re-planning during coding <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

## Utilizing Cursor Directory

The `cursor.directory` website provides a critical resource for optimizing [[best_practices_for_using_cursor_ai | Cursor AI]]'s performance <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Pre-defined Prompts**: `cursor.directory` offers prompts tailored for various technologies (e.g., Next.js, Python) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. These prompts include best practices for each technology, helping to combat the AI model's tendency to pull outdated information <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **`.cursor_rules` File**: Copy the relevant prompt from `cursor.directory` and paste it into a file named `.cursor_rules` at the root of your project <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a> <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
    *   This file serves as an initial prompt that [[building_an_ai_app_with_cursor | Cursor]] reads before any other prompts, informing it about the project's codebase and desired standards <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a> <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Custom Rules**: If your specific technology stack isn't listed, you can copy existing prompts from `cursor.directory` and use other AI models (like [[using_ai_tools_like_cursor_and_claude_for_development | Claude]] or ChatGPT) to generate a customized `.cursor_rules` file based on your technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## Tagging Documentation

Providing [[using_ai_tools_like_cursor_and_claude_for_development | Cursor]] with specific documentation for the technologies you are using is another key preparation step <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

*   **Best Source of Truth**: Official documentation for any technology is typically the most up-to-date and accurate source of information <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. AI models can sometimes rely on outdated information <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.
*   **Adding Docs in Cursor**: In [[building_an_ai_app_with_cursor | Cursor]]'s composer view, you can add documentation URLs (e.g., `nextjs.org/docs`) <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
    *   By adding these "tagged docs," [[building_an_ai_app_with_cursor | Cursor]] gains access to the latest information <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Enhanced Debugging and Learning**: When facing issues, [[building_an_ai_app_with_cursor | Cursor]] can use the tagged documentation to debug problems with the most current information <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. This process also serves as a learning opportunity, helping users understand the ecosystem and terminology of the technologies <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.
*   **Context is Key**: Providing AI models with as much context as possible, including relevant documentation, aligns the AI with your objectives and helps it perform more effectively <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

## Leveraging Existing Code and Templates

Starting with pre-existing code structures can significantly expedite the development process and reduce the initial "pain" of building from scratch <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

*   **Starter Kits**: Develop or find a "starter kit" — a template project with common boilerplate code like a landing page, authentication (e.g., Google Auth), database integration, or a dashboard <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a> <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
    *   This eliminates the need to build the same foundational elements repeatedly <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>.
    *   Platforms like [[features_of_different_ai_coding_tools_like_bolt_cursor_replit_and_lovable | Replit]] are moving towards providing such templates <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>.
*   **GitHub Resources**: Search GitHub for "Next.js starter template" or "React starter template" and download highly-rated options <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.
*   **Building on Top**: Use these templates within [[building_an_ai_app_with_cursor | Cursor]] to build on top of established and functional code, rather than starting from a blank canvas <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. This is considered the "smartest way of doing things" for serious projects <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
*   **Duplicating Functionality**: If you have existing code that performs a specific function well on one page, provide that code to [[using_ai_tools_like_cursor_and_claude_for_development | Cursor]] and ask it to replicate similar functionality with modifications for another page <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

## Learning and Understanding

While using AI for coding can seem like a shortcut, these preparation steps are crucial for genuine learning and becoming a more self-sufficient developer <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. By understanding patterns and asking the AI to explain its code or concepts, users can expedite their learning process <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a> <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>. This investment in learning now will be invaluable as AI models continue to evolve exponentially <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.