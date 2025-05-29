---
title: Challenges and limitations faced by nontechnical users in coding environments
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

For non-technical individuals, navigating coding environments like OpenAI's Codeex can present significant challenges, despite their aim to simplify the development process <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Overwhelm and Complexity
The initial impression of tools like Codeex for a non-technical person can be overwhelming <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The terminology and semantics, such as "GitHub," often feel like a "behemoth" <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.

### Understanding GitHub
A fundamental requirement for using Codeex is connecting to GitHub <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. GitHub is a platform where code is stored <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Key concepts that can be challenging include:
*   **Repositories (repos)**: These are essentially project folders <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Commits**: These are saved changes made to the code files <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Branches**: Code is managed in "branches," with a "main branch" being the primary line of code. When working on new features, a separate branch is created, copied from the main code. Once the feature is successful and has no conflicts, it can be "merged" back into the main branch <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

Even though Codeex automates many actions, users still need to understand these underlying concepts to interact effectively, for example, by creating a new repository or understanding pull requests <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Navigating the Interface
While Codeex aims to keep the code itself out of sight, users still encounter screens showing file changes and terminal commands <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The UI, while different from traditional coding tools, can still be confusing <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. For instance, the "environments" section, where users connect different repositories, is not intuitive for a beginner <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.

## Practical Difficulties in Workflow
*   **Deployment Loop Length**: After a task is completed and merged, the deployment process to see changes live can be slow, taking a "couple of seconds" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, which can be frustrating for immediate feedback.
*   **Debugging and Error Handling**: If a change breaks the site, a non-technical user might need to roll back to a previous version on GitHub <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. While possible, this requires knowing how to use GitHub's version control.
*   **Limited Input Capabilities**: Codeex has certain [[current_limitations_and_future_potential_of_AI_coding_tools | limitations]], such as not allowing users to upload files, images, or define UI directly <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This means non-technical users might need to use other tools (e.g., vZero for design) and integrate that code, adding complexity <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **External Knowledge Required**: Running more complex applications that use frameworks like Next.js or Python requires running specific "terminal commands" (e.g., `pnpm install`) which are unfamiliar to non-technical users <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. Users might need to consult external AI tools like ChatGPT for help understanding these commands <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.

## Comparison to [[exploring_nocode_solutions_for_app_development | No-Code Solutions]]
For a non-technical person, tools like Bolt or Lovable can feel much less overwhelming than Codeex, which requires a deeper understanding of underlying code management <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

*   **Overbuilt vs. Underbuilt Features**: Many text-to-app builders tend to create "overbuilt" tools where the UI looks perfect, but core functionalities are "underbuilt" and don't actually work <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This leads to users focusing on the final product before the underlying pieces are functional, making debugging harder <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Iterative vs. Holistic Building**: Codeex encourages an iterative approach, adding features one by one, with technical checks (tests) theoretically ensuring functionality <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This reduces time spent debugging non-working parts, as tasks can be delegated to the AI <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Mitigation Strategies for Non-Technical Users
*   **Start Simple**: Begin by working on a personal website or a new, non-critical site <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Iterate Small Changes**: Focus on adding features "line by line and piece by piece" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. Examples include adding a header, an about section, or social links <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   **Embrace Experimentation**: There's "no real danger" for personal projects, as users can always revert to previous versions if something breaks <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   **Leverage External AI Help**: Use tools like ChatGPT to ask questions about GitHub or to troubleshoot code issues <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. Users can even copy and paste an entire GitHub repo's code into ChatGPT for analysis <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   **Learn from Open-Source Projects**: Explore open-source repositories on GitHub to see how code is structured and get ideas <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

> [!INFO] Learning to Code with AI
> Using Codeex can be a "lightweight way to learn how to code" <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>, as it introduces core computer science and development terminology in a more accessible and fun manner <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. It "drip feeds" coding concepts, unlike text-to-app builders that might immediately throw users into complex debugging scenarios <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.
