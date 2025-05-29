---
title: Integrals and derivatives
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

This article explores the fundamental concepts of [[relationship_between_integrals_and_derivatives | integrals]] and [[calculating_derivatives_and_their_applications | derivatives]], key components of calculus. The goal is to understand their origin and meaning through a visual approach, demonstrating how these ideas naturally emerge from geometric problems <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Uncovering Calculus through Geometry

The core ideas of calculus, including [[relationship_between_integrals_and_derivatives | integrals]], [[calculating_derivatives_and_their_applications | derivatives]], and their inverse [[relationship_between_integrals_and_derivatives | relationship]], can be glimpsed by deeply contemplating a specific geometric problem: the area of a circle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Approximating the Area of a Circle

To determine the area of a circle, one approach involves slicing it into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Each ring can be approximated as a thin rectangle when straightened out <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

The width of such a rectangle is the circumference of the ring, `2πr` (where `r` is its inner radius), and its thickness is a tiny difference in radius, denoted `dr` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Therefore, the approximate area of one ring is `2πr * dr` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This approximation improves as `dr` becomes smaller <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a> <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Visualizing Integration

These approximate rectangular areas can be visualized by placing them upright, side-by-side, along an axis representing the radius `r` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The height of each rectangle at a given `r` is `2πr`, which is the circumference of the corresponding ring <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This setup forms a collection of rectangles under the graph of `y = 2πr`, a straight line with a slope of `2π` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a> <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

As the thickness `dr` decreases, the sum of these rectangular areas, which approximates the circle's area, approaches the exact area under the graph of `y = 2πr` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. For a circle with radius `R`, this area under the graph from `r=0` to `r=R` is a triangle with base `R` and height `2πR` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a> <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Its area is `½ * base * height = ½ * R * (2πR) = πR²`, which is the correct formula for the area of a circle <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a> <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

This process demonstrates how a sum of many small quantities (`2πr * dr`) can be reframed as finding the area under a graph, leading to the concept of [[visualizing_integration_and_approximations | integrals]] <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a> <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. An [[visualizing_integration_and_approximations | integral]] is a function `A(x)` that gives the area under a given curve (e.g., `x²`) between a fixed point and a variable point `x` <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a> <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. Many practical problems in math and science, such as calculating distance traveled from velocity, can be solved by finding the area under a graph, thus becoming [[visualizing_integration_and_approximations | integral]] problems <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a> <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## Discovering Derivatives

While finding an [[visualizing_integration_and_approximations | integral]] directly can be challenging <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, considering how the area under a curve changes with a small nudge to `x` reveals a crucial relationship. If `A(x)` is the area under a graph (e.g., `x²`), a tiny increase `dx` in `x` results in a tiny change `dA` in the area <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a> <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. This `dA` can be approximated as a thin rectangle with height `x²` (the function's value at `x`) and width `dx` <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a> <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

This implies that `dA` is approximately `x² * dx`, or `dA / dx` is approximately `x²` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a> <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This approximation becomes more accurate as `dx` gets smaller <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

This ratio `dA / dx` is known as the [[computing_derivatives_of_functions | derivative]] of `A(x)` <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. More precisely, the [[computing_derivatives_of_functions | derivative]] is the value this ratio approaches as `dx` approaches zero <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. Loosely, a [[calculating_derivatives_and_their_applications | derivative]] measures how sensitive a function's output is to small changes in its input <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## The Fundamental Theorem of Calculus

The observed [[relationship_between_integrals_and_derivatives | relationship]] — that the [[computing_derivatives_of_functions | derivative]] of an area function (`A(x)`) gives back the original function (`x²`) defining the curve — is the essence of the [[relationship_between_integrals_and_derivatives | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a> <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. This theorem ties together the two major concepts of [[visualizing_integration_and_approximations | integrals]] and [[calculating_derivatives_and_their_applications | derivatives]], demonstrating that they are inverse operations of each other <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a> <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Once proficient with [[computing_derivatives_of_functions | computing derivatives]], one can reverse-engineer a function if its [[computing_derivatives_of_functions | derivative]] is known, thereby solving [[visualizing_integration_and_approximations | integral]] problems <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a> <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a> <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This means finding the [[understanding_antiderivatives_in_calculus | antiderivative]] of a function.