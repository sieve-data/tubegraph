---
title: Derivatives and integrals
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

[[introduction_to_derivatives_and_calculus_concepts | Calculus]] is a branch of mathematics focused on understanding continuous change and accumulation. Its core ideas, particularly [[integration_and_antiderivatives | integrals]] and [[derivatives_of_simple_functions_and_their_intuition | derivatives]], aim to reveal the fundamental origins of mathematical formulas and rules, rather than simply memorizing them <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. A visual approach is often employed to clarify their meaning and derivation <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Integrals

[[integration_and_antiderivatives | Integrals]] represent a method for summing up many small quantities to find a total. They are often visualized as the area under a graph <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### The Area of a Circle: An Introduction to Integration

The concept of integration can be introduced by exploring how the formula for the area of a circle (πr²) is derived <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

1.  **Slicing the Circle:** Imagine dividing a circle into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This method respects the circle's symmetry, which is often rewarded in mathematics <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
2.  **Approximating Ring Area:** Each ring can be straightened out and approximated as a thin rectangle <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   The width of this approximate rectangle is the circumference of the original ring, which is 2πr (where 'r' is the inner radius of the ring) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   The thickness of the rectangle, representing a tiny difference in the radius, is denoted as 'dr' <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Therefore, the approximate area of one ring is 2πr * dr <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   This approximation becomes more accurate as 'dr' (the thickness of the rings) gets smaller <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
3.  **Summing the Rings:** The areas of all these approximate rectangular rings can be visualized by placing them side-by-side along an axis <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   The height of each rectangle corresponds to 2πr (the circumference) for a given 'r' <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   Plotting 2πr as a function of 'r' creates a straight line with a slope of 2π <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   The sum of the areas of these rectangles approximates the area under this graph <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   As 'dr' becomes infinitely small, the sum of the rectangular areas approaches the exact area under the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  **Result:** The area under the graph of y = 2πr (from r=0 to r=R, the circle's radius) is a triangle. Its area is (1/2) * base * height, which works out to (1/2) * R * (2πR) = πR² <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This demonstrates how finding the area under a graph can solve a seemingly complex geometric problem <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Applications of Integrals

Many problems in mathematics and science can be approximated by summing small quantities, and thus can be reframed as finding the area under a graph <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. An example is calculating the total distance a car has traveled based on its velocity at various points in time <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This involves multiplying velocity (v) by a tiny change in time (dt) to get a small bit of distance (v * dt) and then summing these small distances <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

When seeking the area under a more complex curve, like y = x², between 0 and x, the resulting function is called an [[antiderivatives_and_solving_integrals | integral]] of x² <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Derivatives

[[derivatives_of_simple_functions_and_their_intuition | Derivatives]] measure how sensitive a function's output is to small changes in its input <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>, <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### The Derivative of an Area Function

Consider a function `a(x)` that represents the area under a graph (e.g., y = x²) from a fixed starting point (0) to a variable endpoint (x) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>, <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

1.  **Tiny Nudge:** If 'x' is slightly increased by a tiny amount 'dx', the resulting change in area, 'da', can be approximated as a thin rectangle <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
2.  **Sliver Approximation:** This rectangular sliver has a height of x² (the height of the graph at 'x') and a width of 'dx' <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>, <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
3.  **Ratio of Changes:** This means that a change in `a` (da) is approximately equal to x² multiplied by the change in `x` (dx): `da ≈ x² * dx` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
4.  **Defining the Derivative:** Rearranging this, the ratio `da / dx` (the ratio of a tiny change in `a` to the tiny change in `x` that caused it) is approximately equal to x² <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This approximation improves as 'dx' gets smaller <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
    *   This ratio, `da / dx`, is called the [[transformational_view_of_derivatives | derivative]] of `a` <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. More precisely, the derivative is what this ratio approaches as `dx` becomes infinitesimally small <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
    *   This relationship holds for any function defined as the area under a graph: `da / dx` is approximately equal to the height of the original graph at that point <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## The Fundamental Theorem of Calculus

The [[relationship_between_integrals_and_derivatives | relationship between integrals and derivatives]] is formalized by the Fundamental Theorem of Calculus <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. It states that:

*   The [[derivatives_of_simple_functions_and_their_intuition | derivative]] of a function representing the area under a graph will give you back the original function that defined the graph itself <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   This theorem highlights that integrals and derivatives are inverse operations of each other <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

For example, if you know that the derivative of some mystery function `a(x)` is `x²`, you can reverse-engineer what `a(x)` must be <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>, <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This connection between the area under a curve (integration) and the rate of change of that area (differentiation) is central to calculus.