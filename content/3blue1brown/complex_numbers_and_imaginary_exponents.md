---
title: complex numbers and imaginary exponents
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

One way to understand the function e<sup>t</sup> is by its defining property: it is its own derivative <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Combined with the condition that inputting 0 returns 1, it is the only function with this characteristic <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Behavior of e<sup>t</sup>

Consider e<sup>t</sup> describing your position on a number line as a function of time <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Starting at 1 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, this property means your velocity (the derivative of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This implies that the farther you are from 0, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This leads to an accelerating growth, giving an intuitive sense of things quickly getting "out of hand" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## The Constant in the Exponent

### Real Constant (e<sup>kt</sup>)

If a real constant `k` is added to the exponent, such as e<sup>2t</sup>, the chain rule indicates the derivative is `k` times itself <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For e<sup>2t</sup>, the derivative is 2 times e<sup>2t</sup> <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This means your velocity is always twice your position, accelerating the runaway growth <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

If the constant is negative, like e<sup>-0.5t</sup>, your velocity vector is always -0.5 times your position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Geometrically, this means the velocity vector is flipped 180 degrees and its length scaled by half <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Moving under this condition results in exponential decay towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### [[the_concept_of_imaginary_numbers | Imaginary]] Constant (e<sup>it</sup>)

A more complex scenario arises when the constant in the exponent is `i`, the square root of negative 1 <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If your position is e<sup>it</sup>, its derivative will always be `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

[[complex_numbers_multiplication_and_rotation | Multiplying by i]] has the effect of rotating numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This behavior only makes sense when moving beyond the number line and into the [[complex_numbers_in_mathematics | complex plane]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

#### [[geometric_interpretation_of_complex_numbers | Geometric Interpretation]] in the [[complex_numbers_in_mathematics | Complex Plane]]

For any position e<sup>it</sup> yields, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This creates a vector field where the velocity vector at any point is a 90-degree rotation of the position vector <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Given the initial condition that at time t = 0, e<sup>it</sup> is 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, the only trajectory for which the velocity is always a 90-degree rotation of the position is movement around a circle of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This implies:
*   After pi seconds, having traced a distance of pi around the circle, e<sup>iπ</sup> should be -1 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   After tau seconds (2π), having completed a full circle, e<sup>iτ</sup> equals 1 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   More generally, e<sup>it</sup> equals a number that is `t` radians around the unit circle in the [[complex_numbers_in_mathematics | complex plane]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

The notation e<sup>t</sup>, particularly with an [[the_concept_of_imaginary_numbers | imaginary]] exponent, can seem confusing, as it gives the number `e` and the idea of repeated multiplication more emphasis than they might deserve in this context <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.