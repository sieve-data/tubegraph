---
title: Using frameworks and tagging docs for efficient coding
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Using AI tools like Cursor AI to transform ideas into code rapidly is a powerful concept <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. However, to achieve the best results and save significant time, it's crucial to adopt specific best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This guide outlines key strategies for optimizing your [[ai_coding_workflow_optimization | AI coding workflow]], focusing on planning, leveraging documentation, and utilizing existing frameworks.

## The Importance of Planning ("Measure Twice, Cut Once")

Effective planning is the foundational step when using AI coding tools like Cursor AI <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Even when using AI, it's vital to adopt a developer mindset, sketching out what you intend to build and how it should look <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

> [!NOTE] Provide Context to the AI
> When prompting AI models, give as much context as possible <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Don't assume the AI is fully intelligent; you are the boss, and the AI is your co-pilot <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Planning Tools and Techniques
*   **Visual Sketching:** Start with visual aids. This can include:
    *   Figma <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
    *   Paint <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
    *   Handwritten sketches <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>
    *   Drawing on an iPad <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
    Even a simple drawing can be used to plan the structure, like a portfolio page for a web3 client <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **"Rubber Ducking" with AI:** Engage the AI as a sounding board, similar to the "rubber ducking" technique in programming <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. By explaining your thoughts, you can gain new realizations about your approach <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Utilizing v0 for Visualization:** Use tools like v0 to visualize your potential app or Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. v0 is particularly useful because it's built with "shaten UI," allowing for aesthetically pleasing UI designs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   You can input simple prompts, like "build a clean-looking marketplace website for bicycle sellers" <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   More advanced use involves dragging and dropping a screenshot of your sketch into v0 and prompting it to refine the design <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. For example, converting an iPad sketch of a web3 portfolio into a detailed v0 output <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   Spend a significant amount of time, perhaps 10 to 15 prompts, in v0 to get your vision as close as possible before moving to Cursor AI <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

> [!CAUTION] Don't Jump Straight to Coding
> Do not jump straight to Cursor AI or Claude without prior planning <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. The initial step for being proficient with Cursor AI is not to go on Cursor AI at all <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Utilizing `cursor.directory` for Enhanced Context

The `cursor.directory` website provides pre-written prompts that can be copied and pasted into your Cursor AI codebase <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. These prompts act as an initial instruction set for Cursor AI before you begin direct prompting <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Benefits of `cursor.directory`
*   **Sets Context:** It informs Cursor AI about the technologies you are using (e.g., Next.js, TypeScript, React, Tailwind) and best practices to follow <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Prevents Outdated Information:** AI models can sometimes pull outdated information <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. Using `cursor.directory` helps set your Cursor AI codebase for success with current guidelines <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Implementation Steps
1.  Visit `cursor.directory` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Search for the technologies you are using (e.g., "nextjs") <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
3.  Copy the relevant prompt <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
4.  In your Cursor AI project, create a new file named `.cursor_rules` in the root folder <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
5.  Paste the copied text into `.cursor_rules` and save it <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

Now, every time you prompt Cursor AI, it will consider the rules defined in this file, leading to significantly better results <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

### Customizing `.cursor_rules`
If your specific set of technologies isn't listed on `cursor.directory`, you can:
1.  Copy a couple of existing prompts from the site <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
2.  Use another AI model like Claude or GPT to write a similar prompt tailored to your technologies <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. For example, asking for a prompt for React and Python while maintaining a concise flow <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
3.  Manually edit the generated prompt to specify versions (e.g., React 17) or frameworks (e.g., JavaScript instead of TypeScript) <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

## Tagging Documentation (Docs) within Cursor AI

Integrating official documentation directly into Cursor AI provides the most up-to-date and authoritative information for the AI model <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

### Benefits of Tagging Docs
*   **Source of Truth:** Documentation is typically the best source of truth for any technology <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **Latest Information:** AI models' knowledge cut-offs can lead to outdated information <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. Tagging docs ensures Cursor AI uses the latest data <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Improved Debugging:** When encountering bugs, Cursor AI can debug issues with the most current information <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

### Implementation Steps
1.  In Cursor AI's Composer view, click "add" and then "docs" <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
2.  Click "add new Doc" <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>.
3.  Paste the URL of the documentation (e.g., `nextjs.org`) <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.
4.  Name the documentation (e.g., "Next.js Docs") and confirm <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.

Now, you can ask Cursor AI questions, and it will reference the linked documentation. For example, asking "how can I build a simple page that says hello world" will prompt Cursor AI to read relevant pages like "getting started" from the Next.js docs <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.

> [!TIP] Learn as You Build
> Even if you're non-technical, take time to browse documentation. If something doesn't make sense, screenshot it and ask the AI to explain it in simpler terms (e.g., "explain to me like I'm 5") <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. This approach of "doing and learning" helps you grasp the ecosystem and speak the language of development <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Leveraging AI for Learning and Code Explanation

Beyond generating code, AI models are excellent teachers and explainers of code <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>.

### How AI Can Teach
*   **Explaining Existing Code:** You can ask an AI to explain existing code, describing its flow, logic, and overall function <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. For instance, explaining a React component like a "blog card" that handles hover effects <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.
*   **Understanding Concepts:** If a part of the explanation is unclear (e.g., "use client" directive), you can copy that specific phrase and ask the AI for a more detailed explanation <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. This iterative process helps build understanding <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Adding Comments to Code:** AI can also generate comments for your code, making it easier to understand and document <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.

This learning approach, while potentially taking longer in the short term, leads to greater self-sustainability, deeper understanding, and faster building in the long term <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. It prepares developers for future advancements in AI models <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.

## Strategies for Overcoming AI Roadblocks

Sometimes, Cursor AI may get stuck on a bug or issue <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

### Consulting Other AI Models
If Cursor AI continuously struggles, try consulting another AI model like Claude or even ChatGPT <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
*   **Provide Full Context:** When reporting a bug to another AI, don't just copy the error <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. Include:
    *   The bug description <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
    *   The solutions Cursor AI previously attempted but failed <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
    *   The actual output you are receiving <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
    *   Your expected output <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
This comprehensive context will significantly improve the chances of getting a solution <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.

## Duplicating Functionality and [[Utilizing templates and starter kits in development | Using Templates]]

### Reusing Existing Functionality
When you have a similar functionality needed on another page with a slight twist, reference the existing, working code <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. Copy the code and explicitly tell the AI what you want to change <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. More context leads to better answers <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### Leveraging Starter Kits and Templates
The smartest approach to development, especially for serious projects, is to start with a template that includes boilerplate code <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

*   **Common Components:** A good starter kit might include:
    *   A landing page <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>
    *   Payment integration (e.g., Stripe) <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>
    *   Database integration <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>
    *   Authentication (e.g., Google Auth, email login, two-factor authentication) <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>
    *   A dashboard <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>
*   **Time-Saving:** Starting with a template saves immense time, as complex functionalities like authentication and database setup are already handled <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.
*   **Finding Templates:** You can find free templates on platforms like GitHub by searching for "Next.js starter template" or "React starter template" <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>. Download the code and use it as your base in Cursor AI <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.

By implementing these strategies, developers and even beginners can significantly enhance their efficiency and effectiveness when [[Best Practices for Beginners Using Codex | using AI for coding tasks]]. The key is to provide as much context as possible to the AI models, treating them as co-pilots rather than autonomous solution providers <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.