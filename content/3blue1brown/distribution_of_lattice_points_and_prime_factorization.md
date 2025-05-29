---
title: Distribution of lattice points and prime factorization
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

The intersection of [[prime_numbers_and_their_regularities | prime numbers]], complex numbers, and [[pi_and_its_formulas_involving_primes | pi]] is a frequent occurrence in modern mathematics, especially in areas related to the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. One instance where these concepts converge is in deriving a formula for [[pi_and_its_formulas_involving_primes | pi]] as an alternating infinite sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This derivation reveals a hidden circle and showcases a [[prime_numbers_and_their_regularities | regularity]] in the behavior of [[prime_numbers_and_their_regularities | prime numbers]] within the complex numbers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The process involves:
1.  Determining the number of [[finding_integer_solutions_with_lattice_points | lattice points]] within a large circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
2.  Expressing numbers as the sum of two squares <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
3.  Factoring integers within the complex plane <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
4.  Introducing a special function, chi, to simplify the pattern related to the [[distribution_of_prime_numbers_and_dirichlets_theorem | distribution of primes]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Lattice Points and Estimating Pi

A lattice point is defined as a point (a, b) on the plane where both 'a' and 'b' are integers <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For a circle centered at the origin with radius 'r', the number of lattice points inside is approximately equal to its area, πr² <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. For larger radii, this approximation becomes more accurate, with the percent error decreasing <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The goal is to find an alternative method to count these lattice points, which can lead to another way to express the area of a circle and, consequently, [[pi_and_its_formulas_involving_primes | pi]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Counting Lattice Points on Concentric Rings

The distance of a lattice point (a, b) from the origin is given by √(a² + b²) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Since 'a' and 'b' are integers, a² + b² will also be an integer. This means lattice points only appear on rings whose radii are the square roots of whole numbers <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

Examples of lattice points on rings:
*   Radius 0: 1 point (the origin) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   Radius 1 (√1): 4 points (e.g., (1,0), (0,1), (-1,0), (0,-1)) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Radius √2: 4 points (e.g., (1,1), (1,-1), (-1,1), (-1,-1)) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   Radius √3: 0 points <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Radius √4: 4 points (e.g., (2,0), (-2,0), (0,2), (0,-2)) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   Radius √5: 8 points <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Radius √11: 0 points <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   Radius √25: 12 points (e.g., (5,0), (4,3), (3,4), and their reflections) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

The pattern of how many lattice points sit on a given ring appears chaotic, suggesting a connection to deeper mathematical principles, specifically the [[distribution_of_prime_numbers_and_dirichlets_theorem | distribution of primes]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Counting these points is equivalent to finding how many pairs of integers (a, b) satisfy a² + b² = n for a given integer 'n' <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## Gaussian Integers and Factorization

To understand this pattern, it's fruitful to view the 2D plane as the set of complex numbers <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. A lattice point (a, b) can be represented as a complex number a + bi <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The sum of squares a² + b² is equivalent to multiplying the complex number a + bi by its complex conjugate a - bi <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This transforms the problem into a factoring problem within the complex numbers, hence the connection to [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

The collection of all complex numbers a + bi where 'a' and 'b' are integers are called **Gaussian integers** <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The question becomes: how many Gaussian integers, when multiplied by their complex conjugate, yield a specific integer 'n'? <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>

### Unique Factorization in Gaussian Integers

Similar to ordinary integers, Gaussian integers also have a form of unique factorization into **Gaussian primes** <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. However, this uniqueness comes with some allowances:
*   Factors can be multiplied by units (1, -1, i, -i) to produce different-looking factorizations <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The behavior of ordinary [[prime_numbers_and_their_regularities | prime numbers]] when factored in Gaussian integers is crucial:
*   **Primes of the form 4k + 1** (e.g., 5, 13, 17): These can always be factored into exactly two distinct Gaussian primes, which are complex conjugates of each other (e.g., 5 = (2+i)(2-i)) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This explains why rings with radii equal to the square root of such primes hit exactly 8 lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Primes of the form 4k + 3** (e.g., 3, 7, 11): These cannot be factored further within the Gaussian integers; they remain Gaussian primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Consequently, rings with radii equal to the square root of these primes do not hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The prime number 2**: It factors as 2 = (1+i)(1-i) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. These two Gaussian primes are related by a 90-degree rotation (i.e., (1+i) * i = (1-i)), which means multiplying one by 'i' gives the other <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. This special relationship means factors of 2 do not change the count of lattice points <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

## Recipe for Counting Lattice Points (r_n)

To count the number of Gaussian integers (a + bi) such that (a + bi)(a - bi) = n (i.e., a² + b² = n), follow these steps:
1.  **Factor 'n' into its Gaussian prime factors** <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. For example, if n = 25, then 25 = 5² = ((2+i)(2-i))² <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
2.  **Distribute the Gaussian prime factors into two columns**, ensuring that for every prime factor in one column, its conjugate is in the other column <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The product of the factors in the left column will be the Gaussian integer, and the product in the right column will be its conjugate.
    *   For a prime factor (like 5) that splits into two distinct Gaussian primes (2+i, 2-i), if 'p' appears 'k' times (e.g., 5³), there are k+1 ways to distribute these pairs between the columns (e.g., 0 (2+i) on left, 1 (2+i) on left, ..., k (2+i) on left) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
    *   For a prime factor (like 3) that is itself a Gaussian prime, it must appear an even number of times to allow balanced distribution (one 3 in each column) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. If it appears an odd number of times, no lattice points exist for that 'n' <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. If it appears an even number of times, there's only one way to distribute it equally <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
    *   Factors of 2 do not affect the count of options because (1+i) and (1-i) are related by a 90-degree rotation <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
3.  **Multiply the final product from the left column by the four units (1, i, -1, -i)** <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This accounts for all 4 possible orientations of the lattice point on the plane. This final step means the total count is always a multiple of 4 <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

For example, for n = 25 (5²), there are 3 ways to distribute the (2+i) factors, and multiplying by 4 gives 12 lattice points <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. For n = 125 (5³), there are 4 ways to distribute the (2+i) factors, leading to 4 * 4 = 16 lattice points <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. For n = 375 (3 * 5³), there are 0 lattice points because of the odd power of 3 <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

## The Chi Function (χ)

To simplify the counting process, a **multiplicative function** called **chi (χ)** is introduced <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. Chi is defined as:
*   χ(n) = 1 if n is 1 above a multiple of 4 (e.g., 1, 5, 9, 13...) <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   χ(n) = -1 if n is 3 above a multiple of 4 (e.g., 3, 7, 11, 15...) <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   χ(n) = 0 if n is even (e.g., 2, 4, 6, 8...) <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

This results in a cyclic pattern: 1, 0, -1, 0, 1, 0, -1, 0... <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
As a multiplicative function, χ(a * b) = χ(a) * χ(b) for any integers 'a' and 'b' <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

The number of lattice points for a given 'n' can be expressed as 4 times the sum of χ(d) for all divisors 'd' of 'n' <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. This is because:
*   For a prime power p^k where p is 4m+1: The number of options is (k+1), which equals Σ (χ(p^j)) for j=0 to k, as all χ(p^j) are 1 <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   For a prime power p^k where p is 4m+3: If 'k' is even, the sum Σ (χ(p^j)) for j=0 to k is 1 (1 - 1 + 1 - 1 + ... + 1). If 'k' is odd, the sum is 0 (1 - 1 + 1 - 1 + ... - 1) <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. This matches the counting recipe.
*   For a power of 2: The sum Σ (χ(2^j)) for j=0 to k is 1 (1 + 0 + 0 + ...) <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

## Deriving the Formula for Pi

The total number of lattice points inside a large circle of radius 'r' is approximately πr² <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.
This can also be found by summing the number of lattice points on each ring (radius √n) from n=1 to r² <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
So, the total count is approximately:
4 * Σ (Σ χ(d)) for n = 1 to r² (where the inner sum is over all divisors 'd' of 'n') <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.

By reorganizing this sum, instead of summing by 'n' then 'd', we can sum by 'd' then 'n':
*   For each divisor 'd', count how many numbers 'n' (between 1 and r²) have 'd' as a divisor. This count is approximately r²/d <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.
*   So, the total count of lattice points is approximately 4 * Σ ( (r²/d) * χ(d) ) for d = 1 to r² <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.

Factoring out r²:
Total lattice points ≈ 4 * r² * Σ (χ(d)/d) for d = 1 to infinity (as r -> infinity) <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.

Since χ(d) is 0 for even 'd' and alternates between 1 and -1 for odd 'd', the sum becomes:
Σ (χ(d)/d) = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.

Equating the two expressions for the total lattice points:
πr² ≈ 4 * r² * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>.

Dividing by r², we arrive at the **Leibniz formula for Pi**:
π = 4 * (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

This elegant formula's simplicity stems directly from the [[prime_numbers_and_their_regularities | regular pattern]] of how [[prime_numbers_and_their_regularities | prime numbers]] factor within the Gaussian integers <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>. This derivation provides a glimpse into the intersection of algebraic number theory (dealing with new number systems like Gaussian integers) and analytic number theory (involving multiplicative functions like chi and L-functions related to the Riemann zeta function) <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.