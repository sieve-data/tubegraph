---
title: Troubleshooting and consulting multiple AI models
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

When developing with AI tools like Cursor, users may encounter situations where the model gets stuck or provides unhelpful solutions. In such cases, it is beneficial to consult other AI models and apply specific strategies to [[techniques_for_increasing_ai_effectiveness | increase AI effectiveness]] <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

## When Cursor AI Gets Stuck
If Cursor AI continuously gets stuck on a bug or issue, it might be time to consult another AI model <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. Even if Cursor is using models like Claude internally, copying the issue and pasting it into an external Claude or even [[understanding_ai_tools_and_models_for_development | ChatGPT]] can yield different, more effective results <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.

### Providing Context to Other AI Models
Simply copying and pasting the bug to another AI model might lead to the same failed solutions <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. To get better results, it is crucial to provide the new AI model with comprehensive context <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>:
*   **State the issue/bug clearly** <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.
*   **Include the code that is causing the problem** <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
*   **Detail the solutions that the previous AI model attempted but failed to fix the issue** <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
*   **Explain the output you are currently receiving and what you are expecting** <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

This approach tells the AI: "This is the issue, these solutions were tried and failed, so you need to try something new" <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. By providing this detailed context, the results from the new AI model are significantly better <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.

> "Context is king. So instead of just copy pasting the bug and giving it to the next AI model it will probably give you the same solution again but what you do is you give it the solutions it tried that it failed even give it the output you're getting and what you're expecting and I've seen time and time every time I do that the result are just much much better" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>

### Hierarchy of AI Models for Troubleshooting
Different AI models may excel at different tasks:
*   **Claude:** Recommended for everyday tasks and general programming <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
*   **Cursor and v0:** Excellent for starting and UI components <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.
*   **[[understanding_ai_tools_and_models_for_development | ChatGPT]]:** Can be used as a last resort if other models fail <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.

## Learning Through Troubleshooting
Using AI to troubleshoot is also a valuable learning experience <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. When an AI solves a problem for you, you start to understand how things work <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>. This "doing and breaking" cycle, followed by understanding the fix, leads to new learning <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. This process can significantly expedite learning, especially for new technologies <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>.

> [00:24:28] "I think this is one of those things where if people are used to learning then doing it's going to be a tough time because it's one of those things you're going to do it's going to break and then you're going to do again it's going to break and then the when it works you realize oh this is how it works you just learned something new"