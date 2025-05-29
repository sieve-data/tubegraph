---
title: Complex numbers in discrete math
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

The field of discrete mathematics, often concerned with whole numbers and their sums, might seem an unlikely domain for the application of [[complex_numbers_in_mathematics | complex numbers]] [00:00:14]. However, [[complex_numbers_in_mathematics | complex numbers]] are "unreasonably useful for discrete math," a phenomenon exemplified by their role in understanding prime number distribution, a concept central to the famous Riemann hypothesis [00:00:25]. This article explores how [[complex_numbers_in_mathematics | complex numbers]] can provide elegant solutions to discrete counting problems, starting with a specific puzzle.

## The Subset Sum Puzzle

The core problem, taken from a book used to train the USA International Math Olympiad team, is:
> Find the number of subsets of the set 1 up to 2000, the sum of whose elements is divisible by 5. <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>

For instance, the set {2, 3, 5} is a subset whose elements sum to 10, which is divisible by 5, so it would be counted [00:02:13]. The empty set is also counted, with its sum considered 0, which is a multiple of 5 [00:05:36].

A brute-force approach, iterating through all possible subsets, would be impractical as there are 2^2000 total subsets—a "monstrously huge number" [00:02:48]. While a rough estimate might suggest that about a fifth of all subsets would have a sum divisible by 5 due to even distribution [00:03:28], the challenge lies in finding the precise answer [00:03:38].

### A Simpler Example

To understand the problem, consider a smaller set: {1, 2, 3, 4, 5} [00:03:38]. This set has 2^5 = 32 total subsets [00:04:48]. Listing these subsets and their sums reveals that 8 of them have a sum divisible by 5 [00:05:31]. This is slightly more than a fifth (6.4) of the total subsets [00:05:51].

## Generating Functions: The First Twist

The first "unexpected" approach to solving this problem involves a concept called a generating function [00:06:42].

> [!NOTE] What is a Generating Function?
> A generating function is a polynomial (or power series) where the coefficients encode answers to a question associated with positive integers [00:09:30]. By mathematically manipulating and analyzing the properties of this polynomial, insights into the original question can be gained [00:09:47]. A famous example is using generating functions to study Fibonacci numbers [00:09:59].

For the set {1, 2, 3, 4, 5}, the corresponding generating function is the polynomial:
`(1 + x) * (1 + x^2) * (1 + x^3) * (1 + x^4) * (1 + x^5)` <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>

When this polynomial is algebraically expanded, each term in the expansion corresponds to a unique subset [00:08:44]. The exponent of `x` in a term equals the sum of the corresponding subset's elements [00:08:53]. For example, choosing `x` from `(1+x)` and `x^2` from `(1+x^2)` corresponds to the subset {1, 2}, and their product `x^1 * x^2 = x^3` means this subset sums to 3 [00:08:16]. When like terms are collected, the coefficient of `x^n` tells us how many subsets sum to `n` [00:09:24]. For the example, three terms result in `x^10`, meaning three subsets sum to 10 [00:09:06].

For the main puzzle with the set 1 up to 2000, the generating function is:
`f(x) = (1 + x)(1 + x^2)(1 + x^3)...(1 + x^2000)` <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>

If expanded, this function `f(x) = c_0 + c_1x + c_2x^2 + ... + c_Nx^N` would have coefficients `c_n` that indicate the number of subsets with a sum of `n` [00:11:04]. The goal is to find the sum of coefficients `c_n` where `n` is divisible by 5.

## Complex Numbers as Filters: The Second Twist

Treating `f(x)` as an actual function and evaluating it at specific values of `x` can reveal properties of its coefficients [00:12:08].

*   **Evaluating at x = 0**: `f(0) = 1` [00:12:29]. In the expanded form, this leaves only `c_0` [00:12:34]. This tells us there is one subset with sum 0 (the empty set) [00:12:40].
*   **Evaluating at x = 1**: `f(1) = 2^2000` [00:12:57]. In the expanded form, `f(1)` sums all coefficients (`c_0 + c_1 + c_2 + ...`) [00:13:08]. This confirms the total number of subsets is 2^2000 [00:13:31].
*   **Evaluating at x = -1**: `f(-1) = 0` [00:13:53]. When plugged into the expanded form, `f(-1) = c_0 - c_1 + c_2 - c_3 + ...` [00:14:00]. This oscillating sum being zero implies an equal balance between the sums of even coefficients and odd coefficients [00:14:55]. This means half of all subsets have an even sum, and half have an odd sum [00:15:13].

> [!EXAMPLE] Filtering Even Coefficients
> The sum of coefficients corresponding to even sums can be found by `(f(1) + f(-1)) / 2` [00:15:35]. This effectively cancels out the odd coefficients, leaving only the even ones, summed and then halved [00:15:38].

The goal is to generalize this to filter for coefficients corresponding to sums divisible by 5 [00:16:01]. This is where [[complex_numbers_in_mathematics | complex numbers]] become essential, specifically, values that "rotate" with a period of 5 when raised to successive powers [00:16:28].

## Roots of Unity and Their Filtering Power

To achieve a period of 5, we extend into the [[complex_numbers_in_mathematics | complex plane]] and use the **fifth roots of unity** [00:16:34].

> [!NOTE] Roots of Unity
> The fifth roots of unity are the five complex numbers `z` that satisfy the equation `z^5 = 1` [00:18:43]. Geometrically, they are points evenly spaced around the unit circle in the [[complex_numbers_in_mathematics | complex plane]] [00:18:57].
>
> The primary non-real fifth root of unity, denoted `zeta` (ζ), is `e^(2πi/5)` (or `cos(72°) + i sin(72°)`), sitting "a fifth of a turn around the unit circle" [00:17:33].
>
> The key property for this problem is how its powers behave:
> *   `zeta^0 = 1`
> *   `zeta^1` (one-fifth turn)
> *   `zeta^2` (two-fifths turn)
> *   `zeta^3` (three-fifths turn)
> *   `zeta^4` (four-fifths turn)
> *   `zeta^5 = 1` (back to the start)
>
> This creates a cycle of 5 terms [00:18:11]. The sum of all `n`-th roots of unity is always 0, unless `n` is a multiple of the root's order (e.g., sum of fifth roots is 0) [00:20:00].

When evaluating a polynomial `P(x) = c_0 + c_1x + c_2x^2 + ...` at all five roots of unity and summing the results:
`P(ζ^0) + P(ζ^1) + P(ζ^2) + P(ζ^3) + P(ζ^4)` <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>

Due to the rotational property of roots of unity and the linearity of polynomials, terms `c_n * (ζ^k)^n` will cancel out if `n` is *not* a multiple of 5 [00:22:48]. However, if `n` *is* a multiple of 5, then `(ζ^k)^n` will always be `1` for any `k` [00:22:55]. This leads to a "constructive interference," where such terms contribute `5 * c_n` to the sum [00:22:55].

Therefore, the sum `P(ζ^0) + P(ζ^1) + P(ζ^2) + P(ζ^3) + P(ζ^4)` equals `5 * (c_0 + c_5 + c_10 + ...)` [00:23:02]. This means the total number of subsets whose sum is divisible by 5 is:
`(f(ζ^0) + f(ζ^1) + f(ζ^2) + f(ζ^3) + f(ζ^4)) / 5` <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>

## Calculating the Values

The next step is to evaluate `f(x)` at each of these five roots of unity. Recall `f(x) = (1 + x)(1 + x^2)...(1 + x^2000)`.

*   **`f(ζ^0) = f(1)`**: As calculated before, `f(1) = 2^2000` [00:29:06].

*   **`f(ζ^k)` for k = 1, 2, 3, 4**:
    Consider `f(ζ) = (1 + ζ)(1 + ζ^2)...(1 + ζ^2000)` <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
    Since powers of `ζ` repeat every 5 terms (`ζ^n = ζ^(n mod 5)`), the product can be simplified. The sequence `(1+ζ), (1+ζ^2), (1+ζ^3), (1+ζ^4), (1+ζ^5)` repeats 400 times (2000 / 5 = 400) [00:24:46].
    So, `f(ζ) = [(1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)]^400` [00:24:49].

    To evaluate the inner product `(1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)`, we use a final clever trick related to the definition of roots of unity [00:27:25].
    The roots of the polynomial `z^5 - 1` are `ζ^0, ζ^1, ζ^2, ζ^3, ζ^4` [00:27:33]. Therefore, `z^5 - 1` can be factored as:
    `z^5 - 1 = (z - ζ^0)(z - ζ^1)(z - ζ^2)(z - ζ^3)(z - ζ^4)` <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>
    We also know that `z^5 - 1 = (z - 1)(z^4 + z^3 + z^2 + z + 1)`.
    Equating the two factorizations and canceling `(z - 1)`:
    `z^4 + z^3 + z^2 + z + 1 = (z - ζ^1)(z - ζ^2)(z - ζ^3)(z - ζ^4)` <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>

    Now, substitute `z = -1` into this modified equation:
    `(-1)^4 + (-1)^3 + (-1)^2 + (-1)^1 + 1 = (-1 - ζ^1)(-1 - ζ^2)(-1 - ζ^3)(-1 - ζ^4)` <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>
    `1 - 1 + 1 - 1 + 1 = (-1)^4 (1 + ζ^1)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)`
    `1 = (1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)`

    Therefore, the product `(1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)` becomes `1 * (1 + ζ^5) = 1 * (1 + 1) = 2` [00:28:30].

    This means `f(ζ) = 2^400`.
    By the same logic, `f(ζ^2)`, `f(ζ^3)`, and `f(ζ^4)` also equal `2^400` [00:28:51]. This is because raising the roots to a power (e.g., `ζ^2`) simply shuffles their order in the product `(1+x)(1+x^2)...`, maintaining the same set of terms [00:21:12].

### The Final Answer

Summing the evaluated functions:
`f(ζ^0) + f(ζ^1) + f(ζ^2) + f(ζ^3) + f(ζ^4)`
`= 2^2000 + 2^400 + 2^400 + 2^400 + 2^400`
`= 2^2000 + 4 * 2^400` <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>

The total number of subsets whose sum is divisible by 5 is:
` (2^2000 + 4 * 2^400) / 5 ` <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>

> [!EXAMPLE] Sanity Check for the Smaller Case
> For the set {1, 2, 3, 4, 5}, the formula yields:
> `(2^5 + 4 * 2^1) / 5 = (32 + 8) / 5 = 40 / 5 = 8` <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>
> This matches the result obtained by direct enumeration [00:30:08].

## Broader Implications and Connections

This problem, though a "toy problem," demonstrates powerful mathematical techniques. The core idea involves:
1.  Representing a discrete sequence (number of subsets with a given sum) as coefficients of a polynomial (a generating function) [00:30:48].
2.  Evaluating that polynomial on [[complex_numbers_in_mathematics | complex values]] to extract specific information about the coefficients [00:30:52].

This approach is not unique to this puzzle. The way mathematicians study prime numbers, particularly in the context of the Riemann hypothesis, involves similar principles [00:31:08]. They consider a function (a Dirichlet series, not quite a polynomial) whose coefficients carry information about prime numbers, and then analyze this function using [[complex_numbers_and_transformations | complex-valued inputs]] [00:31:53]. The ability to extend the domain of inputs beyond real numbers offers significant analytical power [00:32:22].

The "unreasonable usefulness" of [[complex_numbers_in_mathematics | complex numbers]] often stems from their unique properties related to [[complex_numbers_multiplication_and_rotation | rotation]] and frequency [00:32:32]. In this puzzle, the use of [[geometric_interpretation_of_complex_numbers | roots of unity]] on the unit circle allowed for the detection of frequency information (sums divisible by 5) [00:33:04]. This concept is fundamental to the [[complex_numbers_and_fourier_transform | Fourier Transform]] and Fourier series, which are indispensable in fields like signal processing [00:33:51]. Even Shor's algorithm for quantum computers, used to factor large numbers, leverages [[complex_numbers_and_imaginary_exponents | roots of unity]] to detect frequency information [00:33:41].

To learn more about generating functions, the book "GeneratingFunctionology" by Herbert Wilf is highly recommended [00:34:05].