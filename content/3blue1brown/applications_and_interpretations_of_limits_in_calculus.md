---
title: Applications and interpretations of limits in calculus
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a [[introduction_to_limits_in_calculus | limit]] is fundamental to [[fundamental_concepts_of_calculus | calculus]], even though it's intuitively straightforward. At its core, a limit describes what a value "approaches" [00:00:25] or "gets closer to" [00:00:32]. While seemingly simple, limits provide the rigorous foundation for [[introduction_to_derivatives_and_calculus_concepts | derivatives]] and other advanced concepts.

## Limits and the Formal Definition of Derivatives

The idea of a [[introduction_to_derivatives_and_calculus_concepts | derivative]] involves understanding the ratio of a small change in output (`df`) to a small change in input (`dx`) [00:00:14]. This ratio represents the "rise over run" slope on a graph [00:01:37]. The actual [[introduction_to_derivatives_and_calculus_concepts | derivative]] is precisely what this ratio approaches as `dx` approaches 0 [00:01:49].

The [[formal_definition_of_derivatives_using_limits | formal definition of a derivative]] uses limit notation to express this idea [00:01:40]. For a function `f(x)`, its [[introduction_to_derivatives_and_calculus_concepts | derivative]] at a given input is defined as:

```
lim (h→0) [f(x + h) - f(x)] / h
```

Here, `h` (or `delta x`) is used instead of `dx` in the formal expression to emphasize that it represents an ordinary, non-zero, finitely small number [00:02:25]. The [[introduction_to_derivatives_and_calculus_concepts | derivative]] expression `df/dx` can be seen as shorthand for this more detailed limit process [00:02:44].

This formal definition clarifies that [[introduction_to_limits_in_calculus | limits]] allow [[fundamental_concepts_of_calculus | calculus]] to avoid "infinitely small changes" [00:03:11], instead focusing on what happens as the size of a small change approaches zero [00:04:44]. This approach builds strong intuition for the rules of [[fundamental_concepts_of_calculus | calculus]] [00:04:23].

## Understanding "Approach": Epsilon-Delta Definition

To precisely define what "approach" means, mathematicians use the epsilon-delta definition of [[introduction_to_limits_in_calculus | limits]] [00:04:53].

Consider a function like `(2 + h)^3 - 2^3 / h`. Although it's undefined at `h = 0` (resulting in `0/0`), its graph shows a hole at that point, and the function's output clearly approaches 12 as `h` approaches 0 [00:05:00].

<div style="text-align: center;">
<img src="https://i.imgur.com/example_hole_graph.png" alt="Graph with a hole at h=0" width="300">
</div>
*The graph of (2+h)^3 - 2^3 / h showing a hole at h=0, but approaching 12.* <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

In contrast, for a function with a jump discontinuity at `h = 0`, the limit is not defined because approaching from the right yields one value (e.g., 2) and approaching from the left yields another (e.g., 1) [00:07:06]. There isn't a single unambiguous value the function approaches [00:07:15].

The epsilon-delta definition formalizes this:
*   A [[introduction_to_limits_in_calculus | limit]] exists if, for any arbitrarily small "epsilon" distance away from the limiting output, you can always find a "delta" distance around the limiting input [00:08:58].
*   Any input within that "delta" range (excluding the limiting point itself) will produce an output within the "epsilon" range of the limit [00:09:10].
*   If a limit doesn't exist, you can find an epsilon (no matter how small delta is) where the output range never shrinks sufficiently [00:09:29].

While rigorous, this definition provides an "airtight" way for mathematicians to define intuitive ideas in [[fundamental_concepts_of_calculus | calculus]] [00:08:16].

## L'Hôpital's Rule for Computing Limits

[[introduction_to_limits_in_calculus | Limits]] are crucial for formally defining [[introduction_to_derivatives_and_calculus_concepts | derivatives]], and [[introduction_to_derivatives_and_calculus_concepts | derivatives]], in turn, can help evaluate [[introduction_to_limits_in_calculus | limits]] [00:11:36].

Consider a function like `sin(πx) / (x^2 - 1)`, which results in the indeterminate form `0/0` when `x = 1` [00:10:30]. This means the function is undefined at that point, but the graph appears to approach a specific value [00:10:39]. [[approximating_solutions_using_calculus | Approximating solutions using calculus]] by plugging in a value very close to 1 (e.g., 1.00001) suggests the limit is around -1.57 [00:11:07].

**L'Hôpital's Rule** provides a systematic way to find the precise limit when encountering `0/0` (or `infinity/infinity`) indeterminate forms [00:15:58].

### How L'Hôpital's Rule Works:

If you have two functions `f(x)` and `g(x)` that are both 0 at a common value `x = a` (i.e., `f(a) = 0` and `g(a) = 0`), and their [[introduction_to_derivatives_and_calculus_concepts | derivatives]] exist at `x = a` [00:14:24], then:

`lim (x→a) f(x) / g(x) = lim (x→a) f'(x) / g'(x)` [00:15:37]

This works because, near the "trouble point" `x = a`, the values of `f(x)` and `g(x)` can be approximated by their respective [[introduction_to_derivatives_and_calculus_concepts | derivatives]] multiplied by a small nudge `dx` [00:15:06]. The ratio `f(x)/g(x)` then becomes approximately `(f'(a) * dx) / (g'(a) * dx)`, and the `dx` terms cancel out, leaving the ratio of the [[introduction_to_derivatives_and_calculus_concepts | derivatives]] [00:15:31]. As `dx` gets smaller, these approximations become more accurate, yielding the precise limit value [00:15:45].

Applying this to `sin(πx) / (x^2 - 1)` at `x = 1`:
*   Derivative of numerator `f'(x) = π * cos(πx)` [00:13:33]
*   Derivative of denominator `g'(x) = 2x` [00:13:18]
*   Plug in `x = 1`: `π * cos(π) / (2 * 1) = π * (-1) / 2 = -π/2` [00:13:50]

So, the limit is exactly `-π/2`, which is approximately -1.5708 [00:14:02].

L'Hôpital's Rule is a powerful tool for computing [[introduction_to_limits_in_calculus | limits]] [00:15:55]. However, it's important to note that it cannot be used to discover new [[formal_definition_of_derivatives_using_limits | derivative formulas]] [00:16:45], as that would create a circular dependency. The process of discovering [[introduction_to_derivatives_and_calculus_concepts | derivative formulas]] often requires more creativity and insight [00:17:06].