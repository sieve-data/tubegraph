---
title: NonTechnical People Learning Code with Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[introduction_to_chatgpt_codex | Codex]] is an AI engineer in the browser developed by Sam Altman and OpenAI, designed to assist with coding tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it's often discussed for senior engineers' workflows, it can also be a valuable tool for non-technical individuals to understand and interact with code <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>.

## What is Codex?
[[using_codex_for_coding_tasks | Codex]] allows users to type in a task, which it then codes and can push to [[github_and_codex_integration | GitHub]] <a class="yt-timestamp" data-t="01:43:03">[01:43:03]</a>. It connects to a user's [[github_and_codex_integration | GitHub]] repository, like a personal website, and enables direct modifications <a class="yt-timestamp" data-t="01:54:33">[01:54:33]</a>. It serves as a middle ground for individuals who are "more technical than a non-technical person and less technical than a technical person" <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>.

## Getting Started with Codex for Non-Technical Users

### Prerequisites
To use [[introduction_to_chatgpt_codex | Codex]], you need a [[github_and_codex_integration | GitHub]] account connected to it <a class="yt-timestamp" data-t="02:57:04">[02:57:04]</a>. [[github_and_codex_integration | GitHub]] is a platform where your code is stored in "repositories," which are essentially projects <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Changes made are recorded as "commits" <a class="yt-timestamp" data-t="03:29:05">[03:29:05]</a>.

To begin:
1.  Create a new [[github_and_codex_integration | GitHub]] repository, making it public or private, and add a README file to explain the project <a class="yt-timestamp" data-t="04:01:07">[04:01:07]</a>.
2.  If you have an existing website built on a no-code tool (e.g., Card), you can copy its page source (HTML, CSS, JavaScript) and use a coding agent to put it into your [[github_and_codex_integration | GitHub]] repository <a class="yt-timestamp" data-t="04:40:08">[04:40:08]</a>. This code can then be deployed using services like [[github_and_codex_integration | GitHub]] Pages or Vercel to make your URL live <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

### Using Codex to Make Changes
Once set up, you can add tasks to [[introduction_to_chatgpt_codex | Codex]]. For instance, to add a new tab to a website, you can simply type the instruction: "add another tab next to investments tools that is called food. I like in the dock put tacos" <a class="yt-timestamp" data-t="02:18:29">[02:18:29]</a>.

The workflow involves:
1.  **Prompting:** Input your task as plain language <a class="yt-timestamp" data-t="06:01:03">[06:01:03]</a>. You can hit "ask" for information or "code" to generate changes <a class="yt-timestamp" data-t="06:10:04">[06:10:04]</a>.
2.  **Code Generation:** [[introduction_to_chatgpt_codex | Codex]] analyzes existing files, understands the code, and then creates or updates necessary documents to fulfill the task <a class="yt-timestamp" data-t="07:22:15">[07:22:15]</a>.
3.  **Reviewing Changes:** [[introduction_to_chatgpt_codex | Codex]] shows how many lines of code were added or removed <a class="yt-timestamp" data-t="06:22:04">[06:22:04]</a>. For example, adding a "food" tab might add two lines to a food document and more to the main website file <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
4.  **Pull Requests (PRs):** To make changes live, you create a "pull request" (PR) <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>. Code is managed in "branches," with the "main branch" being the live version <a class="yt-timestamp" data-t="09:23:04">[09:23:04]</a>. When you work on a new feature, you create a separate branch. If the feature is successful and has no conflicts, it can be "merged" back into the main branch <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.
    *   **Merging:** Means the changes have been successfully integrated into the main codebase <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>.
    *   **Closing:** If a change doesn't work or isn't desired, you can "close" the pull request, denying the change without affecting the main code <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.
    *   The numbers next to merged or closed tasks indicate the number of lines of code added (+) and removed (-) across the codebase <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.

## Why Use Codex as a Non-Technical Person?
While tools like [[building_a_prototype_with_bolt_for_nontechnical_users | Bolt]] might seem less overwhelming initially <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>, [[introduction_to_chatgpt_codex | Codex]] offers unique advantages:
*   **Code Abstraction:** You don't directly look at or think about the code; you interact with it through tasks <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
*   **Iterative Building:** [[introduction_to_chatgpt_codex | Codex]] allows for iteratively adding features, with built-in tests and checks to ensure functionality <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>. This reduces time spent debugging <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.
*   **Delegation:** It feels like delegating tasks to a "way more advanced" entity <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>.
*   **Mobile Accessibility:** It's designed to be usable from a mobile device through chat <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   **Contrast with Text-to-App Builders:** Unlike many text-to-app builders that might create an "overbuilt" UI with "underbuilt" features, [[introduction_to_chatgpt_codex | Codex]] focuses on functional pieces <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

## Best Practices for Non-Technical Beginners Using Codex
[[best_practices_for_beginners_using_codex | Best practices for beginners using Codex]]:
*   **Start Simple:** Begin with a personal site or create a new one to experiment <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.
*   **Iterate Piece by Piece:** Focus on adding one feature at a time, such as a website header, an about section, or social links <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.
*   **GitHub Setup:** Ensure you have a [[github_and_codex_integration | GitHub]] repository with at least a README file <a class="yt-timestamp" data-t="19:29:00">[19:29:00]</a>.
*   **Experiment:** Play around with merging and closing tasks <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.
*   **Leverage GitHub's Version Control:** If a change breaks your site, you can always revert to a previous working version on [[github_and_codex_integration | GitHub]], minimizing risk for personal projects <a class="yt-timestamp" data-t="19:59:00">[19:59:00]</a>.
*   **Ask ChatGPT for Help:** For complex [[github_and_codex_integration | GitHub]] actions, like rolling back code, you can use general ChatGPT (chat.openai.com) <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>. You can even copy all the code from your [[github_and_codex_integration | GitHub]] repository (by changing the first letter of "GitHub" to "u" in the URL, e.g., uit.hub) and paste it into ChatGPT to ask questions about bugs or code <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.
*   **Codex Limitations:** [[introduction_to_chatgpt_codex | Codex]] has limitations; it cannot upload files or images directly, nor can it design complex UIs visually <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>. However, you can use other tools like v0 to generate design code and integrate it via [[github_and_codex_integration | GitHub]] <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.

## Future Learning Paths Beyond a Personal Site
After mastering a personal site, the next levels involve more complex tasks:
*   **Databases and Authentication:** Working with databases or user sign-in/sign-up features are significant steps up <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.
*   **Open-Source Projects:** Explore open-source repositories on [[github_and_codex_integration | GitHub]] for inspiration or to contribute <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>. You can "fork" (copy) a repository to your own [[github_and_codex_integration | GitHub]] account <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.
*   **Environments and Terminal Commands:** For more advanced projects using frameworks (Next.js, Python), you'll need to use [[introduction_to_chatgpt_codex | Codex]]'s "environments" feature to connect to different repositories and run terminal commands (e.g., `pmpm install`, `npm run dev`) to set up servers and make the app work <a class="yt-timestamp" data-t="27:22:00">[27:22:00]</a>.

## Overall Takeaway
While the terminology of coding and [[github_and_codex_integration | GitHub]] can feel overwhelming, [[introduction_to_chatgpt_codex | Codex]] offers a lightweight and fun way to learn about computer science and development <a class="yt-timestamp" data-t="32:01:00">[32:01:00]</a>. It introduces users to the full development cycle in a "drip-feed" manner <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>. Starting small with a simple project is key to avoiding frustration and building confidence <a class="yt-timestamp" data-t="32:24:00">[32:24:00]</a>. [[introduction_to_chatgpt_codex | Codex]] feels less like traditional coding and more like delegating tasks, making it an interesting starting point for non-technical individuals looking to build with AI <a class="yt-timestamp" data-t="34:38:00">[34:38:00]</a>.