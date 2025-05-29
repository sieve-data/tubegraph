---
title: Factorization in Gaussian integers
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

Factorization in [[complex_numbers_in_mathematics | complex numbers]] provides a key insight into patterns among prime numbers and their connection to pi <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept is particularly relevant in modern mathematics that involves the Riemann zeta function <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Gaussian Integers Defined

A lattice point `(a,b)` on the plane, where `a` and `b` are both integers, can be thought of as a single [[complex_numbers_in_discrete_math | complex number]], `a + bi` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The collection of all such points is called the Gaussian integers, named after Martin Sheen <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Distance and Complex Conjugates
The distance of a lattice point `(a,b)` from the origin is given by the square root of `a² + b²` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. If this point is represented as a [[complex_numbers_in_mathematics | complex number]] `a + bi`, the sum of the squares of its coordinates (`a² + b²`) can be obtained by multiplying the number by its complex conjugate, `a - bi` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The complex conjugate is formed by reflecting the number over the real axis, replacing `i` with `-i` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This multiplication turns the problem of finding distances into a factoring problem <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Geometrically, multiplying a [[complex_numbers_in_mathematics | complex number]] by its conjugate results in a number on the positive real axis, equal to the square of the original number's magnitude <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Factorization within Gaussian Integers

Similar to ordinary integers, where every number can be factored into a unique collection of prime numbers (up to factors of -1) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, factorization works similarly in Gaussian integers <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Gaussian Primes
A Gaussian integer that cannot be factored into anything smaller is called a Gaussian prime <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Factorization within Gaussian integers is almost unique, with the exception that factors can be multiplied by 1, i, -1, or -i <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Behavior of Ordinary Prime Numbers
The way ordinary prime numbers factor inside the Gaussian integers dictates how any natural number factors <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. This exhibits a crucial and surprising pattern based on their remainder when divided by 4 <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:

*   **Primes (1 mod 4)**: Prime numbers that are 1 above a multiple of 4 (e.g., 5, 13, 17) can always be factored into exactly two distinct Gaussian primes <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. For example, 5 factors as `(2 + i) * (2 - i)` <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This correlates with the fact that circles with a radius equal to the square root of these prime numbers always intersect lattice points <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a> (specifically, 8 lattice points) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Primes (3 mod 4)**: Prime numbers that are 3 above a multiple of 4 (e.g., 3, 7, 11) cannot be factored further inside the Gaussian integers <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>; they are Gaussian primes <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This corresponds to the fact that a circle with a radius equal to the square root of one of these primes will not hit any lattice points <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **The Prime Number 2**: The prime number 2 is a special case <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. It factors as `(1 + i) * (1 - i)` <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. These two Gaussian primes are a 90-degree rotation away from each other, meaning one can be obtained by multiplying the other by `i` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Counting Lattice Points Using Gaussian Integer Factorization

The understanding of factorization in Gaussian integers provides a method for counting how many lattice points lie on a circle with radius square root of `n` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This is equivalent to finding how many Gaussian integers, when multiplied by their complex conjugate, yield `n` <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

The recipe for finding all Gaussian integers that satisfy `z * z̄ = n` involves:
1.  **Factor `n` into its Gaussian prime factors** <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. For example, 25 factors as `(2+i)² * (2-i)²` <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
2.  **Organize these factors into two columns of conjugate pairs** <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Multiply the factors in each column; this will result in a complex conjugate pair <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
3.  **Consider choices for distributing factors**:
    *   For primes that split (like 5), the number of choices for distributing their Gaussian prime factors into the columns corresponds to one more than their exponent in `n` <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>, e.g., for 5², there are 3 choices for distributing `(2+i)` and `(2-i)` factors <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
    *   For primes that do not split (like 3), if they appear with an even power, there is one choice (e.g., one 3 in each column) <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. If they appear with an odd power, there are zero choices, meaning no lattice points for that `n` <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
4.  **Final Multipliers**: After obtaining a product from one column, multiply it by 1, i, -1, or -i <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This accounts for all possible orientations on the circle and captures all 12 distinct Gaussian integers for `n=25` <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### Examples:
*   For `n = 25` (5²), there are 3 choices for distributing the factors of 5 <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Multiplied by the 4 final choices (1, i, -1, -i), this results in 12 lattice points <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   For `n = 125` (5³), there are 4 choices for distributing the factors of 5 <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. Multiplied by 4 final choices, this gives 16 lattice points <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   For `n = 375` (3 * 5³), since 3 appears with an odd power, there are no lattice points <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.
*   For `n = 45` (3² * 5), this results in 8 lattice points, calculated as 4 (final choices) * 1 (for 3²) * 2 (for 5) <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.

### Effect of Factors of 2
Factors of 2 (or any power of 2) do not change the count of lattice points <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This is because the Gaussian prime factors of 2 (`1+i` and `1-i`) are related by multiplication by `i` <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>, making their distribution redundant with the final step of multiplying by 1, i, -1, or -i <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. For example, circles with radius square root of 5, 10, 20, and 40 all hit 8 lattice points <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

## Connection to the Chi Function
The regularity of prime numbers when factored in Gaussian integers can be exploited using a [[multiplicative_functions_in_number_theory | multiplicative function]] called chi (χ) <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a> <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
*   For inputs `n` where `n ≡ 1 (mod 4)`, `χ(n) = 1` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   For inputs `n` where `n ≡ 3 (mod 4)`, `χ(n) = -1` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   For all even numbers, `χ(n) = 0` <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
This function exhibits a cyclic pattern: 1, 0, -1, 0, and repeats <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

The number of lattice points on a circle with radius square root of `n` is `4 * Σ χ(d)`, where the sum is over all divisors `d` of `n` <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. This formula accounts for the choices in factor distribution based on the type of prime factors (1 mod 4, 3 mod 4, or 2) <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

## Broader Context
The exploration of factorization in Gaussian integers and its connection to counting lattice points on circles illustrates an intersection between two main branches of number theory:
*   **Algebraic number theory**, which deals with new number systems like Gaussian integers <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>.
*   **Analytic number theory**, which involves functions like the Riemann zeta function and [[multiplicative_functions_in_number_theory | multiplicative functions]] such as the chi function <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>.