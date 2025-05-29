---
title: Debugging and problemsolving in AIcentered coding projects
videoId: kDcM_xwmP3Q
---

From: [[gregisenberg]] <br/> 

Building applications with [[overview_of_ai_coding_tools | AI coding tools]] is becoming increasingly accessible, but it's not without its challenges. Users often encounter hurdles that require persistence and specific problem-solving strategies <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.

## Common Challenges in AI-Assisted Development

There are two main outcomes for users trying to build apps with AI: either they successfully create a full app they love, or they get stuck early on and give up <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The key differentiator is often the ability to push through errors and keep asking the AI for solutions <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

*   **Dealing with Errors and Bugs**: Expect a lot of errors, especially when integrating features like databases <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. These tools, while powerful, aren't perfect and often require iteration <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.
*   **"Plumbing" and Setup**: The initial setup, including configuring libraries and organizing files, can be the most annoying part of coding <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. While AI tools like v0 handle some of this, connecting different tools (e.g., Replet and Cursor) still requires manual steps <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.
*   **Lack of Clear Error Messages**: Sometimes, the most frustrating issue is a blank screen or a lack of specific error logs, making it difficult to diagnose the problem <a class="yt-timestamp" data-t="00:40:03">[00:40:03]</a>.
*   **API Integration Complexity**: Integrating AI features, especially those that require structured output or complex API interactions (like Open AI or Anthropic), often leads to bugs <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.
*   **Managing Context and Specificity**: AI tools can be sensitive to prompts. Not providing enough context or being too vague can lead to unexpected results <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.

## Strategies for Overcoming Challenges

### 1. Iterative Prompting and Communication with AI

Treating the AI (like Claude or Cursor) as a coworker is crucial <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. If it doesn't work on the first try, keep iterating and refining your prompts <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

*   **Be Specific**: Clearly describe what you want, even for subtle design elements like animations or dot patterns <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>, <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Explain the Purpose**: Telling the AI the "purpose" of a feature (e.g., evaluating startup ideas) can help it generate more creative and appropriate solutions <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Ask for Error Logs**: If the app isn't working and there's no error message, explicitly ask the AI to "add error logs" to the input field to diagnose the problem <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.
*   **Provide Visual Cues (Screenshotting)**: Screenshotting parts of the UI or existing designs and pasting them into the AI prompt can help the AI understand the desired layout and styling <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. You can even draw on screenshots to highlight specific areas for changes <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
*   **"Plead" or "Negotiate"**: Sometimes, a direct plea to the AI to "just make this work" or to "be lenient" can yield results, especially with complex parsing issues <a class="yt-timestamp" data-t="00:54:49">[00:54:49]</a>, <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

### 2. Understanding and Managing Libraries

*   **Install Dependencies**: When the AI suggests `npm install` for a new library (like `openai-edge` or `framer-motion`), it's crucial to run these commands in your project's shell (e.g., in Replet) <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>, <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. These libraries are essential for the AI-generated code to function <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Restart and Refresh**: After making code changes or installing libraries, stopping and re-running the application (e.g., `stop running` then `rerun` in Replet) and refreshing the web view is often necessary to see the changes take effect <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.

### 3. Version Control and Reversibility

*   **"Save All" vs. "Accept All"**: In tools like Cursor, always choose "Save All" over "Accept All" for changes. "Save All" allows you to reject unwanted changes, while "Accept All" is irreversible and requires asking the AI to undo it <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>.
*   **Reverting Changes**: If a change breaks the application, revert to a previous working state <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. This is analogous to version control in traditional coding.

### 4. Leveraging Documentation and Context

*   **Consult Latest Documentation**: When encountering persistent API issues, use tools like Perplexity to find the "latest API docs" for the specific service (e.g., OpenAI, Anthropic) and framework (e.g., Next.js) <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a>. Feeding this up-to-date documentation to the AI helps it make better decisions and write more accurate code <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.
*   **Provide Code Snippets**: If you have existing code that you want the AI to base new features on, paste it into the prompt. This provides crucial context <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

### 5. Mindset and Agency

*   **High Agency**: [[overcoming_challenges_in_aiassisted_app_development | Success with AI coding tools]] separates "high agency" from "low agency" individuals. High agency means taking charge and persistently seeking solutions from the AI, rather than giving up <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Embrace the Mess**: Debugging is part of the learning process. Mistakes are valuable opportunities to learn <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The iterative nature of AI development means sometimes you "carve out... more time than you think you need at first" <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>.
*   **Develop "Taste"**: Regularly using these tools helps you develop an eye for good design and understand what's feasible <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>, <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Knowing design terminology can also be very helpful when prompting <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

> "Once you get the aha moment where you're like oh this works and you realize that like you're in charge you don't need to ask anyone... you just need to ask AI... by the second or third try like you will will your way to a working app." <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

The process involves "composing code" by speaking English and guiding the AI <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This requires patience and a willingness to solve problems, often through trial and error <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.