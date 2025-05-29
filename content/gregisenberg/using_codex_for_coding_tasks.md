---
title: Using Codex for Coding Tasks
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[introduction_to_chatgpt_codex | Codex]], developed by Sam Altman and OpenAI, is an AI engineer in the browser designed to help users, including non-technical individuals, perform coding tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to input a task, which Codex then codes and pushes to GitHub <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. While some perceive it as primarily for senior engineers to optimize their workflow, it can also be leveraged by those with limited technical experience <a class="yt-timestamp" data-t="01:04:05">[01:04:05]</a>.

## Getting Started with Codex

To begin [[using_codex_for_coding_tasks | using Codex]], a crucial first step is to establish a connection with [[github_and_codex_integration | GitHub]] <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

### GitHub Integration
[[github_and_codex_integration | GitHub]] serves as a storage platform for your code, organized into repositories, which are essentially projects <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. When making changes, they are committed to these repositories <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

To set up a new project:
1.  Create a new repository on GitHub <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
2.  Assign it a name and choose whether it's public or private <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.
3.  It's recommended to add a README file, which explains the project <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

Once the repository is created, Codex can be connected to it <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Existing website code, even from no-code builders like Card, can be copied and pasted into a new GitHub repository, initiating the codebase for Codex to work with <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. For live URLs and custom domains, services like GitHub Pages or Vercel can be used for deployment <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Performing Coding Tasks

Codex operates on a task-based system, allowing users to describe desired changes in natural language.

### Task-Based Workflow
The core interaction involves describing a task, such as "add another tab next to investments tools that is called food. I like in the doc. Put tacos" <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

When a task is submitted:
1.  Codex processes the request, analyzing existing files and code <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
2.  It identifies necessary changes, creates new documents or updates existing ones, and aims to match the existing style <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
3.  After completing the task, it generates a "pull request" (PR) <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. A PR is a standard practice in coding where changes are made on a separate "branch" (a copy of the main code) and then proposed to be "merged" back into the main codebase if there are no conflicts <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.
4.  Users can review the PR, check for conflicts, and then merge the changes to update the live site <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
5.  Tasks can be "merged" (integrated into the main code) or "closed" (denied/discarded if unsatisfactory) <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>. The number of lines of code added or removed for each task is displayed <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

### Example: Adding a "Food I Like" Tab
In a demonstration, Codex successfully added a new "Food I Like" tab with "tacos" listed, and it integrated into the existing website's navigation <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. While the initial prompt didn't explicitly ask for keyboard shortcuts to be updated for the new tab, Codex's analysis noted it wouldn't make changes there unless requested <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. The change was then successfully merged to the main codebase and deployed to the live site <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>.

## Benefits and [[ai_coding_workflow_optimization | AI Coding Workflow Optimization]]

Codex streamlines the coding process by delegating tasks to the AI <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.

> "Something that's way way more advanced than you is doing it in a way that feels delegated and off your plate." <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>

Key advantages include:
*   **Iterative Development:** It allows for small, incremental additions to a project <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.
*   **Reduced Debugging:** With built-in tests and checks during the PR process, there's less time spent on debugging <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.
*   **Focus on Outcome:** Users can focus on what they want to achieve rather than the underlying code <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
*   **Mobile Accessibility:** Tasks can be set off via chat on mobile devices <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Learning Aid:** For non-technical users, it can be a lightweight way to learn computer science and development terminology <a class="yt-timestamp" data-t="32:14:00">[32:14:00]</a>.

## [[comparison_of_ai_coding_tools | Comparison of AI Coding Tools]]

[[using_codex_for_coding_tasks | Codex]]'s UI distinguishes it from other tools like Bolt or Lovable <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. While other "text-to-app" builders might generate visually perfect UIs for complex requests (e.g., a Spotify clone), the underlying functionality often remains incomplete <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. Codex, however, focuses on ensuring the core pieces work by iteratively adding features with built-in tests <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>.

Tools like Cursor also offer chat functionalities within the coding environment for asking about the codebase <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.

## [[best_practices_for_beginners_using_codex | Best Practices for Beginners Using Codex]]

For [[nontechnical_people_learning_code_with_codex | non-technical people learning code with Codex]]:

*   **Start Simple:** Begin with a personal site or create a new, non-critical site <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.
*   **Iterate Small:** Add features line by line, piece by piece <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. Examples include adding a header, an about section, or social links <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>.
*   **Utilize GitHub:** Ensure a GitHub repository is set up with at least a README file <a class="yt-timestamp" data-t="19:29:00">[19:29:00]</a>.
*   **Experiment:** Don't hesitate to merge or close tasks <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.
*   **Rollback Capability:** GitHub allows users to revert to previous versions if a change breaks the site, mitigating risk <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   **Seek External Help:** If stuck, use ChatGPT (chat.openai.com) to ask about GitHub actions like rolling back, providing context like the full code from a `uithub` link (by changing the 'G' to 'U' in a GitHub repo URL) <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>.

## [[challenges_and_solutions_in_aidriven_coding_projects | Challenges and Solutions in AI-Driven Coding Projects]]

### Limitations
Codex has some current limitations, such as not being able to upload files (images), or directly interpret UI designs from images <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>. For design elements, users might need to generate code from other tools like VZero and then bring that code into Codex <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.

### Advanced Usage and Future Steps
While simple HTML/CSS/JavaScript sites are a good starting point, integrating databases or authentication, or using frameworks like Next.js or Python, represents a higher level of complexity <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>. These often require running terminal commands within a coding environment (like `pmpm install`) to spin up servers and make the app work <a class="yt-timestamp" data-t="28:28:00">[28:28:00]</a>. Currently, this might involve using other coding tools, but the expectation is that Codex will eventually handle these commands more seamlessly <a class="yt-timestamp" data-t="26:23:00">[26:23:00]</a>.

Exploring open-source repositories on GitHub is a way to find codebases to experiment with <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>. Users can fork these repos, connect them as a new "environment" in Codex, and then task Codex with getting the code "up and running" <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.

### Overall Outlook
Codex can feel overwhelming initially due to terminology and concepts like GitHub <a class="yt-timestamp" data-t="32:01:00">[32:01:00]</a>. However, it serves as a lightweight and fun way to learn about computer science and development <a class="yt-timestamp" data-t="32:14:00">[32:14:00]</a>. It introduces coding in a "drip-fed" manner, allowing users to build capabilities incrementally, rather than attempting large, complex projects from the outset <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>. The aim is to make the process less scary for non-technical individuals, encouraging curiosity to overcome barriers and start building <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>.