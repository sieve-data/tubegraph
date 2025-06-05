---
title: Key framed animations in Angular
videoId: 7JA90VI9fAI
---

From: [[fireship]] <br/> 

## Introduction to Keyframes
While standard animations in Angular typically involve a single starting and ending point, keyframed animations allow for multiple intermediate steps within a transition <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This provides greater control and complexity for your animations.

## Implementing a Keyframed Transition
To implement a keyframed animation for [[router_animations_in_angular|router transitions]], you can define a new animation using a wildcard (`* => *`) to apply it to every route change <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Similar to other animations, the initial position of components should be set to `absolute` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

To run animations for both the entering and leaving pages concurrently, they should be grouped together <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Instead of animating to a single style, the `keyframes` function is used to pass in an array of styles <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. These styles act as steps in the animation <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, with their timing determined by an `offset` value relative to the total animation duration <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Animating the Enter Component
For the entering component:
*   An `offset` of `0` applies a style as soon as the animation begins <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. For instance, the component might be scaled to zero and translated off the page <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   A second style can be added with an `offset` like `0.3` (e.g., 30% of a 2000ms animation would be at 600ms) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   The final style is set with an `offset` of `1`, marking the end of the animation when the component is fully visible at a scale of `1` and a translate of `0` <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

## Animating the Leave Component
The keyframes for the leaving component can be roughly matched to the entering component to create a specific effect <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. For example, to create an effect where the entering component "bumps" the old component off the screen <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, the leaving component can be scaled up to 600% of its original size while simultaneously rotating and fading out to an opacity of zero <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

This combination results in a 3D effect where pages appear to collide <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.