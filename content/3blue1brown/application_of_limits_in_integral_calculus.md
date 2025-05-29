---
title: Application of limits in integral calculus
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a [[limits_in_calculus | limit]] is fundamental to understanding calculus, acting as a bridge between intuitive ideas and rigorous mathematical definitions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Essentially, a [[limits_in_calculus | limit]] describes a value that one quantity "approaches" as another quantity gets closer to a specific point <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While the intuitive idea of approaching a value is straightforward, [[limits_in_calculus | limits]] provide a precise way to express this concept <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## [[derivative_definitions_and_their_relation_to_limits | Limits and Derivative Definitions]]

The [[derivative_definitions_and_their_relation_to_limits | derivative]] of a function, which describes its instantaneous rate of change, is formally defined using [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. For a function `f(x)`, its [[derivative_definitions_and_their_relation_to_limits | derivative]] at a given input `x` (e.g., `x = 2`) is found by:
1.  Imagining a small "nudge" `dx` to the input <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Observing the resulting change in the output, `df` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  Considering the ratio `df / dx`, which represents the slope between the original point and the nudged point on the graph <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The actual [[derivative_definitions_and_their_relation_to_limits | derivative]] is defined as whatever this ratio approaches as `dx` approaches 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This is formally written using [[limits_in_calculus | limit]] notation:

```
lim (as dx -> 0) [ (f(x + dx) - f(x)) / dx ]
```
In standard notation, `dx` is often replaced with `Δx` or `h` to explicitly show that it's a non-zero, finitely small nudge that is *approaching* zero, rather than being infinitely small from the outset <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This approach avoids the paradoxical idea of "infinitely small changes" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The use of [[limits_in_calculus | limits]] provides a rigorous definition of the [[derivative_definitions_and_their_relation_to_limits | derivative]], ensuring that concepts like `dx` are understood as concrete, finitely small nudges that are analyzed as they approach zero <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a> <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### The Epsilon-Delta Definition

For mathematicians, defining "approach" rigorously leads to the epsilon-delta definition of [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This definition states that for a [[limits_in_calculus | limit]] to exist, for any arbitrarily small positive distance `epsilon` (representing the desired closeness to the output [[limits_in_calculus | limit]]), there must exist a corresponding positive distance `delta` (representing the range of inputs around the limiting point) such that any input within `delta` of the limiting input corresponds to an output within `epsilon` of the output [[limits_in_calculus | limit]] <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a> <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. If no such `epsilon` can be found, the [[limits_in_calculus | limit]] does not exist <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a> <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]]

[[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] is a powerful technique for computing [[limits_in_calculus | limits]], especially when direct substitution results in an indeterminate form like 0/0 <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

If `lim (x -> a) f(x) = 0` and `lim (x -> a) g(x) = 0`, then [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] states:

```
lim (x -> a) [ f(x) / g(x) ] = lim (x -> a) [ f'(x) / g'(x) ]
```
where `f'(x)` and `g'(x)` are the [[derivative_definitions_and_their_relation_to_limits | derivatives]] of `f(x)` and `g(x)`, respectively <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

### Example:
Consider the [[limits_in_calculus | limit]]:
`lim (x -> 1) [ sin(πx) / (x² - 1) ]` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

Plugging in `x = 1` yields `sin(π) / (1² - 1) = 0 / 0`, an indeterminate form <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
Applying [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]]:
1.  Find the [[derivative_definitions_and_their_relation_to_limits | derivative]] of the numerator, `f(x) = sin(πx)`: `f'(x) = π cos(πx)` <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
2.  Find the [[derivative_definitions_and_their_relation_to_limits | derivative]] of the denominator, `g(x) = x² - 1`: `g'(x) = 2x` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
3.  Compute the [[limits_in_calculus | limit]] of the ratio of the [[derivative_definitions_and_their_relation_to_limits | derivatives]] as `x` approaches 1:
    `lim (x -> 1) [ (π cos(πx)) / (2x) ]` <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>
    `= (π cos(π)) / (2 * 1)`
    `= (π * -1) / 2`
    `= -π / 2` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>

This rule works because when both `f(x)` and `g(x)` are 0 at `x=a`, their values near `a` can be approximated by their [[derivative_definitions_and_their_relation_to_limits | derivatives]] times a small nudge `dx`. The ratio of `f(x)/g(x)` near `a` then approximates the ratio of their [[derivative_definitions_and_their_relation_to_limits | derivatives]] <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a> <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Application in [[integrals_and_derivatives | Integral Calculus]]

While this discussion has focused on the application of [[limits_in_calculus | limits]] to [[derivative_definitions_and_their_relation_to_limits | derivatives]], [[limits_in_calculus | limits]] are equally crucial for understanding [[integrals_and_derivatives | integrals]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The fundamental concept of an [[integrals_and_derivatives | integral]] involves summing an infinite number of infinitesimally small quantities, a process that is rigorously defined through the use of [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. The [[relationship_between_integrals_and_derivatives | Fundamental Theorem of Calculus]] also leverages [[limits_in_calculus | limits]] to provide a clear meaning to the idea of summing infinitely many tiny parts, often seen in [[visualizing_integration_and_approximations | approximating areas under curves]] <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. The exploration of [[understanding_antiderivatives_in_calculus | antiderivatives]] and the formal definition of [[integrals_and_derivatives | integrals]] similarly relies on the rigorous framework provided by [[limits_in_calculus | limits]].