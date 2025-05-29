---
title: Understanding complex functions and their transformations
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

The Riemann zeta function is a significant object in modern mathematics that can be challenging to understand <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This function is notably associated with a one million dollar prize for anyone who can determine when it equals zero, a challenge known as the [[riemann_hypothesis | Riemann hypothesis]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It's also linked to the seemingly nonsensical idea that the divergent sum 1 + 2 + 3 + 4... up to infinity can equal negative 1/12 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Defining this equation often uses the Riemann zeta function, relying on a concept called [[analytic_continuation | analytic continuation]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Defining the Riemann Zeta Function

The Riemann zeta function, typically denoted as ζ(s) for a given input `s`, is initially defined as an infinite sum:
ζ(s) = 1/1^s + 1/2^s + 1/3^s + 1/4^s + ... <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
This sum adds up reciprocals of natural numbers raised to the power of `s` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

For example, when `s = 2`, the sum becomes 1 + 1/4 + 1/9 + 1/16..., which converges to π²/6 (approximately 1.645) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This sum converges and makes sense only when the real part of `s` is greater than 1 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Beyond this domain, the sum diverges, leading to results like 1 + 2 + 3 + 4... up to infinity, which doesn't approach any value <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Complex Inputs and Exponents

Bernard Riemann was instrumental in developing [[multivariable_calculus_and_complex_analysis | complex analysis]], which studies functions with [[conceptualizing_complex_numbers | complex numbers]] as both inputs and outputs <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. His focus was on understanding the zeta function when `s` is a complex value, like 2 + *i* <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

Raising a number to the power of a [[conceptualizing_complex_numbers | complex number]] (e.g., 1/2 raised to a complex power) can be a strange idea since it doesn't relate to repeated multiplication <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. However, there's a natural way to extend the definition of exponents into the realm of complex values <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The basic idea is that a base raised to a complex number (e.g., `a^(x+iy)`) can be split into `a^x * a^(iy)` <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. When a number is raised to a pure imaginary number (`a^(iy)`), the result is a [[conceptualizing_complex_numbers | complex number]] on the unit circle in the complex plane <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This component rotates the number without changing its size <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

When the input `s` has a complex part (e.g., 2 + *i*), each term in the zeta sum gets rotated by some amount, but their lengths (magnitudes) remain unchanged <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This means the sum still converges for `s` values whose real part is greater than 1, spiraling to a specific point in the complex plane <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Visualizing Complex Functions as Transformations

A powerful way to understand [[complex_numbers_and_transformations | complex functions]] is to visualize them as transformations <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This involves looking at every possible input to the function and mapping it to its corresponding output <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

Consider a simpler example, `f(s) = s²` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>:
*   `s = 2` maps to `4` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   `s = -1` maps to `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   `s = i` maps to `-1` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

Visualizing this as a transformation of a grid in the complex plane reveals a rich picture of the function's behavior in two dimensions <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

Applying this to the Riemann zeta function, a grid on the right half of the complex plane (where the real part of numbers is greater than 1) can be transformed by the function <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The resulting transformed grid shows how points move to their zeta outputs <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## [[analytic_continuation | Analytic Continuation]]: Extending the Function

The transformed grid of the Riemann zeta function on its initial domain (real part of `s` > 1) appears to "beg" for extension <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. For example, the arcs formed by lines after transformation suggest a natural continuation <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. When extending the function into the left half of the plane (where the original sum definition doesn't converge), the challenge is to define the function in a meaningful way <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### The Constraint of Analyticity

While one might think there are many ways to extend the function, adding the restriction that the new extended function must have a [[taking_derivatives_of_complex_combinations_of_functions | derivative]] everywhere locks it into one unique possible extension <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

For [[complex_numbers_and_transformations | complex functions]], the property of having a derivative everywhere has a powerful [[derivatives_of_simple_functions_and_their_intuition | geometric intuition]]: it is "angle-preserving" <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. If two lines in the input space intersect at a certain angle, after the transformation, their transformed curves will still intersect at the same angle <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This is easily seen by observing how grid lines, which initially intersect at right angles, continue to intersect at right angles after the transformation <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

Complex functions that have a derivative everywhere are called **analytic** <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. The field of [[multivariable_calculus_and_complex_analysis | complex analysis]] leverages these properties of analytic functions <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The Riemann zeta function, as defined by its infinite sum on the right half of the plane, is an analytic function <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

The surprising fact is that if an analytic function is extended beyond its original domain, requiring the new function to remain analytic (angle-preserving) forces it into only one possible extension, if such an extension exists <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This process is known as [[analytic_continuation | analytic continuation]] <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

Therefore, the full Riemann zeta function is defined in two parts:
1.  For `s` values with a real part greater than 1, it's defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
2.  For the rest of the complex plane, it's defined by the unique [[analytic_continuation | analytic continuation]] of that sum <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

## The [[riemann_hypothesis | Riemann Hypothesis]]

A crucial aspect of the Riemann zeta function involves the points where it equals zero <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   **Trivial Zeros**: The negative even numbers (-2, -4, -6...) are mapped to zero by the extended function <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. These are considered "trivial" because they are well-understood <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Non-trivial Zeros**: All other points that map to zero are located within a region called the "critical strip" <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. The specific placement of these non-trivial zeros encodes surprising information about prime numbers <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

The [[riemann_hypothesis | Riemann hypothesis]] states that all of these non-trivial zeros sit precisely in the middle of this strip, on the line where the real part of `s` is one half <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. This is known as the "critical line" <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Proving this hypothesis would yield a million-dollar prize and confirm thousands of existing mathematical results <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

### The "Nonsensical" Sum (1+2+3... = -1/12)

The extended Riemann zeta function maps the point `s = -1` to `-1/12` <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. If this were plugged into the *original* sum definition, it would appear to suggest that 1 + 2 + 3 + 4... up to infinity equals -1/12 <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. However, this definition for `s = -1` does not come directly from the sum itself, as the sum diverges for `s = -1` <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. Instead, it arises from the unique [[analytic_continuation | analytic continuation]] of the sum beyond its domain of convergence <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. The uniqueness of this continuation suggests a deep, intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.