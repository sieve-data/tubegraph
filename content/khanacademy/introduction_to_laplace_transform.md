---
title: Introduction to Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The Laplace Transform is considered one of the most useful concepts in mathematics, particularly in the field of [[introduction_to_differential_equations | differential equations]] and especially in [[applications_of_laplace_transform_in_engineering | engineering]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Beyond its utility in [[solving_differential_equations_using_laplace_transform | solving differential equations]], it also facilitates [[transforming_functions_from_time_domain_to_frequency_domain | transforming functions or waveforms from the time domain to the frequency domain]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is the Laplace Transform?
The Laplace Transform is a mathematical operation that converts one set of functions to another set of functions, distinguishing it from typical functions that map numbers to numbers <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. It transforms a function `f(t)` (conventionally a function of time) into another function `F(s)` (a function of `s`, representing frequency) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Notation
The notation for the Laplace Transform is typically a capital `L` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For example, the Laplace Transform of `f(t)` is denoted as `L{f(t)}` <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Mathematical Definition
For practical purposes, the Laplace Transform is defined as the improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$$ L\{f(t)\} = \int_{0}^{\infty} e^{-st}f(t) dt $$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

Since infinity cannot be directly evaluated, this improper integral is typically expressed as a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

$$ L\{f(t)\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st}f(t) dt $$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

## Example: Laplace Transform of `f(t) = 1`
To understand the application of the definition, consider finding the Laplace Transform of the constant function `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>:

1.  **Set up the integral:**
    $$ L\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt $$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

2.  **Find the anti-derivative:**
    The anti-derivative of $e^{-st}$ with respect to $t$ is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

3.  **Evaluate the definite integral with the limit:**
    $$ L\{1\} = \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A} $$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
    $$ = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s \cdot 0} \right) \right) $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    $$ = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right) $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

4.  **Take the limit:**
    Assuming $s > 0$, as $A$ approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    $$ L\{1\} = 0 + \frac{1}{s} = \frac{1}{s} $$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

Thus, the Laplace Transform of `f(t) = 1` is `1/s` <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This demonstrates the transformation from a function of `t` to a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Future Applications
This example serves as the first entry in a table of Laplace Transforms <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Further videos will explore [[laplace_transform_of_basic_functions | more basic Laplace Transforms]] and their derivation <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Eventually, these transforms will be applied to [[solving_differential_equations_using_laplace_transform | solve differential equations]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.