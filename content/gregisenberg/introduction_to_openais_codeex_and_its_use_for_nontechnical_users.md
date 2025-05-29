---
title: Introduction to OpenAIs Codeex and its use for nontechnical users
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

OpenAI's Codeex is a new AI engineer in the browser designed to help users, including non-technical individuals, manage and generate code <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This tool aims to simplify the coding process by allowing users to describe tasks in plain language, which Codeex then translates into functional code <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Ben Tossel, known for explaining no-code tools to non-technical people, highlights Codeex as a way to engage with coding without needing deep technical knowledge <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## What is Codeex?

Codeex is described as a tool where a user can type in a task, it codes the task for them, and then pushes the changes to GitHub <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Its user interface is distinct, focusing on a task-based approach rather than direct code interaction for the user <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. While users will see code, the intention is that they "don't look at the code or think about the code at all" <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

## Getting Started with Codeex

To begin using Codeex, particularly for creating or modifying a website, it is necessary to connect it to GitHub <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Understanding GitHub for Non-Technical Users
GitHub serves as a storage platform for code, organizing projects into "repositories" (repos) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Each repository stores all the code files for a project <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Changes made to the code are recorded as "commits" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

To start a new project:
1.  Create a new repository on GitHub <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
2.  Give it a name and choose if it's public or private <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
3.  Optionally, add a `README` file to explain the project <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Initial Website Setup
One approach for setting up a website with Codeex is to migrate an existing site from a no-code builder (like Card) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This involves:
1.  Viewing the page source of the existing website <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  Copying all the code <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
3.  Using a coding agent (like Codeex or another tool) to put this code into the newly created GitHub repository <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Deployment
Once the code is on GitHub, it needs to be deployed to be live on the internet. Options include:
*   **GitHub Pages:** Allows the URL to be live with custom domains <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Vercel:** A more advanced deployment platform <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Using Codeex: A Live Tutorial Example

To demonstrate, a user can instruct Codeex to add a new tab called "food I like" with "tacos" listed within it, next to existing "investments tools" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### "Ask" vs. "Code"
Codeex offers two main modes:
*   **Ask:** Provides information about your code without generating new code <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Code:** Generates code based on the given task <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Monitoring Task Progress
Once a task is submitted (e.g., "add another tab..."), Codeex lists it as a new task <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Users can see the history of past tasks, including how many lines of code were added or removed <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. While processing, Codeex uses terminal commands to understand and modify the codebase <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It will describe its plan, such as creating a new document, updating the main site, and matching styles <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Understanding Code Changes and Pull Requests
When a task is completed by Codeex, it shows which files have been changed, indicating lines added and removed <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

[[practical_applications_and_stepbystep_guide_of_codeex_for_website_modifications | To apply these changes, the user must create a new Pull Request (PR)]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Branches:** Code is typically managed in "branches." The "main branch" is the primary version <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. When working on new features, a separate branch is created as a copy <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Pull Request:** A PR is a proposal to merge changes from a separate branch back into the main branch <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Codeex provides a summary of changes <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. If "all checks have passed" and there are "no conflicts with the base branch," the changes can be merged <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **"Merged" vs. "Closed":**
    *   **Merged:** The changes have been successfully incorporated into the main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
    *   **Closed:** The proposed changes were denied or discarded without being merged <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This allows experimentation without affecting the main site <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

After merging a PR, the website will deploy the changes, making them live <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. For the example, the "food I like" tab and its content successfully appeared on the live site <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

## Why Use Codeex as a Non-Technical User?

While Codeex might seem overwhelming initially, it offers unique advantages for non-technical users:

*   **Delegated Coding:** The user provides a task, and Codeex, as an "advanced" agent, handles the coding <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This feels like delegating a task off your plate <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Focus on Iteration:** Codeex supports an iterative building process, where features are added piece by piece <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Built-in tests and checks help ensure functionality, reducing time spent debugging <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Mobile Accessibility:** It is possible to interact with Codeex and manage tasks via mobile chat, making it highly accessible <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Avoidance of Overbuilt Tools:** Unlike some "text-to-app builders" that create visually perfect but functionally broken applications, Codeex focuses on ensuring the underlying pieces work correctly before deployment <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   [[considerations_for_learning_to_code_using_aidriven_tools_like_codeex | Lightweight Introduction to Coding Concepts]]: Codeex introduces users to development terminology and computer science concepts in a more accessible and fun way <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>. It "drip feeds" coding knowledge rather than overwhelming users from the start <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>. This allows users to experience the outcome of coding without writing the code themselves <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.

## Challenges and Limitations for Non-Technical Users

*   **Overwhelming Terminology:** Concepts like GitHub, repositories, branches, and pull requests can initially feel like a "behemoth" to non-technical users <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Setup Complexity:** The process of setting up environments or connecting new repositories might not feel intuitive <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.
*   **Limited UI Control:** Codeex does not allow users to upload files, images, or directly specify UI design ("make the UI look like this") <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. For design elements, other tools like Vercel (v0) might be needed <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Early Preview Instability:** As an early preview tool, tasks might break after around 30 minutes <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Terminal Commands for Advanced Frameworks:** For projects using frameworks like Next.js or Python, users might need to manually input terminal commands (e.g., `pnpm install`) in the Codeex execution environment, which can be daunting for non-technical individuals <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

## Best Practices for Non-Technical Users

For those new to Codeex and coding, Ben Tossel recommends:
*   **Start Simple:** Begin by using Codeex on a personal website or creating a new one specifically for experimentation <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   **Iterate Piece by Piece:** Add features gradually, like creating a website with a name as the header, then an about section, and finally social links <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Ensure GitHub Setup:** Make sure to have a GitHub repository connected, ideally with at least a `README` file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Embrace Experimentation:** Don't be afraid to merge or close tasks <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. GitHub allows rolling back to previous versions if changes cause issues <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. There's "no real danger" for personal, non-client-facing sites <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Utilize External LLMs for Help:** If stuck, ask a chatbot like ChatGPT for help with GitHub issues or understanding code. You can even copy the entire codebase (from `uithub.com` link) into ChatGPT for analysis <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   [[steps_for_transitioning_from_consumer_to_ai_coder | Cultivate Curiosity]]: The key is to be "curious enough to go past those barriers" of initial complexity <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **Manage Expectations:** Avoid setting yourself up for failure by attempting complex projects like a "Spotify clone" initially, as these often lead to overwhelming bugs <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

## Future Outlook and Learning with Codeex

The future of AI coding tools suggests that processes like creating and merging pull requests might become fully automated <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. While Codeex is primarily focused on front-end website modifications, future iterations or other tools might integrate advanced features like database interactions or user authentication <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

The open-source nature of many projects on GitHub means users can explore and fork (copy) existing codebases, using tools like Codeex to understand and modify them <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. This hands-on approach, even if assisted by AI, can deepen understanding of how apps are built <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

Codeex is seen as a valuable starting point for learning about coding in the age of AI <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. While it may not be an everyday tool for non-technical users, it serves as an excellent learning project to familiarize oneself with development concepts and processes <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. The iterative and task-based UI of Codeex could become a standard in future AI-driven development environments <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.