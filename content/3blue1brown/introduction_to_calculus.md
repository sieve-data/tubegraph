---
title: Introduction to calculus
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

This article introduces the core concepts of calculus, emphasizing a visual approach and aiming for an intuitive understanding rather than rote memorization <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. The goal is to make the subject feel discoverable, as if one could have "invented calculus" oneself <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## The Essence of Calculus: A Visual Approach

The series begins by exploring how one might "stumble into" the core ideas of calculus by deeply contemplating a specific geometry problem: the area of a circle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Starting with the Area of a Circle

The familiar formula for the area of a circle is $\pi r^2$, but understanding *why* this formula holds can reveal fundamental calculus concepts <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Contemplating this problem can lead to insights into [[understanding_antiderivatives_in_calculus | integrals]], [[intuition_behind_calculus_rules | derivatives]], and their inverse relationship <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

#### Slicing into Concentric Rings

One approach to finding a circle's area is to slice it into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This method respects the circle's symmetry, which math often rewards <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

#### Approximating Rings as Rectangles

An individual ring, with inner radius `r` and a small thickness, can be imagined "straightened out" and approximated as a thin rectangle <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   The width of this rectangle is approximately the circumference of the ring: `2πr` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   The thickness is denoted as `dr`, representing a "tiny difference in the radius" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   The approximate area of this unwrapped ring is `2πr * dr` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

This approximation becomes increasingly accurate as `dr` gets smaller <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

#### Summing Ring Areas as Area Under a Graph

The sum of the areas of all these approximated rings (ranging from `r=0` to the circle's full radius, e.g., 3) can be visualized <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. If each rectangular approximation is placed upright side-by-side, with thickness `dr` and height `2πr`, they form a shape under the graph of the function `y = 2πr` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

This graph of `y = 2πr` is a straight line with a slope of `2π` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The sum of the rectangle areas represents the area under this graph <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. For a circle with radius `R`, the area under this graph from `r=0` to `R` is a triangle with base `R` and height `2πR` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   Area = `(1/2) * base * height` = `(1/2) * R * (2πR)` = `πR^2` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

#### From Approximation to Precision

The transition from an approximate sum to a precise answer is a key insight of calculus <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. As the chosen `dr` becomes smaller and smaller, the sum of the rectangular areas (which approximates the original problem) approaches the exact area under the graph <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This means the precise answer to the original problem is exactly the area under the graph <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

Many problems in math and science, such as calculating distance traveled from velocity data, can be similarly broken down into sums of small quantities that approximate the area under a graph <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## [[understanding_antiderivatives_in_calculus | Integrals]]: Area Under a Curve

The insight gained from the circle problem leads to considering how to find the area under other, more complex graphs, like the graph of `y = x^2` (a parabola) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

A function `a(x)` that gives the area under a graph (e.g., `x^2`) between a fixed point (like 0) and a variable right endpoint `x` is called an [[understanding_antiderivatives_in_calculus | integral]] of `x^2` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Finding this integral function is generally challenging <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## [[intuition_behind_calculus_rules | Derivatives]]: Measuring Sensitivity to Change

When grappling with a hard problem like finding an integral, it's beneficial to play around with the ideas <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Consider the area function `a(x)` under the `x^2` graph:
*   If `x` is slightly increased by a tiny nudge `dx`, the resulting change in area (`da`) can be approximated by a thin rectangle <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   This rectangle's height is `x^2` and its width is `dx`, so `da` is approximately `x^2 * dx` <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   Rearranging, the ratio `da / dx` (a tiny change in `a` divided by the tiny change in `x` that caused it) is approximately `x^2` <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This approximation improves as `dx` gets smaller <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

This ratio, `da / dx`, is called the [[intuition_behind_calculus_rules | derivative]] of `a` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. More technically, the [[intuition_behind_calculus_rules | derivative]] is what this ratio approaches as `dx` becomes infinitesimally small <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. Loosely, a [[intuition_behind_calculus_rules | derivative]] measures how sensitive a function is to small changes in its input <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## The [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]]: Linking Integrals and Derivatives

[[intuition_behind_calculus_rules | Derivatives]] are crucial for solving [[understanding_antiderivatives_in_calculus | integral]] questions (finding the area under a curve) <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. If you know that the [[intuition_behind_calculus_rules | derivative]] of an unknown function `a(x)` is `x^2`, you can "reverse engineer" what `a(x)` must be <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

This inverse relationship—where the [[intuition_behind_calculus_rules | derivative]] of a function representing the area under a graph gives back the function defining the graph itself—is known as the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. It ties together the two major ideas of [[understanding_antiderivatives_in_calculus | integrals]] and [[intuition_behind_calculus_rules | derivatives]], showing them as inverses of each other <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

This initial exploration provides a high-level glimpse into the core ideas that emerge in calculus <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The series aims to delve into the details of [[intuition_behind_calculus_rules | derivatives]], [[understanding_antiderivatives_in_calculus | integrals]], and more, always encouraging the viewer to feel capable of having invented calculus themselves <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.