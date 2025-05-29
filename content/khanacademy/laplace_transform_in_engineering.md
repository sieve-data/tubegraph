---
title: Laplace Transform in Engineering
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is considered one of the most useful concepts in [[mathematics_of_the_laplace_transform | mathematics]], particularly within [[introduction_to_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It holds significant importance for individuals pursuing careers in engineering <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Role in Engineering

Beyond its utility in solving [[laplace_transform_and_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, the [[introduction_to_laplace_transform | Laplace Transform]] also facilitates the transformation of functions or waveforms from the time domain to the frequency domain <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This transformation enables the study and understanding of a wide range of phenomena <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The common convention for functions in [[introduction_to_laplace_transform | Laplace Transform]] is `f(t)` (function of time) rather than `f(x)`, because a key application, especially in engineering, involves converting a function of time to a function of frequency <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Definition and Notation

The [[introduction_to_laplace_transform | Laplace Transform]] is denoted by an 'L' symbol <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Conceptually, a transform is a "function of functions," meaning it takes one set of functions and converts them into another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Mathematically, the [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` is defined as the [[improper_integrals_in_laplace_transform | improper integral]]:

$\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>

This integral transforms the function `f(t)` (of variable `t`) into a new function of `s` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Understanding Improper Integrals

To evaluate the [[improper_integrals_in_laplace_transform | improper integral]] definition, it is expressed as a limit:
$\int_{0}^{\infty} e^{-st} f(t) dt = \lim_{A \to \infty} \int_{0}^{A} e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

This approach allows for evaluation since infinity cannot be directly computed <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Example: Laplace Transform of 1

Let's find the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Set up the integral:**
    $\mathcal{L}\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

2.  **Rewrite as a limit:**
    $\lim_{A \to \infty} \int_{0}^{A} e^{-st} dt$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

3.  **Find the anti-derivative with respect to `t`:**
    The anti-[[derivatives_and_calculus_terminology | derivative]] of $e^{-st}$ is $-\frac{1}{s} e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

4.  **Evaluate the definite integral:**
    $\lim_{A \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_{0}^{A}$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    $= \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} - \left( -\frac{1}{s} e^{-s \cdot 0} \right) \right)$ <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>
    $= \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \right)$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

5.  **Evaluate the limit:**
    Assuming `s > 0` <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, as `A` approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    So, the limit becomes $0 + \frac{1}{s} = \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

Thus, the [[introduction_to_laplace_transform | Laplace Transform]] of $f(t) = 1$ is $\frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This demonstrates how a function of `t` can be transformed into a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

The result can be added to a table of [[introduction_to_laplace_transform | Laplace Transforms]], which are commonly used to solve problems efficiently <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.