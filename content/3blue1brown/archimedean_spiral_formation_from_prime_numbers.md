---
title: Archimedean spiral formation from prime numbers
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

A fascinating pattern observed when plotting numbers in polar coordinates, initially found on the Math Stack Exchange by user Dwymark and answered by Greg Martin, reveals connections between the [[distribution_of_prime_numbers | distribution of prime numbers]] and [[relation_between_pi_and_prime_numbers | rational approximations for pi]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This exploration involves plotting points where both the radial distance (r) and the angle (theta) correspond to a given number <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Polar Coordinates Primer

In two-dimensional space, polar coordinates define a point by its distance from the origin, `r` (radius), and the angle `theta` that its radial line makes with the horizontal <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. For this pattern, angles are measured in radians, where `pi` represents a half-turn and `2pi` represents a full circle <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. It's important to note that polar coordinates are not unique, as adding `2pi` to the angle does not change the point's location <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## The Archimedean Spiral (Whole Numbers)

To understand the observed patterns, it's helpful to first visualize the plot for all whole numbers <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   The point (1,1) is plotted at a distance of 1 unit from the origin with an angle of 1 radian <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   The point (2,2) has twice the angle and twice the distance <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   The point (3,3) involves rotating one more radian and stepping one unit farther from the origin <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Each step forward in the sequence involves a rotation of one radian and an increase of one unit in distance <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. As this continues, these points spiral outwards, forming an **Archimedean spiral** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Prime Numbers: Initial Observations

When the plot is filtered to include only prime numbers, the initial view appears quite random, reflecting the chaotic and difficult-to-predict behavior for which primes are known <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. However, zooming out reveals clear, "galactic-seeming spirals," some with missing arms <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Zooming out even further, these spirals transform into many distinct outward-pointing rays, often appearing in clumps of four with occasional gaps <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Notably, similar spirals appear when plotting all whole numbers, though they are cleaner and more numerous (44 instead of 20 for one scale) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This suggests that the spirals' origin is separate from the prime number filter, but the prime filter still leads to significant patterns <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Understanding the Patterns: Residue Classes and Pi Approximations

The formation of these spiral arms and rays is rooted in the concept of "residue classes" and close rational approximations of `2pi`.

### Residue Classes Modulo N

Each spiral arm corresponds to a sequence of numbers sharing the same remainder when divided by a specific number. This is called a **residue class mod n** <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, numbers that are 1 above a multiple of 6 form a residue class mod 6 <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Mod 6 Spirals**: Six small spirals are initially visible <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This occurs because 6 radians is slightly less than a full turn (2pi) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. When filtering for primes, most of these arms disappear because primes (except for 2 and 3) cannot be multiples of 6, or 2, 3, or 4 above a multiple of 6 <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Only numbers 1 or 5 above a multiple of 6 remain <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

*   **Mod 44 Spirals**: At a larger scale, 44 spirals appear <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This is because 44 radians is very close to 7 full turns (44 / 2pi ≈ 7.000095), indicating that 44/7 is a close approximation for 2pi, or 22/7 for pi <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. When limiting to primes, many of these spirals disappear. For example, residue classes that are even or multiples of 11 (factors of 44) will contain few or no primes (except for 2 and 11 themselves) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. The remaining spirals correspond to residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

*   **Mod 710 Rays**: At the largest scale, the patterns appear as straight lines, or rays <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This is because 710 radians is extremely close to 113 full turns (710 / 2pi ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This relates to the highly accurate [[relation_between_pi_and_prime_numbers | rational approximation for pi]] of 355/113 <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. Because the angle changes microscopically with each step of 710, the sequences appear as nearly straight lines <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. Filtering for primes again removes residue classes that share common factors with 710 (factors are 2, 5, 71) <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This explains the observed clumps of four rays and occasional missing "teeth" in the pattern <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

### Euler's Totient Function (Phi)

The number of spiral arms (or rays) that remain visible after filtering for primes is given by **Euler's totient function**, denoted as `phi(n)`. This function counts the number of integers from 1 up to `n` that are "co-prime" (or "relatively prime") to `n`, meaning they do not share any prime factors with `n` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. For instance, `phi(44) = 20`, which is why 20 spirals were visible when filtering for primes <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Similarly, `phi(710) = 280`, explaining the 280 rays <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. These numbers are sometimes called "totitives" of n <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## Dirichlet's Theorem on Arithmetic Progressions

A key observation from these visualizations is that the primes, after filtering out non-co-prime residue classes, appear to be roughly evenly distributed among the remaining classes <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This empirical observation is a profound fact in number theory formally stated by **Dirichlet's theorem on arithmetic progressions** <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

For any modulus `n` and any integer `r` that is co-prime to `n`, the theorem states that the proportion of primes less than some large number `x` that fall into the residue class `r mod n` approaches `1 / phi(n)` as `x` approaches infinity <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. This means that primes are asymptotically equally distributed among all valid residue classes <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

This theorem ensures that not only do infinitely many primes exist in these classes (a weaker form of the theorem), but they are also distributed with equal density <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. The proof of Dirichlet's theorem heavily relies on complex analysis, illustrating how seemingly unrelated fields of mathematics, like calculus with complex numbers, are crucial for understanding the [[distribution_of_prime_numbers | distribution of prime numbers]] <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This understanding of [[prime_numbers_distribution_and_computational_methods | prime numbers distribution]] in residue classes remains relevant in modern research, such as breakthroughs related to small gaps between primes and the twin-prime conjecture <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

## The Value of Mathematical Exploration

While the specific data visualization of plotting (p,p) in polar coordinates might seem arbitrary <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>, this kind of playful exploration can lead to deeper mathematical inquiries <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. The fact that an arbitrary exploration can lead to significant and deep mathematical facts like Dirichlet's theorem highlights that important math connects to many other topics <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>. Such rediscovery can foster a deeper understanding and appreciation for these mathematical concepts, seeing them as familiar friends rather than abstract definitions <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.