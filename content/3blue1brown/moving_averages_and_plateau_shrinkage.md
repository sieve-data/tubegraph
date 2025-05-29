---
title: Moving averages and plateau shrinkage
videoId: 851U557j6HE
---

From: [[3blue1brown]] <br/> 

Sometimes the universe presents patterns in mathematics that seem random yet predictable, like a sequence of computations that consistently equal pi before subtly breaking the pattern <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores a phenomenon involving integrals of the sinc function and reveals its connection to a seemingly unrelated process of repeated moving averages and the shrinkage of plateaus.

## The Sinc Function and its Integral

The main function involved in this phenomenon is the sinc function, defined as `sine(x) / x` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This function is commonly encountered in math and engineering <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It can be visualized as an oscillating sine curve that is "squished down" as `x` gets further from zero by multiplying it by `1/x` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

At `x = 0`, where it appears as `0/0`, the function approaches `1` <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Redefining `sinc(0)` to `1` creates a continuous curve <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

The integral of the sinc function from negative infinity to infinity (representing the signed area under the curve) remarkably evaluates to exactly pi <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This result is both "nice and also a little weird," and not easily approached with standard calculus tools <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## The Integral Sequence: A Stable Pattern

The puzzling sequence of computations begins with this base integral <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Subsequent steps involve multiplying the sinc function by stretched versions of itself. For example:
*   The first step is the integral of `sinc(x)` (equals pi) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   The next step involves multiplying `sinc(x)` by `sinc(x/3)` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Stretching `sinc(x)` by a factor of 3 horizontally by plugging in `x/3` would normally significantly alter the area, but this integral *also* equals pi <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   The sequence continues by multiplying in `sinc(x/5)`, `sinc(x/7)`, and so on, with new odd numbers <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Each of these integrals remarkably equals pi <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

This pattern, where the integral remains `pi` despite additional factors, continues for a surprisingly long time <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. However, it eventually breaks when the number `15` is introduced in the denominator of the last sinc factor. At this point, the value becomes "just barely, barely less than pi" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The exact value is a fraction of pi with extremely large numerator and denominator, confirming it's not a numerical error <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

This phenomenon was described by Jonathan and David Borwein, with a fellow researcher initially suspecting a bug in their computer algebra system <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

An even stranger extension of this pattern occurs when an additional `2 * cosine(x)` term is included in the integral. This causes the pattern to continue equaling pi for much longer, only breaking when the number `113` is introduced, and again by an "absolutely subtle amount" <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Moving Averages and Plateau Shrinkage

The explanation for this puzzle lies in a seemingly unrelated phenomenon involving [[integration_and_averaging_continuous_variables | moving averages]] and the shrinking of a plateau.

### The Rect Function

Consider a function called `rect(x)`, defined as `1` if `x` is between `-1/2` and `1/2`, and `0` otherwise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This is the first function in a sequence, `f1(x)` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Iterative Moving Averages

Each new function in the sequence is a [[integration_and_averaging_continuous_variables | moving average]] of the previous one:
*   **f2(x):** Defined by taking a sliding window of width `1/3` and averaging the values of `f1(x)` within that window <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   When the window is entirely over `f1(x)`'s plateau (where values are `1`), `f2(x)` also equals `1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   The length of `f2(x)`'s plateau is `1 - 1/3` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The value of `f2(0)` is `1` because `0` is within this plateau <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Subsequent Iterations:** For the next iteration, a moving average is taken with a window width of `1/5`, then `1/7`, and so on, corresponding to the odd numbers in the integral sequence <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
    *   Each iteration further smooths the function and reduces the width of the central plateau <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The length of the plateau at each step is the previous length minus the current window width <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   Crucially, the value of the function at `x = 0` remains `1` as long as `0` is within the shrinking plateau <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### The Break Point

This process continues until the iteration where the window width is `1/15` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. At this point, the sum of the reciprocals of the odd numbers `(1/3 + 1/5 + ...)` becomes greater than `1` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This means the cumulative reduction in plateau width has caused the plateau to become thinner than the window itself, or even disappear entirely <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. As a result, the moving average at `x = 0` will no longer be `1`, but "ever so slightly smaller than 1" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

The values at `f(0)` form a sequence: `1, 1, 1, 1, 1, 1, 1`, and then, by the eighth iteration (which incorporates `1/15`), it falls "ever so slightly" short of `1` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

## The Deep Connection: Fourier Transforms and Convolutions

The two phenomena – the stable sinc integral sequence and the stable moving average sequence – are not just analogous but "quantitatively the same" <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The constant by which the integral falls short of pi is exactly the constant by which the moving average function at `x=0` falls short of `1` <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

The connection is explained through two advanced mathematical concepts:
1.  **Fourier Transforms:** The sinc function (specifically, `sinc(pi*x)`) is directly related to the `rect` function via a Fourier transform <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
    *   A Fourier transform rephrases a function's information in a "different language," often making problems easier <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    *   A key property is that integrating a function from negative infinity to infinity is equivalent to evaluating its Fourier transform at `x = 0` <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This explains why the initial integral of `sinc(pi*x)` is `1` (because `rect(0)` is `1`) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

2.  **Convolutions (The Convolution Theorem):** The product of two functions in one domain corresponds to their convolution in the Fourier domain <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
    *   In the specific case of these rectangular functions, a convolution operation mathematically *looks like* the [[integration_and_averaging_continuous_variables | moving averages]] that were performed earlier <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

Therefore, multiplying more and more sinc functions together (which is integration in the original domain) corresponds to progressively applying moving averages to the `rect` function and evaluating the result at `x = 0` in the Fourier domain <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. This provides a "lovely intuition" for why the value remains stable for so long before breaking down as the plateau's edges "inch closer and closer to the center" <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

The extended pattern with `2 * cosine(x)` that breaks at `113` corresponds to starting with an initial `rect` function with a longer plateau (length `2` instead of `1`), which takes longer for the `1/k` sum to exceed `2` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

This demonstrates how powerful tools like Fourier transforms can offer a shift in perspective, making "hard problems sometimes look easier" <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. The convolution theorem itself has wide-ranging applications, including algorithms for rapidly computing the product of large numbers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.