---
title: Laplace Transform and Differential Equations
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is introduced as a highly useful concept in mathematics, particularly in [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. For those pursuing [[laplace_transform_in_engineering | engineering]], it is invaluable not only for solving [[solutions_to_differential_equations | differential equations]] but also for transforming functions or waveforms from the time domain to the frequency domain, enabling the study of various phenomena <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

While its application in [[laplace_transform_in_engineering | engineering]] and its use in solving [[solutions_to_differential_equations | differential equations]] will be demonstrated in later lessons <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, the initial focus is on understanding what the [[introduction_to_laplace_transform | Laplace Transform]] is and its [[mathematics_of_the_laplace_transform | mathematical foundations]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## What is the Laplace Transform?
The notation for the [[introduction_to_laplace_transform | Laplace Transform]] is an 'L' <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
Conventionally, the function being transformed is denoted as `f(t)` instead of `f(x)` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This is because, in [[introduction_to_differential_equations | differential equations]] and [[laplace_transform_in_engineering | engineering]], there is often a conversion from a function of time (`t`) to a function of frequency (`s`) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The [[introduction_to_laplace_transform | Laplace Transform]] transforms a function of `t` into some other function of `s` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Conceptually, the [[introduction_to_laplace_transform | Laplace Transform]] acts as a "function of functions" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. While a regular function maps one set of numbers to another, a transform maps one set of functions to another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Mathematical Definition
For the purposes of this introduction, the [[laplace_transform_in_engineering | Laplace Transform]] of a function `f(t)` is defined as the [[improper_integrals_in_laplace_transform | improper integral]]:

$L\{f(t)\} = \int_0^\infty e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>

## Example: Laplace Transform of f(t) = 1
To understand the application of this definition, consider the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Given `f(t) = 1`, the [[introduction_to_laplace_transform | Laplace Transform]] becomes:
$L\{1\} = \int_0^\infty e^{-st} \cdot 1 dt$ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

This [[improper_integrals_in_laplace_transform | improper integral]] can be expressed as a limit:
$L\{1\} = \lim_{A \to \infty} \int_0^A e^{-st} dt$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

First, find the anti-derivative of $e^{-st}$ with respect to $t$:
$\int e^{-st} dt = -\frac{1}{s} e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

Now, evaluate the definite integral and then the limit:
$L\{1\} = \lim_{A \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_0^A$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
$L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} - \left( -\frac{1}{s} e^{-s \cdot 0} \right) \right)$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
$L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \right)$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

Assuming that $s > 0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as $A$ approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
Thus:
$L\{1\} = 0 + \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>
$L\{1\} = \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

This demonstrates the first [[introduction_to_laplace_transform | Laplace Transform]]: the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` is $1/s$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This result transforms a function of `t` (even if constant) into a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Further examples and a comprehensive table of [[laplace_transform_in_engineering | Laplace Transforms]] will be explored in subsequent videos <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.