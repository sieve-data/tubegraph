---
title: Transforming Functions from Time Domain to Frequency Domain
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is a highly useful concept in mathematics, particularly in differential equations and engineering <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Beyond [[solving_differential_equations_using_laplace_transform | solving differential equations]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, it enables the transformation of functions or waveforms from the time domain to the frequency domain <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This transformation helps in studying and understanding various phenomena <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is a Transform?

While a typical function takes one set of numbers to another set of numbers <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, a transform acts as a "function of functions" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. It takes one set of functions and transforms them into another set of functions <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Notation and Definition

The [[introduction_to_laplace_transform | Laplace Transform]] is denoted by a script 'L' <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Instead of `f(x)`, the convention for [[applications_of_functions | functions]] in this context is `f(t)` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, because in engineering and differential equations, one often converts from a function of time (`t`) to a function of frequency (`s`) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

The [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` transforms it into some other function of `s` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is defined as an improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$$L\{f(t)\} = \int_0^\infty e^{-st} f(t) dt$$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

## Example: Laplace Transform of 1

To demonstrate the [[introduction_to_laplace_transform | Laplace Transform]], consider `f(t) = 1` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The [[introduction_to_laplace_transform | Laplace Transform]] of 1 is <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>:

$$L\{1\} = \int_0^\infty e^{-st} \cdot 1 \, dt$$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

Since this is an improper integral, it is evaluated as a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

$$L\{1\} = \lim_{A \to \infty} \int_0^A e^{-st} \, dt$$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

1.  **Find the Anti-derivative**:
    The anti-derivative of $e^{-st}$ with respect to `t` is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

2.  **Evaluate the Definite Integral**:
    The integral becomes <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>:
    $$\lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_0^A$$
    $$\lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left(-\frac{1}{s}e^{-s \cdot 0}\right) \right)$$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>

    This simplifies to <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>:
    $$\lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right)$$

3.  **Evaluate the Limit**:
    Assuming that `s` is greater than 0 <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as `A` approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
    Therefore, the limit becomes:
    $$0 + \frac{1}{s} = \frac{1}{s}$$ <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

Thus, the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` is $\frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This result transitions a function of `t` to a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Further examples of [[laplace_transform_of_basic_functions | Laplace Transforms]] will be covered in subsequent videos <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.