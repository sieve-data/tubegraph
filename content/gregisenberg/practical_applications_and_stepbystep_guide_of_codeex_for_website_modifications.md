---
title: Practical applications and stepbystep guide of Codeex for website modifications
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

[[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]], an AI engineer in the browser from Sam Altman and OpenAI, allows users to type in a task, have it coded, and then pushed to [[setting_up_and_using_github_with_codeex | GitHub]] <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. It's designed for non-technical people to get the most out of an AI coding tool <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Setting Up for Website Modification

To use [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] for website modification, you need to have a [[setting_up_and_using_github_with_codeex | GitHub]] account and connect it to [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

### Understanding GitHub
[[setting_up_and_using_github_with_codeex | GitHub]] is a platform where your code is stored. Projects are organized into "repositories" (repos), which store all code files <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Any changes made are called "commits" and are recorded <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

### Creating a New GitHub Repository
1.  Go to [[setting_up_and_using_github_with_codeex | GitHub]] and create a new repository <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
2.  Give it a name and choose if it's public or private <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.
3.  Optionally, add a README file to explain the project <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
4.  Create the repository <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

### Getting Existing Code into GitHub
If you have an existing website built on a [[exploring_nocode_solutions_for_app_development | no-code]] builder like Card, you can get its code into [[setting_up_and_using_github_with_codeex | GitHub]]:
1.  Right-click on your live website and select "view page source" to see the underlying code <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
2.  Copy all the code <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
3.  Use a coding agent (or [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] itself) to put this code into your newly created [[setting_up_and_using_github_with_codeex | GitHub]] repository <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
4.  Connect your [[setting_up_and_using_github_with_codeex | GitHub]] repo to [[setting_up_and_using_github_with_codeex | GitHub]] Pages for a live URL, or use a service like Vercel for deployment <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Step-by-Step Website Modification Example (Adding a Tab)

Once your website is live and connected to [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]], you can make changes through natural language prompts.

### 1. Adding a Task in Codeex
To modify the website, you add a task in [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. For example, to add a new tab: "add another tab next to investments tools that is called food I like in the dock put tacos" <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

### 2. Code Generation by Codeex
Click "Code" in [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to start the process <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>. [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] will:
*   Use the terminal to find different files and understand the existing code <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
*   Plan its actions, such as looking at files, checking document styles, creating new documents for sections, and updating the main site <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   It performs its own tests to ensure functionality <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.

### 3. Reviewing Proposed Changes
Once [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] completes its work, it shows which files were changed and what code was added or removed <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.

### 4. Creating a Pull Request (PR)
To apply the changes, click "Create new PR" <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
*   **Branches:** Code is typically on a "main branch." When working on a new feature, a "branch" is created, which is a copy of the code where changes are made <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.
*   **Pull Request (PR):** A PR is a proposal to merge the changes from your feature branch back into the main branch <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] will check for conflicts with the base branch <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.

### 5. Merging the Pull Request
If there are no conflicts and all checks pass, you can "merge" the PR <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. This integrates the new code into your main codebase, making it part of the live site <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. This process might take a few seconds <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

### 6. Verifying Changes on the Live Site
After merging, refresh your website to see the changes implemented <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.

### Understanding Merged vs. Closed Tasks
*   **Merged:** A task is "merged" when its changes have been successfully integrated into the main codebase <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.
*   **Closed:** A task can be "closed" if the proposed changes are not desired or don't work <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. This is like denying a change, and since it was on a separate branch, it doesn't affect your main code <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.
*   **Line Changes:** The numbers next to merged/closed tasks (+X, -Y) indicate the number of lines of code added (+) or removed (-) across the entire codebase <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>.

## Best Practices for [[considerations_for_learning_to_code_using_aidriven_tools_like_codeex | Non-Technical Users]]

For [[considerations_for_learning_to_code_using_aidriven_tools_like_codeex | non-technical users]] getting started with [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]]:

*   **Start Simple:** Begin with a personal site or create a new one to experiment <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.
*   **Iterate Incrementally:** Work on small, single features at a time, like adding a tab or changing text <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>.
*   **GitHub Basics:** Ensure your [[setting_up_and_using_github_with_codeex | GitHub]] repository has at least a README file enabled when you create it <a class="yt-timestamp" data-t="19:29:00">[19:29:00]</a>.
*   **Rollback Capability:** If a change breaks your site, [[setting_up_and_using_github_with_codeex | GitHub]] allows you to revert to a previous working version <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>. For personal, non-client-facing sites, the risk is low <a class="yt-timestamp" data-t="20:28:00">[20:28:00]</a>.
*   **Leverage External AI (ChatGPT):** When stuck, ask ChatGPT for help with [[setting_up_and_using_github_with_codeex | GitHub]] issues or coding concepts <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>. You can feed your entire codebase (by changing the first letter of "GitHub" to "u" in the URL, e.g., `uithub.com` to view all code) to ChatGPT for analysis <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.
*   **Understand Limitations:** [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] cannot upload files or images directly, nor can it create complex UI designs from scratch <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.
*   **Integrate with Other Tools:** For design, tools like [[practical_tips_for_using_vz_to_build_and_design_web_interfaces | V0]] can generate design code that you can then bring into [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.

## Levels of Using Codeex

1.  **Level 1: Personal Site:** Begin by building or modifying a simple personal site, adding basic elements like a header, about section, and social links <a class="yt-timestamp" data-t="23:53:00">[23:53:00]</a>.
2.  **Next Mini Level:** Integrate [[setting_up_and_using_github_with_codeex | GitHub]] to pull in live information or updates to your site <a class="yt-timestamp" data-t="24:56:00">[24:56:00]</a>.
3.  **Intermediate Levels:** Explore more complex features like user sign-in/sign-up, saving/bookmarking items, working with a database layer, or integrating AI components <a class="yt-timestamp" data-t="25:09:00">[25:09:00]</a>.
4.  **Advanced Usage (Requires Environment Setup):** For projects with frameworks (like Next.js, Python), you'll need to set up "environments" in [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] and run terminal commands (e.g., `pnpm install`, `pnpm dev`) to get the app running and allow [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] to interact with the code <a class="yt-timestamp" data-t="28:28:00">[28:28:00]</a>.

## Why Use Codeex as a [[considerations_for_learning_to_code_using_aidriven_tools_like_codeex | Non-Technical User]]?

While [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] might initially feel overwhelming compared to prototyping tools like [[stepbystep_guidance_on_using_bolt_to_build_web_applications | Bolt]] <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, it offers unique benefits:

*   **Delegated Coding:** [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] allows you to focus on the desired outcome (e.g., "add this tab") rather than looking at or thinking about the code <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. It's like setting a to-do list where an advanced entity handles the tasks <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>.
*   **Iterative Development:** It facilitates building incrementally, adding one feature at a time, with built-in tests and checks that reduce time spent debugging <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.
*   **Mobile Native:** The ability to interact with [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] via chat on mobile makes it accessible for continuous "shipping" <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Learning Aid:** [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] provides a lightweight way to learn computer science and development terminology by introducing concepts like [[setting_up_and_using_github_with_codeex | GitHub]], branches, and pull requests in a more engaging context <a class="yt-timestamp" data-t="32:17:00">[32:17:00]</a>. It "drip feeds" coding concepts <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>.
*   **Avoids Overbuilding:** Unlike some "text-to-app" builders that might generate perfect UI but non-functional features, [[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | Codeex]] focuses on making pieces *work*, allowing you to build from functionality outwards <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Lower Barrier to Entry for "Coding":** It feels less like traditional coding, making it a potentially better starting point for those new to development than complex builders that quickly introduce debugging challenges <a class="yt-timestamp" data-t="34:35:00">[34:35:00]</a>.