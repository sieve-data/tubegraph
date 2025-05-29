---
title: Solving Differential Equations using Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is a highly useful concept in mathematics, particularly in [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is especially valuable in [[applications_of_laplace_transform_in_engineering | engineering]], where it not only assists in [[understanding_solutions_of_differential_equations | solving differential equations]] but also enables the transformation of functions or waveforms from the time domain to the frequency domain, facilitating the study of various phenomena <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While the primary focus here is its utility in [[understanding_solutions_of_differential_equations | solving differential equations]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, it's important to understand its fundamental definition and application.

## Notation and Concept
The [[introduction_to_laplace_transform | Laplace Transform]] is denoted by the letter "L" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
It takes a function, conventionally expressed as `f(t)` (where 't' signifies the time domain, common in [[introduction_to_differential_equations | differential equations]] and [[applications_of_laplace_transform_in_engineering | engineering]]) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, and transforms it into another function of 's' <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

In essence, a transform is conceptualized as a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While a standard function maps numbers from one set to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Definition of the Laplace Transform
For our purposes, the [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` is defined as the improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$$
L\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

This integral is an improper integral, meaning it involves a limit as the upper bound approaches infinity <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It can be rewritten as:

$$
L\{f(t)\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} f(t) dt
$$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

## Example: Laplace Transform of f(t) = 1
Let's find the [[laplace_transform_of_basic_functions | Laplace Transform of f(t) = 1]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Set up the integral**:
    Substitute `f(t) = 1` into the definition:
    $$
    L\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt
    $$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

2.  **Find the antiderivative**:
    The antiderivative of `e^{-st}` with respect to `t` is `(-1/s)e^{-st}` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

3.  **Evaluate the definite integral**:
    $$
    \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A}
    $$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
    Substitute the limits of integration:
    $$
    \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s \cdot 0} \right) \right)
    $$ <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>

4.  **Simplify and take the limit**:
    Since `e^{-s \cdot 0} = e^0 = 1` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>, the expression becomes:
    $$
    \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right)
    $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
    Assuming `s > 0` <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, as `A` approaches infinity, the term `e^{-sA}` approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    Therefore, the limit evaluates to:
    $$
    0 + \frac{1}{s} = \frac{1}{s}
    $$ <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

### Result
The [[laplace_transform_of_basic_functions | Laplace Transform of f(t) = 1]] is `1/s` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This demonstrates the transformation from a function of `t` to a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

This is the first entry in what will become a table of [[laplace_transform_of_basic_functions | Laplace Transforms]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Future discussions will delve into how these transforms are used to [[understanding_solutions_of_differential_equations | solve differential equations]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.