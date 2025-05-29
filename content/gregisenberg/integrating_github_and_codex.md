---
title: Integrating GitHub and Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[introduction_to_chatgpt_codex | Codex]], OpenAI's AI engineer in the browser, can be integrated with GitHub to streamline code development and deployment <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This integration allows users to describe tasks in natural language, have [[introduction_to_chatgpt_codex | Codex]] generate the code, and then push those changes directly to a GitHub repository <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Understanding GitHub's Role

GitHub serves as a central repository for storing and managing code <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Key concepts include:
*   **Repositories (Repos)**: These act as individual projects, storing all associated code files <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Commits**: Any changes made to the code are "committed," and a history of these commits is maintained <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Branches**: Code is typically organized into branches. The "main branch" is the primary line of code. When working on new features, a new branch is created, allowing changes to be made in isolation before being merged back into the main branch <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Pull Requests (PRs)**: A pull request is a proposal to merge changes from one branch into another, typically from a feature branch into the main branch <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Connecting [[introduction_to_chatgpt_codex | Codex]] to GitHub

To use [[introduction_to_chatgpt_codex | Codex]], you need to have GitHub connected to it <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This involves:
1.  **Creating a Repository**: For a new project (e.g., a personal site or marketing site), you create a new repository on GitHub <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can choose to make it public or private and add a "ReadMe" file to explain the project <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  **Connecting in [[introduction_to_chatgpt_codex | Codex]]**: Within [[introduction_to_chatgpt_codex | Codex]], you connect to your GitHub repository by setting up an "environment" that links to the correct repo <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>. While the "environments" setup might not feel intuitive for [[using_codex_for_nontechnical_people | non-technical people]], it's essentially establishing a connection point for [[introduction_to_chatgpt_codex | Codex]] to read and write code <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>, <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
3.  **Initializing a Project**: You can start a project from scratch with [[introduction_to_chatgpt_codex | Codex]] <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, or import existing code. For example, if you have a site built with a no-code tool like Card, you can copy its page source (HTML/CSS) and use another coding agent (or potentially [[introduction_to_chatgpt_codex | Codex]] itself) to put that code onto your GitHub repo <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
4.  **Deployment**: After connecting to GitHub, you can connect your repository to deployment services like GitHub Pages or Vercel to make your website live <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Workflow: From Task to Deployment

The workflow with [[introduction_to_chatgpt_codex | Codex]] and GitHub for making changes is straightforward for [[using_codex_for_nontechnical_people | non-technical people]]:
1.  **Define a Task**: In [[introduction_to_chatgpt_codex | Codex]], you describe the desired change or addition in natural language, such as "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  **Generate Code**: Click "Code" in [[introduction_to_chatgpt_codex | Codex]] to initiate the process <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. [[introduction_to_chatgpt_codex | Codex]] uses its terminal to analyze your existing code files, understand their structure, and then generates new or updated code to fulfill the task <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  **Review Changes**: [[introduction_to_chatgpt_codex | Codex]] shows you the files it has changed and how many lines of code were added or removed <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>, <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. It might also run its own tests <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
4.  **Create a Pull Request (PR)**: After [[introduction_to_chatgpt_codex | Codex]] completes the task, you create a new PR <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This means [[introduction_to_chatgpt_codex | Codex]] creates a separate branch with your changes <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
5.  **Merge the PR**: On GitHub, you can view the PR, review its summary, and check if all automated checks have passed and if there are no conflicts with the main branch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. If everything looks good, you merge the PR, integrating the new code into your main codebase <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
6.  **Deployment and Verification**: Once merged, the changes are typically deployed to your live site (e.g., via Vercel), allowing you to see the updates <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>, <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

## Managing Changes and Recovering from Issues

*   **Merging and Closing Tasks**: A task in [[introduction_to_chatgpt_codex | Codex]] starts as "open" <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Once a pull request is successfully integrated into the main codebase, the task is marked as "merged" <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. If the generated code isn't satisfactory or if checks fail, you can "close" the pull request, effectively denying the changes without affecting your main code <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>, <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Rollback Capability**: A significant [[benefits_of_codex_for_software_development | benefit]] of using GitHub is the ability to revert to previous versions. If a change breaks your site, you can always go back to an earlier, working commit <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>, <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This minimizes the risk, especially for personal sites not handling client or financial data <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

## [[challenges_and_best_practices_in_using_codex | Best Practices]] for [[using_codex_for_nontechnical_people | Non-Technical People]]

When starting with [[introduction_to_chatgpt_codex | Codex]] and GitHub, consider these [[challenges_and_best_practices_in_using_codex | best practices]]:
*   **Start Simple**: Begin by using it on a personal site or create a new, simple personal site for experimentation <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>, <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
*   **Iterate Incrementally**: Add changes line by line, or piece by piece <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. For example, start with a header, then an about section, then social links <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. This iterative approach allows you to verify each change and reduces debugging time <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Don't Fear Experimentation**: Play around with merging and closing tasks <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. The rollback feature in GitHub means there's little danger to your site for personal projects <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   **Leverage AI for Help**: If you get stuck with GitHub-related issues (e.g., how to roll back), ask ChatGPT for assistance <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can even copy all your code from GitHub (by changing `github.com` to `uithub.com` in the URL to view the raw code) and paste it into ChatGPT to ask about bugs or improvements <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

## Limitations and Advanced Usage

While [[introduction_to_chatgpt_codex | Codex]] simplifies many tasks, it has limitations, especially for [[using_codex_for_nontechnical_people | non-technical people]] venturing into more complex projects:
*   **No File Uploads**: [[introduction_to_chatgpt_codex | Codex]] cannot directly upload files or images, nor can it accept design inputs like "make the UI look like this" <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. For design, you might use other tools like v0 to generate design code and then bring it into [[introduction_to_chatgpt_codex | Codex]] via GitHub <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Complex Frameworks and Backend Services**: For projects involving databases, authentication, or frameworks like Next.js or Python, you might need to run specific terminal commands (e.g., `pmpm install`) within a proper coding environment to get the app running and for [[introduction_to_chatgpt_codex | Codex]] to interact with the code properly <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>, <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. These are more advanced use cases beyond simple HTML/CSS/JavaScript <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.
*   **Mobile Experience**: While you can manage tasks on mobile, the experience may not be as optimized as on desktop <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

Ultimately, using [[introduction_to_chatgpt_codex | Codex]] with GitHub provides a lightweight way to learn about coding concepts and terminology like repositories, branches, and pull requests, making the intimidating world of computer science more accessible and fun <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.