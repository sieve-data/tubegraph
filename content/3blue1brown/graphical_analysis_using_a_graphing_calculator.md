---
title: Graphical analysis using a graphing calculator
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

A graphing calculator, such as Desmos, serves as a powerful tool for [[visualizing mathematical concepts|visualizing mathematical concepts]] and discovering non-trivial mathematical facts, even without prior knowledge of formal definitions <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. By interactively manipulating functions, one can gain significant intuition about their behavior and underlying relationships <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Exploring Trigonometric Functions Graphically

### The Cosine Function
Initially, one might encounter the cosine function in the context of sinusoidal waves in physics <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Plugging `cos(x)` into a graphing calculator reveals a cycling phenomenon relevant to wave dynamics <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Manipulating Inputs and Outputs**: Tweaking the input `x` by adding a constant (e.g., `cos(2x)`) squishes the graph, increasing its frequency <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Changing the output (e.g., `2*cos(x)`) stretches it in the y-direction <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Discovering the Identity of Cosine Squared
By squaring the cosine function, `cos(x)^2`, and observing its graph, a surprising pattern emerges <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Although squaring typically affects the y-direction, `cos(x)^2` transforms into another cosine wave that oscillates more quickly and is entirely positive <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

Through [[visual approach to math concepts|graphical experimentation]], it can be deduced that `cos(x)^2` is represented by the identity:
`cos(x)^2 = (1 + cos(2x)) / 2` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
This identity shows that squaring `cos(x)` results in a graph that is a scaled-down version of `cos(2x)` shifted upwards <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This discovery highlights a non-trivial fact about trigonometric functions that is not immediately obvious <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Uncovering Deeper Connections: Trigonometry and Exponentials

The behavior of `cos(x)^2` (where squaring the function affects the input's scaling) hints at a deeper connection to other functions <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Consider functions `f(x)` where `f(2x) = f(x)^2` <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Graphing options like `sqrt(1-x^2)`, `log(x)`, `x^2`, and `2^x` reveals that `2^x` satisfies this property <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

```
f(x) = 2^x
f(x)^2 = (2^x)^2 = 2^(2x)
f(2x) = 2^(2x)
Therefore, f(2x) = f(x)^2
```
This comparison suggests a potential relationship between cosine and exponential functions, hinting at the role of complex numbers in understanding trigonometry <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Visualizing Sine, Cosine, and Tangent

### Unit Circle Perspective
While traditionally introduced via right triangles, trigonometry is fundamentally about circles <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Sine (sin(θ))**: Represents the y-coordinate (height) as a point moves around a unit circle, starting from the rightmost side <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. The graph of `sin(x)` starts at zero and oscillates <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Cosine (cos(θ))**: Represents the x-coordinate (horizontal distance from the y-axis) as a point moves around a unit circle <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. The graph of `cos(x)` starts at one and oscillates <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Radians**: The input to trigonometric functions is typically in radians, which measures the arc length (distance walked) around a unit circle <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. For example, walking π units around the circle gets you halfway around <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

### The Tangent Function
The tangent function (`tan(θ) = opposite / adjacent`) can be geometrically interpreted as the length of a line segment tangent to the unit circle at (1,0), extending vertically to intersect the radial line <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.

Graphing `tan(x)` reveals distinct characteristics:
*   It starts at zero.
*   As the angle approaches π/2 (90 degrees), the value of tangent "blows up to infinity" <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>, as the adjacent side approaches zero <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a>.
*   This leads to vertical asymptotes at odd multiples of π/2 <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>.
*   The pattern repeats periodically.

## Conclusion

[[Visualizing mathematical concepts|Visualizing mathematical concepts]] through graphing calculators allows for an intuitive exploration of functions and the discovery of complex identities <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This [[visual approach to math concepts|visual approach to math concepts]] can precede formal definitions and even reveal subtle connections, such as the surprising relationship between `cos(x)^2` and `cos(2x)`, which hints at the link between trigonometry and exponential functions via [[visualizing mathematical operations using vector fields|complex numbers]] <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. These discoveries, often non-obvious, demonstrate the power of graphical analysis in building a deeper conceptual understanding <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.