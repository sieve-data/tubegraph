---
title: Chi function and its role in number theory
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

The chi function (χ) is a mathematical function that plays a crucial role in expressing the patterns observed when factoring integers within the [[complex_numbers_introduction | complex numbers]], specifically the Gaussian integers, and ultimately in deriving a formula for [[pi_and_its_formulas_involving_primes | pi]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It helps to organize seemingly chaotic patterns related to the [[distribution_of_prime_numbers_and_dirichlets_theorem | distribution of primes]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Definition and Cyclic Pattern

The chi function is defined based on the remainder of its input when divided by 4 <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>:
*   For inputs that are 1 above a multiple of 4 (e.g., 1, 5, 9...), the output of chi is 1 <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   For inputs that are 3 above a multiple of 4 (e.g., 3, 7, 11...), the output of chi is -1 <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   For all even numbers, the output of chi is 0 <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

This definition results in a distinct cyclic pattern when evaluated on natural numbers: 1, 0, -1, 0, and then repeating indefinitely <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

## Multiplicative Property

A key property of the chi function is that it is a *multiplicative function* <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This means that if you evaluate chi on two different numbers and multiply the results, it's the same as evaluating chi on the product of those two numbers <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. For example, chi(3) * chi(5) = chi(15), and chi(5) * chi(5) = chi(25) <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. This property holds for any two natural numbers <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Role in Counting Lattice Points

The chi function helps to systematically count the number of lattice points (points with integer coordinates) that lie on a circle with radius square root of *n* <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This problem is equivalent to determining how many Gaussian integers (numbers of the form *a + bi* where *a* and *b* are integers) have a magnitude of square root of *n* <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>, or whose product with their complex conjugate equals *n* <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

The number of such Gaussian integers (lattice points) for a given *n* can be determined by examining the prime factorization of *n* in the Gaussian integers <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>:
*   **Primes 1 (mod 4)**: Primes like 5, 13, 17 factor into two distinct Gaussian prime factors (e.g., 5 = (2+i)(2-i)) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. If such a prime *p* appears with an exponent *k* in *n* (i.e., *p<sup>k</sup>*), the number of options it contributes to the count is *k* + 1 <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. In terms of chi, this is equivalent to `chi(1) + chi(p) + chi(p^2) + ... + chi(p^k)` <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. Since `chi(p)` is 1 for these primes, this sum is `1 + 1 + ... + 1` (*k*+1 times), which equals *k*+1 <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   **Primes 3 (mod 4)**: Primes like 3, 7, 11 cannot be factored further within the Gaussian integers; they remain Gaussian primes <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. If such a prime *p* appears with an *even* exponent *k* (e.g., 3<sup>4</sup>), it contributes only 1 option to the count <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. If it appears with an *odd* exponent, it contributes 0 options, meaning no lattice points are found for that radius <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. In terms of chi, for `p^k`, this sum is `chi(1) + chi(p) + chi(p^2) + ... + chi(p^k)` <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Since `chi(p)` is -1 for these primes, the sum oscillates `1 - 1 + 1 - 1...` <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. If *k* is even, the sum is 1; if *k* is odd, the sum is 0 <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
*   **The prime 2**: The prime 2 factors as (1+i)(1-i) <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Factors of 2, or any power of 2, do not change the count of lattice points <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This is because multiplying by `i` rotates a Gaussian prime by 90 degrees, leading to redundancy with the final step of multiplying the product by 1, i, -1, or -i <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. In terms of chi, the sum `chi(1) + chi(2) + chi(4) + ...` becomes `1 + 0 + 0 + ...`, which is 1 <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

The total number of lattice points for a given *n* is 4 times the product of these sums for each prime power in the factorization of *n* <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Due to chi's multiplicative property, this product expands to 4 times the sum of `chi(d)` for every divisor *d* of *n* <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.

## Derivation of Pi Formula

To find a formula for [[pi_and_its_formulas_involving_primes | pi]], the problem shifts from counting lattice points on a single ring to counting the total number of lattice points inside a large circle of radius *r* <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This count is approximately `pi * r^2` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Alternatively, this count can be obtained by summing the number of lattice points for each `sqrt(n)` ring where `n` ranges from 1 to `r^2` <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>. By reorganizing the sum, instead of summing by *n*, one sums by divisor *d* <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>:

*   For each divisor *d*, there are approximately `r^2 / d` numbers between 1 and `r^2` that have *d* as a divisor <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   So, the total count of lattice points is approximately `4 * sum(chi(d) * (r^2 / d))` for all *d* <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.

Factoring out `r^2`, the total number of lattice points is approximately `4 * r^2 * (chi(1)/1 + chi(2)/2 + chi(3)/3 + chi(4)/4 + ...)` <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.

Since chi is 0 on every even number and oscillates between 1 and -1 for odd numbers, this sum simplifies to:
`4 * r^2 * (1/1 - 1/3 + 1/5 - 1/7 + ...)` <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.

Equating this to `pi * r^2` and dividing by `r^2` yields the Leibniz formula for pi <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>:

```
pi = 4 * (1 - 1/3 + 1/5 - 1/7 + ...)
```

This derivation highlights how the [[regularity of prime numbers]] in how they factor inside the Gaussian integers (captured by the chi function) leads to a simple, well-known formula for [[pi_and_its_formulas_involving_primes | pi]] <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.

## Broader Context

The chi function is an example of a *Dirichlet character*, a type of multiplicative function used in [[analytic_number_theory | analytic number theory]] <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>. These characters are central to the study of L-functions, which are generalizations of the [[connection_between_zeta_function_and_prime_numbers | Riemann zeta function]] <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>. The connection between [[algebraic_number_theory | algebraic number theory]] (dealing with new number systems like Gaussian integers) and [[analytic_number_theory | analytic number theory]] is an area of active research <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.