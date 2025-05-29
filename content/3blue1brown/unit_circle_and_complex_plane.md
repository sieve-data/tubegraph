---
title: unit circle and complex plane
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The behavior of the exponential function `e^t` can be understood by examining its defining property: it is its own derivative, meaning its velocity is always equal to its position <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If `e^t` describes a position on a number line, starting at 1, then the velocity is always equal to that position, leading to accelerating growth <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. When a constant is added to the exponent, such as `e^(2t)`, its derivative becomes `2 * e^(2t)`, meaning the velocity is twice the position, leading to even faster growth <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. If the constant is negative, like `e^(-0.5t)`, the velocity vector is flipped 180 degrees and scaled, causing exponential decay towards zero <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Exponential Function with an Imaginary Exponent

When the constant in the exponent is `i`, the [[introduction_to_complex_numbers | imaginary number]] (the square root of -1), the behavior changes dramatically <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. For a position described by `e^(it)`, its derivative is always `i` times itself <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

### The Role of 'i' in Rotation

Multiplying a [[geometric_interpretation_of_complex_numbers | complex number]] by `i` has the effect of rotating that number 90 degrees <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. This means that to understand `e^(it)`, one must think beyond the number line and in the [[geometric_interpretation_of_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

### Movement on the Complex Plane

If `e^(it)` describes a position in the [[geometric_interpretation_of_complex_numbers | complex plane]], the velocity at any given time `t` will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

This can be visualized as a vector field where the velocity vector is always perpendicular to the position vector <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

The initial condition for `e^(it)` at `t = 0` is 1 <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. The only trajectory starting from 1 where the velocity is always a 90-degree rotation of the position is movement around a [[sine_and_cosine_on_the_unit_circle_and_angles | circle]] of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This is precisely the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] in the [[geometric_interpretation_of_complex_numbers | complex plane]].

### Connection to Angles and Radians

*   After `pi` seconds, having traced a distance of `pi` around the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]], `e^(i*pi)` is -1 <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
*   After `tau` seconds (where `tau = 2pi`), having completed a full circle, `e^(i*tau)` is 1 <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   More generally, `e^(it)` represents a [[complex numbers and imaginary exponents | complex number]] that is `t` radians around the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] in the [[geometric_interpretation_of_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

The notation `e^t` is considered by some to be a "notational disaster" for its emphasis on the number `e` and repeated multiplication, especially when considering [[complex numbers and imaginary exponents | imaginary exponents]] <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.