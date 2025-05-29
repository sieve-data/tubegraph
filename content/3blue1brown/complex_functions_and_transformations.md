---
title: Complex functions and transformations
videoId: sD0NjbwqlYw
---

From: [[3blue1brown]] <br/> 

Complex functions, which take complex numbers as inputs and produce complex numbers as outputs, can be effectively understood through visualization as [[visualizing_linear_transformations | transformations]] <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. This approach involves imagining every possible input moving to its corresponding output <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

## Visualizing Transformations

To illustrate, consider the function *f*(*s*) = *s*² <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   An input of *s* = 2 yields 4, so the point at 2 moves to 4 <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   An input of *s* = -1 yields 1, moving the point at -1 to 1 <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   An input of *s* = *i* yields -1, moving the point at *i* to -1 <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

When visualized, applying *f*(*s*) = *s*² to an entire grid of complex numbers shows a dynamic [[animating_mathematical_functions | transformation]] <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>. This provides a rich picture of the function's behavior in two dimensions <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.

## The Riemann Zeta Function

The Riemann zeta function, often denoted ζ(*s*), is a significant object in modern mathematics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It is primarily known for the Riemann hypothesis, an unsolved problem regarding when the function equals zero, carrying a one-million-dollar prize <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Initial Definition and Convergence

The zeta function is initially defined as an infinite sum for a given input *s*:
ζ(*s*) = 1/1ˢ + 1/2ˢ + 1/3ˢ + 1/4ˢ + ... <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. This sum includes all natural numbers <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

For example, when *s* = 2, the sum is 1 + 1/4 + 1/9 + 1/16 + ..., which converges to π²/6 (approximately 1.645) <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. This sum converges to a specific number as long as the real part of *s* is greater than 1 <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. In this domain, the function is well-defined <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Complex Inputs

Mathematicians, notably Bernhard Riemann, focused on understanding the zeta function when *s* is a complex number <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. Raising a number to a complex power involves both scaling and rotation <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. Specifically, raising a base to a pure imaginary number results in a complex number on the unit circle <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. The further the base is from 1, the more quickly the output walks around the unit circle as the imaginary input changes <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

When a complex input like 2 + *i* is plugged into the zeta function, each term in the sum (e.g., 1/nˢ) gets rotated by some amount, but its length does not change <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. This means the sum still converges, typically in a spiral, to a specific point on the complex plane <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. This demonstrates that the zeta function is a reasonable complex function as long as the real part of the input is greater than 1 <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.

The [[visualizing_linear_transformations | visualization]] of the zeta function shows how points on the right half of the complex plane (where the real part of numbers is greater than 1) are transformed into corresponding outputs <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.

## Analytic Continuation

For inputs where the real part of *s* is less than or equal to 1, the original infinite sum definition of the zeta function breaks down, producing nonsensical results like 1 + 2 + 3 + ... = -1/12 <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>, <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. However, the transformed grid from the domain where the sum *does* make sense "begs" to be extended <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>, <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.

### The Property of "Analytic" Functions

This extension is achieved through a concept called **analytic continuation** <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>, which relies on the property of a function being "analytic" <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. A complex function is considered analytic if it has a derivative everywhere <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>. Geometrically, this means that the function preserves angles <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>. If any two lines in the input space intersect at a certain angle, they will still intersect at the same angle after the transformation, even if the lines themselves become curved <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. A simple way to observe this is that grid lines, which initially intersect at right angles, continue to intersect at right angles after the transformation <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.

This angle-preserving property is highly restrictive <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>. The surprising fact is that if an analytic function is extended beyond its original domain, and the new extended function is also required to be analytic, there is only *one possible* extension, if one exists at all <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>. This is akin to an infinite, continuous jigsaw puzzle where the angle-preserving requirement locks the extension into a unique solution <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.

### Defining the Full Riemann Zeta Function

The full Riemann zeta function is defined as follows <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>:
*   For values of *s* where the real part is greater than 1, it's defined by the converging infinite sum <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.
*   For the rest of the complex plane, it is defined as the unique analytic continuation of that sum <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>. This is a valid definition because there is only one possible analytic continuation <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## Zeros and the Riemann Hypothesis

The points where the Riemann zeta function equals zero are particularly important <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>.
*   **Trivial Zeros**: The negative even numbers (e.g., -2, -4, -6...) are mapped to zero <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. These are called "trivial" because mathematicians understand them well <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.
*   **Non-trivial Zeros**: The remaining zeros lie within a region called the **critical strip** <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. Their specific placement contains surprising information about prime numbers <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>.

**The Riemann Hypothesis** states that all non-trivial zeros lie on the **critical line**, which is the line of numbers *s* whose real part is exactly one half <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>. Proving this hypothesis would imply a remarkably tight grasp on the pattern of prime numbers and many other mathematical patterns <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>. [[visualizing_linear_transformations | Visualizing]] the critical line under the zeta function's transformation shows it passing through zero many times <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.

Another known property of this extended function is that it maps the point negative one (-1) to negative one twelfth (-1/12) <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>. While this seems to imply that 1 + 2 + 3 + 4 + ... equals -1/12, it's crucial to remember that this value comes from the analytic continuation, not the original diverging sum <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. However, the uniqueness of this analytic continuation suggests a deep connection between these extended values and the original sum <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.