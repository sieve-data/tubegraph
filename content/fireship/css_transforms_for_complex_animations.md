---
title: CSS transforms for complex animations
videoId: 7JA90VI9fAI
---

From: [[fireship]] <br/> 

[[using_css_transforms_for_sliding_animations | CSS transforms]] provide a powerful way to create more intricate and dynamic animations beyond simple slides or fades <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. They allow for advanced effects such as rotation, scaling, skewing, and translation in a single property <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Capabilities of CSS Transforms

While standard animations might involve simple movement, [[using_css_transforms_for_sliding_animations | CSS transforms]] expand possibilities to include:
*   **Rotation**: Making elements spin or rotate from various angles <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Scaling**: Changing the size of an element <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Translation**: Moving an element along the X and Y axes <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Skewing**: Tilting an element <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

These transformations can be combined to create a wide array of "crazy animations" <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

## Implementing Transformations

To implement complex animations using [[using_css_transforms_for_sliding_animations | CSS transforms]], you can define a function that accepts named arguments such as `x`, `y`, and `rotation` values <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This allows for a configurable function to create various animation effects <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Defining Transformations

Transformations are typically defined by interpolating values into CSS strings <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>:
*   **Translate**: `translate(X%, Y%)` using percentages for X and Y values <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Rotate**: `rotate(DEG)` using degrees for rotation <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

These can be extended to include `skew` and `scale`, providing even more customization <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The values for these transforms are then applied within the animation's style definition <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

For a full implementation example, refer to the source code available at Fireship.io <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.