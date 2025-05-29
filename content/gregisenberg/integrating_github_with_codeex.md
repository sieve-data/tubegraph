---
title: Integrating GitHub with Codeex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[codeex_introduction_for_non_technical_users | Codeex]], a new AI engineer in the browser from Sam Altman and OpenAI, allows users to type in a task, have it coded, and then push the changes to GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This tool is explained by Ben Tossell, a renowned expert in no-code tools for non-technical users <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While some might find [[codeex_introduction_for_non_technical_users | Codeex]] overwhelming at first, especially compared to prototyping tools like [[integrating_firebase_with_bolt | Bolt]] <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, it offers a way to iteratively build and deploy code with integrated testing and checks <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

## What is GitHub?
GitHub is a platform where code is stored <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It functions as a profile where you can manage "repos" (repositories), which are essentially your projects <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. A repository stores all your code files <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Any changes made to the code are tracked as "commits" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Creating a GitHub Repository
To start a new project, such as a personal or marketing site, you need to create a new repository <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. When creating a repository, you can:
*   Type in any name <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   Choose to make it public or private <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   Add a README file, which explains what your project does <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Connecting Codeex to GitHub
[[codeex_introduction_for_non_technical_users | Codeex]] needs to be connected to GitHub <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This connection allows [[codeex_introduction_for_non_technical_users | Codeex]] to push coded tasks directly to your repository <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For example, a website can be created and managed entirely with [[codeex_introduction_for_non_technical_users | Codeex]] through this connection <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Workflow: Making Changes with Codeex
1.  **Add a Task**: In [[codeex_introduction_for_non_technical_users | Codeex]], you describe the desired change in plain language, such as "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Generate Code**: You can hit "ask" to get information about your code without generating changes, or hit "code" to have [[codeex_introduction_for_non_technical_users | Codeex]] generate the necessary code <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
3.  **Codeex Processing**: [[codeex_introduction_for_non_technical_users | Codeex]] uses the terminal to find files, understand existing code, and then creates or updates files as needed <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It will describe the actions it plans to take, such as creating a new document or updating the main site <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
4.  **Testing**: [[codeex_introduction_for_non_technical_users | Codeex]] performs its own tests to ensure the changes are successful <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. It shows how many lines of code were added or removed <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
5.  **Create a Pull Request (PR)**: After [[codeex_introduction_for_non_technical_users | Codeex]] completes a task, you need to create a "Pull Request" (PR) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   **Branches**: Code is often managed in "branches." The "main branch" is the primary version of your code <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. When working on a new feature, a copy of the code is made into a new "branch" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   **Merging**: If the feature works correctly and there are no conflicts with the main codebase, you can "merge" it back into the main branch <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   **PR Summary**: The PR provides a summary of what [[codeex_introduction_for_non_technical_users | Codeex]] did <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. If all checks pass and there are no conflicts, you can merge the PR <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
6.  **Deployment**: Once merged, the changes are deployed, and you can see them live on your site <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Deployment can be handled through services like GitHub Pages or Vercel <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Managing Tasks: Merged and Closed
*   **Open**: When you create a task in [[codeex_introduction_for_non_technical_users | Codeex]], it starts as "open" <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Merged**: A task is "merged" when its changes have been successfully integrated into the main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. The numbers displayed next to merged tasks indicate the lines of code added (+) and removed (-) across the entire codebase <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Closed**: If a proposed change is not suitable or doesn't pass checks, you can "close" the pull request, effectively denying the changes <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This means the code on that branch is disregarded, and your main codebase remains unaffected <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

## Benefits for Non-Technical Users
[[codeex_introduction_for_non_technical_users | Codeex]] allows non-technical users to build and deploy websites without writing a single line of code <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Its UI is designed so that you don't need to look at or think about the code <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. Instead, you interact with it as a "to-do list," delegating tasks to the AI <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This iterative approach, combined with built-in tests, reduces time spent debugging <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. It also provides a lightweight introduction to computer science and development terminology, making it a more accessible way to learn about coding concepts <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

## Best Practices and Limitations for Beginners
*   **Start Simple**: Begin by using [[codeex_introduction_for_non_technical_users | Codeex]] on a personal site or by creating a new, simple personal site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Gradually**: Make small, incremental changes, such as adding a header, an about section, or social links <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. Avoid trying to build complex projects like a "Spotify clone" from scratch, as they often involve many non-functional pieces <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   **GitHub Setup**: Ensure you have a GitHub repository with at least a README file enabled <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Rolling Back Changes**: If a change breaks your site, you can always revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   **Leverage AI for Help**: If you get stuck, use external chatbots like ChatGPT to ask how to roll back GitHub changes or address issues <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can feed the entire code from your GitHub repository (by changing `github.com` to `uithub.com` in the URL) into ChatGPT for analysis <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
*   **Limitations**: [[codeex_introduction_for_non_technical_users | Codeex]] currently has limitations, such as not being able to upload files or images directly, or design UIs based on visual input <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. For design elements, you might need to use other tools like v0 and then import the generated code <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Environments**: For more advanced projects involving frameworks like Next.js or Python, you might need to set up "environments" in [[codeex_introduction_for_non_technical_users | Codeex]] and run terminal commands (e.g., `pnpm install`) to ensure the AI can interact with the code properly <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>. This is more akin to a proper development environment <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.
*   **Mobile Usage**: [[codeex_introduction_for_non_technical_users | Codeex]] is designed to be mobile-native, allowing users to ship updates on the go <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.