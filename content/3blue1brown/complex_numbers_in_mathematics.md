---
title: Complex numbers in mathematics
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

[[Complex numbers in discrete math | Complex numbers]] are a key component in understanding various mathematical concepts, including the distribution of prime numbers and formulas for pi <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. They frequently appear in modern mathematics, especially in areas related to the Riemann zeta function <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## [[Introduction to complex numbers | Conceptualizing Complex Numbers]] and the Plane

When exploring two-dimensional problems in mathematics, it can be beneficial to consider the plane as the set of all [[complex_numbers_in_discrete_math | complex numbers]] <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. For instance, a lattice point with integer coordinates `(a, b)` can be conceptualized as a single [[complex_numbers_in_discrete_math | complex number]], `a + bi` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, where 'i' is the imaginary unit.

## [[Geometric interpretation of complex numbers | Complex Conjugate]] and Magnitude

The sum of the squares of a [[complex_numbers_in_discrete_math | complex number]]'s coordinates (e.g., `3^2 + 4^2`) can be found by multiplying the number by its [[geometric_interpretation_of_complex_numbers | complex conjugate]] <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The [[geometric_interpretation_of_complex_numbers | complex conjugate]] of `a + bi` is `a - bi`, obtained by reflecting the number over the real axis (replacing `i` with `-i`) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This product results in `a^2 + b^2`, which is the square of the magnitude (distance from the origin) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### [[Complex numbers multiplication and rotation | Geometric Interpretation of Complex Multiplication]]
Multiplying a [[complex_numbers_in_discrete_math | complex number]] (e.g., `3 + 4i` with a magnitude of 5 and a certain angle) by its [[geometric_interpretation_of_complex_numbers | complex conjugate]] (`3 - 4i`) involves rotating the number by the same angle in the opposite direction, aligning it with the positive real axis. This is then followed by a stretch by a factor equal to the original number's magnitude, resulting in a product equal to the square of the magnitude <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. For `3 + 4i`, this product is 25, the square of its magnitude (5) <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## [[Complex numbers in discrete math | Gaussian Integers]]

The collection of all lattice points `a + bi`, where `a` and `b` are integers, are known as [[Complex numbers in discrete math | Gaussian integers]] <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. When counting lattice points at a certain distance from the origin (e.g., square root of 25), the problem can be rephrased as determining how many [[Complex numbers in discrete math | Gaussian integers]] yield a specific value (e.g., 25) when multiplied by their [[geometric_interpretation_of_complex_numbers | complex conjugate]] <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## [[Complex numbers in discrete math | Factoring in Gaussian Integers]]

Similar to ordinary integers, numbers can be factored into a unique collection of prime numbers within the [[Complex numbers in discrete math | Gaussian integers]] <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This factorization is almost unique, with exceptions for multiplication by `1`, `-1`, `i`, or `-i` <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. A [[complex_numbers_in_discrete_math | Gaussian prime]] is a [[Complex numbers in discrete math | Gaussian integer]] that cannot be factored into smaller [[Complex numbers in discrete math | Gaussian integers]] <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

The behavior of ordinary prime numbers when factored within the [[Complex numbers in discrete math | Gaussian integers]] is crucial:
*   **Primes 1 (mod 4):** Prime numbers that are 1 above a multiple of 4 (e.g., 5, 13, 17) can always be factored into exactly two distinct [[Complex numbers in discrete math | Gaussian primes]] <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that rings with a radius equal to the square root of such a prime always hit lattice points, specifically 8 of them <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes 3 (mod 4):** Prime numbers that are 3 above a multiple of 4 (e.g., 3, 7, 11) cannot be factored further within the [[Complex numbers in discrete math | Gaussian integers]]; they remain [[Complex numbers in discrete math | Gaussian primes]] <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Consequently, a circle with a radius equal to the square root of one of these primes will not hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The Prime 2:** The prime number 2 factors as `1 + i` times `1 - i`. These two [[Complex numbers in discrete math | Gaussian primes]] are a 90-degree rotation from each other, meaning one can be obtained by multiplying the other by `i` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Factors of 2 do not change the count of lattice points on a circle <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

This pattern in how prime numbers behave within the [[Complex numbers in discrete math | Gaussian integers]] is fundamental to understanding the distribution of lattice points and ultimately leads to a formula for pi <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## [[Applications of complex numbers in engineering and mathematics | Applications in Counting Lattice Points]]

The ability to factor numbers within the [[Complex numbers in discrete math | Gaussian integers]] provides a systematic way to count how many lattice points lie on a circle with a given radius <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This process involves:
1.  Factoring the number `n` (where `r^2 = n`) into its prime factors <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
2.  Organizing the [[Complex numbers in discrete math | Gaussian prime]] factors into conjugate pairs <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
3.  Considering the number of ways these factors can be distributed to form a [[complex_numbers_in_discrete_math | Gaussian integer]] and its [[geometric_interpretation_of_complex_numbers | complex conjugate]] <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
4.  Multiplying the result by 4 to account for rotations by `1`, `i`, `-1`, or `-i` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

This method, combined with the properties of a multiplicative function `chi` (which classifies numbers based on their remainder when divided by 4), reveals a deep connection between the distribution of prime numbers in the [[complex_numbers_in_discrete_math | complex plane]] and the number of lattice points inside a circle <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. This connection leads to a specific infinite sum formula for pi <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

## Intersection of Number Theory Branches

The exploration of [[Complex numbers in discrete math | Gaussian integers]] falls under **algebraic number theory**, which deals with new number systems <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. The use of multiplicative functions like `chi` relates to **analytic number theory**, involving concepts like L-functions <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>. The method described in this video provides a glimpse into the intersection of these two complex and actively researched fields <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.