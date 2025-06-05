---
title: Colocation of styles with Tailwind
videoId: lHZwlzOUOZ4
---

From: [[fireship]] <br/> 

Colocation of styles is identified as a primary problem in [[css_for_styling_and_layout | CSS]] development <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Traditional CSS Approach and its Problems

For the past two decades, the standard practice has been to separate [[css_for_styling_and_layout | CSS]] from markup to achieve a clear separation of concerns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. However, this approach introduces several challenges:
*   **Naming Conventions** Programmers often find that naming things is the most difficult part of their job, and this separation requires devising many arbitrary and frequently pointless names for [[css_for_styling_and_layout | CSS]] classes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Maintenance Difficulty** Weeks later, when returning to modify code, it becomes challenging to recall which styles apply to specific elements because the class names and their purposes have been forgotten <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Unintended Side Effects** If class names are reused across multiple parts of an application, changing a style in one place can inadvertently break other, unexpected parts of the UI <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Tailwind CSS Solution

[[tailwind_css_utility_class_approach | Tailwind CSS]] tackles the problem of colocation by providing standard utility classes that are placed directly within the HTML <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Benefits
*   **Elimination of Arbitrary Naming** Developers no longer need to invent numerous arbitrary class names <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Clear Style Application** It becomes immediately clear which styles apply to a specific element, reducing mental overhead <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Safer Modifications** Changes can be made to styles with confidence that they will not inadvertently break other parts of the application <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Drawbacks
*   **Bloated HTML** The initial appearance of HTML using [[tailwind_css_utility_class_approach | Tailwind CSS]] can seem "disgusting" or "bloated" due to the presence of many utility classes, resembling inline styles <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This is a common and valid criticism, often acting as a deterrent for new users <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Pro Tip
For users who dislike the appearance of HTML with many utility classes, the "inline fold" VS Code extension can automatically minimize or collapse them <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.