---
title: Eulers formula and unit circle
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The function `e^t` possesses a unique and defining property: it is its own derivative <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Coupled with the condition that `e^0 = 1`, it is the only function that satisfies these criteria <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This fundamental characteristic can be illustrated with a physical model <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Understanding `e^t` through Motion

Consider `e^t` as describing your position on a number line over time <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Starting Point**: You begin at the number 1 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Velocity**: The derivative of position (velocity) is always equal to your current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means the farther you are from 0, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This relationship creates an intuitive picture of the function's accelerating growth <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Modifying the Exponent: `e^(kt)`

The behavior of the function changes when a constant `k` is introduced into the exponent, resulting in `e^(kt)`:

*   **Positive Constant (e.g., `e^(2t)`)**: The derivative becomes `k` times itself, meaning the velocity is `k` times the position <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For `e^(2t)`, your velocity is always twice your position, leading to an even more rapid, "runaway" growth <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Negative Constant (e.g., `e^(-0.5t)`)**: If `k` is negative, your velocity vector is `k` times your position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This effectively flips the direction of motion by 180 degrees and scales its length <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. As a result, you move in the opposite direction, slowing down in an [[importance_of_eulers_number_e_in_calculus|exponential decay]] towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The Introduction of `i` and [[eulers_formula_and_its_significance|Euler's Formula]]

A crucial insight into [[eulers_formula_and_its_significance|Euler's formula]] comes when the constant in the exponent is the imaginary unit `i` (the square root of -1) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### `e^(it)` in the Complex Plane
If your position is `e^(it)`, the derivative (velocity) will always be `i` times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. A key property of multiplying by `i` is that it rotates numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

This implies that understanding `e^(it)` requires thinking beyond the number line and into the complex plane <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. For any position `e^(it)` gives at a specific time `t`, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Trajectory on the Unit Circle
With an initial condition of `e^(i*0) = 1` <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, there is only one trajectory where the velocity consistently matches a 90-degree rotation of the position <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This trajectory describes moving around a [[understanding_sine_and_cosine_using_unit_circles|unit circle]] (a circle with radius 1) at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

*   After `pi` seconds, having traced a distance of `pi` around the circle, `e^(i*pi)` is negative 1 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This leads to the famous [[eulers_formula_and_its_significance|Euler's identity]]: `e^(i*pi) = -1`.
*   After `tau` (2*pi) seconds, you've completed a full circle, so `e^(i*tau) = 1` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   More generally, `e^(it)` represents a number that is `t` radians around the [[understanding_sine_and_cosine_using_unit_circles|unit circle]] in the complex plane <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

> [!NOTE] Notation
> The notation `e^t` can be seen as misleading, as it overemphasizes the number `e` and repeated multiplication when dealing with complex exponents <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.