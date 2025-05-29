---
title: Applying the Product Rule in derivatives
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

When dealing with functions that combine simple forms, it becomes necessary to understand how to take [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivatives]] of these more [[taking_derivatives_of_complex_combinations_of_functions | complicated combinations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This requires going beyond memorization and developing a clear [[geometric_interpretation_of_derivatives | picture]] of where each rule originates <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

There are three fundamental ways to combine functions: adding them, multiplying them, or composing them (throwing one inside the other) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. While subtraction and division can be expressed using these three, understanding how [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivatives]] interact with these core combination types allows for step-by-step analysis of even the most complex expressions <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Understanding the Product Rule

Unlike the [[understanding_the_sum_rule_for_derivatives | sum rule]], where the derivative of a sum is simply the sum of the derivatives, the product rule is less straightforward <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. If you know the derivative of two functions, the question becomes: what is the derivative of their product <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>?

To [[geometric_interpretation_of_derivatives | visualize]] the product rule, it's often helpful to think of the product of two functions as an area <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Consider a mental setup of a box where its side lengths are determined by two functions, say `sine(x)` and `x²` <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. These side lengths are adjustable, dependent on the value of `x` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The function `f(x)` defined as the product of these two functions, `sine(x) * x²`, represents the area of this box <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Derivation of the Product Rule

To find the derivative of this product, we consider how a tiny change to `x` (denoted as `dx`) influences the total area `f(x)` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

When `x` is nudged by `dx`:
*   The width of the box (`sine(x)`) changes by a small amount, `d sine(x)` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   The height of the box (`x²`) changes by a small amount, `dx²` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

This results in three additional snippets of new area <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  **Bottom Rectangle**: A thin rectangle on the bottom with an area equal to its width (`sine(x)`) times its thin height (`dx²`) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  **Right Rectangle**: A thin rectangle on the right with an area equal to its height (`x²`) times its thin width (`d sine(x)`) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  **Corner Piece**: A tiny bit in the corner whose area is proportional to `dx²` and becomes negligible as `dx` approaches zero <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

We know that `d sine(x)` is approximately `cosine(x) * dx`, and `dx²` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
So, the total change in area `df` is approximately:
`df = sine(x) * (2x * dx) + x² * (cosine(x) * dx)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>

Dividing by `dx` to find the derivative `df/dx`:
`df/dx = sine(x) * (2x) + x² * (cosine(x))` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>

This can be generalized for any two functions `g(x)` and `h(x)` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>:
`d/dx [g(x) * h(x)] = g(x) * h'(x) + h(x) * g'(x)`

### Mnemonic for the Product Rule

A common mnemonic to remember the product rule is "Left d right, right d left" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>:
*   **"Left d right"**: Take the left function (`g(x)`) and multiply it by the derivative of the right function (`h'(x)`) <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. In our example (`sine(x) * x²`), this is `sine(x) * 2x` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This term represents the area of the little bottom rectangle in the [[geometric_interpretation_of_derivatives | visualization]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **"Right d left"**: Add the right function (`h(x)`) multiplied by the derivative of the left function (`g'(x)`) <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. In our example, this is `x² * cosine(x)` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. This term represents the area of the rectangle on the side <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

While this mnemonic is helpful for recall, understanding the [[geometric_interpretation_of_derivatives | adjustable box visualization]] provides insight into what each term genuinely represents <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Constant Multipliers

It's worth noting that if you multiply a function by a constant (e.g., `2 * sine(x)`), the derivative is much simpler: the constant simply multiplies the derivative of the function <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. For `2 * sine(x)`, the derivative is `2 * cosine(x)` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Conclusion

The product rule, along with the [[understanding_the_sum_rule_for_derivatives | sum rule]] and [[understanding_the_chain_rule_for_function_composition_in_derivatives | chain rule]], forms the fundamental toolkit for handling [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivatives]] of [[taking_derivatives_of_complex_combinations_of_functions | combined functions]] <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While understanding these rules conceptually is crucial, fluency in [[calculating_derivatives_and_algebraic_simplification_in_calculus | applying them]] comes from consistent practice <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. These rules are not merely formulas to memorize, but natural patterns that can be discovered by patiently considering the fundamental meaning of a derivative <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.