---
title: Planning before using AI tools
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Effectively utilizing AI tools like Cursor AI for turning ideas into code requires a strategic approach, particularly in the planning phase <a class="yt-timestamp" data-t="00:00:05"></a>. The goal is to obtain the best results from these tools <a class="yt-timestamp" data-t="00:01:19"></a>.

## The Importance of Planning

Jumping directly into a tool like Cursor AI without a clear plan is not recommended <a class="yt-timestamp" data-t="00:02:32"></a>. Even if you're not a seasoned developer, adopting a "developer mindset" by planning what you intend to build and how it should look is crucial <a class="yt-timestamp" data-t="00:02:42"></a>.

The core principle behind this is to provide AI models with as much context as possible <a class="yt-timestamp" data-t="00:03:01"></a>. Consider yourself the "boss" and the AI as your "co-pilot" <a class="yt-timestamp" data-t="00:03:07"></a>.

### Planning Strategies

1.  **Visual Planning and Sketching:**
    *   Start by sketching out your ideas. This can be done using tools like Figma, Paint, or even simply by hand <a class="yt-timestamp" data-t="00:02:50"></a>.
    *   Having a visual representation helps clarify your vision before you begin coding <a class="yt-timestamp" data-t="00:02:56"></a>.
    *   An example given is drawing a web3 portfolio page on an iPad and then using that screenshot with an AI model like ChatGPT to plan the structure <a class="yt-timestamp" data-t="00:04:11"></a>.
    *   This process is similar to "rubber ducking" in programming, where explaining your thoughts helps lead to realizations about the best approach <a class="yt-timestamp" data-t="00:05:30"></a>.

2.  **Using Visualization Tools like V0:**
    *   For those not using design software like Figma, tools like v0 (vzer.dev) are highly recommended <a class="yt-timestamp" data-t="00:05:53"></a>.
    *   v0 excels at helping you visualize what your potential app or Minimum Viable Product (MVP) will look like <a class="yt-timestamp" data-t="00:06:06"></a>.
    *   You can start with a general idea, such as "build a clean looking marketplace website for bicycle sellers," and v0 will generate initial designs <a class="yt-timestamp" data-t="00:07:07"></a>.
    *   V0 is built using Shadcn UI, which helps in generating aesthetically pleasing user interfaces <a class="yt-timestamp" data-t="00:07:51"></a>.
    *   You can refine the design by asking for specific changes (e.g., "better gradient," "more rounded edges," "testimonial section") <a class="yt-timestamp" data-t="00:08:02"></a>.
    *   It's possible to take a handwritten drawing, upload it to v0, and then prompt v0 to build a website based on that wireframe <a class="yt-timestamp" data-t="00:08:35"></a>.
    *   Spend a significant amount of time here, aiming for 10-15 prompts with v0 to get the design as close as possible to your vision <a class="yt-timestamp" data-t="00:10:34"></a>.
    *   Only once you have a solid visual plan from v0 should you then proceed to Cursor AI or other AI models <a class="yt-timestamp" data-t="00:07:30"></a>. The advice is: "Step one of being good at cursor: don't go on cursor" initially <a class="yt-timestamp" data-t="00:10:49"></a>.

## Preparing Cursor AI for Success

Beyond visual planning, preparing your AI environment is equally vital for optimal outputs.

### Utilizing Cursor.directory

*   Cursor.directory is a valuable resource offering pre-written prompts for various technologies (e.g., Next.js, Python) <a class="yt-timestamp" data-t="00:11:17"></a>.
*   These prompts act as an initial guide for Cursor, setting best practices and preventing the model from pulling outdated information <a class="yt-timestamp" data-t="00:12:06"></a>.
*   To implement, copy the relevant prompt from cursor.directory and create a new file named `.cursor_rules` in the root of your project <a class="yt-timestamp" data-t="00:12:37"></a>. Paste the copied text into this file and save it <a class="yt-timestamp" data-t="00:13:37"></a>.
*   This ensures that every time you prompt Cursor, it understands the specific technologies and best practices of your codebase <a class="yt-timestamp" data-t="00:13:52"></a>.
*   If your specific technology isn't listed, you can take an existing prompt, adapt it using another AI like Claude or ChatGPT, and then apply it to your `.cursor_rules` file <a class="yt-timestamp" data-t="00:14:30"></a>.

### Tagging Documentation within Cursor

*   Knowing the technologies you are using, even if you don't fully understand their internal workings, is important <a class="yt-timestamp" data-t="00:19:35"></a>.
*   Every technology typically has official documentation (e.g., nextjs.org for Next.js, supabase.com for Superbase) <a class="yt-timestamp" data-t="00:19:51"></a>.
*   Within Cursor, you can "tag docs" by adding URLs to the documentation of the technologies you are using <a class="yt-timestamp" data-t="00:20:31"></a>.
*   This provides Cursor with the latest and most accurate information, preventing it from relying on potentially outdated scraped data <a class="yt-timestamp" data-t="00:21:01"></a>.
*   When facing an issue, you can prompt Cursor to use the tagged documentation to debug problems, leading to more relevant solutions <a class="yt-timestamp" data-t="00:23:08"></a>.
*   This practice is particularly beneficial for beginners, as it helps them learn the terminology and ecosystem of different frameworks <a class="yt-timestamp" data-t="00:23:55"></a>.

## General AI Workflow Tips for Building

*   **Embrace the "Pain":** Building with AI tools will still involve challenges and getting stuck. Planning and setting up the AI environment properly can reduce this pain <a class="yt-timestamp" data-t="00:18:04"></a>.
*   **Provide Context:** AI models are not magic; they require context. The more information you provide about what you're building and doing, the better they can align with your goals <a class="yt-timestamp" data-t="00:24:57"></a>. This is like "onboarding a new employee" <a class="yt-timestamp" data-t="00:25:13"></a>.
*   **Consult Other AI Models:** If Cursor gets stuck, copy the issue (including potential failed fixes and expected output) and paste it into another AI model like Claude or ChatGPT <a class="yt-timestamp" data-t="00:26:16"></a>. Providing the context of previous attempts and failures helps the new AI model offer fresh solutions <a class="yt-timestamp" data-t="00:27:27"></a>.
*   **AI for Explanation and Learning:** AI models are excellent at explaining existing code or complex concepts <a class="yt-timestamp" data-t="00:29:26"></a>. Use this feature to understand your codebase or new technologies (e.g., asking "explain this code to me like a beginner" <a class="yt-timestamp" data-t="00:30:31"></a> or "what does this mean?" for specific lines <a class="yt-timestamp" data-t="00:31:32"></a>). This helps in learning while doing <a class="yt-timestamp" data-t="00:32:26"></a>.
*   **Adding Code Comments:** AI can automatically add comments to your code, which is helpful for documentation and understanding <a class="yt-timestamp" data-t="00:35:11"></a>.
*   **Duplicating Existing Functionality:** If you have working code or functionality on one page and need something similar but with a twist on another, reference the existing code. Explain what works and how you want it adapted for the new context <a class="yt-timestamp" data-t="00:35:50"></a>. More context leads to better answers <a class="yt-timestamp" data-t="00:36:05"></a>.
*   **Using Starter Templates:** Beginning with a pre-built template that includes common functionalities like a landing page, authentication, payment integration (e.g., Stripe), or database setup can save significant development time <a class="yt-timestamp" data-t="00:36:31"></a>. Many free templates are available on platforms like GitHub (e.g., "Next.js starter template" or "React starter template") <a class="yt-timestamp" data-t="00:38:11"></a>.

By following these [[tips_for_using_ai_tools_effectively_in_design_workflows|planning]] and preparation steps, you can significantly enhance your experience and the results when [[building_apps_using_ai_tools|building apps using AI tools]] like Cursor AI <a class="yt-timestamp" data-t="00:00:39"></a>.