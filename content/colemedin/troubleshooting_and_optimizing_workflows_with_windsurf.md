---
title: Troubleshooting and optimizing workflows with Windsurf
videoId: ukhe1013Jpk
---

From: [[colemedin]] <br/> 

[[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is considered by some to be the best AI IDE, combining the ease of a co-pilot with the ability to perform complex, long-running coding tasks as an agent <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Its design aims to keep developers in a "Flow State," fostering a cohesive experience where the AI agent is fully integrated into the coding process <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This integration means the AI is aware of all changes made by the user, and vice versa, creating a continuous pair programming experience <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. While not perfect, [[benefits_and_features_of_windsurf | Windsurf]] can save hours of coding time, enabling developers to focus on building high-quality, production-ready code <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## General Workflow and Integration

A common workflow involves combining [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] with other tools:
*   **Initial Frontend Development** Tools like oTToDev or Bolt.new are preferred for building the initial frontends <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Export and Refine** Once the initial frontend is developed and reaches a point where it gets "stuck," the project can be exported and imported into [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] for finishing touches <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Backend Development** [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] excels at backend development, particularly with Python coding and database management <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Optimizing Workflows

To maximize productivity and achieve better results with [[introduction_to_windsurf_as_an_ai_ide | Windsurf]], consider the following strategies:

### 1. Be Specific with Prompts and Define Your Tech Stack
*   **Initial Setup** When starting a new application, explicitly define your tech stack, including programming languages and technologies <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. For example, instead of a vague "build me an API endpoint to manage users," specify "use Fast API and Python for the API endpoint... to change a user's email in Postgres hosted with Superbase" and even include schema details <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This specificity is crucial for effective collaboration with the AI <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **Directed Changes** Use the "@" symbol to call out specific files or functions to the agent <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This ensures the AI knows exactly what to edit or reference, preventing hallucinations and incorrect edits <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

### 2. Manage Conversations and Requests Strategically
*   **One Request at a Time** Avoid sending multiple requests or problems in a single prompt <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Giving [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] one request at a time, ensuring it corrects itself if it messes up, leads to much better results and ultimately saves time <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### 3. Utilize Refactoring and Explanation Features
*   **Directed Refactoring** For specific, directed changes to a function or class, use the "refactor" button <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. This narrows the AI's context to that specific element, leading to more focused and accurate results <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
*   **Code Explanation** If you need to understand a function, whether produced by the AI or imported from another project, use the "explain" feature <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This provides a clear explanation of specific code sections <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

### 4. Leverage AI for Documentation and Testing
*   **Documentation** [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is "phenomenal" for documenting code, saving significant time <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Always include a prompt to explicitly state that the AI should *not* update the code when adding documentation <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. While a "doc string" feature exists, direct prompting allows for more detailed comments within the code, not just above functions <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Writing Tests** AI is very helpful for writing tests, a critical but often annoying task for developers <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. While AI-generated tests may not work perfectly initially, they save hours by setting up boilerplate code and handling library imports (e.g., Jest, React Testing Library, Pytest) <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. You can then tweak them to ensure accuracy <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Troubleshooting and Debugging

Despite its capabilities, [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] and the underlying Large Language Models (LLMs) can encounter issues:

### 1. Address Hallucinations and Long Conversations
*   **Start New Conversations** LLMs can get confused and hallucinate when conversations become too long <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. If [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] starts hallucinating, the best approach is to start a brand new conversation <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Although this means losing some context, it often resolves the hallucination issue by re-explaining the problem briefly <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### 2. Leverage Accept/Reject Features for Testing and Reversion
*   **Test Before Accepting** [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] implements changes in the code *before* you formally accept them <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This allows you to test the changes in your application first <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. If the changes are not working or undesired, you can simply "reject" them, and [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] will revert them automatically <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This eliminates the need for manual reversion.
*   **Selective Acceptance/Rejection** You can accept or reject specific changes within different files <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. If [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] makes several correct changes but one is wrong, you can reject only the problematic change before accepting the rest <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The agent will then know which parts were rejected and can correct them <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

### 3. External Tool for Persistent Issues
*   **Switching Models for Debugging** If [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] (which uses Claude 3.5 Sonnet) is struggling with a particular problem, consider using a different AI model, such as 01 <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Some users find 01 to be slightly better at coding and problem-solving in certain scenarios <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. You can provide 01 with your code, the problem description, and any error messages <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>, then bring the fix back into [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Because [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] operates in a "Flow State" and is aware of your manual changes, you can continue where you left off with the applied fixes <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.