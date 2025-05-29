---
title: Understanding derivatives of combined functions
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

When modeling the world, functions often involve mixing, combining, or tweaking simpler functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. To understand how to [[calculating_derivatives_and_their_applications | take derivatives]] of these more complicated combinations, it's crucial to have a clear mental picture of where the rules come from, rather than just memorizing formulas <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Basic Combination Types

Most functions encountered in calculus involve layering together three fundamental types of combinations <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:
1.  **Addition**: Adding functions together <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  **Multiplication**: Multiplying functions <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Composition**: Throwing one function inside another <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Subtraction is effectively multiplication by negative one and then addition <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, and division is composition with the function `1/x` followed by multiplication <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Understanding how [[integrals_and_derivatives | derivatives]] interact with these three basic types allows for step-by-step differentiation of any complex expression <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The Sum Rule

The sum rule states that the [[integrals_and_derivatives | derivative of a sum]] of two functions is the sum of their derivatives <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Visualizing the Sum Rule
Consider the function `f(x) = sin(x) + x^2` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. For any input `x`, the value of `f(x)` is the sum of `sin(x)` and `x^2` at that point <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Visually, if `sin(x)` and `x^2` are represented by vertical bars, `f(x)` is the length obtained by stacking them <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

To find the derivative, consider what happens when the input `x` is nudged slightly to `x + dx` <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The change in the value of `f` (denoted as `df`) is the total change in height <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This total change is the sum of the change in `sin(x)` (called `d sin(x)`) and the change in `x^2` (called `dx^2`) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

We know that the [[computing_derivatives_of_functions | derivative of sine]] is cosine, meaning `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Similarly, because the [[power_rule_for_derivatives | derivative of x squared]] is `2x`, the change `dx^2` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Therefore, `df = cos(x) * dx + 2x * dx` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Dividing by `dx` gives the derivative `df/dx = cos(x) + 2x`, which is indeed the [[integrals_and_derivatives | sum of the derivatives]] of its parts <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## The Product Rule

Unlike the sum rule, the product rule is less straightforward <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. When dealing with a product of two things, it often helps to understand it as an area <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Visualizing the Product Rule
Consider `f(x) = sin(x) * x^2`, which can be visualized as the area of an adjustable box where one side length is `sin(x)` and the other is `x^2` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Both side lengths change as `x` is adjusted <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

When `x` is nudged by a tiny `dx`, the width changes by `d sin(x)` and the height changes by `dx^2` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This creates three snippets of new area <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  **Bottom thin rectangle**: Area is `sin(x) * dx^2` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  **Right thin rectangle**: Area is `x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  **Corner piece**: Its area is proportional to `dx^2` and becomes negligible as `dx` approaches zero <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Using the known derivatives: `dx^2` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, and `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
So, the total change in area `df` is approximately `sin(x) * (2x * dx) + x^2 * (cos(x) * dx)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
Dividing by `dx` gives the product rule for `f(x) = sin(x) * x^2`:
`df/dx = sin(x) * (derivative of x^2) + x^2 * (derivative of sin(x))` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This reasoning applies to any two functions, `g` and `h` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The derivative of their product `g(x) * h(x)` is:
`g(x) * h'(x) + h(x) * g'(x)` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
This is often remembered by the mnemonic "Left d right, right d left" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>: take the left function times the derivative of the right, plus the right function times the derivative of the left <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Each term visually represents one of the thin rectangular areas <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

*Note*: If a function is multiplied by a constant, e.g., `2 * sin(x)`, the derivative is simply the constant multiplied by the derivative of the function, `2 * cos(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## The Chain Rule (Function Composition)

Function composition, where one function is "shoved inside" another, is a very common way to combine functions <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. For example, `sin(x^2)` is `x^2` shoved inside `sin(x)` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Visualizing the Chain Rule
To understand the derivative of `sin(x^2)`, visualize three number lines <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:
1.  **x-line**: Holds the value of `x`.
2.  **x²-line**: Holds the value of `x^2` (or `h`).
3.  **sin(x²)-line**: Holds the value of `sin(x^2)` (or `sin(h)`).

The function `x^2` maps from line 1 to line 2, and the function `sin` maps from line 2 to line 3 <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

When `x` is nudged by a tiny `dx` on the first line, this causes a nudge `dx^2` (or `dh`) on the second line <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. This `dh` then causes a nudge `d sin(h)` on the third line <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

Using what we know:
*   The nudge `dh` is about `2x * dx` (since `h = x^2`, its derivative is `2x`) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   The nudge `d sin(h)` is about `cos(h) * dh` (since the [[computing_derivatives_of_functions | derivative of sine]] is cosine) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Substitute `h` back with `x^2`: `d sin(x^2) = cos(x^2) * dx^2` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
Then, substitute `dx^2` with `2x * dx`: `d sin(x^2) = cos(x^2) * (2x * dx)` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
Dividing by `dx`, the derivative `df/dx` is `cos(x^2) * 2x` <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This demonstrates the [[calculating_derivatives_and_their_applications | chain rule]] <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. For any two functions `g(x)` and `h(x)`, the derivative of their composition `g(h(x))` is:
`g'(h(x)) * h'(x)` <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
Symbolically, this is often written as `dg/dh * dh/dx` <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. The "cancellation" of `dh` reflects how the tiny changes propagate through the chain of functions <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Conclusion

The three fundamental tools for handling [[computing_derivatives_of_functions | derivatives of functions]] that combine smaller things are the sum rule, the product rule, and the chain rule <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While understanding these rules is important, fluency comes from practice and building the "muscles" to perform these computations <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. The goal is to see these rules not as formulas to memorize, but as natural patterns that emerge from patiently considering what a [[visualizing_derivatives_using_graphs | derivative]] truly means <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.