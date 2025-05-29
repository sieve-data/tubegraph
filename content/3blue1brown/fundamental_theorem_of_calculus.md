---
title: Fundamental theorem of calculus
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

The [[the_fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] ties together the two major ideas of [[understanding_antiderivatives_in_calculus | integrals]] and [[geometric_interpretation_of_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. It demonstrates that each concept is the inverse of the other <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Unveiling the Relationship Between Integrals and Derivatives

The [[introduction_to_calculus | introduction to calculus]] often involves exploring problems that can be approximated by summing many small quantities, such as calculating the area of a circle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Contemplating the area of a circle can lead to glimpses of [[understanding_antiderivatives_in_calculus | integrals]], [[geometric_interpretation_of_derivatives | derivatives]], and their inverse relationship <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Approximating Area with Integrals

One approach to finding the area of a circle is to slice it into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Each ring can be approximated as a thin rectangle with a width equal to its circumference (2πr) and a thickness (dr) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The area of such a rectangle is `2πr * dr` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. As `dr` gets smaller, this approximation becomes more accurate <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

Summing the areas of these thin rectangles can be visualized as finding the area under a graph <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. For the circle problem, plotting the rectangles with heights `2πr` and widths `dr` results in an aggregate area that looks like the area under the graph of `2πr` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>, which is a straight line <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. As `dr` approaches zero, the sum of these rectangle areas approaches the exact area under the graph <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Many problems that involve summing small quantities can be reframed as finding the area under a graph, which is the essence of [[understanding_antiderivatives_in_calculus | integration]] <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

If one seeks a function, `A(x)`, that gives the area under a curve (e.g., `x^2`) between a fixed point and a variable point `x`, this function `A(x)` is called an [[understanding_antiderivatives_in_calculus | integral]] of `x^2` <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

### Connecting Area to Derivatives

To understand the relationship between `A(x)` and the original function (`x^2` in this example), one can consider how `A(x)` changes with a tiny increase in `x` by a small nudge `dx` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The resulting change in area, `dA`, can be approximated as a thin rectangle with height `x^2` and width `dx` <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Thus, `dA` is approximately `x^2 * dx` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

Rearranging this approximation, `dA / dx` is approximately equal to `x^2` at that point <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This approximation improves as `dx` gets smaller <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This ratio `dA / dx` is known as the [[geometric_interpretation_of_derivatives | derivative]] of `A(x)` <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. More technically, the [[geometric_interpretation_of_derivatives | derivative]] is the value that this ratio approaches as `dx` becomes infinitesimally small <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

This implies that the [[geometric_interpretation_of_derivatives | derivative]] of a function `A(x)` (which represents the area under a graph) is equal to the height of the original graph at that point <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## The Inverse Relationship

The ability to look at a function whose [[geometric_interpretation_of_derivatives | derivative]] is known (e.g., `x^2`) and reverse engineer what the original function must be (the [[understanding_antiderivatives_in_calculus | integral]] `A(x)`) is a key application of [[geometric_interpretation_of_derivatives | derivatives]] in solving [[understanding_antiderivatives_in_calculus | integral]] problems <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This inverse relationship, where the [[geometric_interpretation_of_derivatives | derivative]] of a function representing an area under a graph gives back the function defining the graph itself, is precisely the [[the_fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. It illustrates how [[understanding_antiderivatives_in_calculus | integrals]] and [[geometric_interpretation_of_derivatives | derivatives]] are inverses of each other <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.