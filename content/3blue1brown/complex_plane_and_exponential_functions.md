---
title: Complex plane and exponential functions
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The function *e*<sup>t</sup> is fundamentally defined by the property that it is its own [[Derivatives of exponential functions | derivative]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, coupled with the initial condition that inputting 0 returns 1 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This means if *e*<sup>t</sup> represents a position on a number line, the velocity (derivative of position) is always equal to that position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. The farther from 0 you are, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, leading to an accelerating rate of growth described as things "getting out of hand quickly" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

If a constant is added to the exponent, such as *e*<sup>2t</sup>, the chain rule dictates that its derivative becomes 2 times itself <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. In this scenario, velocity is always twice the position, intensifying the runaway growth <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Conversely, if the constant is negative (e.g., -0.5), the velocity vector becomes -0.5 times the position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This means the velocity is flipped 180 degrees and scaled by half, leading to [[Exponential growth and decay | exponential decay]] towards 0 as the position moves in the opposite direction and slows down <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Exponential Functions with Imaginary Exponents

When the constant in the exponent is the imaginary unit *i* (the square root of -1), as in *e*<sup>it</sup>, the situation shifts from a number line to the [[Complex numbers and 2D plane transformations | complex plane]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

*   The derivative of *e*<sup>it</sup> is *i* times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Multiplying a number by *i* in the complex plane has the effect of rotating it 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Therefore, for any position *e*<sup>it</sup>, the velocity at that time *t* will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Starting from the initial condition where *t* = 0, *e*<sup>i\*0</sup> = 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, the trajectory where velocity is always a 90-degree rotation of the position causes movement around a circle of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This implies:
*   After pi seconds, *e*<sup>i\*pi</sup> equals -1 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   After tau (2*pi) seconds, *e*<sup>i\*tau</sup> equals 1 (a full circle) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   More generally, *e*<sup>it</sup> represents a number that is *t* radians around the unit circle in the [[Complex plane and winding frequency | complex plane]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

This use of an imaginary number in the exponent can seem counter-intuitive, highlighting that the notation *e*<sup>t</sup>, while common, can be misleading by overemphasizing the number *e* and repeated multiplication <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.