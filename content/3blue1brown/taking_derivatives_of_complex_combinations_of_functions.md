---
title: Taking derivatives of complex combinations of functions
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

After understanding [[derivatives_of_simple_functions_and_their_intuition | derivatives of simple functions]] and the intuition behind their formulas <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, the next step in calculus is to understand how to take [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] of more complicated combinations of functions <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The aim is to have a clear mental picture of where these rules originate, rather than just memorizing formulas <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Most functions encountered in modeling the world involve mixing, combining, or tweaking these simple functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These combinations primarily boil down to three basic operations <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>:
1.  **Adding functions together** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  **Multiplying functions** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **[[understanding_the_chain_rule_for_function_composition_in_derivatives | Composing them]]** (throwing one inside the other) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Subtracting functions is essentially multiplying the second by negative one and adding <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, while dividing functions can be seen as plugging one into `1/x` and then multiplying <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Therefore, understanding how [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] interact with these three combination types allows for step-by-step simplification of any complex expression <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The Sum Rule

The sum rule is the most straightforward: the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of a sum of two functions is the sum of their [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

**Formula:**
If `f(x) = g(x) + h(x)`, then `d/dx [f(x)] = d/dx [g(x)] + d/dx [h(x)]` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

**Intuition (Example: `f(x) = sin(x) + x^2`)**
Consider `f(x) = sin(x) + x^2` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. For any input `x`, `f(x)` is the sum of `sin(x)` and `x^2` at that point <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
If you nudge the input `x` slightly by `dx` (e.g., from `0.5` to `0.5 + dx`), the total change in `f(x)` (called `df`) is the sum of the change in `sin(x)` (called `d sin(x)`) and the change in `x^2` (called `dx^2`) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Since the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of `sin(x)` is `cos(x)`, the change `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Since the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of `x^2` is `2x`, the change `dx^2` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]​.

Therefore, `df = (cos(x) * dx) + (2x * dx)` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
Dividing by `dx` gives `df/dx = cos(x) + 2x`, which is the sum of the [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] of its parts <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## The Product Rule

For products of functions, the pattern is not as straightforward as addition <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Visualizing the product as an area can be helpful <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

**Formula:**
If `f(x) = g(x) * h(x)`, then `d/dx [f(x)] = g(x) * d/dx [h(x)] + h(x) * d/dx [g(x)]` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. This is often remembered as "Left d right, right d left" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

**Intuition (Example: `f(x) = sin(x) * x^2`)**
Imagine `f(x)` as the area of a rectangle with side lengths `sin(x)` and `x^2` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. When `x` is nudged by `dx`, both side lengths change:
*   `sin(x)` changes by `d sin(x)` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   `x^2` changes by `dx^2` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

This results in three new snippets of area that contribute to `df` (the change in total area):
1.  A thin bottom rectangle with area `sin(x) * dx^2` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  A thin right rectangle with area `x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  A tiny corner piece with area `d sin(x) * dx^2` (which is negligible as `dx` approaches zero) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

So, `df = sin(x) * dx^2 + x^2 * d sin(x)` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
Substituting `dx^2 = 2x * dx` and `d sin(x) = cos(x) * dx` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>:
`df = sin(x) * (2x * dx) + x^2 * (cos(x) * dx)` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
Dividing by `dx`:
`df/dx = sin(x) * 2x + x^2 * cos(x)` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
This shows that the derivative of the product is the sum of the area of the bottom rectangle (`left d right`) and the area of the side rectangle (`right d left`) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Constant Multiple Rule

When a function is multiplied by a constant (e.g., `2 * sin(x)`), the derivative is simply the constant multiplied by the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of the function (e.g., `2 * cos(x)`) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## The Chain Rule

The [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]] is used when one function is "shoved inside" another, known as [[understanding_the_chain_rule_for_function_composition_in_derivatives | function composition]] <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

**Formula:**
If `f(x) = g(h(x))`, then `d/dx [f(x)] = g'(h(x)) * h'(x)` <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
This can also be written using Leibniz notation: `df/dx = dg/dh * dh/dx` <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

**Intuition (Example: `f(x) = sin(x^2)`)**
Visualize this using three number lines <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:
1.  **x-line:** Holds the value of `x`.
2.  **h-line:** Holds `h = x^2`. The function `x^2` maps from line 1 to line 2 <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
3.  **g-line:** Holds `g = sin(h)`. The function `sin` maps from line 2 to line 3 <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

When `x` is nudged by a small `dx` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>:
*   This causes a nudge `dh` on the `h`-line. We know `dh = (d/dx [x^2]) * dx = 2x * dx` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   This nudge `dh` then causes a nudge `dg` on the `g`-line (which is `d sin(h)`). We know `dg = (d/dh [sin(h)]) * dh = cos(h) * dh` <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

Now, substitute back:
1.  Replace `h` with `x^2`: `dg = cos(x^2) * dh` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
2.  Replace `dh` with `2x * dx`: `dg = cos(x^2) * (2x * dx)` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

To find `df/dx` (or `dg/dx`), divide both sides by `dx`:
`dg/dx = cos(x^2) * 2x` <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This pattern reveals:
*   The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of the "outside" function (`sin` in this case), still taking in the "inside" function (`x^2`) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   Multiplied by the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of that "inside" function (`2x` for `x^2`) <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

The symbolic cancellation of `dh` in `dg/dh * dh/dx` is a reflection of how tiny nudges propagate through a chain of functions <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Conclusion

The three fundamental tools for handling [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] of complex combinations are the sum rule, the product rule, and the [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]] <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While knowing these rules is important, fluency in [[calculating_derivatives_and_algebraic_simplification_in_calculus | applying them]] comes from practice and building the computational "muscles" <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Understanding the intuition behind these rules, by patiently thinking through what a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] means, makes them natural patterns rather than mere formulas to be memorized <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.