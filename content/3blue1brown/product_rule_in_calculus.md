---
title: Product rule in calculus
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

The field of calculus often involves dealing with functions that are combinations or modifications of simpler functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. To understand how to take [[understanding_derivatives_of_combined_functions | derivatives]] of these more complex combinations, it's crucial to grasp the underlying [[intuition_behind_calculus_rules | intuition]] behind the rules, rather than just memorizing formulas <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Functions are typically combined in three fundamental ways:
*   Adding them together <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Multiplying them <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Composing them (throwing one inside the other) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

While subtraction is just multiplication by -1 and addition <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, and division involves composition and multiplication <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, mastering these three basic combination types allows one to systematically approach any complex expression <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## The Product Rule

Unlike the [[sum_rule_for_derivatives | sum rule]], which is straightforward <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, the derivative patterns for products and function composition are not as intuitive at first glance and require deeper thought <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Visualizing the Product Rule with Area

When dealing with the product of two functions, it's often helpful to visualize it as an area <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Consider a function `f(x)` defined as the product of two other functions, for example, `f(x) = sin(x) * x^2` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Imagine a rectangle where one side length is `sin(x)` and the other is `x^2` <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. These side lengths are adjustable, depending on the value of `x` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The area of this box represents `f(x)` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Deriving the Rule from Tiny Nudges

To find the derivative, `df`, we consider how a tiny change in `x`, denoted as `dx`, influences the area of this box <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
1.  A nudge `dx` causes the width (`sin(x)`) to change by `d sin(x)` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  The same nudge `dx` causes the height (`x^2`) to change by `d x^2` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

This results in three additional areas:
*   A thin rectangle on the bottom with area `sin(x) * d x^2` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   A thin rectangle on the right with area `x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   A small corner piece (which can be ignored because its area is proportional to `dx^2`, becoming negligible as `dx` approaches zero) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

The total change in area, `df`, is the sum of these two main rectangles:
`df = sin(x) * d x^2 + x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

We know that `d x^2` is approximately `2x * dx` (from the [[power_rule_for_derivatives | power rule]]) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, and `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Substituting these into the equation for `df`:
`df = sin(x) * (2x * dx) + x^2 * (cos(x) * dx)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

Dividing by `dx` to find the derivative `df/dx`:
`df/dx = sin(x) * 2x + x^2 * cos(x)` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This demonstrates that the derivative of the product of two functions `g(x)` and `h(x)` (like `sin(x)` and `x^2` in the example) follows a general pattern <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>:

> ### Product Rule
> The derivative of a product of two functions is the first function times the derivative of the second, plus the second function times the derivative of the first <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
>
> Or, symbolically:
> `d/dx [g(x) * h(x)] = g(x) * h'(x) + h(x) * g'(x)` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Mnemonic and Intuition

A common mnemonic to remember the product rule is "Left d right, right d left" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>:
*   "Left d right" refers to the left function (`sin(x)`) times the derivative of the right function (`2x`) <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This term represents the area of the little bottom rectangle <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   "Right d left" refers to the right function (`x^2`) times the derivative of the left function (`cos(x)`) <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This term represents the area of the rectangle on the side <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

Understanding this adjustable box visualization helps to see why these terms appear and how they represent the change in area, making the rule less strange than if it were merely a formula to memorize <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Constant Multiple Rule

A simpler case related to multiplication is when a function is multiplied by a constant, e.g., `2 * sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. The derivative is simply the constant multiplied by the derivative of the function, so `d/dx [2 * sin(x)] = 2 * cos(x)` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Conclusion

Along with the [[sum_rule_for_derivatives | sum rule]] and the [[chain_rule_in_differentiation | chain rule]], the product rule is one of the three basic tools for handling derivatives of combined functions <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While fluency in applying these rules comes from practice, understanding their derivation from first principles provides a deeper, more natural grasp of calculus <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.