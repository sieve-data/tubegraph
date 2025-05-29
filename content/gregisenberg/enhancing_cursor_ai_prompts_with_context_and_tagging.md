---
title: Enhancing Cursor AI prompts with context and tagging
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

For those who have explored [[Cursor AI best practices | Cursor AI]], the ability to transform an idea into code within minutes is remarkable <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To achieve the best results and save hours of time, it's crucial to understand and apply best practices for interacting with AI, particularly focusing on providing ample context <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The core principle is that you are the boss, and the AI is your co-pilot <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## [[Planning and preparing before coding with Cursor AI | Planning and Preparing Before Coding]]

Before diving into coding with [[Cursor AI best practices | Cursor AI]], thorough planning is essential <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This includes:

*   **Developer Mindset**: Even if you're not a developer, adopt a developer mindset by planning what you intend to build and how it should look <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Visualizing**: Sketch out your ideas using tools like Paint, Figma, or even pen and paper <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The more visual context you provide, the better the AI model can understand your vision <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **"Measure Twice, Cut Once" Strategy**: This analogy emphasizes the importance of spending significant time on planning before generating code <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Leveraging V0**: V0 is a highly recommended tool for visualizing what your potential app or Minimum Viable Product (MVP) will look like <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   It helps in visualizing the UI, especially since it's built using Shadcn UI, resulting in nice-looking UIs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   You can start with a sketch (e.g., from an iPad) and then use V0 to refine it through multiple prompts (10-15 prompts are suggested) <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
    *   Once you have a clear visualization from V0, you can copy its code and bring it into [[Cursor AI best practices | Cursor AI]] for further development <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Rubber Ducking**: Use AI as a "rubber duck" to explain your thoughts and ideas <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This process of articulation can lead to new realizations about your project's approach <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

The first step to being good at [[Cursor AI best practices | Cursor AI]] is often *not* starting on Cursor itself, but rather with planning <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Utilizing `cursor.directory` for Initial Context

A key best practice is to use `cursor.directory` to set up initial prompts for your [[Cursor AI best practices | Cursor AI]] codebase <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Purpose**: `cursor.directory` offers pre-defined prompts that inform [[Cursor AI best practices | Cursor AI]] about the technologies you are using (e.g., Next.js, Python, React) and associated best practices <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Implementation**:
    1.  Visit `cursor.directory` <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
    2.  Find a prompt matching your project's technologies <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
    3.  Copy the text and create a new file named `.cursor_rules` in the root of your project directory <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
    4.  Paste the copied text into this `.cursor_rules` file and save it <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Benefits**: This file ensures that every time you prompt [[Cursor AI best practices | Cursor AI]], it understands your codebase's foundation, preventing it from pulling outdated or irrelevant information <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Customization**: If your specific technology stack isn't listed, you can copy existing prompts and use another AI model like Claude or ChatGPT to adapt them for your technologies and desired flow <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## Tagging Official Documentation

Another powerful way to provide context to [[Cursor AI best practices | Cursor AI]] is by tagging official documentation pages within the tool <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

*   **Process**: In [[Cursor AI best practices | Cursor AI]]'s composer view, you can click "add" and then "docs" to add a new document <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. You can paste the URL of official documentation (e.g., `nextjs.org/docs` or `supabase.com/docs`) and name it <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.
*   **Importance**: Documentation is usually the most accurate and up-to-date source of truth for any technology <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. Tagging these ensures [[Cursor AI best practices | Cursor AI]] has access to the latest information, helping it provide current best practices and debug issues more effectively <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
*   **Learning Opportunity**: Even for non-technical users, it's beneficial to browse these documents to become familiar with the terminology and ecosystem <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. If something is unclear, you can screenshot it and ask the AI to explain it simply <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

## Leveraging Other AI Models for Debugging

There will be instances when [[Cursor AI best practices | Cursor AI]] gets stuck on a bug <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. In such cases:

*   **Consult Other AIs**: Copy the issue and paste it into another AI model like Claude or even ChatGPT <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
*   **Provide Full Context**: Crucially, don't just paste the bug <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. Explain what solutions [[Cursor AI best practices | Cursor AI]] already tried that failed, the output you're getting, and what you expect <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. This additional context significantly improves the chances of getting a correct solution <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## Using AI for Explanation and Learning

AI models like [[Cursor AI best practices | Cursor AI]] and Claude are excellent tools for learning and understanding code <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>.

*   **Explaining Code**: Ask the AI to explain existing code, its flow, logic, and overall functionality, especially for beginners <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. If a concept within the explanation is unclear, ask the AI to elaborate further <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.
*   **Adding Comments**: AI can automatically add comments to your code, which is traditionally a tedious task for developers <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.
*   **Learning by Doing**: Embrace the iterative process where code might break initially <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. Each time you fix something, you learn how it works <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>.
*   **Long-term Investment**: Investing time now to learn how to interact with and leverage AI tools for development will pay off significantly as these models continue to improve exponentially <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.

## Duplicating Existing Functionality and Using Templates

*   **Referencing Existing Code**: If you have a functional piece of code or functionality on one page and need something similar with a slight modification on another, reference the existing code <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Explain to the AI that "this works for this page, can we do the same for this page, but [explain the twist]?" <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. This provides crucial context, leading to better results <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
*   **Starter Templates**: Using pre-built starter templates can significantly accelerate serious projects <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>. These templates often include common boilerplate code like landing pages, payment integrations (e.g., Stripe), database integrations, authentication (e.g., Google Auth), and dashboards <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>.
    *   Many free templates are available on platforms like GitHub (e.g., searching "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.
    *   Starting with a robust template allows you to build on top of established functionality, making complex tasks like authentication and database setup much easier <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.

Ultimately, the more context you provide to your AI models, the better and more aligned their answers will be <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>. Think of it as an onboarding phase for a new employee, where you equip them with all the necessary information to succeed <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.