---
title: Graphing functions with discontinuities
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

The concept of a limit is fundamental to calculus, despite being a simple idea at its core <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. When [[graphical_representation_of_limits | graphing functions]], understanding limits is crucial, especially when dealing with discontinuities. Discontinuities occur at points where a function is undefined or behaves unexpectedly.

## Simple Discontinuity Example

Consider the function `f(x)` defined as `x - 1` divided by `x - 1` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>:

`f(x) = (x - 1) / (x - 1)`

While it might seem that `f(x)` simplifies to `1`, this simplification is not entirely true because the original function is undefined when `x` is equal to `1` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. If you try to [[evaluating_functions | evaluate]] `f(1)`, both the numerator and denominator become `0`, resulting in `0/0`, which is undefined <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

To accurately represent this function, you can state that `f(x) = 1` with the added constraint that `x` cannot be `1` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Graphing `f(x) = (x - 1) / (x - 1)`

When [[graphing linear equations | graphing this function]], it appears as a horizontal line at `y = 1` for all `x` values except `x = 1` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. At `x = 1`, there is a "gap" or a hole in the graph, signified by an open circle, indicating that the function is not defined at that specific point <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

<div style="border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; text-align: center;">
    <img src="https://i.imgur.com/example_graph1.png" alt="Graph of f(x) = (x-1)/(x-1) showing a hole at x=1, y=1" width="300"/>
    <p><i>Conceptual representation: A horizontal line at y=1 with a hole at x=1.</i></p>
</div>

### Function Evaluation vs. Limit

*   **Function Evaluation:** If asked "What is `f(1)`?", the answer is "undefined" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Limit:** If asked "What is the function approaching as `x` equals `1`?" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, this refers to the limit. As `x` gets infinitely closer to `1` from either side (but not actually at `1`), the function's value gets closer and closer to `1` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

> [!INFO] Limit Notation
> The limit as `x` approaches `1` of `f(x)` is written as:
> `lim (x→1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

This notation simply asks what value the function approaches as `x` gets arbitrarily close to a certain point <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Piecewise Function with Point Discontinuity

Let's consider a more complex function, `g(x)`, defined piecewise <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>:

`g(x) = x^2` when `x ≠ 2`
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>

This function demonstrates a discontinuity where the function's value at a specific point deviates from the value it approaches.

### Graphing `g(x)`

The graph of `g(x)` will primarily resemble the [[graphing a quadratic function | parabola]] `y = x^2` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. However, at `x = 2`, there's a discontinuity:
*   Instead of being at `y = 2^2 = 4`, the graph has a hole at `(2, 4)` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   The function's actual value at `x = 2` is `1`, so there's a distinct point at `(2, 1)` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

<div style="border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; text-align: center;">
    <img src="https://i.imgur.com/example_graph2.png" alt="Graph of g(x) showing a parabola with a hole at (2,4) and a point at (2,1)" width="300"/>
    <p><i>Conceptual representation: A parabola y=x^2 with a hole at (2,4) and a point at (2,1).</i></p>
</div>

### Function Evaluation vs. Limit for `g(x)`

*   **Function Evaluation:** `g(2)` is defined as `1` according to the function's definition <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Limit:** The limit as `x` approaches `2` of `g(x)` asks what `g(x)` is approaching as `x` gets closer and closer to `2` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Visually, as `x` approaches `2` along the parabolic curve, `g(x)` approaches `4` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

> [!NOTE] Limit vs. Value
> The limit asks what the function *approaches*, not what it *is* at that exact point <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
>
> `lim (x→2) g(x) = 4` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

### Numerical Approximation of Limits

You can also determine limits numerically by evaluating the function at values increasingly close to the point of interest. For `g(x)` as `x` approaches `2` <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>:

*   If `x = 1.9`, `g(1.9) = 1.9^2 = 3.61` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   If `x = 1.99`, `g(1.99) = 1.99^2 = 3.96` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
*   If `x = 1.999`, `g(1.999) = 1.999^2 = 3.996` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

And from the positive direction:
*   If `x = 2.1`, `g(2.1) = 2.1^2 = 4.41` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
*   If `x = 2.01`, `g(2.01) = 2.01^2 = 4.0401` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

Both approaches show that as `x` gets closer to `2`, `g(x)` gets closer to `4` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. This reinforces that the limit is `4`, even though the function's value at `x=2` is `1` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This concept is a key aspect of understanding [[applications_of_functions | how functions behave]] near points of discontinuity.