---
title: Differences Between Codeex and No Code Tools
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[Benefits and Challenges of Using AI Tools like Codex | Codeex]], developed by Sam Altman and OpenAI, is an "AI engineer in the browser" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> designed to assist with coding tasks. While seemingly complex, it offers a distinct approach compared to traditional no-code tools.

## What is Codeex?
[[Using Codex in the Browser for Beginner Developers | Codeex]] is a tool that allows users to type in a task, which it then codes and pushes to GitHub <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. It is presented as a tool that can be used by non-technical people <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>, although its initial perception might be overwhelming compared to visual prototyping tools <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

### Workflow with Codeex
The basic workflow involves:
1.  **Connecting to GitHub**: [[Using Codex in the Browser for Beginner Developers | Codeex]] requires a connection to a GitHub repository, which stores code files <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. Users create a repository for their project (e.g., a personal site) and can make it public or private <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
2.  **Initial Setup**: A website can be initially created with [[Using Codex in the Browser for Beginner Developers | Codeex]] <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>, or by taking existing code (e.g., from a no-code builder like Card) via "view page source" and using another coding agent to put it on GitHub <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
3.  **Adding Tasks**: Users add tasks in natural language, such as "add another tab next to investments tools that is called food I like" <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
4.  **Code Generation**: [[Using Codex in the Browser for Beginner Developers | Codeex]] generates code based on the task, showing lines added or removed <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. It uses the terminal to find files and understand the existing codebase <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
5.  **Pull Requests (PRs)**: After generating code, [[Using Codex in the Browser for Beginner Developers | Codeex]] creates a pull request. A pull request involves creating a separate "branch" of code to work on a feature, which, if successful and without conflicts, can be merged back into the main codebase <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
6.  **Merging or Closing**:
    *   **Merged**: If the changes are satisfactory and checks pass, the pull request is merged, integrating the new code into the main branch <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. The site updates after deployment <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
    *   **Closed**: If the generated code is not suitable (e.g., "awful" design), the pull request can be closed without affecting the main code <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. This is akin to closing a support ticket <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.
7.  **Lines of Code Changed**: [[Using Codex in the Browser for Beginner Developers | Codeex]] shows the number of lines of code added (+) and removed (-) across the codebase for each task <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>.

## Comparison with No-Code Tools

### Interface and Focus
*   **No-Code Tools (e.g., Card, [[comparisons_between_bolt_and_other_tools_like_cursor | Bolt]], Lovable)**: Typically have a visual UI with sidebars for components, offering a "what you see is what you get" experience <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>. They focus on quick prototyping and visual design.
*   **[[Using Codex in the Browser for Beginner Developers | Codeex]]**: Its UI is different, focusing on a chat interface where users input tasks. Users don't typically look at or think about the code directly, even though it's displayed <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. The focus is on delegating tasks to the AI agent <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>.

### Functionality and Iteration
*   **No-Code Tools**: Can quickly spit out visually "UI perfect" clones (e.g., Spotify clone), but often the underlying features are "underbuilt" and don't actually work <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. This can lead to difficulties when trying to get core functionality working.
*   **[[Using Codex in the Browser for Beginner Developers | Codeex]]**: Emphasizes iteratively adding features. Since it technically runs tests and checks, there should be less time spent debugging non-working parts <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>. If something breaks, users can simply give [[Using Codex in the Browser for Beginner Developers | Codeex]] another task or try a different coding agent <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.

### Mobile Usability
*   **[[Using Codex in the Browser for Beginner Developers | Codeex]]**: Allows users to set off "mini tasks to an agent" and monitor progress via chat, making it more mobile-native <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
*   **[[comparisons_between_bolt_and_other_tools_like_cursor | Bolt]]**: While usable on mobile, it might not offer a great experience <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.

### Learning Curve and Target Audience
*   **No-Code Tools**: Generally perceived as easier to start for completely non-technical users due to their visual nature.
*   **[[Using Codex in the Browser for Beginner Developers | Codeex]]**: Despite being for non-technical users, it feels "10 times more overwhelming" due to its reliance on GitHub and underlying coding concepts like branches, commits, and pull requests <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. However, it can serve as a "lightweight way to learn how to code" by introducing computer science and development terminology in a more engaging way <a class="yt-timestamp" data-t="32:14:00">[32:14:00]</a>. It "drip feeds" coding concepts <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>.

### Limitations of [[Using Codex in the Browser for Beginner Developers | Codeex]]
*   **File Uploads**: Currently, [[Using Codex in the Browser for Beginner Developers | Codeex]] cannot upload files or images directly <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.
*   **UI Design**: It struggles with prompts like "make the UI look like this," requiring users to generate design code from other tools (e.g., v0) and then bring it into [[Using Codex in the Browser for Beginner Developers | Codeex]] <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a>.
*   **Advanced Features**: Working with databases or authentication is several steps up in complexity and requires more advanced understanding or external tools <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.

## Best Practices for Non-Technical Users with Codeex
For non-technical individuals exploring [[Using Codex in the Browser for Beginner Developers | Codeex]]:
*   **Start Simple**: Begin with a personal site or a new, non-critical personal site <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.
*   **Iterate Gradually**: Add features "line by line and piece by piece" <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.
*   **Understand GitHub Basics**: Ensure a GitHub repo exists with at least a README file enabled <a class="yt-timestamp" data-t="19:29:00">[19:29:00]</a>.
*   **Experiment**: Play around with merging and closing tasks <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.
*   **Safety Net**: GitHub allows reverting to previous versions if a change breaks the site, mitigating risk for personal projects <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   **Seek External Help**: Use external AI chat tools (like [[Comparison between ChatGPT Pro and Perplexity AI | ChatGPT.com]]) for questions about GitHub or to understand complex code, as [[Using Codex in the Browser for Beginner Developers | Codeex]]'s "ask" function is limited to its repo's knowledge <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>. Users can copy the entire code of their GitHub repo (by changing the first letter to 'u' in the URL, e.g., `uithub.com`) and paste it into [[Comparison between ChatGPT Pro and Perplexity AI | ChatGPT]] for analysis <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.

## Future of AI Coding Tools
The future of AI coding tools like [[Using Codex in the Browser for Beginner Developers | Codeex]] is expected to include more automation, such as automated merging of successful pull requests <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. While [[Using Codex in the Browser for Beginner Developers | Codeex]] is still in early preview, its approach of "delegating" tasks to an AI agent might become a standard UI for tools like [[comparisons_between_bolt_and_other_tools_like_cursor | Bolt]] and Cursor in the future <a class="yt-timestamp" data-t="32:50:00">[32:50:00]</a>. This method is seen as a potentially better starting point for learning coding than "text-to-app builders" that create overly complex but functionally flawed applications from the outset <a class="yt-timestamp" data-t="34:13:00">[34:13:00]</a>.