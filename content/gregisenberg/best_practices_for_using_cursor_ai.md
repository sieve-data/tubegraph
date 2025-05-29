---
title: Best practices for using Cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor AI]] has revolutionized the process of turning ideas into functional code within minutes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its potential and ensure effective app development, it's crucial to follow best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This guide outlines key strategies for getting the best results from [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor AI]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Core Best Practices

### 1. Plan Before You Prompt
The most critical step is [[planning_before_using_ai_tools | planning]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Do not simply jump into the [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] composer and start asking it to build <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

*   **Developer Mindset**: Even if you're not a seasoned developer, adopt a developer mindset <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Visualize**: Plan what you're going to build and what it should look like <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Sketch**: Create sketches using tools like Paint or Figma, or even by hand <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. These visuals provide essential context to the AI model <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **You are the Boss**: Remember, you are the boss; the AI is your co-pilot <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **"Measure Twice, Cut Once"**: This strategy emphasizes thorough preparation before execution <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Leverage [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]]**: For visualizing your app's Minimum Viable Product (MVP), start with [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. It's excellent for generating UI based on prompts, especially with its integration of `shaten UI` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can even upload your hand-drawn wireframes to [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]] to refine them <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Aim for 10-15 prompts with [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]] to get your design as close as possible to your vision before moving to [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### 2. Utilize `cursor.directory` for Rules Files
The `cursor.directory` website provides pre-written prompts that set up your [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] codebase for success <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Initial Context**: These prompts act as the initial instructions [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] reads before you even begin your specific prompts <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Prevent Outdated Information**: AI models can sometimes pull outdated information. Using `cursor.directory` helps ensure [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] follows current best practices for specific technologies (e.g., Next.js, TypeScript, React) <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Implementation**: Create a `.cursor-rules` file in the root of your project folder <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. Copy the relevant prompt from `cursor.directory` (e.g., for Next.js) and paste it into this file <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This ensures [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] is aware of your codebase's foundation <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Custom Prompts**: If your technology stack isn't listed, you can take existing prompts from `cursor.directory`, go to an LLM like Claude or ChatGPT, and ask it to write a similar prompt for your specific technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### 3. Tag Documentation (Tagging Docs)
AI models scrape the internet, and sometimes the information they have might be outdated or not reflect best practices <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. The official documentation for any technology is usually the best source of truth <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

*   **Provide Latest Information**: Within the [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] composer, you can add documentation links (e.g., `nextjs.org/docs`) <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This gives [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] access to the latest and most accurate information for specific technologies like Next.js or Superbase <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Debug with Up-to-Date Context**: When encountering issues, [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] can debug them using the most up-to-date documentation <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Learning Opportunity**: Even for non-technical users, it's beneficial to browse through documentation <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. If something is unclear, screenshot it and ask the AI to explain it in simple terms <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This helps you understand the ecosystem and "speak the language" <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.

### 4. Consult Other AI Models
There will be times when [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] gets stuck on a bug or problem <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

*   **Diversify Your AI Tools**: When [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] struggles, consult other AI models like Claude, [[using_v0_and_cursor_ai_for_developing_apps_and_prototypes | V0]], or even ChatGPT <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.
*   **Provide Comprehensive Context**: When sharing the issue with another AI, don't just copy-paste the bug <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. Provide:
    *   The bug itself <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
    *   The solutions [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] tried that failed <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
    *   The output you're currently getting and what you expect <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
*   This rich context significantly improves the results from the new AI model <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## Specific AI Strengths for Development

### 1. Explaining and Teaching Code
AI models are excellent at explaining existing code and teaching complex concepts <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.

*   **Code Explanation**: Ask the AI to explain existing code like a beginner, detailing the flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
*   **Concept Clarification**: If a term or concept doesn't make sense, copy it and ask the AI for a simpler explanation <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. This process of asking "What did you do here?", "What do you mean by this?", or "How does this work?" accelerates learning <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>.

### 2. Adding Comments to Code
For developers, writing documentation can be tedious. AI is great at automatically adding comments to existing code, making it more understandable <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

### 3. Duplicating and Modifying Functionality
If you have a well-functioning piece of code or functionality on one page and need something similar but with a twist on another page, leverage the AI <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

*   **Reference Existing Code**: Copy the existing functional code and prompt the AI, "This works for this page. Can we do the same thing for this page, but [explain the desired modification]?" <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
*   **More Context, Better Results**: The more context you provide about the existing functionality and the desired changes, the better the AI's output will be <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### 4. Using Starter Templates/Boilerplate Code
Starting from scratch for every project can be inefficient, especially for common functionalities like authentication, payments, or basic dashboards <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>.

*   **Build on Boilerplate**: Find or create a "starter kit" or template that includes common boilerplate code (e.g., landing page, Google Auth, database integration, dashboard) <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Leverage GitHub**: Search GitHub for "Next.js starter template" or "React starter template" and download highly-rated ones <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.
*   **Efficiency**: Using a template as your starting point in [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor]] allows you to build on top of existing, complex functionalities, saving significant development time <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.

## General Advice for Developers Using AI

*   **Embrace the "Pain"**: Building things often involves challenges and getting stuck <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Embrace this pain as a learning opportunity; planning helps mitigate it <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Context is King**: AI models don't possess magic; they operate on the context they are given <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. Providing as much detailed context as possible aligns the AI with your goals <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. Think of it as onboarding a new employee <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.
*   **Long-Term Investment**: While it might seem to take longer initially, investing time in planning and learning how to effectively use AI tools will make you more self-sustaining and efficient in the long run <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. The best time to be a developer is now, with these powerful AI models acting as co-pilots <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.
*   **Learn by Doing**: Expect to encounter issues and break things; the learning often happens when you fix them and understand *why* they work <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

By integrating these best practices, developers can significantly enhance their workflow, save hours of time, and build more robust applications with [[introduction_to_bolt_and_comparison_with_cursor_ai | Cursor AI]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.