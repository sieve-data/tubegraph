---
title: Time and Frequency Domain Conversion
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is a highly useful concept in mathematics, especially in differential equations and engineering <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Beyond its role in solving differential equations, it serves to transform functions or waveforms from the **time domain** to the **frequency domain** <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This conversion allows for the study and understanding of a broad range of phenomena <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

In many engineering applications and differential equations, functions of time (`f(t)`) are converted into functions of frequency (`F(s)`) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## What is a Transform?
While a typical function maps one set of numbers to another, a "transform" takes one set of functions and converts them into another set of functions <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The [[introduction_to_laplace_transform | Laplace Transform]] is a specific example of this, transforming a function of time, `f(t)`, into a function of `s`, denoted as `F(s)` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

## Definition of the Laplace Transform
The [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` is defined as the [[improper_integrals_in_laplace_transform | improper integral]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>:

$$ L\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt $$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>

This [[improper_integrals_in_laplace_transform | improper integral]] is formally expressed as a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:

$$ \lim_{A \to \infty} \int_{0}^{A} e^{-st} f(t) dt $$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>

### Notation
The notation for the [[introduction_to_laplace_transform | Laplace Transform]] uses an 'L' symbol, often likened to "Laverne" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The function being transformed is typically represented as `f(t)` to indicate its dependence on time <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## [[basic_example_of_laplace_transform | Basic Example]]: Laplace Transform of 1
To illustrate, consider `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
The [[introduction_to_laplace_transform | Laplace Transform]] of 1 is <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>:

$$ L\{1\} = \int_{0}^{\infty} e^{-st} (1) dt = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt $$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>

1.  **Find the anti-derivative**: The anti-derivative of $e^{-st}$ with respect to $t$ is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  **Evaluate the definite integral**:
    $$ \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A} $$ <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
    Substitute $t=A$ and $t=0$:
    $$ \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s \cdot 0} \right) \right) $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
    This simplifies to:
    $$ \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right) $$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>, <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>, <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>
3.  **Evaluate the limit**: Assuming $s > 0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, as $A \to \infty$, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    Therefore, the limit becomes:
    $$ 0 + \frac{1}{s} = \frac{1}{s} $$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>

Thus, the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` is $\frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This is often the first entry in a table of [[introduction_to_laplace_transform | Laplace Transforms]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.