---
title: exponential growth and decay
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The function `e` to the `t` (`e^t`) is central to understanding [[understanding_exponential_growth | exponential growth]] and decay. Its most important, and often defining, property is that it is its own [[Derivatives of Exponential Functions | derivative]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Coupled with the condition that inputting 0 returns 1, `e^t` is the *only* function with this characteristic <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Intuitive Understanding through a Physical Model

A physical model can illustrate the meaning of `e^t` being its own derivative <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

*   If `e^t` describes your position on a number line as a function of time, you start at the number 1 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   The equation implies that your velocity (the [[Derivatives of Exponential Functions | derivative]] of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   This means the farther away from 0 you are, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   This relationship of associating each position with a velocity paints an intuitive picture of how the function grows <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. You accelerate at an accelerating rate, leading to a feeling of things getting out of hand quickly <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Modifying the Exponent: `e^(ct)`

When a constant is added to the exponent, such as `e^(2t)`, the [[Chain Rule and Exponential Functions | chain rule]] states that the derivative is now 2 times itself <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   This means that for any position, the velocity vector is double the magnitude of the position vector <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   Moving so your velocity is always twice your position makes the runaway growth feel even more out of control <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This exemplifies [[applications_of_exponential_growth_in_natural_phenomena | exponential growth]].

### Exponential Decay

If the constant in the exponent is negative, for example, `e^(-0.5t)`, your velocity vector is always negative 0.5 times your position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

*   This involves flipping the vector 180 degrees and scaling its length by a half <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   Moving this way means you go in the opposite direction, slowing down in an [[applications_of_exponential_growth_in_natural_phenomena | exponential decay]] towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The Imaginary Exponent: `e^(it)`

A particularly interesting case arises when the constant is `i`, the square root of negative 1, as in `e^(it)` <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

*   The [[Derivatives of Exponential Functions | derivative]] of your position will always be `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Multiplying by `i` has the effect of rotating numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   This concept only makes sense when thinking beyond the number line and in the complex plane <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   For any position given by `e^(it)`, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

When visualized as a vector field (where velocity vectors are attached to positions), and given the initial condition that `e^(i0)` is 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, the only trajectory starting from that position where velocity always matches a 90-degree rotation of the position is motion around a circle of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This leads to significant results:
*   After pi seconds, having traced a distance of pi around, `e^(iπ)` should be -1 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   After tau seconds (where tau equals `2π`), you've gone full circle, so `e^(iτ)` equals 1 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   More generally, `e^(it)` equals a number that is `t` radians around the unit circle in the complex plane <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Notational Considerations

The notation `e^t` can be considered a "notational disaster," as it gives the number `e` and the idea of repeated multiplication more emphasis than they might deserve in a broader mathematical context <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Despite its common use, understanding the underlying properties, especially its derivative characteristic, is key to grasping [[exponential_functions_and_their_properties | exponential functions and their properties]].