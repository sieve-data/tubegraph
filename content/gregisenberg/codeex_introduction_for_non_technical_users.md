---
title: Codeex introduction for non technical users
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codeex is a new AI engineer in the browser from Sam Altman and OpenAI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article provides an introduction to Codeex for [[nontechnical_users_using_ai_tools | non-technical people]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, explaining how to use it to its fullest potential <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is Codeex?
Codeex is effectively a way to type in a task, have it code the solution for you, and then push it to GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It's an AI tool that allows users to interact with code without needing to understand the underlying technical details <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

## [[integrating_github_with_codeex | Integrating GitHub with Codeex]]
To use Codeex, you need to have GitHub connected <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. GitHub is a platform where your code is stored <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Key GitHub Concepts
*   **Repositories (Repos)**: These are essentially your projects, storing all your code files <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Commits**: Any changes you make to your code are recorded as "commits" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Branches**: Code is typically managed on "branches." The "main branch" is the primary version of your code <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. When you work on a new feature, you create a new branch, copy the code, work on the feature, and then merge it back into the main branch if successful <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Pull Request (PR)**: A pull request is created when you want to propose changes from your branch to be merged into the main branch <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. If there are no conflicts, the changes can be merged <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

For a new project like a personal or marketing site, you need to create a new repository <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can name it anything and choose whether it's public or private, optionally adding a README file to explain the project <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

Codeex can be used to create the initial website from scratch, or you can import existing code, such as by copying the page source from a no-code builder like Card <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## [[simplifying_the_coding_and_deployment_process | Simplifying the Coding and Deployment Process]] with Codeex
The core workflow in Codeex involves adding a task, letting Codeex generate the code, and then pushing those changes <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Step-by-Step Example: Adding a Tab
1.  **Define the Task**: Type your request, e.g., "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Generate Code**: Click "code" in Codeex <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Codeex will then analyze the existing files and code to understand the changes needed <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It will create new documents or update existing ones to match your request <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  **Review Changes**: Codeex shows which files were changed and how many lines of code were added or removed <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
4.  **Create Pull Request (PR)**: After Codeex finishes, you create a new PR <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
5.  **Merge Changes**: In GitHub, you can review the PR. If all checks pass and there are no conflicts, you can merge it into your main branch <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
6.  **Deployment**: Once merged, the changes deploy and become visible on your live site <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

> [!info] Understanding "Merged" and "Closed"
> *   **Merged**: This means the changes have been successfully incorporated into your main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
> *   **Closed**: If you create a task and review the changes, but they don't work or are unsatisfactory, you can simply close the pull request, effectively denying the changes <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This ensures your main code remains unaffected because the work was done on a separate branch <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
> *   **Lines of Code Changed**: The numbers next to merged or closed tasks (+12, -0) indicate the number of lines of code added (+) or removed (-) across your entire codebase <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## [[benefits_and_limitations_of_codeex_for_beginners | Benefits and Limitations of Codeex for Beginners]]
While Codeex might initially feel overwhelming to a non-technical person compared to prototyping tools <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, it offers unique advantages for [[nontechnical_users_using_ai_tools | non-technical users]] interested in coding.

### Benefits
*   **Abstracts Code**: You don't have to look at or think about the actual code <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. You simply define the task, and Codeex handles the implementation <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Iterative Development**: It allows for iteratively adding features, with built-in tests and checks to minimize debugging time <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Delegation**: It feels like delegating tasks to a more advanced entity, freeing you from doing the actual coding <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   **Mobile Accessibility**: The ability to interact with Codeex and manage tasks via chat makes it accessible even on mobile devices <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Learning Aid**: Codeex can serve as a lightweight way to learn about computer science and development terminology in a fun manner, making you better at [[creating_digital_products_without_coding | building with AI]] <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.

### Limitations
*   **No File Uploads**: You cannot upload files or images directly to Codeex <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **Limited UI Design**: It cannot directly interpret prompts like "make the UI look like this" <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. For design, you might use other tools like vzero and then bring the generated code into Codeex <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Early Preview Instability**: As an early preview, tasks might break after around 30 minutes <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

## Best Practices for Non-Technical Users
*   **Start Simple**: Begin with a personal site or create a new one if you're concerned about your existing one <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Start by making small, incremental changes, like adding a header, an about section, or social links <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>, <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   **Ensure GitHub Repo**: Make sure you have a GitHub repository set up, at least with a README file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Experiment**: Play around with merging and closing tasks <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **No Real Risk**: For personal, non-client-facing sites, there's no major risk. You can always revert to a previous working version on GitHub if something breaks <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Use External AI for Help**: If you get stuck, ask large language models like ChatGPT how to resolve issues or understand concepts (e.g., "how do I roll back this GitHub stuff?") <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can even copy your entire codebase from GitHub (by changing 'github.com' to 'uithub.com' in the URL) and paste it into ChatGPT to ask for bug analysis <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.

## Advancing with Codeex
After mastering basic personal site tasks, you might explore more complex features. While Codeex can handle basic HTML, CSS, and JavaScript, more advanced applications involving databases or authentication might still require higher-level tools or more technical interaction <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

However, Codeex is ideal for incrementally adding "nice to have" features, like animations, keyboard shortcuts, or light/dark mode switchers, often seen on developer websites <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

Codeex can also be used to get other open-source projects or codebases up and running by defining "environments" and running necessary terminal commands through its execution piece <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.

## Conclusion
Codeex offers a unique entry point for [[nontechnical_users_using_ai_tools | non-technical users]] into the world of coding <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. Despite the initial overwhelming terminology, it provides a "drip-feed" introduction to development concepts like GitHub, pull requests, and deployment <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.

The key is to start with simple, manageable tasks rather than trying to build complex applications from the outset <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. By iteratively building and seeing changes deployed, [[leveraging_ai_tools_for_code_explanation_and_education | Codeex helps users learn about coding]] without writing a single line of code themselves <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>, making the process less scary and more accessible <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.