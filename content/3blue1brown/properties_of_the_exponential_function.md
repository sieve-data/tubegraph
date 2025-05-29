---
title: Properties of the exponential function
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The exponential function, often denoted as e^t, can be understood by examining its fundamental properties <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Self-Derivative Property

The most crucial property of the function e^t is that it is its own [[derivatives_of_exponential_functions | derivative]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This means that the rate of change of the function at any point is equal to the value of the function at that point <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Combined with the initial condition that inputting 0 returns 1 (e^0 = 1), this property uniquely defines the function <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Physical Analogy: Position and Velocity

To illustrate this property, consider e^t as describing your position on a number line over time <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   You begin at the position 1 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   Your velocity (the [[derivatives_of_exponential_functions | derivative]] of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   This implies that the farther you are from 0, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

This relationship provides a strong [[Intuition behind the growth of exponential functions | intuitive picture]] of how the function grows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. You will be accelerating, and at an accelerating rate, leading to a feeling of things getting "out of hand quickly" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This behavior is characteristic of [[exponential growth | exponential growth]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Effect of a Constant in the Exponent (e^(kt))

When a constant `k` is added to the exponent, such as in e^(2t), the [[derivatives_of_exponential_functions | derivative]] changes due to the chain rule <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   The derivative of e^(kt) is `k` times itself <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Positive Constant (k > 0)
If `k` is a positive constant (e.g., e^(2t)), your velocity is always `k` times your position <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. For e^(2t), your velocity is twice your position <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This means the "runaway growth" feels even more out of control <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This relationship between velocity and position is an example of a [[Proportionality constants in exponential functions | proportionality constant]] in the growth rate.

### Negative Constant (k < 0)
If `k` is a negative constant (e.g., e^(-0.5t)), your velocity vector is always `k` times your position vector <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This means:
*   The velocity vector is flipped 180 degrees from the position vector <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   Its length is scaled by the absolute value of `k` (e.g., by half for -0.5) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
Moving under these conditions means you go in the opposite direction, slowing down in an [[exponential growth and decay | exponential decay]] towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Imaginary Constant in the Exponent (e^(it))

When the constant in the exponent is the imaginary unit `i` (the square root of negative 1), as in e^(it) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:
*   The [[derivatives_of_exponential_functions | derivative]] of your position is always `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Multiplying a number by `i` has the effect of rotating it 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Movement in the [[Complex plane and exponential functions | Complex Plane]]
This scenario makes sense only when considering movement beyond a simple number line and into the [[Complex plane and exponential functions | complex plane]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   For any position e^(it) might take, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   With an initial condition of e^(i*0) = 1, the trajectory is a circle of radius 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   The movement occurs at a speed of 1 unit per second around this unit circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Examples:
*   After pi seconds, e^(i*pi) = -1, as you've traced a distance of pi around the circle <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   After tau (2*pi) seconds, e^(i*tau) = 1, as you've completed a full circle <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   In general, e^(it) equals a number that is `t` radians around the unit circle in the [[Complex plane and exponential functions | complex plane]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The notation "e to the t" can be considered a "notational disaster" because it places undue emphasis on the number `e` and the idea of repeated multiplication, which can be misleading when dealing with imaginary exponents <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.