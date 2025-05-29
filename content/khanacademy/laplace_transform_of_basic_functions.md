---
title: Laplace Transform of Basic Functions
videoId: OiNh2DswFt4
---

From: [[khanacademy]] <br/> 

The [[introduction_to_laplace_transform | Laplace Transform]] is introduced as a highly useful concept in mathematics, particularly in [[solving_differential_equations_using_laplace_transform | differential equations]] and [[applications_of_laplace_transform_in_engineering | engineering]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Beyond [[solving_differential_equations_using_laplace_transform | solving differential equations]], it helps to [[transforming_functions_from_time_domain_to_frequency_domain | transform functions]] or waveforms from the time domain to the frequency domain to study various phenomena <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

## Notation and Concept

The notation for the [[introduction_to_laplace_transform | Laplace Transform]] is represented by a stylized 'L' <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. When applied to a function, the convention often uses `f(t)` instead of `f(x)`, as it frequently deals with functions of time being converted to functions of frequency in [[applications_of_laplace_transform_in_engineering | engineering]] contexts <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. The [[introduction_to_laplace_transform | Laplace Transform]] takes a function of `t`, `f(t)`, and transforms it into some other function of `s`, often denoted as `F(s)` <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

It can be thought of as a "function of functions" or a "transform," meaning it takes one set of functions and converts them into another set of functions, much like a regular function converts one set of numbers to another <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

## Definition of the Laplace Transform

For practical purposes, the [[introduction_to_laplace_transform | Laplace Transform]] of a function `f(t)` is defined as the improper integral <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>:

$$L\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt$$ <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>

This integral transforms the function `f(t)` into a new function that depends on `s` <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Example: Laplace Transform of 1

To understand the [[introduction_to_laplace_transform | Laplace Transform]], consider finding the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>:

1.  **Substitute into the definition**:
    $$L\{1\} = \int_{0}^{\infty} e^{-st} \cdot 1 dt$$ <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>

2.  **Address the improper integral**:
    An improper integral with an infinite limit is evaluated using a [[introduction_to_limits_in_calculus | limit]] as a variable approaches infinity <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>:
    $$L\{1\} = \lim_{A \to \infty} \int_{0}^{A} e^{-st} dt$$ <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>

3.  **Find the antiderivative**:
    The antiderivative of `e^(-st)` with respect to `t` is `-1/s * e^(-st)` <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>:
    $$L\{1\} = \lim_{A \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_{0}^{A}$$ <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>

4.  **Evaluate at the limits**:
    Substitute `A` and `0` for `t`:
    $$L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} - \left( -\frac{1}{s} e^{-s \cdot 0} \right) \right)$$ <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>
    $$L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \cdot 1 \right)$$ <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>
    $$L\{1\} = \lim_{A \to \infty} \left( -\frac{1}{s} e^{-sA} + \frac{1}{s} \right)$$ <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>

5.  **Evaluate the limit**:
    Assuming `s > 0` <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>:
    *   As `A` approaches infinity, the term `e^(-sA)` approaches `0` <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.
    *   Therefore, `(-1/s) * e^(-sA)` approaches `0` <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
    *   The term `1/s` is unaffected by `A` <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.
    $$L\{1\} = 0 + \frac{1}{s}$$ <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>
    $$L\{1\} = \frac{1}{s}$$ <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>

Thus, the [[introduction_to_laplace_transform | Laplace Transform]] of `f(t) = 1` is `1/s`, provided `s > 0` <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. This demonstrates how a function of `t` (even a constant one not explicitly dependent on `t`) is transformed into a function of `s` <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. This is the first entry in a table of [[introduction_to_laplace_transform | Laplace Transforms]] <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.