---
title: Borwein integrals and their peculiar patterns
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

The "Borwein integrals" refer to a sequence of computations involving the sinc function that exhibit a surprising and seemingly stable pattern, initially equaling pi, before abruptly changing by a very small amount <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This phenomenon, described by Jonathan and David Borwein, puzzled even experienced researchers <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## The Sinc Function and Its Integral

The central character in this sequence is the **sinc function**, defined as `sin(x) / x` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Visualization**: It resembles an oscillating sine curve that is "squished down" as `x` moves away from zero, due to multiplication by `1/x` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Behavior at x=0**: Although plugging in `x=0` initially appears to be `0/0`, as `x` approaches `0`, the function approaches `1` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. By redefining `sinc(0)` to be `1`, the function becomes continuous <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Integral**: The integral of the `sinc` function from negative infinity to infinity, representing the [[signed_area_and_negative_integrals | signed area]] between the curve and the x-axis, happens to be exactly pi <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This is a non-obvious result using traditional calculus tools <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The Integral Sequence

The peculiar pattern emerges when modifying the sinc function through multiplication:
1.  **Initial Integral**: The integral of `sinc(x)` from negative infinity to infinity equals pi <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **First Iteration**: A copy of `sinc(x)` is taken, but with `x` replaced by `x/3` (stretching the graph horizontally by a factor of 3). When this `sinc(x/3)` is multiplied by the original `sinc(x)`, the resulting integral *still* equals pi <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This is counter-intuitive, as multiplying functions usually changes their area <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
3.  **Subsequent Iterations**: The pattern continues by multiplying the current function by increasingly stretched versions of the sinc function, using odd numbers in the denominator: `sinc(x/5)`, `sinc(x/7)`, `sinc(x/9)`, `sinc(x/11)`, `sinc(x/13)` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. In each case, the integral amazingly remains exactly pi <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
4.  **The Break**: This stability persists until the `sinc(x/15)` factor is introduced. At this point, the integral no longer equals pi, but a value "just barely, barely less than pi" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The exact value is a complex fraction of pi, with extremely large numerator and denominator <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
5.  **The Illusion of Error**: Due to the tiny difference, a researcher computing these integrals on a computer algebra system initially assumed it was a bug related to floating-point arithmetic <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. However, it is a genuine mathematical phenomenon <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Extended Pattern with `2cos(x)`
The pattern becomes even stranger when an additional factor of `2cos(x)` is included in the integral <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This new integral sequence continues to equal pi for much longer, only breaking when the factor `sinc(x/113)` is introduced <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. The deviation from pi is again extremely subtle <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## The Explanation: An Analogous Phenomenon

The bizarre behavior of the Borwein integrals can be understood through an analogy involving a sequence of moving averages.

### The Rect Function and Moving Averages
Consider a function `rect(x)`, which equals 1 if `x` is between -0.5 and 0.5, and 0 otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. Let this be `f1(x)` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
A sequence of new functions is defined by taking moving averages of the previous function:
1.  **f2(x)**: A moving average of `f1(x)` using a sliding window of width `1/3` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The value of `f2(x)` at a given `x` is the average value of `f1(x)` within the window centered at `x` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   This process smooths out the function.
    *   Crucially, when the window is entirely within the plateau of `f1(x)` (where `f1(x)=1`), `f2(x)` also equals `1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   The length of the plateau in `f2(x)` is `1 - 1/3` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  **Subsequent Iterations**: Each subsequent function `f_n(x)` is a moving average of `f_{n-1}(x)`, using a window width of `1/(2n-1)` (e.g., `1/5`, `1/7`, etc.) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
    *   The plateau in `f_n(x)` shrinks by the window width of that step <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. For example, the plateau length for `f3(x)` is `(1 - 1/3) - 1/5` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   As long as the window is entirely within the previous plateau, the function's value at `x=0` (which is within the plateau) remains `1` <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
3.  **The Break**: The plateau continues to shrink with each iteration. The "break" occurs when the sum of the reciprocals of the odd numbers (`1/3 + 1/5 + 1/7 + ...`) exceeds `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This happens when `1/15` is added, causing the total width reduction to be greater than the initial plateau width of 1 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   At this point (the eighth iteration, `f8(x)`), the plateau at `x=0` has completely disappeared, and the value of `f8(0)` becomes slightly less than `1` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Quantitative Correspondence
This "moving average" sequence exhibits the exact same pattern as the Borwein integrals: a stable value (1 for the function, pi for the integral) followed by a slight, precise drop at the same iteration (when the sum of `1/(2n-1)` terms first exceeds 1) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The amount of the drop in the moving average sequence corresponds to the factor by which the integral deviates from pi <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Extending the Analogy
For the case where the integral includes `2cos(x)`, the corresponding moving average analogy starts with an initial `rect` function that has a longer plateau (e.g., width 2 instead of 1) <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. It then takes longer for the sum of the `1/(2n-1)` reciprocals to exceed this larger initial width. The sum exceeds 2 when `1/113` is added, explaining why the integral pattern lasts until the 113th term <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## The Deeper Connection: Fourier Transforms and Convolutions

The reason these two seemingly unrelated phenomena are connected lies in the mathematical machinery of [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transforms]] and convolutions <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### Normalizing the Sinc Function
For clarity, the sinc function is often normalized by replacing `x` with `pi*x`, giving `sinc(pi*x) = sin(pi*x)/(pi*x)` <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This "engineer's sinc function" has an integral of exactly 1 from negative infinity to infinity <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. The patterns observed in the Borwein integrals are the same, just scaled by pi <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

### Fourier Transforms
A [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transform]] takes one function and produces another, rephrasing its information in a different "language" <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Sinc and Rect**: The [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transform]] of the normalized `sinc(pi*x)` function is precisely the `rect(x)` (top-hat) function <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Stretching Property**: Stretching the `sinc` function (e.g., `sinc(x/k)`) corresponds to a stretched and squished version of the `rect` function after a [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transform]] <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Key Facts Bridging the Gap
1.  **Integral to Evaluation**: The integral of a function `f(x)` from negative infinity to infinity is equivalent to evaluating its [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transform]] `F(s)` at `s=0` <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
    *   For the normalized sinc integral, this means `integral(sinc(pi*x) dx) = rect(0) = 1` <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>, explaining its baseline value.
2.  **Convolution Theorem**: When two functions are multiplied in one domain (e.g., the `x` domain for the sinc functions), their [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transforms]] in the other domain (the frequency domain) are combined using a new operation called a [[fourier_transforms_and_their_applications_in_integral_evaluation | convolution]] <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   Crucially, for the specific `rect` functions arising from the sinc transforms, the [[fourier_transforms_and_their_applications_in_integral_evaluation | convolution]] operation is precisely analogous to the "moving average" process described earlier <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Synthesis
The Borwein integrals can be understood by transforming the problem into the Fourier domain:
*   Each `sinc` function in the product transforms into a `rect` function.
*   Multiplying `sinc` functions (in the original domain) corresponds to convolving their `rect` function counterparts (in the Fourier domain) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   Integrating the product of `sinc` functions (in the original domain) corresponds to evaluating the final convolved `rect` function at zero (in the Fourier domain) <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

Since the [[fourier_transforms_and_their_applications_in_integral_evaluation | convolution]] operation in this context is identical to the moving average process that produces the shrinking plateau, the behavior of the integrals mirrors the values of the moving average functions at zero <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The eventual "break" in the integral sequence corresponds to the point where the `rect` function's plateau, reduced by successive convolutions (moving averages), finally shrinks past the evaluation point at zero.

This example elegantly demonstrates how [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier transforms]] can provide a "shift in perspective" that simplifies otherwise intractable problems, making complex integral evaluations understandable through simpler geometric analogies <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. The convolution theorem itself has wide-ranging applications, including surprisingly fast algorithms for multiplying large numbers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.