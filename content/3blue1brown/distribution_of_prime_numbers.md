---
title: Distribution of prime numbers
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The observation of patterns related to the [[prime_numbers_distribution_and_computational_methods | distribution of prime numbers]] and rational approximations for pi was first presented in a question on the Math Stack Exchange by a user named Dwymark and answered by Greg Martin <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This pattern involves plotting points in polar coordinates where both the radius (r) and the angle (theta) are set to a given prime number <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The angle is measured in radians, where pi represents a half-turn and 2pi a full circle <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Initial Observations

When all whole numbers are plotted in this manner, they form an [[archimedean_spiral_formation_from_prime_numbers | Archimedean spiral]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Each step forward increases the distance from the origin by one unit and rotates the point by one radian <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

When this visualization is limited to just [[prime_numbers_and_their_regularities | prime numbers]], the initial plot appears random, consistent with the known chaotic behavior of primes <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. However, zooming out reveals distinct "galactic-seeming spirals" with missing arms <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Further zooming out transforms these spirals into outward-pointing rays, often appearing in clumps of four <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

It is important to note that the presence of these spirals is not unique to prime numbers; similar spirals are observed when plotting all whole numbers, indicating that the spiral formation is separate from the characteristics of primes <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The question then becomes what happens when the view *is* limited to primes <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Explaining the Patterns: Residue Classes Modulo N

The observed patterns are explained by the concept of residue classes modulo N.

### Modulo 6 Spirals

At a smaller scale, six distinct spirals are visible when plotting all whole numbers <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Each arm of these spirals corresponds to a residue class modulo 6 <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. This is because 6 radians is approximately one full turn (2pi) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

When the plot is filtered for primes, all but two of these spiral arms disappear <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This occurs because, with the exceptions of 2 and 3, prime numbers cannot be:
*   Multiples of 6 (e.g., 6, 12, 18, ...) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
*   Two or four above a multiple of 6 (i.e., even numbers like 8, 10, 14, 16, ...) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>
*   Three above a multiple of 6 (i.e., multiples of 3 like 9, 15, 21, ...) <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>

Therefore, prime numbers (excluding 2 and 3) must fall into residue classes 1 or 5 modulo 6 <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Modulo 44 Spirals

At a larger scale, 44 spirals are observed for all whole numbers <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This is due to 44 radians being very close to 7 full turns (44 / (2 * pi) ≈ 7.0028) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This approximation is related to the famous [[relation_between_pi_and_prime_numbers | 22/7 approximation for pi]] <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. Each of these 44 spiral arms corresponds to a residue class modulo 44 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

When filtered for primes, only 20 of these spiral arms remain <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Primes are excluded from residue classes that share common factors with 44 (which is 2 * 2 * 11). For example, primes cannot be:
*   Multiples of 44 <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>
*   Even numbers (residues like 2, 4, 6, ...) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
*   Multiples of 11 (residues like 11, 22, 33, ...) <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>

The remaining spiral arms correspond to residue classes that are "relatively prime" or "co-prime" to 44, meaning they share no prime factors with 44 <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The count of such numbers between 1 and 44 is 20, which is denoted by Euler's totient function, φ(44) = 20 <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

### Modulo 710 Rays

At an even larger scale, the spirals appear as nearly straight lines, or "rays" <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. This is because 710 radians is extremely close to a whole number of full turns (710 / (2 * pi) ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This relates to the highly accurate [[relation_between_pi_and_prime_numbers | 355/113 approximation for pi]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Each of these rays represents a residue class modulo 710 <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

When filtered for primes, the number of visible rays is 280 <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, corresponding to the numbers from 1 to 710 that are co-prime to 710 (φ(710) = 280) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. The factors of 710 are 71, 5, and 2 <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Residue classes divisible by these factors (e.g., even numbers, multiples of 5, multiples of 71) contain almost no primes and thus appear as gaps <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. This explains the clumps of four rays and the occasional "missing tooth" <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Dirichlet's Theorem on Arithmetic Progressions

The apparent even distribution of primes among the remaining residue classes, after filtering out those with obvious common factors, is a profound observation <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This phenomenon is explained by [[Dirichlets_theorem_in_number_theory | Dirichlet's theorem on arithmetic progressions]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

For example, when considering primes modulo 10, primes larger than 5 must end in 1, 3, 7, or 9 <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. [[Dirichlets_theorem_in_number_theory | Dirichlet's theorem]] states that as one considers more and more primes, the proportion of primes ending in each of these digits approaches 25% <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

More generally, for any modulus 'n' and any 'r' co-prime to 'n', the proportion of primes less than 'x' that have a residue of 'r' modulo 'n' approaches 1/φ(n) as 'x' approaches infinity <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. This means that primes are asymptotically equally distributed among all residue classes that are co-prime to the modulus <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.

Dirichlet proved this theorem in 1837, marking a cornerstone in modern analytic number theory <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. The proof heavily relies on complex analysis, illustrating the deep connections between continuous mathematics and the discrete world of prime numbers <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Understanding the [[prime_numbers_distribution_and_computational_methods | distribution of primes]] in residue classes remains relevant in modern research, contributing to breakthroughs in areas like the twin prime conjecture <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.