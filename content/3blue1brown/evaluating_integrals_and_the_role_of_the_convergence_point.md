---
title: Evaluating integrals and the role of the convergence point
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

Sometimes, mathematical sequences present patterns that seem to defy intuition, only to break at a specific point. One such sequence involves a series of integrals that, for a considerable time, all evaluate to exactly pi, before suddenly dropping to a value just slightly less than pi <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Sinc Function

The central character in this mathematical mystery is the function `sinc(x)`, defined as `sin(x) / x` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This function is commonly encountered in mathematics and engineering <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

Visually, `sinc(x)` starts with a normal oscillating sine curve, which is then "squished down" as `x` moves away from zero due to the multiplication by `1/x` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. At `x = 0`, directly plugging in the value would result in `0/0` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. However, using [[introduction_to_limits_in_calculus | limits]], as `x` approaches `0`, the function approaches `1` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. By redefining `sinc(0)` to be `1`, a smooth continuous curve is achieved <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### The Integral of Sinc(x)

The [[derivatives_and_integrals | integral]] of `sinc(x)` from negative infinity to positive infinity represents the signed area between the curve and the x-axis <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This means areas above the x-axis are added, and areas below are subtracted <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Surprisingly, this integral evaluates to exactly pi <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, a result not easily derived using standard [[antiderivatives_and_solving_integrals | calculus]] tools <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The Peculiar Integral Sequence

The initial sequence that mystifies observers begins with the integral of `sinc(x)` from negative infinity to infinity, which is pi. Subsequent steps involve multiplying `sinc(x)` by progressively stretched versions of itself, such as `sinc(x/3)`, `sinc(x/5)`, and so on, with the denominator being an increasing odd number <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

Despite these modifications creating increasingly complex waves with mass concentrated towards the middle <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, the integral of the resulting function continues to equal pi for several iterations <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This is counter-intuitive, as multiplying by `sinc(x/k)` (for k > 1) results in progressively smaller values for most `x` (except `x=0`), suggesting the area should decrease <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### The "Breaking" Point

The stability of the integral value, remaining at pi, persists for a surprising duration. However, it eventually "breaks" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. When a factor of `sinc(x/15)` is introduced, the integral's value drops to slightly less than pi <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This phenomenon, initially thought by some researchers to be a computer bug due to floating-point arithmetic <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>, was described in a paper by Jonathan and David Borwein <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The exact value of the integral when it breaks is a specific fraction of pi, with extremely large numerator and denominator <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

Even stranger, if an additional factor of `2cos(x)` is included in the integral, the pattern of equaling pi continues for much longer, breaking only when the `113` factor is introduced <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## An Analogous Phenomenon: Moving Averages

To explain this, a seemingly unrelated phenomenon is introduced: a sequence of functions `f_n(x)` starting with a "rect" function (`rect(x)`), which equals `1` for `x` between `-1/2` and `1/2` and `0` otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. Each subsequent function `f_{n+1}(x)` is a moving average of `f_n(x)`, using a sliding window whose width is the reciprocal of an odd number (e.g., `1/3`, `1/5`, `1/7`, etc.) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

When the sliding window is entirely within the plateau (where the function value is `1`), the average value remains `1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The length of this plateau shrinks with each iteration by the width of the averaging window <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. The value of `f_n(0)` (the function evaluated at `0`) remains `1` as long as the plateau extends across `0` <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### The Moving Average "Breaking" Point

The "break" in this analogy occurs when the sum of the reciprocals of the odd numbers (e.g., `1/3 + 1/5 + 1/7 + ...`) exceeds the initial plateau width (which is `1` for `rect(x)`) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. When the sum of these reciprocals reaches `1/15`, the accumulated reduction in plateau width causes the plateau to become thinner than the `1/15` window itself <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Consequently, the moving average at `x=0` drops slightly below `1` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This pattern, `1, 1, 1, 1, 1, 1, 1,` then "falls short" at the eighth iteration (corresponding to the `1/15` factor) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This is quantitatively the same as the factor by which the integral sequence drops below pi <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

Similarly, when the initial plateau length is `2` (as in the `2cos(x)` integral case), it takes longer for the sum of reciprocals to exceed the initial plateau length, specifically until `113` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

## The Connection: Fourier Transforms and Convolutions

The seemingly unrelated phenomena are, in fact, two sides of the same coin, linked by powerful mathematical tools: [[fourier_transforms | Fourier transforms]] and [[convolutions | convolutions]] <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

Firstly, the `sinc` function (specifically, `sin(πx)/πx`, often called the engineer's sinc function) is related to the `rect` function via a [[fourier_transforms | Fourier transform]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. A [[fourier_transforms | Fourier transform]] "rephrases" a function's information in a different domain, often making problems easier to analyze <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

One crucial fact is that the [[application_of_integrals_in_real_world_problems | integral]] of a function from negative infinity to infinity is equivalent to evaluating its [[fourier_transforms | Fourier transformed]] version at the input zero <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. For the `sinc` function, its [[fourier_transforms | Fourier transform]] is the `rect` function. Thus, the integral of `sinc(πx)/πx` from negative infinity to infinity is simply `rect(0)`, which is `1` <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>, <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. This explains the initial integral value.

Secondly, the [[convolution_theorem | convolution theorem]] states that the product of two functions in one domain corresponds to the [[convolutions | convolution]] of their individual [[fourier_transforms | Fourier transforms]] in the other domain <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. In this specific case, multiplying `sinc` functions in the integral context corresponds to performing [[convolutions | convolutions]] on their `rect` function counterparts <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. For these rectangular functions, a [[convolutions | convolution]] behaves exactly like the moving average process described earlier <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

Therefore, multiplying more `sinc` functions together and evaluating their [[application_of_integrals_in_real_world_problems | integrals]] is equivalent to repeatedly performing moving averages on the `rect` function and evaluating the result at zero <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. This provides a clear [[visual_intuition_in_calculus | visual intuition]] for why the value remains stable (the plateau remains at `1`) until the accumulated "eating away" of the plateau finally causes the function value at zero to drop <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

This sophisticated explanation highlights the power of [[fourier_transforms | Fourier transforms]] in providing a shift in perspective, transforming difficult problems into more manageable ones <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. The choice of `1/3`, `1/5`, `1/7` etc. was merely the sequence highlighted by the Borweins; any sequence of positive numbers whose sum ultimately exceeds the initial plateau width would cause the value to drop <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This phenomenon demonstrates the subtle nature of [[concept_of_infinite_sums_and_convergence | convergence]] and divergence in mathematical sequences.