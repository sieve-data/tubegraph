---
title: Cycling behaviors using roots of unity
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

Complex numbers, despite their seemingly abstract nature, prove to be "unreasonably useful" for solving problems in discrete mathematics, especially when dealing with questions related to cycling behaviors or patterns <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This utility is particularly evident when using "roots of unity" to filter and count specific elements within a set based on properties like divisibility.

## The Unexpected Role of Complex Numbers
Initially, it seems absurd to use complex numbers to solve purely discrete questions involving whole numbers and their sums <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, just as complex numbers are fundamental to understanding the distribution of prime numbers and the Riemann hypothesis <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, they offer powerful techniques for analyzing discrete sequences. The core idea involves treating a discrete sequence as coefficients of a polynomial (a "generating function") and then evaluating that polynomial using complex values <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>.

## Introduction to Roots of Unity
[[newtons_fractal_and_roots_of_polynomial_equations | Roots of polynomial equations]] are numbers that solve an equation like `z^n = 1` <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. When `n` is 5, these are called the fifth roots of unity. These roots, including 1 itself (which can be considered the "zeroth" root), are specific complex numbers that, when plotted, are evenly spaced around the unit circle in the complex plane <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

For instance, the fifth roots of unity include `zeta` (e.g., e^(2πi/5)), `zeta^2`, `zeta^3`, `zeta^4`, and `zeta^0` (which is 1) <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
Their defining characteristic is their "cycling behavior": when raised to the fifth power, each of them returns to 1 <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This means `zeta^5 = 1`, `(zeta^2)^5 = 1`, and so on. This cyclical property is key to their application.

## Applying Roots of Unity for Filtering
Consider a generating function `f(x) = c_0 + c_1x + c_2x^2 + ... + c_N x^N`, where each coefficient `c_n` represents the number of subsets with a sum of `n` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. The goal is to find the sum of coefficients `c_n` where `n` is divisible by 5.

A similar, simpler example can be seen by evaluating `f(1)` and `f(-1)`:
*   `f(1)` sums all coefficients (`c_0 + c_1 + c_2 + ...`) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   `f(-1)` creates an alternating sum (`c_0 - c_1 + c_2 - ...`) <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
    *   The terms `(-1)^n` effectively rotate by 180 degrees <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    *   When `f(-1)` evaluates to 0 (as it does in the example for subsets of 1 to 2000), it implies an equal balance between even and odd coefficients (i.e., `c_0 + c_2 + ... = c_1 + c_3 + ...`) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
    *   Adding `f(1)` and `f(-1)` and dividing by 2 effectively "filters" out the odd coefficients, leaving only the sum of even coefficients <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

This concept can be generalized to find coefficients divisible by 5. By evaluating the generating function `f(x)` at all five roots of unity (`1, zeta, zeta^2, zeta^3, zeta^4`) and summing the results, a powerful filtering mechanism emerges <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
*   For any term `c_k x^k` in the polynomial expansion, when `x` is a root of unity:
    *   If `k` is a multiple of 5 (e.g., `k=5m`), then `(root of unity)^k` will always evaluate to `1` (because `(root of unity)^5 = 1`). These terms will "constructively interfere" <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
    *   If `k` is *not* a multiple of 5, then the sum `(root of unity_0)^k + (root of unity_1)^k + ... + (root of unity_4)^k` will sum to zero due to their balanced distribution around the origin <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. These terms "cancel out" or "destructively interfere".

Therefore, the sum `f(1) + f(zeta) + f(zeta^2) + f(zeta^3) + f(zeta^4)` will yield 5 times the sum of coefficients `c_k` where `k` is a multiple of 5 <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Dividing this sum by 5 gives the exact answer to the problem.

## Broader Significance
This technique, using roots of unity to extract frequency information, is incredibly powerful and appears in many areas of mathematics and computer science <a class="yt-timestamp" data-t="00:33:20">[00:33:20]</a>.
*   It forms the core idea behind Fourier transforms and Fourier series, which are essential tools for analyzing frequencies in signals and data <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
*   It's utilized in advanced algorithms, such as Shor's algorithm for quantum computers, which leverages roots of unity to detect frequency information for factoring large numbers <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>.
*   The approach of using a function whose coefficients encode discrete information and then studying its behavior with complex inputs is a cornerstone of modern number theory, exemplified by Riemann's study of primes using the Zeta function <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

By extending the domain to complex numbers, mathematicians gain more power in making deductions about coefficients, revealing patterns and frequencies that might otherwise remain hidden in purely discrete systems <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>.