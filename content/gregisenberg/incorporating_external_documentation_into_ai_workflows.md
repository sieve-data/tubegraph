---
title: Incorporating external documentation into AI workflows
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Optimizing the use of AI tools like Cursor AI involves more than just prompting; it requires strategic preparation and the integration of relevant external documentation. This approach ensures the AI is well-informed, leading to more accurate and efficient outputs <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. The core principle is to provide the AI with as much context as possible, treating it as a co-pilot rather than the sole decision-maker <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>, <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>, <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>, <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>, <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>, <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>, <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.

## 1. Plan Before You Code

Before even touching an AI coding tool, it's crucial to adopt a developer mindset and plan what you intend to build <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. This "measure twice, cut once" strategy saves significant time and prevents headaches later on <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>, <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.

### Visualize Your Application

*   **Sketching**: Start with hand-drawn sketches, or use tools like Paint or Figma, to create a visual representation of your idea <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>, <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. The goal is to have a clear picture in mind before prompting the AI <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Utilize v0**: For more refined mockups, use tools like v0. This platform helps visualize your potential app's Minimum Viable Product (MVP) and can generate code built with UI libraries like Shadcn UI, resulting in aesthetically pleasing interfaces <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>, <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. You can even upload your sketches to v0 for further refinement <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>, <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.
*   **Iterate in v0**: Spend ample time (e.g., 10-15 prompts) in v0 to get the app as close as possible to your vision before moving to Cursor AI <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>, <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.
*   **Transfer to Cursor AI**: Once you have a satisfactory visual and initial code from v0, copy that code and bring it into Cursor AI. This provides Cursor AI with a strong foundation to build upon <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>, <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>, <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

## 2. Configure Cursor AI with Project-Specific Rules

Cursor AI can be further optimized by providing it with specific rules and best practices related to your project's technology stack.

### Use `cursor.directory`

*   **Purpose**: `cursor.directory` is a valuable resource offering pre-written prompts or "rules" that guide Cursor AI's behavior based on common technologies <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   **Implementation**: Create a new file named `.cursor_rules` in the root of your project directory <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>, <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. Search `cursor.directory` for your specific technologies (e.g., Next.js, Python), copy the relevant prompt, and paste it into this file <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>, <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.
*   **Benefit**: This file acts as an initial prompt, ensuring Cursor AI understands the context of your codebase and adheres to current best practices, preventing the use of outdated information <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>, <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Customization**: If your specific technologies aren't listed, you can copy an existing rule, then use another AI model (like Claude or ChatGPT) to modify it for your unique stack, ensuring it follows a similar structure and flow <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.

## 3. Tag Relevant Documentation within Cursor AI

Beyond general rules, directly linking official documentation within Cursor AI enhances its ability to provide accurate and up-to-date solutions.

*   **Process**: In Cursor AI's composer view, you can "tag" documentation by clicking `+` (add), then `docs`, and finally `add new doc` <a class="yt-timestamp" data-t="20:31:00">[20:31:00]</a>, <a class="yt-timestamp" data-t="20:37:00">[20:37:00]</a>. Paste the URL of the official documentation (e.g., `nextjs.org` or `supabase.com/docs`) and give it a name <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>, <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>.
*   **Advantages**:
    *   **Latest Information**: AI models may have outdated information from their training data <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>. Tagging docs ensures Cursor AI uses the most current and authoritative source for information <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>, <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>.
    *   **Accurate Debugging**: When encountering bugs, Cursor AI can debug issues using the precise, up-to-date information from the tagged documentation, making problem-solving easier <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>.
    *   **Learning Aid**: This feature is especially beneficial for beginners. By exposing yourself to official documentation and having the AI explain concepts, you can quickly grasp the language and ecosystem of different frameworks and platforms like Next.js or Supabase <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>, <a class="yt-timestamp" data-t="24:01:00">[24:01:00]</a>.

## 4. Consult Other AI Models When Stuck

Sometimes, Cursor AI might get stuck on a particular bug or issue.

*   **Cross-Pollination**: If Cursor AI is continuously struggling, copy the problem, including the bug details and any failed solutions it attempted, and paste it into another AI model like Claude or ChatGPT <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>, <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>.
*   **Provide Full Context**: It's crucial not just to copy the bug, but also to tell the new AI what solutions were tried and failed, what the current output is, and what you expect. This detailed context significantly improves the chances of getting a useful solution <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>, <a class="yt-timestamp" data-t="27:48:00">[27:48:00]</a>.

## 5. Leverage AI for Code Understanding and Reusability

AI is excellent at explaining and adapting existing code, which is a powerful way to integrate documentation into your workflow.

*   **Code Explanation and Teaching**: Use AI to explain existing code, especially for complex components or unfamiliar patterns <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>. Ask it to explain the flow, logic, and overall functionality like you're a beginner <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>. If a concept is unclear (e.g., `use client` directive in Next.js), ask for further simplification <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>. This iterative process accelerates learning and helps you understand code patterns <a class="yt-timestamp" data-t="32:04:00">[32:04:00]</a>.
*   **Automate Documentation**: AI can automatically add comments to your code, which is a traditionally tedious but essential task for developers <a class="yt-timestamp" data-t="30:30:00">[30:30:00]</a>, <a class="yt-timestamp" data-t="31:11:00">[31:11:11]</a>, <a class="yt-timestamp" data-t="35:11:00">[35:11:00]</a>.
*   **Duplicate and Adapt Functionality**: If you have existing code that performs a specific function well on one page and need similar functionality elsewhere with a slight modification, copy the existing code. Then, prompt the AI by explaining what the existing code does and precisely how you want it adapted for the new context <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>, <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. This provides strong context for the AI to build upon.

## 6. Start with Boilerplate Templates

For serious development projects, beginning with a robust starter template can significantly streamline the process.

*   **Pre-built Foundations**: Use templates that already include common functionalities like landing pages, payment integrations (e.g., Stripe), database setup, authentication (e.g., Google Auth, email login, 2FA), and dashboards <a class="yt-timestamp" data-t="36:35:00">[36:35:00]</a>, <a class="yt-timestamp" data-t="37:12:00">[37:12:00]</a>.
*   **Leverage Existing Work**: Developers often repeat setup tasks for different projects. Creating your own "starter kit" or finding well-regarded open-source templates (e.g., Next.js starter templates on GitHub) allows you to build on a solid, pre-documented foundation <a class="yt-timestamp" data-t="37:38:00">[37:38:00]</a>, <a class="yt-timestamp" data-t="38:11:00">[38:11:00]</a>.
*   **Focus on Core Logic**: By starting with a template, complex integrations like authentication and database setup are already handled, freeing you to focus on the unique aspects of your application <a class="yt-timestamp" data-t="38:32:00">[38:32:00]</a>.

By diligently planning, setting up environmental rules, integrating external documentation, leveraging multiple AI tools, and building on existing templates, you can significantly enhance your [[Building apps with AI tools | AI-powered application development]] workflow, making it more efficient and reliable.