---
title: Techniques for Olympiad level counting problems
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

Olympiad-level counting problems, often categorized as [[Problemsolving strategies in mathematics | discrete mathematics]] questions involving whole numbers and their sums, can be exceptionally challenging <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Solving these problems, while sometimes appearing as "toy problems," develops skills applicable to other complex mathematical challenges <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

## Example Problem

A representative problem, found in a book used for training the USA team for the [[International Math Olympiad overview | International Math Olympiad]], asks: "Find the number of subsets of the set 1 up to 2000, the sum of whose elements is divisible by 5." <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

For instance, the set {3, 1, 4} sums to 8 (not counted), while {2, 3, 5} sums to 10 (counted) <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. The empty set, whose sum is 0, is also counted as a multiple of 5 <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

A brute-force approach to this problem would involve iterating through all possible subsets, calculating their sums, and counting those divisible by 5 <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. The total number of subsets for a set of 2000 elements is 2^2000, as each element can either be included or not included in a subset <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. This number is "monstrously huge," rendering brute force impractical <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. While a heuristic guess might be one-fifth of all subsets due to an assumed even distribution of sums modulo 5, the true challenge is to find a precise answer <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

## Problem Solving Strategies

When tackling such a problem, a general [[Problemsolving strategies in mathematical puzzles | problem-solving strategy]] is to start with a simpler example <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. For the subset sum problem, consider the set {1, 2, 3, 4, 5}. This set has 2^5 = 32 subsets <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>. Listing all subsets and their sums reveals that 8 of them have a sum divisible by 5 <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. This is slightly more than the heuristic guess of 6.4 (1/5 of 32) <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

While approaches like examining subset structure, sum distribution modulo 5, or [[Problemsolving strategies in mathematics | proof by induction]] might seem natural <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>, a powerful, albeit less intuitive, technique for these problems is the use of generating functions <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

## Generating Functions

A **generating function** is a polynomial (or power series) where coefficients encode information about a sequence <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. For the subset sum problem, we construct a polynomial where the act of algebraic expansion mirrors the act of constructing subsets, and the exponent of 'x' in each term equals the sum of the corresponding subset <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.

For the set {1, 2, 3, 4, 5}, the generating function is:
`f(x) = (1 + x^1)(1 + x^2)(1 + x^3)(1 + x^4)(1 + x^5)` <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.

*   Choosing '1' from each parenthesis corresponds to the empty set (sum 0) <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   Choosing `x^1` and '1's from others corresponds to the set {1} (sum 1) <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   Choosing `x^1` and `x^2` and '1's from others corresponds to the set {1, 2} (sum 3), resulting in an `x^3` term <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

When expanded, the coefficient of `x^k` (denoted as `c_k`) represents the number of subsets whose elements sum to `k` <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

For the general problem with the set {1, ..., 2000}, the generating function is:
`f(x) = (1 + x^1)(1 + x^2)...(1 + x^2000)` <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
In its expanded form, `f(x) = Σ c_n x^n`, where `c_n` is the number of subsets summing to `n` <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>.

### Evaluating Generating Functions

Evaluating the function at specific values can reveal properties of its coefficients:

*   `f(0) = 1`: This means `c_0 = 1`, corresponding to the single empty set <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.
*   `f(1) = 2^2000`: This is the sum of all coefficients (`Σ c_n`), representing the total number of subsets <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>.
*   `f(-1) = 0`: For the given function, plugging in `x = -1` results in `(1 - 1)(1 + (-1)^2)... = 0` <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. When applied to the expanded form, this means `c_0 - c_1 + c_2 - c_3 + ... = 0` <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>. This implies an equal balance between the sum of even-indexed coefficients and odd-indexed coefficients, meaning half of all subsets have an even sum, and half have an odd sum <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.

A useful manipulation derived from `f(1)` and `f(-1)` is:
`(f(1) + f(-1)) / 2 = Σ c_n` for even `n` <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.
This filters out odd coefficients, giving the total number of subsets with an even sum <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

### Incorporating Complex Numbers

To find the sum of coefficients `c_n` where `n` is divisible by 5, we generalize the approach using [[Creative approaches in mathematical proofs | complex numbers]] <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. This leverages the "unreasonable usefulness" of complex numbers in discrete math <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

The key is to use the **fifth roots of unity**: complex numbers that, when raised to successive powers, rotate with a period of 5 around the unit circle <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. These are the solutions to `z^5 = 1` <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>:
*   `zeta_0 = 1` (or `e^(i * 0)`)
*   `zeta_1 = e^(i * 2π/5)`
*   `zeta_2 = e^(i * 4π/5)`
*   `zeta_3 = e^(i * 6π/5)`
*   `zeta_4 = e^(i * 8π/5)`

When we sum `f(zeta_0) + f(zeta_1) + f(zeta_2) + f(zeta_3) + f(zeta_4)`, a crucial property emerges:
*   If `k` is *not* a multiple of 5, `zeta_0^k + zeta_1^k + zeta_2^k + zeta_3^k + zeta_4^k = 0` (due to cancellation/balance around zero) <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>.
*   If `k` *is* a multiple of 5, `zeta_0^k + zeta_1^k + zeta_2^k + zeta_3^k + zeta_4^k = 5` (due to constructive interference, as all terms become 1) <a class="yt-timestamp" data-t="22:06:00">[22:06:00]</a>.

This means that if we sum `f(z)` for all five roots of unity:
`f(zeta_0) + f(zeta_1) + f(zeta_2) + f(zeta_3) + f(zeta_4) = 5 * (sum of c_n where n is a multiple of 5)` <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>.
Therefore, the desired sum of coefficients (number of subsets with sum divisible by 5) is:
`1/5 * [f(zeta_0) + f(zeta_1) + f(zeta_2) + f(zeta_3) + f(zeta_4)]` <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>.

### Calculating the Values

1.  **`f(zeta_0) = f(1)`**: As determined previously, `f(1) = 2^2000` <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.
2.  **`f(zeta_k)` for `k = 1, 2, 3, 4`**:
    `f(zeta_k) = (1 + zeta_k^1)(1 + zeta_k^2)...(1 + zeta_k^2000)` <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.
    Since powers of `zeta_k` repeat every 5 terms (`zeta_k^(j+5) = zeta_k^j`), this product can be simplified. The entire expression up to 2000 terms is essentially a copy of the product of the first five terms (from 1 to 5) repeated 400 times (2000/5 = 400) <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
    So, `f(zeta_k) = [(1 + zeta_k^1)(1 + zeta_k^2)(1 + zeta_k^3)(1 + zeta_k^4)(1 + zeta_k^5)]^400` <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.

    To evaluate the product `(1 + zeta^1)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)`:
    Recall that `z^5 - 1 = (z - zeta_0)(z - zeta_1)(z - zeta_2)(z - zeta_3)(z - zeta_4)` <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.
    Also, `z^5 - 1 = (z - 1)(z^4 + z^3 + z^2 + z + 1)` <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.
    Thus, `(z - zeta_1)(z - zeta_2)(z - zeta_3)(z - zeta_4) = z^4 + z^3 + z^2 + z + 1` <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.

    To get `(1 + zeta^1)...(1 + zeta^5)`, we can substitute `z = -1` into the factored form.
    `(-1)^5 - 1 = (-1 - zeta_0)(-1 - zeta_1)(-1 - zeta_2)(-1 - zeta_3)(-1 - zeta_4)` <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.
    `-2 = (-1)(1 + zeta_1)(1 + zeta_2)(1 + zeta_3)(1 + zeta_4)` <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.
    Since `zeta_0 = 1`, `(1 + zeta_0) = 2`.
    So, `(-1)^5 - 1 = -2` on the left.
    On the right, `(-1 - 1)(-1 - zeta_1)(-1 - zeta_2)(-1 - zeta_3)(-1 - zeta_4)`
    `= (-2) * (-1)^4 * (1 + zeta_1)(1 + zeta_2)(1 + zeta_3)(1 + zeta_4)`
    `= -2 * (1 + zeta_1)(1 + zeta_2)(1 + zeta_3)(1 + zeta_4)` <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.

    This means `(1 + zeta_1)(1 + zeta_2)(1 + zeta_3)(1 + zeta_4) = 1` <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.
    Multiplying by `(1 + zeta_5) = (1 + 1) = 2`, the full product of the five terms is `2 * 1 = 2` <a class="yt-timestamp" data-t="28:30:00">[28:30:00]</a>.

    Therefore, `f(zeta_k)` for `k = 1, 2, 3, 4` is `2^400` <a class="yt-timestamp" data-t="28:47:00">[28:47:00]</a>.

### Final Solution

The total number of subsets whose sum is divisible by 5 is:
`1/5 * [f(1) + f(zeta_1) + f(zeta_2) + f(zeta_3) + f(zeta_4)]` <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>
`= 1/5 * [2^2000 + 2^400 + 2^400 + 2^400 + 2^400]` <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>
`= 1/5 * (2^2000 + 4 * 2^400)` <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>

For the smaller example of {1, 2, 3, 4, 5}, the formula yields:
`1/5 * (2^5 + 4 * 2^1) = 1/5 * (32 + 8) = 1/5 * 40 = 8` <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>, which matches the explicit count <a class="yt-timestamp" data-t="30:08:00">[30:08:00]</a>.

## Broader Implications

This method of taking a discrete sequence and representing it as coefficients of a polynomial, then evaluating that polynomial on complex values, is a powerful and general technique in mathematics <a class="yt-timestamp" data-t="30:43:00">[30:43:00]</a>.

### Connection to Prime Numbers and Riemann Hypothesis

The technique used for this [[Combinatorial puzzles and strategy development | combinatorial puzzle]] is "similar in spirit" to how prime numbers are studied <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Questions about prime distribution involve studying functions whose inputs and outputs are complex numbers <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. The famous Riemann Hypothesis, for example, concerns a specially designed function (the Riemann zeta function) that, on the surface, seems unrelated to the discrete world of primes, but encodes all information about them <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. Certain questions about primes are easier to answer by analyzing this complex function than by directly analyzing the primes <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. The approach involves a discrete sequence carrying information about prime numbers, considering a function (a Dirichlet series) whose coefficients are terms in that sequence, and then deducing information about these coefficients by studying the function's behavior with complex-valued inputs <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>.

### The Power of Complex Numbers in Frequency Questions

The reason complex numbers are "unreasonably useful" in this context is their ability to reveal hidden information about coefficients by providing a richer space of inputs <a class="yt-timestamp" data-t="32:47:00">[32:47:00]</a>. Specifically, for "frequency questions" like finding sums divisible by 5, complex numbers on the unit circle (roots of unity) allow for "cycling behavior" through successive powers <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>. This concept of using roots of unity to detect frequency information is "extremely fruitful" <a class="yt-timestamp" data-t="33:17:00">[33:17:00]</a> and is core to concepts like Fourier transforms and Fourier series <a class="yt-timestamp" data-t="33:49:00">[33:49:00]</a>, as well as algorithms like Shor's algorithm for quantum factoring <a class="yt-timestamp" data-t="33:31:00">[33:31:00]</a>.

### Further Reading

For those interested in learning more about generating functions, the book "GeneratingFunctionology" by Herbert Wilf is highly recommended <a class="yt-timestamp" data-t="34:01:00">[34:01:00]</a>.