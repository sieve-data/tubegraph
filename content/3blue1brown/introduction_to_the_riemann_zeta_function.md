---
title: Introduction to the Riemann zeta function
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 
The [[Introduction to the Riemann zeta function | Riemann zeta function]] is a significant object in modern mathematics, often heard of but challenging to grasp <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It's famous due to a one-million-dollar prize associated with solving the [[the_riemann_hypothesis_and_trivial_zeros | Riemann hypothesis]], which asks when the function equals zero <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Some may also recognize it from the context of the divergent sum 1 + 2 + 3 + 4... up to infinity, which is sometimes said to equal -1/12 <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This seemingly nonsensical result is defined using the [[Introduction to the Riemann zeta function | Riemann zeta function]] through a concept called analytic continuation <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Initial Definition of the Zeta Function

The [[Introduction to the Riemann zeta function | Riemann zeta function]], denoted as `zeta(s)`, is initially defined as an infinite sum for a given input `s` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>:
`zeta(s) = 1/(1^s) + 1/(2^s) + 1/(3^s) + 1/(4^s) + ...` summing over all natural numbers <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

For instance, if `s = 2`, the sum becomes `1 + 1/4 + 1/9 + 1/16 + ...` which approaches `pi^2/6`, approximately 1.645 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This sum converges, meaning it approaches a finite number <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

However, this initial definition only holds when `s` is greater than 1 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For values like `s = -1`, the sum `1 + 2 + 3 + 4 + ...` clearly doesn't approach -1/12 <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Similarly, for `s = -2`, the sum `1 + 4 + 9 + 16 + ...` doesn't approach zero <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This highlights the need for a more comprehensive definition for the [[Introduction to the Riemann zeta function | function]] to be defined for other values <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Complex Inputs and Exponents

Bernhard Riemann, a key figure in complex analysis, focused on understanding the [[Introduction to the Riemann zeta function | zeta function]] when `s` is a [[introduction_to_complex_numbers | complex number]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Raising a number to a complex power extends beyond simple repeated multiplication <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

When a number (e.g., 1/2) is raised to a complex power `a + bi`, it's split into `(1/2)^a * (1/2)^(bi)` <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The term `(1/2)^(bi)` results in a [[introduction_to_complex_numbers | complex number]] on the unit circle <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. As the imaginary input `bi` changes, the output rotates around the unit circle <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

This means that when a complex number `s = a + bi` is plugged into the [[Introduction to the Riemann zeta function | zeta function]], each term `1/n^s` can be thought of as `1/(n^a)` (which determines the size) multiplied by `1/(n^bi)` (which dictates a rotation) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. If the real part of `s` (i.e., `a`) is greater than 1, the sum `1/(n^a)` converges, and the additional rotations cause the sum to converge in a spiral towards a specific point in the [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Visualizing Complex Functions

Complex functions can be visualized as transformations, where every input point in the [[introduction_to_complex_numbers | complex plane]] moves to its corresponding output point <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. For example, the function `f(s) = s^2` transforms a grid by squaring each point <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

The [[Introduction to the Riemann zeta function | Riemann zeta function]] defined by the infinite sum on the right half of the [[introduction_to_complex_numbers | complex plane]] (where the real part of `s` is greater than 1) is shown as a transformation <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This [[visualization_of_the_riemann_zeta_function | visualization]] reveals how the grid lines are stretched and curved <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### Analytic Continuation: Extending the Function

The transformed grid lines for the [[Introduction to the Riemann zeta function | zeta function]] appear to abruptly stop <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This suggests extending the function's definition beyond its initial domain (where the sum converges) into the left half of the [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

However, the original infinite sum doesn't make sense for `s` values whose real part is less than 1 <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The question then becomes how to define the [[Introduction to the Riemann zeta function | function]] on the rest of the plane <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

The crucial concept is "analytic continuation." If we add the restriction that the new extended function must have a derivative everywhere (be "analytic"), it uniquely determines the extension <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

#### What Does "Analytic" Mean Geometrically?

For complex functions, "having a derivative everywhere" (being analytic) has a clear geometric intuition: it means the function is "angle-preserving" <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. If two lines in the input space intersect at a certain angle, after the transformation, the corresponding curved lines will still intersect at that *same* angle <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This is easily seen by observing how the grid lines, after transformation, still intersect at right angles <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

This angle-preserving property is highly restrictive <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. Yet, most named functions are analytic <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. The [[Introduction to the Riemann zeta function | Riemann zeta function]], defined by its sum, is analytic on its initial domain <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

> [!Definition] Analytic Continuation
> The process of extending an analytic function beyond its original domain in the *only possible way* that preserves its analytic (angle-preserving) property <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. It's like an "infinite continuous jigsaw puzzle" with only one solution <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

Thus, the full [[Introduction to the Riemann zeta function | Riemann zeta function]] is defined in two parts: the infinite sum for inputs where the real part is greater than 1, and the unique analytic continuation for the rest of the [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

### The Riemann Hypothesis

The places where the [[Introduction to the Riemann zeta function | Riemann zeta function]] equals zero (i.e., points mapped to the origin after transformation) are crucial <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.

*   **[[the_riemann_hypothesis_and_trivial_zeros | Trivial Zeros]]**: One known property of the analytic continuation is that all negative even numbers (e.g., -2, -4) are mapped to zero <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. These are called "trivial" because mathematicians understand them well, despite their non-obvious nature <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
*   **Non-Trivial Zeros**: All other zeros of the [[Introduction to the Riemann zeta function | function]] lie within a specific region called the "critical strip" <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. Their placement encodes significant information about [[Riemann hypothesis and prime numbers | prime numbers]] <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

> [!Theorem] The Riemann Hypothesis
> Riemann hypothesized that all of these non-trivial zeros sit precisely on the "critical line," which is the line of [[introduction_to_complex_numbers | complex numbers]] `s` whose real part is exactly one-half <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.

Proving this hypothesis would earn one million dollars from the Clay Math Institute and validate hundreds, if not thousands, of existing mathematical results contingent on its truth <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. The [[visualization_of_the_riemann_zeta_function | visualization]] of the transformed critical line shows it passing through zero many times <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

### The Divergent Sum Revisited

The seemingly nonsensical result that `1 + 2 + 3 + 4 + ...` equals -1/12 comes from the analytic continuation of the [[Introduction to the Riemann zeta function | Riemann zeta function]], where `zeta(-1)` maps to -1/12 <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. It's important to remember that this value is not derived from the original divergent sum directly, but from the unique extended definition of the [[Introduction to the Riemann zeta function | zeta function]] <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. The uniqueness of this analytic continuation, however, suggests a profound intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.