---
title: Analytic continuation and complex analysis
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

The Riemann zeta function is a significant object in modern mathematics, though it can be challenging to understand <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is widely known due to a one million dollar prize offered for proving the Riemann hypothesis, which concerns the function's zeros <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The function is also connected to the divergent sum 1 + 2 + 3 + 4... up to infinity, which, in a particular sense, is said to equal -1/12 <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This seemingly nonsensical result is defined using the Riemann zeta function via a concept called [[analytic_continuation | analytic continuation]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Defining the Riemann Zeta Function

The Riemann zeta function, often denoted with the variable *s*, is initially defined as an infinite sum over all natural numbers <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>:
$$ \zeta(s) = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \dots $$
For example, if *s* = 2, the sum becomes 1 + 1/4 + 1/9 + 1/16... <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This sum converges to $\pi^2/6$, approximately 1.645 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For values of *s* greater than 1, this sum converges to a specific number, making it a reasonable function <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

However, for values of *s* less than or equal to 1, the infinite sum does not converge <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For instance, if *s* = -1, the sum becomes 1 + 2 + 3 + 4..., which clearly diverges <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Similarly, for *s* = -2, it becomes 1 + 4 + 9 + 16..., which also diverges and does not approach zero <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Yet, specific values like $\zeta(-1) = -1/12$ and $\zeta(-2) = 0$ are associated with the function <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Complex Inputs and Visualization

Bernard Riemann significantly contributed to [[multivariable_calculus_and_complex_analysis | complex analysis]], which involves studying functions that take [[complex_numbers | complex numbers]] as inputs and produce [[complex_numbers | complex numbers]] as outputs <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Instead of limiting *s* to the real number line, Riemann focused on what happens when *s* is a [[complex_numbers | complex number]] (e.g., 2 + *i*) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

Raising a number to a [[complex_numbers | complex number]] involves a specific extension of exponent definitions <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. If you raise a number (like 1/2) to a [[complex_numbers | complex number]] (e.g., 2 + *i*), you split it into a real part and a pure imaginary part (1/2 to the power of 2, multiplied by 1/2 to the power of *i*) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The pure imaginary part results in a [[geometric_interpretation_of_complex_numbers | complex number]] on the unit circle in the [[conceptualizing_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. As the imaginary input varies, the output moves around the unit circle <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This means that when a term like 1/2 to the power of *i* is multiplied by 1/2 squared, it rotates the result without changing its magnitude <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

When plugging a complex number *s* into the zeta function, each term in the sum gets rotated <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. The lengths of these terms do not change, so the sum still converges for inputs where the real part of *s* is greater than 1 <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This convergence results in a spiral in the [[conceptualizing_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
<a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
This demonstrates that the zeta function, defined as an infinite sum, is a valid [[understanding_complex_functions_and_their_transformations | complex function]] as long as the real part of *s* is greater than 1 <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This means the input *s* must be in the right half of the [[conceptualizing_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Complex Functions as Transformations

A common way to visualize [[understanding_complex_functions_and_their_transformations | complex functions]] is to view them as transformations <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This involves observing how every point in an input grid moves to its corresponding output <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. For example, for *f*(*s*) = *s*², an input of 2 maps to 4, -1 maps to 1, and *i* maps to -1 <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. When a grid is transformed by *f*(*s*) = *s*², it creates a rich visual representation of the function's behavior <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
<a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>

When applying this visualization to the Riemann zeta function for inputs where the real part is greater than 1, the transformed grid shows a specific pattern <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The transformed grid reveals lovely arcs that abruptly stop at the boundary where the real part of *s* is 1 <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This visual encourages the idea of extending the function beyond its initial domain <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
<a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>

## Analytic Continuation

When the input *s* moves to a region where its real part is less than 1, the original infinite sum definition of the zeta function no longer makes sense <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. However, the visual transformation suggests that the function's definition can be extended <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

Initially, one might think that there could be many ways to extend the function into this new domain <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. However, if an additional restriction is applied – that the new extended function must have a derivative everywhere – it forces the extension into one and only one possible form <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Geometric Intuition: Angle Preservation

For [[multivariable_calculus_and_complex_analysis | complex functions]], the property of "having a derivative everywhere" has a strong [[geometric_interpretation_of_complex_numbers | geometric intuition]] <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. If a function has a derivative everywhere, it means that any two lines in the input space that intersect at a certain angle will still intersect at that *same angle* after the transformation <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. The lines might curve, but the angle between them is preserved <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This is easily seen by observing how the grid lines, which initially intersect at right angles, continue to intersect at right angles after the transformation <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

Complex functions that possess a derivative everywhere are called [[continuity_and_mathematical_functions | analytic]] <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Therefore, the term [[continuity_and_mathematical_functions | analytic]] can be intuitively understood as "angle-preserving" <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. (A minor caveat: at inputs where the derivative is zero, angles are multiplied by an integer, but this is rare <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.) The field of [[multivariable_calculus_and_complex_analysis | complex analysis]] heavily relies on leveraging the properties of [[continuity_and_mathematical_functions | analytic functions]] <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

The Riemann zeta function, as defined by its infinite sum on the right half of the plane, is an [[continuity_and_mathematical_functions | analytic function]] <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. The transformed grid lines continue to intersect at right angles, confirming this property <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### The Uniqueness Principle

A surprising fact about [[multivariable_calculus_and_complex_analysis | complex functions]] is that if an [[continuity_and_mathematical_functions | analytic function]] is extended beyond its original domain (e.g., extending the zeta function into the left half of the plane), requiring the new extended function to *still be [[continuity_and_mathematical_functions | analytic]]* (i.e., angle-preserving everywhere) limits the extension to *only one possible form*, if such an extension exists <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. This process of extending an [[continuity_and_mathematical_functions | analytic function]] in the only possible way that remains [[continuity_and_mathematical_functions | analytic]] is called [[analytic_continuation | analytic continuation]] <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

The full Riemann zeta function is defined as follows:
*   For values of *s* in the right half of the [[conceptualizing_complex_numbers | complex plane]] (where the real part of *s* > 1), it is defined by the converging infinite sum <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
*   For the rest of the [[conceptualizing_complex_numbers | complex plane]], it is defined by the unique [[analytic_continuation | analytic continuation]] of that sum <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This definition is valid because only one such [[analytic_continuation | analytic continuation]] exists <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

This makes the definition of the zeta function on the left half of the plane rather implicit, relying on the solution of this unique "jigsaw puzzle" <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

## Zeros and the Riemann Hypothesis

The points where the Riemann zeta function equals zero (where points are mapped to the origin after transformation) are particularly important <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

*   **Trivial Zeros**: The [[analytic_continuation | extended function]] maps negative even numbers to zero <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. These are called "trivial zeros" because they are well-understood <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
*   **Non-trivial Zeros**: The remaining zeros lie within a specific region of the [[conceptualizing_complex_numbers | complex plane]] called the "critical strip" <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. The precise locations of these non-trivial zeros hold surprising information about prime numbers <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

### The Riemann Hypothesis

Riemann hypothesized that all of these non-trivial zeros are located exactly in the middle of the critical strip, on the line of [[complex_numbers | complex numbers]] *s* where the real part is one half <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. This line is known as the "critical line" <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. If this hypothesis is true, it provides a remarkably strong understanding of the pattern of prime numbers and many other mathematical patterns <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

When the critical line is transformed by the zeta function, it passes through the number zero many times <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Proving that all non-trivial zeros lie on this line would lead to a one million dollar prize from the Clay Math Institute and validate numerous modern mathematical results <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
<a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>

## The "Sum" of 1 + 2 + 3...

The statement that 1 + 2 + 3 + 4... equals -1/12 comes from the [[analytic_continuation | analytic continuation]] of the Riemann zeta function <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. The [[analytic_continuation | extended function]] maps the point -1 to -1/12 <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. While it may seem misleading to call this a "sum" since the definition of the zeta function for negative values is not directly from the divergent sum, the uniqueness of the [[analytic_continuation | analytic continuation]] suggests an intrinsic connection between these extended values and the original sum <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This "jigsaw puzzle" has only one solution <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.