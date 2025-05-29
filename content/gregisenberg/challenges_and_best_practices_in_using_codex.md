---
title: Challenges and Best Practices in Using Codex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

Codex, a new AI engineer in the browser from Sam Altman and OpenAI, allows users to type in a task, have it coded, and then pushed to [[integrating_github_and_codex | GitHub]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While powerful, especially for those who prefer not to delve into code <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>, it presents specific challenges, particularly for non-technical users.

## Challenges in Using Codex

For individuals unfamiliar with traditional coding environments, Codex can be overwhelming <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The user interface, while unique, may not feel intuitive, especially when navigating features like "environments" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

Key challenges include:
*   **Overwhelm for Non-Technical Users** The terminology and concepts like [[integrating_github_and_codex | GitHub]] can feel like a "behemoth," making the tool seem daunting <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Deployment Loop Length** The time taken from submitting a task to seeing the changes live on a site can be long <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Current Limitations** Codex currently has limitations such as the inability to upload files or images, or to directly instruct it to "make the UI look like this" <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **Early Preview Instability** As an early preview, the tool can be "a bit on the fritz" <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   **Complexity for Advanced Projects** For projects beyond basic HTML, CSS, and JavaScript, users might need to run complex terminal commands (e.g., `pmpm install`) to get the code running, which can be confusing for non-technical individuals <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   **Contrast with Text-to-App Builders** While text-to-app builders like Bolt might seem simpler by spitting out a "UI perfect" app, their underlying features are often "underbuilt," leading to non-functional components <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This means more time is spent debugging or fixing issues that should have worked <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

## Best Practices for Using Codex

Despite the challenges, Codex offers a structured way to iteratively build and learn <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

Here are some best practices, especially for non-technical users:

### Start Simple and Iterate
*   **Personal Projects** Begin with a personal site or create a new one if you're concerned about your existing project <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. This allows for low-risk experimentation <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
*   **Gradual Additions** Tackle tasks "line by line and like piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. For example, start by asking Codex to "make a website with my name as the header," then add an "about section," and then "some social links" <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   **Test Small Features** Focus on adding simple, interactive elements, like keyboard shortcuts or a dark/light mode switcher, that you might see on other developer websites <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

### Understand the Workflow
*   **Connect to [[integrating_github_and_codex | GitHub]]** Ensure you have a [[integrating_github_and_codex | GitHub]] repository connected, ideally with at least a README file enabled upon creation <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Leverage Pull Requests (PRs)** When Codex completes a task, it creates a pull request (PR). This is a copy of your main code (a "branch") where changes are made <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. If the changes work and have no conflicts, you can merge it back into the main code <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Use "Merged" and "Closed" States**
    *   **Merged:** Indicates changes have been successfully integrated into your main codebase <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
    *   **Closed:** Means the changes were discarded, often because they didn't work as expected <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. If a change breaks your site, you can revert to a previous working version on [[integrating_github_and_codex | GitHub]] <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

### Seek External Help
*   **Utilize ChatGPT** If you encounter issues or have questions about [[integrating_github_and_codex | GitHub]] concepts (e.g., how to roll back changes), use ChatGPT (<a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>). You can even provide it with your entire codebase by changing the first letter of "GitHub" to 'u' (uit hub) to get a view of all the code <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
*   **Explore Other Tools** For design aspects (like UI), combine Codex with other tools like vzero that generate design code <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Educational Value
[[using_codex_for_nontechnical_people | Using Codex for Nontechnical People]] can serve as a lightweight and engaging way to learn about computer science and development terminology <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>. While not a replacement for traditional coding, it introduces concepts like codebases, branches, commits, and pull requests in a practical context. This approach "drip feeds" coding knowledge, making it less intimidating than diving directly into complex text-to-app builders that might overcomplicate the learning process with early-stage bugs <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.