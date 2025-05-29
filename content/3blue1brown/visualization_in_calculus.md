---
title: Visualization in calculus
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

[[Visualization in calculus | Visualization]] is a core component of understanding calculus, aiming to reveal the origin and meaning of its concepts rather than presenting them as formulas to be memorized <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. The goal of a visual approach is to make it feel as though one could have "invented calculus" themselves by "drawing out the right diagrams" and exploring ideas in a specific way <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>.

## Uncovering Core Calculus Ideas Through Geometry

Fundamental concepts in [[fundamental_concepts_of_calculus | calculus]] can be glimpsed by deeply considering specific geometric problems <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. For example, exploring the area of a circle can lead to understanding integrals, derivatives, and their inverse relationship <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

### Area of a Circle: A First Glimpse of Integrals

To find the area of a circle (e.g., with radius 3), one might try slicing it into many concentric rings <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This approach respects the circle's symmetry, which is often rewarded in mathematics <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

Each ring, with an inner radius `r` (between 0 and 3), can be imagined straightened out and approximated as a rectangle <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   The width of this approximate rectangle is the ring's circumference: `2πr` <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   The thickness is denoted as `dr`, representing a tiny difference in radius from one ring to the next <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
*   Thus, the approximate area of one ring is `2πr * dr` <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

This approximation becomes more accurate as `dr` gets smaller, as the inner and outer circumferences of the ring become more similar in length <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

#### Visualizing the Sum of Rings

The areas of these rectangular approximations can be visualized by fitting them upright side-by-side along an axis representing the radius `r` <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. Each rectangle has a thickness of `dr` and a height of `2πr` (the circumference of the corresponding ring) <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

This setup forms a graph where the height of each rectangle touches the line representing `2πr`, which is a straight line with a slope of `2π` <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.

As `dr` becomes smaller, the sum of these rectangle areas looks increasingly like the area under the graph of `2πr` <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>. For a circle with radius 3, this area forms a triangle with a base of 3 and a height of `2π * 3` <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. The area of this triangle is `(1/2) * base * height = (1/2) * 3 * (2π * 3) = π * 3^2`, which is the correct formula for the area of a circle <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. This demonstrates how an approximate sum transitions to a precise area under a graph <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

## Generalizing to the Area Under a Graph (Integrals)

Many problems in mathematics and science can be approximated as the sum of many small quantities <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. When these quantities can be visualized as the areas of thin, side-by-side rectangles, the problem becomes equivalent to finding the area under a graph <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. This concept is fundamental to [[fundamental_concepts_of_calculus | calculus]] and is known as integration.

For example, considering the graph of `x^2`, determining the area under the curve between `x=0` and a variable `x` involves finding a function `A(x)` that represents this area <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. Such a function is called an integral of `x^2` <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.

## Derivatives as a Measure of Change

When exploring the area function `A(x)` (the integral), one might observe how a slight increase in `x` by a tiny nudge `dx` affects the area <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. This resulting change in area, `dA`, can be approximated by a rectangle with height `x^2` and width `dx` <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. As `dx` gets smaller, this approximation becomes more accurate <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

This leads to the relationship `dA ≈ x^2 * dx`, or `dA / dx ≈ x^2` <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>. The ratio `dA / dx` is known as the [[geometric_interpretation_of_derivatives | derivative]] of `A`, which technically is what this ratio approaches as `dx` becomes infinitesimally small <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. The [[Introduction to derivatives and calculus concepts | derivative]] measures how sensitive a function's output is to small changes in its input <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. There are many ways to [[Visual Intuition in Calculus – Link name: visual_intuition_in_calculus | visualize a derivative]] depending on the function and how tiny nudges are considered <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

## The Fundamental Theorem of Calculus

This relationship between areas and rates of change highlights a crucial connection: solving integral problems (finding area under a curve) is often achieved by understanding [[Introduction to derivatives and calculus concepts | derivatives]] <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. If one knows a function `A(x)` whose [[derivative of polynomial functions using geometric visualization | derivative]] is `x^2`, then `A(x)` must be the integral of `x^2` <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.

This inverse relationship, where the [[geometric_interpretation_of_derivatives | derivative]] of a function representing an area under a graph gives back the original function defining the graph, is known as the [[Fundamental concepts of calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. It shows that integrals and derivatives are inverse operations <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.

## Conclusion

This [[Introduction to calculus series | series]] aims to delve into these core ideas, detailing derivatives and integrals, always emphasizing that by "drawing the right pictures" and engaging playfully with the concepts, the formulas and rules of calculus can emerge naturally from one's own explorations <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.