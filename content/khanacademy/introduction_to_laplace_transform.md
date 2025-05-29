---
title: Introduction to Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The Laplace Transform is a highly useful concept in [[introduction_to_differential_equations | differential equations]] and broader [[mathematics_of_the_laplace_transform | mathematics]], particularly for those going into [[laplace_transform_in_engineering | engineering]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Beyond helping to [[laplace_transform_and_differential_equations | solve differential equations]], it assists in transforming functions or waveforms from the time domain to the frequency domain, enabling the study of various phenomena <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## What is the Laplace Transform?

The Laplace Transform is a *transform*, which can be thought of as a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While a standard function typically maps one set of numbers to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Notation and Convention
The notation for the Laplace Transform is typically a capital "L" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. When defining the Laplace Transform of a function, the convention is to use `f(t)` instead of `f(x)` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This is because in engineering and [[introduction_to_differential_equations | differential equations]], functions are often being converted from a function of time (`t`) to a function of frequency (`s`) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The Laplace Transform converts a function of `t` into some other function of `s` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Definition
For our purposes, the Laplace Transform of a function `f(t)` is defined as the [[improper_integrals_in_laplace_transform | improper integral]] from 0 to infinity <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>:

$$
\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

The [[improper_integrals_in_laplace_transform | improper integral]] from 0 to infinity can be expressed as a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

$$
\mathcal{L}\{f(t)\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} f(t) dt
$$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

This formulation helps evaluate the integral, as infinity cannot be directly evaluated, but a limit as a variable approaches infinity can be <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Example: Laplace Transform of 1

Let's find the Laplace Transform of the constant function `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Set up the integral**:
    $$
    \mathcal{L}\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt
    $$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

2.  **Find the antiderivative**:
    The antiderivative of $e^{-st}$ with respect to $t$ is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

3.  **Evaluate the definite integral**:
    $$
    \mathcal{L}\{1\} = \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A}
    $$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
    $$
    = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s \cdot 0} \right) \right)
    $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    Since $e^0 = 1$:
    $$
    = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right)
    $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

4.  **Take the limit**:
    Assuming $s > 0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as $A \to \infty$, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    Therefore, the term $-\frac{1}{s}e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    The limit becomes:
    $$
    \mathcal{L}\{1\} = 0 + \frac{1}{s} = \frac{1}{s}
    $$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

Thus, the Laplace Transform of 1 is $1/s$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This demonstrates how a function of `t` (in this case, a constant not dependent on `t`) is transformed into a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. In subsequent videos, more Laplace Transforms will be explored, which can be found in reference tables <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.