---
title: LHpitals rule for computing limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a [[introduction_to_limits_in_calculus | limit]] is fundamental in calculus, helping to define what it means for one value to "approach" another <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It's essentially a matter of assigning fancy notation to the intuitive idea of one value getting closer to another <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. [[applications_and_interpretations_of_limits_in_calculus | Limits]] allow mathematicians to make intuitive ideas more airtight and rigorous <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Limits and the Definition of a Derivative

The idea of a [[formal_definition_of_derivatives_using_limits | derivative]] heavily relies on [[introduction_to_limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. When considering a function `f(x)`, its [[formal_definition_of_derivatives_using_limits | derivative]] at a point (e.g., `x = 2`) involves imagining a small nudge `dx` to the input and observing the resulting change `df` in the output <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The ratio `df / dx` represents the rise over run slope <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The actual [[formal_definition_of_derivatives_using_limits | derivative]] is whatever this ratio approaches as `dx` approaches 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

The formal definition of a [[formal_definition_of_derivatives_using_limits | derivative]] is expressed using [[introduction_to_limits_in_calculus | limits]]:
`lim (h → 0) [f(x + h) - f(x)] / h` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
Here, `h` (or `delta x`) represents the finite, non-zero nudge to the input, avoiding the paradoxical idea of an infinitely small change <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The use of lowercase `d` terms like `dx` in typical [[formal_definition_of_derivatives_using_limits | derivative]] expressions implicitly contains this idea of a [[introduction_to_limits_in_calculus | limit]], where `dx` is supposed to eventually go to 0 <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Understanding "Approach"

The [[epsilondelta_definition_of_limits | epsilon-delta definition of limits]] provides a rigorous way to understand what "approach" means <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. For a [[introduction_to_limits_in_calculus | limit]] to exist, for any desired small distance `epsilon` around the limiting output value, there must be a corresponding input range `delta` around the limiting input point such that all outputs within that `delta` range are within `epsilon` of the limiting value <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. If no such `delta` can be found for a given `epsilon` (meaning the output range can't be made arbitrarily small), then the [[introduction_to_limits_in_calculus | limit]] does not exist <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## The Problem: Indeterminate Forms

Sometimes, when evaluating a function at a specific input, direct substitution leads to an indeterminate form like 0/0 <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. For example, consider the function `(sin(pi * x)) / (x^2 - 1)` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. If you try to plug in `x = 1`, both the numerator `sin(pi)` and the denominator `(1^2 - 1)` become 0, making the function undefined at that point <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. However, the graph might appear to approach a distinct value as `x` approaches 1 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

One way to [[approximating_solutions_using_calculus | approximate]] this value is to plug in a number very close to 1, like 1.00001 <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This might suggest a value around -1.57 <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. But to find the precise [[introduction_to_limits_in_calculus | limit]], a systematic process is needed <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## L'Hopital's Rule: A Clever Trick

After [[introduction_to_limits_in_calculus | limits]] are used to define [[formal_definition_of_derivatives_using_limits | derivatives]], [[formal_definition_of_derivatives_using_limits | derivatives]] can, in turn, help evaluate [[introduction_to_limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This is where L'Hopital's Rule comes in <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Derivation/Intuition

Consider two functions, `f(x)` and `g(x)`, both equal to 0 at some common value `x = a` <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. When examining the ratio `f(x) / g(x)` as `x` approaches `a`, a tiny nudge `dx` away from `a` can be considered <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

*   The value of `f` at `a + dx` is approximately its [[formal_definition_of_derivatives_using_limits | derivative]] `f'(a)` multiplied by `dx` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   Similarly, the value of `g` at `a + dx` is approximately its [[formal_definition_of_derivatives_using_limits | derivative]] `g'(a)` multiplied by `dx` <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

Therefore, near the "trouble point" `a`, the ratio `f(x) / g(x)` is approximately `(f'(a) * dx) / (g'(a) * dx)` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The `dx` terms cancel out, meaning the ratio of `f` and `g` near `a` is approximately the same as the ratio between their [[formal_definition_of_derivatives_using_limits | derivatives]] evaluated at `a` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. Since these approximations become more accurate for smaller `dx`, this ratio of [[formal_definition_of_derivatives_using_limits | derivatives]] gives the precise value for the [[introduction_to_limits_in_calculus | limit]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Applying the Rule

L'Hopital's Rule states that if `lim (x → a) f(x) = 0` and `lim (x → a) g(x) = 0`, then:

`lim (x → a) [f(x) / g(x)] = lim (x → a) [f'(x) / g'(x)]` <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

For the example `(sin(pi * x)) / (x^2 - 1)` as `x` approaches 1:
1.  **Numerator derivative**: The [[formal_definition_of_derivatives_using_limits | derivative]] of `sin(pi * x)` is `cos(pi * x) * pi` (by the chain rule) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. At `x = 1`, this is `cos(pi) * pi = -1 * pi = -pi` <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
2.  **Denominator derivative**: The [[formal_definition_of_derivatives_using_limits | derivative]] of `x^2 - 1` is `2x` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. At `x = 1`, this is `2 * 1 = 2` <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

Applying L'Hopital's Rule, the [[introduction_to_limits_in_calculus | limit]] is `(-pi) / 2` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This tells us the precise limiting value for the original function <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Important Considerations

*   **When to use**: L'Hopital's Rule is useful whenever an expression evaluates to an indeterminate form (like 0/0) when you plug in a particular input <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
*   **Limitations**: It cannot be used to *discover* new [[formal_definition_of_derivatives_using_limits | derivative]] formulas because applying it would require already knowing the [[formal_definition_of_derivatives_using_limits | derivative]] of the numerator <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **History**: Although known as L'Hopital's Rule, it was actually discovered by Johann Bernoulli, who was paid by L'Hopital for the rights to some of his mathematical discoveries <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.