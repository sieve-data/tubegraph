---
title: Introduction to ChatGPT Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codeex is OpenAI's new AI engineer in the browser, developed by Sam Altman and OpenAI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It functions as a tool where users can type in a task, and it will code it for them, then push the changes to [[GitHub and Codex Integration | GitHub]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is particularly useful for [[NonTechnical People Learning Code with Codex | non-technical people]] to get the most out of coding <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## How Codeex Works

Codeex allows users to interact with their codebase without directly viewing or thinking about the code itself <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. Instead, users provide tasks, and Codeex generates the necessary code and integrates it <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

### Integration with GitHub

Codeex requires a connection to a GitHub repository to function <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

*   **GitHub** is a platform for storing code <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Projects are stored as "repositories" (repos) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Creating a Repository**: To start a project like a personal or marketing site, users need to create a new repository, give it a name, and can choose to make it public or private <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Adding a `README` file explains the project's purpose <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Commits**: Any changes made to the code are recorded as "commits" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Codeex can perform these commits automatically <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **GitHub Pages**: Users can connect their GitHub repo to GitHub Pages to host their website live with a custom URL <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Workflow Example: Adding a New Tab

1.  **State the Task**: Type the desired change, for example, "add another tab next to investments tools that is called food. I like in the dock. Put tacos" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  **Generate Code**: Click "code" to have Codeex generate the code <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Codeex will analyze existing files and plan its actions, such as creating new documents and updating the main site <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
3.  **Review Changes**: Codeex shows which files were changed and how many lines of code were added or removed <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>, <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
4.  **Create a Pull Request (PR)**: To apply changes, click "Create new PR" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   A **pull request** is a proposal to merge changes from a separate "branch" (a copy of the code where new features are worked on) back into the "main branch" (the primary codebase) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   Codeex performs tests to ensure no conflicts exist <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
5.  **Merge the PR**: If all checks pass and there are no conflicts, the PR can be merged <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Merging integrates the new code into the main codebase, making it part of the live site <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
6.  **Deployment**: After merging, the changes are deployed, making them visible on the live site <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

*   **Open**: A task starts as "open" when created <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Closed**: If a proposed change is deemed unsatisfactory or problematic (e.g., checks fail), the pull request can be "closed," discarding the changes without affecting the main code <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>, <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

## Why Use Codeex?

While initially overwhelming for [[NonTechnical People Learning Code with Codex | non-technical people]] compared to prototyping tools, Codeex offers distinct advantages:

*   **Focus on Outcome, Not Code**: Users describe what they want to achieve, and Codeex handles the underlying code, abstracting away technical complexity <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Iterative Building**: It promotes an iterative approach to building. New features are added piece by piece, with built-in tests and checks to minimize bugs and debugging time <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>, <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   **Delegation**: Codeex acts like an advanced assistant, taking "to-dos" and executing them in a delegated fashion <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   **Mobile Functionality**: Tasks and updates can be managed quite easily on mobile via chat <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Learning Aid**: Codeex can introduce [[NonTechnical People Learning Code with Codex | non-technical people]] to computer science and development terminology in a lightweight and fun way <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. It drip-feeds coding concepts <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.
*   **Reduced Debugging**: Compared to text-to-app builders that create complex but non-functional UI, Codeex's iterative approach means less time spent debugging <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>, <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Limitations

*   **File Uploads**: Codeex cannot upload files or images directly <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **UI Design from Prompts**: It cannot directly "make the UI look like this" <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. Users might need to use other tools like V0 to generate design code and then bring it into Codeex <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Environment Setup**: Setting up environments (connecting different repos) is not always intuitive <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## Best Practices for Beginners Using Codeex

*   **Start Simple**: Begin with basic tasks on a personal site or a new, non-critical personal site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   Examples: "make a website with my name as the header," "create an about section," "add some social links" <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Ensure GitHub Setup**: Have a GitHub repo ready with at least a `README` file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Iterate Small**: Add features line by line, piece by piece <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>, <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   **Don't Fear Mistakes**: If a merge breaks the site, it's possible to revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. For personal sites, the risk is low <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Use [[Using ChatGPT Operator for Business Automation | ChatGPT]] for Questions**: For complex issues or understanding GitHub actions (like rolling back changes), ask [[Increasing ChatGPT effectiveness with a 3step process | ChatGPT]] for guidance <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
    *   A useful trick for [[ChatGPT 40 for generating ads | ChatGPT]] is to change the first letter of "GitHub" to "u" (uit hub) in a repo URL to view all the underlying code, which can then be copied and pasted into [[Comparison between ChatGPT Pro and Perplexity AI | ChatGPT]] for analysis <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

## Next Levels of Learning

Once comfortable with basic personal site modifications, users can explore more advanced concepts:

*   **Integrations**: For example, integrating GitHub to pull in the latest information <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
*   **User Management**: Implementing user sign-in/sign-up functionality <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
*   **Database Interaction**: Working with databases, which are a few steps up in complexity <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>, <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.
*   **AI Piece**: Integrating AI features into the project <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **Open Source Projects**: Experimenting with open-source repositories on GitHub. Users can fork (copy) a project and use Codeex to understand or run the code, though it may require specific terminal commands for more complex frameworks like Next.js or Python <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. This interaction is done via the Codeex execution piece <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

While Codeex is still in early preview and some features are "on the fritz," it offers a promising, less intimidating entry point into coding compared to traditional methods or even some text-to-app builders <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>.