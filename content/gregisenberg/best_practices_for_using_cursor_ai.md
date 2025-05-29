---
title: Best practices for using Cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]] offers an amazing way to turn ideas into code quickly <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To maximize its effectiveness and save development time, it's crucial to follow best practices <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These foundational strategies help in building functional applications and setting up your AI co-pilot for success <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## 1. Plan Before You Prompt

Planning is the most crucial step when using [[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Avoid immediately jumping into the composer to ask the AI to build something <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

*   **Developer Mindset**: Adopt a developer mindset by planning what you're going to build and how it might look <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Visualize with Sketches**: Create sketches, even if handwritten, or use tools like Paint or Figma, to visualize your idea <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This provides crucial context to the AI model, as you are the "boss," and the AI is the "co-pilot" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **The "Measure Twice, Cut Once" Strategy**: This approach emphasizes thorough planning before execution <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **"Rubber Ducking"**: Engaging the AI as a co-pilot to discuss your thoughts (similar to "rubber ducking" in programming) can lead to realizations about your approach <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Utilize v0**: A highly recommended tool for initial visualization is [[Using tools like Cursor AI for functionality and VZ for UI | v0]] <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. It excels at helping you visualize what your potential app or Minimum Viable Product (MVP) will look like <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. You can take a sketch or screenshot and upload it to [[Using tools like Cursor AI for functionality and VZ for UI | v0]] to generate initial designs and code <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
    *   [[Using tools like Cursor AI for functionality and VZ for UI | v0]] is built using Shadcn UI, a UI library that produces professional-looking interfaces <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   Spend at least 10-15 prompts with [[Using tools like Cursor AI for functionality and VZ for UI | v0]] to refine your vision before moving to [[Building AI Apps with Cursor Firebase and Vercel | Cursor]] <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    *   This initial planning saves significant headache later, especially for those new to development <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

## 2. Leverage Cursor.directory for Context

[[Building AI Apps with Cursor Firebase and Vercel | Cursor.directory]] is a valuable resource that provides prompts to optimize [[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]]'s understanding of your project's technology stack <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Initial Prompts**: These prompts, pasted into a `.cursor-rules` file in your project's root directory, serve as initial instructions for the AI before you even begin specific prompting <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Combat Outdated Information**: AI models can sometimes pull outdated information <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. By setting up these rules, you guide [[Building AI Apps with Cursor Firebase and Vercel | Cursor]] to adhere to current best practices for your chosen technologies (e.g., Next.js, TypeScript, React, Tailwind) <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Customization**: If your technology stack isn't explicitly listed, you can copy existing prompts from [[Building AI Apps with Cursor Firebase and Vercel | Cursor.directory]] and use other AI models (like Claude or ChatGPT) to adapt them for your specific technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## 3. Tag Official Documentation

Providing [[Embedding AI to enhance app functionality | Cursor]] with access to official documentation for your chosen technologies is crucial for accurate and up-to-date results <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

*   **Source of Truth**: Official documentation is typically the most reliable source of truth for how a technology works <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **How to Tag Docs**: In [[Building AI Apps with Cursor Firebase and Vercel | Cursor]], you can add URLs to documentation (e.g., Next.js, Superbase) as "docs" within the composer view <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This allows [[Building AI Apps with Cursor Firebase and Vercel | Cursor]] to read the latest information when responding to prompts or debugging <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Learning Opportunity**: Even for non-technical users, reviewing documentation can help you "speak the language" and understand the ecosystem <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. [[Embedding AI to enhance app functionality | AI]] can then expedite the learning process by explaining complex concepts based on these docs <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

## 4. Consult Other AI Models When Stuck

There will be instances where [[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]] gets stuck on a bug or issue <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

*   **Cross-Pollination**: Copy the problem, including the code causing the issue and any failed solutions [[Building AI Apps with Cursor Firebase and Vercel | Cursor]] has attempted, and paste it into another AI model like Claude or ChatGPT <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.
*   **Provide Context**: Crucially, provide *all* the context, including the bug, the failed solutions, the expected output, and the actual output <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. This tells the new AI that previous attempts have failed and new solutions are needed, leading to much better results <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>.

## 5. Leverage AI's Strengths

[[Embedding AI to enhance app functionality | AI]] excels at specific tasks that can significantly streamline your workflow:

*   **Explaining and Teaching Code**: Ask the AI to explain existing code (even your own) to you like a beginner, detailing its flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. This is an excellent way to learn new concepts and technologies <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Adding Comments and Documentation**: [[Embedding AI to enhance app functionality | AI]] is highly effective at generating documentation and adding comments to your codebase, which is often a tedious task for developers <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.
*   **Duplicating and Adapting Functionality**: If you have existing code or functionality that works well on one page, but need something similar with slight modifications on another, reference the working code <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. Tell the AI, "This works for this page, can we do the same thing for *this* page, but [explain the twist]?" <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. More context leads to better results <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

## 6. Build on Existing Templates and Boilerplate Code

Starting from scratch can be challenging, especially for common functionalities like authentication or payment processing <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

*   **Use Starter Kits**: Find and utilize starter kits or boilerplate code that already include common features like landing pages, authentication (e.g., Google Auth), database integrations, and dashboards <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>.
*   **GitHub Resources**: Look for well-regarded starter templates on GitHub (e.g., "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>. Download and use this code as your base in [[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]] <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.
*   **Efficiency**: Building on these templates allows you to "cook" much faster, as complex initial setups are already handled <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>.

By applying these best practices, you can significantly enhance your experience with [[Building AI Apps with Cursor Firebase and Vercel | Cursor AI]], build more effectively, and continuously learn throughout the development process.