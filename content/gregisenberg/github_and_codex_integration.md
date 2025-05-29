---
title: GitHub and Codex Integration
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[Introduction to ChatGPT Codex | Codex]], an AI engineer in the browser developed by Sam Altman and OpenAI, is designed to allow users to input a task, have it coded, and then push the changes to GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This integration is central to how [[Introduction to ChatGPT Codex | Codex]] operates, providing a way for both technical and non-technical users to manage and deploy code <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What is GitHub?

GitHub is a platform where code can be stored and managed <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It functions as a central location for your projects, referred to as "repositories" or "repos" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. A repository stores all the code files for a project <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

Key GitHub concepts explained:
*   **Repositories (Repos)**: Essentially, a project folder that stores all associated code files <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For example, a personal website would have its own repository <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Commits**: Any changes made to the code are recorded as "commits" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Branches**: Code is often organized into "branches" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The "main branch" is the primary version of the code <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. When working on new features, it's standard practice to create a new branch, which is a copy of the main code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This allows for isolated development without affecting the main codebase <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Pull Request (PR)**: When changes on a separate branch are complete and tested, a "pull request" is created to propose merging these changes back into the main branch <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. If there are no conflicts, the changes can be merged <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

To begin with GitHub, you need to create a new repository <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can name it anything, set it as public or private, and add a README file to explain the project <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Initial Setup with [[Introduction to ChatGPT Codex | Codex]]
For [[NonTechnical People Learning Code with Codex | non-technical people]], a GitHub account and a connected repository are prerequisites for [[Using Codex for Coding Tasks | using Codex]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. A website can even be created using [[Introduction to ChatGPT Codex | Codex]] from scratch, starting with an existing website's page source code <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The user copied the page source from a no-code builder like Card and used another coding agent (not [[Introduction to ChatGPT Codex | Codex]]) to push it to a GitHub repo <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Once the code is on GitHub, it can be connected to [[Using GitHub and Vercel for App Deployment | GitHub Pages]] to host the URL live, allowing for custom domains <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Alternatively, tools like [[Using GitHub and Vercel for App Deployment | Vercel]] can be used for deployment, which offers more advanced deployment options <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Workflow with [[Introduction to ChatGPT Codex | Codex]] and GitHub

The general workflow for [[Using Codex for Coding Tasks | using Codex]] involves:
1.  **Adding a Task**: Input a task into [[Introduction to ChatGPT Codex | Codex]], such as "add another tab next to investments tools that is called food I like in the dock. Put tacos" <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  **[[Using Codex for Coding Tasks | Codex]] Generates Code**: [[Introduction to ChatGPT Codex | Codex]] processes the request, analyzes existing files, creates new documents, and updates the main site to match the requested changes <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. It even performs its own internal tests <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
3.  **Create a Pull Request (PR)**: After [[Introduction to ChatGPT Codex | Codex]] completes the task, you create a new PR <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This action proposes the changes made by [[Introduction to ChatGPT Codex | Codex]] to be integrated into the main branch <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
4.  **Review and Merge**: On GitHub, you can review the PR, which provides a summary of the changes <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. If all checks pass and there are no conflicts with the base branch, you can merge the PR <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Merging integrates the new code into the main codebase <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
5.  **Deployment**: Once merged, the changes will deploy and become visible on your live site, though this may take a few seconds <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Understanding GitHub Terminology within [[Introduction to ChatGPT Codex | Codex]]

Within the [[Introduction to ChatGPT Codex | Codex]] interface, you will see statuses and numbers related to your tasks:
*   **Open**: A task starts as "open" when you initiate it <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Merged**: This indicates that the changes from the task have been successfully integrated into the main codebase or branch <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Closed**: If a task's output is unsatisfactory (e.g., the code doesn't work), you can close the pull request, effectively denying the proposed changes without affecting the main code <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   **Numbers (+/-)**: These numbers represent the lines of code changed. A positive number (+) indicates lines added, and a negative number (-) indicates lines removed across the entire codebase <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## [[Best Practices for Beginners Using Codex | Best Practices for Beginners Using Codex]]

For [[NonTechnical People Learning Code with Codex | non-technical people]] starting with [[Introduction to ChatGPT Codex | Codex]] and GitHub:

*   **Start Simple**: Begin by [[Using Codex for Coding Tasks | using Codex]] on a personal site or by creating a new one if you're concerned about your existing site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Small Changes**: Work "line by line" and "piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. For example, start by asking [[Introduction to ChatGPT Codex | Codex]] to "make a website with my name as the header," then add an "about section," and then "social links" <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Have a README**: Ensure your GitHub repo has at least a README file enabled when you create it <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Don't Fear Mistakes**: If a merged change breaks your site, you can always revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. There's little risk if it's a personal, non-client-facing site <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Ask [[Introduction to ChatGPT Codex | ChatGPT]] for Help**: If you get stuck or need to perform actions not directly available in [[Introduction to ChatGPT Codex | Codex]] (like rolling back GitHub changes), ask [[Introduction to ChatGPT | ChatGPT]] (the main chat.openai.com version) <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can even copy your entire code base (by changing `github.com` to `uithub.com` in the URL to view raw code) and paste it into [[Introduction to ChatGPT | ChatGPT]] for analysis <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Limitations and Advanced Usage

While powerful, [[Introduction to ChatGPT Codex | Codex]] has some limitations:
*   **File Uploads**: You cannot upload files, images, or directly instruct it to make UI look a certain way <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **Integrating Designs**: For UI design, you might use other tools like Vercel's v0 to generate design code and then bring that code into your GitHub repo for [[Introduction to ChatGPT Codex | Codex]] to interact with <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Environments and Terminal Commands
[[Introduction to ChatGPT Codex | Codex]] uses "environments" which are different connections to specific repositories <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>. This feature is more advanced, especially for projects using frameworks like Next.js or Python <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

To run more complex applications with [[Introduction to ChatGPT Codex | Codex]], you might need to use the "code execution" feature to run terminal commands (like `pnpm install` or `pnpm dev`) <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. These commands spin up necessary servers and components for the app to function <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. This is part of a "proper development environment" that goes beyond basic HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.

## Why Use [[Introduction to ChatGPT Codex | Codex]] with GitHub?

Despite potentially feeling overwhelming initially, [[Introduction to ChatGPT Codex | Codex]] offers unique benefits:
*   **Delegation**: [[Introduction to ChatGPT Codex | Codex]] acts as a delegated "agent" that handles the coding tasks for you, allowing you to focus on what you want to build rather than the how <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Iterative Development**: It supports an iterative approach, allowing you to continuously add small features with built-in tests and checks, reducing time spent debugging <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Learning Tool**: For [[NonTechnical People Learning Code with Codex | non-technical people]], [[Introduction to ChatGPT Codex | Codex]] can be a "lightweight way to learn how to code" by exposing you to computer science and development terminology in a practical, fun context <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>. It "drip feeds" coding concepts without requiring you to write code yourself <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.
*   **Future of [[Code deployment and integration with tools | AI-assisted building]]**: The task-based UI seen in [[Introduction to ChatGPT Codex | Codex]] is likely to become more common in other building tools <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

While [[Introduction to ChatGPT Codex | Codex]] may not be for daily use for everyone right now, it serves as an excellent learning project to explore [[Code deployment and integration with tools | AI-driven code development]] and gain familiarity with concepts like GitHub <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. The ultimate goal for non-technical users is to become "curious enough" to overcome barriers and start building <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.