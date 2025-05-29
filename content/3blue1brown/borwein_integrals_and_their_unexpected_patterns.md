---
title: Borwein integrals and their unexpected patterns
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

The universe sometimes presents patterns in mathematical computations that appear predictable but eventually break, leading to surprising results <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A notable example involves a sequence of integrals whose values consistently equal pi for many iterations before subtly deviating <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Sinc Function

The primary function in this phenomenon is `sinc(x)`, defined as sine of x divided by x (sin(x)/x) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This function is significant in [[Derivatives and integrals | mathematics]] and [[Application of integrals in real world problems | engineering]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It can be visualized as an oscillating sine curve squished down by multiplying it by `1/x` as it moves away from zero <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While plugging in x=0 results in 0/0, calculus reveals that as x approaches 0, the function approaches 1 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Redefining `sinc(0)` to be 1 yields a continuous curve <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

The integral of `sinc(x)` from negative infinity to infinity, representing the signed area between the curve and the x-axis, evaluates to exactly pi <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This result is unexpected and not straightforward to compute with standard [[Antiderivatives and solving integrals | calculus tools]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## The Integral Sequence

The surprising pattern begins with this `sinc(x)` integral. The next step involves multiplying `sinc(x)` by a stretched version of itself, `sinc(x/3)`, which stretches the graph horizontally by a factor of 3 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Despite forming a more complicated wave, the integral of this product also remarkably equals pi <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

This pattern continues:
*   Subsequent iterations involve multiplying by `sinc(x/5)`, `sinc(x/7)`, `sinc(x/9)`, and so on, each time stretching by a new odd number <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   For many iterations, the integral continues to be exactly pi <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   Intuitively, as more `sinc` terms are multiplied (which are generally less than 1 except at x=0), one might expect the area under the curve to shrink <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   However, the integrals remain stable at pi until the eighth iteration, when the factor `sinc(x/15)` is introduced <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   At this point, the value of the integral becomes ever so slightly less than pi <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The exact value is a fraction of pi with extremely large numerator and denominator, confirming it's not a numerical error <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

This phenomenon was described in a paper by Jonathan and David Borwein, leading some researchers to initially believe it was a computational bug <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

Adding another factor, `2cos(x)`, to these integrals makes the pattern of equaling pi persist for much longer, breaking only when the denominator reaches 113 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Again, the deviation from pi is miniscule <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## The Analogy: Moving Averages and Rect Functions

A "satisfying explanation" for this behavior lies in a seemingly unrelated phenomenon involving [[Analogies between moving averages and integral patterns | moving averages]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Consider a function `rect(x)` defined as 1 if x is between -0.5 and 0.5, and 0 otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. Let this be `f1(x)` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
A sequence of new functions (`f2(x)`, `f3(x)`, etc.) is created by taking a [[Analogies between moving averages and integral patterns | moving average]] of the previous function using a sliding window:
*   `f2(x)` is the [[Analogies between moving averages and integral patterns | moving average]] of `f1(x)` with a window width of 1/3 <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The value of `f2(x)` at `x=0` is 1, as the window is entirely within `f1(x)`'s plateau <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The plateau length of `f2(x)` is `1 - 1/3` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Subsequent functions (`f3(x)`, `f4(x)`, etc.) are created by taking [[Analogies between moving averages and integral patterns | moving averages]] of the previous function with progressively smaller window widths of 1/5, 1/7, 1/9, and so on <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   The value of each function at x=0 remains 1 as long as the plateau of the previous function is wider than the current window width <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   The plateau shrinks with each step by the window width. The initial plateau width is 1 <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   This pattern breaks when the sum of the reciprocals of the odd numbers (1/3 + 1/5 + 1/7 + ...) becomes greater than 1 <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This occurs when the term 1/15 is added <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. At this point, the previous plateau is thinner than the current window, causing the value of the function at x=0 to be slightly less than 1 <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

```
Example Sequence of values at x=0:
1, 1, 1, 1, 1, 1, 1, (slightly less than 1)
```

This sequence's pattern mirrors the integral pattern: stable values followed by a tiny drop <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The factor by which the moving average constant at x=0 drops is *exactly* the factor by which the integral deviates from pi <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

The case where `2cos(x)` was added to the integral, extending the pattern to 113, corresponds to starting the [[Analogies between moving averages and integral patterns | moving average]] process with a `rect` function that has a longer plateau (e.g., length 2, from x=-1 to 1) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. It takes longer for the sum of the reciprocal odd numbers to exceed 2, which happens at the 113th term <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## The Connection: Fourier Transforms and Convolutions

The fundamental reason these two seemingly disparate phenomena are linked lies in the properties of [[Fourier transforms and convolutions in integral computation | Fourier transforms]] and [[Fourier transforms and convolutions in integral computation | convolutions]] <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

A simple substitution can transform the initial `sinc(x)` integral (`sin(x)/x` from -inf to inf equals pi) into one that evaluates to 1 by replacing `x` with `pi*x`. This version, `sin(pi*x)/(pi*x)`, is sometimes called the "engineer sinc function" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

The core connection is that the `sinc` function (or its "engineer" variant) is related to the `rect` function via a [[Fourier transforms and convolutions in integral computation | Fourier transform]] <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. A [[Fourier transforms and convolutions in integral computation | Fourier transform]] rephrases a function's information in a "different language," often making problems easier to solve <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. For example, the [[Fourier transforms and convolutions in integral computation | Fourier transform]] of the `sinc` function looks like the `rect` function <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

Two key facts bridge the gap:
1.  **Integral to Evaluation**: The integral of any function from negative infinity to infinity is equivalent to evaluating its [[Fourier transforms and convolutions in integral computation | Fourier transformed]] version at the input zero <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This explains why the integral of `sinc(pi*x)/(pi*x)` is 1, as it corresponds to `rect(0)`, which is 1 <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
2.  **Product to Convolution (Convolution Theorem)**: If you multiply two functions and then take the [[Fourier transforms and convolutions in integral computation | Fourier transform]] of that product, it's equivalent to taking the individual [[Fourier transforms and convolutions in integral computation | Fourier transforms]] of the original functions and then combining them using a [[Fourier transforms and convolutions in integral computation | convolution]] <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

For the specific case of `rect` functions, a [[Fourier transforms and convolutions in integral computation | convolution]] operation behaves like the [[Analogies between moving averages and integral patterns | moving averages]] described earlier <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Therefore, the sequence of multiplying `sinc` functions and integrating them in one domain is equivalent to performing progressive [[Analogies between moving averages and integral patterns | moving averages]] on `rect` functions and evaluating them at zero in the [[Fourier transforms and convolutions in integral computation | Fourier transform]] domain <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. This provides a deep intuition for why the stable value holds before breaking, as it reflects the shrinking of the plateau towards the center in the [[Analogies between moving averages and integral patterns | moving average]] analogy <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

These powerful tools, particularly the [[Fourier transforms and convolutions in integral computation | convolution theorem]], offer a systematic way to shift perspective on challenging problems, often making them more tractable <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. The [[Fourier transforms and convolutions in integral computation | convolution theorem]] also has practical applications, such as enabling very fast algorithms for computing the product of large numbers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.