---
title: Prime numbers and their regularities
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

Prime numbers, complex numbers, and [[pi_and_its_formulas_involving_primes | pi]] frequently appear together in modern mathematics, especially in areas related to the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A key to understanding deep formulas for [[pi_and_its_formulas_involving_primes | pi]] is often a hidden circle <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, and the fundamental truth behind such formulas stems from "a certain regularity in the way that prime numbers behave when you put them inside the complex numbers" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Counting Lattice Points and Prime Factorization

A method to discover formulas for [[pi_and_its_formulas_involving_primes | pi]] involves counting [[distribution_of_lattice_points_and_prime_factorization | lattice points]] (points `(A, B)` where `A` and `B` are integers) within a large circle centered at the origin <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The number of these points is approximately equal to the circle's area, $\pi r^2$ <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

The distance of a [[distribution_of_lattice_points_and_prime_factorization | lattice point]] `(A, B)` from the origin is $\sqrt{A^2 + B^2}$ <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Since `A` and `B` are integers, `A^2 + B^2` is also an integer <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Thus, we only consider rings with radii that are the square roots of whole numbers <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Systematically counting how many [[distribution_of_lattice_points_and_prime_factorization | lattice points]] fall on a given ring (a given distance from the origin) initially reveals a "really chaotic" pattern <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. However, this chaotic appearance is a sign of interesting mathematics, as the pattern is "rooted in the [[distribution_of_prime_numbers_and_Dirichlets_theorem | distribution of primes]]" <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This counting problem translates to finding how many pairs of integers `(A, B)` satisfy `A^2 + B^2 = n` for a given `n` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### Gaussian Integers and Prime Factorization

The problem of summing two squares can be reframed by viewing the 2D plane as the set of complex numbers <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. A [[distribution_of_lattice_points_and_prime_factorization | lattice point]] `(A, B)` can be considered as a complex number `A + Bi` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The sum of squares `A^2 + B^2` is equivalent to multiplying the complex number `A + Bi` by its complex conjugate `A - Bi` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This transforms the counting problem into a factoring problem, which directly involves patterns among prime numbers <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

The collection of `A + Bi` where `A` and `B` are integers are known as **Gaussian integers** <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Just as ordinary integers have unique prime factorizations (up to units like -1) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, Gaussian integers also have almost unique factorizations, where factors can be multiplied by `i`, `-i`, `1`, or `-1` <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

#### Prime Numbers and Their Behavior in Gaussian Integers

A crucial and surprising fact reveals the regularity in how prime numbers behave within the Gaussian integers:
*   **Primes `p = 4k + 1`:** Prime numbers that are 1 above a multiple of 4 (e.g., 5, 13, 17) can *always* be factored into exactly two distinct Gaussian primes <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This corresponds to the fact that rings with radius $\sqrt{p}$ for such primes always intersect [[distribution_of_lattice_points_and_prime_factorization | lattice points]] (specifically, 8 [[distribution_of_lattice_points_and_prime_factorization | lattice points]]) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes `p = 4k + 3`:** Prime numbers that are 3 above a multiple of 4 (e.g., 3, 7, 11) *cannot* be factored further within the Gaussian integers <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. They are Gaussian primes themselves <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Consequently, a ring with radius $\sqrt{p}$ for such primes will never hit any [[distribution_of_lattice_points_and_prime_factorization | lattice points]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The Prime 2:** The prime number 2 is special; it factors as `(1 + i) * (1 - i)` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. These two Gaussian primes are related by a 90-degree rotation (multiplying by `i`) <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Factors of 2 (or any power of 2) do not change the count of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] on a circle <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

This pattern, based on a prime number's remainder when divided by 4, is the regularity exploited to simplify the counting of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

### The Character Function Chi ($\chi$)

To systematize the counting of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] based on prime factorization, a simple function called **chi** ($\chi$) is introduced <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>:
*   $\chi(n) = 1$ if `n` is 1 above a multiple of 4 (`n = 4k + 1`) <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   $\chi(n) = -1$ if `n` is 3 above a multiple of 4 (`n = 4k + 3`) <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   $\chi(n) = 0$ for all even numbers <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

This function exhibits a cyclic pattern: `1, 0, -1, 0, 1, 0, -1, 0, ...` <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Crucially, $\chi$ is a **multiplicative function**, meaning $\chi(a \cdot b) = \chi(a) \cdot \chi(b)$ for any two numbers `a` and `b` <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

The number of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] on a circle with radius $\sqrt{n}$ can be expressed using $\chi$ based on the prime factorization of `n` <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. For each prime power $p^k$ in the factorization of `n`, a sum $\sum_{j=0}^{k} \chi(p^j)$ is computed <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
*   For primes $p = 4k + 1$, the sum is $1 + 1 + ... + 1 = k+1$, indicating $k+1$ options <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   For primes $p = 4k + 3$, the sum oscillates $1 - 1 + 1 - 1 + ...$. If `k` is even, the sum is 1; if `k` is odd, the sum is 0 <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. This correctly reflects the available choices for factoring <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
*   For factors of 2, the sum is $1 + 0 + 0 + ... = 1$, showing they don't affect the count <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

Ultimately, the total number of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] at distance $\sqrt{n}$ from the origin is 4 times the sum of $\chi(d)$ for all divisors `d` of `n` <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>. This connection between divisor sums and the $\chi$ function highlights the "wholly unexpected" organization that arises from the chaotic pattern <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.

## Connecting to Pi

The total number of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] inside a large circle of radius `r` is approximately $\pi r^2$ <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This same count can be achieved by summing the number of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] on each ring from $\sqrt{1}$ to $\sqrt{r^2}$ <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.

By reorganizing the sum of $\chi(d)$ over all divisors `d` of `n`, it can be shown that the total count of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] for a circle of radius `r` is approximately $4 \cdot r^2 \cdot \left( \sum_{k=1}^{\infty} \frac{\chi(k)}{k} \right)$ <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>. Since $\chi(k)$ is 0 for even numbers and alternates between 1 and -1 for odd numbers, this sum simplifies to:

$1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$ <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>

Equating the two expressions for the total number of [[distribution_of_lattice_points_and_prime_factorization | lattice points]] (and dividing by $r^2$), an infinite sum that converges to [[pi_and_its_formulas_involving_primes | pi]] is derived <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>:

$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$ <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>

This elegant formula, known as the Leibniz formula for [[pi_and_its_formulas_involving_primes | pi]], is simple because its description requires relatively low information. Its simplicity ultimately stems from the "regular pattern and how prime numbers factor inside the Gaussian integers" <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>. This demonstration illustrates an intersection of algebraic number theory (dealing with new number systems like Gaussian integers) and analytic number theory (dealing with functions like $\chi$ and the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]]) <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.