---
title: Limits in calculus
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a limit is fundamental to calculus, serving as a rigorous way to define ideas like the [[derivative_definitions_and_their_relation_to_limits | derivative]] and later, the [[application_of_limits_in_integral_calculus | integral]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Intuitively, a limit describes what value a function "approaches" as its input gets closer and closer to a particular value <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Limits and the Formal Definition of a Derivative

In [[introduction_to_calculus | calculus]], the [[derivative_definitions_and_their_relation_to_limits | derivative]] of a function `f(x)` at a specific input (e.g., `x = 2`) is conceptually understood by considering a "nudge" to the input, `dx`, and the resulting change in the output, `df` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The ratio `df/dx` represents the slope between the original point and the nudged point on the graph <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The actual derivative is defined as what this `df/dx` ratio approaches as `dx` approaches 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
Formally, this is written using limit notation:
`lim (h -> 0) [f(x + h) - f(x)] / h` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

Here:
*   `df` is expressed as `f(x + h) - f(x)` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   `h` (or sometimes `delta x`) is used instead of `dx` in the limit expression to explicitly state that it's an ordinary, non-zero number that is *approaching* zero, rather than an "infinitesimally small change" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The `lim` notation with `h -> 0` below it indicates that the expression should be evaluated as `h` gets arbitrarily close to zero <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

This formal definition validates the intuitive understanding of `dx` and `df` as concrete, finitely small nudges <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The purpose of limits is to avoid paradoxical notions of "infinitely small changes" by instead analyzing what happens as the size of a small change approaches zero <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Understanding "Approach": Epsilon-Delta Definition

To precisely define what it means for a value to "approach" another, mathematicians use the epsilon-delta definition of limits <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Consider the function `(2 + h)^3 - 2^3 / h` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. While this function is undefined at `h = 0` (resulting in 0/0), its graph appears to be a continuous parabola with a hole at `h = 0` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. As `h` approaches 0 from either side, the corresponding output of the function approaches 12 <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

The epsilon-delta definition makes this precise:
*   **When a limit exists:** For *any* desired small distance from the limiting output value (called `epsilon`, denoted `ε`), you can always find a corresponding small distance around the input point (called `delta`, denoted `δ`) such that any input within `delta` of the limiting input will produce an output within `epsilon` of the limiting output <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The key is that this holds true for *any* `epsilon`, no matter how small <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **When a limit does not exist:** If a function jumps or has different approach values from different sides (e.g., approaching 2 from the right and 1 from the left at `h = 0`), the limit does not exist <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. In such cases, no matter how tiny the input range (`delta`) is made around the limiting point, the corresponding output range will not narrow in on a single value, or it will remain larger than some minimum `epsilon` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

While potentially "heavy duty" for an introduction, the epsilon-delta definition provides a rigorous foundation for the intuitive idea of "approach" and is explored in fields like real analysis <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Computing Limits: [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]]

One practical application of limits is computing values for functions that are undefined at a specific point, often producing an "indeterminate form" like 0/0. [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] is a powerful technique for this <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### The Problem

Consider the function `sin(pi * x) / (x^2 - 1)` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
If you plug in `x = 1`, the numerator `sin(pi)` is 0, and the denominator `(1^2 - 1)` is also 0, resulting in 0/0, which is undefined <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. However, the graph clearly approaches a distinct value at `x = 1` <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

### The Solution: [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]]

[[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] states that if you have a limit of the form `lim (x -> a) [f(x) / g(x)]` where both `f(a) = 0` and `g(a) = 0` (or both approach infinity), then:

`lim (x -> a) [f(x) / g(x)] = lim (x -> a) [f'(x) / g'(x)]` <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

This means you can find the limit by taking the [[derivative_definitions_and_their_relation_to_limits | derivative]] of the numerator and the [[derivative_definitions_and_their_relation_to_limits | derivative]] of the denominator separately, and then evaluating their ratio at the problem point <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

Applying this to the example `sin(pi * x) / (x^2 - 1)` as `x` approaches 1:
1.  **Numerator:** `f(x) = sin(pi * x)`. Its derivative `f'(x) = pi * cos(pi * x)` (using the chain rule) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
    At `x = 1`, `f'(1) = pi * cos(pi) = pi * (-1) = -pi` <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
2.  **Denominator:** `g(x) = x^2 - 1`. Its derivative `g'(x) = 2x` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
    At `x = 1`, `g'(1) = 2 * 1 = 2` <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

Therefore, `lim (x -> 1) [sin(pi * x) / (x^2 - 1)] = f'(1) / g'(1) = -pi / 2` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

This rule leverages the idea that near the trouble point, the behavior of `f(x)` and `g(x)` is approximated by their tangent lines (whose slopes are given by the derivatives), and the ratio of the original functions becomes approximately the ratio of their derivatives <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

It's important to note that while [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] uses derivatives to compute limits, it cannot be used to *discover* derivative formulas themselves, as that would be circular reasoning <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

## Conclusion

Limits provide the rigorous backbone for many concepts in [[introduction_to_calculus | calculus]], offering a precise way to analyze the behavior of functions as inputs approach specific values, particularly when dealing with phenomena that "flirt with infinity" <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. The understanding of limits paves the way for further exploration into topics such as [[application_of_limits_in_integral_calculus | integrals]] and the [[the_fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.