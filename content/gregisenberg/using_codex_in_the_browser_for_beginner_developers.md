---
title: Using Codex in the Browser for Beginner Developers
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codex is presented as an "AI engineer in the browser" designed to assist users in coding tasks <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While some might consider it suitable for senior engineers <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, it's also introduced as a tool that non-technical individuals can use to "get the most of it" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Ben Tossel, known for explaining [[differences_between_codeex_and_no_code_tools | no-code tools]] to non-technical users, provides a tutorial on its application <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## What is Codex?

Essentially, Codex functions as a platform where users can describe a task, and it will generate the necessary code and push it to GitHub <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It connects to your GitHub repository and can work on your main branch <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Getting Started: Setting Up with GitHub

To use Codex, you need to have GitHub connected <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Understanding GitHub Basics
GitHub serves as a storage for your code <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Repositories (repos)**: These are your projects, storing all code files <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Commits**: Any changes you make to the code are recorded as commits <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Branches**: Code is often managed on "branches," with the "main branch" being the primary line of code. When working on new features, it's standard practice to create a new branch, work on it, and then merge it back into the main branch if successful <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This ensures your main code remains stable <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

### Creating a GitHub Repository
To start a new project (like a personal site or marketing site), you need to create a new repository <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
1.  Choose a name for your repository <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  Decide if it should be public or private <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
3.  Add a README file, which explains what your project does <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
4.  Create the repository <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Initializing a Website with Codex
You can start a website from scratch using Codex. One method demonstrated involves taking the page source from an existing [[differences_between_codeex_and_no_code_tools | no-code builder]] (like Card) and instructing a coding agent to put that code onto your GitHub repository <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Deploying Your Site
Once your code is on GitHub, you can deploy it to make it live:
*   **GitHub Pages**: Allows you to have a live URL and custom domains <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   [[using_vercels_v0_for_web_development | Vercel]]: Another deployment option, used for more advanced needs <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Using Codex for Tasks

Once your website is live and connected, you can use Codex to make changes.
1.  **Add a Task**: Type your desired change as a task in Codex (e.g., "add another tab next to investments tools that is called food I like in the dock put tacos") <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Generate Code**: Click "code" to have Codex generate the code for your task <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  **Review Task Progress**: Codex will show its progress, including which files it's examining and the actions it plans to take (e.g., creating a new document, updating the main site) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. It also provides information on how many lines of code were added or removed <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
4.  **Create a Pull Request (PR)**: After Codex finishes the task, you'll see a button to "Create new PR" <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A pull request proposes the changes to be merged into your main code <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
5.  **Merge the PR**: If there are "no conflicts with the base branch" and "all checks have passed," you can merge the pull request <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Merging integrates the new code into your main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. The site will then deploy the changes, which may take a few seconds <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Managing Tasks: Merged vs. Closed
*   **Open**: A task begins as "open" when you create it <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Merged**: Means the changes have been successfully integrated into your main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Closed**: If a task's output (like a generated feature) isn't satisfactory or breaks something, you can close the pull request, effectively denying the changes <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This is like closing a support ticket for a problem that couldn't be resolved <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Why Use Codex as a Beginner Developer?

While other prototyping tools exist, Codex offers a unique approach for beginners:
*   **Focus on Iteration, Not Deep Code**: Users don't need to directly look at or understand the code much. The process is iterative: add a task, check if it works, and move on <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Built-in Checks**: Codex includes tests and checks to ensure code stability, reducing time spent on debugging <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. If something fails, you can give Codex another task or try a different coding agent <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Delegated Tasks**: It feels like delegating tasks to a more advanced entity, rather than doing the coding yourself <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Learning Terminology**: [[introduction_to_chatgpt_codex_for_nontechnical_users | Using Codex]] is a lightweight way to learn computer science and development terminology in a more engaging way <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>.
*   **Foundation for AI Building**: Familiarity with Codex can make you better at building with [[ai_tools_in_web_design_and_development | AI tools]] in general <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.

## Best Practices for Non-Technical Users

*   **Start Simple**: Begin with a personal site or create a new one if you're concerned about your existing site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Gradually**: Make small, line-by-line changes. Examples include adding a food tab, removing text animation, adding keyboard shortcuts, or a dark/light mode switcher <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Ensure a Readme**: When creating a GitHub repository, always enable the README file <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Experiment**: Play around with merging and closing tasks <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Don't Fear Mistakes**: If your site breaks after a merge, you can always revert to a previous version on GitHub <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. There's "no real danger" for a personal site <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Seek External Help**: If you get stuck, use ChatGPT or other large language models to ask questions like "how do I roll back this GitHub stuff?" <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can even copy all your site's code from GitHub (by changing the first letter of GitHub to 'u' in the URL to `uit hub`) and paste it into ChatGPT for analysis <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

### Limitations of Codex for Beginners
*   **File Uploads**: You cannot upload files or images directly <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   **UI Design**: It's challenging to ask Codex to "make the UI look like this" <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. For design, you might use other tools like [[using_vercels_v0_for_web_development | Vercel's v0]] and then bring that code into Codex or deploy it on GitHub <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Advanced Functionality**: Dealing with databases or authentication is several steps up in complexity <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. For building apps with frameworks like Next.js or Python, you might need to use the "code execution" feature to run terminal commands (like `pmpm install`) to spin up servers <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

## Next Steps for Learning
1.  **Level 1: Personal Site**: Start by building a personal site and adding small features <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
2.  **Level 2: Integrations**: Try adding simple integrations, such as pulling the latest information from GitHub into your site <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
3.  **Level 3 & 4 (Advanced)**: Explore user sign-in/sign-up, bookmarking features, database layers, and integrating [[ai_tools_in_web_design_and_development | AI components]] <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

The open-source nature of GitHub provides many repositories you can fork and adapt using Codex <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.

Ultimately, Codex offers a path to learning coding concepts and building functional websites without writing traditional lines of code, by delegating complex tasks to an AI <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. It's a stepping stone that introduces fundamental development workflows in a less intimidating way compared to [[developing_app_functionality_with_no_coding_experience | text-to-app builders]] that might create complex but non-functional features initially <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.