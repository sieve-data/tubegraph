---
title: Residue classes in modular arithmetic
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

## Introduction to Residue Classes
In mathematics, particularly number theory, a "residue class" groups integers together based on their remainder when divided by a specific number <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The term "residue" is a more formal way of saying "remainder," and "mod" (short for "modulo") indicates the number by which division is performed <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

For example, when considering "mod 6," numbers are grouped by the remainder they leave when divided by 6 <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   The number 20, when divided by 6, goes in three times and leaves a remainder of 2 <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Thus, 20 is said to have a residue of 2 mod 6 <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   The **residue class mod 6** for a remainder of 2 includes 20 and all other numbers that leave a remainder of 2 when divided by 6 <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is equivalent to "everything 2 above a multiple of 6" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Visualizing Residue Classes
When points are plotted in polar coordinates (r, θ) where both r and θ are the same integer *n*, and θ is measured in radians, these sequences form distinct spiral arms <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Each of these spiral arms visually represents a residue class <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Modulo 6 Spirals
At a smaller scale, observing points where both coordinates are whole numbers, six distinct spirals emerge <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This occurs because 6 radians is approximately one full turn (2π radians) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. As you count up by 6, each point's angle is almost the same as the last, just slightly less than a full turn, creating a gently curving spiral <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Each of these spirals corresponds to a **residue class mod 6** <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### Modulo 44 Spirals
Zooming out further, a larger pattern of 44 spirals becomes visible when all whole numbers are plotted <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This phenomenon arises because 44 radians is very close to 7 full turns (44 / (2π) ≈ 7.006) <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This means 44/7 is a good rational approximation for 2π, or 22/7 for π <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Consequently, counting by multiples of 44 results in points with nearly identical angles, forming a very gentle spiral <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Each of these corresponds to a **residue class mod 44** <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### Modulo 710 Rays
At an even larger scale, the spirals appear as straight lines or "rays" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This is because 710 radians is extremely close to 113 full turns (710 / (2π) ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This close approximation (355/113 for π) means that points separated by 710 units have angles that are microscopically different, making the spiral appear as a straight line <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. These "rays" represent **residue classes mod 710** <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

## Residue Classes and Prime Numbers
When the visualization is filtered to show only [[prime_numbers_and_their_regularities | prime numbers]], many residue classes disappear <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This is due to the fundamental properties of [[prime_numbers_and_their_regularities | prime numbers]]:
*   **Mod 6:** Only two spiral arms remain visible for [[prime_numbers_and_their_regularities | prime numbers]]: those with a residue of 1 mod 6 or 5 mod 6 (with exceptions for 2 and 3 themselves) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This is because [[prime_numbers_and_their_regularities | prime numbers]] (other than 2 and 3) cannot be multiples of 6, or be 2, 3, or 4 above a multiple of 6, as they would be divisible by 2 or 3 <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Mod 44:** [[prime_numbers_and_their_regularities | Prime numbers]] cannot be multiples of 44, or be 2, 4, etc. above a multiple of 44 (even numbers) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. Similarly, they cannot be multiples of 11 (except 11 itself), so residue classes such as 11 above or 33 above a multiple of 44 are empty of [[prime_numbers_and_their_regularities | primes]] <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. The visible spirals correspond to residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

## Co-primality and [[eulers_totient_function_and_relative_primality | Euler's Totient Function]]

> **Co-primality / Relatively Prime**
> When two numbers do not share any prime factors (other than 1), they are called "relatively prime" or "co-prime" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

For a given modulus *n*, only residue classes *r mod n* where *r* is co-prime to *n* can contain infinitely many [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

[[eulers_totient_function_and_relative_primality | Euler's totient function]], denoted by φ(*n*), counts the number of positive integers up to *n* that are co-prime to *n* <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. These integers are sometimes referred to as the "totitives" of *n* <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

*   For example, φ(44) = 20 <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, meaning there are 20 numbers between 1 and 44 that are co-prime to 44 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. These 20 residue classes are the ones that can potentially contain many [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   For mod 710, φ(710) = 280 <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>, indicating 280 residue classes that are not trivially empty of [[prime_numbers_and_their_regularities | primes]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Dirichlet's Theorem on Arithmetic Progressions
A significant observation from these visualizations is that [[prime_numbers_and_their_regularities | prime numbers]] appear to be evenly distributed among the allowable residue classes <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This empirical observation is formalized by **Dirichlet's Theorem on Arithmetic Progressions** <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

The theorem states that for any integer *n* and any integer *r* that is co-prime to *n*, the proportion of [[prime_numbers_and_their_regularities | prime numbers]] less than some large number *x* that fall into the residue class *r mod n* approaches 1/φ(*n*) as *x* approaches infinity <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

*   **Example (mod 10):** [[prime_numbers_and_their_regularities | Primes]] greater than 5 can only end in digits 1, 3, 7, or 9 <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. φ(10) = 4 <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. Dirichlet's theorem implies that, in the long run, about 25% of [[prime_numbers_and_their_regularities | primes]] will end in 1, 25% in 3, 25% in 7, and 25% in 9 <a class="yt-timestamp" data-t="00:15:52">[00:15:56]</a>.
*   **Example (mod 44):** Among the 20 co-prime residue classes for mod 44, [[prime_numbers_and_their_regularities | primes]] are observed to be evenly spread, with approximately 1/20th of [[prime_numbers_and_their_regularities | primes]] appearing in each class <a class="yt-timestamp" data-t="00:17:08">[00:17:12]</a>.

The proof of Dirichlet's theorem is complex and relies heavily on [[complex_numbers_in_discrete_math | complex analysis]], which involves calculus with [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] <a class="yt-timestamp" data-t="00:19:27">[00:19:32]</a>. This connection between the continuous world of calculus and the discrete nature of [[prime_numbers_and_their_regularities | prime numbers]] has been a cornerstone of modern analytic number theory since the early 19th century <a class="yt-timestamp" data-t="00:19:44">[00:19:48]</a>. The study of [[prime_numbers_and_their_regularities | prime distribution]] within residue classes remains relevant in modern research, contributing to breakthroughs in understanding the gaps between [[prime_numbers_and_their_regularities | primes]] <a class="yt-timestamp" data-t="00:19:56">[00:20:06]</a>.