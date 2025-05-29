---
title: Derivatives of exponential functions
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The function e<sup>t</sup> possesses a unique and defining property: it is its own derivative <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Combined with the condition that inputting 0 returns 1, it is the only function with this characteristic <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Intuition Behind Growth

This property can be understood through a physical model <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. If e<sup>t</sup> represents your position on a number line as a function of time, you begin at position 1 <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The equation states that your velocity (the derivative of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means the farther you are from 0, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

This relationship provides a strong [[intuition_behind_the_growth_of_exponential_functions | intuitive picture]] of how the function grows, even without knowing its exact computation <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. You accelerate at an accelerating rate, leading to a feeling of things rapidly getting "out of hand" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Derivatives of Exponential Functions with a Constant Exponent

When a constant `c` is added to the exponent, such as e<sup>ct</sup>, the [[computing_derivatives_of_functions | chain rule]] dictates that the derivative becomes `c` times the original function <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   **Positive Constant:** If `c` is positive (e.g., e<sup>2t</sup>), your velocity is always twice your position <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This results in an even more pronounced "runaway growth" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Negative Constant:** If `c` is negative (e.g., e<sup>-0.5t</sup>), your velocity vector is always `c` times your position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This means the velocity vector is flipped 180 degrees and its length is scaled <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Moving under this condition causes you to go in the opposite direction, slowing down in a process of [[exponential_growth_and_decay | exponential decay]] towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Derivatives of Exponential Functions with an Imaginary Exponent

A fascinating case arises when the constant in the exponent is `i`, the square root of negative 1 (e.g., e<sup>it</sup>) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

*   **Derivative Property:** The derivative of e<sup>it</sup> is always `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Geometric Interpretation:** Multiplying by `i` has the effect of rotating numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Movement in the Complex Plane:** To understand this, one must think beyond the number line and within the [[complex_plane_and_exponential_functions | complex plane]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. For any position e<sup>it</sup> might yield, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Trajectory:** Starting at time t=0, where e<sup>it</sup> is 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, the only trajectory where velocity consistently matches a 90-degree rotation of position is moving around a circle of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   After π seconds, you've traced a distance of π, so e<sup>iπ</sup> = -1 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   After τ (2π) seconds, you've completed a full circle, so e<sup>iτ</sup> = 1 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   Generally, e<sup>it</sup> equals a number that is `t` radians around this unit circle in the complex plane <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Notational Considerations

The notation "e to the t" is considered by some to be a "notational disaster" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, as it gives the number `e` and the concept of repeated multiplication more emphasis than they might deserve for its fundamental properties <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.