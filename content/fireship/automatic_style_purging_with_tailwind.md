---
title: Automatic style purging with Tailwind
videoId: lHZwlzOUOZ4
---

From: [[fireship]] <br/> 

One of the problems [[comparison_between_tailwind_css_and_traditional_css | CSS]] users face is the tendency to write styles that are never actually used, leading to a bloated [[comparison_between_tailwind_css_and_traditional_css | CSS]] bundle <a class="yt-timestamp" data-t="03:09:59">[03:09:59]</a>. These are often referred to as "zombie styles" <a class="yt-timestamp" data-t="03:09:59">[03:09:59]</a>.

[[benefits_and_drawbacks_of_tailwind_css | Tailwind]] addresses this issue by automatically purging all unused styles <a class="yt-timestamp" data-t="03:14:622">[03:14:622]</a>. This process effectively "kills the zombies" and removes dead code from the final bundle <a class="yt-timestamp" data-t="03:14:622">[03:14:622]</a>.

## Considerations
While automatic purging is a beneficial feature, it's worth noting that [[benefits_and_drawbacks_of_tailwind_css | Tailwind]] can be a "heavy-handed approach" in its setup <a class="yt-timestamp" data-t="03:19:902">[03:19:902]</a>. Installing and configuring [[benefits_and_drawbacks_of_tailwind_css | Tailwind]] typically involves several steps, including setting up the [[css_tools_and_preprocessors | Tailwind CLI]], PostCSS, and a VS Code extension <a class="yt-timestamp" data-t="03:24:622">[03:24:622]</a>. For this reason, it is often recommended for larger projects rather than small demos <a class="yt-timestamp" data-t="03:30:192">[03:30:192]</a>.