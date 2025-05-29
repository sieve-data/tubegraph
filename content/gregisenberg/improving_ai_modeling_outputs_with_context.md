---
title: Improving AI Modeling Outputs with Context
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

To get the best results from AI models like Cursor AI, it's crucial to provide them with as much context as possible. This approach helps in building functional and robust applications, saving hours of development time <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Key Strategies for Improving AI Outputs

### 1. Planning and Sketching
Before diving into coding with AI, adopt a developer mindset and plan what you intend to build <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This includes having a visual picture in mind, even if it's just rough sketches.

*   **Visual Aids** Consider drawing out your ideas using tools like Paint, Figma, or even pen and paper <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **"Measure Twice, Cut Once"** This strategy emphasizes thorough planning before execution <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Giving Context** When prompting AI models, provide as much context as possible. You are the boss; the AI is your co-pilot <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Using v0 for Visualization** Tools like v0 are excellent for visualizing what your potential app or Minimum Viable Product (MVP) will look like <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Start with v0 (or sketches) to refine your vision before moving to Cursor or Claude <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. It's recommended to spend 10 to 15 prompts in v0 to get your design as close to your vision as possible <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

> "The first step of being good at Cursor: don't go on Cursor" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>

### 2. Utilizing `cursor.directory`
`cursor.directory` is a valuable resource offering pre-written prompts that can be copied and pasted into your Cursor AI codebase <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

*   **Set Up for Success** These prompts act as initial instructions for Cursor, informing it about the technologies you are using (e.g., Next.js, Python, React, Tailwind) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This helps prevent the model from pulling outdated information and sets up your Cursor codebase for success <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Implementation** To use it, create a file named `.cursor_rules` in the root folder of your project, then copy and paste the relevant prompt from `cursor.directory` into it <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Custom Prompts** If your specific technologies aren't listed, you can take existing prompts and use other AI models like [[integrating_ai_models_like_grock_and_claude | Claude]] or ChatGPT to generate a similar custom prompt for your needs <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### 3. Tagging Documentation
Knowing the technologies you're building with and providing their official documentation to the AI is crucial for accurate and up-to-date responses <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

*   **Source of Truth** Documentation is generally the most reliable source of information for any technology <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **Adding Docs to Cursor** In Cursor's composer view, you can add documentation by providing the URL (e.g., Next.js docs, Supabase docs) <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. This gives Cursor access to the latest information, enabling it to debug issues with up-to-date best practices <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.
*   **Learning Opportunity** Even if you're non-technical, briefly reviewing documentation can help you understand the ecosystem and language, allowing you to ask better questions and learn while building <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

### 4. Consulting Other AI Models
There will be times when Cursor AI gets stuck on a bug or an issue <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

*   **Cross-Platform Consultation** If Cursor is stuck, copy the issue and paste it into another AI model like [[integrating_ai_models_like_grock_and_claude | Claude]] or ChatGPT <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
*   **Provide Full Context** When asking other AIs, don't just provide the bug. Also include the solutions Cursor attempted that failed, the current output you're getting, and what you're expecting <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. This additional context leads to much better results <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

### 5. Leveraging AI for Explaining and Teaching Code
AI models excel at explaining existing code and teaching concepts <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

*   **Documentation Generation** AI can effectively generate documentation for already written code, a task often disliked by developers <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>.
*   **Concept Clarification** Ask the AI to explain specific parts of your code or concepts you don't understand, like "Explain this code to me like a beginner," or "What does this mean?" <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>, <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. This iterative process helps you learn patterns and understand how things work <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.
*   **Accelerated Learning** By asking AI to explain new technologies, developers can pick up skills much faster than traditional methods <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.

### 6. Adding Comments to Code
AI can be used to automatically add comments to your code, improving readability and understanding for others (or your future self) <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.

### 7. Duplicating and Modifying Existing Functionality
If you have working code or functionality on one page that needs to be adapted for another with a slight modification, provide that existing code to the AI <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Referencing for Efficiency** Reference the existing functionality and explain the desired "twist" <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. This gives the AI a concrete starting point and more context, leading to better and more efficient results <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

### 8. Using Starter Templates
Building from a robust starter template saves significant time, especially for common functionalities <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.

*   **Boilerplate Code** A good template includes pre-built components like a landing page, payment integration (e.g., Stripe), database setup, user authentication (Google Auth, email/password, 2FA), and a dashboard <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Building on Foundations** Instead of starting from scratch, begin with a template and use AI to build on top of it <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>. This is particularly useful for complex features like authentication or database setup, which can be challenging to build from the ground up <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.
*   **Finding Templates** You can find many free starter templates on platforms like GitHub (e.g., "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.