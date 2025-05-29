---
title: Fourier transforms and convolutions in integral computation
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

The universe sometimes seems to mess with us through predictable, yet seemingly random, patterns in computations <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. One such sequence involves integrals that consistently evaluate to pi, only to subtly break this pattern later <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Sinc Function and Its Peculiar Integral

The central element in this phenomenon is the `sinc` function, defined as `sin(x) / x` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This function is common in mathematics and engineering <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It can be visualized as an oscillating sine curve that is "squished down" by `1/x` as `x` moves away from zero <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. At `x = 0`, where it initially appears as `0/0`, the function approaches `1` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Redefining `sinc(0)` as `1` makes the function continuous <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

The integral of `sinc(x)` from negative infinity to infinity, representing its signed area, surprisingly evaluates to exactly pi <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This result is unexpected and not easily derived using standard calculus tools <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The Puzzling Integral Sequence

The peculiar pattern begins with this `sinc(x)` integral:
1.  **First iteration**: The integral of `sinc(x)` equals pi <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Next iteration**: Multiply `sinc(x)` by `sinc(x/3)`. The `sinc(x/3)` function is `sinc(x)` stretched horizontally by a factor of 3 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Even though multiplying these functions creates a more complex wave, the integral of their product still equals pi <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  **Further iterations**: Continue multiplying by increasingly stretched versions of `sinc(x)` using new odd numbers (e.g., `sinc(x/5)`, `sinc(x/7)`, etc.) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. In each case, the integral of the cumulative product continues to equal pi <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

This stability is bizarre, especially since each multiplication by `sinc(x/k)` (where `k > 1`) progressively squishes the function, suggesting the area should decrease <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### The Borwein Phenomenon

The pattern eventually breaks <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. When the sequence reaches the term `sinc(x/15)`, the integral evaluates to a value that is barely less than pi <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This isn't a numerical error, but an exact mathematical result <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The exact value is a fraction of pi with extremely large numerator and denominator, around 400 billion billion billion <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

This phenomenon was described in a paper by Jonathan and David Borwein, who noted that a fellow researcher initially suspected a bug in his computer algebra system when he encountered this break <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

The pattern becomes even stranger when another factor, `2 cos(x)`, is included in the integral product. This modification would typically change the integral's value entirely <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. However, the integral continues to equal pi for much longer, only breaking when the term `sinc(x/113)` is included <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Even then, the deviation from pi is incredibly subtle <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## The Seemingly Unrelated Phenomenon: Moving Averages of Rectangular Functions

A satisfying explanation for this integral behavior comes from a seemingly unrelated phenomenon involving moving averages of functions <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Consider a "rect" function, `rect(x)`, defined as `1` if `x` is between `-1/2` and `1/2`, and `0` otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This is the first function in a sequence, `f1(x)` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

Each subsequent function in the sequence is a moving average of the previous one:
1.  `f2(x)` is a moving average of `f1(x)` using a sliding window of width `1/3` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. When the window is entirely over the plateau of `f1(x)` (where `f1(x)` is `1`), `f2(x)` also equals `1` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The length of `f2(x)`'s plateau will be `1 - 1/3` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  `f3(x)` is a moving average of `f2(x)` using a window of width `1/5` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Its plateau length will be `(1 - 1/3) - 1/5` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
3.  This continues, with each iteration using a window width of `1/k` where `k` is the next odd number (1/7, 1/9, etc.), causing the plateau to get thinner <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

The value of these functions at `x = 0` is observed <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Initially, `f1(0)`, `f2(0)`, `f3(0)`, and so on, all equal `1` because `x=0` is within their respective plateaus <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. However, this pattern breaks when the sum of the reciprocals of the odd numbers (`1/3 + 1/5 + 1/7 + ...`) grows to be greater than the initial plateau width of `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This happens at the iteration corresponding to `1/15` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, causing the plateau to become thinner than the window itself, and thus `f_n(0)` becomes slightly less than `1` <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

The value of this function at `x=0` drops by the exact same tiny factor that the integrals drop below pi <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This suggests a deep quantitative similarity between the two phenomena <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

For the case with the `2 cos(x)` term, which extended the integral pattern to `113`, the analogy is a `rect` function with an initial plateau length of `2` (from `-1` to `1`) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. It takes longer for the sum of reciprocals of odd numbers to exceed `2`, specifically until `1/113` is added <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## The Connection: [[introduction_to_fourier_transform | Fourier Transforms]] and [[fast_fourier_transform_and_convolution | Convolutions]]

The two phenomena are not just analogous; they are secretly the same, revealed through the machinery of [[introduction_to_fourier_transform | Fourier Transforms]] and [[fast_fourier_transform_and_convolution | Convolutions]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

To align the integral values, the `sinc(x)` function is substituted with `sinc(πx)` (often called the "engineer's sinc" function), which effectively squishes the graph horizontally by `π`, making its integral equal to `1` instead of `π` <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. The sequence of integrals then consistently equals `1` until it breaks <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

The core connection lies in these key properties:

1.  **[[introduction_to_fourier_transform | Fourier Transform]] of Sinc and Rect**: The `sinc(πx)` function is directly related to the `rect(x)` function via a [[introduction_to_fourier_transform | Fourier Transform]] <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. The [[introduction_to_fourier_transform | Fourier Transform]] acts as a rephrasing of a function's information into a different language, like looking at it from a new perspective <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
2.  **Integral as [[introduction_to_fourier_transform | Fourier Transform]] at Zero**: The integral of any function `f(x)` from negative infinity to infinity is equivalent to evaluating the [[introduction_to_fourier_transform | Fourier Transform]] of `f(x)` at `x=0` <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
    *   This directly explains the initial integral of `sinc(πx)`: `∫ sinc(πx) dx = FourierTransform(sinc(πx))(0) = rect(0) = 1` <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This provides a way to compute a tricky integral by simply evaluating a value in the transformed domain <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
3.  **The [[fast_fourier_transform_and_convolution | Convolution Theorem]]**: The product of two functions in one domain (e.g., multiplying `sinc` functions in the `x` domain) corresponds to the [[fast_fourier_transform_and_convolution | convolution]] of their respective [[introduction_to_fourier_transform | Fourier Transforms]] in the other domain <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. In this specific case, [[fast_fourier_transform_and_convolution | convolution]] operations directly correspond to the moving average process described with the `rect` functions <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

Therefore, the sequence of multiplying `sinc` functions and computing their integrals is equivalent to performing successive moving averages of `rect` functions and evaluating them at zero <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. This explains the observed stability of the value (the plateau) and why it eventually breaks when the cumulative effect of the "eating into" process (the sum of reciprocal widths) exceeds the initial "plateau" width <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Broader Implications

The [[fast_fourier_transform_and_convolution | Convolution Theorem]] and [[introduction_to_fourier_transform | Fourier Transforms]] are powerful tools because they offer a systematic shift in perspective, making difficult problems potentially easier to solve <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. For example, the [[fast_fourier_transform_and_convolution | convolution theorem]] also enables algorithms for very fast multiplication of large numbers <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.