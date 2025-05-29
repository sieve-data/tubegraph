---
title: Using Codeex to automate coding tasks
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[codeex_introduction_for_non_technical_users | Codeex]], a new AI engineer in the browser from Sam Altman and OpenAI, is designed to automate coding tasks by allowing users to simply type in a task and have the AI code it and push it to GitHub <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It is particularly highlighted as a tool that could benefit non-technical users in interacting with code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Core Functionality
[[Codeex]] enables users to type a task, which it then codes and can push to GitHub <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The user interface allows for a chat-like interaction where tasks are set for an AI agent to complete <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Users don't necessarily need to view or understand the underlying code as [[Codeex]] handles the generation and modification <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

### Integrating with GitHub
A fundamental part of [[Codeex]]'s workflow is its integration with GitHub <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. GitHub is a platform where code is stored in "repositories" (projects) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

Key GitHub concepts explained:
*   **Repositories (Repos)**: Essentially a project that stores all code files <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Users must create a new repository for each project, such as a personal or marketing site <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Commits**: Any changes made to the code are recorded as commits within the repository <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. [[Codeex]] automates these commits <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Branches**: Code is typically managed on a "main branch." When working on a new feature, a "branch" is created, which is a copy of the main code <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This allows for isolated development without affecting the main codebase <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Pull Request (PR)**: After changes are made on a branch, a pull request is created to propose merging these changes back into the main branch <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. [[Codeex]] can create new PRs automatically <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Merging**: If checks pass and there are no conflicts, the changes from the branch can be "merged" into the main codebase, making them live <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Closing**: If a proposed change is deemed undesirable or non-functional during testing, the pull request can be "closed" or denied, preventing the changes from affecting the main code <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

### Example Workflow: Adding a Tab to a Website
1.  **Connect to GitHub**: Ensure [[Codeex]] is connected to your GitHub repository and the specific branch you wish to modify <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
2.  **Define the Task**: Input a clear task, e.g., "add another tab next to investments tools that is called food. I like tacos" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  **Generate Code**: Click the "code" button in [[Codeex]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. [[Codeex]] will then analyze existing files, create new documents for the new section, and update the main site, attempting to match existing styles <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
4.  **Review Changes**: [[Codeex]] displays the files it changed and performs its own tests <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. It shows how many lines of code were added or removed <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
5.  **Create a Pull Request**: Click "Create new PR" to initiate the process of merging changes into the live site <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
6.  **Merge the PR**: On GitHub, verify that all checks pass and there are no conflicts, then merge the pull request <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
7.  **Deploy**: Once merged, the changes are deployed and visible on the live site <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

[[testing_and_deploying_a_website_using_codeex | Deployment]] can be handled via GitHub Pages or services like Vercel <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Benefits for Non-Technical Users
[[benefits_and_limitations_of_codeex_for_beginners | Codeex]] offers several advantages for those without a coding background:
*   **Abstraction of Code**: Users don't need to directly view or manipulate the code <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Iterative Development**: Allows for small, incremental additions to a project, with built-in tests and checks to ensure functionality <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This reduces time spent debugging <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Delegated Tasks**: It feels like delegating tasks to an advanced helper, rather than directly coding <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Mobile Accessibility**: Tasks can be initiated and managed via mobile through chat <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Lightweight Introduction to Coding**: [[Codeex]] can serve as a "drip-feed" introduction to computer science and development terminology, making it less overwhelming than traditional coding <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.
*   **Reduced Debugging**: If something doesn't work, users can simply give [[Codeex]] another task or try a different coding agent <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

## Limitations and Challenges
Despite its benefits, [[benefits_and_limitations_of_codeex_for_beginners | Codeex]] has limitations:
*   **No File/Image Upload**: Users cannot upload files or images directly <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   **Limited UI Design Control**: It cannot directly interpret commands like "make the UI look like this" <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. Other [[nocode_ai_tools_for_workflow_automation | AI tools]] like vzero can be used for design generation and then integrated <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Early Preview**: As an early preview tool, it can be "on the fritz" <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   **Setup Complexity**: Initial setup requires understanding GitHub and creating repositories, which can still be daunting for absolute beginners <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Advanced Environments**: For projects using frameworks (Next.js, Python), users may need to run terminal commands (e.g., `pmpm install`) within [[Codeex]]'s execution environment, which requires more technical understanding <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   **Mobile Experience**: While possible on mobile, it may not be ideal for complex tasks <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

## Best Practices for Beginners
For non-technical users exploring [[Codeex]]:
*   **Start Simple**: Begin by using it for a personal site or create a new, non-critical personal site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Gradually**: Add features line by line and piece by piece, rather than attempting complex projects like a Spotify clone from scratch <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Ensure GitHub Repo**: Have a GitHub repository with at least a README file to begin <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Experiment**: Play around with merging and closing tasks to understand the workflow <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Utilize Rollbacks**: Understand that GitHub allows reverting to previous versions if changes break the site, minimizing risk for personal projects <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
*   **Ask External AI Tools**: When stuck, use tools like ChatGPT (chatgpt.com) to ask questions about GitHub or specific coding issues, even providing full codebases for analysis <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.

## Next Steps and Future Potential
Once comfortable with basic website building, users can explore more complex tasks:
*   **Integrations**: Integrating services like GitHub to pull in live information <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
*   **User Management**: Implementing features like user sign-in/sign-up or bookmarking items <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
*   **Databases**: Working with database layers <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.
*   **[[AI applications for automating tasks | AI Piece]]**: Leveraging the broader [[AI applications for automating tasks | AI ecosystem]] <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **Open-Source Repos**: Exploring open-source repositories on GitHub for mini [[ai_applications_for_automating_tasks | AI tools]] and attempting to run their code using [[Codeex]] environments <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. This represents a more advanced use case requiring understanding of environments and terminal commands <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.

While [[Codeex]] might seem overwhelming initially due to terminology like GitHub, it serves as a lightweight, fun way to learn about computer science and development, ultimately making users better at building with [[ai_coding_workflow_and_challenges | AI]] <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. It's a stepping stone into understanding how code works without the burden of writing it from scratch <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.