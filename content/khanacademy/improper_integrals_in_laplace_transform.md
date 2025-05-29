---
title: Improper Integrals in Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 
The [[introduction_to_laplace_transform | Laplace Transform]] is a highly useful concept in mathematics, particularly in [[differential_calculus_and_its_applications | differential equations]] and engineering <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It allows for the transformation of functions or waveforms from the time domain to the frequency domain <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Definition of the Laplace Transform <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>

The [[introduction_to_laplace_transform | Laplace Transform]], denoted by `L`, is a function of functions, transforming one set of functions into another <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Conventionally, it takes a function of time, `f(t)`, and transforms it into a function of `s`, denoted `F(s)` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This is defined by an improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>:

$L\{f(t)\} = \int_0^\infty e^{-st} f(t) dt$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

### Understanding Improper Integrals <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

The presence of infinity as an integration limit means this is an improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. To evaluate such an integral, one must use limits <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The improper integral is rewritten as the limit of a definite integral <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

$ \int_0^\infty e^{-st} f(t) dt = \lim_{A \to \infty} \int_0^A e^{-st} f(t) dt $ <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>

### Example: Laplace Transform of f(t) = 1 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>

To illustrate, consider finding the [[basic_example_of_laplace_transform | Laplace Transform of f(t) = 1]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>:

1.  **Set up the integral:**
    $L\{1\} = \int_0^\infty e^{-st} (1) dt$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
2.  **Rewrite using limits:**
    $L\{1\} = \lim_{A \to \infty} \int_0^A e^{-st} dt$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
3.  **Find the antiderivative:**
    The antiderivative of $e^{-st}$ with respect to $t$ is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
4.  **Evaluate the definite integral:**
    $ \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_0^A $ <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>
    $= \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s(0)} \right) \right) $ <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>
    $= \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s}(1) \right) $ <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
    $= \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right) $ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
5.  **Evaluate the limit:**
    Assuming that $s > 0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as $A$ approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    Therefore, the first term $-\frac{1}{s}e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    The second term $\frac{1}{s}$ is unaffected by $A$ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

    Thus, $L\{1\} = 0 + \frac{1}{s} = \frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

The result demonstrates that the [[introduction_to_laplace_transform | Laplace Transform]] takes a function of `t` (even a constant one) and transforms it into a function of `s` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This specific result can be considered the first entry in a table of [[introduction_to_laplace_transform | Laplace Transforms]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.