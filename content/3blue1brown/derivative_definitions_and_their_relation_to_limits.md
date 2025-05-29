---
title: Derivative definitions and their relation to limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of [[limits_in_calculus | limits]] is fundamental to understanding [[understanding_what_a_derivative_is | derivatives]] in calculus, serving as a bridge before delving into [[antiderivatives_and_their_role_in_integration | integrals]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Fundamentally, the idea of a limit is intuitive: it's about one value getting closer to another <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This concept allows for assigning formal notation to this intuitive idea <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Formal Definition of a Derivative

The way [[calculating_derivatives_and_their_applications | derivatives]] are typically described, using "concrete non-zero nudges" like `dx` and `df`, aligns with their formal definition, providing confidence that this intuitive approach is backed by rigor <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

To understand a function `f(x)`'s [[calculating_derivatives_and_their_applications | derivative]] at a specific input (e.g., `x = 2`), one imagines a small "nudge" `dx` to the input, observing the resulting change `df` in the output <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The [[calculating_derivatives_and_their_applications | ratio `df` divided by `dx`]] represents the rise-over-run slope between the initial and nudged points on the graph <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The actual [[calculating_derivatives_and_their_applications | derivative]] is defined as whatever this ratio [[limits_in_calculus | approaches]] as `dx` [[limits_in_calculus | approaches]] 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. The change in output `df` is precisely `f(starting input + dx) - f(starting input)` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

To express this rigorously, the `lim` notation is used, with `dx → 0` (or `h → 0` or `Δx → 0`) indicating that `dx` [[limits_in_calculus | approaches]] zero <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:

```
lim (dx→0) [f(x + dx) - f(x)] / dx
```
Variables like `dx` in typical [[calculating_derivatives_and_their_applications | derivative]] expressions implicitly contain the idea of a [[limits_in_calculus | limit]] where `dx` eventually goes to zero <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The expression `df/dx` can be seen as shorthand for this more detailed [[calculating_derivatives_and_their_applications | formal definition of a derivative]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

It's important to note that the [[calculating_derivatives_and_their_applications | formal definition of a derivative]] avoids the [[paradoxes_in_the_concept_of_derivatives | paradoxical idea of an infinitely small change]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The [[limits_in_calculus | point of limits]] is specifically to bypass such concepts <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The variable `h` (or `dx`) represents a [[calculating_derivatives_and_their_applications | concrete, finitely small nudge]], and the analysis focuses on what happens as this `h` becomes arbitrarily small <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Interpreting `dx` as a [[calculating_derivatives_and_their_applications | concrete, finitely small nudge]] helps build stronger intuition for the [[understanding_what_a_derivative_is | rules of calculus]] <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Understanding What "Approach" Means in Limits

The primary function of [[limits_in_calculus | limits]] is to avoid the notion of infinitely small changes by instead examining what happens as the size of a small change [[limits_in_calculus | approaches]] 0 <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This leads to a deeper understanding of what it means for one value to "approach" another <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Consider the function `(2 + h)^3 - 2^3` all divided by `h` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This expression, while deriving from a [[calculating_derivatives_and_their_applications | derivative]] of `x^3` at `x=2`, can be viewed as any function of `h` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. At `h = 0`, the function is undefined (0/0) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, creating a "hole" in its graph <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. However, as `h` [[limits_in_calculus | approaches]] 0, the output of the function [[limits_in_calculus | approaches]] 12 from either side <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### The Epsilon-Delta Definition of Limits

To define "approach" unambiguously, mathematicians use the [[limits_in_calculus | epsilon-delta definition of limits]] <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This definition provides rigor to the intuitive idea that a limit exists if, for any desired closeness to the output limit (`epsilon`), one can find a corresponding closeness to the input limit (`delta`) such that all inputs within `delta` (excluding the limit point itself) yield outputs within `epsilon` of the limit <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

*   **When a limit exists**: The output range can be made as small as desired (`epsilon`) <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   **When a limit does not exist**: For a sufficiently small `epsilon`, the output range cannot shrink smaller than a particular value, regardless of how tiny the input range (`delta`) becomes <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. For example, a function that jumps at `h=0` (approaching 2 from the right, 1 from the left) has no defined limit at `h=0` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## L'Hôpital's Rule: Computing Limits with Derivatives

After [[limits_in_calculus | limits]] help define [[understanding_what_a_derivative_is | derivatives]], [[understanding_what_a_derivative_is | derivatives]] can, in turn, help evaluate [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This is particularly useful for expressions that result in the indeterminate form `0/0` when a value is plugged in <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

Consider the limit of `sin(πx) / (x^2 - 1)` as `x` [[limits_in_calculus | approaches]] 1 <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. Plugging in `x=1` yields `sin(π)/0 = 0/0`, meaning the function is undefined at this point <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

To find this limit, one can zoom in around `x=1` and consider a tiny nudge `dx` away from it <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>:
1.  **Numerator change**: `sin(πx)` changes by `d(sin(πx))`, which is approximately `cos(πx) * π * dx` (using the chain rule) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. At `x=1`, this is `cos(π) * π * dx = -π * dx` <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
2.  **Denominator change**: `x^2 - 1` changes by `d(x^2 - 1)`, which is approximately `2x * dx` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. At `x=1`, this is `2 * 1 * dx = 2 * dx` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

The ratio `sin(πx) / (x^2 - 1)` near `x=1` is approximately `(-π * dx) / (2 * dx)` <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. The `dx` terms cancel, leaving `-π/2` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. As `dx` becomes infinitesimally small, this approximation becomes exact, meaning the precise [[limits_in_calculus | limiting]] value is `-π/2` <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

This [[limits_in_calculus | clever trick]] is known as [[limits_in_calculus | L'Hôpital's Rule]] <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. It states that if you have a limit of `f(x)/g(x)` as `x` [[limits_in_calculus | approaches]] `a`, and both `f(a)` and `g(a)` are 0 (or infinity), then the limit is equal to the limit of `f'(x)/g'(x)` as `x` [[limits_in_calculus | approaches]] `a` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. It's a powerful tool for evaluating limits that result in indeterminate forms <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

However, [[limits_in_calculus | L'Hôpital's Rule]] cannot be used to discover new [[understanding_what_a_derivative_is | derivative]] formulas because it requires knowing the [[understanding_what_a_derivative_is | derivatives]] of the numerator and denominator already <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. The process of discovering [[understanding_what_a_derivative_is | derivative]] formulas often requires creativity rather than a systematic method <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

## Looking Ahead

The next topic in the series will be [[antiderivatives_and_their_role_in_integration | integrals]] and the [[relationship_between_integrals_and_derivatives | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>, further demonstrating how [[limits_in_calculus | limits]] provide a clear meaning to concepts that involve notions of infinity <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.