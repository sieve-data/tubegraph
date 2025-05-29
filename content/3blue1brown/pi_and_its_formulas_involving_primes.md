---
title: Pi and its formulas involving primes
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

This article explores a deep [[relationship_between_counting_and_pi | formula for pi]] that intricately connects [[prime_numbers_and_generating_functions | prime numbers]], [[relationship_between_natural_logs_and_prime_numbers | complex numbers]], and pi itself <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This connection often appears in modern mathematics, particularly with the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The derivation reveals a hidden circle <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> and demonstrates a surprising [[prime_numbers_and_their_regularities | regularity in the way that prime numbers behave]] when viewed within the complex numbers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Approaching Pi through Lattice Points

One method to derive a [[algorithm_for_computing_pi_using_physics | formula for pi]] is by asking how many [[distribution_of_lattice_points_and_prime_factorization | lattice points]] (points with integer coordinates) lie inside a large circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For a circle centered at the origin with radius `r`, the number of lattice points is approximately equal to the circle's area, `πr²` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. As the radius increases, this approximation becomes more accurate <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The goal is to find a second way to count these lattice points, leading to an alternative expression for the area of a circle and thus for pi <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

Instead of counting all points at once, one can count lattice points on individual "rings" or circles of specific radii <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A lattice point `(a,b)` has a distance from the origin of `√(a² + b²)`, where `a² + b²` is an integer <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Counting how many lattice points sit on a ring with radius `√n` means finding integer pairs `(a,b)` such that `a² + b² = n` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The pattern of how many points are on each ring appears chaotic <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, suggesting that interesting mathematics, rooted in the [[distribution of prime numbers and Dirichlets theorem | distribution of primes]], is involved <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For example, a ring with radius `√11` hits no lattice points because 11 cannot be expressed as the sum of two squares <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Gaussian Integers and Prime Factorization

To understand this pattern, the problem is reframed using [[relationship_between_natural_logs_and_prime_numbers | complex numbers]] <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. A lattice point `(a,b)` is thought of as a [[gaussian_integers | Gaussian integer]], `a + bi` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The sum of squares `a² + b²` is equivalent to multiplying `a + bi` by its complex conjugate, `a - bi` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This transforms the counting problem into a factoring problem within the Gaussian integers <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Factoring Ordinary Primes in Gaussian Integers
Factoring within Gaussian integers is "almost unique" <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Ordinary [[eulers_totient_function_and_relative_primality | prime numbers]] behave differently when factored into Gaussian primes:
*   **Primes `1 mod 4`**: Prime numbers that are one above a multiple of four (e.g., 5, 13, 17) can *always* be factored into exactly two distinct Gaussian primes (e.g., 5 = (2+i)(2-i)) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that a circle with a radius equal to the square root of such a prime will hit lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes `3 mod 4`**: Prime numbers that are three above a multiple of four (e.g., 3, 7, 11) *cannot* be factored further within the Gaussian integers; they are also Gaussian primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This means a circle with a radius equal to the square root of such a prime will not hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The prime 2**: The prime number 2 is special because it factors as `(1+i)(1-i)`. These two Gaussian primes are rotations of each other, meaning one can be obtained by multiplying the other by `i` <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

This pattern of how [[prime_numbers_and_their_regularities | prime numbers]] behave based on their remainder when divided by 4 is a crucial [[prime_numbers_and_their_regularities | regularity]] that will be exploited <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## The Chi Function and Lattice Point Count

A systematic way to count lattice points with a given magnitude `√n` involves a "recipe":
1.  **Factor `n`**: Factor `n` into its prime powers in the ordinary integers <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
2.  **Factor into Gaussian Primes**: Further factor primes that are `1 mod 4` into their conjugate Gaussian prime pairs <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Primes `3 mod 4` remain unsplittable.
3.  **Divvy up Factors**: Organize these Gaussian prime factors into two columns, ensuring conjugate pairs are kept together <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Each distinct product from the left column represents a unique Gaussian integer whose product with its conjugate equals `n` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
4.  **Account for Rotations**: Finally, multiply the result from the left column by `1`, `i`, `-1`, or `-i` to account for all possible rotations that preserve the magnitude <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This means there are always 4 final choices <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

*   For prime factors `p` that are `1 mod 4` (e.g., 5), if `p^k` is a factor of `n`, this contributes `k+1` options to the count <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.
*   For prime factors `p` that are `3 mod 4` (e.g., 3), if `p^k` is a factor of `n`:
    *   If `k` is even, this contributes 1 option <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
    *   If `k` is odd, this contributes 0 options (no lattice points) <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   Factors of 2 (or any power of 2) do not change the count of lattice points; they effectively contribute 1 option <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

To simplify this complex recipe, a multiplicative function, `χ` (chi), is introduced <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>:
*   `χ(n) = 1` if `n` is `1 mod 4` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
*   `χ(n) = -1` if `n` is `3 mod 4` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
*   `χ(n) = 0` if `n` is even <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>
This results in a cyclic pattern: 1, 0, -1, 0, repeating indefinitely <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

The number of lattice points on a circle with radius `√n` can be expressed as 4 times the sum of `χ(d)` for all divisors `d` of `n` <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. This holds for any natural number `n` <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.

## Deriving the Pi Formula

To find the total number of lattice points inside a large circle of radius `r`:
1.  Sum the number of lattice points on all rings `√n` for `n` from 1 to `r²` <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
2.  This sum can be reorganized by considering how many times each `χ(d)` contributes. For example, `χ(1)` is added for every `n`, `χ(2)` for every even `n`, `χ(3)` for every `n` divisible by 3, and so on <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
3.  Approximately, the total number of lattice points is `r² * (χ(1)/1 + χ(2)/2 + χ(3)/3 + ...)` <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
4.  Multiplying by the final factor of 4 from the recipe <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>, the total count is approximately `4 * r² * (χ(1)/1 + χ(2)/2 + χ(3)/3 + ...) ` <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.
5.  Since `χ(n)` is 0 for even numbers and alternates between 1 and -1 for odd numbers <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>, the sum becomes `1 - 1/3 + 1/5 - 1/7 + ...` <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.

Equating this to the area approximation `πr²` <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a> and dividing by `r²` yields:

> `π = 4 * (1 - 1/3 + 1/5 - 1/7 + ...)` <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>

This is the Leibniz formula for pi, an alternating infinite sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Its simplicity ultimately stems from the [[prime_numbers_and_their_regularities | regular pattern]] of how [[eulers_totient_function_and_relative_primality | prime numbers]] factor within the [[gaussian_integers | Gaussian integers]] <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. This derivation provides a glimpse into the intersection of algebraic number theory (dealing with new number systems like Gaussian integers) and analytic number theory (dealing with functions like `χ` and the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]]'s cousins, L-functions) <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.