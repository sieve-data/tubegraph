---
title: Cursor AI best practices
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

[[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]] offers the exciting prospect of translating ideas into code rapidly <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. To maximize results and save significant time, adopting specific best practices is crucial <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. This guide outlines key strategies for getting the most out of [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]].

## 1. Plan and Visualize Before Coding

The most important step is thorough planning, even if you are not a seasoned developer <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Approach development with a "developer mindset" by planning what you intend to build and how it should look <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

### Planning Techniques
*   **Sketching**: Have a visual representation in mind, using tools like Paint, Figma, or even a handwritten sketch <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This provides crucial context for the AI <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
*   **You are the Boss**: Remember, you are the "boss," and the AI is merely a "co-pilot" <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. Do not assume the AI is smart enough to infer your needs <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **"Measure Twice, Cut Once" Strategy**: Planning extensively beforehand ensures better outputs and saves significant time and effort in the long run <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>, <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.
*   **Utilize [[comparison_with_cursor_ai_and_v0 | V0]]**: Before moving to [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]], use [[comparison_with_cursor_ai_and_v0 | V0]] to visualize your potential app or Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. Spend a substantial amount of time here, ideally 10-15 prompts, to get the visualization as close to your vision as possible <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>. This provides a strong starting point <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
*   **Start with Visuals**: It is recommended to start with a drawing (like a wireframe) and then use [[comparison_with_cursor_ai_and_v0 | V0]] to generate the UI from that drawing <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>, <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   **Delay Coding**: Avoid jumping directly into [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] (or Claude) to build things without prior planning <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.

## 2. Implement Cursor Rules via `cursor.directory`

To set up your [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]] codebase for success, use the `cursor.directory` website. This resource provides pre-written prompts that guide [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] on best practices for specific technologies.

### How to Use `cursor.directory`
1.  **Find Relevant Prompts**: Visit `cursor.directory` and search for the technologies you are using (e.g., Next.js, Python) <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.
2.  **Copy Prompt**: Select and copy the prompt that best aligns with your project <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. These prompts inform [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] that it should act as an expert in those technologies and follow specific best practices <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.
3.  **Create `.cursor_rules` File**: In the root of your project folder in [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]], create a new file named `.cursor_rules` <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
4.  **Paste and Save**: Paste the copied prompt into the `.cursor_rules` file and save it <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.

This simple implementation takes about 30 seconds but yields "night and day results" in [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]]'s outputs, preventing it from pulling outdated information <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>, <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>. If your specific technologies aren't listed, you can use other AI models (like Claude or GPT) to generate a custom `.cursor_rules` prompt based on existing examples <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.

## 3. Tag Relevant Documentation

Understanding the technologies you use is essential, even if you don't know every detail of how they work <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>. Documentation is the most reliable "source of truth" for any technology <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>.

### How to Tag Docs in Cursor
1.  **Find Documentation**: Locate the official documentation for the technologies in your project (e.g., nextjs.org, Superbase docs) <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>.
2.  **Add Doc in Composer**: In [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]]'s composer view, click "add" and then "docs" <a class="yt-timestamp" data-t="20:29:00">[20:29:00]</a>.
3.  **Paste URL and Name**: Click "add new doc," paste the documentation URL, and give it a name (e.g., "Next.js Docs") <a class="yt-timestamp" data-t="20:37:00">[20:37:00]</a>.

By tagging documentation, you provide [[efficient_use_of_ai_tools_like_chat_gpt_and_cursor_ai | Cursor]] with the latest and most accurate information, helping it debug issues with up-to-date solutions <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>, <a class="yt-timestamp" data-t="23:17:00">[23:17:17]</a>. This is particularly helpful for beginners to learn about frameworks and platforms <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>. Providing context is key for all AI models; the more context you give, the better the answers <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.

## 4. Leverage Other AI Models When Stuck

Sometimes [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]] may get stuck on a bug or issue <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>. When this happens, consider consulting other AI models.

### Strategies for Consulting Other AIs
*   **Copy Issue to Another AI**: Copy the problem or bug and paste it into another AI model, such as Claude or [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | ChatGPT]] <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>.
*   **Provide Context on Failed Attempts**: Crucially, include the solutions that [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] tried but failed to implement <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>. Explain the issue, the attempted solutions, the output you received, and the expected output <a class="yt-timestamp" data-t="27:48:00">[27:48:00]</a>. This additional context significantly improves the results from the new AI <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.

## 5. Other Valuable Uses of AI in Development

Beyond initial setup, AI models like [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] and Claude excel at several development tasks:

*   **Explaining and Teaching Code**: Ask the AI to explain existing code, its flow, logic, and overall functionality as if to a beginner <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>. This can help you understand complex concepts and underlying patterns <a class="yt-timestamp" data-t="32:08:00">[32:08:00]</a>.
*   **Generating Documentation**: For developers, AI is excellent at writing documentation for existing code, which can be an otherwise annoying task <a class="yt-timestamp" data-t="29:30:00">[29:30:00]</a>.
*   **Adding Code Comments**: Instruct the AI to add comments to your code to improve readability and understanding <a class="yt-timestamp" data-t="35:11:00">[35:11:00]</a>.
*   **Duplicating and Modifying Functionality**: If you have existing functionality on one page that you want to replicate with a twist on another page, reference the original code. Explain what you want done, and the AI can adapt it <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>.
*   **Using Starter Templates**: Building on a template with boilerplate code (e.g., landing page, authentication, database integration) is a smart way to start serious projects <a class="yt-timestamp" data-t="36:35:00">[36:35:00]</a>. Many free templates are available on platforms like GitHub (e.g., Next.js starter template, React starter template) <a class="yt-timestamp" data-t="38:11:00">[38:11:00]</a>. [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor]] and other AI platforms are also expected to provide such templates <a class="yt-timestamp" data-t="37:57:00">[37:57:00]</a>.

By embracing these practices, users can significantly enhance their experience with [[efficient_use_of_ai_tools_like_chatgpt_and_cursor_ai | Cursor AI]], building more efficiently and effectively.