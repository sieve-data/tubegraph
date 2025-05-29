---
title: Derivatives of simple functions and their intuition
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

Previous discussions have focused on the [[geometric_interpretation_of_derivatives | geometric interpretation of derivatives]] and intuition behind the [[derivatives_of_exponential_functions | derivatives of simple functions]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The goal is to provide a clear picture for where derivative formulas originate, rather than just memorizing them <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. When modeling the world, functions are often mixed, combined, or tweaked <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Therefore, the next step is to understand how to take [[taking_derivatives_of_complex_combinations_of_functions | derivatives of more complicated combinations]] of functions <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Basic Ways to Combine Functions

There are three fundamental ways to combine functions <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>:
1.  **Addition**: Adding functions together <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Subtraction is essentially adding a function multiplied by -1 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
2.  **Multiplication**: Multiplying functions <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Division can be seen as composing one function with `1/x` and then multiplying <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
3.  **Composition**: Plugging one function inside another <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Most complex functions are built by layering these three combination types <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Knowing how [[derivatives_and_integrals | derivatives]] interact with these three forms allows for step-by-step differentiation of any complex expression <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The core questions are: if you know the derivative of two functions, what is the derivative of their sum, product, and composition <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>?

## The Sum Rule

The sum rule states that the derivative of a sum of two functions is the sum of their [[derivatives_and_integrals | derivatives]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Intuition through Tiny Nudges

Consider a function `f(x) = sin(x) + x²` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This function adds the values of `sin(x)` and `x²` at every input <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

If `x` is nudged slightly to `x + dx`, the total change in `f(x)` (called `df`) is the sum of the change in `sin(x)` (called `d sin(x)`) and the change in `x²` (called `d x²`) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The change `d sin(x)` is approximately `cos(x) * dx`, because the [[derivatives_of_trigonometric_and_exponential_functions | derivative of sine is cosine]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   The change `d x²` is approximately `2x * dx`, because the [[derivative_of_polynomial_functions_using_geometric_visualization | derivative of x² is 2x]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Thus, `df = (cos(x) * dx) + (2x * dx)`. Dividing by `dx`, the derivative `df/dx` is `cos(x) + 2x`, which is the sum of the [[derivatives_and_integrals | derivatives]] of its parts <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## The Product Rule

The derivative of a product of functions is more complex than a simple sum of [[derivatives_and_integrals | derivatives]] <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Intuition through Area Visualization

For a product of two things, it often helps to visualize it as an area <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Consider `f(x) = sin(x) * x²`, represented as the area of a box with side lengths `sin(x)` and `x²` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. These side lengths are adjustable based on `x` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

When `x` is nudged by a tiny `dx`, the width `sin(x)` changes by `d sin(x)`, and the height `x²` changes by `d x²` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This change creates three new snippets of area around the original box <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  A thin rectangle on the bottom: `width * thin_height = sin(x) * d x²` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  A thin rectangle on the right: `height * thin_width = x² * d sin(x)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  A small corner piece: `d sin(x) * d x²`. This piece is proportional to `dx²` and becomes negligible as `dx` approaches zero <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

The total change in area `df` is approximately `sin(x) * d x² + x² * d sin(x)`.
Substituting `d x² = 2x * dx` and `d sin(x) = cos(x) * dx` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, and dividing by `dx`:
`df/dx = sin(x) * (2x) + x² * (cos(x))` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

This leads to the **Product Rule**: If `f(x) = g(x) * h(x)`, then `f'(x) = g(x) * h'(x) + h(x) * g'(x)` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. A common mnemonic is "Left d right, right d left" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Each term visually corresponds to the area of one of the thin rectangles <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

*Note*: If a function is multiplied by a constant, like `2 * sin(x)`, the derivative is simply the constant multiplied by the derivative of the function (e.g., `2 * cos(x)`) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## The Chain Rule (Function Composition)

Function composition involves nesting one function inside another, e.g., `sin(x²)`, where `x²` is "shoved inside" `sin(x)` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Intuition through Number Lines

Visualize the process with three number lines <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>:
1.  **x**: The input value.
2.  **h = x²**: The intermediate value derived from `x`.
3.  **g(h) = sin(h)**: The final output value, `sin(x²)`.

If `x` is nudged by a tiny `dx` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>:
*   This causes a change in `h` (i.e., `x²`), denoted `dh` (or `d x²`) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. We know `dh ≈ 2x * dx` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   This change in `h` then causes a change in the final output `g(h)` (i.e., `sin(h)`), denoted `dg` (or `d sin(h)`) <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. We know `dg ≈ cos(h) * dh` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Substituting `h = x²` back into the expression for `dg`:
`dg ≈ cos(x²) * dx²` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
Then, substitute `dx² = 2x * dx`:
`dg ≈ cos(x²) * (2x * dx)` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

To find the derivative `dg/dx`, we divide by `dx`:
`dg/dx = cos(x²) * 2x` <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This pattern demonstrates the **Chain Rule**: If `f(x) = g(h(x))`, then `f'(x) = g'(h(x)) * h'(x)` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
Symbolically, this is often written as `df/dx = (dg/dh) * (dh/dx)` <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. The `dh` terms appear to cancel, which is a genuine reflection of how the tiny nudges propagate through the chain of functions <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. The derivative of the outer function `g` is taken with respect to the intermediate variable `h`, and then multiplied by the derivative of the inner function `h` with respect to `x` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## Conclusion

The sum rule, product rule, and chain rule are the three fundamental tools for handling [[derivatives_and_integrals | derivatives]] of combined functions <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While understanding these rules is important, fluency in applying them requires practice <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The true value lies not just in memorizing the formulas, but in understanding the natural patterns and how they arise from the fundamental concept of tiny nudges in [[introduction_to_derivatives_and_calculus_concepts | calculus]] <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.