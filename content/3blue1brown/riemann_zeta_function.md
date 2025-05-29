---
title: Riemann zeta function
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

The [[riemann_zeta_function | Riemann zeta function]] is a significant object in modern mathematics, though it can be challenging to understand <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is notably associated with a one million dollar prize for resolving the [[riemann_hypothesis | Riemann hypothesis]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Initial Definition: An Infinite Sum

The [[riemann_zeta_function | Riemann zeta function]], denoted as zeta(s), is initially defined for a given input `s` as an infinite sum over all natural numbers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>:

$$ \zeta(s) = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots $$ <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

For instance, when `s = 2`, the sum becomes:
$$ \zeta(2) = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots $$
This sum converges to $\pi^2/6$, which is approximately 1.645 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The appearance of [[pi_and_its_formulas_involving_primes | pi]] in this context is a significant mathematical beauty <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For values of `s` greater than 1, the terms in the sum become increasingly smaller, ensuring that the sum approaches a specific number <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

However, for `s` values less than or equal to 1, this initial definition leads to divergent sums. For example, if `s = -1`, the sum becomes `1 + 2 + 3 + 4 + ...`, which obviously does not approach a finite value <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Similarly, for `s = -2`, the sum is `1 + 4 + 9 + 16 + ...`, which also diverges <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This suggests that the function is only defined for `s > 1` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Complex Inputs and Exponents

Bernard Riemann, a pioneer in complex analysis, focused on understanding the [[riemann_zeta_function | zeta function]] when `s` is a complex number <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Raising a number to a complex power extends the concept of exponents beyond repeated multiplication <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

When a number (like 1/2) is raised to a complex power (e.g., `2 + i`), it can be split into two parts: `(1/2)^2 * (1/2)^i` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The `(1/2)^2` part determines the size, while the `(1/2)^i` part, involving a pure imaginary exponent, results in a complex number on the unit circle <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. As the imaginary part of the exponent changes, the output point moves around the unit circle <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

When a complex number `s` is plugged into the [[riemann_zeta_function | zeta function]]:
*   The real part of `s` determines the size of each term in the sum <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   The imaginary part of `s` dictates a rotation for each term <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

For inputs `s` where the real part is greater than 1, the sum still converges, but it does so in a spiral path in the complex plane <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This means that the initial sum definition is valid for all complex numbers whose real part is greater than 1, forming the right half of the complex plane <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## Visualizing Complex Functions

Complex functions can be visualized as transformations, where every input point moves to its corresponding output point <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. For example, `f(s) = s^2` transforms points like `2` to `4`, `-1` to `1`, and `i` to `-1` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. When applied to a grid in the complex plane, such a transformation shows how the entire plane is stretched and rotated <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

Visualizing the [[riemann_zeta_function | zeta function]] involves transforming the right half of the complex plane (where the real part of `s` is greater than 1) to its corresponding outputs <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The resulting transformed grid shows beautifully curved lines that abruptly stop at the boundary where the real part of `s` equals 1 <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Analytic Continuation

The sudden termination of the transformed grid lines suggests that the function could be extended beyond its initial domain of definition (where the sum converges) <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This process is known as **analytic continuation** <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

To achieve this extension, a crucial restriction is applied: the new extended function must be **analytic** everywhere <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

> [!NOTE] The property of being "analytic" for a complex function roughly means that it preserves angles between intersecting lines after the transformation <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. For example, a grid of perpendicular lines in the input space will transform into a grid of perpendicular curves in the output space <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

This angle-preserving property is very restrictive <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The remarkable fact is that if an analytic function needs to be extended beyond its original domain, requiring the new function to *also* be analytic everywhere forces it into **one and only one possible extension** <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This is akin to an infinite jigsaw puzzle where the angle-preserving requirement provides a unique solution <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

Thus, the full [[riemann_zeta_function | Riemann zeta function]] is defined in two parts:
1.  For complex numbers `s` with a real part greater than 1, it is defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
2.  For the rest of the complex plane, it is defined by its unique analytic continuation, which ensures the function remains angle-preserving everywhere <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

This definition is implicit, relying on the existence and uniqueness of the analytic continuation <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

## Key Properties and the Riemann Hypothesis

### Zeros of the Zeta Function

The points where the [[riemann_zeta_function | zeta function]] equals zero are of great importance <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   **Trivial Zeros**: The negative even numbers (`-2, -4, -6, ...`) are mapped to zero <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. These are called "trivial" because mathematicians understand them well, even if they aren't immediately obvious <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Non-trivial Zeros**: The remaining zeros are located within a vertical band in the complex plane called the **critical strip** <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. The precise placement of these zeros holds surprising information about [[connection_between_zeta_function_and_prime_numbers | prime numbers]] <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

### The Riemann Hypothesis

The [[riemann_hypothesis | Riemann hypothesis]] states that all non-trivial zeros of the [[riemann_zeta_function | zeta function]] lie exactly on the **critical line**, which is the line of complex numbers `s` whose real part is exactly one half <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. If proven true, this hypothesis would provide a profound understanding of the pattern of [[connection_between_zeta_function_and_prime_numbers | prime numbers]] and impact numerous other mathematical results <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. Observing the transformation of the critical line shows it passing through zero many times <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Proving this hypothesis would earn one million dollars from the Clay Math Institute <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

### Zeta of Negative One

Another known property of the analytically continued [[riemann_zeta_function | zeta function]] is that it maps the point `s = -1` to the value `-1/12` <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. This means that, through analytic continuation, the sum `1 + 2 + 3 + 4 + ...` can be understood to "equal" -1/12 <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. While this result seems counter-intuitive based on the original divergent sum, the uniqueness of the analytic continuation suggests a deep intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.