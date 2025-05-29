---
title: Best Practices for Beginners Using Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[Introduction to ChatGPT Codex | Codex]], developed by OpenAI, is an AI engineer in the browser designed to help both technical and non-technical users write and manage code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide provides best practices for beginners, particularly non-technical individuals, looking to leverage [[Introduction to ChatGPT Codex | Codex]] for their projects <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What is [[Introduction to ChatGPT Codex | Codex]]?

[[Introduction to ChatGPT Codex | Codex]] allows users to describe a task in natural language, and it will generate the necessary code, then push it to GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It integrates directly with your GitHub repository, acting as a delegated agent that handles coding tasks <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## Getting Started with [[Introduction to ChatGPT Codex | Codex]]

### Prerequisites: GitHub Setup
To use [[Introduction to ChatGPT Codex | Codex]], you need a GitHub account <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. GitHub is a platform where your code is stored in "repositories" (repos), which are essentially your projects <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

1.  **Create a Repository**: For any project (e.g., a personal site, marketing site), you must create a new repository <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can name it anything, choose public or private, and add a `README` file to describe your project <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  **Populate Your Repository**:
    *   You can start a new project from scratch by asking [[Introduction to ChatGPT Codex | Codex]] to "make a website with my name as the header" <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
    *   Alternatively, if you have an existing site built on a no-code tool (like Card), you can view its page source, copy all the HTML, and use a coding agent (like [[Introduction to ChatGPT Codex | Codex]] itself) to put that code onto your new GitHub repo <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
3.  **Deployment**: Once your code is on GitHub, you can connect it to services like GitHub Pages or Vercel to make your website live with a custom URL <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Core Workflow: Task, Code, Pull Request, Merge

The typical workflow with [[Introduction to ChatGPT Codex | Codex]] involves submitting a task, reviewing the changes, and then integrating them into your project:

1.  **Add a Task**: In [[Introduction to ChatGPT Codex | Codex]], type your desired change as a task, e.g., "add another tab next to investments tools that is called food I like in the dock, put tacos" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   **"Ask" vs. "Code"**: You can hit "Ask" to get information about your code without generating changes, or "Code" to initiate the coding process <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
2.  **Task Execution**: [[Introduction to ChatGPT Codex | Codex]] will process your request, using its terminal to find relevant files and understand the code <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It will propose changes, potentially creating new files or updating existing ones <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
3.  **Create a Pull Request (PR)**: After [[Introduction to ChatGPT Codex | Codex]] completes the task, you'll see a summary of changes (lines added/removed) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. You then create a "pull request" (PR) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   **Branches**: A PR means [[Introduction to ChatGPT Codex | Codex]] has copied your main code (main branch) to a separate "branch" (a side version) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. It makes changes on this branch, ensuring your main codebase isn't affected until you approve <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
4.  **Merge or Close the PR**:
    *   **Merge**: If all checks pass and there are no conflicts, you can "merge" the PR <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This integrates the changes from the branch into your main codebase <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>, <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. Your live site will then update <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   **Close**: If the changes aren't suitable or checks fail, you can "close" the PR <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This discards the changes made on that branch, leaving your main code untouched <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
    *   The numbers next to merged/closed tasks (+/-) indicate the number of lines of code added or removed across your codebase <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## Why Use [[Introduction to ChatGPT Codex | Codex]] as a Non-Technical Person?
While it might seem overwhelming initially, [[Introduction to ChatGPT Codex | Codex]] offers unique benefits for non-technical users:

*   **Iterative Development**: It allows you to add features piece by piece <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Reduced Debugging**: With built-in tests and checks, it minimizes time spent debugging <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. If something breaks, you can give [[Introduction to ChatGPT Codex | Codex]] another task to fix it or try a different coding agent <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Delegated Coding**: You define the "to-do list," and a highly advanced AI does the coding, taking complex tasks off your plate <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Mobile Capabilities**: The ability to manage tasks via chat and mobile makes "shipping" (deploying changes) potentially more frequent <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>, <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
*   **Contrasting with Text-to-App Builders**: Unlike tools that might spit out visually perfect but non-functional apps, [[Introduction to ChatGPT Codex | Codex]] focuses on making the underlying pieces *work*, leading to deployable products <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Best Practices for Beginners

*   **Start Simple**: Begin by using [[Introduction to ChatGPT Codex | Codex]] on your personal site or create a new, non-critical personal site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Small**: Go line by line, piece by piece <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. Examples include adding a food tab, removing text animations, adding keyboard shortcuts, or a dark/light mode switcher <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
*   **Essential GitHub Setup**: Ensure your GitHub repo has at least a `README` file enabled when you create it <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Experiment Freely**: Don't be afraid to merge or close tasks. If a change breaks your site, you can always revert to a previous working version on GitHub <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. There's no real danger if it's a personal, non-client-facing project <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Know Limitations**: [[Introduction to ChatGPT Codex | Codex]] currently has limitations, such as not being able to upload files or images directly, or perfectly replicate a specific UI design <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   **Leverage Other Tools**: For design needs, you can use tools like Vercel or vzero to generate design code and then bring that code into [[Introduction to ChatGPT Codex | Codex]] or GitHub <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Ask for Help (External AI)**: If you get stuck or don't understand terminology (like rolling back GitHub changes), use external AI tools like [[Introduction to ChatGPT Codex | ChatGPT]] (chat.openai.com) <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>, <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
    *   You can copy your entire codebase (e.g., by changing the first letter of github.com to 'u' -> uitub.com to see all code) and paste it into [[Introduction to ChatGPT Codex | ChatGPT]] to ask questions about bugs or improvements <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
    *   [[Introduction to ChatGPT Codex | Codex]]'s internal "Ask" function is limited to its understanding of your repo and doesn't connect to the internet <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

## Next Steps and Learning Progression

After mastering the basics of building a personal site:

*   **Integrations**: Explore pulling in dynamic information, such as integrating with GitHub to display the latest updates <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
*   **User Features**: Try adding user sign-in/sign-up functionality or features like saving/bookmarking items within your product <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
*   **Database Layer**: Advance to implementing a database layer for more complex data management <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.
*   **AI Components**: Integrate AI functionalities into your projects <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **Open-Source Repos**: Leverage the vast number of open-source repositories on GitHub to learn and build upon existing projects <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
    *   To use these, you might "fork" the repo (copy it to your GitHub) <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
    *   More complex open-source projects often require running terminal commands (e.g., `pnpm install`, `pnpm dev`) within a coding environment to get them working <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. [[Introduction to ChatGPT Codex | Codex]] has an "execution" piece for this, but it requires understanding basic development environments and frameworks (like Next.js, Python) <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## [[Introduction to ChatGPT Codex | Codex]] as a Learning Tool

While the terminology surrounding coding (e.g., GitHub, pull requests, branches) can be daunting <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>, [[Introduction to ChatGPT Codex | Codex]] serves as a lightweight and fun way to learn these computer science and development concepts <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>. It drip-feeds coding exposure <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>. By starting with simple tasks and seeing the results, beginners can gain confidence and progressively tackle more complex projects <a class="yt-timestamp" data-t="00:30:22">[00:30:22]</a>. The key is to start small and avoid trying to build an "overbuilt" project like a Spotify clone from the outset, which can lead to overwhelming bugs and discouragement <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.