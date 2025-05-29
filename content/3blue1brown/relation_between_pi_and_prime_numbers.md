---
title: Relation between pi and prime numbers
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

The connection between pi (π), [[prime_numbers_and_their_regularities | prime numbers]], and complex numbers is a fascinating braid in modern mathematics, especially in areas touching upon the [[riemann_hypothesis_and_prime_numbers | Riemann zeta function]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This exploration reveals an instance of this connection that doesn't demand an extensive technical background <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, culminating in an alternating infinite sum formula for pi <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This particular formula is famously said to have inspired Leibniz to pursue mathematics <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

A core principle in mathematics is that whenever pi appears, a [[geometric_intuition_of_pi | circle is hiding somewhere]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The objective is not merely to discover this sum, but to deeply understand the [[geometric_intuition_of_pi | circle hiding behind it]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. While this result can be proven with a few lines of calculus, such proofs often lack intuitive understanding of the underlying circle <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The path explored here reveals that the fundamental truth behind this sum and its hidden circle lies in a [[prime_numbers_and_their_regularities | certain regularity in the way that prime numbers behave when you put them inside the complex numbers]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## The Quest for Pi: Counting Lattice Points

The journey begins with a [[counting_puzzle_involving_pi | desire to find a formula for computing pi]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. One approach is to ask how many lattice points (points with integer coordinates) lie inside a large circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Lattice Points and Area
A lattice point (A, B) is where grid lines cross, with A and B being integers <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For a circle centered at the origin with radius `r`, the number of lattice points inside it is approximately equal to the circle's area, πr² <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. For a very large circle (e.g., radius 1 million), this approximation becomes much more accurate, meaning the percent error between the estimate and the actual count of lattice points decreases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The goal is to find a second method to count these lattice points, leading to an alternative expression for the circle's area and, consequently, pi <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### Counting Lattice Points on Rings
Every lattice point (A, B) is at a distance of √(A² + B²) from the origin <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Since A² + B² is an integer, lattice points only exist on rings whose radii are the square roots of whole numbers <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Radius 0: 1 point (the origin) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
*   Radius 1: 4 points <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
*   Radius √2: 4 points <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   Radius √3: 0 points <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
*   Radius √4 (or 2): 4 points <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   Radius √5: 8 points <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

Initially, the pattern for counting lattice points on a given ring appears chaotic <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, which hints at the involvement of interesting mathematics, particularly the [[distribution_of_prime_numbers | distribution of primes]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For example, a radius of √25 (or 5) hits 12 lattice points <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, while a radius of √11 hits none <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, because 11 cannot be expressed as the sum of two squares <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Gaussian Integers: The Key to Order

To bring order to this chaos, the problem shifts from the 2D plane to the complex plane <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. A lattice point (A, B) is reinterpreted as a complex number A + Bi <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The sum of squares A² + B² corresponds to multiplying the complex number A + Bi by its complex conjugate A - Bi <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This transforms the counting question into a factoring problem, which is where patterns among [[prime_numbers_and_their_regularities | prime numbers]] become crucial <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Gaussian Primes and Factorization
The set of all lattice points (A + Bi where A, B are integers) are called **Gaussian integers** <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The goal is to count how many Gaussian integers, when multiplied by their complex conjugate, yield a specific integer `n` (e.g., 25) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This requires understanding how numbers factor within Gaussian integers <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

Just as ordinary integers have unique prime factorizations (up to multiplication by -1) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, Gaussian integers also have a form of unique factorization. However, in Gaussian integers, factors can also be multiplied by `i` or `-i` to yield different looking factorizations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

A crucial and surprising fact about ordinary prime numbers and their factorization within Gaussian integers:
*   **Primes 1 (mod 4)**: Primes that are one above a multiple of 4 (e.g., 5, 13, 17) can always be factored into exactly two distinct Gaussian primes <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that rings with a radius equal to the square root of such a prime always hit exactly 8 lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes 3 (mod 4)**: Primes that are three above a multiple of 4 (e.g., 3, 7, 11) cannot be factored further within the Gaussian integers; they remain Gaussian primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This corresponds to rings with a radius equal to the square root of such a prime never hitting any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The prime 2**: The prime number 2 is special; it factors as (1 + i)(1 - i). These two Gaussian primes are 90 degrees apart (one is `i` times the other), which will require special handling <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

This pattern, based on a prime number's remainder when divided by 4, is the [[prime_numbers_and_their_regularities | regularity within prime numbers]] that is exploited <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

### A Recipe for Counting Gaussian Integers
To count how many Gaussian integers have a specific magnitude (i.e., how many lattice points are on a ring), a systematic recipe based on prime factorization is used:

1.  **Factor `n` into Gaussian primes**: For example, 25 = 5² = (2 + i)² (2 - i)² <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
2.  **Distribute factors into conjugate pairs**: Arrange the Gaussian prime factors into two columns, ensuring conjugate pairs are kept together <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The product of each column will be a complex conjugate pair.
3.  **Count combinations**: For each prime `p` that factors into a conjugate pair (like 5), if `p` appears `k` times in the factorization of `n` (e.g., 5³), there are `k+1` ways to distribute its Gaussian prime factors between the two columns <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
    *   For example, for 5³, there are 4 choices (0, 1, 2, or 3 copies of (2+i) in the left column) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   For primes `p` that remain Gaussian primes (like 3), if `p` appears an even number of times, there is only one choice (split them evenly between columns) <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. If `p` appears an odd number of times, there are zero choices, meaning no lattice points for that radius <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
4.  **Account for rotations**: Finally, multiply the resulting Gaussian integer by 1, `i`, -1, or `-i`. This accounts for the 4 possible rotations (multiples of 90 degrees) of the lattice points on the circle <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This gives a total of 4 final choices.
    *   Factors of 2 (or any power of 2) do not change the count of options because their Gaussian prime factors are rotations of each other, making their effect redundant with the final 4 choices <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

## The Chi Function: Regularizing the Count

To simplify this complex recipe, a function `chi` (χ) is introduced:
*   χ(n) = 1 if n ≡ 1 (mod 4) <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
*   χ(n) = -1 if n ≡ 3 (mod 4) <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
*   χ(n) = 0 if n is even <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>

This function generates a cyclic pattern: 1, 0, -1, 0, 1, 0, -1, 0... <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Importantly, `chi` is a **multiplicative function**: χ(a × b) = χ(a) × χ(b) <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

The number of options for a prime power `p^k` in the factorization of `n` can be expressed using `chi`:
*   For `p` ≡ 1 (mod 4), like 5³: χ(1) + χ(5) + χ(5²) + χ(5³) = 1 + 1 + 1 + 1 = 4 <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
*   For `p` ≡ 3 (mod 4), like 3⁴: χ(1) + χ(3) + χ(3²) + χ(3³) + χ(3⁴) = 1 - 1 + 1 - 1 + 1 = 1 <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. If `k` is odd, this sum is 0.
*   For `p` = 2 (or any power of 2): χ(1) + χ(2) + ... = 1 + 0 + 0 + ... = 1 <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

The total number of lattice points on a circle with radius √n (excluding the origin) is then 4 times the product of these sums for each prime factor `p` raised to its power `k` in the factorization of `n` <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. Due to the multiplicative property of `chi`, this product simplifies to 4 times the sum of χ(d) for all divisors `d` of `n` <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.

## The Culmination: A Formula for Pi

The total number of lattice points inside a large circle of radius `r` is approximately πr² <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This count can also be found by summing the number of lattice points on each ring (radius √n) for `n` from 1 to `r²` <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.

Thus, the total count is approximately:
Σ(n=1 to r²) [4 × Σ(d|n) χ(d)] <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>

By reorganizing the sum, counting how many times each χ(d) term appears (which is approximately `r²/d` for large `r`) <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>, and factoring out `r²`, we get:
Total lattice points ≈ 4 × r² × [ χ(1)/1 + χ(2)/2 + χ(3)/3 + χ(4)/4 + ... ] <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>

Since χ(n) is 0 for even numbers and alternates between 1 and -1 for odd numbers, the sum simplifies to:
Total lattice points ≈ 4 × r² × [ 1 - 1/3 + 1/5 - 1/7 + ... ] <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>

Equating this to the area approximation:
πr² ≈ 4r² [ 1 - 1/3 + 1/5 - 1/7 + ... ] <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>

Dividing by r², we arrive at the beautiful **Leibniz formula for pi**:
π = 4 [ 1 - 1/3 + 1/5 - 1/7 + ... ] <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>

This simple formula for pi, requiring surprisingly little information to describe, ultimately emerges from the [[prime_numbers_and_their_regularities | regular pattern]] of how [[prime_numbers_and_their_regularities | prime numbers]] factor within the Gaussian integers <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>. This journey highlights an intersection between **algebraic number theory** (dealing with new number systems like Gaussian integers) and **analytic number theory** (involving functions like `chi` and their relation to structures like the [[riemann_hypothesis_and_prime_numbers | Riemann zeta function]] and L-functions) <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.