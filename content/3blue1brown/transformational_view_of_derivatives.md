---
title: Transformational View of Derivatives
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

Traditional introductions to [[introduction_to_derivatives_and_calculus_concepts | calculus]] often present visual intuitions primarily based on graphs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. While this approach is effective for functions with numerical inputs and outputs, it can create a conceptual hurdle when generalizing [[understanding the meaning and computation of derivatives | derivatives]] beyond such simple cases <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The transformational view offers an alternative perspective that integrates more seamlessly into advanced topics like multivariable [[calculus]] and complex analysis <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Standard Graphical Intuition

In a typical [[calculus]] course, the [[understanding the meaning and computation of derivatives | derivative]] of a function is introduced as the slope of its graph <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This means the [[understanding the meaning and computation of derivatives | derivative]] is a new function that returns the slope for every input `x` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. However, it's encouraged to think of the [[understanding the meaning and computation of derivatives | derivative]] more fundamentally as a measure of how sensitive a function is to small changes around the input, with slope being just one way to visualize this sensitivity <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## The Transformational View

The core idea behind the transformational view of the [[understanding the meaning and computation of derivatives | derivative]] is to visualize a function as mapping input points on one number line to their corresponding outputs on a different number line <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. In this context, the [[understanding the meaning and computation of derivatives | derivative]] provides a measure of how much the input space gets stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

Specifically, if you zoom in on a small cluster of evenly spaced points around a particular input, the [[understanding the meaning and computation of derivatives | derivative]] at that input tells you how spread out or contracted those points become after the function maps them <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The closer you zoom in, the more this local behavior resembles multiplication by a constant factor <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Examples with the function x²

Consider the function `f(x) = x²`:
*   **Derivative = 2 (at `x=1`)**: Around the input `x=1`, a small neighborhood of points gets stretched out by a factor of 2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This is what it means for the [[understanding the meaning and computation of derivatives | derivative]] of `x²` at `x=1` to be 2 <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Derivative = 6 (at `x=3`)**: A neighborhood of points around `x=3` gets stretched out by a factor of 6 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Derivative < 1 (at `x=1/4`)**: Around `x=1/4`, a small region tends to get contracted by a factor of 1/2 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Derivative = 0 (at `x=0`)**: As you zoom in on `x=0`, a small neighborhood of points around it appears to collapse into 0 itself <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This indicates the local behavior increasingly resembles multiplication by 0 <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Negative Derivative (at `x=-2`)**: For negative inputs like `x=-2`, points in a small neighborhood not only get stretched out but also get flipped around <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The action resembles multiplication by a negative factor, for example, negative 4 around `x=-2` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

This view focuses solely on the local behavior of the function, which is particularly relevant for [[understanding the meaning and computation of derivatives | derivatives]] <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Application: Stability of Fixed Points in Infinite Fractions

The transformational view is highly useful for analyzing the stability of fixed points, such as those found in infinite fractions.

### The Infinite Fraction Problem
Consider the infinite fraction `1 + 1/(1 + 1/(1 + ...))` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This expression can be evaluated by setting it equal to `x` and noticing that a copy of the full fraction appears within itself, leading to `x = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This means finding the fixed points of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Solving `x = 1 + 1/x` yields two solutions:
1.  **The golden ratio (`phi`)**: Approximately 1.618 <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  **`phi`'s little brother**: Approximately -0.618, which is equivalent to `-1/phi` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

A question arises: Is the infinite fraction also equal to `phi`'s little brother? <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>

To understand this, one way to define the infinite fraction is as a limiting process: starting with a constant (e.g., 1) and repeatedly applying the function `f(x) = 1 + 1/x`, then observing what the series approaches <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

When this process is performed with a calculator, starting with any random number (even a negative one), the repeated application of `1 + 1/x` consistently converges to `phi` (1.618) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Even numbers very close to `phi`'s little brother tend to move away from it and converge to `phi` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Graphical Analysis (Spiderweb Plot)
A common way to analyze repeated function application graphically is the "spiderweb plot" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. This involves:
1.  Starting with an input `x` on the x-axis, moving vertically to the function's graph `y=f(x)`.
2.  Moving horizontally from the graph to the line `y=x`.
3.  Moving vertically back to the function's graph.
4.  Repeating the process <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

This method can show convergence or divergence from fixed points, and the conditions for stability are related to slopes <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### Transformational View of Fixed Point Stability

The transformational view provides a more intuitive understanding of fixed point stability <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. When repeatedly applying the function `f(x) = 1 + 1/x` in this view:
*   **Around `phi` (1.618)**: A neighborhood of points around `phi` gets contracted towards `phi` during each application <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This indicates that the [[understanding the meaning and computation of derivatives | derivative]] of `f(x)` at `x=phi` has a magnitude less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This "scrunching" behavior makes `phi` a **stable fixed point**, acting like a gravitational pull <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Around `phi`'s little brother (-0.618)**: Conversely, in the neighborhood of `phi`'s little brother, the [[understanding the meaning and computation of derivatives | derivative]] has a magnitude greater than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Points near this fixed point are repelled away from it, meaning the neighborhood gets stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This makes `phi`'s little brother an **unstable fixed point** <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

In summary, the stability of a fixed point is determined by whether the magnitude of its [[understanding the meaning and computation of derivatives | derivative]] is less than or greater than 1 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This explains why `phi` is always observed in numerical iterations, while `phi`'s little brother is not <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

> [!NOTE] Practicality
> While the transformational view can be less practical or "clunky" for visualizing an entire function compared to traditional graphs <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>, its flexibility and ability to generalize to more complex scenarios make it a valuable perspective that deserves more attention in introductory [[calculus]] courses <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. It significantly enhances the understanding of [[understanding the meaning and computation of derivatives | derivatives]] for advanced topics <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.