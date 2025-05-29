---
title: Exponential growth and decay
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The function `e^t` is fundamental in understanding [[exponential_growth | exponential growth]] and decay, often described by its most important defining property: it is its own derivative <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Coupled with the condition that inputting `0` returns `1` (`e^0 = 1`), it is the unique function possessing this characteristic <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Intuitive Understanding: Position and Velocity

A physical model helps illustrate the meaning of `e^t` being its own derivative <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. If `e^t` represents your position on a number line as a function of time, you start at the number `1` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The property means your velocity (the derivative of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This implies that the farther you are from `0`, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

This relationship between position and velocity paints a strong intuitive picture of how the function grows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. You know you will be accelerating, and at an accelerating rate, leading to a feeling of things rapidly getting "out of hand" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This is the essence of [[exponential_growth | exponential growth]].

### Modifying the Exponent: `e^(kt)`

When a constant `k` is added to the exponent, such as `e^(2t)`, the [[Derivatives of exponential functions | chain rule]] indicates that the derivative becomes `k` times itself <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a> <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   **[[exponential_growth | Exponential Growth]] (k > 0):** If `k` is positive (e.g., `e^(2t)`), your velocity is `k` times your position <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This makes the "runaway growth" feel even more out of control <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **[[exponential_decay | Exponential Decay]] (k < 0):** If `k` is negative (e.g., `e^(-0.5t)`), your velocity vector is `k` times your position vector <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This means the vector is flipped 180 degrees and its length scaled by `|k|` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Moving in this way causes you to go in the opposite direction, slowing down in an [[exponential_decay | exponential decay]] towards `0` <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Complex Exponents: `e^(it)`

If the constant `k` is an imaginary number, specifically `i` (the square root of negative 1), the situation changes <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If your position is `e^(it)`, its derivative is always `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Multiplying by `i` has the effect of rotating numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. To make sense of this, one must think beyond the number line and in the complex plane <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

For any position `e^(it)` might yield, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Starting at `e^(i*0) = 1` (our initial condition) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a> <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, the only trajectory where your velocity always matches a 90-degree rotation of your position is when you go around a circle of radius `1` at a speed of `1` unit per second <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Examples of this motion include:
*   After `pi` seconds, you've traced a distance of `pi` around, so `e^(i*pi)` should be `-1` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   After `tau` seconds, you've gone a full circle, so `e^(i*tau)` equals `1` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a> <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   More generally, `e^(it)` equals a number that is `t` radians around the unit circle in the complex plane <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

> [!NOTE] Notation
> The notation `e^t` itself is considered by some to be a "notational disaster," giving the number `e` and the idea of repeated multiplication more emphasis than they might deserve <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.