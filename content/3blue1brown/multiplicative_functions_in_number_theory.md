---
title: Multiplicative functions in number theory
videoId: NaL_Cb42WyY
---

From: [[3blue1brown]] <br/> 

## Introduction to Multiplicative Functions

In number theory, a function is considered **multiplicative** if, for any two coprime integers *a* and *b*, the function of their product is equal to the product of their functions: f(*ab*) = f(*a*)f(*b*). This property simplifies the analysis of such functions, particularly when dealing with [[prime_numbers_distribution_and_computational_methods | prime numbers]].

## The Chi Function

A specific example of a multiplicative function is the chi function (χ), introduced in the context of counting lattice points within a circle <a class="yt-timestamp" data-t="02:12:46">[02:12:46]</a>. The chi function is defined based on the remainder of its input when divided by 4:
*   For inputs that are 1 above a multiple of 4 (e.g., 1, 5, 9, 13), the output of χ is 1 <a class="yt-timestamp" data-t="02:09:49">[02:09:49]</a>.
*   For inputs that are 3 above a multiple of 4 (e.g., 3, 7, 11, 15), the output of χ is -1 <a class="yt-timestamp" data-t="02:09:55">[02:09:55]</a>.
*   For all even numbers, the output of χ is 0 <a class="yt-timestamp" data-t="02:10:01">[02:10:01]</a>.

Evaluating χ on natural numbers produces a repeating cyclic pattern: 1, 0, -1, 0, and then repeats indefinitely <a class="yt-timestamp" data-t="02:11:15">[02:11:15]</a>.

### Multiplicative Property of Chi

The chi function possesses the multiplicative property. If you evaluate χ on two different numbers and multiply the results (e.g., χ(3) × χ(5)), the outcome is the same as evaluating χ on the product of those two numbers (χ(15)) <a class="yt-timestamp" data-t="02:21:27">[02:21:27]</a>. This holds true for any two natural numbers <a class="yt-timestamp" data-t="02:21:50">[02:21:50]</a>.

## Application in Counting Lattice Points and Formulas for Pi

The chi function proves useful in systematically counting lattice points on circles, which is related to finding a formula for Pi.

### Counting Lattice Points using Chi

The number of lattice points on a circle with radius √*n* (where *n* is an integer) can be expressed using the chi function. This involves considering the [[factorization_in_gaussian_integers | prime factorization]] of *n* within the [[factorization_in_gaussian_integers | Gaussian integers]] <a class="yt-timestamp" data-t="02:22:01">[02:22:01]</a>.

For each prime power *p*<sup>*k*</sup> in the factorization of *n*, the contribution to the count of lattice points is determined by the sum:
χ(1) + χ(*p*) + χ(*p*<sup>2</sup>) + ... + χ(*p*<sup>*k*</sup>) <a class="yt-timestamp" data-t="02:22:10">[02:22:10]</a>.

*   **Primes ≡ 1 (mod 4):** If a prime factor *p* is 1 above a multiple of 4 (e.g., 5), then χ(*p*<sup>*j*</sup>) = 1 for all powers *j*. Thus, the sum χ(1) + ... + χ(*p*<sup>*k*</sup>) equals *k* + 1 <a class="yt-timestamp" data-t="02:22:27">[02:22:27]</a>. For example, for 5<sup>3</sup>, the sum is 1+1+1+1 = 4.
*   **Primes ≡ 3 (mod 4):** If a prime factor *p* is 3 above a multiple of 4 (e.g., 3), then χ(*p*<sup>*j*</sup>) alternates between 1 and -1 (e.g., 1, -1, 1, -1, 1) <a class="yt-timestamp" data-t="02:22:58">[02:22:58]</a>.
    *   If *k* is an even power (e.g., 3<sup>4</sup>), the sum is 1 <a class="yt-timestamp" data-t="02:23:07">[02:23:07]</a>.
    *   If *k* is an odd power, the sum is 0 <a class="yt-timestamp" data-t="02:23:19">[02:23:19]</a>.
*   **Prime 2:** A factor of 2, or any power of 2, does not change the count of lattice points. The sum for powers of 2 is always 1 (e.g., 1 + 0 + 0 + ...) since χ is 0 on even numbers <a class="yt-timestamp" data-t="02:23:24">[02:23:24]</a>.

The total number of lattice points for a given *n* is obtained by multiplying the results for each prime power factor, and then multiplying by 4 (to account for rotations by 90, 180, 270 degrees in the complex plane) <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>.

Due to the multiplicative property of chi, this complicated recipe for counting lattice points can be simplified. The total number of lattice points on a circle with radius √*n* (denoted as *r*(*n*)) is equal to 4 times the sum of χ(*d*) for all divisors *d* of *n* <a class="yt-timestamp" data-t="02:49:58">[02:49:58]</a>.
<div class="callout">
**Formula for Lattice Points on a Circle (Approximate)**
*r*(*n*) ≈ 4 Σ<sub>*d*|*n*</sub> χ(*d*)
</div>
This formula links the seemingly chaotic pattern of lattice points to the ordered behavior of [[prime_numbers_distribution_and_computational_methods | prime numbers]] through the chi function <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>.

### Deriving a Formula for Pi

The total number of lattice points inside a large circle of radius *r* is approximately π*r*<sup>2</sup> <a class="yt-timestamp" data-t="02:56:29">[02:56:29]</a>. This total can also be found by summing *r*(*n*) for all *n* from 1 to *r*<sup>2</sup>.

By reorganizing the sum, it can be shown that the total number of lattice points is approximately 4 *r*<sup>2</sup> multiplied by the infinite series:
1 - 1/3 + 1/5 - 1/7 + ... <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

Equating the two expressions for the total number of lattice points and dividing by *r*<sup>2</sup> yields the Leibniz formula for Pi:
π = 4 (1 - 1/3 + 1/5 - 1/7 + ...) <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>.

This derivation highlights how the regular patterns in how [[prime_numbers_distribution_and_computational_methods | prime numbers]] factor inside the [[factorization_in_gaussian_integers | Gaussian integers]], captured by the multiplicative chi function, ultimately lead to this simple and fundamental formula for Pi <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>.

## Multiplicative Functions and Number Theory Branches

Multiplicative functions, like the chi function, are fundamental in **analytic number theory**. This field, along with **algebraic number theory** (which deals with new number systems like [[factorization_in_gaussian_integers | Gaussian integers]]), represents key branches of number theory <a class="yt-timestamp" data-t="02:58:36">[02:58:36]</a>. The connection demonstrated between the properties of [[factorization_in_gaussian_integers | Gaussian integers]] and the chi function provides a glimpse into the intersection of these two fields <a class="yt-timestamp" data-t="03:02:18">[03:02:18]</a>.