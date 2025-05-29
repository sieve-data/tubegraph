---
title: Basic Example of Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is presented as one of the most useful concepts in mathematics, particularly in [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is especially significant for those entering [[application_of_laplace_transform_in_engineering | engineering]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, where it aids in solving [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> and converting functions or waveforms from the [[Time and Frequency Domain Conversion | time domain]] to the [[Time and Frequency Domain Conversion | frequency domain]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Notation and Purpose
The [[introduction_to_laplace_transform | Laplace Transform]] of a [[Function notation and examples | function of t]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, typically denoted as `f(t)` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, is represented by a script 'L' symbol, reminiscent of "Laverne from Laverne and Shirley" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This transform converts the [[Function notation and examples | function of t]] into some other [[Function notation and examples | function of s]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The concept of a transform is analogous to a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While a standard function maps one set of numbers to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Definition
For practical purposes, the [[introduction_to_laplace_transform | Laplace Transform]] of a [[Function notation and examples | function of t]] is defined as the [[Improper Integrals in Laplace Transform | improper integral]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:

$$
\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

This [[Improper Integrals in Laplace Transform | improper integral]] means evaluating the limit as the upper bound approaches infinity <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Basic Example: Laplace Transform of 1
To understand the process, consider finding the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Set up the integral**:
    Substitute `f(t) = 1` into the definition:
    $$
    \mathcal{L}\{1\} = \int_{0}^{\infty} e^{-st} (1) dt = \int_{0}^{\infty} e^{-st} dt
    $$ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

2.  **Convert to a limit**:
    Since it's an [[Improper Integrals in Laplace Transform | improper integral]], express it as a limit:
    $$
    \mathcal{L}\{1\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt
    $$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

3.  **Find the anti-derivative**:
    The anti-derivative of $e^{-st}$ with respect to $t$ is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>:
    $$
    \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A}
    $$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>

4.  **Evaluate at the bounds**:
    Substitute the upper and lower bounds:
    $$
    \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left(-\frac{1}{s}e^{-s(0)}\right) \right)
    $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    This simplifies to:
    $$
    \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right)
    $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
    (Since $e^0 = 1$) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>

5.  **Evaluate the limit**:
    Assuming that $s > 0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as $A$ approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    $$
    \mathcal{L}\{1\} = 0 + \frac{1}{s} = \frac{1}{s}
    $$ <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

### Result
The [[introduction_to_laplace_transform | Laplace Transform]] of $f(t) = 1$ is $\frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This demonstrates the conversion from a [[Function notation and examples | function of t]] (even a constant one) to a [[Function notation and examples | function of s]] <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.