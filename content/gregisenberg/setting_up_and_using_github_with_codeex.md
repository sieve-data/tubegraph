---
title: Setting up and using GitHub with Codeex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

This article explores the integration and practical application of [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]], OpenAI's AI engineer in the browser, with GitHub for non-technical users looking to modify websites and manage code without deep coding knowledge. Ben Tossel, known for explaining no-code tools, provides a live tutorial and insights into this process <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What is GitHub?

GitHub serves as a platform for storing and managing code <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It allows users to:
*   **Store Code**: Effectively acts as a storage solution for all your code files <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Repositories (Repos)**: Projects on GitHub are called "repositories" or "repos." Each project, like a personal website, is a separate repository <a class="yt-timestamp" data-t="00:03:16">[00:03:23]</a>.
*   **Commits**: Any changes made to the code are recorded as "commits," which are visible within the repository's history <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## Connecting Codeex to GitHub

[[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] is designed to connect to your GitHub repository, allowing it to type in a task, code it for you, and then push the changes to GitHub <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Initial Setup Steps:
1.  **GitHub Account**: You need to have a GitHub account connected to [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
2.  **Create a New Repository**: For a new project, such as a personal or marketing site, you must create a new repository <a class="yt-timestamp" data-t="00:04:01">[00:04:12]</a>.
    *   You can name it anything <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   Choose whether it's public or private <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   It is recommended to add a README file, which explains what your project does <a class="yt-timestamp" data-t="00:04:16">[00:04:19]</a>.

### Importing Existing Code (Optional)
One way to get an existing website into GitHub for use with [[introduction_to_openais_and_its_use_for_nontechnical_users | Codeex]] is by:
1.  Building a site on a no-code builder like Card <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  Viewing the page source (right-click -> `view page source`) to see the underlying HTML code <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
3.  Copying and pasting this code into another coding agent or environment that can then push it to a GitHub repository <a class="yt-timestamp" data-t="00:05:12">[00:05:24]</a>.
4.  Once the code is in GitHub, you can connect it to services like GitHub Pages or [[deploying_apps_with_vercel | Vercel]] to make your URL live and use custom domains <a class="yt-timestamp" data-t="00:05:30">[00:05:43]</a>.

## Using Codeex for Website Modifications

Once your GitHub repository is set up and connected, you can instruct [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to make changes.

### The Modification Process
1.  **Add a Task**: In [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]], you type a task describing the change you want, e.g., "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="00:02:19">[00:02:29]</a>.
2.  **Generate Code**: You can choose `Ask` (to get information about your code without generating changes) or `Code` (to generate and apply changes) <a class="yt-timestamp" data-t="00:06:10">[00:06:17]</a>.
3.  **Codeex Internal Actions**: [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] uses a terminal-like interface to find relevant files, understand the existing code, and then propose changes. It outlines the steps it will take, such as creating new documents, updating main site files, and adding new sections <a class="yt-timestamp" data-t="00:06:43">[00:07:50]</a>.
4.  **Tests**: [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] often performs its own tests to ensure the changes are successful <a class="yt-timestamp" data-t="00:08:42">[00:08:59]</a>.

### Pull Requests (PRs)
After [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] completes a task, it creates a Pull Request (PR) in GitHub <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Branches**: Code is typically managed in "branches." The "main" branch is the primary codebase. When you work on a new feature, a new branch is created (a copy of the main code) to work on that feature in isolation <a class="yt-timestamp" data-t="00:09:23">[00:09:38]</a>.
*   **Merging**: If the changes in the new branch are successful and don't conflict with the main codebase, they can be "merged" back into the main branch <a class="yt-timestamp" data-t="00:09:40">[00:09:47]</a>.
*   **Review and Merge**: You click "Create new PR" in [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to initiate this. On GitHub, you can view the PR summary, check for conflicts, and then merge it if all checks pass <a class="yt-timestamp" data-t="00:09:52">[00:10:14]</a>.
*   **Deployment**: After merging, the changes typically deploy to your live site, though there might be a short delay <a class="yt-timestamp" data-t="00:10:29">[00:10:31]</a>.

### Understanding Codeex Statuses
*   **Open**: A task starts as "open" when you initiate it <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Merged**: Indicates the changes have been successfully integrated into your main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:55]</a>.
*   **Closed**: If the generated code is not suitable or breaks something, you can "close" the pull request, effectively denying the changes without affecting your main code <a class="yt-timestamp" data-t="00:16:25">[00:16:41]</a>.
*   **Lines of Code Changed**: The numbers next to merged/closed tasks (+X/-Y) represent the number of lines of code added (+) or removed (-) across your entire codebase <a class="yt-timestamp" data-t="00:17:23">[00:17:35]</a>.

## Why Use Codeex as a Non-Technical Person?

While potentially overwhelming initially, [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] offers a unique approach to interacting with code <a class="yt-timestamp" data-t="00:11:00">[00:11:06]</a>:
*   **Focus on Task, Not Code**: You primarily focus on stating the task you want to achieve, rather than looking at or thinking about the actual code <a class="yt-timestamp" data-t="00:12:16">[00:12:19]</a>.
*   **Iterative Development**: It promotes an iterative approach to building, where you add small pieces of functionality, and each addition is technically checked and tested <a class="yt-timestamp" data-t="00:14:49">[00:14:59]</a>. This reduces time spent debugging <a class="yt-timestamp" data-t="00:14:07">[00:14:10]</a>.
*   **Delegated Coding**: It feels like delegating tasks to a highly advanced agent, freeing you from the manual coding <a class="yt-timestamp" data-t="00:14:51">[00:14:55]</a>.
*   **Mobile Use**: [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] can be used on mobile devices through chat, facilitating constant shipping of changes <a class="yt-timestamp" data-t="00:12:48">[00:12:53]</a>.
*   **Comparison to Text-to-App Builders**: Unlike some text-to-app builders that might create an "overbuilt" UI with "underbuilt" features, [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]]'s iterative method ensures pieces actually work, making it more suitable for deployable applications <a class="yt-timestamp" data-t="00:13:06">[00:13:42]</a>.

## Best Practices and Limitations for Non-Technical Users

*   **Start Simple**: Begin with simple tasks on a personal site or a new, non-critical project <a class="yt-timestamp" data-t="00:18:38">[00:18:43]</a>.
*   **Iterate Gradually**: Focus on adding features "line by line" and "piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:05]</a>. Examples include adding social links or an about section <a class="yt-timestamp" data-t="00:19:44">[00:19:46]</a>.
*   **GitHub Setup**: Always ensure your GitHub repository has at least a README file enabled when creating it <a class="yt-timestamp" data-t="00:19:29">[00:19:34]</a>.
*   **Reverting Changes**: If your site breaks after a merge, you can always revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:20:08">[00:20:20]</a>. There is little risk when working on a personal, non-client-facing site <a class="yt-timestamp" data-t="00:20:28">[00:20:38]</a>.
*   **Leverage External AI**: If you get stuck, use external AI tools like ChatGPT (chat.openai.com) to ask questions about rolling back GitHub changes or understanding code. You can even copy your entire codebase (by changing 'github.com' to 'uithub.com' in the URL to see all raw code) and paste it into ChatGPT for analysis <a class="yt-timestamp" data-t="00:20:47">[00:23:05]</a>.
*   **Limitations of Codeex**:
    *   Cannot directly upload files or images <a class="yt-timestamp" data-t="00:20:58">[00:21:00]</a>.
    *   Cannot directly make UI look like a specific design without external tools like VZero <a class="yt-timestamp" data-t="00:21:01">[00:21:04]</a>.

## Advanced Scenarios (Beyond Basic HTML/CSS)

While the focus is on simpler modifications, [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] can interact with more complex codebases:
*   **Complex Projects**: For projects involving databases, authentication, or frameworks like Next.js or Python, you might need to use the "Codeex execution" feature <a class="yt-timestamp" data-t="00:28:02">[00:28:22]</a>.
*   **Terminal Commands**: This involves running terminal commands (e.g., `pmpm install`, `pmpm dev`) within [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to spin up servers and dependencies necessary for the application to function <a class="yt-timestamp" data-t="00:28:30">[00:29:16]</a>.
*   **Environments**: In [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]], "environments" are used to connect to different GitHub repositories or projects, allowing [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to interact with and write code to specific locations <a class="yt-timestamp" data-t="00:27:22">[00:27:31]</a>.

### Learning Curve
Using [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] serves as a "lightweight way to learn how to code" <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>. It introduces fundamental computer science and development terminology in a more engaging manner than traditional coding <a class="yt-timestamp" data-t="00:32:20">[00:32:26]</a>. By dealing with concepts like GitHub, branches, and pull requests, users gain exposure to the software development workflow <a class="yt-timestamp" data-t="00:32:05">[00:32:08]</a>. The iterative, task-based UI of [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] is likely a precursor to how many future AI-powered building tools will operate <a class="yt-timestamp" data-t="00:32:50">[00:32:55]</a>.