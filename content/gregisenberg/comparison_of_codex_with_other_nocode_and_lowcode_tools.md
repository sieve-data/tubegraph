---
title: Comparison of Codex with other nocode and lowcode tools
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codex, a new AI engineer in the browser from Sam Altman and OpenAI, is designed to allow users, including non-technical individuals, to generate and manage code through natural language prompts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores how Codex compares to other [[nocode_automation_tools_comparison | no-code]] and low-code tools.

## What is Codex?

Codex is a tool where users can type in a task, and it will code it for them and then push the changes to GitHub <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It connects to a user's GitHub repository, allowing for direct code storage and change management <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Ben Tossell, renowned for explaining [[exploring_nocode_tools_for_rapid_prototyping_and_deployment | no-code tools]] to non-technical audiences, notes that while some perceive Codex as primarily for senior engineers, he aims to demonstrate its utility for those with less technical backgrounds <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Core Workflow with Codex
The basic workflow involves:
1.  **Connecting to GitHub:** GitHub acts as a storage for code, where projects (repositories) hold all code files <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Creating a Repository:** Users create a new repository for each project, such as a personal or marketing site <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
3.  **Adding Tasks:** Users add a task by typing what they want to change or add to their website <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
4.  **Generating Code:** Codex generates the necessary code for the task <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. It runs internal tests and checks to ensure functionality <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
5.  **Creating a Pull Request (PR):** After code generation, a PR is created on GitHub. This process involves copying the main code to a side "branch," working on the feature there, and then merging it back if there are no conflicts <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
6.  **Merging or Closing:** If checks pass and there are no conflicts, the PR can be merged to the main branch, integrating the changes into the live site <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. If the changes are unsatisfactory or cause issues, the PR can be closed, effectively denying the changes <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This process is likened to opening and closing a support ticket <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

## Codex vs. "Prototyping First" No-Code Tools

For non-technical individuals, Codex might initially seem more overwhelming than [[exploring_nocode_tools_for_rapid_prototyping_and_deployment | prototyping-first tools]] like Bolt and Lovable <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

### Bolt and Lovable
These tools are often described as "text to app builders" that tend to overbuild everything or have underbuilt features <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **UI Focus:** They can spit out a visually perfect UI (e.g., a Shopify Spotify clone) <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Functional Gaps:** However, often the underlying features don't actually work, requiring users to debug or build backward from the visual output <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. This makes them less suitable for actual deployment <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Mobile Experience:** While possible, using them on mobile is "not going to be great" <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

### Codex
In contrast, Codex focuses on iterative development and backend functionality:
*   **Code Abstraction:** Users don't need to look at or think about the code directly <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The focus is on the task <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
*   **Iterative & Tested:** Codex supports iteratively adding features, with built-in tests and checks to ensure functionality and minimize debugging <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Delegated Work:** It enables a "delegated" feel, where an advanced AI agent handles the coding tasks <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Mobile Native:** Codex is described as "mobile native," allowing for frequent shipping of changes from a mobile device <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

## Codex vs. Other AI Coding Tools and Environments

While Codex is an [[overview_of_ai_coding_tools | AI coding tool]], it exists in a broader ecosystem.

### Card (No-Code Builder)
Previously, sites could be built on [[nocode_tools_and_marketplaces | no-code builders]] like Card <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The HTML code from such a site can be copied (via "view page source") and then used with a coding agent to be put onto GitHub <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Coding Agent Factory
This was used to take the copied code from a [[nocode_tools_and_marketplaces | no-code builder]] like Card and put it onto a GitHub repository, effectively converting a [[nocode_tools_and_marketplaces | no-code]] site into a code-based one <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Cursor
Cursor is a coding environment where users can chat and ask questions about the codebase, similar to Codex's "ask" feature <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### VZero
VZero is a tool that can generate design elements, specifically UI code. This generated code can then be imported into Codex or deployed directly to GitHub <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### ChatGPT (.com)
For more complex debugging or understanding GitHub operations (like rolling back changes), using ChatGPT directly is recommended <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. Unlike Codex's internal "ask" feature, ChatGPT.com can access the internet and provide broader knowledge, in addition to analyzing specific code pasted in by the user <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

## Limitations of Codex and Workarounds

Codex has specific limitations that highlight the need for other tools or methods:
*   **File Uploads:** Codex cannot directly upload files or images <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **UI Design from Images:** It cannot take a visual design (e.g., from an image) and convert it into a UI <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. For this, tools like VZero are needed <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Environment Setup:** To work with more complex applications (e.g., those using frameworks like Next.js or Python), users need to run specific terminal commands (like `pmpm install`) within Codex's execution environment <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

## User Experience and Learning Curve

For non-technical people, the terminology around tools like Codex and GitHub can be overwhelming <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. However, playing with Codex can be a lightweight way to learn coding fundamentals and development terminology in a more engaging manner <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

### Best Practices for Non-Technical Users
*   **Start Simple:** Begin with a personal site or create a new one to avoid being precious about existing work <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Small:** Add features line by line and piece by piece, like adding a tab, removing text, or adding shortcuts <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **GitHub Setup:** Ensure a GitHub repo is set up with at least a `README` file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Experimentation:** Play around with merging and closing tasks <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. There is no real danger of permanently breaking a personal site, as GitHub allows reverting to previous versions <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
*   **Leverage External AI:** Use tools like ChatGPT for help with GitHub issues or complex coding questions <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   **Gradual Complexity:** After mastering a personal site, users can explore integrations (e.g., pulling live info from GitHub), user authentication, databases, or AI features <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.

### Conclusion for Learning
Codex's approach is seen as a better starting point for learning about coding compared to "text to app builders" <a class="yt-timestamp" data-t="00:34:13">[00:34:13]</a>. While the latter might create impressive, large-scale UIs, they often lead to more complex debugging challenges for novices <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>. Codex "drip-feeds" coding concepts by requiring GitHub setup first, then allowing iterative development <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>. It makes coding feel less like traditional coding, making it more approachable <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. It's suggested that future tools like Bolt and Lovable might adopt a similar task-based UI as seen in Codex <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.