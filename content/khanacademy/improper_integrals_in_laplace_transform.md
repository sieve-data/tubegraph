---
title: Improper Integrals in Laplace Transform
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is fundamentally defined using an improper integral <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This concept is crucial for understanding how the transform operates, especially when converting functions from the time domain to the frequency domain <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Definition of the Laplace Transform using Improper Integrals

The [[introduction_to_laplace_transform | Laplace Transform]] of a function, typically denoted as *f(t)* (where *t* often represents time) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, transforms it into another function of *s* (representing frequency) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This transformation is defined by the following improper integral:

$$ \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) \, dt $$ <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

Since one cannot directly evaluate an integral at infinity, an improper integral is formally expressed as a limit <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This means the [[Laplace Transform]] can be written as:

$$ \mathcal{L}\{f(t)\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} f(t) \, dt $$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

This formulation allows for the evaluation of the integral by taking the [[understanding_the_concept_of_limits_in_calculus | limit]] as the upper bound approaches infinity <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Example: Laplace Transform of f(t) = 1

To illustrate the application of improper integrals in the [[Laplace Transform]], consider finding the [[introduction_to_laplace_transform | Laplace Transform]] of *f(t) = 1* <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The integral becomes:

$$ \mathcal{L}\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 \, dt $$ <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>

This is evaluated as a limit:

$$ \mathcal{L}\{1\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} \, dt $$ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

1.  **Find the antiderivative**: The antiderivative of $e^{-st}$ with respect to *t* is $-\frac{1}{s}e^{-st}$ <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   To verify, taking the [[derivatives_and_calculus_terminology | derivative]] of $-\frac{1}{s}e^{-st}$ yields $e^{-st}$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

2.  **Evaluate the definite integral**:
    $$ \lim_{A \to \infty} \left[ -\frac{1}{s}e^{-st} \right]_{0}^{A} $$ <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
    $$ = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} - \left( -\frac{1}{s}e^{-s \cdot 0} \right) \right) $$ <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    $$ = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s}e^{0} \right) $$
    Since $e^0 = 1$:
    $$ = \lim_{A \to \infty} \left( -\frac{1}{s}e^{-sA} + \frac{1}{s} \right) $$ <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>

3.  **Apply the limit**: Assuming *s > 0* <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, as *A* approaches infinity, the term $e^{-sA}$ approaches 0 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    $$ = 0 + \frac{1}{s} $$
    $$ = \frac{1}{s} $$ <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>

Thus, the [[introduction_to_laplace_transform | Laplace Transform]] of *f(t) = 1* is $\frac{1}{s}$ <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This demonstrates how the transform converts a function of *t* into a function of *s* <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.