---
title: Visual approach to math concepts
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

This article introduces a visual approach to understanding fundamental calculus concepts, aiming to make complex ideas intuitive and accessible.

## The Essence of Calculus: A Visual Journey

The goal of this series is to uncover the core ideas of calculus in a way that clarifies their origins and meanings through an all-around [[Visualizing mathematical concepts | visual approach]] <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. The intent is for the viewer to feel they "could have invented calculus themselves" <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>, by pondering ideas and drawing diagrams, making the truths seem reasonable to stumble upon <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. This emphasizes the [[Creative approaches in mathematical proofs | creative approaches]] and the [[role of visual reasoning in mathematical proofs | role of visual reasoning]] in mathematical discovery.

## Unveiling Core Ideas Through Geometry: Area of a Circle

The journey into calculus begins by deeply exploring a specific geometric problem: the area of a circle <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. Contemplating this problem visually can lead to a glimpse of three major calculus concepts: integrals, derivatives, and their inverse relationship <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. This demonstrates how [[visualizing mathematical concepts]] can aid in [[understanding difficult math problems]].

### Slicing the Circle into Concentric Rings

To find the area of a circle, one might consider slicing it into many concentric rings <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This approach respects the circle's symmetry, a principle often rewarded in mathematics <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

### Approximating Ring Area as a Rectangle

Each ring, with an inner radius `r` and a tiny thickness `dr`, can be imagined straightened out and approximated as a thin rectangle <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   The width of this rectangle is the circumference of the ring: `2πr` <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
*   The thickness is `dr`, representing a tiny difference in radius <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   The area of this approximate rectangle is `2πr * dr` <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

This approximation becomes increasingly accurate as `dr` gets smaller <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### Summing Ring Areas Visually

The areas of all these approximate rings can be visualized as thin, upright rectangles placed side by side along an axis representing `r` <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   Each rectangle has a thickness `dr` <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
*   The height of each rectangle at a given `r` is `2πr`, representing the circumference of the corresponding ring <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

This arrangement forms a [[Graphical intuition versus transformational understanding in calculus | graphical intuition]] under the graph of the function `y = 2πr`, which is a straight line with slope `2π` <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### From Approximation to Precision: The Integral Concept

As `dr` becomes smaller and smaller, the sum of the areas of these many rectangles approaches the exact area under the graph <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. In the case of `y = 2πr`, the area under the graph (from `r=0` to the circle's radius `R`) forms a triangle <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.

The area of this triangle (½ * base * height) is:
½ * `R` * `(2πR)` = `πR²` <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

This visual method precisely derives the formula for the area of a circle. This transition from an approximate sum to a precise area under a graph is a core concept in calculus, leading to the idea of an **integral** <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. Many problems in math and science, such as calculating distance from velocity, can be approximated by summing small quantities and then reframed as finding the area under a graph <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. An integral function, denoted `a(x)`, gives the area under a curve between a fixed point and a variable point `x` <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.

## Introduction to Derivatives: Measuring Sensitivity

While finding an integral directly can be difficult, examining how the area under a graph changes with a tiny nudge to the input reveals another key concept: **derivatives** <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

If we consider the area under a graph `y = x²`, and slightly increase `x` by `dx`, the resulting change in area (`da`) can be approximated by a thin rectangle <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.
*   This rectangle's height is `x²` <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
*   Its width is `dx` <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
*   So, `da ≈ x² * dx` <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

Rearranging this, the ratio `da / dx` (a tiny change in area divided by a tiny change in `x`) is approximately `x²` <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>. This approximation improves as `dx` gets smaller <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.

This ratio, `da/dx`, is called the **derivative** of `a(x)` <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. Loosely, a derivative measures how sensitive a function's output is to small changes in its input <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. There are many ways to [[Visualizing mathematical operations using vector fields | visualize a derivative]] depending on the function and how tiny nudges are considered <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

## The Fundamental Theorem of Calculus: Integrals and Derivatives as Inverses

The relationship observed between the area function `a(x)` and the original graph `x²` (where `da/dx = x²`) is fundamental. Once methods for computing derivatives are understood, one can reverse-engineer a function if its derivative is known <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.

This interconnectedness, where the derivative of a function representing the area under a graph gives back the function defining the graph itself, is known as the **Fundamental Theorem of Calculus** <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. It reveals that integrals and derivatives are inverse operations <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. This highlights the importance of [[spatial intuition in math]] and [[visual proofs and misconceptions in math | visual proofs]] in building a robust understanding of these concepts.