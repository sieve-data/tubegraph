---
title: Fourier transforms and their applications in integral evaluation
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

A seemingly random sequence of computations involving integrals of `sinc` functions, which initially appears to follow a predictable pattern of equaling pi, eventually breaks, yielding a value just barely less than pi <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This peculiar phenomenon is explored through the lens of [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] and convolutions, revealing a deeply satisfying mathematical explanation <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## The Sinc Function and Its Mysterious Integrals

The central character in this mathematical mystery is the function `sinc(x)`, defined as `sine(x) / x` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This function is common in mathematics and engineering <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It can be visualized as a normal oscillating sine curve that is "squished down" as `x` moves away from zero due to multiplication by `1/x` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. At `x = 0`, where it appears as `0/0`, the function approaches `1`, so it's typically redefined as `sinc(0) = 1` to ensure continuity <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

The integral of `sinc(x)` from negative infinity to infinity, representing its signed area, surprisingly evaluates to exactly pi <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This result is not easily derived using standard calculus tools <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### The Sequence of Integrals

The peculiar pattern involves a sequence of integrals where increasingly stretched versions of the `sinc` function are multiplied together <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. For example, the next step involves multiplying `sinc(x)` by `sinc(x/3)`, which results in a more complicated wave <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Unexpectedly, the integral of this product also equals pi <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. The pattern continues, with each iteration adding a `sinc` function stretched by a new odd number (e.g., `sinc(x/5)`) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

Despite each term being progressively multiplied by something smaller than 1 (except at `x=0`), which would suggest the area should shrink <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, the integral remains exactly pi for many iterations <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The stability breaks when the stretching factor reaches `15`, at which point the integral becomes just barely less than pi <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This is a real phenomenon, not a numerical error, with the exact value being a complex fraction of pi <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

The pattern was described by Jonathan and David Borwein <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Even stranger, adding a factor of `2 cos(x)` to these integrals makes the pattern of equaling pi continue for much longer, breaking only at the number `113` by a minimal amount <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## An Analogous Phenomenon: Moving Averages and Plateaus

To understand this, an analogous phenomenon is introduced: a sequence of functions `f_n(x)` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

1.  **`rect(x)` Function**: The first function, `f1(x)`, is a rectangular pulse, `rect(x)`, which equals `1` between -1/2 and 1/2, and `0` otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
2.  **Moving Averages**: Each subsequent function `f_n(x)` is a moving average of the previous one, using a sliding window <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. For `f2(x)`, the window width is `1/3` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The value of `f_n(x)` at a given `x` is the average value of `f_(n-1)(x)` within the window centered at `x` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  **Plateau Shrinkage**: When the window is entirely within the previous function's plateau of `1`, the new function also equals `1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The length of this plateau shrinks with each iteration. For `f2(x)`, the plateau length is `1 - 1/3` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This continues, with `f3(x)` using a `1/5` window, `f4(x)` a `1/7` window, and so on, each time shrinking the plateau by the window's width <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The value of these functions at `x=0` is recorded <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Initially, it remains `1` because `x=0` is within the shrinking plateau <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. However, when the window width (`1/15` for the eighth iteration) becomes wider than the previous plateau, the value at `x=0` drops slightly below `1` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This occurs when the sum of the reciprocals of the odd numbers (`1/3 + 1/5 + ...`) first exceeds `1` <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

This pattern of `1, 1, 1, 1, 1, 1, 1`, then a slight drop, is analogous to the `pi, pi, pi, pi, pi, pi, pi` sequence of integrals <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The constant by which the moving average value falls short of 1 is precisely the factor by which the integral falls short of pi <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. When a `2 cos(x)` term is included in the integral, corresponding to starting with a `rect` function twice as wide (length 2), it takes longer for the plateau to disappear, explaining the `113` breakdown point <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## The Underlying Connection: Fourier Transforms and Convolutions

The seemingly disparate integral problem and moving average process are in fact two ways of computing the exact same thing <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. The connection lies in the use of [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] and convolutions <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

First, the original integral of `sinc(x)` (which equals pi) can be simplified by substituting `x` with `pi*x` <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This horizontal squishing makes the integral equal to exactly `1` <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This normalized function is sometimes called the "engineer's sinc function" <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Fourier Transform as a Translation

A [[introduction_to_fourier_transform | Fourier transform]] takes one function and produces another, essentially rephrasing the information of the original function in a "different language" or from a "new perspective" <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. It's often described as breaking down a function into a continuous integral of pure frequencies <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

Crucially, the `sinc` function (specifically, the normalized `sinc(pi*x)`) and the `rect` function are related by a [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. The [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] of `sinc(pi*x)` looks like the `rect` function <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Similarly, the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] of a stretched `sinc` function (e.g., `sinc(x/k)`) corresponds to a stretched and squished version of the `rect` function <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

One powerful fact in [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] theory is that computing the integral of a function from negative infinity to infinity is equivalent to evaluating its [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transformed]] version at the input zero <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This means the tricky integral of `sinc(x)` (or `sinc(pi*x)`) can be solved by evaluating its [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] (the `rect` function) at zero, which is simply `1` (or `pi` after undoing the normalization) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### The [[fast_fourier_transform_and_its_role_in_efficient_convolution | Convolution Theorem]]

The final piece of the puzzle is the [[fast_fourier_transform_and_its_role_in_efficient_convolution | convolution theorem]] <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This theorem states that if you take the product of two functions, and then take the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] of that product, it's equivalent to individually taking the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] of the original functions and then combining them using an operation called convolution <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

In the context of the `rect` functions, convolution precisely corresponds to the moving average process described earlier <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Therefore, the sequence of multiplying more and more `sinc` functions in the integral domain corresponds exactly to performing successive moving averages on the `rect` function in the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] domain <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. When combined with the fact that integrating in one context (the `sinc` function products) is equivalent to evaluating at zero in the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] context (the `rect` function's moving averages), the strange stability and subtle breakdown of the integrals are fully explained by the shrinking plateau of the moving average functions <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

This demonstrates how powerful tools like [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] can provide a systematic shift in perspective, making hard problems appear much simpler <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.