---
title: Testing and deploying a website using Codeex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codeex, an AI engineer in the browser from OpenAI, allows users to type in a task, have it coded, and then pushed to GitHub <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This tool is designed to help users, including non-technical individuals, [[using_codeex_to_automate_coding_tasks | automate coding tasks]] and deploy websites <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Connecting and Setting Up Your Project

To begin using Codeex for web development, you need to connect it to your GitHub repository <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. GitHub serves as a storage location for your code, where projects are organized into "repositories" <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### GitHub Repositories

Changes made to your code are recorded as "commits" in GitHub <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. When creating a new website or marketing site, you must first create a new repository on GitHub <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can name it, set it to public or private, and add a README file to explain the project <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

A website can be initially built using Codeex itself <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Alternatively, if you have an existing site built on a no-code tool like Card, you can copy its page source code and use a coding agent to convert it into code and place it on a GitHub repository <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Deployment Options

Once your code is on GitHub, you can connect it to services like GitHub Pages for a live URL and custom domains <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Another option for deploying applications is [[deploying_applications_using_vercel | Vercel]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Making Changes and Deploying

With Codeex, you can instruct it to add or change elements on your website <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Task Execution

1.  **Input Task**: Provide a task description, e.g., "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **Generate Code**: Click "code" to have Codeex generate the necessary code <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  **Process**: Codeex analyzes files, understands the existing code, creates new documents (e.g., for "food I like"), and updates main site files to match the style <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It uses the terminal to find files and understand code <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
4.  **Testing**: Codeex can perform its own tests <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. While useful for technical users, this feature might be less relevant for simple workflows <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### Pull Request and Merging

After Codeex completes a task, the changes are not immediately live <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. You must create a "pull request" (PR) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Branches**: Code is managed in "branches," with the "main branch" being the primary version <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. When you work on a new feature, a separate branch is created, acting as a copy of the main code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Merging**: If the feature is successful and has no conflicts with the main codebase, you can "merge" it back into the main branch <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Deployment**: After merging, the changes will deploy, and you'll be able to see them on your live site <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Managing Codeex Tasks

Codeex tasks have different statuses:
*   **Open**: A task is "open" when it's initially created and being worked on <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Merged**: The task's changes have been successfully integrated into the main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Closed**: If changes are undesirable or break the site, you can close the pull request, denying the merge <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This ensures your main code remains unaffected as changes were made on a separate branch <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Lines of Code Changed**: Next to merged or closed tasks, you'll see positive and negative numbers indicating the lines of code added (+) or removed (-) across the entire codebase <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

## Best Practices and Limitations for Non-Technical Users

For non-technical users, Codeex offers a lightweight way to learn about coding and development terminology <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.

### Getting Started

*   **Start Simple**: Begin by using Codeex on your personal website or create a new one to avoid being overly cautious with an existing site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **GitHub Setup**: Ensure you have a GitHub repository with at least a README file enabled during creation <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Iterate**: Progress line by line and piece by piece. Start with basic tasks like "make a website with my name as the header," then "create an about section," and "add some social links" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Experiment**: Play around by merging and closing tasks <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Rollback**: If a change breaks your site, GitHub allows you to revert to a previous, working version <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. This means there's no significant risk when working on a personal, non-client-facing site <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

### Codeex Limitations

*   **File Uploads**: Codeex currently does not support uploading files or images <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **UI Design**: It cannot directly make the UI "look like this" <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. For design elements, you might use other tools like v0 to generate design code and then bring that into Codeex or deploy it via GitHub <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Advanced Usage and Troubleshooting

*   **Environments**: When working with more complex projects, such as those with frameworks like Next.js or Python, you might need to create and manage different "environments" in Codeex to connect to the correct repositories <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.
*   **Terminal Commands**: For Codeex to properly interact with and understand your code, you may need to run terminal commands (e.g., `pmpm install`) within Codeex's execution environment to spin up servers and necessary components <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   **External AI Help**: If you get stuck or encounter bugs, you can ask external AI tools like ChatGPT for help <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. You can copy your entire codebase (e.g., from `uithub.com` instead of `github.com` for a raw text view) and paste it into ChatGPT to ask for bug fixes or explanations <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

### Progression and Future

While Codeex is currently in early preview <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, it provides a unique way to interact with coding. Rather than starting with complex projects like a Spotify clone, which often have underbuilt features that don't work <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, Codeex allows for iterative development where tests and checks are theoretically in place <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This approach can lead to less time spent debugging <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

The experience of using Codeex is described as feeling delegated, like setting a to-do list for an advanced agent to complete <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. While tools like [[design_and_deployment_with_bolt | Bolt]] and Lovable exist for prototyping, Codeex offers a pathway to learning development and computer science terminology in a more engaging way <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. It drip-feeds the coding experience, making the process of [[simplifying_the_coding_and_deployment_process | simplifying the coding and deployment process]] less intimidating <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.