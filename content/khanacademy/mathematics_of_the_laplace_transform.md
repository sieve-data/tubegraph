---
title: Mathematics of the Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is a highly useful concept in [[laplace_transform_in_engineering | mathematics]], particularly within [[laplace_transform_and_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is especially valuable in [[laplace_transform_in_engineering | engineering]], where it aids in solving [[laplace_transform_and_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> and transforming functions or waveforms from the time domain to the frequency domain <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This transformation allows for the study and understanding of a wide range of phenomena <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Notation and Purpose

The notation for the [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` is represented by an "L" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The convention typically uses `f(t)` instead of `f(x)` because many applications in [[laplace_transform_and_differential_equations | differential equations]] and [[laplace_transform_in_engineering | engineering]] involve converting a function of time to a function of frequency <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The [[introduction_to_laplace_transform | Laplace Transform]] converts a function of `t`, `f(t)`, into another function of `s`, `F(s)` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Conceptually, a transform can be thought of as a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While a standard function maps one set of numbers to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Mathematical Definition

The [[introduction_to_laplace_transform | Laplace Transform]] for our purposes is defined as the [[improper_integrals_in_laplace_transform | improper integral]] from 0 to infinity <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$$ L\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt $$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

## Example: Laplace Transform of `f(t) = 1`

To understand the application of this definition, let's find the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>:

$$ L\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt $$ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

Since this is an [[improper_integrals_in_laplace_transform | improper integral]] with an upper limit of infinity, it is evaluated using a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

$$ L\{1\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt $$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

### Finding the Anti-derivative

The [[derivatives_and_calculus_terminology | anti-derivative]] of `e^(-st)` with respect to `t` is `-1/s * e^(-st)` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Evaluating the Limit

Now, substitute the limits of integration and evaluate the limit as `A` approaches infinity <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>:

$$ \lim_{A \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_{0}^{A} $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>

Substitute `A` for `t`:

$$ -\frac{1}{s} e^{-sA} $$ <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>

Substitute `0` for `t`:

$$ -\frac{1}{s} e^{-s \cdot 0} = -\frac{1}{s} \cdot 1 = -\frac{1}{s} $$ <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>

Combining these:

$$ \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} - \left(-\frac{1}{s}\right) \right) = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \right) $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

Assuming `s > 0`, as `A` approaches infinity, the term `e^(-sA)` approaches 0 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Therefore, `(-1/s) * e^(-sA)` approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

$$ L\{1\} = 0 + \frac{1}{s} = \frac{1}{s} \quad \text{for } s > 0 $$ <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>

### Result

The [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` is `1/s` <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This demonstrates the transformation from a function of `t` (even if constant) to a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Whole tables of [[introduction_to_laplace_transform | Laplace Transforms]] exist, which can be proven using this method <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.