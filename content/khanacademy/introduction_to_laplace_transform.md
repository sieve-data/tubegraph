---
title: Introduction to Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The Laplace Transform is considered one of the most useful concepts in mathematics, particularly in [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. For those pursuing [[application_of_laplace_transform_in_engineering | engineering]], it is invaluable not only for solving [[introduction_to_differential_equations | differential equations]] but also for transforming functions or waveforms from the time domain to the frequency domain, enabling the study of various phenomena <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## What is the Laplace Transform?

The Laplace Transform, denoted by the letter L <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, converts a function of `t` (often representing time, `f(t)`) into a different function of `s` (often representing frequency, `F(s)`) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It can be thought of as a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While a typical function maps one set of numbers to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Mathematical Definition

For our purposes, the Laplace Transform of a function `f(t)` is defined as the [[improper_integrals_in_laplace_transform | improper integral]] from `0` to `infinity` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$L\{f(t)\} = \int_0^{\infty} e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

This [[improper_integrals_in_laplace_transform | improper integral]] is evaluated using a limit:

$L\{f(t)\} = \lim_{A \to \infty} \int_0^{A} e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

## Example: Laplace Transform of f(t) = 1

Let's find the Laplace Transform of the constant function `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Set up the integral:**
    $L\{1\} = \int_0^{\infty} e^{-st} (1) dt$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

2.  **Rewrite as a limit:**
    $L\{1\} = \lim_{A \to \infty} \int_0^{A} e^{-st} dt$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

3.  **Find the anti-derivative with respect to `t`:**
    The anti-derivative of $e^{-st}$ with respect to `t` is $-\frac{1}{s} e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

4.  **Evaluate the definite integral:**
    $L\{1\} = \lim_{A \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_0^{A}$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
    $L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} - \left( -\frac{1}{s} e^{-s(0)} \right) \right)$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    $L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} e^0 \right)$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
    $L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \right)$ <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>

5.  **Evaluate the limit:**
    Assuming that `s > 0` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as `A` approaches `infinity`, the term $e^{-sA}$ approaches `0` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    Therefore:
    $L\{1\} = 0 + \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>
    $L\{1\} = \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

Thus, the Laplace Transform of `f(t) = 1` is `1/s` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This demonstrates how a function of `t` (even if not explicitly dependent on `t`) is transformed into a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.