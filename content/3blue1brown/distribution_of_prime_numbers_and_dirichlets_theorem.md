---
title: Distribution of prime numbers and Dirichlets theorem
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The study of [[prime_numbers_and_density | prime numbers]] often involves exploring their distribution. A unique pattern emerges when [[prime_numbers_and_their_regularities | prime numbers]] are visualized using polar coordinates, leading to insights into a fundamental theorem in number theory known as Dirichlet's theorem <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Visualizing Primes in Polar Coordinates

The initial observation of this pattern came from a question on the Math Stack Exchange asked by user Dwymark and answered by Greg Martin <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This visualization uses polar coordinates, where points in 2D space are labeled by their distance from the origin (`r` for radius) and the angle (`theta`) that radial line makes with the horizontal <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. For this visualization, the angle is measured in radians, where pi (π) is halfway around and 2π is a full circle <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Polar coordinates are not unique, as adding 2π to the angle does not change the point's location <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The pattern explored centers around plotting points where both the radius (`r`) and the angle (`theta`) are the same given number <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Plotting All Whole Numbers

When plotting all whole numbers (n, n) in polar coordinates:
*   The point (1,1) is at distance 1 with an angle of 1 radian <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   The point (2,2) has twice that angle and twice the distance <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Each step forward involves a turn of one radian and a growth of one unit in distance <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   These points spiral outwards, forming an "archimedean spiral" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Plotting Only Prime Numbers

When only [[prime_numbers_and_their_regularities | prime numbers]] (p, p) are plotted, the initial view appears quite random <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. However, zooming out reveals clear "galactic-seeming spirals" with some arms missing <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Zooming out even further, these spirals give way to "outward-pointing rays," often appearing in clumps of four with occasional gaps <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Initially, 20 spirals were counted, and at a larger scale, 280 rays <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

It's important to note that the presence of these spirals is not unique to [[prime_numbers_and_their_regularities | prime numbers]]; they also appear when plotting all whole numbers, though they are much cleaner and more numerous (44 instead of 20) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This indicates that the origin of the spirals is separate from the filtering by primes <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Explaining the Spiral Patterns: Residue Classes

The formation of these spiral arms is explained by the concept of residue classes.

### Smaller Scale: Modulo 6

At a smaller scale, six distinct spirals are visible <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Each spiral arm corresponds to a "residue class mod 6" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. "Residue" refers to the remainder, and "mod" indicates the number being divided by <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. For example, 20 has a residue of 2 mod 6 <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. These spirals appear because 6 radians is approximately a full turn (2π radians) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

When filtering for [[prime_numbers_and_their_regularities | prime numbers]], most of these arms disappear:
*   Primes (except 2 and 3) cannot be multiples of 6, or 2 or 4 above a multiple of 6 (all even numbers) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   Primes (except 3) cannot be 3 above a multiple of 6 (all divisible by 3) <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   Therefore, only two arms remain visible: primes that are 1 or 5 above a multiple of 6 (with exceptions for 2 and 3) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Larger Scale: Modulo 44

The 44 spirals observed at a larger scale arise because 44 steps (44 radians) is very close to a whole number of turns (7 full turns, specifically 44 / (2π) ≈ 7.0028) <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This relates to the famous rational approximation for [[pi_and_its_formulas_involving_primes | pi]], 22/7 <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Each of these spiral arms corresponds to a residue class mod 44 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

When filtering for [[prime_numbers_and_their_regularities | prime numbers]]:
*   Primes cannot be multiples of 44, or 2, 4, etc., above a multiple of 44 (even numbers) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   Primes (except 11) cannot be multiples of 11, such as 11 or 33 above a multiple of 44 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   The remaining spirals are residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   Numbers that do not share any prime factors are called [[eulers_totient_function_and_relative_primality | relatively prime]] or co-prime <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   There are 20 such numbers between 1 and 44 that are co-prime to 44. This is compactly written as φ(44) = 20, where φ (phi) is [[eulers_totient_function_and_relative_primality | Euler's totient function]] <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The numbers themselves are sometimes called "totitives" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### Largest Scale: Modulo 710

The "straight lines" observed at the largest scale arise because 710 radians is extremely close to a whole number of full turns (113 full turns, specifically 710 / (2π) ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This relates to the very good rational approximation for [[pi_and_its_formulas_involving_primes | pi]], 355/113 <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. When steps of 710 are taken, the angle of each new point is almost exactly the same as the last, appearing as nearly straight lines <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

The factors of 710 are 71, 5, and 2 <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. When filtering for primes:
*   Residue classes divisible by 2 (even numbers) disappear, explaining the "every other ray" pattern <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   Residue classes divisible by 5 disappear, explaining why the lines come in clumps of four <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
*   Residue classes divisible by 71 disappear, explaining occasional gaps in the clumps of four <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The total number of remaining rays, 280, is φ(710), representing the numbers from 1 to 710 that do not share any prime factors with 710 <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

## Dirichlet's Theorem on Arithmetic Progressions

The most interesting observation is that primes appear to be fairly evenly distributed among the remaining residue classes <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This relates to [[prime_numbers_and_their_regularities | Dirichlet's theorem]], a deep fact in number theory <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

Consider residue classes mod 10, which correspond to the last digit of a number <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Primes (other than 2 and 5) must end in 1, 3, 7, or 9 <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. A histogram of primes by their last digit shows that as more primes are considered, they are spread almost evenly among these four classes, about 25% each <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

This pattern holds generally:
*   **Dirichlet's Theorem**: For any number `n` and any integer `r` that is [[eulers_totient_function_and_relative_primality | co-prime]] to `n` (i.e., `gcd(r, n) = 1`), the proportion of [[prime_numbers_and_density | prime numbers]] less than `x` that have a residue of `r` mod `n` approaches `1 / φ(n)` as `x` approaches infinity <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   This means that primes are just as dense in any one of these allowable residue classes as in any other <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   Combined with Euclid's proof that there are infinitely many primes, Dirichlet's theorem implies that there are infinitely many primes in each of these residue classes <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

The proof of Dirichlet's theorem, first achieved in 1837, heavily relies on complex analysis <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This connection between the continuous world of calculus (with complex numbers) and the discrete world of [[prime_numbers_and_density | prime numbers]] is a cornerstone of modern analytic number theory <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Understanding the [[prime_numbers_and_density | distribution of primes]] in residue classes remains relevant in modern research, influencing breakthroughs on topics like small gaps between primes and the twin-prime conjecture <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

This exploration demonstrates how seemingly arbitrary data visualization can lead to deep and important mathematical facts like Dirichlet's theorem, which connects to many other areas of mathematics <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.