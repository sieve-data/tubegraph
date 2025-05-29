---
title: Analytic continuation
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

[[Analytic vs geometric reasoning | Analytic continuation]] is a fundamental concept in complex analysis, allowing for the extension of a function's domain while preserving crucial properties. It is notably used to define the [[Riemann zeta function | Riemann zeta function]] across the entire complex plane beyond its initial convergent sum definition <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Riemann Zeta Function: Initial Definition

The [[Riemann zeta function | Riemann zeta function]], denoted as zeta(s), is initially defined as an infinite sum:
$$ \zeta(s) = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots $$
This sum is taken over all natural numbers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

For example, when `s = 2`, the sum is:
$$ \zeta(2) = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots $$
This sum approaches a value of $\pi^2/6$, approximately 1.645 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For values where `s` is greater than 1, this sum converges to a specific number <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

However, for `s` values less than or equal to 1, the infinite sum definition breaks down. For instance, plugging in `s = -1` results in the sum `1 + 2 + 3 + 4 + ...` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, which obviously does not approach any finite value <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Similarly, for `s = -2`, the sum becomes `1 + 4 + 9 + 16 + ...` <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, which also diverges <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Therefore, based on this sum, the function is only defined when the real part of `s` is greater than 1 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Extending to Complex Numbers

[[Riemann zeta function | Bernard Riemann]], a key figure in complex analysis, focused on understanding functions where inputs and outputs are [[Continuity and function limits in mathematical curves | complex numbers]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This means `s` can be a complex value, such as `2 + i` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

When raising a number to a complex power (e.g., `1/2` to the power of a complex number), it can be split into `(1/2)^(real part) * (1/2)^(pure imaginary part)` <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The term raised to a pure imaginary part will result in a [[Continuous mapping and its application in topology | complex number]] on the unit circle in the complex plane <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This means it rotates the number without changing its size <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

For the [[Riemann zeta function | zeta function]], when the input `s` has a complex part, each term in the sum gets rotated <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Crucially, the lengths of these terms do not change <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, so the sum still converges in a spiral pattern to a specific point on the complex plane, as long as the real part of the input `s` is greater than 1 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Visualizing Complex Functions as Transformations

Complex functions can be visualized as transformations, where every input point on a grid moves to its corresponding output point <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. For example, the function `f(s) = s^2` transforms points:
*   `s = 2` moves to `4` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   `s = -1` moves to `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   `s = i` moves to `-1` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

When applying the [[Visualizing integration and approximations | zeta function transformation]] to the right half of the complex plane (where `Re(s) > 1`), the grid lines transform into curved arcs <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. These transformed curves appear to "beg" to be extended into the left half of the plane <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## The Principle of Analytic Continuation

While the original sum definition of the [[Riemann zeta function | zeta function]] doesn't work for `Re(s) <= 1` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>, the visual transformation suggests a natural extension. The question then becomes: how should this function be defined on the rest of the complex plane <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>?

This is where the concept of an [[Analytic vs geometric reasoning | analytic function]] becomes critical. An analytic function is one that has a [[Visualizing derivatives beyond graphs | derivative]] everywhere <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Geometrically, this translates to an "angle-preserving property" <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>: any two lines intersecting at a certain angle in the input space will still intersect at that same angle after the function's transformation <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This is easily observed by how the grid lines still intersect at right angles after transformation <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

This angle-preserving property is highly restrictive <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The surprising fact is that if an [[Analytic vs geometric reasoning | analytic function]] is extended beyond its original domain, and it is required that the new extended function also remains analytic (i.e., angle-preserving everywhere), then there is *only one possible extension*, if one exists at all <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>, <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This uniqueness is akin to solving an infinite jigsaw puzzle where the angle-preserving constraint dictates the only correct fit <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

This process of uniquely extending an [[Analytic vs geometric reasoning | analytic function]] is called [[Analytic vs geometric reasoning | analytic continuation]] <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

## The Riemann Zeta Function and Its Continuation

The full [[Riemann zeta function | Riemann zeta function]] is defined through [[Analytic vs geometric reasoning | analytic continuation]] <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. For the right half of the complex plane (where `Re(s) > 1`), it's defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. For the rest of the plane, it's defined by the unique analytic continuation of that sum <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. This is an implicit definition, relying on the fact that such a unique extension must exist <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

### Important Consequences:

*   **Riemann Hypothesis**: The [[Riemann zeta function | Riemann hypothesis]] is an unsolved problem regarding the locations where the analytically continued [[Riemann zeta function | zeta function]] equals zero <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
    *   **Trivial Zeros**: It is known that the negative even numbers (`-2, -4, -6, ...`) are mapped to zero by the continued function; these are called "trivial zeros" <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>, <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
    *   **Non-trivial Zeros**: All other zeros of the function lie within a vertical strip called the "critical strip" <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>, <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. These non-trivial zeros encode crucial information about [[Integration and averaging continuous variables | prime numbers]] <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
    *   [[Riemann zeta function | Riemann]] hypothesized that all non-trivial zeros lie on the "critical line," where the real part of `s` is one-half <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>, <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. Proving this hypothesis would have significant implications for understanding [[Integration and averaging continuous variables | prime numbers]] and other mathematical patterns <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>, <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

*   **The "Sum" 1 + 2 + 3 + ... = -1/12**: While the infinite sum `1 + 2 + 3 + ...` diverges, the analytically continued [[Riemann zeta function | zeta function]] maps the input `s = -1` to the output `-1/12` <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. This result is obtained by defining the function via [[Analytic vs geometric reasoning | analytic continuation]] to the left half of the plane, not directly from the original divergent sum <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. The uniqueness of this continuation suggests a deep, intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.