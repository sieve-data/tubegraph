---
title: Benefits and Challenges of Using AI Tools like Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codex, Sam Altman and OpenAI's AI engineer, allows users to type in a task, have it coded, and then pushed to GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This tool is designed to assist in coding within the browser <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## How Codex Works
Codex integrates with GitHub repositories, enabling it to store code and manage changes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Users need to connect their GitHub account and select a repository or create a new one for their project <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The workflow involves:
1.  **Defining a task:** Users describe the desired change or addition in natural language <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
2.  **Generating code:** Codex processes the request, analyzes existing code, and generates the necessary changes <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  **Creating a Pull Request (PR):** After generating code, Codex creates a PR, which is a standard practice in coding to propose changes to the main codebase <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a> <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
4.  **Merging or Closing:** Users review the PR; if checks pass and there are no conflicts, they can merge it to the main branch, applying the changes to the live site <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a> <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a> <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. If unsatisfied, the PR can be closed without affecting the main code <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a> <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

Each merged or closed task displays the number of lines of code added (+) and removed (-) <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a> <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## Benefits of Using Codex

### For Non-Technical Users
*   **Delegated Coding:** Codex allows non-technical users to delegate coding tasks without writing any code themselves <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a> <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a> <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This makes it feel like writing a to-do list that is completed by an advanced entity <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a> <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Iterative Development:** It supports an iterative approach, allowing users to add features incrementally with built-in tests and checks to ensure functionality <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a> <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a> <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **Reduced Debugging:** The system aims to minimize time spent debugging, as tasks either work or prompt the user to try a different approach or another coding agent <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a> <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
*   **Mobile Accessibility:** The ability to operate via chat, including on mobile devices, enhances convenience <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a> <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Learning Opportunity:** Playing with Codex can serve as a lightweight and fun way to learn computer science and development terminology, easing non-technical people into the world of coding <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a> <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>.
*   **Lower Risk for Personal Projects:** For non-client-facing or non-money-making personal sites, there's minimal risk in experimenting, as changes can always be rolled back to a previous working version via GitHub <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a> <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a> <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.

> [!info] Codex for Beginners
> [[using_codex_in_the_browser_for_beginner_developers | Using Codex in the Browser for Beginner Developers]] can help overcome the initial intimidation of coding and the complexities of setup. It offers a structured way to start coding by handling the heavy lifting <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.

## Challenges and Limitations of Using AI Tools like Codex

### Current Limitations
*   **[[challenges_in_coding_with_ai | Challenges in coding with AI]]:** The process loop for seeing changes (writing task, getting code, pushing to codebase, deploying, seeing change) can be lengthy <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **No Direct File/Image Uploads:** Codex cannot directly upload files or images <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a> <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
*   **UI Customization Challenges:** It struggles with complex UI generation; for instance, specifying "make the UI look like this" is difficult <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a> <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.
*   **Early Preview Instability:** As an early preview, the tool can be "on the fritz," and tasks might break after about 30 minutes <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a> <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

> [!warning] Overwhelm for Beginners
> For non-technical users, Codex can still feel overwhelming due to the underlying concepts and terminology like GitHub, branches, pull requests, and terminal commands <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a> <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. Setting up environments and connecting repositories isn't always intuitive <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a> <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.

### Comparison to other AI Tools
*   **Text-to-App Builders (e.g., Bolt):** While tools like Bolt might spit out a UI-perfect application, their underlying features are often "underbuilt," meaning the functional pieces don't actually work <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a> <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a> <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This leads to a difficult process of working backward to make features functional <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a> <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   **Other Coding Agents:** Users might need to try different coding agents if Codex doesn't solve a task <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. The ecosystem of [[the_role_and_importance_of_ai_agents_in_coding_platforms | AI agents in coding platforms]] is evolving, with tools like Cursor offering integrated chat for codebase inquiries <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a> <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## Best Practices for Non-Technical Users
*   **Start Simple:** Begin with small, manageable tasks on a personal site, such as creating a basic website with a header, about section, and social links <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a> <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a> <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a> <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   **Utilize GitHub:** Ensure a GitHub repository is set up, even if it only contains a README file <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a> <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Experiment:** Play around with merging and closing pull requests to understand the workflow <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Leverage External AI:** If stuck, use general-purpose AI chat models like ChatGPT (chat.openai.com) to ask questions about GitHub rollback or general coding issues, often by providing relevant code or repository links <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a> <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a> <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a> <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   **Iterate Small:** Focus on adding features "line by line" and "piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Use Open Source:** Explore open-source repositories on GitHub to learn and potentially fork codebases for personal projects <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a> <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

> [!tip] Learning Pathway
> The journey with AI coding tools can be seen as a progressive learning path:
> 1.  **Level 1: Personal Site:** Start by building and modifying a simple personal website <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
> 2.  **Next Levels:** Gradually advance to more complex features such as integrating with databases, implementing user authentication, or enabling user sign-in/sign-up and bookmarking functionalities <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a> <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a> <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a> <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

## Future Outlook

The landscape of AI coding tools is rapidly evolving. Automation of processes like merging pull requests is likely to become standard <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a> <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. While Codex currently focuses on simpler HTML, CSS, and JavaScript projects, it is expected to handle more advanced frameworks like Next.js or Python in the future <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a> <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>. This shift suggests a future where AI tools could become the primary method for development, making coding accessible even to those who cannot write a single line of code <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a> <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.