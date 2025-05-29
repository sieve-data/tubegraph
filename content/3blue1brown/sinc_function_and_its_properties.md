---
title: Sinc function and its properties
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

The sinc function, defined as `sine(x) / x`, is a mathematical function that appears commonly in mathematics and engineering <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It is also referred to as the "engineer sinc function" when a factor of pi is included in the argument, becoming `sine(pi*x) / (pi*x)`, which has an area under its curve equal to 1 <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

## Characteristics of the Sinc Function

The sinc function can be visualized as a normal oscillating sine curve that is "squished down" as `x` moves away from zero by being multiplied by `1/x` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

At `x = 0`, the function appears to be `0/0` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. However, for values closer and closer to zero, the function approaches `1` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. By redefining the sinc function at `0` to equal `1`, it becomes a continuous curve <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Integral of the Sinc Function

The integral of `sine(x) / x` from negative infinity to infinity, representing the signed area between the curve and the x-axis, evaluates to exactly [[pi]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This result is unexpected and not easily approached with standard calculus tools <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The Borwein Integrals Phenomenon

A sequence of computations involving the sinc function exhibits a peculiar pattern:
1.  The integral of `sinc(x)` (i.e., `sine(x)/x`) from negative infinity to infinity equals [[pi]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Multiplying `sinc(x)` by a stretched version, `sinc(x/3)`, and integrating, also results in [[pi]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This is surprising, as multiplying functions usually changes the area <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
3.  Continuing this pattern by multiplying by `sinc(x/5)`, `sinc(x/7)`, and so on (stretched by odd numbers), the integral continues to equal [[pi]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
4.  This pattern breaks when the next factor is `sinc(x/15)` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The integral becomes slightly less than [[pi]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This is a real phenomenon, not a numerical error <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

This pattern was described by Jonathan and David Borwein in a paper, leading to initial assumptions of a computer bug due to its counter-intuitive nature <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

#### Variation with `2 cos(x)`

If an additional factor of `2 cos(x)` is included in the integral, the pattern of equaling [[pi]] continues for much longer, breaking only when the last factor corresponds to the number `113` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Even then, the deviation from [[pi]] is extremely subtle <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Generalization

The phenomenon is not exclusive to reciprocals of odd numbers (1/3, 1/5, 1/7, etc.) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. If any sequence of positive numbers is used for the stretching factors in the sinc functions, the integral will equal [[pi]] as long as the sum of those numbers is less than 1 <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. As soon as their sum exceeds 1, the expression drops slightly below [[pi]] <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Connection to Moving Averages

The behavior of the Borwein integrals can be understood through an analogous process involving moving averages of a simple rectangular function, `rect(x)` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

### The `rect(x)` Function

`rect(x)` is defined as `1` if `x` is between `-1/2` and `1/2`, and `0` otherwise <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Sequence of Moving Averages

A sequence of functions, `f_n(x)`, is created where each new function is a moving average of the previous one <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The window widths for these averages are `1/3`, `1/5`, `1/7`, and so on, mirroring the odd number denominators in the sinc integral sequence <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

When evaluating `f_n(0)`:
*   Initially, for `f1(0)`, `f2(0)`, etc., the value is `1` because the center of the plateau remains `1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   The length of the plateau for `f_n(x)` is `1 - (1/3 + 1/5 + ... + 1/(2n+1))` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   This plateau shrinks with each iteration <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   The pattern breaks when the sum of the reciprocals (`1/3 + 1/5 + ...`) becomes greater than `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This happens when the last fraction added is `1/15` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. At this point, the plateau is thinner than the moving average window, causing `f_n(0)` to be slightly less than `1` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

The value of `f_n(0)` in this moving average process is exactly the factor that multiplies [[pi]] in the corresponding sinc integral <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

For the case with `2 cos(x)` in the integral, the analogous starting function in the moving average process would have an initial plateau of length `2` instead of `1` <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. It takes longer for the sum of reciprocals to exceed `2`, specifically until the number `113` is reached, which matches the integral's breaking point <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Deep Mathematical Explanation

The underlying connection between the sinc function integrals and the moving averages lies in two powerful mathematical tools: [[Fourier transforms]] and [[convolution]]s <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Fourier Transform Relationship

The `sinc` function (with `pi*x` as its argument) is related to the `rect` function via a [[Fourier transform]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   A [[Fourier transform]] takes a function and "rephrases" its information in a different language, often making questions about the function easier to answer <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   The [[Fourier transform]] of the sinc function (with `pi*x`) is the `rect` function <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   Conversely, for symmetric functions, the [[Fourier transform]] is its own inverse <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
*   Transforming a horizontally stretched `sinc` function (stretched by a factor `k`) results in a stretched and squished version of the `rect` function <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Integral as Fourier Transform at Zero

A key property of [[Fourier transform]]s is that the integral of a function from negative infinity to infinity is equivalent to evaluating its [[Fourier transform]] at the input `0` <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   This explains why the integral of `sinc(pi*x)` is `1` (which implies the integral of `sinc(x)` is [[pi]]) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. The integral is equivalent to `rect(0)`, which is `1` <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### Convolution Theorem

The [[convolution]] theorem states that the product of two functions in one domain corresponds to the [[convolution]] of their individual [[Fourier transform]]s in the other domain <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   In the context of the `rect` functions, a [[convolution]] operation behaves exactly like the moving average process described earlier <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   Therefore, multiplying more and more sinc functions together (which are in the "Fourier domain") can be interpreted as performing progressive moving averages on their corresponding `rect` functions (in the "original domain") <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   Combined with the fact that integrating in one domain is equivalent to evaluating the [[Fourier transform]] at zero in the other, this provides a "lovely intuition" for why the stable values are observed before the eventual breakdown as the plateaus shrink <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

This [[connection_between_trigonometry_and_complex_numbers | shift in perspective]] offered by [[Fourier transforms]] and the [[convolution]] theorem simplifies otherwise tricky problems and reveals deeper connections between seemingly disparate mathematical phenomena <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.