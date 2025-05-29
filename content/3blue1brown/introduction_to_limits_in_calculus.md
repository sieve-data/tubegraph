---
title: Introduction to limits in calculus
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a limit in calculus is an intuitive idea of one value getting closer to another, assigned with fancy notation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. It's essentially understanding what the word "approach" means <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Limits are foundational for defining derivatives and integrals, and for making the intuitive ideas of calculus more rigorous <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Limits and the Formal Definition of Derivatives

Previous discussions of derivatives have involved the idea of a "nudge" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The formal definition of a derivative in calculus courses and textbooks aligns with this intuition <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

To understand the derivative of a function $f(x)$ at a specific input, say $x=2$:
1.  Imagine nudging the input by a small `dx` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Observe the resulting change to the output, `df` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  The ratio `df/dx` represents the rise-over-run slope between the starting point and the nudged point on the graph <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
4.  The actual derivative is whatever this ratio approaches as `dx` approaches 0 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

The change in output `df` is the difference between $f(\text{starting input} + dx)$ and $f(\text{starting input})$ <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. To express that this ratio approaches a value as `dx` approaches 0, the notation `lim` (for limit) is used, with `dx -> 0` written below it <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

Instead of `dx`, standard notation often uses `Δx` (delta x) or `h` within a limit expression <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This distinction emphasizes that `h` is an ordinary, non-zero, finitely small number, avoiding the paradoxical idea of an infinitely small change <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. The expressions `dx` and `df` used in [[introduction_to_derivatives_and_calculus_concepts | typical derivative expressions]] implicitly build in the idea of a limit, meaning `dx` is supposed to eventually go to 0 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The ratio `df/dx` is essentially shorthand for the more detailed [[formal_definition_of_derivatives_using_limits | formal definition of a derivative]] that explicitly spells out the limit process <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### The Problem with Infinitesimals
A key purpose of limits is to avoid talking about infinitely small changes. Instead, limits ask what happens as the size of some small change to a variable approaches 0 <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The interpretation of `dx` as a concrete, finitely small nudge, with the understanding that it approaches 0, helps build stronger intuition for where the rules of [[fundamental_concepts_of_calculus | calculus]] originate <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

## Understanding "Approach": Epsilon-Delta Definition

To rigorously define "approach," mathematicians use the epsilon-delta definition of limits <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This concept, part of real analysis, provides a rigorous framework for intuitive ideas <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

Consider a function $f(h) = \frac{(2+h)^3 - 2^3}{h}$ (which is the derivative of $x^3$ evaluated at $x=2$) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   This function is undefined at $h=0$ (results in $0/0$) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, creating a hole in its graph <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>, <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   However, as `h` approaches 0, the output of the function approaches 12 <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

When a limit exists, as the range of input values around the limiting point closes in, the corresponding range of output values also closes in around a specific value, and the size of that output range can be made as small as desired <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>, <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

For a function where the limit does not exist (e.g., a jump discontinuity at the point), as you shrink the input range, the corresponding outputs do not narrow in on any specific value; instead, they straddle a range that never shrinks smaller than a certain value <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Epsilon-Delta Defined
For a limit to exist at a value $L$, it means that for any arbitrary small distance `epsilon` (ε) away from $L$ (representing the desired smallness of the output range) <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>:
*   You can always find a corresponding range of inputs around the limiting input, defined by a distance `delta` (δ), such that any input within `delta` of the limiting point produces an output within `epsilon` of $L$ <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   This must hold true for *any* `epsilon`, no matter how small <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

If a limit does not exist, you can find a sufficiently small `epsilon` for which, no matter how tiny the `delta` (input range) you choose, the corresponding output range will always be too large to fall within `epsilon` of any single limiting output <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>, <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

## L'Hôpital's Rule for Computing Limits

Limits are essential for formally defining derivatives <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. In return, derivatives can help evaluate limits, particularly in indeterminate forms like $0/0$ <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This is known as L'Hôpital's Rule <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### How L'Hôpital's Rule Works

If you have a function that yields $0/0$ when you plug in a particular input (e.g., $\frac{\sin(\pi x)}{x^2-1}$ at $x=1$) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, you can find its limit as $x$ approaches that input.

The core idea is that if two functions, $f(x)$ and $g(x)$, are both 0 at a common value $x=a$ (and are differentiable at $x=a$) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>:
1.  Consider an input $x$ that is a tiny nudge `dx` away from $a$ <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
2.  The value of $f(x)$ at this nudged point is approximately its derivative, $f'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
3.  Similarly, the value of $g(x)$ at the nudged point is approximately $g'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
4.  Near this "trouble point," the ratio $\frac{f(x)}{g(x)}$ is approximately $\frac{f'(a) \cdot dx}{g'(a) \cdot dx}$ <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
5.  The `dx` terms cancel out, leaving $\frac{f'(a)}{g'(a)}$ <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
6.  Since these approximations become more accurate for smaller `dx`, this ratio of derivatives gives the precise limiting value <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

Therefore, whenever an expression results in $0/0$ upon direct substitution, you can try taking the derivative of the numerator and the derivative of the denominator separately, then plug in the problematic input again to find the limit <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

### Limitations of L'Hôpital's Rule
While powerful for evaluating limits, L'Hôpital's Rule cannot be used to discover new [[applications_and_interpretations_of_limits_in_calculus | derivative formulas]], as that would create a circular dependency (you need to know the derivative to use the rule) <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>, <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

## Conclusion

Limits are a fundamental concept in [[introduction_to_calculus_series | calculus]], providing a precise way to define concepts like the derivative and paving the way for understanding integrals and the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. They allow us to assign clear meaning to ideas that might otherwise flirt with infinity <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>, contributing to the strong [[visual_intuition_in_calculus | visual intuition in calculus]].