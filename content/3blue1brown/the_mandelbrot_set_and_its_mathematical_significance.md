---
title: The Mandelbrot set and its mathematical significance
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

The [[Mandelbrot set and its mathematical significance | Mandelbrot set]] is an iconic shape and a "poster child of math" that arises from the field of holomorphic dynamics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This field studies what happens when complex functions are repeatedly applied <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Holomorphic Dynamics: The Core Concept

Holomorphic dynamics involves functions with complex number inputs and outputs that are also differentiable <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Geometrically, being differentiable in this context means that when zoomed in near a point, the function's behavior looks approximately like scaling and rotating (multiplying by a complex constant) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This includes common functions like polynomials, exponentials, and trigonometric functions <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The "dynamics" refers to the process of repeatedly applying one of these functions: evaluating on an input, then evaluating the same function on the output, and so on <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The resulting sequence of points can exhibit various behaviors:
*   **Cycles**: The pattern of points gets trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Limiting points**: The sequence approaches a specific point, including "the point at infinity" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Chaotic behavior**: No apparent pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

When these behaviors are visualized, they often result in intricate [[Fractal dimension and its implications | fractal]] patterns <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. An example of this is [[Newtons fractal and its relation to polynomials | Newton's fractal]], which arises from iterating a rational function <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Defining the [[Mandelbrot set and its mathematical significance | Mandelbrot Set]]

The most popular example of a rational function studied in this context is `z² + c`, where `c` is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The [[Mandelbrot set and its mathematical significance | Mandelbrot set]] is constructed by considering `c` as a changeable parameter, while always starting the iterative process with an initial value of `z = 0` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

The iterative process is:
1.  Start with `z₀ = 0`.
2.  `z₁ = z₀² + c = c` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
3.  `z₂ = z₁² + c = c² + c` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>
4.  And so on, `z_n+1 = z_n² + c` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The set is then visualized by coloring points in the complex plane based on the behavior of this iteration for different values of `c`:
*   Points where the process remains bounded (does not "blow up") are colored black <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. (If the value gets as big as 2, it will blow up to infinity <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.)
*   Divergent values are assigned a gradient of colors based on how quickly they rush off to infinity <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

This results in the iconic image of the [[Mandelbrot set and its mathematical significance | Mandelbrot set]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. It functions as a "parameter space" because each pixel corresponds to a unique function determined by the parameter `c` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Interpreting the Mandelbrot Set's Features

The different sections of the [[Mandelbrot set and its mathematical significance | Mandelbrot set]] represent specific dynamic behaviors:
*   The largest cardioid section (main body) includes values of `c` where the process eventually converges to some limit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This corresponds to when at least one of the function's fixed points is attracting <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   The large circle on the left indicates values where the process gets trapped in a cycle between two values <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Smaller circles, like the top and bottom ones, show values where the process gets trapped in cycles of three values, and so on <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Relation to [[Mathematical concepts related to Newtons fractal | Julia Sets]]

While the [[Mandelbrot set and its mathematical significance | Mandelbrot set]] is a parameter space (tweak `c`, fix `z₀`), [[Mathematical concepts related to Newtons fractal | Julia sets]] are formed by fixing `c` and letting the pixels represent different initial seed values (`z₀`) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. These images, often called [[Mathematical concepts related to Newtons fractal | Julia fractals]], also color pixels black if the process remains bounded, and use gradients for divergent values <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

It's important to note that the term "[[Mathematical concepts related to Newtons fractal | Julia set]]" refers specifically to the boundaries of these regions, not the interior black regions <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Stability and Attracting Cycles

A key concept in understanding these dynamics is "stability" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   A fixed point (`f(z) = z`) is **attracting** if nearby points tend to get drawn towards it <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   It's **repelling** if nearby points are pushed away <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

This stability can be computed using the function's derivative at the fixed point <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>:
*   If the absolute value of the derivative is less than 1, it's an attracting fixed point <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   If the absolute value is greater than 1, it's a repelling fixed point <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

Cycles can also be attracting or repelling. An attracting cycle means a neighborhood of points around a value from that cycle tends to get pulled in <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. For the [[Mandelbrot set and its mathematical significance | Mandelbrot set]], the fact that we only use `z = 0` as a seed value is sufficient because of a theorem by Fatou, which states that if a rational map has an attracting cycle, at least one of the values where the derivative of the iterated function equals zero must fall into that cycle <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This means if a stable cycle exists, the `z=0` seed value will find it <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

### The Mandelbrot Set's Universal Appearance

The appearance of the [[Mandelbrot set and its mathematical significance | Mandelbrot set]] is not exclusive to the `z² + c` function <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. It can be found in parameter spaces for other dynamic systems, for instance, when visualizing which cubic polynomials have attracting cycles for [[Mathematical concepts related to Newtons fractal | Newton's method]] <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. This suggests that the [[Mandelbrot set and its mathematical significance | Mandelbrot set]] relates to a more general and universal property of parameter spaces in such iterative processes <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

## Why Fractals? The Link Between Chaos and Complexity

The intricate fractal boundaries in these diagrams are a result of the inherent chaotic behavior of points in the [[Mathematical concepts related to Newtons fractal | Julia set]] <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

*   **Fatou Set**: Points that eventually fall into some stable, predictable pattern are part of the Fatou set <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. A small disc around a point in the Fatou set will eventually shrink as it falls into stable behavior <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **[[Mathematical concepts related to Newtons fractal | Julia Set]]**: This is everything else; the rough boundaries between colored regions <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. Points in the [[Mathematical concepts related to Newtons fractal | Julia set]] tend to behave chaotically, meaning their nearby neighbors will eventually fall into qualitatively different behaviors <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

A key result known as the "stuff-goes-everywhere principle" (a corollary to Montel's theorem) states that if you draw a small disc around a point on the [[Mathematical concepts related to Newtons fractal | Julia set]], it tends to expand over time and eventually hits almost every point on the complex plane <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. This principle implies that if there are three or more attracting behaviors, the [[Mathematical concepts related to Newtons fractal | Julia set]] cannot be smooth; it must be complicated and fractal-like <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. This highlights a deep, logical link between chaos and the generation of fractals <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.