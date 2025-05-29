---
title: Complex numbers and Gaussian integers
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

This article explores the connection between [[complex_numbers_introduction | complex numbers]], prime numbers, and pi, particularly focusing on the role of Gaussian integers in deriving a formula for pi <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This relationship highlights a regularity in how prime numbers behave within the [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Geometric Interpretation and Lattice Points

When considering a problem in the 2D plane, it can be fruitful to view the plane as the set of all [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. For example, a lattice point with integer coordinates (A, B) can be thought of as a single [[complex_numbers_introduction | complex number]] A + Bi <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

The distance of a lattice point (A, B) from the origin is given by the square root of A² + B² <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This value is always the square root of some integer, since A and B are integers <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

A key question is to count how many lattice points sit inside a large circle of radius *r* <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Approximately, this count is equal to the circle's area, πr² <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. As *r* increases, the percentage error of this approximation decreases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The goal is to find an alternative way to count these lattice points, which can lead to a formula for pi <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

Counting lattice points can be approached by considering rings of various radii (square root of *n*) and summing the number of points on each ring <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The number of lattice points on a ring with radius √*n* corresponds to the number of pairs of integers (A, B) such that A² + B² = *n* <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. For example, a circle with radius √25 hits 12 lattice points <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, while a circle with radius √11 hits none, because 11 cannot be expressed as the sum of two squares <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Gaussian Integers and Complex Conjugates

The collection of all points A + Bi, where A and B are integers, are called [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Counting lattice points at a given distance from the origin is equivalent to asking how many [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers A + Bi have the property that (A + Bi)(A - Bi) = *n* <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. The term (A - Bi) is called the [[complex_numbers_introduction | complex conjugate]] of (A + Bi) <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Multiplying a [[complex_numbers_introduction | complex number]] by its [[complex_numbers_introduction | complex conjugate]] yields the sum of the squares of its coordinates (A² + B²) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This operation involves a rotation and stretch that lands the product on the positive real axis, equal to the square of the magnitude of the original [[complex_numbers_introduction | complex number]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This transforms the counting problem into a factoring problem within the [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Factoring in Gaussian Integers

Just like ordinary integers have unique prime factorizations (up to signs), [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers also exhibit an "almost unique" factorization into [[gaussian_distribution_and_the_role_of_pi | Gaussian]] primes <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. The "almost unique" aspect in [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers means factors can be multiplied by 1, -1, *i*, or -*i* without changing the overall product <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

The behavior of ordinary prime numbers when factored within the [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers depends on their remainder when divided by 4:
*   **Primes 1 (mod 4)**: Prime numbers that are one above a multiple of 4 (e.g., 5, 13, 17) can always be factored into exactly two distinct [[gaussian_distribution_and_the_role_of_pi | Gaussian]] primes that are [[complex_numbers_introduction | complex conjugate]]s (e.g., 5 = (2 + *i*)(2 - *i*)) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that rings with a radius equal to the square root of such a prime always hit lattice points, specifically 8 lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes 3 (mod 4)**: Prime numbers that are three above a multiple of 4 (e.g., 3, 7, 11) cannot be factored further within the [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers; they remain [[gaussian_distribution_and_the_role_of_pi | Gaussian]] primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This means a ring with a radius equal to the square root of such a prime will not hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The prime 2**: The prime number 2 is special; it factors as (1 + *i*)(1 - *i*) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. These two [[gaussian_distribution_and_the_role_of_pi | Gaussian]] primes are 90 degrees apart, meaning one can be obtained by multiplying the other by *i* <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Factors of 2 (or any power of 2) do not change the count of lattice points <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

### Counting Lattice Points using Gaussian Prime Factorization

To count [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers A + Bi such that (A + Bi)(A - Bi) = *n*, the process involves:
1.  Factor *n* into its [[gaussian_distribution_and_the_role_of_pi | Gaussian]] prime factors <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
2.  Organize these factors into two columns (representing a [[complex_numbers_introduction | complex number]] and its [[complex_numbers_introduction | conjugate]]) ensuring conjugate pairs are together <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The number of ways to distribute the factors that are 1 (mod 4) between these columns affects the possible outputs <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
3.  Multiply the [[gaussian_distribution_and_the_role_of_pi | Gaussian]] primes in each column. The resulting products will be a [[complex_numbers_introduction | conjugate]] pair <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
4.  Multiply the product from one column by 1, *i*, -1, or -*i* to account for all four "units" in the [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers, which corresponds to rotations by multiples of 90 degrees <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

If *n* has a prime factor that is 3 (mod 4) raised to an odd power, it's impossible to balance the columns, resulting in zero lattice points for that radius <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. If it's an even power, the factor can be split evenly but doesn't add new options <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

## The Chi Function

To systematize the counting of lattice points, a multiplicative function called chi (χ) is introduced <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>:
*   χ(*p*) = 1 if *p* ≡ 1 (mod 4) <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
*   χ(*p*) = -1 if *p* ≡ 3 (mod 4) <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
*   χ(*n*) = 0 if *n* is even <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>

This function generates a cyclic pattern: 1, 0, -1, 0, 1, 0, -1, 0... <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. As a multiplicative function, χ(*a*b) = χ(*a*)χ(*b*) <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

The number of options for a prime power *p*^k^ in the factorization process can be expressed as the sum: χ(1) + χ(*p*) + χ(*p*²) + ... + χ(*p*^k^) <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
*   For *p* ≡ 1 (mod 4), this sum is *k* + 1, matching the number of options <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   For *p* ≡ 3 (mod 4):
    *   If *k* is even, the sum is 1, indicating one choice <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
    *   If *k* is odd, the sum is 0, indicating no choices <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   For *p* = 2, the sum is always 1 (since χ(even) = 0), showing no change in options <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

For any number *n*, the total number of lattice points on the circle of radius √*n* (excluding the origin) is 4 times the sum of χ(*d*) for all divisors *d* of *n* <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. This is because the multiplicative property of χ allows the product of sums for prime powers to expand into a sum over all divisors of *n* <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.

## Deriving a Formula for Pi

Summing the number of lattice points for all *n* from 1 to r² gives the total count of lattice points within the circle <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>. By rearranging this sum, rather than summing by *n*, one can sum by divisor *d* <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.
*   The term χ(1) appears *r*² times (for every *n* divisible by 1) <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
*   The term χ(2) appears approximately *r*²/2 times <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   The term χ(3) appears approximately *r*²/3 times <a class="yt-timestamp" data-t="00:26:59">[00:26:59]</a>.
And so on, for every integer *k*, the term χ(*k*) appears approximately *r*²/*k* times <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.

Thus, the total number of lattice points (excluding the origin) is approximately:
4 * r² * (χ(1)/1 + χ(2)/2 + χ(3)/3 + χ(4)/4 + ...) <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.

Since χ(*n*) is 0 for even *n*, and oscillates between 1 and -1 for odd *n*, this sum simplifies to:
4 * r² * (1/1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.

Equating this to the area approximation (πr²):
πr² ≈ 4 * r² * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.

Dividing by r² gives the Leibniz formula for pi:
π = 4 * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

This derivation demonstrates how the simple [[complex_numbers_introduction | complex number]] system of [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers, and the regular pattern of prime factorization within them, leads to a fundamental formula for pi <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.

## Connections to Number Theory

This derivation touches upon two main branches of number theory <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>:
*   **Algebraic Number Theory**: Deals with new number systems like the [[gaussian_distribution_and_the_role_of_pi | Gaussian]] integers <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>.
*   **Analytic Number Theory**: Involves multiplicative functions like the chi function, often seen in the context of L-functions (cousins of the Riemann zeta function) <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>.
The path followed to derive the pi formula showcases an intersection of these two fields <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.