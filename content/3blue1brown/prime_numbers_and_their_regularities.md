---
title: Prime numbers and their regularities
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

This article explores the intricate relationship between [[prime_numbers_distribution_and_computational_methods | prime numbers]], complex numbers, and pi, particularly focusing on how regularities in prime numbers reveal a formula for pi <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This connection often appears in modern mathematics, especially when involving the Riemann zeta function <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Formula for Pi and Hidden Circles

A specific alternating infinite sum formula for pi, known as the Leibniz formula (1 - 1/3 + 1/5 - 1/7 + ...), is the culmination of this exploration <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. When pi appears in mathematics, there is almost always a circle subtly hidden <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The deeper understanding of this sum and its hidden circle lies in a certain regularity in how [[prime_numbers_distribution_and_computational_methods | prime numbers]] behave when placed within the complex numbers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Counting Lattice Points in a Circle

One approach to finding a formula for pi involves counting the number of lattice points (points with integer coordinates) inside a large circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
The number of lattice points within a circle of radius `r` is approximately equal to its area, which is πr² <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. As the radius increases, this approximation becomes more accurate <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Counting Lattice Points on Rings

To find an alternative way to express π, one can systematically count how many lattice points lie on rings with radii equal to the square roots of whole numbers <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. A lattice point (a, b) has a distance from the origin of √(a² + b²) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
Initially, the pattern for how many lattice points sit on a given ring appears chaotic and hard to find order in <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. However, this pattern is rooted in the [[distribution_of_prime_numbers | distribution of primes]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
For example, the ring with radius √25 hits 12 lattice points because 25 can be expressed as the sum of two squares in multiple ways (e.g., 5²+0² and 4²+3²) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Conversely, a ring with radius √11 hits no lattice points because 11 cannot be expressed as the sum of two squares <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Gaussian Integers and Factoring

A crucial step in understanding this pattern is to view the 2D plane as the set of all complex numbers, where lattice points (a,b) become Gaussian integers (a + bi) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The sum of the squares of coordinates (a² + b²) for a Gaussian integer (a + bi) is equivalent to multiplying the number by its complex conjugate (a - bi) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This transforms the counting problem into a factoring problem within the Gaussian integers <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Similar to ordinary integers having unique prime factorizations (up to multiplication by -1) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, Gaussian integers also have an almost unique factorization into Gaussian primes <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. The difference is that factors can also be multiplied by `i` or `-i` to yield different-looking factorizations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Regularities of Prime Numbers in Gaussian Integers

A surprising fact emerges regarding how ordinary [[prime_numbers_distribution_and_computational_methods | prime numbers]] factor inside the Gaussian integers <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:

*   **Primes that are 1 above a multiple of 4** (e.g., 5, 13, 17) can always be factored into exactly two distinct Gaussian primes (e.g., 5 = (2+i)(2-i)) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that rings with a radius equal to the square root of one of these primes always hit exactly 8 lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes that are 3 above a multiple of 4** (e.g., 3, 7, 11) cannot be factored further inside the Gaussian integers; they remain Gaussian primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This corresponds to the fact that a ring whose radius is the square root of one of these primes will never hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The prime number 2** is a special case. It factors as (1+i)(1-i), where the two Gaussian prime factors are a 90-degree rotation away from each other <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This means factors of 2 (or any power of 2) do not change the count of lattice points <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

This pattern, based on a prime number's remainder when divided by 4, is the fundamental regularity that is exploited <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## The Chi Function

To simplify the complex counting recipe, a simple function, denoted by the Greek letter chi (χ), is introduced <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>:
*   χ(n) = 1 if n is 1 above a multiple of 4 <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
*   χ(n) = -1 if n is 3 above a multiple of 4 <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
*   χ(n) = 0 if n is an even number <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>

This function generates a cyclic pattern: 1, 0, -1, 0, and repeats <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Importantly, chi is a [[multiplicative_functions_in_number_theory | multiplicative function]], meaning that χ(a * b) = χ(a) * χ(b) for any two natural numbers a and b <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

Using the chi function, the number of lattice points on a circle with radius √n (or equivalently, Gaussian integers (a+bi) such that (a+bi)(a-bi)=n) can be expressed as 4 times the sum of χ(d) for all divisors 'd' of 'n' <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. This formula treats all prime factors equally and simplifies the counting process <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

## Connecting to Pi

By summing the number of lattice points for all radii up to `r`, an approximation for the total number of lattice points inside a large circle with radius `r` is found <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This total sum can be rearranged by summing the values of χ(d) for each divisor `d` that appears <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.

The total number of lattice points is approximately:
4 * r² * (χ(1)/1 + χ(2)/2 + χ(3)/3 + χ(4)/4 + ...) <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>

Since χ(n) is 0 for even numbers and alternates between 1 and -1 for odd numbers, this sum simplifies to:
4 * r² * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>

Equating this to the area formula πr² <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>, and dividing by r², yields the elegant formula for pi:

π = 4 * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>

This derivation highlights how the simplicity of this formula for pi, which might seem to require knowledge of the [[distribution_of_prime_numbers | distribution of primes]], ultimately stems from the regular pattern in how [[prime_numbers_distribution_and_computational_methods | prime numbers]] factor within the Gaussian integers <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>. This intersection is a glimpse into the fields of algebraic number theory (dealing with new number systems like Gaussian integers) and analytic number theory (dealing with multiplicative functions and L-functions) <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.