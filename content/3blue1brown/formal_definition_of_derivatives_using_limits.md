---
title: Formal definition of derivatives using limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The idea of a [[introduction_to_derivatives_and_calculus_concepts | derivative]] has been discussed previously <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. To understand its formal definition, it's necessary to first understand the concept of a [[introduction_to_limits_in_calculus | limit]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. While the intuitive understanding of a [[introduction_to_limits_in_calculus | limit]] is simply one value getting closer to another <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, its formal application is crucial for the rigorous definition of a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Defining the Derivative Formally

When considering the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of a function `f(x)` at a specific input, such as `x = 2`, the process involves:
1.  Imagining a small "nudge" to the input, denoted as `dx` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Observing the resulting change in the output, `df` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  Forming the ratio `df/dx`, which represents the "rise over run" slope between the starting point and the nudged point on the graph <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The actual [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is what this ratio `df/dx` [[applications_and_interpretations_of_limits_in_calculus | approaches]] as `dx` [[applications_and_interpretations_of_limits_in_calculus | approaches]] 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

The change in output `df` is the difference between `f(x + dx)` and `f(x)` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. To express that this ratio [[applications_and_interpretations_of_limits_in_calculus | approaches]] a value as `dx` [[applications_and_interpretations_of_limits_in_calculus | approaches]] 0, the notation `lim` (for limit) is used, with `dx → 0` written below it <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The formal definition commonly uses `h` (or `Δx`) instead of `dx` for the small change in input. This is to clarify that `h` is an ordinary, non-zero number, rather than an "infinitesimal" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The terms like `dx` in typical [[understanding_the_meaning_and_computation_of_derivatives | derivative]] expressions inherently contain the idea of a [[introduction_to_limits_in_calculus | limit]], implying `dx` is meant to eventually go to 0 <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

Thus, the common shorthand `df/dx` is formally spelled out as:

```
df/dx = lim (as h approaches 0) [f(x + h) - f(x)] / h
```
This expression is the formal definition of a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] found in most calculus textbooks <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Avoiding Infinitely Small Changes
The purpose of [[introduction_to_limits_in_calculus | limits]] in this context is to avoid the concept of "infinitely small changes" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Instead, it analyzes what happens as the size of a small, finite change [[applications_and_interpretations_of_limits_in_calculus | approaches]] 0 <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. The `dx` (or `h`) is considered a concrete, finitely small nudge, and the definition asks what happens as that nudge [[applications_and_interpretations_of_limits_in_calculus | approaches]] 0 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This approach provides stronger intuition for the rules of calculus <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## How Derivatives Aid in Computing Limits

The definition of a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] itself relies on computing a [[introduction_to_limits_in_calculus | limit]] that often takes the form of `0/0` <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. Paradoxically, once [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] are defined using [[introduction_to_limits_in_calculus | limits]], they can then be used to evaluate other [[introduction_to_limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

For a function that results in an indeterminate form (like `0/0`) when a value is plugged in, [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] can help find the true [[introduction_to_limits_in_calculus | limit]] at that point <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### L'Hopital's Rule
When evaluating the [[introduction_to_limits_in_calculus | limit]] of a ratio of two functions, `f(x)/g(x)`, where both `f(a)` and `g(a)` equal 0 at a particular value `x = a` <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>, [[derivatives_of_simple_functions_and_their_intuition | L'Hopital's Rule]] can be applied <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

For `x` values infinitesimally close to `a` (i.e., `x = a + dx`), the value of `f(x)` is approximately its [[understanding_the_meaning_and_computation_of_derivatives | derivative]] `f'(a)` multiplied by `dx`. Similarly, `g(x)` is approximately `g'(a)` multiplied by `dx` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

Thus, the ratio `f(x)/g(x)` near `x = a` is approximately:

```
[f'(a) * dx] / [g'(a) * dx]
```
The `dx` terms cancel out, leaving `f'(a) / g'(a)` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. As `dx` [[applications_and_interpretations_of_limits_in_calculus | approaches]] 0, these approximations become more accurate, meaning the [[introduction_to_limits_in_calculus | limit]] of `f(x)/g(x)` as `x` [[applications_and_interpretations_of_limits_in_calculus | approaches]] `a` is precisely the ratio of their [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] at `a` <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

This rule states: If `lim (x→a) f(x) = 0` and `lim (x→a) g(x) = 0` (or if both [[applications_and_interpretations_of_limits_in_calculus | approach]] infinity), then:

```
lim (x→a) [f(x) / g(x)] = lim (x→a) [f'(x) / g'(x)]
```
This powerful tool allows for the computation of many [[introduction_to_limits_in_calculus | limits]] that initially appear undefined <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. However, it cannot be used to discover new [[understanding_the_meaning_and_computation_of_derivatives | derivative]] formulas, as that would be circular reasoning <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

### Next Steps in Calculus
Following the discussion of [[introduction_to_limits_in_calculus | limits]] and [[understanding_the_meaning_and_computation_of_derivatives | derivatives]], the next topic is [[derivatives_and_integrals | integrals]] and the [[relationship_between_integrals_and_derivatives | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. This further demonstrates how [[introduction_to_limits_in_calculus | limits]] provide a clear meaning to concepts that involve notions of infinity <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.