---
title: Rational approximations for pi
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The patterns observed when plotting prime numbers in polar coordinates reveal insights into [[Approximation of functions using Taylor series | rational approximations for pi]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This visualization method, where points are labeled with a distance from the origin (radius `r`) and an angle (`theta`) measured in radians, provides a unique way to understand these mathematical relationships <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. In radians, an angle of pi (π) represents halfway around a circle, and 2 pi (2π) represents a full circle <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Adding 2π to the angle coordinate does not change the point's location <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Visualizing Approximations

When plotting points where both the radius and angle are a given whole number (e.g., (1,1), (2,2), (3,3)), these points spiral outwards, forming an Archimedean spiral <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. Each step forward increases the angle by one radian and the distance by one unit <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. The emergence of distinct spiral arms at different scales is directly tied to how closely certain integers approximate a multiple of 2π.

### The 6-Radian Approximation

At a smaller scale, six distinct spiral arms can be observed in the plot of all whole numbers <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. This occurs because six radians is slightly less than a full turn (2π radians) <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Therefore, every sixth point in the sequence returns to approximately the same angular position, creating the illusion of a continuous curving line <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. Each of these spiral arms corresponds to a "residue class mod 6" <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

### The 22/7 Approximation for Pi

Zooming out further, a different pattern emerges with 44 distinct spirals <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. This phenomenon is due to the fact that taking 44 steps, turning 44 radians, is very close to a whole number of turns <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. Specifically, 44 radians equates to 44 divided by 2π rotations, which is just over 7 full turns (approximately 7.0069 rotations) <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.

This implies that 44/7 is a close approximation for 2π, which is more commonly recognized as the famous [[Approximation of functions using Taylor series | 22/7 approximation for pi]] <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. Because 44 is very close to 7 * 2π, when counting up by multiples of 44, each point has almost the same angle as the last, resulting in a very gentle spiral that appears as a distinct arm <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. Each of these 44 spiral arms represents a residue class mod 44 <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

### The 355/113 Approximation for Pi

At an even larger scale, the spirals give way to outward-pointing rays <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. This is explained by an even more precise [[Approximation of functions using Taylor series | rational approximation for pi]]: 355/113 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This approximation is unusually good <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

The visual effect comes from the fact that 710 radians (which is 2 * 355 radians) is extremely close to a whole number of full turns <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Performing the calculation, 710 radians divided by 2π rotations equals approximately 113.000095 rotations <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This means that when moving forward by steps of 710, the angle of each new point is almost exactly the same as the last, just microscopically bigger <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Consequently, these sequences appear as nearly straight lines, which are actually very gentle spirals <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. The fact that it takes so long for the spiral to become prominent is a testament to how good this approximation for 2π is <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Unusually Good Approximations

These specific [[Approximation of functions using taylor series | rational approximations for pi]] (22/7 and 355/113) are considered "unusually good" because they are significantly more accurate than one might expect for other famous irrational numbers like phi or the square root of 2 <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Understanding the origin of such approximations and what makes them unusually good often involves studying concepts like continued fractions <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

## Relation to Prime Numbers

While the patterns of spirals and rays are primarily explained by these [[Approximation of functions using Taylor series | rational approximations for pi]], the initial visualization specifically involved prime numbers <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The absence of certain spiral arms or rays when only primes are plotted is due to divisibility rules <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. For example, primes cannot be multiples of 44 (except for 2 and 11), nor can they fall into residue classes that share common factors with 44 (e.g., even numbers or multiples of 11) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This filtering effect of prime numbers reveals the underlying structure created by the approximations <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

Euler's totient function (phi, φ) quantifies the number of integers coprime to a given number 'n' (i.e., not sharing any prime factors with n) <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. For example, φ(44) = 20, which corresponds to the 20 visible spirals when filtering for primes using the 44-radian approximation <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. Similarly, for the 710-radian approximation, the number of visible rays (280) is equal to φ(710) <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. The distribution of primes within these remaining residue classes is described by Dirichlet's theorem on arithmetic progressions <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.