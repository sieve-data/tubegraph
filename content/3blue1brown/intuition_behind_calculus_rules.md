---
title: Intuition behind calculus rules
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

Understanding calculus rules goes beyond mere memorization; the goal is to develop a clear picture or [[mathematical_intuition_and_counterintuitive_results | intuition]] that explains their origins <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This article explores the intuitive basis for the fundamental rules of differentiation: the sum rule, product rule, and chain rule <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Basic Function Combinations

Most functions encountered in modeling involve mixing, combining, or tweaking simpler functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These combinations primarily boil down to three basic operations <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>:
1.  **Addition**: Adding functions together <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  **Multiplication**: Multiplying functions <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Composition**: Plugging one function inside another <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Other operations like subtraction and division can be reduced to these three basic forms <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   Subtracting functions is equivalent to multiplying the second by -1 and adding them <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Dividing functions is the same as composing one function with `1/x` and then multiplying the two functions <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Understanding how derivatives interact with these three combination types allows one to systematically approach the derivative of any complex expression <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The [[sum_rule_for_derivatives | Sum Rule]]

The [[sum_rule_for_derivatives | sum rule]] states that the derivative of a sum of two functions is the sum of their derivatives <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Intuition
Consider a function `f(x) = sin(x) + x^2` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. For any input `x`, the value of `f(x)` is the sum of `sin(x)` and `x^2` at that point <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Visually, if `sin(x)` and `x^2` represent heights, their sum `f(x)` is obtained by stacking these heights <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

When the input `x` is nudged slightly to `x + dx`, the total change in `f(x)` (denoted `df`) is simply the sum of the change in `sin(x)` (d `sin(x)`) and the change in `x^2` (d `x^2`) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   The change d `sin(x)` is approximately `cos(x) * dx` (since the derivative of sine is cosine) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   The change d `x^2` is approximately `2x * dx` (since the derivative of `x^2` is `2x`) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Therefore, `df = (cos(x) * dx) + (2x * dx)` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Dividing by `dx` gives the derivative `df/dx = cos(x) + 2x`, which is the sum of the individual derivatives <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## The [[product_rule_in_calculus | Product Rule]]

The [[product_rule_in_calculus | product rule]] is less straightforward than the sum rule <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Intuition
To understand the derivative of a product, such as `f(x) = sin(x) * x^2`, it's helpful to visualize it as an area <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Imagine a rectangle where one side length is `sin(x)` and the other is `x^2` <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. The area of this rectangle is `f(x)` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

When the input `x` changes by a tiny `dx`, both `sin(x)` and `x^2` change:
*   The width (`sin(x)`) changes by d `sin(x)` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   The height (`x^2`) changes by d `x^2` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

This change results in three small snippets of new area <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  **Bottom rectangle**: Width `sin(x)` multiplied by the thin height d `x^2` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  **Right rectangle**: Height `x^2` multiplied by the thin width d `sin(x)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  **Corner square**: Area is `d sin(x) * d x^2`. This term becomes negligible as `dx` approaches zero (it's proportional to `dx^2`) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

So, the total change in area `df` is approximately `sin(x) * d x^2 + x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
Substituting the derivatives:
*   `d x^2` is `2x * dx` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   `d sin(x)` is `cos(x) * dx` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

Thus, `df = sin(x) * (2x * dx) + x^2 * (cos(x) * dx)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Dividing by `dx` yields the [[product_rule_in_calculus | product rule]]:
`df/dx = sin(x) * (2x) + x^2 * (cos(x))` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This pattern, often remembered as "left d right, right d left" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, applies to any two functions `g(x)` and `h(x)`: `(gh)' = g'h + gh'` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Each term in the rule corresponds to the area of one of the thin rectangles <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

> For multiplication by a constant, like `2 * sin(x)`, the derivative is simply the constant multiplied by the derivative of the function (e.g., `2 * cos(x)`) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## The Chain Rule

Function composition involves nesting one function inside another, such as `f(x) = sin(x^2)` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Intuition
Visualize the process using three number lines <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>:
1.  **Top line**: Represents the input `x` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
2.  **Middle line**: Represents the inner function's output, `x^2` (let's call this `h`) <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
3.  **Bottom line**: Represents the final output, `sin(x^2)` (or `sin(h)`) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

A change in `x` by `dx` causes a change in `h` (i.e., `x^2`) by `dh` (or `dx^2`) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This `dh` then causes a change in `sin(h)` by `d sin(h)` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

*   The change `dh` is approximately `(derivative of x^2) * dx = 2x * dx` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   The change `d sin(h)` is approximately `(derivative of sin(h) with respect to h) * dh = cos(h) * dh` <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

Substituting `h` with `x^2`: `d sin(x^2)` is approximately `cos(x^2) * dx^2` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
Further substituting `dx^2` with `2x * dx`: `d sin(x^2)` is approximately `cos(x^2) * (2x * dx)` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

To find the derivative `df/dx`, we divide `d sin(x^2)` by `dx`:
`df/dx = cos(x^2) * 2x` <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This pattern is the chain rule: for a composition `g(h(x))`, its derivative is `g'(h(x)) * h'(x)` <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
Expressed in Leibniz notation, `dg/dx = (dg/dh) * (dh/dx)` <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. This form highlights the "cancellation" of `dh`, which is not just a notational trick but reflects how tiny changes propagate through the chain of functions <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Conclusion

The [[sum_rule_for_derivatives | sum rule]], [[product_rule_in_calculus | product rule]], and chain rule are the core tools for differentiating combined functions <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Understanding the intuitive origins of these rules—whether through adding changes, visualizing areas, or tracing cascades of nudges—transforms them from memorized formulas into natural patterns <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. While conceptual understanding is crucial, practical application and practice are essential for fluency in calculus computations <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.