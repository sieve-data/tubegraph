---
title: Using Codex for Nontechnical People
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

OpenAI's new AI engineer in the browser, Codex, offers a unique way for non-technical individuals to interact with and generate code <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This tool is designed to translate natural language tasks into functional code, making software development more accessible <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Ben Tossell, renowned for explaining [[nocode_automation_tools | no-code tools]] to non-technical audiences, provides a live tutorial on how to leverage Codex effectively <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What is Codex?

Codex is an AI tool that allows users to type in a task, which it then codes and pushes to GitHub <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Its core function is to generate code based on a description, serving as an "AI engineer in the browser" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started with Codex

For non-technical users, setting up Codex involves understanding and utilizing GitHub <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### GitHub Fundamentals

GitHub is a platform where code is stored and managed <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Repositories (Repos)**: These are essentially your project folders, storing all code files <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. For example, a personal website would be a repository <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Commits**: Any changes made to the code are recorded as "commits" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Branches**: Code often exists on a "main branch" <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. When working on new features, a new "branch" is created as a copy, allowing isolated development <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Pull Requests (PRs)**: After working on a feature in a branch, a pull request is created to propose merging the changes back into the main branch <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. If there are no conflicts, the changes can be merged <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Creating a New Repository**: To start a new project (e.g., a personal or marketing site), you must create a new repository on GitHub, naming it and deciding if it's public or private <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Including a README file, which explains the project, is recommended <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Initial Website Setup

A website can be created from scratch with Codex or by importing existing code <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. One method involves building a site on a [[nocode_automation_tools | no-code builder]] like Card, then viewing the page source (the underlying code), copying it, and using a coding agent (like Codex) to put it into a GitHub repository <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Deployment

After setting up a GitHub repository, users can connect it to services like GitHub Pages or Vercel to make their website live with a custom URL <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## How to Use Codex: A Practical Example

To make changes to a live website, users can submit tasks to Codex <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

1.  **Adding a Task**: Type a clear command, such as "add another tab next to investments tools that is called food. I like in the dock. put tacos" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
2.  **"Ask" vs. "Code"**:
    *   The "Ask" button provides information about the code without generating new code <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   The "Code" button initiates the code generation process <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  **Monitoring Progress**: Codex will display its actions, such as analyzing files and outlining its plan (e.g., creating a new document, updating the main site) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. It also performs internal tests <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
4.  **Reviewing Changes**: Once complete, Codex shows which files were changed and how many lines of code were added or removed <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. For example, adding a "food I like" tab involved adding a button and the food content in relevant files <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
5.  **Creating a Pull Request (PR)**: After the task is coded, click "Create new PR" to propose the changes to the main codebase <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
6.  **Merging the PR**: On GitHub, check the pull request summary. If all checks pass and there are no conflicts with the base branch, the PR can be merged <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
7.  **Seeing Live Changes**: After merging, the changes deploy, and the updated site becomes visible <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Why Use Codex as a Non-Technical Person?

Despite the initial learning curve, Codex offers several advantages for non-technical users:

*   **Delegated Development**: It allows users to create a "to-do list" for the AI, with the actual coding work delegated to a more advanced entity <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. This feels like having a task done "off your plate" <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Iterative Building**: Codex promotes an iterative approach to building <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Features are added piece by piece, with technical tests and checks ensuring functionality <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This reduces time spent debugging issues <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Focus on Functionality**: Unlike some text-to-app builders that might generate a visually perfect UI but with broken functionality, Codex focuses on making the underlying pieces work correctly <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **Accessibility**: Codex tasks can be managed on mobile via chat <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Simplified Coding Process**: Users don't need to look at or think about the code directly <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The process boils down to adding a task, checking if it worked, creating a pull request, and merging <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Learning Aid**: Playing with Codex can serve as a lightweight introduction to computer science and development terminology <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. It "drip feeds" coding concepts <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.

## Challenges and Limitations

Despite its benefits, Codex has challenges for non-technical users:

*   **Overwhelming Terminology**: Concepts like GitHub, repositories, branches, and pull requests can feel daunting at first <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Limited Direct UI Control**: Codex cannot directly upload files or images, nor can it accept commands like "make the UI look like this" <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. Users might need other tools for design generation <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Task Durability**: In its early preview, tasks might break after about 30 minutes <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **Complex Project Setup**: For projects involving frameworks like Next.js or Python, users might need to interact with terminal commands (e.g., `pmpm install`) to spin up servers and make the app work <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. This requires understanding concepts beyond simple HTML/CSS/JavaScript <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.

## [[challenges_and_best_practices_in_using_codex | Best Practices]] for Non-Technical Users

For non-technical individuals looking to experiment with Codex:

*   **Start Simple**: Begin with a personal website or create a new, non-critical personal site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Use GitHub**: Ensure you have a GitHub repository with at least a README file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Iterate Small**: Add changes "line by line and piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. Examples include adding a header, an about section, or social links <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   **Embrace Experimentation**: "Play around with everything and just merge stuff, close stuff" <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. There's minimal risk for personal, non-client-facing sites <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Leverage Version Control**: If a change breaks the site, you can always revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
*   **Ask for Help**: Use ChatGPT for explanations on technical concepts, such as how to roll back GitHub changes <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. When using ChatGPT, you can copy the entire code from your GitHub repository (by changing the first letter of GitHub to 'u' in the URL to view the raw code) and paste it into ChatGPT for analysis <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
*   **Explore Open Source**: GitHub hosts many open-source repositories that can be cloned and adapted <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. Users can fork (copy) these projects and try to get them running in Codex <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
*   **Understand Environments**: In Codex, "environments" are different connections to repositories where code is written <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>. While not always intuitive, they allow linking to different projects <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## Future Outlook

Codex, and similar tools, are changing how people interact with code. While it might feel overwhelming initially due to [[technical_standards_and_protocols_in_programming_and_apis | terminology]], it provides a lightweight and engaging way to learn about development <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. The iterative approach of Codex, focusing on working features rather than superficial UI, makes it a potentially better starting point for beginners than text-to-app builders that might create complex but non-functional applications <a class="yt-timestamp" data-t="00:34:13">[00:34:13]</a>. The ongoing development of AI agents suggests that even tasks like merging pull requests may become fully automated <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, further simplifying the process for non-technical users.