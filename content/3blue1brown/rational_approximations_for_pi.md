---
title: Rational approximations for pi
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The phenomenon of spiral patterns emerging when plotting numbers in polar coordinates, where both the radius and angle correspond to the same number (e.g., a prime number), is intimately linked with [[Pi and its formulas involving primes | rational approximations for pi]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. In this visualization, points are plotted using polar coordinates `(r, θ)`, where `r` is the distance from the origin and `θ` is the angle in radians <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. A full circle is `2π` radians <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The appearance of these patterns is due to certain integers being very close to a whole number of `2π` rotations <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. When a number `N` of radians is plotted, if `N` is close to `k * 2π` (where `k` is an integer), then `N / (2k)` is a good rational approximation for pi.

## Approximations Leading to Spiral Patterns

### The 22/7 Approximation

A prominent spiral pattern observed when plotting all whole numbers (not just primes) reveals 44 distinct spirals <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This occurs because 44 steps, representing 44 radians, is very close to a whole number of turns <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

Specifically:
*   44 radians divided by `2π` rotations is approximately 7.000000000... <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   This means that `44/7` is a close approximation for `2π` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   Consequently, `22/7` is recognized as a famous [[approximations_and_limits_in_geometry | approximation for pi]] <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

When numbers are plotted in steps of 44, each point has almost the same angle as the last, resulting in a very gentle spiral <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. This illustrates how residue classes modulo 44 correspond to these spiral arms <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### The 355/113 Approximation

At an even larger scale, plotting the numbers reveals a pattern of outward-pointing rays <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This phenomenon is tied to another highly accurate rational approximation of pi:

*   710 radians is extremely close to a whole number of full turns <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   Analytically, 710 radians is `710 / (2π)` rotations, which evaluates to approximately 113.000095 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   This implies that `710/113` is a close approximation for `2π` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   Dividing by two, `355/113` is known as a very good [[approximations_and_limits_in_geometry | approximation for pi]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

When moving in steps of 710, the angle of each new point is microscopically bigger than the last, causing the sequences to appear as nearly straight lines, even at very large scales <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The fact that it takes so long for the spiral to become prominent is a strong illustration of how good this approximation is for `2π` <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

## Significance of "Unusually Good" Approximations

The concept of "unusually good" rational approximations for pi, such as 355/113, is a notable aspect of number theory. These approximations are significantly better than what might be expected for other famous irrational numbers like `e` or the square root of 2 <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. Understanding the origin and quality of these approximations often involves the study of continued fractions <a class="yt-timestamp" data-t="00:21:37">[00:21:37]</a>.

The visual patterns serve as a compelling illustration of these mathematical facts <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Although the initial data visualization might seem arbitrary, it leads to significant mathematical concepts, such as Dirichlet's theorem on arithmetic progressions, by prompting questions about the distribution of prime numbers within these patterns <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.