---
title: Polar coordinates and spiral patterns
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

This article explores the fascinating visual patterns that emerge when plotting numbers, particularly prime numbers, in polar coordinates. The patterns reveal surprising connections to rational approximations of [[pis_relationship_to_circles_and_geometry | pi]] and fundamental theorems in number theory, such as Dirichlet's theorem <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Introduction to Polar Coordinates

Polar coordinates are a system for labeling points in two-dimensional space <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Instead of using the familiar `xy` Cartesian coordinates, points are defined by:
*   **r (radius):** The distance from the origin <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **theta (angle):** The angle that the radial line makes with the horizontal axis, measured in radians <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. An angle of pi radians is halfway around a circle, and 2pi is a full circle <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

It's important to note that polar coordinates are not unique; adding 2pi to the angle `theta` does not change the point's location <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The patterns discussed here originated from a Math Stack Exchange question by user Dwymark <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core idea is to plot points where both the radius `r` and the angle `theta` are a given number, such as a prime number <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Archimedean Spiral from Whole Numbers

To understand the plotting method, consider all whole numbers (1, 2, 3, ...).
*   The point (1,1) is plotted at a distance of 1 unit from the origin with an angle of 1 radian <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   The point (2,2) is at twice the distance and twice the angle <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   The point (3,3) is at three times the distance and three times the angle <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Each subsequent point involves rotating one more radian and stepping one unit farther away from the origin <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. As this process continues, the points form an outward spiraling shape known as an **Archimedean spiral** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Prime Number Patterns

When only prime numbers are plotted (e.g., (2,2), (3,3), (5,5), etc.), the initial result appears random due to the unpredictable nature of primes <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. However, zooming out reveals distinct patterns:
*   **Galactic-seeming spirals:** At an intermediate zoom, clear [[slone_galactic_survey_and_galaxy_mapping | galactic-seeming spirals]] emerge, with some arms appearing to be missing <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. There are 20 such spirals <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Outward-pointing rays:** Zooming out further, these spirals give way to many distinct outward-pointing rays, often appearing in clumps of four with occasional gaps <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. There are 280 such rays <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

The presence of these patterns, especially given their connection to prime numbers, seems mysterious <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Unpacking the Mystery: Residue Classes and Approximations of Pi

The existence of the spirals is not unique to prime numbers; they are also visible when plotting all whole numbers, though they appear cleaner and more numerous (44 instead of 20) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This indicates that the spirals' origin is separate from the prime number filter, though the filtering itself leads to profound insights <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The patterns arise from specific rational approximations of [[pis_relationship_to_circles_and_geometry | 2pi]].

### Modulo 6 Spirals

A smaller scale reveals six distinct spirals <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Each arm corresponds to integers sharing the same remainder when divided by 6. For example, all multiples of 6 form one arm <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

This occurs because 6 radians is slightly less than 2pi (a full turn) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. So, every 6 steps, the angle nearly completes a full turn, creating a gentle spiral <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

*   **Residue Classes:** Each of these sequences (e.g., numbers that are 2 above a multiple of 6) is called a **residue class mod 6** <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. "Residue" means remainder, and "mod" refers to the number being divided by <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Primes and Mod 6:** When filtering for primes, only two spiral arms remain (with exceptions for 2 and 3) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This is because prime numbers (other than 2 and 3) cannot be multiples of 6, or 2, 3, or 4 above a multiple of 6 <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Primes larger than 3 must be 1 or 5 above a multiple of 6 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Modulo 44 Spirals (The "Galactic" Spirals)

The 44 spirals observed at the intermediate zoom arise because 44 radians is very close to 7 full turns (44 / (2pi) ≈ 7.0028) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This means 44/7 is a close approximation for [[pis_relationship_to_circles_and_geometry | 2pi]], or 22/7 for [[pis_relationship_to_circles_and_geometry | pi]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Similar to mod 6, each of these 44 spiral arms corresponds to a residue class mod 44 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   **Primes and Mod 44:** When filtering for primes, many residue classes disappear <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. Primes cannot be multiples of 44, or multiples of 2 or 11 (the prime factors of 44), unless they are 2 or 11 themselves <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The remaining spirals correspond to residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Relatively Prime / Co-prime:** Two numbers that don't share any prime factors are called **relatively prime** or **co-prime** <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Euler's Totient Function (Phi):** The number of integers between 1 and `n` that are co-prime to `n` is given by Euler's totient function, denoted `phi(n)` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. For example, `phi(44) = 20`, explaining why 20 spirals remain <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Modulo 710 Rays (The "Straight Lines")

At the largest scale, the patterns appear as nearly straight lines <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. This is because 710 radians is extremely close to a whole number of full turns (710 / (2pi) ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This means 355/113 is a very good approximation for [[pis_relationship_to_circles_and_geometry | pi]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

When moving in steps of 710, the angle of each new point is almost exactly the same as the last, leading to the illusion of straight lines <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Primes and Mod 710:** The prime factors of 710 are 2, 5, and 71 <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Residue classes divisible by these factors (unless it's the prime itself) will contain no primes and disappear <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
    *   The absence of even numbers leaves every other ray missing <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
    *   The absence of multiples of 5 explains the "clumps of 4" <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   The absence of multiples of 71 explains the "missing teeth" in these clumps <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The number 280 (of rays) comes from `phi(710)`, which counts the numbers from 1 to 710 that don't share prime factors with 710 <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

## Dirichlet's Theorem

A crucial observation from these visualizations is that prime numbers appear to be quite evenly distributed among the remaining allowable residue classes <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This empirical observation is formalized by **Dirichlet's Theorem on Arithmetic Progressions** <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

The theorem states that for any given modulus `n` and any integer `r` that is co-prime to `n`, there are infinitely many prime numbers in the arithmetic progression `r, r+n, r+2n, ...` <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. More strongly, it states that the primes are asymptotically evenly distributed among these co-prime residue classes <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

For example, when looking at primes modulo 10 (based on their last digit):
*   Primes (other than 2 and 5) can only end in 1, 3, 7, or 9 <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   Dirichlet's theorem predicts that as the number of primes considered increases, the proportion of primes ending in 1, 3, 7, or 9 will each approach 1/4 (since `phi(10) = 4`) <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

In general, for any `n`, the proportion of primes up to a large number `x` that fall into a specific residue class `r mod n` (where `r` is co-prime to `n`) approaches `1 / phi(n)` as `x` approaches infinity <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

The proof of Dirichlet's theorem is complex and relies heavily on **complex analysis**, the study of calculus with complex numbers <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. This connection between the continuous world of calculus and discrete prime numbers is a hallmark of modern analytic number theory <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Dirichlet's theorem remains relevant in modern research, informing breakthroughs in areas like the study of small gaps between primes <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

## Conclusion

While the initial data visualization of `p,p` in polar coordinates might seem arbitrary <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>, this kind of playful exploration can lead to questions that uncover deep and important mathematical facts <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. The patterns observed provide a beautiful illustration of concepts like rational approximations of [[pis_relationship_to_circles_and_geometry | pi]], Euler's totient function, and the profound distribution properties of prime numbers formalized by Dirichlet's theorem <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.