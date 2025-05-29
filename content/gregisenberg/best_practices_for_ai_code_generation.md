---
title: Best practices for AI code generation
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

Leveraging AI tools like Cursor AI can significantly accelerate the process of turning ideas into functional code within minutes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. However, to achieve optimal results, it's crucial to adopt specific best practices, even if you are not a seasoned developer <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Mike, a front-end and full-stack developer who prefers Cursor over other copilots like GitHub Copilot, shares his insights on maximizing AI's potential in the coding process <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Plan Extensively: The "Measure Twice, Cut Once" Strategy

The first and most critical step is thorough planning before engaging an AI code generation tool <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Avoid the temptation to jump directly into the composer and ask the AI to build something without prior thought <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

- **Adopt a Developer Mindset**: Even if you're not a developer, cultivate a "developer mindset" by planning what you intend to build and how it should look <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
- **Visualize with Sketches**: Create visual representations, whether through simple sketches on paper, Paint, or design tools like Figma <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
- **Provide Context**: When prompting AI models, give them as much context as possible. Remember, you are the boss, and the AI is your co-pilot <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
- **Utilize Wireframing Tools**:
    - **Hand-drawn Sketches**: An example involved drawing a web3 portfolio page on an iPad, screenshotting it, and uploading it to an AI (like ChatGPT) to discuss planning and structure <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This acts as a form of "rubber ducking," where explaining your thoughts to the AI can lead to realizations <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    - **v0**: Highly recommended for visualizing potential applications or MVPs (Minimum Viable Products) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. You can feed v0 a prompt (e.g., "build a clean looking marketplace website for bicycle sellers") <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>, or even upload a sketch and describe what you want <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. v0 uses UI libraries like Shadcn UI to generate visually appealing interfaces <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
- **Workflow**: Start with v0 (or drawing it out) to get a clear sense of what you want to build. Only then should you transition to Cursor or other AI models <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Aim for at least 10 to 15 prompts with v0 to refine your vision <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

> "Step one of being good at cursor: don't go on cursor." <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>

This planning phase saves significant time and headache, especially for those new to building with AI, by helping to anticipate and avoid issues <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.

## Set Up Your AI Environment with `cursor.directory`

To ensure your Cursor AI operates with the most relevant and up-to-date best practices for your chosen technologies, utilize `cursor.directory` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

- **Purpose**: This site provides pre-defined prompts or "rules" that Cursor AI will read *before* you even begin prompting it <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. This helps to prevent the model from pulling outdated information <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
- **Implementation**:
    1. Visit `cursor.directory` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    2. Search for the technologies you are using (e.g., Next.js, Python) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>, <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
    3. Copy the relevant prompt (e.g., "You are an expert in TypeScript, Node.js, Next.js App Router, React, Shadcn UI, Radix UI, and Tailwind") <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    4. In your project's root folder in Cursor, create a new file named `.cursor-rules` <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
    5. Paste the copied prompt into this file and save it <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
- **Customization**: If your specific technologies aren't listed, you can copy a few existing prompts and use another AI (like Claude or ChatGPT) to generate a similar `.cursor-rules` file tailored to your stack <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. For instance, you can ask for a prompt for React and Python, and even specify JavaScript instead of TypeScript <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>, <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
- **Benefits**: This simple, 30-second setup leads to "Night and Day Results" by providing your AI with proper context about your codebase <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>, <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Tag Documentation for Up-to-Date Information

Knowing the technologies you're building with and providing their documentation to your AI is critical for accurate and current assistance <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

- **Importance of Docs**: Technology documentation (e.g., `nextjs.org/docs` <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>) is typically the most reliable "source of truth" <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. AI models might scrape the internet, but some information could be outdated <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
- **How to Tag Docs in Cursor**:
    1. In Cursor's composer view, click "Add" then "Docs" <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
    2. Click "Add New Doc" <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
    3. Paste the URL of the documentation (e.g., `https://nextjs.org/docs`) and name it (e.g., "Next.js Docs") <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
    4. Confirm to save <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
- **Benefits**:
    - **Up-to-Date Solutions**: When you ask Cursor a question (e.g., "How can I build a simple page that says hello world?" <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>), it will refer to the tagged documentation for the latest information and best practices <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
    - **Debugging**: The AI can debug issues using the most current documentation, helping you resolve bugs faster <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.
    - **Learning**: For beginners, browsing documentation helps you understand the language and ecosystem of different frameworks (e.g., Superbase, Next.js) <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. AI can expedite this learning process by explaining complex concepts <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
- **"Learning by Doing"**: Embrace the process of learning by doing. When something breaks, understand why it broke with AI's help, and you'll learn how things work <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

## Consult Other AI Models When Stuck

Sometimes, an AI model like Cursor might get "stuck" on an issue, even if it seems simple <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

- **Switching Models**: If Cursor is continuously stuck, it's time to consult another AI model, such as Claude, v0, or even ChatGPT <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
- **Provide Comprehensive Context**: When moving to a different AI, don't just copy the bug. Include:
    - The issue itself <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
    - The solutions the previous AI tried that failed <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
    - The output you're currently getting and what you're expecting <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
- **Benefits**: Providing this complete context forces the new AI to think differently, leading to much better results <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>, <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.

## Leverage AI for Explanation and Teaching

AI models are excellent at explaining and teaching code and concepts, which is invaluable for both developers and non-developers <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.

- **Explaining Existing Code**: If you have existing code, ask the AI to explain it "like a beginner," including the flow, logic, and overall functionality <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. For example, an AI can break down a React component, explaining its setup, props, and how it handles client-side interactions <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>.
- **Clarifying Concepts**: If the explanation includes terms you don't understand (e.g., "use client" directive), you can copy that specific phrase and ask the AI to elaborate <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. This iterative process allows you to gradually understand patterns and build knowledge <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
- **Adding Comments**: AI can automatically add comments to your code, which is a traditionally "annoying" task for developers <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
- **Long-Term Growth**: Investing time in learning how to use these tools effectively now will better prepare you for when AI models become even more powerful in the future <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>. Developers can pick up new technologies much faster with AI as a co-pilot, learning while building <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

## Duplicate and Adapt Existing Functionality

When building, if you have a piece of code or functionality that works well on one page and you need something similar (with a slight modification) on another, leverage what already exists <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.

- **Process**: Copy the existing code or describe the functionality and tell the AI, "This works for this page; can we do the same thing for this page, but [explain the desired twist]?" <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
- **Context is Key**: The more context you provide about the existing functionality and the desired changes, the better the AI's output will be <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.

## Start with Boilerplate Templates

For serious projects, starting with a well-structured template can save immense development time <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

- **Benefits of Templates**: Templates often include common, complex functionalities like landing pages, payment integrations (e.g., Stripe), database setup, and various authentication methods (e.g., Google Auth, email, two-factor authentication) <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>.
- **Workflow**: Instead of building these elements from scratch repeatedly, start with a pre-built "starter kit" <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>. You can find free templates on platforms like GitHub by searching for "Next.js starter template" or "React starter template" <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>.
- **AI Integration**: Download a template and use it as your base in Cursor. This allows you to "cook" quickly by building on top of established foundations, rather than spending time on common boilerplate code <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>. It's expected that AI platforms themselves will increasingly provide such templates <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

By following these practices, users can transform their ideas into working code more efficiently and effectively, leveraging AI as a powerful co-pilot in the development journey.