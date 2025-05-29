---
title: Using multiple AI models to solve coding issues
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

To achieve the best results when coding with AI, particularly with tools like Cursor AI, it's crucial to understand best practices and workflow fundamentals that go beyond simply asking the AI to build something <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This approach can save hours of time and help build functional applications <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Key Strategies for Effective AI Coding

### 1. Planning: The "Measure Twice, Cut Once" Strategy
Before jumping into coding with AI, it's vital to adopt a developer mindset and plan what you intend to build <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This includes:
*   **Visualizing the Output** Have a clear picture in mind of what you want to build <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Sketching Designs** Use tools like Figma, Paint, or even handwritten sketches to outline the design <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Using AI for Early Visualization** Platforms like v0 are highly recommended for visualizing your potential app or Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. You can prompt v0 with design ideas, and it generates UI using libraries like `shaten UI` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can even upload your sketches to v0 for further refinement <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **"Rubber Ducking" with AI** Use AI to discuss your thought process, similar to the programming concept of "rubber ducking," which can lead to new realizations about your approach <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
Spending significant time in this planning phase, even before using a coding AI like Cursor, sets up the AI for success by providing ample context <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### 2. Utilizing Cursor.Directory for Best Practices
A crucial step is to use `cursor.directory` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. This website provides pre-written prompts that can be copied and pasted into a `.cursor_rules` file in the root of your project <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Setting AI Context** These prompts set up Cursor AI with initial instructions and best practices tailored to specific technologies (e.g., Next.js, Python, React) <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Avoiding Outdated Information** This helps prevent the AI models from pulling outdated information, ensuring the code generated aligns with current best practices <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Customizing Prompts** If your specific technology stack isn't listed, you can copy existing prompts from `cursor.directory` and use other AI models (like Claude or ChatGPT) to adapt them for your technologies <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### 3. Tagging Documentation
Inside Cursor, you can "tag" documentation links directly into your project <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Providing Up-to-Date Context** This gives Cursor AI access to the latest and most accurate information for the technologies you are using (e.g., Next.js, Superbase) <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Enhanced Debugging** When issues arise, Cursor can use this up-to-date documentation to [[debugging_and_problemsolving_strategies_with_ai_coding | debug]] more effectively and provide relevant solutions <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **Learning Opportunity** Even non-technical users can review the documentation mentioned by the AI to learn more about the underlying technologies and better understand the ecosystem <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

### 4. Consulting Other AI Models for [[debugging_and_problemsolving_strategies_with_ai_coding | Debugging and Problem-Solving]]
There will be instances when Cursor AI gets stuck on a bug or problem <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. When this happens:
*   **Switch AI Models** Copy the issue and paste it into another AI model, such as Claude or even ChatGPT <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. Even if they use similar underlying models, a fresh context can often yield a solution <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   **Provide Full Context** Don't just paste the bug. Include:
    *   The problem description <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
    *   The solutions Cursor (or the previous AI) attempted that failed <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.
    *   The output you're getting and what you're expecting <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
*   **Iterative Approach** Providing this comprehensive context to the new AI significantly increases the chances of a successful resolution <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>. This iterative process of using multiple AI models to overcome [[challenges_in_coding_with_ai | challenges]] is key to success <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.

### 5. Leveraging AI for Explaining and Teaching Code
AI is excellent at explaining and teaching code, which is invaluable for learning and improving code <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.
*   **Understanding Existing Code** Ask the AI to explain already written code, including its flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Clarifying Concepts** If a term or concept doesn't make sense, copy it and ask the AI for a simpler explanation (e.g., "explain this to me like a beginner") <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.
*   **Generating Documentation** AI can generate documentation and comments for your code, saving developers significant time <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>.
*   **Learning by Doing** Embrace the "pain" of coding, as you learn the most when code breaks and you have to [[debugging_and_problemsolving_strategies_with_ai_coding | debug]] and fix it <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. This process, combined with AI explanations, accelerates learning.

### 6. Duplicating and Adapting Existing Functionality
When building similar features on different pages, leverage existing code <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
*   **Reference Existing Code** Copy the existing, well-functioning code and tell the AI: "This works for this page; can we do the same thing for this page, but [explain desired twist]?" <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
*   **Context is Key** The more context you provide, the better the AI's answers will be <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### 7. Utilizing Starter Templates
Starting with a well-structured template can significantly accelerate development <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.
*   **Boilerplate Code** These templates often include common functionalities like landing pages, payment integrations (e.g., Stripe), database setup, authentication (e.g., Google Auth), and dashboards <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Building on Top** Instead of building from scratch, use a reliable template found on platforms like GitHub (e.g., "Next.js starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>. You can then use Cursor AI to [[building_apps_with_ai_tools | build]] on top of this pre-existing foundation <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.
*   **Saving Time** This strategy helps bypass the complex initial setup of difficult features like authentication or database configuration <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.

By combining these strategies, users can overcome [[challenges_in_coding_with_ai | challenges in coding with AI]], learn more effectively, and achieve better, more consistent results with tools like Cursor AI <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. The ongoing development of AI models means that investing time in learning these practices now will prepare you for future advancements <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.