---
title: Sum rule for derivatives
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

Understanding how to take [[calculating_derivatives_and_their_applications | derivatives]] of simple functions provides an intuitive foundation for understanding where their formulas originate <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, most real-world models involve functions that mix, combine, or tweak these simple functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The next step in [[understanding_derivatives_of_combined_functions | understanding derivatives of combined functions]] is to learn how to handle these more complex combinations, focusing on a clear conceptual picture rather than rote memorization <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

Functions can be combined in three fundamental ways:
1.  **Addition**: Adding functions together <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.
2.  **Multiplication**: Multiplying functions <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.
3.  **Composition**: Plugging one function inside another <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

Subtraction is considered a form of addition (multiplying by -1 and adding) <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, and division is a combination of composition (with 1/x) and multiplication <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Most complex functions are just layers of these three basic combinations <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. The key is to understand how derivatives interact with these three combination types, allowing for a step-by-step approach to even the most complex expressions <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

## The Sum Rule

The [[Sum rule for derivatives | sum rule for derivatives]] is the most straightforward of the combination rules <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>:

> The [[calculating_derivatives_and_their_applications | derivative]] of a sum of two functions is the sum of their [[calculating_derivatives_and_their_applications | derivatives]] <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

While simple to state, it's beneficial to think through its meaning to prepare for the more complex rules like the [[product_rule_in_calculus | product rule]] and [[chain_rule_in_differentiation | chain rule]] <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

### Visualizing the Sum Rule

Consider the function `f(x) = sin(x) + x^2` <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. For any input `x`, the value of `f(x)` is the sum of `sin(x)` and `x^2` at that point <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. Graphically, if you take the height of the sine graph and the height of the x-squared parabola at a given `x`, their sum is simply these two vertical bars stacked together <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

To find the [[calculating_derivatives_and_their_applications | derivative]], we consider what happens when the input `x` is nudged slightly, by a tiny amount `dx` (e.g., from `0.5` to `0.5 + dx`) <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. The resulting difference in the value of `f` is `df` <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

Visually, the total change in height (`df`) is the sum of the change in the sine graph's height (`d sin(x)`) and the change in the x-squared graph's height (`dx^2`) <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>:
`df = d sin(x) + dx^2` <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>

We know that:
*   The [[calculating_derivatives_and_their_applications | derivative]] of `sin(x)` is `cos(x)` <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. This means `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
*   The [[calculating_derivatives_and_their_applications | derivative]] of `x^2` (using the [[power_rule_for_derivatives | power rule]]) is `2x` <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. This means `dx^2` is approximately `2x * dx` <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

Substituting these into the equation for `df`:
`df = (cos(x) * dx) + (2x * dx)` <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>

Dividing both sides by `dx` to find the [[calculating_derivatives_and_their_applications | derivative]] `df/dx`:
`df/dx = cos(x) + 2x` <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>
This result shows that the [[calculating_derivatives_and_their_applications | derivative]] of `sin(x) + x^2` is indeed the sum of the [[calculating_derivatives_and_their_applications | derivatives]] of its parts <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

## Constant Multiple Rule

As a simpler case, if a function is multiplied by a constant (e.g., `2 * sin(x)`), the [[calculating_derivatives_and_their_applications | derivative]] is simply the constant multiplied by the [[calculating_derivatives_and_their_applications | derivative]] of the function (e.g., `2 * cos(x)`) <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## Conclusion

The [[Sum rule for derivatives | sum rule]], [[product_rule_in_calculus | product rule]], and [[chain_rule_in_differentiation | chain rule]] are the three fundamental tools for handling [[understanding_derivatives_of_combined_functions | derivatives of combined functions]] <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. While understanding these rules is important, fluency in applying them requires practice <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>. The goal is not merely to memorize formulas, but to grasp the natural patterns and derive them by patiently thinking through the fundamental meaning of a [[calculating_derivatives_and_their_applications | derivative]] <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.